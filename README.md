# Dr. Dhanush — client documents

Two documents for the same client, in sequence. **The build plan is current; the
Ayurveda quotation is superseded** and kept only for reference.

## Current — Malnad store quotation

Shopify storefront, Razorpay payments and a WhatsApp Business community for a
Malnad produce business (coffee, spices, estate goods).

| File | What it is |
|---|---|
| `quotation-malnad.html` | Source. Loads webfonts from Google Fonts; theme-aware. **Edit this one.** |
| `quotation-malnad-print.html` | Self-contained build with fonts inlined — used to render the PDF. Regenerated, not hand-edited. |
| `JTACS-Quotation-Malnad-Store.pdf` | 15-page A4 PDF. |
| `dashboard-mockup.html` | Design mockup of the owner dashboard — sample data, agreed before building. |

**Commercials**

- **Build fee:** **₹38,000** flat, one time, no GST added
- **Cost to go live (incl. third-party):** ₹60,626 — ₹62,396 with the WhatsApp API
- **Running cost:** ₹3,982–6,371/month at 200 orders, paid by the client directly
  to Shopify and Razorpay; ₹7,830–10,219 if the WhatsApp API is added
- Milestones 50/25/25 — ₹19,000 / ₹9,500 / ₹9,500

**Scope:** Shopify Basic store · Razorpay prepaid checkout with Magic Checkout
(avoids Shopify's 2% third-party gateway fee, ~₹28,700/yr) · WhatsApp Business
community on the free app, with the paid API priced as an optional upgrade ·
order and dispatch workflow for the packing team · **owner dashboard** with
offline-sale entry, shown at ₹8,000 and included at no charge · FSSAI and
Legal Metrology declarations enforced as required product fields · GST 5% for
coffee and most spices. No logistics, no COD, no retainer.

## Build — runbook and templates

Internal working documents for the build itself.

| File | What it is |
|---|---|
| `build-runbook.html` | Source. **Edit this one.** |
| `build-runbook-print.html` | Fonts-inlined build used to render the PDF. Regenerated, not hand-edited. |
| `JTACS-Malnad-Build-Runbook.pdf` | 15-page A4 PDF. |
| `templates/catalogue-template.csv` | 30-column product data sheet — one row per pack size. Goes to the client on day one. |
| `templates/HOW-TO-FILL.md` | Column-by-column guide for whoever fills the sheet. |

**Eight stages, each with a gate.** Stage 3 (payments) is gated hardest: the
16-row payment test matrix must pass in test mode and again live, and a
settlement must be confirmed landed in the client's bank before anything
proceeds.

**Credential posture — the whole point of the document.** Secrets are generated
and entered by the client, directly into the destination system, never into a
chat transcript. Claude receives exactly two grants: Shopify **collaborator**
access with listed permissions, and Google Analytics/Search Console. No
passwords, no OTPs, no live Razorpay keys, no bank details, no KYC documents,
at any stage.

## Superseded

Kept for reference only.

| File | What it was |
|---|---|
| `build-plan.html`, `JTACS-Malnad-Build-Plan.pdf` | Delivery plan for a custom-built storefront and owner dashboard. Dropped in favour of Shopify — below roughly ₹3 lakh/month in sales, Shopify costs less than self-hosted infrastructure. |
| `quotation.html`, `JTACS-Quotation-Dr-Dhanush-Ayurveda.pdf` | ₹36,000 Shopify quotation for selling Ayurvedic medicines. Overtaken by the pivot to Malnad produce. |

## Regenerating a PDF

```sh
/opt/pw-browsers/chromium --headless --disable-gpu --no-sandbox \
  --virtual-time-budget=30000 --run-all-compositor-stages-before-draw \
  --no-pdf-header-footer \
  --print-to-pdf=JTACS-Quotation-Malnad-Store.pdf \
  "file://$PWD/quotation-malnad-print.html"
```

Third-party rates and regulatory references are as published in September 2026
and are set by those bodies, not by JTACS. Sources are listed in each document's
footer.
