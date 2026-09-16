"""Generates the Shopify weight-based shipping rates from a small rate card.

The courier prices by distance and by weight, which Shopify expresses as
zones x weight brackets. That is 28 rates, which nobody wants to type or keep
in step by hand. So the whole table is generated from **eight numbers** - a
base and a per-kilo figure for each of four zones - and this script prints the
GraphQL variables to push.

Rates are charged at the TOP of each bracket. A 1.2 kg parcel pays the 2 kg
price. That is deliberate: under-recovering postage costs real money on every
single order, and the error is invisible until the month's accounts.

    python3 scripts/build_shipping_rates.py            # show the table
    python3 scripts/build_shipping_rates.py --json     # emit GraphQL variables
"""

import json
import sys

# --- the eight numbers -------------------------------------------------------
# PROVISIONAL. These are a sensible shape for a small-town courier, not quoted
# tariffs. Replace both columns per zone from the real rate card and re-run.
RATE_CARD = {
    "karnataka": {"base": 40, "per_kg": 30},
    "south_west": {"base": 60, "per_kg": 40},
    "rest": {"base": 80, "per_kg": 50},
    "remote": {"base": 110, "per_kg": 70},
}

# Province codes are Shopify's own, not ISO 3166-2:IN, and four of them differ.
# Probed against the API rather than assumed, because Shopify accepts a zone
# containing a bad code, drops that province, and reports no error at all:
#   Chhattisgarh CG (not CT) - Telangana TS (not TG) - Uttarakhand UK (not UT)
#   Dadra and Nagar Haveli DN and Daman and Diu DD, still listed separately
# --- zones -------------------------------------------------------------------
# Shopify zones are province lists, not distances, so the distance bands the
# courier actually prices on are approximated by grouping states.
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

# --- weight brackets, in kg --------------------------------------------------
# Finer at the low end because almost every order here lands between 200 g and
# 3 kg: a 140 g packet of pepper up to a 1.97 kg tin of coconut oil.
BRACKETS = [(0, 0.5), (0.5, 1), (1, 2), (2, 3), (3, 5), (5, 10), (10, 20)]


def rate_for(zone_key, upper_kg):
    """Price at the top of the bracket, rounded up to the nearest 5 rupees."""
    card = RATE_CARD[zone_key]
    billable = max(0.0, upper_kg - 0.5)
    raw = card["base"] + card["per_kg"] * billable
    return int(-(-raw // 5) * 5)


def zones_to_create():
    out = []
    for key, name, provinces in ZONES:
        methods = []
        for lo, hi in BRACKETS:
            methods.append({
                "name": "Standard delivery",
                "active": True,
                "rateDefinition": {
                    "price": {"amount": str(rate_for(key, hi)), "currencyCode": "INR"}
                },
                "weightConditionsToCreate": [
                    {"criteria": {"value": lo, "unit": "KILOGRAMS"},
                     "operator": "GREATER_THAN_OR_EQUAL_TO"},
                    {"criteria": {"value": hi, "unit": "KILOGRAMS"},
                     "operator": "LESS_THAN_OR_EQUAL_TO"},
                ],
            })
        out.append({
            "name": name,
            "countries": [{"code": "IN",
                           "provinces": [{"code": p} for p in provinces]}],
            "methodDefinitionsToCreate": methods,
        })
    return out


def main():
    if "--json" in sys.argv:
        print(json.dumps(zones_to_create(), indent=2))
        return

    head = "kg bracket".ljust(14) + "".join(n.rjust(24) for _, n, _ in ZONES)
    print(head)
    print("-" * len(head))
    for lo, hi in BRACKETS:
        label = f"{lo:g} - {hi:g}".ljust(14)
        row = "".join(f"Rs {rate_for(k, hi)}".rjust(24) for k, _, _ in ZONES)
        print(label + row)
    print()
    print("Provinces covered:", sum(len(p) for _, _, p in ZONES), "of 36 states and UTs")
    print("Rates generated  :", len(ZONES) * len(BRACKETS))


if __name__ == "__main__":
    main()
