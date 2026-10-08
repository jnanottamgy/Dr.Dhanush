#!/usr/bin/env python3
"""One-page GST and HSN summary for the accountant, from a Shopify order export.

    Shopify admin -> Orders -> Export -> "Orders by date" -> CSV for Excel
    python3 scripts/gst_monthly_summary.py orders_export.csv [YYYY-MM]

Writes a Markdown file to `build/gst-summary-<period>.md`.

WHAT THIS IS FOR. The quotation promises "a one-page GST and HSN summary you can
hand to your accountant each month". GSTR-1 wants an HSN-wise table: HSN code,
quantity, taxable value, and tax split into CGST/SGST (intra-state) or IGST
(inter-state). Shopify's own export gives none of that — it has no HSN column,
because HSN lives in our `compliance` metafields — so this joins the export to
`catalogue/malnad-catalogue.csv` on SKU and does the arithmetic.

THREE THINGS IT DELIBERATELY SURFACES RATHER THAN SMOOTHING OVER:

1. **Shopify charges more tax than the declared rate.** Order #1001 proved it:
   the India country rate is applied to CGST *and* to SGST, so a 5% product is
   taxed 5 + 5 = 10%. At 5% inclusive, 1,100 should carry 1100*5/105 = 52.38;
   Shopify computed 100.00. Prices are tax-inclusive so the customer pays the
   same either way, and the whole difference comes out of the seller's margin at
   filing. The summary prints BOTH figures and the gap on every run until the
   India country rate is set to 2.5% in Settings -> Taxes and duties. **Which
   figure to file is the CA's call** — this only refuses to hide the difference.

2. **Place of supply, not billing address.** Under IGST s.10 the place of supply
   for goods is where delivery ends, so the intra/inter split is taken from the
   SHIPPING province. Seller is in Karnataka, so Karnataka is intra-state
   (CGST+SGST) and everything else is inter-state (IGST).

3. **Shipping is currently untaxed.** `taxShipping` is false on this shop, so
   delivery carries no GST. Delivery on a taxable supply is normally a composite
   supply at the principal rate, so this is reported as its own line rather than
   folded into the goods.

Rounding: each order line is computed to paise and summed; only the printed
totals are rounded, so the HSN rows add up to the order totals.
"""
import csv
import os
import sys
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

CATALOGUE = "catalogue/malnad-catalogue.csv"
SELLER_STATE = "Karnataka"
ZERO = Decimal("0.00")


def money(value):
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def load_tax_map(path=CATALOGUE):
    """SKU -> (hsn, rate, product name, pack size). SKU is the only stable join."""
    out = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            sku = row["SKU"].strip()
            if not sku:
                continue
            out[sku] = (row["HSN Code"].strip(),
                        Decimal(row["GST Rate (%)"].strip() or "0"),
                        row["Product Name"].strip(),
                        row["Pack Size"].strip())
    return out


def split_inclusive(gross, rate):
    """A GST-inclusive amount -> (taxable value, tax). gross = taxable * (1+r)."""
    taxable = gross * Decimal(100) / (Decimal(100) + rate)
    return taxable, gross - taxable


def read_orders(path, period=None):
    """Shopify's export repeats order-level columns only on the first line of
    each order and leaves them blank on the rest, so order context is carried
    forward. Refunds and cancellations are excluded, not netted — a refund
    belongs in the month it was issued, which this export cannot tell us."""
    orders, current = {}, None
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            name = (row.get("Name") or "").strip()
            if name:
                current = name
                orders.setdefault(current, {
                    "created": (row.get("Created at") or "").strip(),
                    "province": (row.get("Shipping Province Name")
                                 or row.get("Shipping Province") or "").strip(),
                    "financial": (row.get("Financial Status") or "").strip().lower(),
                    "shipping": Decimal(row.get("Shipping") or 0),
                    "taxes_charged": Decimal(row.get("Taxes") or 0),
                    "total": Decimal(row.get("Total") or 0),
                    "lines": [],
                })
            if current is None:
                continue
            qty = (row.get("Lineitem quantity") or "").strip()
            if not qty:
                continue
            orders[current]["lines"].append({
                "sku": (row.get("Lineitem sku") or "").strip(),
                "name": (row.get("Lineitem name") or "").strip(),
                "qty": int(qty),
                "price": Decimal(row.get("Lineitem price") or 0),
                "discount": Decimal(row.get("Lineitem discount") or 0),
            })

    kept, skipped = {}, []
    for name, order in orders.items():
        if period and not order["created"].startswith(period):
            continue
        if order["financial"] in ("refunded", "voided"):
            skipped.append((name, order["financial"]))
            continue
        kept[name] = order
    return kept, skipped


def summarise(orders, tax_map):
    hsn = defaultdict(lambda: {"qty": 0, "gross": ZERO, "taxable": ZERO,
                               "tax": ZERO, "rate": None, "products": set(),
                               "intra": ZERO, "inter": ZERO})
    unmatched, shipping_total, charged_total = defaultdict(Decimal), ZERO, ZERO
    intra_orders = inter_orders = 0

    for order in orders.values():
        intra = order["province"].strip().lower() == SELLER_STATE.lower()
        intra_orders += intra
        inter_orders += not intra
        shipping_total += order["shipping"]
        charged_total += order["taxes_charged"]

        for line in order["lines"]:
            gross = line["price"] * line["qty"] - line["discount"]
            entry = tax_map.get(line["sku"])
            if entry is None:
                unmatched[line["sku"] or line["name"]] += gross
                continue
            code, rate, product, pack = entry
            taxable, tax = split_inclusive(gross, rate)
            bucket = hsn[code]
            bucket["qty"] += line["qty"]
            bucket["gross"] += gross
            bucket["taxable"] += taxable
            bucket["tax"] += tax
            bucket["rate"] = rate
            bucket["products"].add(f"{product} {pack}".strip())
            bucket["intra" if intra else "inter"] += tax

    return {"hsn": hsn, "unmatched": unmatched, "shipping": shipping_total,
            "charged": charged_total, "intra_orders": intra_orders,
            "inter_orders": inter_orders}


def render(result, orders, skipped, period):
    hsn, lines = result["hsn"], []
    total_gross = sum(b["gross"] for b in hsn.values()) or ZERO
    total_taxable = sum(b["taxable"] for b in hsn.values()) or ZERO
    total_tax = sum(b["tax"] for b in hsn.values()) or ZERO
    total_intra = sum(b["intra"] for b in hsn.values()) or ZERO
    total_inter = sum(b["inter"] for b in hsn.values()) or ZERO

    add = lines.append
    add(f"# GST and HSN summary — {period or 'all orders in this export'}")
    add("")
    add("Malnad Spices · Devaramane, Horanadu Post, Kalasa Taluk, "
        "Chikkamagaluru 577181 · FSSAI 21223055000121")
    add("")
    add(f"**{len(orders)} orders** — {result['intra_orders']} within Karnataka "
        f"(CGST + SGST), {result['inter_orders']} to other states (IGST).")
    add("All selling prices are GST-inclusive, so the taxable value below is "
        "worked out of the price rather than added to it.")
    add("")
    add("## HSN-wise summary")
    add("")
    add("| HSN | Rate | Qty | Gross (incl. GST) | Taxable value | CGST | SGST | IGST | Total GST |")
    add("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for code in sorted(hsn):
        b = hsn[code]
        cgst = sgst = b["intra"] / 2
        add(f"| {code} | {b['rate']}% | {b['qty']} | {money(b['gross'])} | "
            f"{money(b['taxable'])} | {money(cgst)} | {money(sgst)} | "
            f"{money(b['inter'])} | {money(b['tax'])} |")
    add(f"| **Total** | | | **{money(total_gross)}** | **{money(total_taxable)}** "
        f"| **{money(total_intra / 2)}** | **{money(total_intra / 2)}** "
        f"| **{money(total_inter)}** | **{money(total_tax)}** |")
    add("")
    add("### What sits under each HSN code")
    add("")
    for code in sorted(hsn):
        add(f"- **{code}** — " + "; ".join(sorted(hsn[code]["products"])))
    add("")

    add("## Delivery charges")
    add("")
    add(f"Delivery collected: **{money(result['shipping'])}**, carrying **no GST**.")
    add("")
    add("`taxShipping` is off on this store, so Shopify charges no tax on "
        "delivery. Delivery on a taxable supply is normally a composite supply "
        "at the principal rate. If that treatment is wanted, the setting is "
        "Settings → Taxes and duties → *Charge tax on shipping rates*. Because "
        "prices are tax-inclusive, switching it changes the invoice split, not "
        "what the customer pays.")
    add("")

    add("## Reconciliation — what Shopify actually charged")
    add("")
    charged = result["charged"]
    gap = charged - total_tax
    add(f"| | Amount |")
    add(f"|---|---:|")
    add(f"| GST at the declared rates (this summary) | {money(total_tax)} |")
    add(f"| GST as computed by Shopify at checkout | {money(charged)} |")
    add(f"| **Difference** | **{money(gap)}** |")
    add("")
    if gap > Decimal("0.50"):
        add(f"**Shopify is over-charging by {money(gap)} this period.** The India "
            "country rate in Settings → Taxes and duties is applied to CGST *and* "
            "to SGST, so a 5% product is taxed 5 + 5 = 10%. The fix is to set the "
            "India country rate to **2.5%**, which yields CGST 2.5 + SGST 2.5 = 5%, "
            "and to leave the per-state IGST rows at 5% \"instead of federal\". "
            "Until that is changed the two figures above will keep diverging, and "
            "the difference comes out of the seller's margin — the customer pays "
            "the same either way, because prices are tax-inclusive.")
    elif gap < Decimal("-0.50"):
        add(f"**Shopify is under-charging by {money(-gap)} this period.** Check the "
            "India country rate in Settings → Taxes and duties before filing.")
    else:
        add("The two agree. The India country rate is configured correctly.")
    add("")

    if result["unmatched"]:
        add("## Lines with no HSN code — NEEDS ATTENTION")
        add("")
        add("These sold but are not in `catalogue/malnad-catalogue.csv`, so no "
            "HSN or rate could be applied and they are **excluded from every "
            "figure above**. A product added in Shopify without being added to "
            "the catalogue lands here.")
        add("")
        add("| SKU or name | Gross |")
        add("|---|---:|")
        for key, gross in sorted(result["unmatched"].items()):
            add(f"| {key} | {money(gross)} |")
        add("")

    if skipped:
        add("## Excluded")
        add("")
        for name, status in skipped:
            add(f"- {name} — {status}")
        add("")
        add("Refunded and voided orders are left out rather than netted off: a "
            "refund belongs in the month it was issued, and this export cannot "
            "say when that was.")
        add("")

    add("---")
    add("")
    add("Generated by `scripts/gst_monthly_summary.py` from a Shopify order "
        "export joined to `catalogue/malnad-catalogue.csv` on SKU. Figures are "
        "worked to paise and rounded only for printing, so the rows add up.")
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    export, period = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else None)
    tax_map = load_tax_map()
    orders, skipped = read_orders(export, period)
    if not orders:
        print(f"No orders found in {export}"
              + (f" for {period}" if period else ""))
        return 1
    text = render(summarise(orders, tax_map), orders, skipped, period)
    os.makedirs("build", exist_ok=True)
    out = f"build/gst-summary-{period or 'all'}.md"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    print(f"\nWritten to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
