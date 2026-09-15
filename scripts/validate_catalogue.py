#!/usr/bin/env python3
"""Validate a filled catalogue sheet before anything reaches Shopify.

Errors block the import. Warnings need a human decision but do not block.

    python3 scripts/validate_catalogue.py templates/catalogue-template.csv
"""
import csv, sys, re
from collections import defaultdict

# Declarations required on every food listing (Legal Metrology + FSSAI).
# Per variant — these differ between a 250 g and a 1 kg pack.
PER_VARIANT = ["Net Quantity", "MRP (INR incl. all taxes)", "Best Before / Use By",
               "Date of Manufacture or Packing"]
# Per product — must be identical on every row of the same product.
PER_PRODUCT = ["Manufacturer or Packer Name", "Manufacturer or Packer Full Address",
               "Country of Origin", "Consumer Care Name", "Consumer Care Phone",
               "Consumer Care Email", "FSSAI Licence Number", "HSN Code", "GST Rate (%)"]
# "Stock Qty" is deliberately NOT here: the client packs to order and holds no
# counted stock, so the column stays in the sheet but is never mandatory. It is
# still range-checked below if he ever chooses to fill it.
COMMERCIAL = ["Product Name", "Category", "Pack Size", "SKU",
              "Selling Price (INR)", "Shipping Weight (g)"]

VALID_GST = {"0", "5", "12", "18"}
COFFEE_HSN = {"0901"}
SPICE_HSN = {"0904", "0905", "0906", "0907", "0908", "0909", "0910"}


def money(v):
    try:
        return float(str(v).replace(",", "").replace("₹", "").strip())
    except ValueError:
        return None


def main(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        print("FAIL  sheet is empty"); return 1

    errors, warnings = [], []
    missing_cols = [c for c in COMMERCIAL + PER_VARIANT + PER_PRODUCT if c not in rows[0]]
    if missing_cols:
        print("FAIL  sheet is missing columns: " + ", ".join(missing_cols)); return 1

    seen_sku, product_fields = {}, defaultdict(dict)

    for i, r in enumerate(rows, start=2):        # row 2 = first data row in a spreadsheet
        name = (r.get("Product Name") or "").strip()
        tag = f"row {i} ({name or 'unnamed'} {r.get('Pack Size','').strip()})"

        for c in COMMERCIAL + PER_VARIANT + PER_PRODUCT:
            if not (r.get(c) or "").strip():
                errors.append(f"{tag}: '{c}' is empty")

        sku = (r.get("SKU") or "").strip()
        if sku:
            if sku in seen_sku:
                errors.append(f"{tag}: SKU '{sku}' already used on row {seen_sku[sku]}")
            seen_sku[sku] = i

        price, mrp = money(r.get("Selling Price (INR)")), money(r.get("MRP (INR incl. all taxes)"))
        if price is None and (r.get("Selling Price (INR)") or "").strip():
            errors.append(f"{tag}: selling price is not a number")
        if mrp is None and (r.get("MRP (INR incl. all taxes)") or "").strip():
            errors.append(f"{tag}: MRP is not a number")
        if price is not None and mrp is not None and price > mrp:
            errors.append(f"{tag}: selling price {price:g} is above MRP {mrp:g} — illegal")
        if price is not None and price <= 0:
            errors.append(f"{tag}: selling price must be greater than zero")

        for c, lo in (("Stock Qty", 0), ("Shipping Weight (g)", 1)):
            v = (r.get(c) or "").strip()
            if v:
                try:
                    if float(v) < lo:
                        errors.append(f"{tag}: '{c}' must be at least {lo}")
                except ValueError:
                    errors.append(f"{tag}: '{c}' is not a number")

        hsn = (r.get("HSN Code") or "").strip()
        if hsn:
            if not re.fullmatch(r"\d{4,8}", hsn):
                errors.append(f"{tag}: HSN '{hsn}' must be 4 to 8 digits")
            else:
                head, cat = hsn[:4], (r.get("Category") or "").strip().lower()
                if cat.startswith("coffee") and head not in COFFEE_HSN:
                    warnings.append(f"{tag}: category Coffee but HSN starts {head} — expected 0901")
                if cat.startswith("spice") and head not in SPICE_HSN:
                    warnings.append(f"{tag}: category Spices but HSN starts {head} — expected 0904-0910")

        gst = (r.get("GST Rate (%)") or "").strip().rstrip("%")
        if gst and gst not in VALID_GST:
            errors.append(f"{tag}: GST rate '{gst}' is not 0, 5, 12 or 18")
        if gst == "18":
            warnings.append(f"{tag}: GST 18% on a food product — confirm with the accountant")

        if not (r.get("Image File Names") or "").strip():
            warnings.append(f"{tag}: no image listed — it will publish without a photograph")

        # product-level fields must agree across every pack size of the product
        if name:
            for c in PER_PRODUCT:
                v = (r.get(c) or "").strip()
                if not v:
                    continue
                prev = product_fields[name].get(c)
                if prev is None:
                    product_fields[name][c] = v
                elif prev != v:
                    errors.append(f"{tag}: '{c}' is '{v}' but another pack size of "
                                  f"{name} says '{prev}' — they must match")

    print(f"Checked {len(rows)} rows across {len(product_fields)} products.\n")
    for kind, items in (("ERROR", errors), ("WARN ", warnings)):
        for m in items:
            print(f"{kind}  {m}")
    if errors or warnings:
        print()
    print(f"{len(errors)} error(s), {len(warnings)} warning(s).")
    if errors:
        print("\nNot ready to import. Fix every error above, then run this again.")
        return 1
    print("\nReady to import. Warnings are worth a look but do not block.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "templates/catalogue-template.csv"))
