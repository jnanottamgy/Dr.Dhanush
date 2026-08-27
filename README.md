# Dr. Dhanush Ayurveda — JTACS Quotation

Client quotation and proforma invoice for **Dr. R. Dhanush** (Ayurvedic physician),
covering an online store to sell medicines and wellness products.

## Files

| File | What it is |
|---|---|
| `quotation.html` | The source document. Loads webfonts from Google Fonts; theme-aware (light/dark). Edit this one. |
| `quotation-print.html` | Self-contained build with fonts inlined as base64 — used to render the PDF. Regenerated, not hand-edited. |
| `JTACS-Quotation-Dr-Dhanush-Ayurveda.pdf` | 17-page A4 PDF. This is what goes to the client. |

## Scope covered

- Shopify storefront (India-configured: INR, GST, HSN, pin-code shipping)
- Razorpay payment gateway + Magic Checkout
- Logistics via Shiprocket, with Delhivery / Blue Dart / India Post comparison
- WhatsApp Business — Community (free app) + Business Platform API for broadcast and order updates

## Commercials

- **Build fee:** **₹36,000** flat, one time, no GST added
- **Cost to go live (incl. third-party):** ₹60,396
- **Steady-state running cost:** ₹14,211–16,600/month at 100 orders, paid by the
  client directly to Shopify, Razorpay, the courier and Meta

## Before sending

Fill the placeholders marked `[...]` in the document (highlighted in amber).
Only Dr. Dhanush's details are outstanding: clinic name, address, GSTIN and
AYUSH licence number. The JTACS side carries no details beyond the name.

## Regenerating the PDF

```sh
/opt/pw-browsers/chromium --headless --disable-gpu --no-sandbox \
  --virtual-time-budget=30000 --run-all-compositor-stages-before-draw \
  --no-pdf-header-footer \
  --print-to-pdf=JTACS-Quotation-Dr-Dhanush-Ayurveda.pdf \
  "file://$PWD/quotation-print.html"
```

Third-party rates are as published in August 2026 and are set by those vendors,
not by JTACS. Sources are listed in the document footer.
