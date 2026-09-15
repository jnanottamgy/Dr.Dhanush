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

**Commercials**

- **Build fee:** **₹38,000** flat, one time, no GST added
- **Cost to go live (incl. third-party):** ₹60,626 — ₹62,396 with the WhatsApp API
- **Running cost:** ₹3,982–6,371/month at 200 orders, paid by the client directly
  to Shopify and Razorpay; ₹7,830–10,219 if the WhatsApp API is added
- Milestones 50/25/25 — ₹19,000 / ₹9,500 / ₹9,500

**Scope:** Shopify Basic store · Razorpay prepaid checkout with Magic Checkout
(avoids Shopify's 2% third-party gateway fee, ~₹28,700/yr) · WhatsApp Business
community on the free app, with the paid API priced as an optional upgrade ·
order and dispatch workflow for the client's own delivery team · FSSAI and
Legal Metrology declarations enforced as required product fields · GST 5% for
coffee and most spices. No logistics, no COD, no retainer.

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
