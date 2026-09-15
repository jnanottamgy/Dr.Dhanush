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
- **Transcribe declarations only from the raw, unprocessed photograph.** Never
  from an AI-enhanced image — generative tools rewrite text they cannot read
  cleanly, so a blurred digit in an FSSAI number comes back crisp and wrong. If
  the raw photo is illegible, ask for a better one.
- The client will **not** fill the catalogue spreadsheet. He sends images and
  product names as a PDF; Claude builds the catalogue from those, including
  working out variants from what is visible on the packs.

### Client answers — 15 Sep

His replies to my information-gap list. These are decisions, not suggestions.

- **Price list is coming.** He will send it; nothing gets listed until it lands.
- **No stock tracking.** *"Stock, well give according to orders"* — he packs to
  order. Shopify inventory tracking is **off** and variants stay buyable.
  `build_shopify_import.py` writes an empty tracker and `continue`, and
  `Stock Qty` is no longer a mandatory column in the validator.
- **Label photos stay as they are.** He will not re-photograph the unlabelled
  packs. See the conflict noted below.
- **Pack sizes come from the catalogue name for each product**, and *"the quantity
  is measured"* — he weighs it out, so the name is the quantity. Verified: the two
  names of that group whose packs also print a net quantity both agree (½ kg
  special tea = `500gm`, ½ liter coconut oil = `500 ml`), which settles the
  stripped fraction as **½** across all seven mangled filenames. Full table in
  `catalogue/quantities.md` — **51 of 65 resolved**, 14 still need him.
- **Because he measures, he is the packer** for the repacked goods, so his own
  compliant pack supplies packer name, address, FSSAI 21223055000121, consumer
  care and country of origin. Only MRP is genuinely missing. This retires most of
  the "25 products unlistable" blocker — but he still has to print the
  declaration on the pack he ships, and it does **not** extend to sealed
  third-party packs (Kalpatharu, Sanjivni, QTF, Shree Durga).
- **Tea and coconut oil are named off the pack images** — done, recorded in
  `catalogue/extracted.md` §6. Both filename sets were wrong.
- **Third-party makers' products are listed as his own stock.** He resells them;
  they go on the site. The maker's declarations still get printed as the maker's.
- **`malnadspices.in` will be replaced** by the new store. Not migrated, replaced.

### Two things I will not silently do

Both were raised with him; they are not resolved by his answers.

1. **No fabricated nutrition panel.** "General nutritional info" is fine as
   descriptive copy — what the product is, how it is used, what is in it from the
   printed ingredients list. A **per-100 g nutrition table is a regulated
   declaration** and I will not compute or invent one. Only two packs in the
   catalogue print a panel at all, and one of those (Shree Durga coconut oil) is
   arithmetically wrong. Retyping a wrong panel onto our listing makes it our
   misdeclaration, not the maker's.
2. **"Labels as is" — largely resolved, see the measured-quantity note above.**
   The listings can now be built, because as packer his own declarations apply.
   What remains is physical: the tubs and poly bags he ships still go out with a
   name sticker only, and as packer the full declaration belongs on the pack, not
   just the website. Under the 2026 amendment rules penalties are assessed **per
   package**. Flagged to him; the shipping label is his call, not a listing
   blocker.

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

## Catalogue intake — IN PROGRESS

Jnanottam is sending products **five at a time** and will say **"done"** when the
list is complete. Until then: receive, record each batch in
`catalogue/intake.md`, save pack images to `assets/packs/`, flag anything
illegible — and do not start transcribing into the Shopify sheet or ask for the
next batch. He drives the pace.

## Brand — corrected 15 Sep

The client is **Malnad Variety Centre**, Horanadu, Chikkamagaluru, trading
**since 1999**. Brand on pack is **Swad Horanadu** / **SWAD**. Products are
Malnad specialty foods — spice blends (puliyogare powder, rasam powder) and
coffee powder — **not** a single-estate coffee plantation.

The storefront design at `storefront-design.html` was written before the packs
were seen and tells an invented estate story (shade-grown arabica, 3,200 ft,
grind options). **Its copy must be rewritten** once the product list is complete.
The visual direction and layout still hold.

**Superseded in part by the pack backs — read this with it.** The entity printed
as manufacturer, packer and marketer is **MALNAD SPICES**, Devaramane, Horanadu
Post, Kalasa Tq, Chikkamagaluru 577181, FSSAI **21223055000121**, web
`malnadspices.in`. *Swad Horanadu* and *Malnad Chai* are its own sub-brands. He
also **resells twelve third-party brands** (Sanjivni, QTF, Kalpatharu, Aaradhya,
Shree Durga, Malnad's Nisarga, Nanjangud Suruchi's, Hallimane, Hayat, Karthik
Traders, Annapoorneshwari, Malenadu Special) and those go on the site as his
stock, under the maker's own declarations. So: a **multi-brand Malnad dry-goods
retailer**, not a producer and not a coffee estate. Full detail in
`catalogue/extracted.md`.

Open tax question: puliyogare and rasam powders are **mixed spice blends**, which
can attract **12% GST** rather than the 5% on whole spices. Needs the CA's
written call before any listing goes live.

## Where we are

**Stage 0 in progress** — Jnanottam is setting up Shopify and Razorpay.
**Stage 1 — intake complete, blocked on the price list.** All 65 products
received, photographed and transcribed. Six brand images filed in
`assets/brand/`, 71 pack images in `assets/packs/`. Scripts written and tested
against fixtures.

Blocking the first import, in order:
1. **The price list** — requested, `catalogue/price-list-request.txt`.
2. **Net quantity for 14 products** — the three unnamed powders, all six seeds,
   dry grapes, both dates, soapnut and pista. `catalogue/quantities.md`.
3. **GST rate per product** — needs the CA's written call on the blends.
4. **The three health-claim packs** — Diabeat, Nellikai powder, Amla syrup.
5. **Storefront copy is written for the wrong business** and must be rewritten.
   The visual direction and layout still hold.

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
| `catalogue/intake.md` | Intake log, 65 products, findings |
| `catalogue/extracted.md` | Everything read off the packs — brands, MRPs, findings |
| `catalogue/quantities.md` | Net quantity for all 65, from the catalogue names |
| `catalogue/client-message.txt` | Sent: the information-gap list |
| `catalogue/price-list-request.txt` | Drafted: the price-list request |
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
