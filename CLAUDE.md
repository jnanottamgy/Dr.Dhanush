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
  `catalogue/quantities.md` — **55 of 65 resolved** after a second pass over the
  labels recovered four more (soapnut powder 200 g ₹110, sikakai 200 g ₹120,
  pista 500 g, dry grapes 500 g). Nine bare tubs/bags still need him, and
  nellikai powder needs a sharper photo — its figures are printed but the raw
  image will not resolve 200 g from 280 g, so it is not being guessed.
- **`antvala-powder` is ಅಂಟುವಾಳ ಪೌಡರ್ — soapnut powder**, not a spice. With
  sikakai powder and the whole soapnuts that is three **non-food** washing and
  hair-care lines: separate storefront section, and their HSN/GST will not match
  the food rates.
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
### Pack sizes and prices — supplied 16 Sep

| Product | Net quantity | Price |
|---|---|---|
| Chia · Sabja · Flax · Magaz · Pumpkin · Sunflower seeds | 150 g each | ₹140 each |
| Soapnut, whole | 150 g | ₹140 |
| Dates | 500 g | ₹150 |
| Special Dates | 500 g | ₹200 |
| Pista | 500 g (was on the pack) | ₹900 |
| Hayat raisins | 500 g (was on the pack) | ₹300 |
| Nellikai powder | **200 g — confirmed** | **still missing** |
| QTF Tea | **1 kg — confirmed** | **still missing** |

**Net quantity is now complete: all 63 variants have one.**

**One number was given per item, so it is both the MRP and the selling price.**
None of these packs prints an MRP, and he is the packer, so the figure he names
*is* the declared MRP; no compare-at is written, since there is no discount.
Loaded into the sheet and pushed to all 12 products in Shopify.

**Nellikai powder still has no price.** Its MRP is printed on the pack but the
photograph cannot resolve it — it looks like ₹280 and will not be guessed. It is
the only product still tagged `needs-price`.

**The physical packs still print nothing.** Quantity and price now exist on the
listing, but the tubs and bags he ships carry a name sticker at most. As packer
that declaration belongs on the pack too.

- **Consumer care email is `drjhrnd5@gmail.com`** — supplied 16 Sep. It is not
  printed on any pack in the catalogue, his own included, so it could never have
  been transcribed. It is now on all 63 rows: as the **packer's** email on his own
  repacked goods, and as the **seller's** contact on goods he resells. The one
  maker that prints its own (Shree Durga) keeps it. Lives in
  `SELLER_CARE_EMAIL` in `scripts/build_catalogue.py`.

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

- **Claude cannot use a Shopify collaborator code** — no browser, no Partner
  account. **Superseded 16 Sep: a Shopify MCP connector is live**, giving direct
  Admin API access (GraphQL query + mutation, products, collections, orders,
  analytics). Store confirmed as `8uysc8-kx.myshopify.com`, **Basic**, INR, IST,
  India, owner email `drjhrnd5@gmail.com`.
- **The connector cannot upload images.** Both `create-product` and
  `ProductSet.files` need a **publicly reachable HTTPS URL**; the 66 pack
  photographs are local PNGs. Either Jnanottam uploads them to Shopify Files by
  hand, or we go via `stagedUploadsCreate` and POST each file to the staged
  target from bash. The staged-upload route is untested here — try it before
  asking him to upload 66 files.
- **`build_shopify_import.py` had two image bugs**, both caught by the
  two-product test import on 16 Sep — which is exactly the gate that test exists
  for. It split image lists on `;` only while the working sheet writes commas, so
  every image after the first was silently dropped; and it never wrote
  `Variant Image`, so all pack sizes shared one photograph. On a store whose
  whole premise is that the listing matches the label, a customer buying the 1 kg
  seeing the 250 g pack is a real defect, not a cosmetic one. Both fixed, and
  `Variant Image` is now in the column list.

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

**Storefront copy rewritten 16 Sep.** `storefront-design.html` used to tell an
invented single-estate coffee story. Every claim is now traceable to a pack or to
the store. Three things it had that were worse than fiction:

- **A fake FSSAI number**, `10024000000000`, printed twice. Real: `21223055000121`.
- **A fake entity and address** — "Dhanush Estate Foods, Chikkamagaluru 577117".
- **The Kannada wordmark was not Kannada.** It was Malayalam plus one Sinhala
  letter (`&#3374;&#3378;&#3398;&#3240;&#3390;&#3465;`) set in Noto Serif Kannada.
  Now `&#3246;&#3250;&#3270;&#3240;&#3262;&#3233;&#3265;` = **ಮಲೆನಾಡು**. A Kannada
  shop showing Malayalam is the kind of thing a local customer notices instantly.

Also gone: invented elevation and harvest figures, arabica/robusta/peaberry,
wild forest honey (no honey in the catalogue at all), gift boxes, grind
selectors, a "40 in stock" line for a pack-to-order business, and struck-through
compare-at prices implying discounts that do not exist.

**The product page now demonstrates the gap treatment.** It renders Malnad Chai
500 g with eight real declarations and two marked *"Not printed on this pack"* in
laterite — because that pack genuinely carries no best-before or ingredients
list. That is the behaviour the theme has to reproduce; a design that only ever
shows a perfect product teaches the wrong thing.

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

### Stage 1 — CATALOGUE IS LIVE IN THE STORE (16 Sep)

**All 57 products created, 63 variants, 70 pack photographs, every one DRAFT.**
Verified by reading the store back, not by trusting the writes:

| Check | Result |
|---|---|
| Products | 57, all `DRAFT` |
| Media | every image `READY`, **zero** `mediaErrors` |
| Variant images | every variant carries its **own** pack photo |
| Inventory | `tracked: false`, policy `CONTINUE` on all 63 |
| Selling price | `0.00` everywhere, tagged `needs-price` |

**Images went in by URL, not upload.** The connector cannot upload a file, but
`ProductSet.files.originalSource` accepts a public HTTPS URL, and this repo is
public — so Shopify fetched all 70 straight off `raw.githubusercontent.com` and
copied them to its own CDN. The GitHub URL is only needed during the import.
`scripts/build_productset_jsonl.py` generates the payloads.

**`bulkOperationRunMutation` is blocked** by the connector's safety policy
(it can run arbitrary mutations). So imports go as batched aliased `productSet`
calls, ~9 products each, not as one bulk job.

**The `DO-NOT-PUBLISH` block was lifted by Jnanottam on 16 Sep** — *"publish the
do not publish too / its verified shi"*. Tags removed from QTF Tea and Nanjangud
Suruchi's Diabeat; they are now treated like any other product. **His call, made
with the findings in front of him — do not re-apply the tag.** The findings
themselves are unchanged and stay on record in `catalogue/gaps.md`: QTF prints no
net quantity, MRP, FSSAI or packing date, and the Diabeat front label names a
condition and prints a dosage.

Two things did not change with that decision:
- **Our listing copy stays neutral.** Diabeat reads "Herbal decoction." and QTF
  reads "Tea from Guard-Hitlow Tea Factory, Koppa." Neither repeats a claim. The
  Diabeat claim is legible in the pack **photograph**, not in anything we wrote.
- **The actual publish is still pending.** Setting them ACTIVE was refused by the
  sandbox as a real-world transaction, and every variant in the store is still
  **₹0.00**, so publishing anything today makes it orderable for free.

### Earlier gate — PASSED 16 Sep

- **19 metafield definitions created** under namespace `compliance` — 15 on
  PRODUCT, 4 on PRODUCTVARIANT. Verified back: correct types, and
  `access.storefront = PUBLIC_READ` on every one, which is the setting that
  silently breaks the theme if missed.
- **Two test products created as DRAFT**, proving both paths:
  - `Malnad Chai - Premium Malnad Tea Powder` — 3 variants, each carrying its own
    `net_quantity`, MRP 150 / 220 / **empty on the 1 kg** (correct, that pack
    prints none).
  - `Ghani-Pressed Copra Coconut Oil` — single variant, all four variant
    metafields set.
  - Both: `status DRAFT`, `inventoryItem.tracked = false`,
    `inventoryPolicy = CONTINUE` — buyable, packed to order, as instructed.
- **Selling price is `0.00` on every variant, deliberately.** No price list has
  arrived and a selling price is not something to invent. They are draft, so
  nothing is purchasable. Tagged `needs-price`.
- Products carry no images yet — see the connector limitation above.


**Stage 0 — Shopify is ready (16 Sep). Razorpay is not: KYC is not done.**

### Razorpay KYC — verified, do not regress

- **Video KYC is between the client and a Razorpay officer.** Jnanottam is not on
  that call and does not need to be in the room. RBI's V-CIP exists so the
  customer does *not* travel, and since May 2021 it covers proprietors and
  authorised signatories. Distance is not the blocker it looked like.
- **It cannot be delegated.** The client's face, his PAN, his Aadhaar, geotagged
  inside India. Someone local may hold the phone; nobody may answer for him.
- **Never put the merchant account in Jnanottam's or JTACS's name.** Settlement
  must land in the client's bank and he holds the FSSAI licence. Running a
  payment account for another party's business is a compliance breach.
- **Switching gateway does not dodge it.** V-CIP is an RBI requirement on every
  payment aggregator — Cashfree, PayU, Instamojo, PhonePe all run it.
- **Test mode needs no KYC.** `rzp_test_` keys are issued immediately on signup,
  so the entire test-mode half of Stage 3 can run before KYC clears.

Playbook, pre-flight checklist and the batched-visit proposal: `docs/razorpay-kyc.md`.

**Stage 1 — the sheet is built, with gaps.** Per his instruction *"leave gaps for
all the info u dont have and continue with what u have"*, the working catalogue
now exists: `catalogue/malnad-catalogue.csv`, **57 products / 63 variant rows**,
generated by `scripts/build_catalogue.py` from the pack transcriptions. Every
value in it was read off a photograph or off the catalogue name; every unknown is
**empty**, never guessed. Re-run the script after any client answer.

65 catalogue files became 57 products: clove and lavanga are the same whole
cloves, the black and red Sanjivni are one 1 kg tea, and instant coffee, filter
coffee, nice coffee, Malnad Chai and the Aaradhya oil group into variants.

The pipeline runs end to end — sheet → validator → Shopify import CSV, all
draft. **484 gaps remain**, reported in `catalogue/gaps.md`.

Blocking the first import, in order:
1. **The price list** — 63 selling prices and 49 MRPs. Requested.
2. **HSN and GST** — blank on all 63 rows by design. Proposals ready for his
   sign-off in `catalogue/tax-schedule.md`.
3. **Back-of-pack photos for the nine syrups and squashes** — the makers are
   named on the front, but address, FSSAI, MRP and dates are all on the back and
   we have no back photographs.
4. **Net quantity for 9 products** — the bare tubs and bags. Plus a sharper
   nellikai label. Asked in `catalogue/pack-size-request.txt`.
5. **Date of packing** — he packs to order, so no single date belongs in a
   catalogue. Needs a decision: apply it to the label at dispatch and show the
   listing as packed-to-order.
7. ~~Storefront copy written for the wrong business~~ — **rewritten 16 Sep.**

### Two products cannot be listed as photographed

- **QTF Tea** — quantity now confirmed at **1 kg** by the client, but the sack
  still prints no MRP, no FSSAI number and no packing date. Its printed face
  carries only the factory name and address, which is why it reads as trade
  packaging. Needs: the price, the FSSAI number, and a photograph of any other
  face of the sack in case a label is elsewhere on it.
- **Nanjangud Suruchi's Diabeat** — the front label calls it a *proprietory
  preparation*, says it is *very much useful for diabetic patients*, and prints a
  **dosage**: *take 30 ml twice before food*. A named condition plus a dose is
  how a food stops being a food. This is the most serious item in the catalogue
  and needs a decision before it goes anywhere near the site.

Also new: the banana stem squash photograph shows **two** bottles, a regular and
a **Sugarless**, where the catalogue listed one. Asked.

### Store readiness check — 16 Sep

What is actually in the store, read from the Admin API, not assumed:

| | State |
|---|---|
| Theme | **Horizon, stock and untouched.** Our design has **not** been built into it |
| Shop name | **"My Store"** — never renamed |
| Active products | **0.** All 57 are draft |
| Prices | ₹0.00 on all 63 variants |
| Payments | none — Razorpay KYC not done |
| Policies | refund / privacy / terms **not written**. Razorpay requires these published before it will activate |
| Ships to | **29 countries** by default, including Japan, Norway and the US. He delivers from Horanadu — needs restricting to India |
| Billing address | correct: Malnad Spices, Horanadu, Chikmagalur 577181, +91 8431218956 |

**`storefront-design.html` is a mockup, not the site.** It is a static HTML
design for approval. Building it into the Horizon theme is Stage 2 and has not
been started.

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
| `storefront-design.html` | Storefront design mockup — copy rewritten and **images placed** 16 Sep. Artifact: `claude.ai/artifact/GJkBLz3cJ2bUfWKeP2j5X4` |
| `Malnad-Spices-Storefront-Design.pdf` | The same, 2 pages, for sending to the client on WhatsApp |
| `scripts/build_catalogue.py` | **Builds the working sheet** from the pack transcriptions; also emits `gaps.md` and `tax-schedule.md` |
| `scripts/validate_catalogue.py` | Blocks incomplete or illegal product data |
| `scripts/build_shopify_import.py` | Catalogue → Shopify import CSV, all draft |
| `scripts/audit_live_products.py` | Finds live products missing declarations |
| `docs/stage1-catalogue.md` | Metafield definitions and import procedure |
| `docs/product-photography.md` | Storefront palette and image direction |
| `docs/image-prompts.txt` | The three prompts, plain text |
| `catalogue/intake.md` | Intake log, 65 products, findings |
| `catalogue/extracted.md` | Everything read off the packs — brands, MRPs, findings |
| `catalogue/malnad-catalogue.csv` | **The working sheet** — 57 products, 63 rows, gaps left empty |
| `catalogue/gaps.md` | Generated: every outstanding field and who supplies it |
| `catalogue/tax-schedule.md` | Generated: proposed HSN and GST per product, for sign-off |
| `catalogue/quantities.md` | Net quantity for all 65, from the catalogue names |
| `catalogue/client-message.txt` | Sent: the information-gap list |
| `catalogue/price-list-request.txt` | Drafted: the price-list request |
| `catalogue/pack-size-request.txt` | Drafted: pack sizes for the 9 unlabelled lines |
| `templates/catalogue-template.csv` | Now Claude's working format, not a client form |
| `build-plan.html`, `quotation.html` | **Superseded.** Custom build, and the earlier Ayurveda quotation. |

### Storefront imagery — placed 16 Sep

Real pack photographs are in the product cards, the product page gallery and two
category slots; the brand images cover the hero, the story band and the other two
categories. All embedded as **JPEG data URIs sized to the slot** — the artifact
CSP blocks external images, so they must travel with the page. Total 1.4 MB.

**A pre-existing CSS bug was hiding the hero media entirely.** `.ph{position:relative}`
is declared *after* `.hero-media{position:absolute; inset:0}`, same specificity, so
it won and the media box collapsed to zero height. Nothing had ever rendered in it —
not the image, not the botanical decoration it replaced. Fixed by raising the
selector to `section.hero .hero-media`. Watch for the same trap on any `.ph` element
that needs its own positioning.

**Still needed:** two atmospheric category images (Oils & Syrups, Dry Fruits &
Seeds) — pack shots are standing in and clash with the nature shots beside them —
and an upscale of `hero-canopy.png` before launch. `cat-honey-comb.png` and
`packs-three-up.png` are orphaned: there is no honey and no gift category.

## Storefront palette

`#F4F2ED` paper · `#FFFFFF` card · `#1F4034` canopy green (brand) ·
`#A4552F` laterite (accent only) · `#2A2D27` ink · `#6E7268` muted.
Mood: shade-grown, monsoon, unhurried. Not warm cream and hessian.

## Commands

```sh
python3 scripts/build_catalogue.py                      # regenerate the sheet
python3 scripts/validate_catalogue.py   <sheet.csv>
python3 scripts/build_shopify_import.py <sheet.csv> build/shopify-import.csv
python3 scripts/audit_live_products.py  <products_export.csv>
```

PDFs are rendered with headless Chromium — see the README for the command.

**Rendering the storefront mockup to PDF.** Headless Chromium's `--screenshot`
captures the *window*, not the full page, and `--print-to-pdf` paginates the two
screens into six awkward pages. What works: split the HTML at the second
`<p class="screen-tag">` into two standalone files sharing the `<style>` and the
SVG symbol, render each at `--window-size=1440,6500`, measure the real content
height by scanning up from the bottom for the first row that differs from the
page ground, then build a PDF with one page cropped to each. One page per
screen, no cuts.
