"""Renders the declarations block against mock catalogue data.

The block cannot be exercised on the store yet - every product is DRAFT - so
this is the gate that catches a Liquid error before it reaches a product page.
It renders with python-liquid, stubbing the Shopify-only filters and snippets,
and checks the cases that matter: a pack missing a declaration, a complete
pack, a part-known consumer care line, and the three shapes a price takes.

    pip install python-liquid
    python3 scripts/render_declarations_test.py

Run from the repository root, after any edit to blocks/compliance-declarations.liquid
or snippets/compliance-row.liquid.
"""
import re
from liquid import Environment
from liquid import DictLoader

def strip_shopify_blocks(src):
    for tag in ("schema", "stylesheet", "javascript", "doc"):
        src = re.sub(r"\{%-?\s*" + tag + r"\s*-?%\}.*?\{%-?\s*end" + tag + r"\s*-?%\}",
                     "", src, flags=re.S)
    return src

block = strip_shopify_blocks(open("theme/blocks/compliance-declarations.liquid").read())
row   = strip_shopify_blocks(open("theme/snippets/compliance-row.liquid").read())

env = Environment(loader=DictLoader({
    "compliance-row": row,
    "text-block-styles": "",
    "spacing-style": "padding-block-start: 8px;",
}))

# Shopify-only filters python-liquid does not ship.
env.add_filter("asset_url", lambda s: "//cdn.shopify.com/s/files/1/0/t/assets/" + str(s))
env.add_filter("t", lambda s, **kw: str(s))
env.add_filter("money", lambda s: "Rs. " + str(s))

def mf(**kw):
    return {k: {"value": v} for k, v in kw.items()}

# Malnad Chai: three packs. The 1 kg prints no MRP and no best-before - the
# real case from the catalogue, and the one the gap treatment exists for.
variants = [
    {"id": 101, "metafields": {"compliance": mf(net_quantity="250 g", mrp=150.0,
        mfg_date="SEP 2025", best_before="SEP 2026")}},
    {"id": 102, "metafields": {"compliance": mf(net_quantity="500 g", mrp=220.0,
        mfg_date="SEP 2025", best_before="SEP 2026")}},
    {"id": 103, "metafields": {"compliance": mf(net_quantity="1 kg", mrp="",
        mfg_date="SEP 2025", best_before="")}},
]
product = {
    "id": 900, "title": "Malnad Chai", "variants": variants,
    "selected_or_first_available_variant": variants[1],
    "metafields": {"compliance": mf(
        packer_name="Malnad Spices",
        packer_address="Devaramane, Horanadu Post, Kalasa Tq,\nChikkamagaluru Dist - 577181, Karnataka, India",
        country_of_origin="India", care_name="Malnad Spices",
        care_phone="8431218956, 9480956035", care_email="drjhrnd5@gmail.com",
        fssai_licence="21223055000121", hsn_code="0902", gst_rate=5.0,
        ingredients="", storage="Store in a cool, dry place.",
        estate="", altitude_ft="", harvest_month="", roast_level="")},
}
settings = {"heading": "Declarations", "heading_preset": "h6",
    "intro": "Printed on the pack you receive.",
    "gap_notice": "Not printed on this pack.",
    "gap_footnote": "Where a declaration is not printed on the pack we leave it blank.",
    "gap_color": "#9C4A28", "rule_color": "#DCE0D8",
    "show_origin_notes": True, "show_trade": True}

out = env.from_string(block).render(
    closest={"product": product},
    block={"settings": settings, "shopify_attributes": "", "id": "b1"},
    section={"id": "s1"})

print(re.sub(r"\n{3,}", "\n\n", out).strip())

# --- edge cases -------------------------------------------------------------
print("\n" + "=" * 60)

def render(prod, sett=None):
    s = dict(settings); s.update(sett or {})
    return env.from_string(block).render(closest={"product": prod},
        block={"settings": s, "shopify_attributes": "", "id": "b1"}, section={"id": "s1"})

# 1. Single variant, every declaration present -> no gap notices at all.
v = [{"id": 1, "metafields": {"compliance": mf(net_quantity="500 ml", mrp=200.0,
      mfg_date="AUG 2025", best_before="AUG 2026")}}]
full = dict(product, variants=v, selected_or_first_available_variant=v[0])
full["metafields"] = {"compliance": dict(product["metafields"]["compliance"],
      **mf(ingredients="Coconut"))}
out1 = render(full)
print("complete product, gap notices:", out1.count("decl__value--gap"), "(want 0)")
print("packs rendered:", out1.count("decl__pack"), "| hidden:", out1.count(" hidden"))

# 2. Only the care email known -> no dangling separator.
sparse = dict(full)
sparse["metafields"] = {"compliance": mf(care_email="drjhrnd5@gmail.com",
    packer_name="", packer_address="", country_of_origin="", care_name="",
    care_phone="", fssai_licence="", hsn_code="", gst_rate="", ingredients="",
    storage="", estate="", altitude_ft="", harvest_month="", roast_level="")}
out2 = render(sparse)
care = [l for l in out2.splitlines() if "Consumer care" in l][0]
print("care row:", care.split("<dd")[1][:80])
print("leading separator bug:", "\">·" in out2 or "> ·" in out2)

# 3. Trade row off by default.
print("trade hidden when show_trade false:", "HSN and GST" not in render(full, {"show_trade": False}))

# 4. Non-integer MRP keeps its paise.
v2 = [{"id": 9, "metafields": {"compliance": mf(net_quantity="1 kg", mrp=249.5,
      mfg_date="", best_before="")}}]
out4 = render(dict(full, variants=v2, selected_or_first_available_variant=v2[0]))
print("decimal MRP:", [l for l in out4.splitlines() if "Maximum retail" in l][0].split("<dd")[1][:60])

print()
for amt, want in [(150.0, '₹150'), (249.5, '₹249.50'), (249.05, '₹249.05'), (110, '₹110')]:
    vv = [{"id": 9, "metafields": {"compliance": mf(net_quantity="1 kg", mrp=amt, mfg_date="", best_before="")}}]
    o = render(dict(full, variants=vv, selected_or_first_available_variant=vv[0]))
    got = [l for l in o.splitlines() if "Maximum retail" in l][0].split('decl__value">')[1].split(' ·')[0]
    print("%-8s -> %-10s %s" % (amt, got, "OK" if got == want else "MISMATCH want " + want))
