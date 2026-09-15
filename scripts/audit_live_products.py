#!/usr/bin/env python3
"""Audit a Shopify product export for live products missing a legal declaration.

Shopify does NOT natively refuse to publish a product with an empty metafield.
This script is what makes the compliance promise real: run it before launch and
weekly afterwards, so a product added by hand in admin cannot quietly go live
without its declarations.

    Shopify admin -> Products -> Export -> All products -> CSV
    python3 scripts/audit_live_products.py ~/Downloads/products_export.csv
"""
import csv, sys

NS = "compliance"
REQUIRED_PRODUCT = ["packer_name", "packer_address", "country_of_origin",
                    "care_name", "care_phone", "care_email", "fssai_licence",
                    "hsn_code", "gst_rate"]
REQUIRED_VARIANT = ["net_quantity", "mrp", "mfg_date", "best_before"]

LABEL = {
    "packer_name": "packer name", "packer_address": "packer address",
    "country_of_origin": "country of origin", "care_name": "consumer care name",
    "care_phone": "consumer care phone", "care_email": "consumer care email",
    "fssai_licence": "FSSAI licence number", "hsn_code": "HSN code",
    "gst_rate": "GST rate", "net_quantity": "net quantity", "mrp": "MRP",
    "mfg_date": "date of manufacture", "best_before": "best before",
}


def get(row, scope, key):
    for c in (f"{scope}.metafields.{NS}.{key}",
              f"{key} ({scope}.metafields.{NS}.{key})"):
        if c in row:
            return (row[c] or "").strip()
    return None


def main(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        print("Export is empty."); return 1

    if get(rows[0], "product", "fssai_licence") is None:
        print("This export has no compliance metafield columns.\n"
              "Re-export from Shopify with metafields included, or the audit proves nothing.")
        return 1

    product_state, findings = {}, []
    for r in rows:
        h = (r.get("Handle") or "").strip()
        if not h:
            continue
        status = (r.get("Status") or "").strip().lower()
        title = (r.get("Title") or "").strip()
        if title or status:
            product_state.setdefault(h, {"title": title or h, "status": status or "unknown",
                                         "missing": set()})
        st = product_state.setdefault(h, {"title": h, "status": "unknown", "missing": set()})
        if title:
            st["title"] = title
        if status:
            st["status"] = status
        if title:                                    # product-level row
            for k in REQUIRED_PRODUCT:
                if not get(r, "product", k):
                    st["missing"].add(LABEL[k])
        if (r.get("Variant SKU") or "").strip():     # variant row
            for k in REQUIRED_VARIANT:
                if not get(r, "variant", k):
                    st["missing"].add(f"{LABEL[k]} (on {(r.get('Option1 Value') or 'a pack size').strip()})")

    live_bad = draft_bad = 0
    for h, st in product_state.items():
        if not st["missing"]:
            continue
        live = st["status"] == "active"
        if live:
            live_bad += 1
        else:
            draft_bad += 1
        findings.append((live, st["title"], sorted(st["missing"])))

    findings.sort(key=lambda f: (not f[0], f[1]))
    for live, title, missing in findings:
        print(f"{'LIVE ' if live else 'draft'}  {title}")
        for m in missing:
            print(f"         missing: {m}")

    total = len(product_state)
    print(f"\n{total} product(s) checked. "
          f"{live_bad} LIVE product(s) incomplete, {draft_bad} draft(s) incomplete.")
    if live_bad:
        print("\nLive products are missing legal declarations. Unpublish them or complete them today —\n"
              "Legal Metrology penalties are assessed per package.")
        return 1
    print("\nEvery live product carries a complete set of declarations.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "products_export.csv"))
