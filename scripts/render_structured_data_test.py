"""Renders snippets/structured-data.liquid and validates every JSON-LD block.

Hand-written Liquid that emits JSON fails in exactly one way: it emits JSON that
does not parse. A stray comma after the last array element, an unquoted price, a
title containing a double quote — any of them silently kills the whole block, and
Google reports nothing because there is nothing to report. The live theme cannot
be previewed from this container (the egress proxy 403s malnadproducts.in), so
this is the gate.

It renders the snippet with python-liquid against mock data shaped like the real
catalogue, then runs ``json.loads`` on each ``application/ld+json`` block and
asserts the fields that matter.

    pip install python-liquid
    python3 scripts/render_structured_data_test.py

Run from the repository root after any edit to snippets/structured-data.liquid.
Note: plain ``python3``, not ``python3 -I`` — isolated mode hides the user
site-packages where python-liquid lives.
"""

import json
import re
import sys

from liquid import Environment

SRC = "theme/snippets/structured-data.liquid"


def strip_comments(src: str) -> str:
    return re.sub(r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}", "", src, flags=re.S)


class Img(dict):
    """Stands in for a Shopify image/media drop; image_url just returns the src."""

    def __init__(self, src, media_type="image"):
        super().__init__(src=src, media_type=media_type)

    def __getitem__(self, k):
        return dict.get(self, k)


def image_url(obj, width=None, **kw):
    if isinstance(obj, dict):
        return obj.get("src", "")
    return str(obj or "")


def money_without_currency(v):
    return f"{(v or 0) / 100:.2f}"


def json_filter(value):
    """Shopify's `json` filter. The whole template's correctness rests on it."""
    if isinstance(value, dict):
        value = value.get("src", "")
    return json.dumps(value)


env = Environment()
env.add_filter("json", json_filter)
env.add_filter("image_url", image_url)
env.add_filter("money_without_currency", money_without_currency)

template = env.from_string(strip_comments(open(SRC).read()))


def variant(title, sku, price, url, available=True):
    return {"title": title, "sku": sku, "price": price, "url": url, "available": available}


MULTI = {
    "title": 'Malnad Chai - Premium Malnad Tea Powder',
    "url": "/products/malnad-chai-premium-malnad-tea-powder",
    "description": "<p>Our own tea powder, blended and packed at Horanadu.</p>",
    "vendor": "Malnad Spices",
    "type": "Tea",
    "price_min": 15000,
    "price_max": 30000,
    "media": [Img("//cdn.shopify.com/a.png"), Img("//cdn.shopify.com/b.png")],
    "variants": [
        variant("250 g", "malnad-chai-250-g", 15000, "/products/x?variant=1"),
        variant("500 g", "malnad-chai-500-g", 22000, "/products/x?variant=2"),
        variant("1 kg", "malnad-chai-1-kg", 30000, "/products/x?variant=3"),
    ],
}
MULTI["selected_or_first_available_variant"] = MULTI["variants"][0]

# A title carrying an apostrophe and a quote, because Suruchi's and Malnad's are
# real product names and a naive template breaks on them.
SINGLE = {
    "title": 'Nanjangud Suruchi\'s "Jamboo" Syrup',
    "url": "/products/nanjangud-suruchi-s-jamboo-syrup",
    "description": "<p>Jamboo syrup from Nanjangud Suruchi's, dark & fruity.</p>",
    "vendor": "Nanjangud Suruchi's",
    "type": "Syrups",
    "price_min": 20000,
    "price_max": 20000,
    "media": [Img("//cdn.shopify.com/c.png")],
    "variants": [variant("700 ml", "jamboo-700-ml", 20000, "/products/y?variant=9")],
}
SINGLE["selected_or_first_available_variant"] = SINGLE["variants"][0]

COLLECTION = {
    "title": "Whole Spices",
    "url": "/collections/whole-spices",
    "description": "<p>Pepper, cardamom, cloves &amp; cinnamon bark.</p>",
    "products_count": 17,
    "products": [
        {"title": "Black Pepper", "url": "/products/black-pepper"},
        {"title": 'Cloves (Lavanga)', "url": "/products/cloves-lavanga"},
    ],
}

BASE = {
    "request": {"origin": "https://malnadproducts.in"},
    "cart": {"currency": {"iso_code": "INR"}},
    "settings": {"logo": None},
}


def render(**over):
    ctx = dict(BASE)
    ctx.update(over)
    return template.render(**ctx)


def blocks(html):
    return re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.S
    )


def parse_all(html, label):
    found = blocks(html)
    if not found:
        sys.exit(f"FAIL [{label}]: no JSON-LD block rendered at all")
    out = []
    for i, raw in enumerate(found):
        try:
            out.append(json.loads(raw))
        except json.JSONDecodeError as e:
            lines = raw.strip().splitlines()
            near = "\n".join(lines[max(0, e.lineno - 3): e.lineno + 2])
            sys.exit(
                f"FAIL [{label}] block {i + 1}: invalid JSON at line {e.lineno} — {e.msg}\n"
                f"--- near ---\n{near}\n------------"
            )
    return out


failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


# ---- every page: Organization + WebSite -------------------------------------
home = parse_all(render(request={"origin": "https://malnadproducts.in", "page_type": "index"}), "home")
graph = home[0]["@graph"]
org = next(n for n in graph if n["@type"] == "Organization")
site = next(n for n in graph if n["@type"] == "WebSite")
check(org["name"] == "Malnad Products", "organization name wrong")
check(org["alternateName"] == "Malnad Spices", "alternateName should carry the packer name")
check(org["address"]["postalCode"] == "577181", "postcode wrong")
check(org["address"]["addressCountry"] == "IN", "country should be IN")
check(len(org["contactPoint"]) == 2, "both footer phone numbers should be published")
check("aggregateRating" not in org, "must not invent a rating")
check("{search_term_string}" in site["potentialAction"]["target"]["urlTemplate"], "search action broken")

# ---- product, multi-variant --------------------------------------------------
pm = parse_all(render(request={"origin": "https://malnadproducts.in", "page_type": "product"},
                      product=MULTI), "product/multi")
prod = next(b for b in pm if b.get("@type") == "Product")
crumb = next(b for b in pm if b.get("@type") == "BreadcrumbList")
offers = prod["offers"]
check(offers["@type"] == "AggregateOffer", "multi-variant should use AggregateOffer")
check(offers["lowPrice"] == 150.0, f"lowPrice should be 150.0, got {offers['lowPrice']}")
check(offers["highPrice"] == 300.0, f"highPrice should be 300.0, got {offers['highPrice']}")
check(offers["offerCount"] == 3, "offerCount wrong")
check(offers["priceCurrency"] == "INR", "currency should be INR")
check(len(offers["offers"]) == 3, "should emit one Offer per pack size")
check(offers["offers"][1]["price"] == 220.0, f"500 g should be 220.0, got {offers['offers'][1]['price']}")
check(all(isinstance(o["price"], (int, float)) for o in offers["offers"]), "price must be a JSON number")
check(prod["brand"]["name"] == "Malnad Spices", "brand should come from vendor")
check(len(prod["image"]) == 2, "should emit every product image")
check("<p>" not in prod["description"], "description must be stripped of HTML")
check("aggregateRating" not in prod and "review" not in prod, "must not invent reviews")
check("hasMerchantReturnPolicy" not in prod, "must not assert a returns policy")
check(len(crumb["itemListElement"]) == 2, "breadcrumb without a collection should be 2 deep")

# ---- product, single variant, with quotes and an apostrophe in the title ------
ps = parse_all(render(request={"origin": "https://malnadproducts.in", "page_type": "product"},
                      product=SINGLE), "product/single")
prod1 = next(b for b in ps if b.get("@type") == "Product")
check(prod1["offers"]["@type"] == "Offer", "single-variant should use a plain Offer")
check(prod1["offers"]["price"] == 200.0, f"price should be 200.0, got {prod1['offers']['price']}")
check('"Jamboo"' in prod1["name"], "quotes in the title should survive escaping")
check("Suruchi's" in prod1["name"], "apostrophe in the title should survive")

# ---- product inside a collection: 3-deep breadcrumb ---------------------------
pc = parse_all(render(request={"origin": "https://malnadproducts.in", "page_type": "product"},
                      product=MULTI, collection=COLLECTION), "product/in-collection")
crumb3 = next(b for b in pc if b.get("@type") == "BreadcrumbList")
check(len(crumb3["itemListElement"]) == 3, "breadcrumb inside a collection should be 3 deep")
check(crumb3["itemListElement"][1]["name"] == "Whole Spices", "middle crumb should be the collection")

# ---- collection page ----------------------------------------------------------
cl = parse_all(render(request={"origin": "https://malnadproducts.in", "page_type": "collection"},
                      collection=COLLECTION), "collection")
coll = next(b for b in cl if b.get("@type") == "CollectionPage")
check(coll["mainEntity"]["numberOfItems"] == 17, "numberOfItems should be the real count")
check(len(coll["mainEntity"]["itemListElement"]) == 2, "should list the products it has")
check("&amp;" not in coll["description"], "collection description should be unescaped text")

# ---- page ---------------------------------------------------------------------
pg = parse_all(render(request={"origin": "https://malnadproducts.in", "page_type": "page"},
                      page={"title": "About us", "url": "/pages/about"}), "page")
check(any(b.get("@type") == "WebPage" for b in pg), "page should emit WebPage")

if failures:
    print("FAILED:")
    for f in failures:
        print("  -", f)
    sys.exit(1)

print("structured data renders and every JSON-LD block parses")
print(f"  home        : {len(home)} block(s)")
print(f"  product x3  : {len(pm)} block(s)  AggregateOffer 150.0-300.0 INR, 3 offers")
print(f"  product x1  : {len(ps)} block(s)  Offer 200.0 INR, quotes survived")
print(f"  collection  : {len(cl)} block(s)  ItemList of 17")
print(f"  page        : {len(pg)} block(s)")
