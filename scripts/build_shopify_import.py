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
        "Image Src","Image Position","Image Alt Text","SEO Title","SEO Description","Status"]


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
            row["Variant Inventory Tracker"] = "shopify"
            row["Variant Inventory Qty"] = num(v.get("Stock Qty"))
            row["Variant Inventory Policy"] = "deny"          # never oversell
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

            imgs = [i.strip() for i in (v.get("Image File Names") or "").split(";") if i.strip()]
            if first and imgs:
                row["Image Src"] = imgs[0]
                row["Image Position"] = "1"
                row["Image Alt Text"] = name
            images_needed += imgs
            out_rows.append(row)

            for extra_pos, img in enumerate(imgs[1:], start=2):
                if not first:
                    break
                e = {c: "" for c in cols}
                e["Handle"] = h; e["Image Src"] = img; e["Image Position"] = str(extra_pos)
                e["Image Alt Text"] = name
                out_rows.append(e)

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader(); w.writerows(out_rows)

    print(f"Wrote {out}")
    print(f"  {len(groups)} products, {len(rows)} variants, {len(out_rows)} CSV rows, {len(cols)} columns")
    print(f"  every row Status=draft, Published=FALSE, inventory policy=deny (no overselling)")
    print(f"  {len(set(images_needed))} distinct image files must be uploaded to Shopify Files first")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:] or ["fixtures/catalogue-filled-sample.csv", "build/shopify-import.csv"]
    sys.exit(main(a[0], a[1] if len(a) > 1 else "build/shopify-import.csv"))
