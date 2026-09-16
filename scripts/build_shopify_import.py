#!/usr/bin/env python3
"""Turn a validated catalogue sheet into a Shopify product import CSV.

Everything is written as Status: draft. Nothing reaches the storefront until a
human publishes it, and validate_catalogue.py must pass first.

    python3 scripts/build_shopify_import.py fixtures/catalogue-filled-sample.csv build/shopify-import.csv
"""
import csv, sys, re, os
from collections import OrderedDict

NS = "compliance"

# key -> (source column, Shopify metafield type)
PRODUCT_MF = OrderedDict([
    ("packer_name",        ("Manufacturer or Packer Name",         "single_line_text_field")),
    ("packer_address",     ("Manufacturer or Packer Full Address", "multi_line_text_field")),
    ("country_of_origin",  ("Country of Origin",                   "single_line_text_field")),
    ("care_name",          ("Consumer Care Name",                  "single_line_text_field")),
    ("care_phone",         ("Consumer Care Phone",                 "single_line_text_field")),
    ("care_email",         ("Consumer Care Email",                 "single_line_text_field")),
    ("fssai_licence",      ("FSSAI Licence Number",                "single_line_text_field")),
    ("hsn_code",           ("HSN Code",                            "single_line_text_field")),
    ("gst_rate",           ("GST Rate (%)",                        "number_decimal")),
    ("ingredients",        ("Ingredients",                         "multi_line_text_field")),
    ("storage",            ("Storage Instructions",                "multi_line_text_field")),
    ("estate",             ("Estate / Origin",                     "single_line_text_field")),
    ("altitude_ft",        ("Altitude (ft)",                       "number_integer")),
    ("harvest_month",      ("Harvest Month",                       "single_line_text_field")),
    ("roast_level",        ("Roast Level",                         "single_line_text_field")),
])
# these genuinely differ between a 250 g and a 1 kg pack, so they live on the variant
VARIANT_MF = OrderedDict([
    ("net_quantity", ("Net Quantity",                   "single_line_text_field")),
    ("mrp",          ("MRP (INR incl. all taxes)",      "number_decimal")),
    ("mfg_date",     ("Date of Manufacture or Packing", "single_line_text_field")),
    ("best_before",  ("Best Before / Use By",           "single_line_text_field")),
])

BASE = ["Handle","Title","Body (HTML)","Vendor","Product Category","Type","Tags","Published",
        "Option1 Name","Option1 Value","Option2 Name","Option2 Value",
        "Variant SKU","Variant Grams","Variant Weight Unit","Variant Inventory Tracker",
        "Variant Inventory Qty","Variant Inventory Policy","Variant Fulfillment Service",
        "Variant Price","Variant Compare At Price","Variant Requires Shipping","Variant Taxable",
        "Image Src","Image Position","Image Alt Text","Variant Image",
        "SEO Title","SEO Description","Status"]


def handle(name):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", name.lower())).strip("-")


def num(v):
    s = str(v or "").replace(",", "").replace("₹", "").strip()
    return s if s else ""


def main(src, out):
    with open(src, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))

    cols = (BASE
            + [f"product.metafields.{NS}.{k}" for k in PRODUCT_MF]
            + [f"variant.metafields.{NS}.{k}" for k in VARIANT_MF])

    groups = OrderedDict()
    for r in rows:
        groups.setdefault((r.get("Product Name") or "").strip(), []).append(r)

    out_rows, images_needed = [], []
    for name, variants in groups.items():
        h = handle(name)
        has_grind = any((v.get("Grind / Form") or "").strip() for v in variants)
        product_images = []   # every distinct image across this product's variants
        for idx, v in enumerate(variants):
            first = idx == 0
            row = {c: "" for c in cols}
            row["Handle"] = h
            row["Option1 Name"] = "Pack Size" if first else ""
            row["Option1 Value"] = (v.get("Pack Size") or "").strip()
            if has_grind:
                row["Option2 Name"] = "Grind" if first else ""
                row["Option2 Value"] = (v.get("Grind / Form") or "").strip()
            row["Variant SKU"] = (v.get("SKU") or "").strip()
            row["Variant Grams"] = num(v.get("Shipping Weight (g)"))
            row["Variant Weight Unit"] = "g"
            # Client instruction: he does not hold counted stock — everything is
            # packed to order. So inventory tracking is OFF and the variant stays
            # buyable regardless of quantity. An empty tracker column is how
            # Shopify's importer expresses "don't track this variant"; "continue"
            # is belt-and-braces so a later switch to tracking cannot silently
            # take the catalogue out of stock.
            row["Variant Inventory Tracker"] = ""
            row["Variant Inventory Qty"] = ""
            row["Variant Inventory Policy"] = "continue"
            row["Variant Fulfillment Service"] = "manual"
            row["Variant Price"] = num(v.get("Selling Price (INR)"))
            mrp, price = num(v.get("MRP (INR incl. all taxes)")), num(v.get("Selling Price (INR)"))
            # Compare-at is a marketing field: set it only when there is a real discount.
            # The legal MRP declaration lives in its own metafield regardless.
            if mrp and price and float(mrp) > float(price):
                row["Variant Compare At Price"] = mrp
            row["Variant Requires Shipping"] = "TRUE"
            row["Variant Taxable"] = "TRUE"
            row["Status"] = "draft"
            row["Published"] = "FALSE"

            if first:
                row["Title"] = name
                row["Body (HTML)"] = (v.get("Full Description") or "").strip()
                row["Vendor"] = (v.get("Manufacturer or Packer Name") or "").strip()
                row["Type"] = (v.get("Category") or "").strip()
                row["Tags"] = ", ".join(t for t in [(v.get("Category") or "").strip(), "malnad"] if t)
                row["SEO Title"] = f"{name} | Malnad Estate"[:70]
                row["SEO Description"] = (v.get("Short Description") or "").strip()[:320]
                for k, (col, _t) in PRODUCT_MF.items():
                    row[f"product.metafields.{NS}.{k}"] = (v.get(col) or "").strip()
            for k, (col, _t) in VARIANT_MF.items():
                row[f"variant.metafields.{NS}.{k}"] = (v.get(col) or "").strip()

            # Accept both separators. The working sheet writes commas; the old
            # template used semicolons. Splitting on only one silently dropped
            # every image after the first.
            raw = (v.get("Image File Names") or "").replace(";", ",")
            imgs = [i.strip() for i in raw.split(",") if i.strip()]

            # Each pack size gets its OWN photograph on the variant. Without
            # this a customer buying the 1 kg sees the 250 g pack, which for a
            # store whose whole point is that the listing matches the label is
            # not a cosmetic problem.
            if imgs:
                row["Variant Image"] = imgs[0]
                if imgs[0] not in product_images:
                    product_images.append(imgs[0])
            if first and imgs:
                row["Image Src"] = imgs[0]
                row["Image Position"] = "1"
                row["Image Alt Text"] = name
            images_needed += imgs
            for extra in imgs[1:]:
                if extra not in product_images:
                    product_images.append(extra)
            out_rows.append(row)

        # Shopify wants a product's extra images as trailing rows carrying only
        # the handle, the source and the position. Position 1 is already on the
        # first variant row, so these start at 2.
        for pos, img in enumerate(product_images[1:], start=2):
            e = {c: "" for c in cols}
            e["Handle"] = h
            e["Image Src"] = img
            e["Image Position"] = str(pos)
            e["Image Alt Text"] = name
            out_rows.append(e)

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader(); w.writerows(out_rows)

    print(f"Wrote {out}")
    print(f"  {len(groups)} products, {len(rows)} variants, {len(out_rows)} CSV rows, {len(cols)} columns")
    print(f"  every row Status=draft, Published=FALSE, inventory tracking off (packed to order)")
    print(f"  {len(set(images_needed))} distinct image files must be uploaded to Shopify Files first")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:] or ["fixtures/catalogue-filled-sample.csv", "build/shopify-import.csv"]
    sys.exit(main(a[0], a[1] if len(a) > 1 else "build/shopify-import.csv"))
