# Malnad Store — project memory

Standing context for this project. **Keep this updated** as decisions are made,
so nothing has to be reconstructed from memory after a session compacts.

---

## Who

- **Jnanottam** — runs JTACS, owns the client relationship, does everything that
  needs a password, an OTP, KYC or a browser. Works at a chartered accountancy
  firm, so tax questions are his own shop.
- **Claude** — the dev team. Writes code, themes, configuration, copy, docs,
  checklists. Cannot complete KYC, receive an OTP, or log into anything.
- **Dr. R. Dhanush** — the client. Sells Malnad produce: coffee, spices, honey,
  estate goods. Holds all required licences already.

## What is being built

Shopify Basic storefront · Razorpay prepaid checkout · WhatsApp Business
community · owner dashboard. **₹38,000 flat**, one time.

---

## Standing instructions from Jnanottam

These are his explicit preferences. Do not reintroduce anything he has removed.

### Documents
- **Flat fee, no GST added** on JTACS charges. ₹38,000 is the price.
- JTACS is identified as **"Jnanottam" only**. No entity name, address, GSTIN,
  PAN, phone, email or bank details anywhere.
- Client block is **name and descriptor only**. **No fill-in placeholders
  anywhere** — documents must never ask the client to supply something.
- **No logistics section.** Client has his own delivery arrangement.
- **Prepaid only, no Cash on Delivery.**
- **No maintenance or retainer section.** He removed it; do not re-add it.
- Plain, simple English. Professional. Written so a non-technical reader follows it.

### Product data
- **Every declaration is printed on the product packaging.** FSSAI number, net
  quantity, MRP, packer name and address, manufacture date, best before,
  consumer care — read them off the pack photographs.
- **Never invent a declaration.** If it is not visible on the pack, it does not
  go on the listing. No exceptions, no "reasonable assumptions".
- **A pack missing a mandatory declaration is a finding**, reported to the
  client. It is not a gap to fill in.
- The client will **not** fill the catalogue spreadsheet. He sends images and
  product names as a PDF; Claude builds the catalogue from those, including
  working out variants from what is visible on the packs.

### Working style
- **Verify plan and platform claims before stating them.** He has twice called
  out over-hedging. Check, then state plainly. Do not pad with "verify this later"
  when it can be verified now.
- Update this file as instructions accumulate.

---

## Decisions made, and why

| Decision | Reason |
|---|---|
| **Shopify, not a custom build** | Below roughly ₹3 lakh/month in sales, Shopify's plan plus Magic Checkout costs less than self-hosted infrastructure, and carries none of the operational burden. The custom build plan is superseded, kept for reference. |
| **Razorpay Magic Checkout** | Shopify adds 2% on Basic because Shopify Payments is unavailable in India. Magic Checkout is ~0.65% and currently falls outside that fee. Saves ~₹28,700/year. Flagged to the client as a gap in Shopify's rules, not a guarantee. |
| **Prepaid only** | Client instruction. Also removes COD refusal losses entirely. |
| **WhatsApp community on the free Business App** | Communities only exist on the Business App; the API cannot run one, and a number moved to the API loses Communities permanently. API is priced as a separate optional upgrade, triggered by the 256-contact broadcast cap. |
| **Owner dashboard included at no charge** | Listed at ₹8,000 then discounted to zero, so the client sees the value. Total stays ₹38,000. |
| **Offline sales as real Shopify draft orders** | Not a dashboard field. This way stock decrements, a GST invoice is raised, and the website cannot sell what was already sold at the estate gate. Draft orders work on Basic and on the Shopify phone app. |
| **Dashboard reads the Admin API, read-only** | Scopes `read_orders`, `read_products`, `read_customers` only. No write scope, no payout scope. Free on Basic. |
| **Metafields: some on variant, not product** | Net quantity, MRP, manufacture date and best before differ between a 250 g and a 1 kg pack. Putting them on the product is how a store ends up declaring the wrong net quantity. |
| **MRP ≠ compare-at price** | Compare-at is a marketing field; MRP is a legal declaration. MRP lives in its own metafield always; compare-at is written only where the selling price is genuinely lower. |
| **Enhance images, never generate** | Image-to-image only. A redrawn label misrepresents a food product. Test: customer holds pack beside photo, they match. |

## Corrections already made — do not regress

- Shopify **does not** natively block publishing a product with an empty
  metafield. Validation rules constrain values, not presence. Enforcement is our
  pipeline: validator, draft-only import, theme rendering, and the audit script.
- **Shopify Flow is not needed** for order source tracking. Native order
  attribution plus UTM parameters cover it on Basic.
- **UTM parameters on WhatsApp links are mandatory.** WhatsApp strips the
  referrer header, so without them every WhatsApp order looks like direct traffic
  and the channel split is silently wrong.
- Shopify products are **unlimited on every plan**, including Basic. Limits that
  do apply: 2,048 variants per product, 3 option types, **2 staff logins**,
  10 locations. Collaborator access does not consume a staff seat.

---

## Security posture

- **No secret ever enters a chat transcript.** Not a password, API key, OTP or
  bank detail. Jnanottam generates them and pastes them directly into the
  destination system.
- Claude receives exactly two grants: **Shopify collaborator access** (listed
  permissions only) and **Google Analytics / Search Console**.
- Claude needs **nothing from Razorpay**. Live keys are pasted by Jnanottam on a
  screen-share.
- Never send: passwords · OTPs · live Razorpay keys · bank details · 2FA recovery
  codes · the client's KYC documents.
- Nothing secret in this repository. `.gitignore` covers env files and exports.

---

## Where we are

**Stage 0 in progress** — Jnanottam is setting up Shopify and Razorpay.
**Stage 1 built and waiting on data** — scripts written and tested against
fixtures; waiting on the client's product images and names PDF.

Eight stages total, each with a gate. Full detail in `build-runbook.html`.
Stage 3 (payments) is gated hardest: the 16-row test matrix runs in test mode and
again live, and is not complete until a settlement is confirmed landed in the
client's bank.

## Repository

| Path | What |
|---|---|
| `quotation-malnad.html` | **Current** client quotation, ₹38,000 |
| `build-runbook.html` | Internal eight-stage build runbook |
| `dashboard-mockup.html` | Owner dashboard design mockup, sample data |
| `scripts/validate_catalogue.py` | Blocks incomplete or illegal product data |
| `scripts/build_shopify_import.py` | Catalogue → Shopify import CSV, all draft |
| `scripts/audit_live_products.py` | Finds live products missing declarations |
| `docs/stage1-catalogue.md` | Metafield definitions and import procedure |
| `docs/product-photography.md` | Storefront palette and image direction |
| `docs/image-prompts.txt` | The three prompts, plain text |
| `templates/catalogue-template.csv` | Now Claude's working format, not a client form |
| `build-plan.html`, `quotation.html` | **Superseded.** Custom build, and the earlier Ayurveda quotation. |

## Storefront palette

`#F4F2ED` paper · `#FFFFFF` card · `#1F4034` canopy green (brand) ·
`#A4552F` laterite (accent only) · `#2A2D27` ink · `#6E7268` muted.
Mood: shade-grown, monsoon, unhurried. Not warm cream and hessian.

## Commands

```sh
python3 scripts/validate_catalogue.py   <sheet.csv>
python3 scripts/build_shopify_import.py <sheet.csv> build/shopify-import.csv
python3 scripts/audit_live_products.py  <products_export.csv>
```

PDFs are rendered with headless Chromium — see the README for the command.
