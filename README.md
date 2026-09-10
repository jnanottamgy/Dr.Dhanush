# Dr. Dhanush — client documents

Two documents for the same client, in sequence. **The build plan is current; the
Ayurveda quotation is superseded** and kept only for reference.

## Current — Malnad commerce build plan

Custom-built storefront, owner dashboard and WhatsApp ordering for a Malnad
produce business (coffee, spices, estate goods). No rented platform.

| File | What it is |
|---|---|
| `build-plan.html` | Source. Loads webfonts from Google Fonts; theme-aware. **Edit this one.** |
| `build-plan-print.html` | Self-contained build with fonts inlined — used to render the PDF. Regenerated, not hand-edited. |
| `JTACS-Malnad-Build-Plan.pdf` | 17-page A4 PDF. |

**Scope:** storefront on a Medusa commerce core with a Next.js front end ·
two-layer dashboard (operations console + bespoke Owner View) · Razorpay
prepaid checkout · WhatsApp Community plus in-chat ordering via Flows ·
FSSAI and Legal Metrology declarations enforced as required product fields ·
GST at 5% for coffee and most spices.

**Engineering commitments:** designed for 1,500 orders/day against an expected
20–40 (~40× headroom) · catalogue served from CDN edge so ~98% of browsing never
reaches the database · idempotent payment webhooks with an hourly reconciliation
sweep · stock decremented under row lock · load test and backup-restore drill
both gated before launch.

**Timeline:** six weeks in five phases, each with an explicit gate. The critical
path is Razorpay/Meta verification and client catalogue content, not code.

**Open before quoting:** after-launch support model, and whether source code is
transferred outright or licensed.

## Superseded — Ayurveda quotation

| File | What it is |
|---|---|
| `quotation.html` / `quotation-print.html` | Source and print build |
| `JTACS-Quotation-Dr-Dhanush-Ayurveda.pdf` | 15-page A4 PDF |

Quoted a Shopify store at a flat ₹36,000 for selling Ayurvedic medicines.
Overtaken by the pivot to Malnad produce and the decision to build in-house.

## Regenerating a PDF

```sh
/opt/pw-browsers/chromium --headless --disable-gpu --no-sandbox \
  --virtual-time-budget=30000 --run-all-compositor-stages-before-draw \
  --no-pdf-header-footer \
  --print-to-pdf=JTACS-Malnad-Build-Plan.pdf \
  "file://$PWD/build-plan-print.html"
```

Third-party rates and regulatory references are as published in September 2026
and are set by those bodies, not by JTACS. Sources are listed in each document's
footer.
