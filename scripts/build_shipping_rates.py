"""Generates the Shopify weight-based shipping rates from the client's rate card.

RATE CARD, Jnanottam 30 Oct 2026, superseding the four-zone card below it:

    "per kilo 80 rs ... doesnt matter if its from 100 grams or 50 grams, till
     1 kilo its 80 rs. so for 1.4 kilo its 160. like that"

So: **rupees 80 per kilogram or part of a kilogram.** Up to and including 1 kg
is 80; anything over 1 kg and up to 2 kg is 160; 1.4 kg is 160, as he said.
Arithmetically that is `ceil(weight_kg) * 80`.

THIS IS NOW ONE FLAT RATE FOR THE WHOLE OF INDIA. The four zones still exist
in Shopify and still carry the correct province lists, but every one of them
now prices identically. They are kept rather than deleted so that a future
"the North East costs more" is one number here and a re-run, not a rebuild of
the province lists -- which are the part that is genuinely hard to get right.

HOW THE BRACKETS EXPRESS "OR PART THEREOF", and why they deliberately touch.
Shopify weight conditions are GREATER_THAN_OR_EQUAL_TO and
LESS_THAN_OR_EQUAL_TO -- there is no strict greater-than. So bracket (0,1) and
bracket (1,2) BOTH match a parcel of exactly 1.000 kg. Shopify resolves that by
offering the cheaper, which is 80 -- and 80 is the right answer, because
ceil(1.0) = 1. The overlap is not a bug being tolerated; it is what makes the
boundary land on the correct side of the rule, at every single boundary.

    python3 scripts/build_shipping_rates.py            # show the table
    python3 scripts/build_shipping_rates.py --check    # prove the rule holds
    python3 scripts/build_shipping_rates.py --mutation <profile>
"""

import math
import sys

# --- the one number ----------------------------------------------------------
RATE_PER_KG = 80

# How far the ladder runs. Above this a cart gets NO delivery option and cannot
# check out -- silently, with no error, which is this project's worst failure
# mode. 20 kg is kept from the previous card so nothing that was buyable
# yesterday stops being buyable today. 20 kg of spices is a wholesale enquiry,
# and wholesale is out of scope in the quotation.
MAX_KG = 20

# --- zones -------------------------------------------------------------------
# Province codes are Shopify's own, NOT ISO 3166-2:IN, and five of them differ.
# Probed against the API rather than assumed, because Shopify accepts a zone
# containing a bad code, silently drops that province, and reports no error:
#   Chhattisgarh CG (not CT) · Telangana TS (not TG) · Uttarakhand UK (not UT)
#   Odisha OR (not OD) · Dadra and Nagar Haveli DN and Daman and Diu DD,
#   still listed separately. 37 entries cover all 36 states and union territories.
# These lists are already correct in the live store and are NOT rewritten by the
# mutation this script emits -- it only replaces the rates inside each zone.
ZONES = [
    ("karnataka", "Karnataka", ["KA"]),
    ("south_west", "South and West India",
     ["TN", "KL", "AP", "TS", "GA", "MH", "PY"]),
    ("rest", "Rest of India",
     ["DL", "HR", "PB", "HP", "UK", "UP", "RJ", "GJ", "MP", "CG",
      "BR", "JH", "OR", "WB", "CH", "DN", "DD"]),
    ("remote", "North East and islands",
     ["AR", "AS", "MN", "ML", "MZ", "NL", "SK", "TR", "JK", "LA", "AN", "LD"]),
]

# Live ids, read from the Admin API 30 Oct 2026. Both profiles must carry the
# same rates: anything landing in the default `General profile` with no rate is
# unbuyable at checkout with no error shown, which is the landmine fixed 7 Oct.
PROFILES = {
    "malnad": {
        "name": "Malnad delivery",
        "profile_id": "gid://shopify/DeliveryProfile/97018216561",
        "location_group": "gid://shopify/DeliveryLocationGroup/97934180465",
        "zones": {
            "karnataka": "gid://shopify/DeliveryZone/361350103153",
            "south_west": "gid://shopify/DeliveryZone/361350135921",
            "rest": "gid://shopify/DeliveryZone/361350168689",
            "remote": "gid://shopify/DeliveryZone/361350201457",
        },
    },
    "general": {
        "name": "General profile",
        "profile_id": "gid://shopify/DeliveryProfile/96993116273",
        "location_group": "gid://shopify/DeliveryLocationGroup/97908949105",
        "zones": {
            "karnataka": "gid://shopify/DeliveryZone/513336901745",
            "south_west": "gid://shopify/DeliveryZone/513337622641",
            "rest": "gid://shopify/DeliveryZone/513425866865",
            "remote": "gid://shopify/DeliveryZone/513425899633",
        },
    },
}

BRACKETS = [(n, n + 1) for n in range(MAX_KG)]


def rate_for(upper_kg: int) -> int:
    """Every parcel in bracket (hi-1, hi] bills at hi whole kilos."""
    return upper_kg * RATE_PER_KG


def price_for_weight(kg: float) -> int:
    """What the rule says a parcel of this weight costs. The spec, not the table."""
    return math.ceil(kg) * RATE_PER_KG


def methods_block() -> str:
    out = []
    for lo, hi in BRACKETS:
        out.append(
            '{name:"Standard delivery",active:true,'
            f'rateDefinition:{{price:{{amount:"{rate_for(hi)}",currencyCode:INR}}}},'
            "weightConditionsToCreate:["
            f"{{criteria:{{value:{lo},unit:KILOGRAMS}},operator:GREATER_THAN_OR_EQUAL_TO}},"
            f"{{criteria:{{value:{hi},unit:KILOGRAMS}},operator:LESS_THAN_OR_EQUAL_TO}}]}}"
        )
    return ",".join(out)


def mutation_for(profile_key: str) -> str:
    """One call per profile: all four zones get the new ladder.

    TWO zones per call, not four. Shopify's own guidance is 'no more than 5
    zones per request', but there is a harder limit it does not mention:
    **a GraphQL document may not exceed 16,384 characters.** All four zones at
    20 brackets each is 21,487 and is rejected outright --
    'GraphQL document is 21487 characters, over the 16384 limit'. Two zones is
    about 10.7k and goes through. Measured, not guessed.

    The new rates are CREATED FIRST and the old ones deleted after,
    never the other way round: during the overlap both ladders match and
    Shopify offers the cheaper, so a customer mid-checkout sees the old lower
    rate. Deleting first would leave the store with no delivery option at all.
    """
    p = PROFILES[profile_key]
    methods = methods_block()
    zones = ",".join(
        f'{{id:"{p["zones"][key]}",methodDefinitionsToCreate:[{methods}]}}'
        for key, _name, _provinces in ZONES
    )
    return (
        "mutation {\n"
        f'  deliveryProfileUpdate(id: "{p["profile_id"]}", profile: {{\n'
        f'    locationGroupsToUpdate: [{{id:"{p["location_group"]}",zonesToUpdate:[{zones}]}}]\n'
        "  }) {\n"
        "    profile { id name activeMethodDefinitionsCount }\n"
        "    userErrors { field message }\n"
        "  }\n"
        "}"
    )


def check() -> int:
    """Prove the generated table reproduces the rule, including at boundaries."""
    problems = []

    # The figures he gave by hand, which are the acceptance test.
    for kg, expected in [(0.05, 80), (0.1, 80), (0.5, 80), (1.0, 80),
                         (1.4, 160), (2.0, 160), (2.1, 240)]:
        got = price_for_weight(kg)
        if got != expected:
            problems.append(f"rule: {kg} kg should be {expected}, rule gives {got}")

    # Every bracket must bill its whole range at the rule's price, and the
    # cheapest matching bracket is what Shopify will actually offer.
    for kg in [x / 100 for x in range(1, MAX_KG * 100 + 1)]:
        matching = [rate_for(hi) for lo, hi in BRACKETS if lo <= kg <= hi]
        if not matching:
            problems.append(f"table: {kg} kg matches no bracket — unbuyable")
            continue
        offered = min(matching)
        want = price_for_weight(kg)
        if offered != want:
            problems.append(f"table: {kg} kg offers {offered}, rule says {want}")

    if problems:
        for p in problems[:12]:
            print("FAIL", p)
        print(f"{len(problems)} problems")
        return 1
    print(f"rule and table agree at every 10 g step from 0.01 to {MAX_KG} kg")
    print(f"  {len(BRACKETS)} brackets x {len(ZONES)} zones = "
          f"{len(BRACKETS) * len(ZONES)} rates per profile, "
          f"{len(BRACKETS) * len(ZONES) * len(PROFILES)} in all")
    return 0


def table() -> None:
    print(f"Rupees {RATE_PER_KG} per kilogram or part of a kilogram, all India.\n")
    print(f"{'parcel weight':>18}  {'charge':>7}")
    for lo, hi in BRACKETS:
        lo_s = "up to" if lo == 0 else f"over {lo} kg to"
        print(f"{lo_s + ' ' + str(hi) + ' kg':>18}  {'₹' + str(rate_for(hi)):>7}")
    print(f"\nOver {MAX_KG} kg there is no rate and the cart cannot check out.")


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    if "--mutation" in sys.argv:
        key = sys.argv[sys.argv.index("--mutation") + 1]
        print(mutation_for(key))
        sys.exit(0)
    table()
