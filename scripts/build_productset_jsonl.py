#!/usr/bin/env python3
"""Turn the working sheet into productSet JSONL for bulkOperationRunMutation.

Images are referenced by their raw.githubusercontent.com URL. Shopify fetches
each one at creation and copies it onto its own CDN, so the GitHub URL is only
needed for the duration of the import.
"""
import csv, json, sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHEET = ROOT / "catalogue" / "malnad-catalogue.csv"
OUT = ROOT / "build" / "productset.jsonl"

RAW = ("https://raw.githubusercontent.com/jnanottamgy/Dr.Dhanush/"
       "claude/dhanush-ayurveda-quotation-ymmhi5/assets/packs/")

# Products already created by hand during the gate test — pass their IDs so the
# bulk run updates them in place instead of creating duplicates.
EXISTING = {
    "Malnad Chai - Premium Malnad Tea Powder": "gid://shopify/Product/7836399140977",
    "Ghani-Pressed Copra Coconut Oil":         "gid://shopify/Product/7836399304817",
}

PRODUCT_MF = [
    ("Manufacturer or Packer Name", "packer_name", "single_line_text_field"),
    ("Manufacturer or Packer Full Address", "packer_address", "multi_line_text_field"),
    ("Country of Origin", "country_of_origin", "single_line_text_field"),
    ("Consumer Care Name", "care_name", "single_line_text_field"),
    ("Consumer Care Phone", "care_phone", "single_line_text_field"),
    ("Consumer Care Email", "care_email", "single_line_text_field"),
    ("FSSAI Licence Number", "fssai_licence", "single_line_text_field"),
    ("HSN Code", "hsn_code", "single_line_text_field"),
    ("GST Rate (%)", "gst_rate", "number_decimal"),
    ("Ingredients", "ingredients", "multi_line_text_field"),
    ("Storage Instructions", "storage", "multi_line_text_field"),
    ("Estate / Origin", "estate", "single_line_text_field"),
    ("Altitude (ft)", "altitude_ft", "number_integer"),
    ("Harvest Month", "harvest_month", "single_line_text_field"),
    ("Roast Level", "roast_level", "single_line_text_field"),
]
VARIANT_MF = [
    ("Net Quantity", "net_quantity", "single_line_text_field"),
    ("MRP (INR incl. all taxes)", "mrp", "number_decimal"),
    ("Date of Manufacture or Packing", "mfg_date", "single_line_text_field"),
    ("Best Before / Use By", "best_before", "single_line_text_field"),
]


def handle(name):
    out = "".join(c if c.isalnum() else "-" for c in name.lower())
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


# These two must never reach the storefront. QTF is a bulk sack with no retail
# declarations at all; Diabeat prints a condition and a dosage on its front
# label. They are still created, as drafts, so the catalogue is complete - the
# tag is what stops a bulk publish sweeping them live by accident.
DO_NOT_PUBLISH = {
    "QTF Tea - Guard-Hitlow Tea Factory",
    "Nanjangud Suruchi's Diabeat",
}


def tags_for(name, first):
    t = [x for x in [handle(first.get("Category") or ""), "needs-price"] if x]
    if name in DO_NOT_PUBLISH:
        t.append("DO-NOT-PUBLISH")
    return t


def mf(row, spec):
    out = []
    for col, key, typ in spec:
        v = (row.get(col) or "").strip()
        if v:
            out.append({"namespace": "compliance", "key": key,
                        "value": v, "type": typ})
    return out


def main():
    groups = OrderedDict()
    for r in csv.DictReader(SHEET.open(encoding="utf-8")):
        groups.setdefault((r.get("Product Name") or "").strip(), []).append(r)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    n_files = 0
    with OUT.open("w", encoding="utf-8") as fh:
        for name, variants in groups.items():
            first = variants[0]
            # Every distinct image across the product, front first.
            imgs = []
            for v in variants:
                raw = (v.get("Image File Names") or "").replace(";", ",")
                for i in [x.strip() for x in raw.split(",") if x.strip()]:
                    if i not in imgs:
                        imgs.append(i)
            n_files += len(imgs)

            p = {
                "title": name,
                "handle": handle(name),
                "status": "DRAFT",
                "vendor": (first.get("Manufacturer or Packer Name") or "").strip() or "Malnad Spices",
                "productType": (first.get("Category") or "").strip(),
                "tags": tags_for(name, first),
                "metafields": mf(first, PRODUCT_MF),
                "files": [{"originalSource": RAW + i, "contentType": "IMAGE",
                           "filename": i, "alt": name} for i in imgs],
                "productOptions": [{
                    "name": "Pack size", "position": 1,
                    "values": [{"name": (v.get("Pack Size") or "Default").strip() or "Default"}
                               for v in variants],
                }],
                "variants": [],
            }
            if name in EXISTING:
                p["id"] = EXISTING[name]
            desc = (first.get("Short Description") or "").strip()
            if desc:
                p["descriptionHtml"] = f"<p>{desc}</p>"

            for v in variants:
                pack = (v.get("Pack Size") or "Default").strip() or "Default"
                raw = (v.get("Image File Names") or "").replace(";", ",")
                vimgs = [x.strip() for x in raw.split(",") if x.strip()]
                sw = (v.get("Shipping Weight (g)") or "").strip()
                var = {
                    "optionValues": [{"optionName": "Pack size", "name": pack}],
                    "sku": (v.get("SKU") or "").strip(),
                    "price": "0.00",
                    "inventoryPolicy": "CONTINUE",
                    "inventoryItem": {"tracked": False, "requiresShipping": True},
                    "metafields": mf(v, VARIANT_MF),
                }
                if sw:
                    var["inventoryItem"]["measurement"] = {
                        "weight": {"value": float(sw), "unit": "GRAMS"}}
                if vimgs:
                    var["file"] = {"originalSource": RAW + vimgs[0],
                                   "contentType": "IMAGE", "filename": vimgs[0]}
                p["variants"].append(var)

            fh.write(json.dumps({"input": p}, ensure_ascii=False) + "\n")

    print(f"Wrote {OUT}")
    print(f"  {len(groups)} products, {n_files} image references")
    print(f"  {sum(1 for g in groups if g in EXISTING)} updated in place by ID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
