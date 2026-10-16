#!/usr/bin/env python3
"""Alt text for all 70 pack photographs — source of truth, re-pushable.

Same pattern as ``descriptions.py`` and ``seo.py``: the text lives here, in git,
not only in Shopify. ``check()`` fails the push rather than letting a bad record
through.

Why this file exists: an audit on 16 October 2026 found **64 of 70 images with an
empty alt attribute**, and the 6 that had one simply repeated the product title
verbatim — which is weak alt text, because it duplicates the H1 and describes
nothing. Alt text matters here more than on a typical store: Google Images is a
real entry point for "marati moggu", "sikakai powder" and the other local names
nobody else competes for, and alt text is one of the few signals an answer engine
has about what a pack photograph actually shows.

**What this file may and may not say.** The photographs have not been looked at
from here. So every line is built only from what the store record states — the
product, the maker, the pack size on the variant, and the origin already
published in the listing. **No line describes a visual detail that has not been
verified**: no colours, no textures, no "close-up of", no count of objects in
frame. That is the same rule as the pack declarations — nothing is invented.

Where a product has exactly as many photographs as pack sizes, the photographs
are paired to the sizes in order, which is how the import created them. Where it
has more photographs than sizes, the extras get a line that names the product and
its origin but **asserts no size**, because which pack is in which frame is not
something the record settles.

The pack size is joined with a dash rather than "in its 150 g pack" so the line
reads correctly for a plural head noun — "Whole soapnuts in its 150 g pack" does
not.
"""

from __future__ import annotations

import re

MAX_LEN = 125

# Product handle -> short descriptor used after the name. Kept separate from the
# titles so a wording change is one edit here, not 70 scattered strings.
ORIGIN = {
    # Malnad Spices' own packs, weighed and packed at Horanadu
    "own": "from Malnad Products, Horanadu",
    # Goods resold under the maker's own label
    "sanjivni": "from Nagashree Coffee Works, Kalasa",
    "qtf": "from the Guard-Hitlow Tea Factory, Koppa",
    "shree-durga": "from Shree Durga Industries",
    "aaradhya": "double filtered",
    "kalpatharu": "from Ganesh Flour and Oil Mill",
    "nisarga": "from Malnad's Nisarga",
    "suruchi": "from Nanjangud Suruchi's",
    "hallimane": "from Hallimane",
    "hayat": "from Pahul Agro",
    "karthik": "from Karthik Traders",
    "annapoorneshwari": "from Annapoorneshwari, Kalasa",
}

# handle -> (display name used in alt, origin key)
# Display name is NOT the SEO title and NOT always the product title: it is what
# the thing is, in the words a customer would search.
PRODUCTS: dict[str, tuple[str, str]] = {
    "malnad-chai-premium-malnad-tea-powder": ("Malnad Chai tea powder", "own"),
    "ghani-pressed-copra-coconut-oil": ("Ghani-pressed copra coconut oil", "shree-durga"),
    "swad-instant-coffee": ("Swad instant coffee powder", "own"),
    "swad-malnad-premium-coffee-powder-filter": ("Swad Malnad filter coffee powder", "own"),
    "swad-malnad-premium-coffee-powder-nice": ("Swad Malnad nice coffee powder", "own"),
    "sanjivni-special-tea": ("Sanjivni special tea powder", "sanjivni"),
    "qtf-tea-guard-hitlow-tea-factory": ("QTF estate tea", "qtf"),
    "black-pepper": ("Malnad black pepper, whole", "own"),
    "cloves-lavanga": ("Whole cloves, lavanga", "own"),
    "green-cardamom": ("Green cardamom pods, elakki", "own"),
    "black-cardamom": ("Black cardamom pods", "own"),
    "nutmeg": ("Whole nutmeg, jaikai", "own"),
    "jathipathri-mace": ("Jathipathri, mace", "own"),
    "chekke-cinnamon-bark": ("Chekke, cinnamon bark", "own"),
    "star-anise": ("Whole star anise", "own"),
    "fennel-seed": ("Fennel seed, sompu", "own"),
    "shahi-jeera": ("Shahi jeera, black caraway", "own"),
    "kasturi-menthi": ("Kasturi menthi, dried fenugreek leaves", "own"),
    "marati-moggu": ("Marati moggu, kapok buds", "own"),
    "naga-kesari-moggu": ("Naga kesari moggu, a Malnad spice", "own"),
    "kalhoo": ("Kalhoo, a Malnad spice", "own"),
    "mintiya": ("Mintiya, a Malnad spice", "own"),
    "palavele": ("Palavele, a Malnad spice", "own"),
    "sasive-mustard-seed": ("Sasive, mustard seed", "own"),
    "swad-horanadu-bisibele-bath-powder": ("Swad Horanadu bisibele bath powder", "own"),
    "swad-horanadu-garam-masala-powder": ("Swad Horanadu garam masala powder", "own"),
    "swad-horanadu-palav-powder": ("Swad Horanadu palav powder", "own"),
    "swad-horanadu-puliyogare-powder": ("Swad Horanadu puliyogare powder", "own"),
    "swad-horanadu-rasam-powder": ("Swad Horanadu rasam powder", "own"),
    "swad-horanadu-sambar-powder": ("Swad Horanadu sambar powder", "own"),
    "horanadu-nellikai-powder": ("Nellikai powder, dried amla", "annapoorneshwari"),
    "chia-seeds": ("Chia seeds", "own"),
    "sabja-seeds": ("Sabja seeds, basil seed", "own"),
    "flax-seeds": ("Flax seeds, whole", "own"),
    "magaz-seeds": ("Magaz seeds, melon kernels", "own"),
    "pumpkin-seeds": ("Pumpkin seed kernels", "own"),
    "sunflower-seeds": ("Sunflower seed kernels", "own"),
    "badam-almonds": ("Badam, whole almonds", "own"),
    "pista-pistachios": ("Pista, pistachios in the shell", "own"),
    "hayat-organic-raisins-dry-grapes": ("Hayat raisins, kishmish", "hayat"),
    "dates": ("Dates, khajur", "own"),
    "special-dates": ("Special grade dates", "own"),
    "mixed-dry-fruits-gift-pack": ("Mixed dry fruits and nuts", "karthik"),
    "nisarga-amla-health-drink": ("Nisarga amla concentrate", "nisarga"),
    "malnad-s-nisarga-banana-stem-squash": ("Banana stem squash", "nisarga"),
    "malnad-s-nisarga-jamun-squash": ("Jamun squash", "nisarga"),
    "nanjangud-suruchi-s-ginger-lime-syrup": ("Ginger lime syrup", "suruchi"),
    "nanjangud-suruchi-s-grapes-syrup": ("Grapes syrup", "suruchi"),
    "nanjangud-suruchi-s-jamboo-syrup": ("Jamboo syrup", "suruchi"),
    "nanjangud-suruchi-s-sugarless-jamboo-syrup": ("Sugarless jamboo syrup", "suruchi"),
    "hallimane-kokam-syrup": ("Kokam syrup", "hallimane"),
    "nanjangud-suruchi-s-diabeat": ("Diabeat herbal decoction", "suruchi"),
    "aaradhya-pure-double-filtered-coconut-oil": ("Aaradhya pure coconut oil", "aaradhya"),
    "kalpatharu-special-double-filtered-pure-coconut-oil": ("Kalpatharu pure coconut oil", "kalpatharu"),
    "antuvala-soapnut-powder": ("Antuvala soapnut powder", "annapoorneshwari"),
    "sikakai-shikakai-powder": ("Sikakai, shikakai powder", "annapoorneshwari"),
    "soapnut-whole": ("Whole soapnuts, antuvala", "own"),
}

# Any claim about a health effect is barred, exactly as in descriptions.py and
# seo.py. "Diabeat" is the maker's product name, not a claim we make.
BANNED = re.compile(
    r"\b(immun\w*|cholesterol|antioxidant\w*|detox\w*|cure\w*|heal(s|ing)?|"
    r"diabet\w*|weight[- ]loss|remedy|therapeutic|medicinal)\b",
    re.I,
)
# Phrases that waste the attribute. A screen reader already says "image".
FILLER = re.compile(r"\b(image of|picture of|photo of|photograph of|graphic of)\b", re.I)


def _container(handle: str, size: str) -> str:
    """What the goods are actually in, per the published product description.

    Not a guess: the syrups and squashes are described as bottles and Kalpatharu
    as "sold in the large tin" in ``descriptions.py``. Calling a 700 ml bottle a
    "pack" is not wrong, but it is vaguer than the record allows.
    """
    if handle.startswith("kalpatharu"):
        return "tin"
    if handle == "mixed-dry-fruits-gift-pack":
        return "gift pack"
    if re.search(r"\b(ml|l)$", size.strip()):
        return "bottle"
    return "pack"


def alt_for(handle: str, pack_sizes: list[str], image_count: int) -> list[str]:
    """Return one alt string per image, in media order.

    Pairs photographs to pack sizes when the counts match. When there are more
    photographs than sizes, the extras name the product without asserting a size.
    """
    if handle not in PRODUCTS:
        raise KeyError(f"{handle} is not in PRODUCTS — add it before pushing")
    name, origin_key = PRODUCTS[handle]
    origin = ORIGIN[origin_key]

    out: list[str] = []
    for i in range(image_count):
        if image_count == len(pack_sizes):
            out.append(f"{name} \u2014 {pack_sizes[i]} {_container(handle, pack_sizes[i])}, {origin}")
        elif i < len(pack_sizes) and len(pack_sizes) > 1:
            out.append(f"{name} \u2014 {pack_sizes[i]} {_container(handle, pack_sizes[i])}, {origin}")
        elif len(pack_sizes) == 1 and i == 0:
            out.append(f"{name} \u2014 {pack_sizes[0]} {_container(handle, pack_sizes[0])}, {origin}")
        else:
            # More frames than the record can account for: no size claim.
            out.append(f"{name} {origin}")
    return out


def check(records: list[tuple[str, str]]) -> None:
    """Fail loudly rather than push a bad record. records = [(media_id, alt)]."""
    problems: list[str] = []
    for mid, alt in records:
        if not alt or not alt.strip():
            problems.append(f"{mid}: empty")
        if len(alt) > MAX_LEN:
            problems.append(f"{mid}: {len(alt)} chars, over {MAX_LEN} — {alt!r}")
        if BANNED.search(alt):
            problems.append(f"{mid}: health claim — {alt!r}")
        if FILLER.search(alt):
            problems.append(f"{mid}: filler phrase — {alt!r}")
        if alt.strip().endswith(","):
            problems.append(f"{mid}: trailing comma — {alt!r}")
    if problems:
        raise SystemExit("alt text check FAILED:\n  " + "\n  ".join(problems))
    print(f"alt text check passed: {len(records)} records")


if __name__ == "__main__":
    print(f"{len(PRODUCTS)} products defined")
