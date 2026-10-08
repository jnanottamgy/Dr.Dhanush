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
- **Dheeraj** — **Dhanush's brother, and the one who actually runs the business.**
  The Razorpay merchant account is in his name and greets him by it. Asked and
  answered 17 Sep: *"dheeraj is dhanush brother / he runs the business / everything
  is legit."* **Settled — do not re-raise it.** The name on the Razorpay account
  not matching the name on the quotation is expected, not a finding.

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
- **If the pack does not disclose it, the listing does not mention it at all.**
  Client instruction 16 Sep: *"if that information is not provided in the product
  then dont add that information in the site, just dont mention it... everything
  is obtained, everything is legal, they are just not ready to disclose it."*
  So the **"Not printed on this pack" treatment is retired** — an empty row is
  simply left out. This does **not** loosen the rule above it: nothing is
  invented, ever. It only changes what we do about a blank, from announcing it to
  staying quiet about it. The mechanism survives behind `show_gaps` in the
  declarations block, **off by default**.
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
  hair-care lines: separate storefront section, and their HSN codes (3401,
  3305, 1404) do not sit with the food ones. The client has since put all three
  at 5% along with everything else — recorded, and the validator warns on the
  two powders.
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
- **New domain, 16 Sep: he intends to buy `malnadproducts.in`** and connect it.
  **There is no domain mutation in the Admin API** — only `urlRedirect*`, which
  is in-store redirects, not DNS. Connecting a domain is Shopify admin plus
  registrar DNS, entirely manual.
  **Raised with him:** the packs print `malnadspices.in`, and the FSSAI licence
  and the packer name are both **MALNAD SPICES**, while the shop is now named
  *Malnad Products* and the new domain would be `malnadproducts.in`. A customer
  holding a pack will type the printed address. `malnadspices.in` should be added
  to the same store as a second domain so it redirects, whichever one ends up
  primary. Awaiting his call on which is primary.
### Pack sizes and prices — supplied 16 Sep

| Product | Net quantity | Price |
|---|---|---|
| Chia · Sabja · Flax · Magaz · Pumpkin · Sunflower seeds | 150 g each | ₹140 each |
| Soapnut, whole | 150 g | ₹140 |
| Dates | 500 g | ₹150 |
| Special Dates | 500 g | ₹200 |
| Pista | 500 g (was on the pack) | ₹900 |
| Hayat raisins | 500 g (was on the pack) | ₹300 |
| QTF Tea | **1 kg — confirmed** | **₹250 per kg** |
| Nellikai powder | 200 g | **₹200** |

**Net quantity is complete: all 63 variants have one.**

### Prices — COMPLETE 16 Sep. All 63 variants priced, nothing at zero.

*"selling prices are as mentioned above in the packs itself."* Where a pack
prints an MRP that figure is both the MRP and the selling price; no compare-at is
ever written, because there is no discount to show.

The 36 that printed nothing were supplied by the client in two batches on 16 Sep
and are all in. **`needs-price` is gone from every product**, verified by reading
all 63 variants back.

Prices live in **`PRICES_16SEP`** in `scripts/build_catalogue.py`, keyed
`(product name, pack size)` — a client answer is one edit there, not 27 scattered
through the product definitions.

**Whether a price also becomes the declared MRP depends on who packs it**, and
that is enforced by the **`RESOLD_NO_MRP`** set in the same file:

- **His own packs** — the 17 whole spices, both Swad coffees, Malnad Chai 1 kg,
  Badam — print no MRP, and as packer his number **is** the MRP. Both set.
- **Goods he only resells** — Sanjivni, Aaradhya x2, Kalpatharu and **all nine
  syrups** — are sealed by their own maker. Selling price set, **MRP left
  undeclared**. Kalpatharu's is printed but smudged; the syrup labels carry an
  `M.R.P. ₹ (Incl. of all taxes)` box the maker left blank. Either way the
  declaration is theirs to make. Putting our own figure on somebody else's sealed
  pack would be a misdeclaration, and if the real printed figure were lower,
  selling above it is an offence.

Same reasoning already applied to QTF and nellikai powder, which are third-party
and carry a price with no MRP.

**One thing flagged to him, not an error:** Malnad Chai runs ₹600/kg at 250 g,
₹440/kg at 500 g and ₹300/kg at 1 kg, so two 500 g packs cost ₹440 against ₹300
for the kilo. Coherent with Sanjivni at ₹270/kg and QTF at ₹250/kg — the kilos are
a bulk band and the small packs carry retail margin — but the 500 g is dominated
by the 1 kg for anyone paying attention.

### Prices are GST-inclusive — confirmed by the client 16 Sep

*"all the prices mentioned above are all inclusive of gst."* The store was
already set up that way and was verified, not assumed:
`shop.taxesIncluded = true`, `taxable = true` on all 63 variants, so Shopify
works GST **out of** the price for the invoice and adds nothing at checkout. The
terms and the declarations panel both already say so. **Nothing needed changing.**

Two consequences worth keeping in view:

- **`taxShipping` is `false`.** Delivery is currently treated as carrying no GST.
  Under GST, delivery charged on a taxable supply is normally a composite supply
  taxed at the principal rate — so this may want to be `true`. Because prices are
  tax-inclusive, switching it would **not** change what the customer pays; it
  changes how the invoice apportions the tax. Jnanottam is the CA; his call.
- **The `compliance.gst_rate` metafield does not drive checkout tax.** It is our
  own field, for display and for the accountant. Shopify calculates tax from
  **Settings → Taxes and duties**, not from a metafield. So "inclusive of GST"
  only produces a correct invoice once the real rates are configured there. The
  nine category collections were the natural vehicle for per-collection
  overrides, but **that is no longer needed** — the client answered a flat 5%
  across the catalogue, so it is one India-wide rate.

### GST — COMPLETE 16 Sep. 5% on all 57, HSN on all 57.

Dr. Dhanush answered on WhatsApp: *"All meterials r 5%"*, split
*"2 1/2 cgst and 2 1/2 sgst"*, and to the instant-coffee follow-up,
*"Same sir"*. Also *"Coconut oil is for both"* — cooking and hair — which
settles that question and leaves the descriptions as written.

**Applied everywhere and verified.** `proposed_gst="5"` on every product in
`scripts/build_catalogue.py`; all 63 catalogue rows carry a rate and an HSN
code, none blank; `compliance.gst_rate = 5.0` and `compliance.hsn_code` pushed
to all 57 products in Shopify and read back product by product. **Instant
coffee's 18% is reversed.** The 5%-vs-12% masala question is answered 5%, and
they sit at HSN **0910** (mixtures of spices), which is the heading that agrees
with 5% — 2103 at 12% was the competing reading.

**Twelve products sit in headings that normally carry more than 5%**, and the
validator now warns on each: instant coffee at **2101**, the **nine syrups** at
2106, and the two hair powders at **3401** and **3305**. The rate is his and it
stands; the mismatch is recorded, not reconciled behind his back. Full reasoning
in `docs/gst-classification.md`. The two I would put back to him in writing are
instant coffee and the nine syrups.

**Open, and only Jnanottam can close it: Shopify's own tax settings.**
`compliance.gst_rate` is our field, for the accountant — Shopify taxes from
**Settings → Taxes and duties**, which is still on the default. One flat India
rate of 5% now that the whole catalogue is one rate. Same screen carries the
`taxShipping` checkbox, still `false`.

**One unresolved classification question**, if he wants it settled: none of the
six masala packs prints an ingredients list, so 0910 vs 2103 cannot be decided
from the photographs. One question — what goes into the bisibele bath and
puliyogare powders besides spices — decides all six.

### Syrup back labels — not required, client's call 16 Sep

He does not want them chased. Consequence, recorded once: those nine listings
carry no packer address, no FSSAI number and no packing date, because those live
on back labels we will not photograph. Their makers are named from the fronts.

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
| **Razorpay Magic Checkout** | **THE RATE IN THIS ROW IS WRONG — corrected 8 Oct, see "Magic's 0.5% is additive" below.** Magic Checkout's fee is **0.5% + 18% GST ON TOP OF** the normal transaction fee, not ~0.65% instead of it (Razorpay support, in writing). The decision survives only if Shopify's own 2% genuinely disappears on a Magic-completed order, which is unconfirmed. Original reasoning kept for the record: Shopify adds 2% on Basic because Shopify Payments is unavailable in India. Magic Checkout is ~0.65% and currently falls outside that fee. Saves ~₹28,700/year. Flagged to the client as a gap in Shopify's rules, not a guarantee. **Re-confirmed by Jnanottam 17 Sep** — *"lets go with magic checkout"* — after being shown the comparison and the caveats, including that Magic's headline feature is COD and this store is prepaid only, so the purchase is the fee gap plus one-click address, not the product's main draw. |
| **Prepaid only** | Client instruction. Also removes COD refusal losses entirely. |
| **WhatsApp community on the free Business App** | Communities only exist on the Business App; the API cannot run one, and a number moved to the API loses Communities permanently. API is priced as a separate optional upgrade, triggered by the 256-contact broadcast cap. |
| **Owner dashboard included at no charge** | Listed at ₹8,000 then discounted to zero, so the client sees the value. Total stays ₹38,000. |
| **Offline sales as real Shopify draft orders** | Not a dashboard field. This way stock decrements, a GST invoice is raised, and the website cannot sell what was already sold at the estate gate. Draft orders work on Basic and on the Shopify phone app. |
| **Dashboard reads the Admin API, read-only** | Scopes `read_orders`, `read_products`, `read_customers` only. No write scope, no payout scope. Free on Basic. |
| **DECIDED 8 Oct — the dashboard is PARKED, not built** | Jnanottam's call, closing the question below after three weeks: hand over without it. Shopify's own admin and phone app already cover orders, money, packing slips and fulfilment, and the owner's manual is written around them, so nothing is left without a tool. **Say it plainly at handover**: the dashboard comes after launch, once Dhanush knows what he actually wants to see. The price does not change — it was listed at ₹8,000 and discounted to zero, so parking it costs the client nothing. **Do not re-raise the read-vs-write question**; it is moot until the dashboard is revived. With this parked, the **WhatsApp Business community is the only unstarted build item in scope.** |
| **~~OPEN 16 Sep — dashboard write access~~ — superseded by the row above** | Jnanottam asked whether the dashboard can add products, remove products and enter tracking numbers. All three are possible, but they need write scopes, which reverses the read-only decision above and the promise in `build-runbook.html` Stage 4. Recommended split: **tracking entry yes** (`write_fulfillments` only, genuinely repetitive, low blast radius); **product add/remove via Shopify's own free admin app**, unless it is built as a guided form that enforces the `compliance` metafields, the category tag and the `Malnad delivery` profile — a naive add-product form would silently create products with no declarations and no shipping. Awaiting his call. |
| **Metafields: some on variant, not product** | Net quantity, MRP, manufacture date and best before differ between a 250 g and a 1 kg pack. Putting them on the product is how a store ends up declaring the wrong net quantity. |
| **MRP ≠ compare-at price** | Compare-at is a marketing field; MRP is a legal declaration. MRP lives in its own metafield always; compare-at is written only where the selling price is genuinely lower. |
| **Enhance images, never generate** | Image-to-image only. A redrawn label misrepresents a food product. Test: customer holds pack beside photo, they match. |

## Corrections already made — do not regress

- **Claude cannot use a Shopify collaborator code** — no browser, no Partner
  account. **Superseded 16 Sep: a Shopify MCP connector is live**, giving direct
  Admin API access (GraphQL query + mutation, products, collections, orders,
  analytics). Store confirmed as `8uysc8-kx.myshopify.com`, **Basic**, INR, IST,
  India, owner email `drjhrnd5@gmail.com`.
- ~~**The connector cannot upload images.**~~ **Superseded 16 Sep: it can.**
  `fileCreate` takes `originalSource` as a **public HTTPS URL**, so the four
  brand images went straight into Shopify Files off `raw.githubusercontent.com`
  and came back `READY` with their filenames intact. `stagedUploadsCreate` was
  never needed and remains untried. Anything in this repo can be put in Files
  this way; only video and 3D models genuinely require a staged upload.
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

~~**The product page demonstrates the gap treatment.**~~ **Superseded 16 Sep.**
The mockup still shows two rows marked *"Not printed on this pack"* in laterite.
The live theme no longer does — those rows are omitted entirely, on the client's
instruction. `storefront-design.html` has not been updated to match and is now
out of step with the theme on this one point.

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

### Connector scopes — checked, do not guess at these

Read from `currentAppInstallation { accessScopes }`, so this is the real list,
not inference from a failed call.

**Has:** `write_products` · `write_themes` · `write_files` · `write_content`
(pages, blogs) · `write_online_store_navigation` (menus) · `write_shipping` ·
`write_publications` · `write_markets` · `write_discounts` · `write_draft_orders`
· `write_inventory` · `write_translations` · `write_metaobjects`.

**Does not have:** `write_legal_policies`. It holds `read_legal_policies` only,
so **store policies cannot be published from here** — they are written in
`policies/` and pasted by hand. Re-confirmed 17 Sep by actually calling
`shopPolicyUpdate`, which returns *"Access denied ... Required access:
`write_legal_policies` access scope."* Not inferred.

### POLICIES ARE FIXED — verified 6 Oct by reading `shopPolicies { body }`

All six now store as real markup — `<p dir="ltr"><strong>…` — with **no `&lt;`
anywhere**. Contact, Legal notice, Refund, Shipping, Terms and Privacy all render
properly on the storefront. Jnanottam redid them. **This closes the longest-running
manual defect in the project** and removes the most likely cause of a Razorpay
website-review rejection. Do not re-raise it. The history below is kept only so the
cause is not repeated on any future paste.

**STATE READ THE SAME DAY:** shop `Malnad Products` at `https://malnadproducts.in`
with SSL · **57 products** · live theme still `Malnad Spices — build`,
`config/settings_data.json` unchanged at 8,082 bytes / `c6b03740…` so the Magic
embed is **still enabled** · **orders still 1** — #1001, 28 Sep, `test: true`,
gateway `01 Cards, UPI, NB, Wallets by Razorpay`. **No live order has ever been
taken, so payments never went live.**

---

**All five pasted policies went in ESCAPED — 17 Sep. FIXED, see above.** Jnanottam pasted them and
every one stored as `&lt;h2&gt;...` rather than markup, so the storefront shows
the raw tags as text. The refund one is worse: wrapped in `<pre>`, so it renders
as a monospace code block. Cause: the policy editor's rich-text view escapes
anything pasted into it, and copying out of a chat fenced code block can also
carry code-block formatting in. **The `<>` (Show HTML) toggle must be clicked
BEFORE pasting**, and the box must be emptied first, or the old escaped text
stays. Only `PRIVACY_POLICY` is correct, because it is Shopify's own and was
never touched — and it now correctly interpolates *Malnad Products*, the real
phone and the real email. **I cannot fix this; it is his to redo.** Verify by
reading `shopPolicies { body }` back and looking for `&lt;`.

**~~`deliveryProfileUpdate` cannot touch zones at all.~~ WRONG — CORRECTED
7 Oct. It works, and the default profile IS fixable from the API.** The earlier
attempt must have put `zonesToCreate` at the top level of `DeliveryProfileInput`,
where it does not exist. **Zones go inside `locationGroupsToUpdate`**, keyed by
the location group id:

    deliveryProfileUpdate(id: <profileId>, profile: {
      locationGroupsToUpdate: [{
        id: <locationGroupId>,
        zonesToCreate: [{ name, countries: [{code: IN, provinces: [{code}]}],
                          methodDefinitionsToCreate: [{ name, active,
                            rateDefinition: { price: { amount, currencyCode } },
                            weightConditionsToCreate: [
                              { criteria: {unit: KILOGRAMS, value}, operator: GREATER_THAN_OR_EQUAL_TO },
                              { criteria: {unit: KILOGRAMS, value}, operator: LESS_THAN_OR_EQUAL_TO }] }] }] }] })

Confirmed field names, read from the schema rather than guessed:
`DeliveryLocationGroupZoneInput` = countries · id · methodDefinitionsToCreate ·
methodDefinitionsToUpdate · name. `DeliveryMethodDefinitionInput` = active ·
conditionsToUpdate · description · id · name · participant ·
priceConditionsToCreate · **rateDefinition** · **weightConditionsToCreate**.
Shopify recommends **no more than 5 zones per request**; one zone per call is
safest and makes a failure traceable.

**THE DEFAULT-PROFILE LANDMINE IS FIXED — 7 Oct.** `General profile`
(`DeliveryProfile/96993116273`, location group `97908949105`) had **zero zones**,
so any product added after handover would have landed there with **no delivery
option at checkout** — unbuyable, no error shown. It now carries all four zones
and **28 rates**, identical to `Malnad delivery`: Karnataka 1 province,
South and West India 7, Rest of India 17, North East and islands 12, each with
the same 7 weight bands. **Verified by reading the profile back**, not by trusting
`userErrors: []`.

**Shopify's India province codes are not ISO 3166-2:IN**, and a zone containing
a bad code is accepted, silently drops that province, and reports no error — so
four states went missing on the first build. Probed and confirmed:
**CG** Chhattisgarh (not CT) · **TS** Telangana (not TG) · **UK** Uttarakhand
(not UT) · **DN** Dadra and Nagar Haveli and **DD** Daman and Diu, still listed
separately · **OR** Odisha (not OD). 37 entries cover all 36 states and UTs.

**There is no Admin API mutation for the shop name.** Confirmed against the full
`Mutation` field list, not inferred: the only `shop*` mutations are
`shopLocaleEnable/Disable/Update`, `shopPolicyUpdate` and
`shopResourceFeedbackCreate`. Renaming is admin-only on every plan.

**Done 16 Sep: the shop is renamed — it is now `Malnad Products`**, not
"My Store". Note it does **not** match the packer name printed on the packs and
on the FSSAI licence, which is **MALNAD SPICES**. Raised with Jnanottam once;
his call, not a blocker.

**Also fixed by the shipping rebuild: "मानक" is gone.** It lived on the deleted
Domestic zone's method. Every method in `Malnad delivery` is named
**Standard delivery**. Do not carry the old finding forward.

**Checkout branding is Plus-only.** `checkoutBrandingUpsert` is refused on Basic:
*"the shop must be on a Plus plan or a Development store plan"*. Do not retry it,
and do not promise the client a styled Shopify checkout on this plan. It does not
matter much in practice — Razorpay Magic Checkout replaces that page, and it is
brandable on Razorpay's side.

**Only `en` is installed** and it is primary and published, so the Hindi shipping
method name **"मानक"** is not a translation — it is the stored name on the method
definition, set by Shopify's India onboarding. The translations API is not a
route to fixing it.

### Product descriptions — written 16 Sep

All **57 rewritten** from one-line stubs (*"Whole black pepper."*) to real copy,
on his instruction to *"put flattery description for all products... shld be
accurate"*. Source of truth is **`catalogue/descriptions.py`**, not the store, so
they are version-controlled and re-pushable. Pushed and verified by reading all
57 back and matching them against the file.

Two rules held throughout, and worth keeping:

- **No health claims.** Nothing about immunity, cholesterol, omega-3,
  antioxidants or any named condition. A regex check over the file enforces it.
  **Diabeat reads only "A herbal decoction from Nanjangud Suruchi's, Nanjangud.
  Supplied as bottled by the maker."** — its own label makes a claim; we do not
  repeat it. The unresolved question about that product is unchanged.
- **No invented botany.** `Kalhoo`, `Mintiya`, `Palavele` and `Naga Kesari` are
  genuinely local and their botanical identity could not be confirmed, so they
  are described as what is certain — a Malnad spice used in local blends — rather
  than given a plausible-sounding identity. Marati moggu is named as kapok buds
  because that one is well established.

The three home-care lines each end **"Not a food."**, which is a safety line, not
a disclosure.

### Shipping — weight-based, rebuilt 16 Sep

The client ships by India Post and general courier from Horanadu, priced **by
distance and per kilo**. A flat rate cannot express that, so the ₹379 placeholder
is gone and the real shape is built.

**Profile `Malnad delivery`**, `gid://shopify/DeliveryProfile/97018216561` —
4 zones x 7 weight bands = **28 rates**, all active, **63 of 63 variants
associated**, verified by reading it back.

| Zone | Provinces |
|---|---|
| Karnataka | 1 |
| South and West India | 7 |
| Rest of India | 17 |
| North East and islands | 12 |

**Every variant already had a shipping weight**, set at import from net quantity
plus a packing allowance (100 g pack → 140 g, 700 ml syrup → 1,025 g, 1 l oil →
1,150 g). That is why weight-based rates worked immediately. Note the
distinction: the Shopify `weight` field is **logistics**, used only to price
postage; net quantity is the **legal declaration** and lives untouched in the
`compliance` metafields. Setting one from the other is not inventing a
declaration.

**The rate table is generated, not typed.** `scripts/build_shipping_rates.py`
builds all 28 from **eight numbers** — a base and a per-kg figure per zone.
The numbers currently in the store are a plausible shape, **not quoted
tariffs**; regenerate from the client's real rate card. Bands charge at their
**top** weight on purpose: under-recovering postage is invisible until the
month's accounts.

**~~Known trap: the default General profile has no zones.~~ FIXED 7 Oct** —
all four zones and 28 rates added to `General profile` through
`deliveryProfileUpdate` → `locationGroupsToUpdate` → `zonesToCreate`, verified by
reading back. A product added later now gets correct weight-based delivery. See
the corrected API note in the connector-scopes section.

**Origin does not need modelling — client answer 16 Sep.** Asked whether
dispatching from Horanadu or from Kalasa changes the charge: *"5rs + -"*. About
five rupees either way, so a single origin is correct and a second location
group would be false precision. The existing rounding already absorbs it: rates
round **up** to the nearest ₹5 and each band charges at its **top** weight.

**CLOSED 28 Sep — the rates stand as built.** Jnanottam: *"use the old price we
decided."* The 28 generated rates are now the shipping prices, not a placeholder.
He was told three times that they are a plausible shape rather than quoted
tariffs; this is his decision with that in front of him. **Do not re-raise it.**
If a real rate card ever arrives, `scripts/build_shipping_rates.py` still
regenerates all 28 from eight numbers.

### Stage 2 — STOREFRONT BUILT (16 Sep)

Everything that does not depend on Razorpay is done. The manual remainder, and
who owns each item, is in **`docs/store-setup.md`**.

| Built | State |
|---|---|
| Collections | **9 smart collections**, tag-driven. 17+7+3+3+3+9+6+6+3 = **57, every product in exactly one** |
| Homepage | hero · promise · categories · featured · story |
| Footer | trading name, address, both phones, care email, FSSAI number; policy list; fake socials removed |
| Menus | main menu with a 9-collection Shop dropdown; footer menu |
| Pages | **About us** written; the stock empty **Contact** filled in |
| Shipping | **ships to India only** — the 28-country international zone is deleted |
| Files | 4 brand images in Shopify Files, all `READY` |
| Collection art | nature shots on Whole Spices and Coffee; the rest fall back to a pack photo |

**Four brand sections, written rather than bent out of Horizon's.** Horizon's
`hero` and `collection-list` schemas are 45KB and 26KB; guessing setting names
out of them produces a section that renders empty with no error. These are small,
match the approved design, and stay editable in the theme editor:
`malnad-hero`, `malnad-promise`, `malnad-categories`, `malnad-story`. All four
parse under python-liquid. The featured row reuses Horizon's own `product-list`
settings lifted verbatim from its default `index.json`, not reconstructed.

**`needs-price` is a true worklist again.** It was stale on 13 products that had
since been priced — 46 tagged where only 33 have a ₹0 variant. Corrected, and
re-verified by reading each record rather than the tag search, which lags.
Confirmed against prices: **36 variants across 33 products are still ₹0.00**,
which matches what this file already said.

**Two defects found in Shopify's own defaults, both fixed:**
- Horizon's footer shipped with social links pointing at `facebook.com`,
  `instagram.com`, `x.com` — the platforms' front doors, not the shop's. Removed.
- The India shipping rate is a flat **₹379** placeholder. Six of the seeds sell
  at ₹140. Left as found because the real rate is the client's, but it is the
  most commercially dangerous setting in the store and is flagged first in
  `docs/store-setup.md`.

**An empty-string schema default makes `themeFilesUpsert` reject the whole file,
silently.** `"type": "textarea", "default": ""` in a block's `{% schema %}` was
enough: the upsert returned `userErrors: []` twice, the file simply did not
change, and GitHub was serving the correct content the whole time. Omit the
`default` key instead of setting it empty. **Always verify a theme write by
checksum** — a clean mutation response means nothing here.

**Shopify normalises JSON on write.** `templates/index.json` went up at 11,364
bytes and is stored as 6,859; `config/settings_data.json` likewise. Nothing was
dropped — verified by reading both back in full. Only `.liquid` files match by
checksum; verify JSON templates by reading the values.

### Stage 2 — THEME BUILD STARTED (16 Sep)

Working theme: **`Malnad Spices — build`**,
`gid://shopify/OnlineStoreTheme/146238865521`, **UNPUBLISHED**, duplicated from
Horizon. The live theme is never written to — the connector blocks writes to
MAIN, which is also the right way round. `themeDuplicate` returns **`newTheme`**,
not `theme`.

**Theme source lives in `theme/`** and goes in by **URL, not paste**:
`themeFilesUpsert` accepts a body of `type: URL`, and this repo is public, so
Shopify fetches each file off `raw.githubusercontent.com` — the same route the
70 pack photographs took. Pin the commit SHA in the URL. Shopify **copies** at
upsert time; it does not track the URL, so re-run the upsert after every push.

In the theme and verified by checksum against the local file:

| File | |
|---|---|
| `blocks/compliance-declarations.liquid` | The pack declarations panel |
| `snippets/compliance-row.liquid` | One row, incl. the gap treatment |
| `assets/compliance-declarations.js` | Switches declarations with the selected pack |
| `templates/product.json` | The block wired into `_product-details` |
| `config/settings_data.json` | Brand palette and typography |

**The declarations panel is the compliance work made visible.** Two things it
exists to get right, neither of them optional:

1. **Nothing is invented.** Each row reads a `compliance` metafield transcribed
   off the pack. **A blank row is simply not rendered** — client instruction
   16 Sep. The "Not printed on this pack" notice still exists behind the
   `show_gaps` setting, which is **off**. Verified by re-running the render test:
   the Malnad Chai 1 kg pack now shows net quantity and packed-on only, with the
   MRP and best-before rows gone rather than flagged.
2. **Declarations follow the selected pack.** Net quantity, MRP, packing date
   and best before differ between a 250 g and a 1 kg, and **Horizon updates
   variant-dependent blocks in place rather than re-rendering the section**
   (`assets/product-sku.js` is the precedent). A panel rendered only for the
   selected variant would keep declaring the wrong net quantity after a size
   change. So every variant is rendered server-side and the component reveals
   the selected one, reading only the id from the event.

**It is render-tested, because it cannot be rendered on the store.** All 57
products are DRAFT, so no product page exists to open.
`scripts/render_declarations_test.py` renders the block with **python-liquid**
against mock catalogue data. It found three real defects before they shipped:
`required:` is rejected as a reserved render argument (now `is_required`); MRP
with paise printed as `249.5` where the declaration reads `249.50` (`round: 2`
will not pad, so it is worked in paise); and a three-line `hidden` attribute.
**Re-run it after any edit to the block or the snippet.**

**Brand applied** — `config/settings_data.json`. Body/subheading **Archivo**,
headings/accent **Fraunces**; both are in Shopify's free font library and the
handles were checked against the fonts reference, because a bad handle falls
back silently and the theme would just look like stock Inter. Horizon's 56/48/32
scale is built for Inter, so h1–h3 come down a step to 48/32/24, using only
sizes already present in the file. Palette: paper `#F2F0EA`, ink `#121714`,
muted `#6B7268`, mist `#DCE0D8`. Buttons, cards and badges squared off from
Horizon's 14/4/100. **`presets.Horizon` is left exactly as Horizon shipped it**,
so "reset to preset" still restores the stock theme rather than our brand.

Shopify **normalises `config/settings_data.json` on write** — it reformats the
file, so its stored size and checksum will not match what you uploaded. Verify
that one by reading the values back, not by checksum. The other four match
byte for byte.

**Not yet verified, and cannot be from here:** that the panel renders on a real
product page, and that the two font handles resolve on the storefront. Both need
a product set ACTIVE, or a theme preview, which is Jnanottam's to open.

**Still to build in Stage 2:** homepage sections (hero, categories, story),
header and footer, collection template, and the four policy pages Razorpay
requires. `storefront-design.html` remains the reference.

### PRODUCTS ARE PUBLISHED — 16 Sep, on Jnanottam's instruction

*"add the products mate / i gotta get thing going live"*. **All 57 are ACTIVE
and published to the Online Store channel.** Checked before publishing that
every one of the 63 variants carries a real price and that no `needs-price`
tag survives — nothing went live orderable for free.

**The same trap bit the COLLECTIONS too — found 28 Sep.** Every
`/collections/...` URL returned **404**, so the Shop dropdown and the homepage
category tiles both led nowhere. Cause: all nine collections sat at
`resourcePublicationsCount: 0`. They were created, tag-rules working, 57 of 57
products sorted into them — and on **zero sales channels**, so Shopify would not
serve their pages at all. Fixed with `publishablePublish` against the Online
Store publication; all nine read back `1`. **Publishing products does NOT publish
the collections they belong to — they are separate resources and each needs its
own publish.** `frontpage` was already on 2 channels because Shopify creates it.

**Two steps, not one, and the second is the one that gets missed.**
`bulk-update-product-status` sets `status: ACTIVE`, and that alone left all 57
on **zero sales channels** — invisible on the storefront, and the status field
gives no hint of it. `resourcePublicationsCount` read back `0` across the board.
The channel is a separate mutation: **`publishablePublish`** with the Online
Store publication `gid://shopify/Publication/177970544753`, one call per
product, batched as aliases 15 at a time. **Always verify a publish by
`resourcePublicationsCount`, never by `status`.**

Verified after: 57 ACTIVE, `publishedAt` set on all 57,
`resourcePublicationsCount: 1` on all 57. The nine smart collections picked
them up — 17+7+3+3+3+9+6+6+3 = **57, every product in exactly one**.

**The earlier refusal is superseded.** Setting products ACTIVE was previously
blocked as a real-world transaction; on 16 Sep it went through, 25 + 25 + 7,
zero failures.

**What being published does NOT mean.** The live theme is still **stock
Horizon** — the brand palette, the homepage sections and the declarations panel
all live in the unpublished `Malnad Spices — build`. And there is **no payment
provider**, so a customer can reach checkout and not pay. Publishing the theme
and connecting Razorpay are both Jnanottam's.

**Original import, for the record.** 57 products, 63 variants, 70 pack
photographs, created DRAFT:

| Check | Result |
|---|---|
| Media | every image `READY`, **zero** `mediaErrors` |
| Variant images | every variant carries its **own** pack photo |
| Inventory | `tracked: false`, policy `CONTINUE` on all 63 |

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


**Stage 0 — Shopify is ready (16 Sep). Razorpay KYC cleared 17 Sep.**

### Magic Checkout — chosen 17 Sep, and what it changes about testing

Because Magic **replaces the whole checkout** rather than just the payment step,
four rows of the Stage 3 test matrix were describing a store that no longer
exists, and have been rewritten in `build-runbook.html`:

- **Row 1 and 2 no longer mention stock.** Inventory is untracked and policy is
  CONTINUE — there is no count to decrement or release.
- **Row 2's abandoned cart now sits on Razorpay's side**, not Shopify's. Magic
  owns the checkout, so Shopify never sees the abandonment.
- **Row 13 was "last unit race"**, which is meaningless with no stock tracking.
  Replaced by **"order lands back in Shopify"** — with Magic the order arrives by
  API from Razorpay, and that join is the new silent-failure point.
- **Row 14 — checked 28 Sep, and the expected trap did NOT apply.** I had
  recorded that Magic ships with COD **on** and would need disabling. On this
  account it is **off**: `dashboard.razorpay.com/app/magic/settings/cod-setup`
  shows *"Enable COD as a payment option"* with an **Enable Now** button, which
  only renders while COD is disabled. Most likely cause: **Smart COD
  Configurations was deliberately not ticked during onboarding**, so the COD
  product was never switched on. The Basic Settings below it (*All Zones in
  India*, *All Product*) are the rules that would apply **if** it were enabled —
  they are not evidence that it is. **Do not click Enable Now.** The row still
  gets tested at the checkout itself, because a settings page is not proof.
- **Row 15 dropped a free-delivery threshold that does not exist**, and now tests
  what actually matters: that Magic reads the four-zone, seven-band
  `Malnad delivery` profile. A custom checkout falling back to one flat rate, or
  to none, would misprice postage on every parcel.

**Stop conditions are now rows 7, 10, 12, 13 and 15** — 15 added because wrong
delivery pricing is invisible until the month's accounts.

### Test-mode scare, 28 Sep — MOSTLY A FALSE ALARM, corrected same day

First real checkout attempt exposed this. Two facts that look contradictory and
are not:

- Shopify → Payments → *01 Cards, UPI, NB, Wallets by Razorpay* shows
  **"Test mode is on"**, and it is.
- The actual payment page rejected Razorpay's own test card `4111 1111 1111 1111`
  with **"International cards are not supported"**, and served a real QR code,
  real Google Pay and ICICI PayLater. That is **live** behaviour.

**The real cause was my own bad test card.** `4111 1111 1111 1111` is the
classic **international** Visa test number. Razorpay has international payments
**off** by default — correct for this business — so it is refused with exactly
that message *even in test mode*. Jnanottam then confirmed the keys on the
Razorpay dashboard read **`rzp_test_`**.

**I also over-read the page.** A real-looking QR, Google Pay and ICICI PayLater
are what Razorpay's test checkout shows; they simulate rather than charge. I
called that live behaviour and should not have.

**Use a DOMESTIC test card, or UPI.** `success@razorpay` / `failure@razorpay` as
the VPA is the reliable route and sidesteps the card-origin problem entirely.
Razorpay's docs carry the domestic test card list; do not reach for 4111 again.

**What survives from the scare, and is still true:** Shopify's test-mode toggle
governs the **Shopify gateway**, not Magic. If Magic owns the checkout it runs on
the Razorpay app's own keys. So "Test mode is on" in Shopify is not by itself
proof that a Magic checkout is safe — check the app's key prefix. On this store
that check came back `rzp_test_`, so it was safe.

**The 2% is confirmed in writing.** The same Shopify page states *"2% transaction
fee · processing fees apply"*. That is the fee Magic was chosen to avoid — so it
also confirms that any order that does fall through to Shopify's checkout costs
the extra 2%.

**Unresolved and blocking:** whether Magic is genuinely intercepting, or whether
the customer went Shopify checkout → Razorpay hosted page (the Secure pattern, at
4% all-in). The page said *"Retry payment of ₹1,155"* with no address collection
on it, which points at address/shipping having happened elsewhere.

### FIRST REAL CHECKOUT — 28 Sep. Two defects, one thing verified good.

Cart: Black Cardamom 100 g ₹240 · Badam 500 g ₹750 · Soapnut Powder 200 g ₹110.
Subtotal ₹1,100. Shipping ₹55. Total ₹1,155 "including ₹100.00 in taxes".
Delivered to Bangalore 560080 (Karnataka).

**1. MAGIC CHECKOUT IS NOT INTERCEPTING — settled, not a theory.** The checkout
URL was **`malnadproducts.in/checkouts/cn/...`** — Shopify's own checkout, with
Shopify's Contact / Delivery layout. Only *after* that does Razorpay's hosted
payment page appear. That is the **Razorpay Secure** pattern, the one we
explicitly chose against: **Shopify's 2% plus Razorpay's ~2%, about 4% all-in,
against Magic's ~0.65%.** Corroborating evidence on the app page at the time: **Extensions
0 active** — Magic needs a storefront extension to replace the checkout button
and none was enabled. **STALE — see below: that page now reads Extensions 1
active, Functions 1 active.** Do not cite the 0 as current.

**2. TAX IS COMPUTING AT 10%, NOT 5% — and order #1001 names the exact cause.**
Read back from the order's `taxLines`:

    CGST  ratePercentage 5  ->  ₹50.00
    SGST  ratePercentage 5  ->  ₹50.00
                    total       ₹100.00

So Shopify applies the **country rate to each of CGST and SGST**, not one 5%
split into 2.5 + 2.5. Correct at 5% inclusive is `1100 x 5/105 = ₹52.38`, so the
client over-declares **₹47.62 on this order — 4.33% of goods value, on every
sale.** Prices are tax-inclusive so the customer still pays ₹1,155 either way;
the difference comes entirely out of the client's own margin at filing.

**THE FIX: set the India country rate to 2.5%, not 5%.** That yields
CGST 2.5 + SGST 2.5 = 5% on intra-state. **Leave the per-state IGST rows at 5%
"instead of federal"** — those govern inter-state sales and 5% is right there.
Jnanottam is the CA and this is his screen, but the arithmetic is settled by the
order record, not inferred.

**3. Shipping is CORRECT — verified.** Variant weights read back: 140 + 540 +
240 = **920 g**, which lands in the 0.5–1 kg band; the Karnataka rate for that
band is **₹55**, exactly what checkout charged. The four-zone weight-based
profile works.

**Order #1001 — everything else verified good.** `test: true`, `PAID`,
`UNFULFILLED`. Total ₹1,155 = subtotal ₹1,100 + shipping ₹55. All three line
items correct with the right variant titles (100 g / 500 g / 200 g). Shipping
line named **Standard delivery** at ₹55, matching the Karnataka 0.5–1 kg band
for a 920 g basket. Phone **7204038395** captured despite the field being marked
optional. **The Razorpay → Shopify join works** — matrix row 13 passes.

**Gateway on the transaction reads `01 Cards, UPI, NB, Wallets by Razorpay`**,
which is final confirmation the order went the **Shopify-gateway route**, not
Magic. Finding 1 above is now proven from the order record as well as the URL.

**Not yet cross-checked against Razorpay:** the MCP connector has disconnected
again and needs re-authorising. Shopify's `paymentId` on the transaction is
`rUEmUk2hWnDV9gEOJtNdr7YPq`, which is not a Razorpay `pay_` id — matching the two
sides still needs that connector back.

**Also observed:** the phone field still reads **"Phone (optional)"** — the
Settings → Checkout change has not been made yet.

### Magic Checkout — now intercepting, 28 Sep. Razorpay backend still erroring.

**How the storefront integration actually works, and how to verify it.** Magic
needs the **`Magic Checkout Script` app embed** enabled on the live theme:
Online Store → Themes → Edit theme → left panel, bottom → **App embeds**. Three
Razorpay embeds are offered — `Login with Razorpay`, `Magic Checkout Script`,
`Razorpay Reviews`. **Only the middle one is wanted.** Login with Razorpay pushes
customer identity outside Shopify, which the owner dashboard reads; Reviews is a
separate decision entirely.

**VERIFY AN APP EMBED BY READING `config/settings_data.json`.** Enabled embeds
are written into **`current.blocks`**. If that key is absent, **nothing is
enabled** — regardless of what the toggle looked like. That is exactly what
happened here: the toggle was flipped but **Save was never pressed**, the file
had no `blocks` key at all, and three checkout tests were burned chasing
password protection, cart drawers and theme incompatibility. After a proper save
the file went **7,877 → 8,082 bytes**. Size alone is enough to confirm.

**Sequence that was wrongly blamed, for the record:** the cart drawer
(`cart_type: drawer`) was not the cause — `/cart` behaved identically. Password
protection was not the cause either; the store was launched
(`passwordProtection.enabled = false`, verified) and nothing changed. Both were
reasonable hypotheses and both were wrong. The unsaved toggle was the whole
thing.

**Current state:** Magic's modal now opens over the storefront, branded
*Secured By Razorpay* — so the button is hooked and the script runs. It then
fails with **"Something went wrong, please try again after some time."** Not yet
diagnosed. Leading suspicion is that Magic does not run properly in **test
mode** on a real storefront, since both the Razorpay dashboard and the Shopify
gateway are in test. The browser console is the next diagnostic step — the modal
text is generic and the console will carry the real API error.

### Magic modal hangs on the loading shield — 28 Sep, diagnosed to Razorpay's side

**The storefront side is DONE and proven from the file, not the toggle.** The live
theme's `config/settings_data.json` (8,082 bytes, MAIN = `Malnad Spices — build`)
carries:

    "blocks": {
      "3557650678667880288": {
        "type": "shopify://apps/razorpay-cod-magic-checkout/blocks/magicx-script/c13c688d-5c45-4054-b95f-1edd63faa705",
        "disabled": false,
        "settings": {}
      }
    }

So the `Magic Checkout Script` embed is enabled and persisted. **Do not re-chase
the embed, the cart drawer, the theme or password protection** — all four have now
been eliminated, three of them after wasting a test each.

**Symptom:** the modal opens, branded *Secured By Razorpay*, then sits on the
loading shield indefinitely. Console carries no red error — only preload warnings
and `[bugsnag] Loaded!` from `checkout-DTJs6qRt.js`, i.e. Razorpay's own bundle
and error reporter load fine. A browser that loads the script and renders the
chrome but never gets a checkout body is waiting on an API call that does not
return. **The failure is server-side at Razorpay, not in the theme.**

**Evidence from the Shopify side:** one abandoned checkout, 28 Sep 16:03,
**₹685 / 4 items**, `AbandonedCheckout/66758444351601`. Orders still stand at one
(#1001, 15:28, the Shopify-gateway route). So no Magic attempt has ever produced
an order on either side.

**Leading cause, and it is a settings item not a code one: the Magic Checkout app
still reads "Needs Activation"** in Shopify (recorded in the readiness table
above and never cleared). Until Razorpay activates the integration for this
store, its backend has no store to serve and the modal has nothing to render.
Second candidate: **Magic is a production feature.** Its saved-address network,
serviceability and coupon services are live-only, so it is not expected to
complete against `rzp_test_` keys on a real storefront.

**I cannot reproduce it from this container.** Chromium and Playwright are
installed and the store is public, but the session's egress policy answers **403
to CONNECT** for both `malnadproducts.in:443` and `checkout.razorpay.com:443`, so
no browser here can reach either. Driving the checkout is Jnanottam's browser only.

**The read I wanted is NOT available in test mode — checked, 28 Sep.** The
Razorpay connector came back and returns 0 orders / 0 payments / 0 settlements,
but it is **live-mode only** (proved against order #1001's test-mode ₹1,155
Razorpay transaction — see the connector section below). So it cannot say whether
Magic's backend created an order at 16:03, and no read from here can while the
store stays in test.

**That removes the last reason to keep debugging in test mode.** Going live is now
both the leading candidate fix and the only route to verifying anything from this
side. Order of work: confirm Magic is activated at Razorpay (the app has read
"Needs Activation" since 17 Sep and was never cleared), then switch to live keys
and buy one ₹80 pack to prove it end to end.

**Customer-facing consequence while this is open.** The store is public
(`passwordProtection.enabled = false`) and the embed is live, so a real customer
clicking Check out gets a modal that hangs — nobody can buy. Setting
`"disabled": true` on that block restores the working Shopify checkout (proven by
order #1001) at the higher ~4% fee. That is a one-line theme write from here.

### SHOPIFY'S SIDE OF MAGIC IS COMPLETE — verified 28 Sep, stop looking here

Jnanottam: *"i want magic to work / until that works im not giving this away."*
Fair — the fee gap is ~₹28,700/year to the client. So the Shopify half was read
out properly rather than guessed at. **It is finished.**

`appInstallations` shows three apps only: Shopify Messaging, this connector, and
**`razorpay-magicx-app` — "Razorpay COD & Magic Checkout", developer Razorpay
Payments, `AppInstallation/622535835761`, `embedded: false`.** So there is one
Razorpay app, not two; the readiness table's "a second Razorpay app not yet
installed" is not a gap, the gateway is a Shopify payment provider rather than an
app.

**The app holds 41 access scopes and every one Magic needs is granted** —
`write_orders`, `write_order_edits`, `write_draft_orders`,
`unauthenticated_write_checkouts`, `unauthenticated_write_customers`,
`write_themes`, `write_shipping`, `write_delivery_customizations`,
`write_payment_customizations`, `write_app_proxy`. **A missing scope is ruled
out.** Keep this list: after any reinstall, read it back and compare.

So everything on our side is done — app installed and fully authorised, embed
enabled and saved, domain primary with SSL, 57 products and 9 collections
published, weight-based shipping proven twice. **The remaining fault is in
Razorpay's own configuration, and every screen for it is behind Jnanottam's
login.** `embedded: false` means opening the app from Shopify Apps hands off to
Razorpay's dashboard — that is where setup lives and where "Needs Activation"
clears.

**LEADING HYPOTHESIS — DOMAIN MISMATCH, and it fits the hang better than test
mode.** The primary domain became `malnadproducts.in` on **28 Sep**, the same day,
and `myshopifyDomain` is still `8uysc8-kx.myshopify.com`. Magic's script asks
Razorpay for the configuration belonging to the domain it is running on. If the app
was set up before the domain was connected, Razorpay holds the myshopify domain,
there is no config for `malnadproducts.in`, and the modal waits on an answer that
never comes. **That explains the clean console** — nothing errored, so bugsnag had
nothing to report. Test mode would more likely return an error than hang forever.

**THE DOMAIN HYPOTHESIS IS WITHDRAWN — it was my third wrong call on this
integration.** Jnanottam checked and Razorpay's settings do read
`8uysc8-kx.myshopify.com`. That is **not** a finding: `.myshopify.com` is
Shopify's permanent internal shop identifier, which every Shopify app stores and
which never changes when a custom domain is connected. Seeing it there is normal.
**Do not reinstall the app to "fix" the domain** — it would cost time and risk
breaking a setup that is otherwise correct. Withdrawn before he acted on it.

**Razorpay's own documentation cannot be read from here either** —
`razorpay.com` is blocked by the session egress proxy, same as
`malnadproducts.in` and `checkout.razorpay.com`. So **do not state Razorpay
dashboard menu paths**; they would be invented. That limit is the reason this
stopped being diagnosable from this side.

**WHERE IT NOW STANDS.** Everything checkable has been checked and is correct.
The remaining fault is inside Razorpay's account configuration, which neither of
us can see. Two actions, in order:

1. **The app tile's "Needs Activation" link** — Shopify → Apps → Razorpay COD &
   Magic Checkout. The tile is itself the link, the app is non-embedded so it
   hands off to Razorpay, and this is the only definitely-relevant screen
   Jnanottam can reach. It has been outstanding since 17 Sep.
2. **Razorpay support.** Magic Checkout is a product *they* activate. A
   paste-ready request is written at
   **`docs/razorpay-magic-support-request.txt`** — it carries the store id, the
   symptom, the five things already ruled out with the evidence for each, and
   four direct questions including whether Magic works in test mode at all.

**Do not gate the handover on this.** It depends on a third party, so the working
store (Shopify checkout, proven by order #1001) is what gets handed over, with
Magic described as a pending fee optimisation.

### The app admin page, read 28 Sep 22:39 IST — the integration is ALIVE

Screenshot of `admin.shopify.com/store/8uysc8-kx/settings/apps/app_installations/app/90fdd4c5dcda479affa5f5bfb4681573`:

| | |
|---|---|
| Razorpay COD & Magic Checkout | Installed 1 week ago |
| **Extensions** | **1 active**, available for 2 areas |
| **Functions** | **1 active**, available for 2 areas |
| Orders | view + edit, **recent activity 55 minutes ago** |
| Customers | view + edit, 1 hour ago |
| Online Store · Discounts · Shopify Functions · Products | 1 week ago |

**Extensions is 1, not 0.** That supersedes the 28 Sep finding above and matches
`config/settings_data.json` — the storefront hook is registered on both sides.

**The app is actively calling Shopify.** Orders touched 55 minutes before the
screenshot, Customers an hour before, both with edit rights — so Razorpay's
backend is reaching Shopify now, not a week ago. **The integration is not dead**,
which narrows the fault to Magic's own configuration rather than the link.

**But nothing landed.** Re-read immediately after: still **1 order** (#1001,
15:28Z, test, PAID, ₹1,155), **1 abandoned checkout** (16:03Z, ₹685) and
**1 customer**. So that Orders call read or attempted and did not create.

**No "Needs Activation" banner appears on this page.** Next control to try is the
**Open app** button, top right beside *More actions* — non-embedded, so it hands
off to Razorpay's dashboard for this store, which is where Magic's settings live.

### MAGIC IS ACTIVATED — Razorpay's own settings read, 28 Sep 23:03 IST

Reached via `dashboard.razorpay.com/app/magic/settings/checkout-setup`. Magic
Checkout's settings live under **Payments → (left rail) Magic Checkout → Setup &
Settings**, with entries: Checkout Setup · Cash On Delivery · RazorpayID ·
Delivery Statuses · Shipping Setup · Order Settings · Analytics · Upload ·
Magic Cart, plus a Magic Suite group. **Magic is NOT in the top nav**, which is
why it looked absent — `Open app` from Shopify lands on `/app/home`, not here.

**"Magic Checkout Settings — Magic Checkout activated. Set up COD and other
configurations here."** Store shown: `8uysc8-kx.myshopify.com`, with an Edit
link beside it.

**So the "Needs Activation" hypothesis is DEAD — my fourth wrong call on this
integration.** Magic is activated and the store is linked. Do not chase
activation again. For the record the wrong calls were: three causes before the
unsaved app-embed toggle, the live-mode scare, the domain mismatch, and now
activation.

Checkout Settings on that page, all **Disabled**: Capture billing address ·
Capture GSTIN · Capture order instructions · Hide COD payment when disabled ·
Pay with gift card. None of these would cause a load failure.

**DO NOT ENABLE "Magic Shipping" — `/app/magic/settings/shipping-setup`.** The
toggle is **off** and must stay off. Its own text: *"Enabling Magic Shipping will
bypass all shipping configurations from any plugins on your E-commerce platform
and follow configurations added below."* Turning it on would discard the
four-zone, seven-band `Malnad delivery` profile that has been proven correct
twice against real carts (920 g → ₹55, 1,570 g → ₹85). It is a tempting toggle
that would silently regress working shipping.

**REAL DEFECT FOUND THERE, and it is the Shopify trap seen from Razorpay's side.**
Razorpay has synced the profiles correctly:

| Profile | Zones |
|---|---|
| **All Other Products** (Default) | **— empty** |
| Malnad delivery | Karnataka · North East and islands · Rest of India · South and West India |

All 63 current variants sit in `Malnad delivery`, so today's catalogue is fine.
**Any product added later lands in the empty default and gets no delivery option
at checkout** — unbuyable, with no error shown. Already recorded from the Shopify
end; this is independent confirmation. Fix is Shopify → Settings → Shipping and
delivery, adding zones to the default profile; it cannot be done through the API.

**WHAT IS LEFT.** Activation, store link, app embed, 41 scopes, Extensions,
Functions and shipping profiles have each been checked and are correct. **The
only remaining difference from a working Magic setup is TEST mode**, still shown
as a green TEST toggle at the top of every Razorpay screen. That is now the last
standing hypothesis by elimination rather than by guess. If Magic still hangs on
live keys it is a Razorpay-side bug and `docs/razorpay-magic-support-request.txt`
goes in.

### RAZORPAY'S OWN DOCS, via WebSearch — 28 Sep. Three documented causes.

**`WebSearch` works even though direct fetching does not.** `razorpay.com`,
`youtube.com`, `google.com`, `bing.com` and `duckduckgo.com` all fail at the
egress proxy, but the `WebSearch` tool routes elsewhere and returns Razorpay's
documentation. **Use WebSearch for any platform question in this project** — the
earlier conclusion that Razorpay's docs were unreachable was true only of
WebFetch/curl. Jnanottam's idea to go and research it was the right call and it
produced more than four hours of my own hypotheses did.

**1. ~~A REQUIRED SETUP STEP WAS NEVER DONE — "disable Auto fetch coupon".~~
WITHDRAWN SAME NIGHT — the setting does not exist on this account.** Jnanottam
scrolled Checkout Setup to the bottom: it ends at Checkout Settings → Gift Card
Settings (*Pay with gift card, Disabled*) → *Enable the Abandoned webhook to
track* (off, URL blank) → **Save settings**. **There is no Auto fetch coupon
toggle.** Most likely it only renders where the Coupons feature is provisioned —
in which case the checkout is not fetching coupons either, and this is not the
cause. Recorded so nobody hunts for that toggle again. The original reasoning,
kept because the mechanism is still worth knowing:
Razorpay's Shopify integration procedure reads: *"Navigate to Checkout Setup,
disable Auto fetch coupon and click Save settings."* It sits below the Gift Card
Settings on `/app/magic/settings/checkout-setup`, past where the screenshot
scrolled. **Coupons is a separate on-demand feature** requiring its own request
form, so on an account without it, a checkout that auto-fetches coupons on load
calls a service that is not enabled. **A call that never returns is exactly a
modal that renders its chrome and then waits forever with a clean console** —
nothing threw, so bugsnag reported nothing. Best mechanical fit found for this
symptom, and it is a documented step rather than a hypothesis.

**2. Payment method customizations — FOUND AND IDENTIFIED, 28 Sep 23:27.**
`admin.shopify.com/store/8uysc8-kx/settings/payments/customizations` shows exactly
one, **Active**:

> **"Hides COD payment method for Non MagicX shipping methods"** — by *Razorpay
> COD & Magic Checkout*

That closes the "Functions: 1 active" question: it is Razorpay's own COD function.
**COD is disabled on this account, so the function has nothing to do** — it is a
no-op. (This connector cannot read these; `paymentCustomizations` needs
`read_payment_customizations`, which it lacks. Read from Jnanottam's screen.)

Razorpay's troubleshooting does say *"Disable or remove all customizations listed
under this section"*, but that guidance is about **their gateway not appearing in
Shopify's checkout** — a different symptom from a Magic modal that never loads,
and this Function acts on Shopify's checkout, which Magic replaces. So: worth
disabling because it is their documented step, costs nothing and risks nothing
with COD off — but **do not expect it to be the fix**. If it changes nothing,
every documented cause has been tried and the support mail is the next step.

**3. Theme changed.** Their first troubleshooting question is *"check if your
website's theme was recently changed. If the theme is unchanged, raise a ticket."*
The theme was published **today**, after the app was installed a week ago. Their
documented flow is *"Magic Checkout will be enabled on a test theme; you can then
publish this on your live theme post-integration"* — so a theme swap after setup
is a known breakage.

**On test mode — my long-running hypothesis is WEAKER than I claimed.** The docs
say plainly *"You can test a payment for All-in-one Razorpay Payment Gateway on
the Shopify store by switching to test mode."* The real documented limitation is
narrower: *"Razorpay does not support using live and test keys simultaneously in
a staging environment, as the URL configured in live mode is used for testing."*
So test mode is not by itself a reason Magic cannot load. **Demote it below the
three causes above.**

**Escalate to `magic-checkout-support@razorpay.com`**, not generic support — it
is the address Razorpay gives for getting Magic features enabled on an account.

**A DOCUMENTED STEP THAT HAS NO SCREEN ON THIS ACCOUNT.** The configuration doc
says: *"navigate to Magic Checkout → Setup & Settings → **Platform Settings**,
select Shopify from the Platform drop-down list and enter your Shopify Store
ID."* **There is no Platform Settings entry in this account's sidebar** —
Checkout Setup · Cash On Delivery · RazorpayID · Delivery Statuses · Shipping
Setup · Order Settings · Analytics · Upload · Magic Cart · Magic Suite. The store
ID does appear on Checkout Setup with an Edit link, so this may be the same step
in a newer layout — or a step this account never got. **Put it to Razorpay
rather than guessing.** Note `Coupons` IS present as a top-level sidebar item.

**Razorpay's own walkthrough video:** `youtube.com/watch?v=Cr9IdCU5o8Q` —
*Integrate Razorpay Magic Checkout with Shopify Website*. Not viewable from this
container (YouTube is blocked at the proxy, like everything else), so it is
Jnanottam's to watch.

**STILL UNTESTED after all of the above:** payment method customizations
(cause 2) and the theme change (cause 3). Those two plus Platform Settings are
what remains.

Sources: `razorpay.com/docs/payments/magic-checkout/troubleshooting-faqs/` ·
`razorpay.com/docs/payments/magic-checkout/shopify/` ·
`razorpay.com/docs/payments/magic-checkout/shopify/configuration/`

### Magic Cart reads "unpublished" — that is CORRECT, do not publish it

`dashboard.razorpay.com/app/magic/settings/magic-cart` shows a banner: *"Magic
Cart is unpublished! Your configurations here won't show on your website till you
publish Magic Cart."* with a **Republish Cart** button. It is the only thing in
the whole Razorpay dashboard in an explicitly incomplete state, so it looks like
the find. **It is not.**

**Magic Cart is a separate product from Magic Checkout** — Razorpay's own
description is a cart that "transforms your static cart into a conversion engine",
with upsell, cross-sell, discount nudges and AOV widgets. Nothing in their
documentation makes it a prerequisite for Magic Checkout. Unpublished is the
correct state for a product that was never configured.

**Do not press Republish Cart.** It would push a Razorpay cart drawer onto the
live storefront over Horizon's own cart, with `Cart theme color` currently
`#000` rather than the brand palette — a visible change to a store being handed
over, for a feature nobody asked for.

Its preview does confirm the catalogue sync is healthy: real products with real
prices (Soapnut Whole 150 g ₹140, Sikakai Powder 200 g ₹120, grand total ₹260).

### SMS notifications — Shopify barely does them. Answered 28 Sep, no app bought.

Jnanottam saw a notice while making the phone number compulsory, saying an app is
needed to send SMS. It is accurate. Checked rather than answered from memory:

**Shopify sends natively, and only these four:** order confirmation (only when the
customer supplies a **phone number instead of an email**), local pickup notices,
gift card issuance, POS receipts — and only in supported countries.

**Everything else needs a paid third-party app:** shipping and dispatch updates,
delivery notifications, abandoned cart, anything promotional.

**Consequence for this store:** customers get order confirmation and shipping
updates **by email only**. For an Indian customer buying spices that is a real
service gap — a parcel going out with no message is how "where is my order"
happens.

**DECISION: no SMS app. Do not add a subscription.** Out of the ₹38,000 scope,
and a recurring monthly cost on a store that has not taken a real order yet. The
answer is already in scope and free: **the WhatsApp Business App**. The phone
number is now **required at checkout**, so every order carries a mobile number;
he packs to order, so when a parcel goes out he sends one WhatsApp with the
tracking number from his phone. Better service than an automated SMS at this
volume. Revisit only when order volume makes the typing the bottleneck — at which
point the cost is obviously justified.

Source: `help.shopify.com/en/manual/fulfillment/setup/notifications/sms-notifications`

### DEEP ANALYSIS, 29 Sep — the config may be MODE-SPLIT, and that is testable free

Asked for a proper analysis rather than more single guesses. Every layer has now
been verified correct: app installed with 41 scopes, embed enabled and saved,
Extensions 1, Functions 1, Magic **activated**, store linked, catalogue synced
(Magic Cart preview shows real products and prices), shipping profiles synced,
and Razorpay's backend actively calling Shopify's Orders API. **Nothing is
misconfigured. The two systems are talking. Nothing renders.**

**What the symptom rules out.** A modal that draws its chrome, loads bugsnag,
throws nothing and never fills is not a broken script, a missing scope or a
plugin conflict — all of those throw. It is a request whose answer never
arrives: Razorpay's frontend asking Razorpay's backend for this store's checkout
configuration and getting silence. So the question is not what is misconfigured,
it is **why the backend cannot find the config the frontend asks for.**

**THE DOCUMENTED LINE THAT EXPLAINS IT, previously under-read:**

> *"Razorpay does not support using live and test keys simultaneously in a
> staging environment, **as the URL configured in live mode is used for
> testing**."*

**The store URL registration is a LIVE-MODE object.** It lives in live config and
is used for testing — not duplicated into test mode. Every dashboard screen read
so far carried the green **TEST** toggle, so those may be the **test-mode copy**
of Magic's settings while the registration that matters sits in live.

That fits everything: the config pages look complete (test-mode settings do
exist); the storefront asks for `malnadproducts.in` config in test mode and there
is no registration to return; nothing errors because an empty lookup is not an
exception; and Razorpay still reaches Shopify because the *app* install is a
separate channel from checkout config.

**THE TEST — one toggle, no keys, no Shopify change.** Flip the Razorpay
dashboard **TEST → LIVE** and re-open the same screen, Magic Checkout → Setup &
Settings → **Checkout Setup**. Compare against the test-mode screenshot:

- **Different** (different store, different toggles, or the "Magic Checkout
  activated" line absent) → config IS mode-split, test mode was the cause,
  proceed to live keys.
- **Identical** → config is not mode-split, this theory is dead, and it is a
  Razorpay-side bug. Send `docs/razorpay-magic-support-request.txt`, having
  eliminated everything a merchant can eliminate.

**Either answer is worth having.** Note this supersedes the earlier demotion of
the test-mode hypothesis: the docs do say test payments work on Shopify, but that
is about the *gateway*, not about where Magic's *store registration* lives. Those
are different objects and conflating them was the error.

### CONFIRMED 29 Sep 10:59 IST — THE CONFIG IS MODE-SPLIT

Jnanottam switched the dashboard to LIVE. **The Magic Checkout sidebar is not the
same in the two modes**, which settles it:

| TEST mode | LIVE mode |
|---|---|
| Checkout Setup | **Control Center** — absent in test |
| Cash On Delivery | Checkout… |
| RazorpayID | COD Setup |
| Delivery Statuses | RazorpayID |
| Shipping Setup | **RTO Reduction…** — absent in test |
| Order Settings | Delivery Statuses |
| Analytics · Upload · **Magic Cart** | Shipping Setup · Order Settings · Upload |

**Live mode carries screens test mode does not.** So the two modes are separate
configuration spaces, and every screen inspected on 28 Sep — Checkout Setup,
Shipping Setup, Magic Cart, the COD page — was the **test-mode copy**. The
conclusions drawn from them ("activated", "store linked", "shipping synced")
describe test-mode config and say nothing about live. A live-mode banner
**"78 Free* Days"** also appears, which test mode never showed.

**This is the first confirmed progress on the hang.** It does not by itself prove
the checkout will work; it proves the thing we were reading was the wrong copy.

**Next two screens, in order, before any retest:**
1. **Control Center** — the screen test mode never had; likely carries Magic's
   live status and setup state.
2. **Checkout Setup in LIVE** — compare against the test-mode screenshot. If
   *"Magic Checkout activated"* or the `8uysc8-kx.myshopify.com` line is missing
   or different, that is the answer.

**Do not retest the cart yet.** Switching the dashboard view does not change the
storefront: Shopify still holds `rzp_test_` keys, so the checkout behaves exactly
as before until live keys are generated and pasted in. A retest now would produce
a false negative.

### Website submission started 6 Oct — the "Food category" condition

The **Add new Website/App** modal opens on a notes screen before the form. Its
first condition: *"The product/services that you are selling on the website/app
should fall under **Food** category."* Further notes sit below the fold.

**Worth knowing before a reviewer asks: three of the 57 products are NOT food.**
Soapnut (whole), soapnut powder and sikakai powder are household and hair-care
goods — our own copy ends each with *"Not a food."*, they carry HSN 1404 / 3401 /
3305, and they sit in their own Home & Personal Care collection. That is normal
for a Malnad dry-goods shop and the separation is already visible on the site, so
**do not hide them**. If queried, the honest answer is: a food retailer that also
sells three traditional washing and hair-care items, listed separately and
labelled as non-food.

Also seen on that screen: a red **"Something Went Wrong"** toast. Treated as a
page-load artefact; if it recurs *after* submitting, that is the submission
failing and is a real finding.

Trial banner now reads **71 Free* Days**, down from 78 on 29 Sep — consistent
with a week elapsed.

### SUBMITTED AND UNDER REVIEW — 7 Oct 12:09 IST

`https://malnadproducts.in` is listed on
`dashboard.razorpay.com/app/website-app-settings/business-website-details` with
the status **Under review** — *"Expect an update in 24-48 hours."* **+ Add
website/app** is now greyed out, which is the correct state for a pending
submission, and **Generate Key** stays disabled until approval lands. Trial
banner **70 Free* Days**.

So the 6 Oct "Something Went Wrong" was transient at Razorpay's end, as read, and
the retry after Jnanottam's ticket went through. **The 24–48 hour clock is
running and is held entirely by Razorpay** — there is no action on either side
until it returns. Razorpay's own docs allow up to three working days, so a
Thursday or Friday answer is normal, not a failure.

**Nothing about the payment chain is diagnosable while this is pending.** On
approval, in order: Generate live keys → paste into Shopify's Razorpay gateway →
untick test mode → Magic resolves against live config, where its enable toggle
already reads ON. That is the whole remaining fix for the Magic hang.

The 6 Oct record below is kept because the UPI workaround still stands as the way
to trade before approval.

---

### 6 Oct — the submission error, and the UPI workaround

Clicking **Proceed to update website/app** returned **"Something Went Wrong"**
every time. **Cleared on 7 Oct — see above.** Razorpay documents that string as *"We are facing some trouble
completing your request at the moment"* — **an exceptional server-side error at
their end**, to be retried or raised with support. Jnanottam has raised a ticket.

**There is NO workaround for the Razorpay gate.** Live API keys require an
approved website; the Generate Key button is disabled server-side. Do not look
for one, and do not propose switching gateway — V-CIP KYC applies at every Indian
aggregator, so a new provider is slower, not faster.

**BUT THE STORE CAN TRADE TODAY, with zero fees: a Shopify CUSTOM MANUAL PAYMENT
METHOD for UPI.** Available on every plan. Settings → Payments → Manual payment
methods → Create custom payment method. Orders land **Pending** until the owner
confirms payment and marks them Paid.

- **Still prepaid** — payment before dispatch, so the no-COD instruction holds.
- **Zero fees**, against ~4% on the Shopify gateway or ~0.65% on Magic.
- **Normal for an Indian retailer**; UPI is how this trade actually settles.
- Name it **`UPI`** — Shopify reserves *"Bank Deposit"* and *"custom"*.
- Needs Dhanush's business UPI ID, typed straight into Shopify, never into this
  transcript.
- Trade-off: manual reconciliation per order, nothing auto-captures.

**When Razorpay approves, the gateway is added alongside or instead; swapping
payment methods does not disturb products, shipping or the theme.** So the
handover is no longer blocked: the client receives a store that genuinely sells,
with Razorpay as an upgrade added during the week.

Source: `help.shopify.com/en/manual/payments/manual-payments`

### ROOT CAUSE, 29 Sep 11:05 — NO WEBSITE IS REGISTERED WITH RAZORPAY

`dashboard.razorpay.com/app/website-app-settings/business-website-details`, live
mode, **Websites & API keys** tab:

- **Website/app details** — *"Submit the website/app where you want to collect
  payments. **Verification takes 24-48 hours**."* with **+ Add website/app**.
  **The list is EMPTY — no website has ever been submitted.**
- **API keys & integration** — *"You will be able to generate API keys once your
  website is approved."* **The Generate Key button is DISABLED.**
- Side panel: *"You can generate API keys after your website is approved.
  Meanwhile you can switch to test mode to get test API keys for integration."*

**This is the bottom of the whole problem.** Razorpay holds no live registration
for `malnadproducts.in`, so there is no live store configuration for Magic to
serve — which is why the modal asks and receives nothing. It is also the
"Platform Settings / store URL" step flagged on 28 Sep as documented but having
no screen: **it lives under Account & Settings → Website and app settings, not
under Magic Checkout.**

**CONSEQUENCE, AND IT IS BIGGER THAN MAGIC.** Live API keys cannot be generated
at all until a website is submitted and approved. So **the store cannot take real
money by any route today** — not Magic, not the Shopify gateway. Everything has
been running on `rzp_test_` keys because those are the only keys that exist.

**ACTION: submit `https://malnadproducts.in` via + Add website/app.** That starts
a 24–48 hour verification clock held by Razorpay, which neither of us controls.

**FIX THE POLICIES BEFORE THE REVIEW LANDS.** A human reviews the site. Five of
the six store policies still render as **escaped HTML** (`&lt;h2&gt;` visible as
text, refund wrapped in `<pre>` as a monospace block). A payments reviewer opening
Terms, Refund or Shipping sees broken markup — a plausible reason to reject or
query, costing another 24–48 hours. Redo them with the `<>` (Show HTML) toggle
clicked **before** pasting, box emptied first.

**Handover framing changes shape:** a finished store that goes live the moment
Razorpay approves the website. That is accurate and simple to say.

### SOLVED 29 Sep 11:01 — MAGIC'S ENABLE SWITCH EXISTS ONLY IN LIVE MODE

The live-mode Checkout Settings page is a **different page at a different URL**
from the one inspected all of 28 Sep:

| | TEST | LIVE |
|---|---|---|
| URL | `/app/magic/settings/checkout-setup` | `/app/magic/settings/magicx-store-settings` |
| **Enable Magic Checkout** | **absent** | **present, ON** |
| Other settings | Capture billing address · GSTIN · order instructions · Hide COD · Gift card · Abandoned webhook | Email Field · Theme Color · Mandatory OTP |

Both pages carry *"Magic Checkout activated"* and `8uysc8-kx.myshopify.com`, which
is why test mode looked complete.

**THE CAUSE.** There is **no way to enable Magic Checkout in test mode** — the
toggle does not exist there. The storefront runs on `rzp_test_` keys, so Razorpay
resolves the store in test context, where Magic has no enabled configuration to
serve. The script receives nothing, the modal renders its chrome and waits
forever, and **nothing errors because nothing failed** — there was nothing to
return. That accounts for every observation: the clean console, the complete-looking
settings, the healthy app-to-Shopify traffic, and the endless shield.

**THE FIX IS THE LIVE KEYS.** Not a workaround. Generate live keys, paste into the
Shopify Razorpay gateway, untick test mode. Magic then resolves against live
config, where it is already enabled.

**TWO DEFECTS ON THAT LIVE PAGE, both flagged:**

1. **`Email Field` = Optional → must be MANDATORY.** Shopify sends order
   confirmations and shipping updates by **email only** on this store (see the SMS
   section — no app is being bought). A customer checking out without an email
   gets **no confirmation at all** and is unreachable except by WhatsApp. This is
   a service defect, not a preference.
2. **`Theme Color` = `#528FF0`** — Razorpay's default blue, not the brand. Should
   be canopy green **`#1F4034`**. It is the screen every customer pays on.

`Mandatory OTP` is **off** and can stay off — it adds friction and guards
saved-address reuse, which is not needed for a prepaid store.

**Sequence from here:** fix those two → Save → generate live keys → paste into
Shopify's gateway → untick test mode → buy Black Pepper 100 g at ₹80 → Claude
matches the order against Razorpay's payment record from both sides, which the
connector can finally do because it is live-mode only.

**For the record, the wrong calls before this one:** three causes before the
unsaved app-embed toggle, the live-mode scare, the domain mismatch, activation,
and the auto-fetch-coupon step. The thing that actually cracked it was
Jnanottam's instruction to go and research rather than keep reasoning, followed
by comparing the two modes screen by screen.

### Live-theme writes ARE blocked — confirmed by the mutation, 28 Sep

`themeFilesUpsert` against the MAIN theme is refused outright by the connector's
safety policy: *"This mutation targets the live (published) theme. Theme file
writes against the live storefront are blocked."* Now that `Malnad Spices — build`
IS MAIN, **no theme file can be written from here at all.** Every theme change is
either a duplicate-edit-publish cycle or Jnanottam in the theme editor. Do not
plan a fix that needs a live theme write.

**CLOSED 7 Oct — the repo and the live theme agree again.** Jnanottam turned the
*Magic Checkout Script* embed off and saved on the live theme. Read back from
`config/settings_data.json`: **`"disabled": true`**, size **8081** (was 8082 —
`false`→`true` is one byte shorter), md5 **`938f1564badfb4ec385e8434e1b89497`**
(was `c6b03740…`). **The hanging modal is off the storefront**; Check out now goes
to Shopify's own checkout, the route proven by order #1001, at the ~4% fee until
Razorpay approves the website and Magic can resolve against live config.

**Two traps on the way there, both worth keeping:**

1. **There is a second theme that looks like ours.** `Updated copy of Malnad
   Spices — build`, id **188710879345**, DRAFT — Shopify's auto-generated update
   copy. Its App embeds panel shows all three Razorpay embeds off and its Save
   greyed out, so toggling there changes nothing and looks like success. **The
   live theme is `Malnad Spices — build`, id 146238865521.** Check the theme name
   and the **Active** badge in the editor's title bar before touching anything,
   and never press Publish on the update copy.
2. **The App embeds toggle can show OFF while the file says the block is ON.**
   Observed directly on the live theme at 12:17 — panel off, file `disabled:
   false`. The inverse of the September failure and the same lesson: **the toggle
   is not state, the file is.** Always verify by re-reading
   `config/settings_data.json` and comparing the checksum.

The repo copy also gained `content_for_index: []`, which the live file already had.

### HANDOVER, 28 Sep — the store is in TEST MODE and that is the real blocker

Told to sort the checkout inside 10 minutes with handover 45 minutes out. Magic is
not fixable in that window — it waits on Razorpay activating the integration.
What matters more, and had not been said out loud: **Shopify's Razorpay gateway
still has test mode ON, so the store takes zero rupees regardless of Magic.**
Critical path given to him, in order:

1. Magic Checkout Script embed **off** + Save → restores Shopify's checkout,
   proven working by order #1001. Fee goes to ~4% all-in instead of Magic's
   ~0.65%. That is a price, not an outage.
2. Razorpay **Test → Live**, generate live keys, paste into the Shopify gateway,
   **uncheck test mode**. His browser, never this transcript.
3. One real ₹80 purchase (Black Pepper 100 g), then refund. **This is now
   verifiable from both sides by Claude**, because the connector is on live keys.

**What he was told to promise the client:** the store is live and taking Razorpay
payments; Magic Checkout is a fee optimisation pending Razorpay activation, added
later with no downtime. **Not** promised for today.

**Also flagged before signing:** two items inside the ₹38,000 scope are not built —
the **owner dashboard** is still `dashboard-mockup.html` with sample data, and the
**WhatsApp Business community** has not been started. Better said up front than
discovered.

### Razorpay MCP connector — live 28 Sep, and it is READ-ONLY

Jnanottam connected a Razorpay MCP. **24 tools, every one of them `fetch_*`.**
There is no mutation, no settings write, no key management.

**What it CAN do — and this genuinely changes how Stage 3 is verified:**
`fetch_all_payments` · `fetch_payment` · `fetch_payment_card_details` ·
`fetch_all_orders` · `fetch_order` · `fetch_order_payments` ·
`fetch_all_refunds` · `fetch_refund` · `fetch_specific_refund_for_payment` ·
`fetch_all_settlements` · `fetch_settlement_with_id` ·
`fetch_settlement_recon_details` · `fetch_all_instant_settlements` ·
payment links, QR codes, payouts.

So the test matrix no longer depends on him screenshotting two dashboards.
**Rows 8 (order lands in Shopify), 10 (settlement lands) and the refund rows can
now be checked from BOTH sides by Claude** — Shopify's order against Razorpay's
payment record, by id and amount. That is exactly the "one system agreeing with
itself proves nothing" gate, and it is now automatable.

**What it CANNOT do — do not promise these:** turn COD off, switch test/live,
enter or rotate API keys, or touch any Magic Checkout setting. All of that stays
in Jnanottam's browser.

**THE CONNECTOR IS LIVE-MODE ONLY — established 28 Sep, do not re-read it as
"nothing happened".** Re-read after reconnecting: `fetch_all_orders` **0**,
`fetch_all_payments` **0**, `fetch_all_settlements` **0**. That is not evidence
of no activity. Shopify's order #1001 carries a **SUCCESS** Razorpay `SALE`
transaction for **₹1,155** with `test: true` on both the order and the
transaction — so a Razorpay test-mode payment certainly exists, and this
connector cannot see it. Either it is authorised on live keys only, or it is
pointed at a different Razorpay account. Either way the consequence is the same:

- **It cannot verify anything while the store is in test mode.** The Stage 3
  both-sides cross-check (rows 8, 10 and the refund rows) only starts working
  once the store is live.
- **It is the reason to go live rather than keep testing.** In test mode I am
  blind on Razorpay's side; in live mode every order can be matched by id and
  amount from both directions.

**It also closes the 28 Sep live-mode scare with evidence rather than reasoning.**
If the store had been running on live keys, order #1001's ₹1,155 would be sitting
in `fetch_all_payments`. It is not, and there are **zero live payments and zero
settlements on this account** — nothing real has ever been charged. Do not
re-open that question.

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
2. ~~**HSN and GST**~~ — **done 16 Sep.** 5% and an HSN code on all 63 rows,
   pushed to all 57 products. Twelve HSN/rate mismatches recorded in
   `docs/gst-classification.md`. What remains is Shopify's own
   **Settings → Taxes and duties**, which only Jnanottam can reach.
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

### Store readiness check — re-read from the Admin API 17 Sep

What is actually in the store, read from the Admin API, not assumed:

| | State |
|---|---|
| Theme | **PUBLISHED 28 Sep.** `Malnad Spices — build` is now `MAIN`; stock Horizon is demoted to UNPUBLISHED. A third theme, `Updated copy of Malnad Spices — build`, sits as a draft — Shopify's auto-generated update copy, not ours |
| Shop name | ~~"My Store"~~ **renamed to "Malnad Products" 16 Sep** |
| Active products | ~~**0.** All 57 are draft~~ **all 57 ACTIVE and on the Online Store channel, 16 Sep** |
| Prices | ~~₹0.00 on all 63~~ **all 63 priced 16 Sep** |
| Payments | KYC cleared 17 Sep. **Magic Checkout app installed but "Needs Activation"**, a second Razorpay app not yet installed, and **no provider is configured in Shopify Settings → Payments** — so nothing can take money yet |
| Policies | All six exist as of 17 Sep, but **five render as escaped text** (`&lt;h2&gt;`) on the storefront. Written, pasted, broken. Must be redone by hand |
| Ships to | **India only** — the 28-country international zone was deleted 16 Sep. 4 zones x 7 weight bands, 28 active rates, **but the figures are invented, not the courier's** |
| Domain | `malnadproducts.in` **bought** 17 Sep. WHOIS registrant verification pending (15-day ICANN clock), and **not connected** — `primaryDomain` still reads `8uysc8-kx.myshopify.com` |
| Billing address | correct: Malnad Spices, Horanadu, Chikmagalur 577181, +91 8431218956 |

**`storefront-design.html` is a mockup, not the site.** It is a static HTML
design for approval. Building it into the Horizon theme is Stage 2 and has not
been started.

Eight stages total, each with a gate. Full detail in `build-runbook.html`.
Stage 3 (payments) is gated hardest: the 16-row test matrix runs in test mode and
again live, and is not complete until a settlement is confirmed landed in the
client's bank.

### SEO — written and pushed 8 Oct. Every record had a null title.

Read first: `seo { title description }` was **null on all 57 products, all 9
collections and both pages**, so Shopify was falling back to the bare product
title. Google saw *"Black Pepper"* where it should see *"Malnad Black Pepper
100 g"*. The quotation promises "Basic SEO — page titles, descriptions", so this
was an unbuilt scope item, not a nicety.

**Source of truth is `catalogue/seo.py`**, same pattern as `descriptions.py`,
with a `check()` that fails the push rather than letting a bad record through.
Pushed as batched aliased `productUpdate` / `collectionUpdate` calls and
**verified by reading all 68 records back.**

The rules it enforces, each for a reason worth keeping:

- **No shop name in the SEO title.** `snippets/meta-tags.liquid` appends
  ` – {{ shop.name }}` **unless the title already contains it**, so a title
  carrying "Malnad Products" suppresses the append and one that does not gets it
  free. Titles are capped at **42 characters**; + 18 for the append = 60, which
  is Google's display width.
- **Local names where they are the search term** — nellikai, sikakai, antuvala,
  sasive, chekke, marati moggu, kishmish, elakki, sompu. A Kannada-speaking
  customer does not search "Indian gooseberry powder".
- **No health claims**, same regex discipline as the descriptions. "Diabeat" is
  whitelisted because it is the maker's product name, not a claim we make.
- **No prices in meta descriptions.** They change, and a stale Google snippet
  undercutting the live price is a consumer-law problem, not an annoyance.
- **No duplicates.** Duplicated meta descriptions across 57 pages is the commonest
  way a small catalogue gets flattened in search.
- **Origin named wherever true** — Horanadu, Kalasa, Koppa, Chikkamagaluru. Nobody
  else competes for "marati moggu online"; everybody competes for "buy almonds".

**Pages have no `seo` field on `PageUpdateInput`** — checked against the schema,
not guessed. Theirs go in as the `global.title_tag` and `global.description_tag`
metafields, which is what Shopify's own SEO editor writes.

**THE HOMEPAGE CANNOT BE SET FROM THE API.** Its title and meta description live
in **Online Store → Preferences** and need a browser. `shop.description` reads
`null`, which also means `og:description` falls back to the shop name on every
page that has no description of its own. The wording is parked in `seo.py` as
`HOMEPAGE_TITLE` and `HOMEPAGE_DESCRIPTION` so it is version-controlled and
consistent with the rest.

**Still missing from the SEO scope**, and all of it needs his login:
Google Analytics, Search Console, a Google Business Profile, and the free
**Shopify Search & Discovery** app — `appInstallations` shows only three apps, so
it is not installed and the collection pages therefore have **no filters**, which
the quotation also promises.

### Collection images — all nine now set, 8 Oct

Seven of the nine had `image: null` and were falling back to whatever pack photo
Shopify picked. Each now carries a deliberately chosen pack photograph with real
alt text, set through `collectionUpdate(input: {image: {src, altText}})` — `src`
takes a public URL, so they went straight off `raw.githubusercontent.com` pinned
to a commit SHA, the same route the 70 pack photos took.

**This is an improvement, not the finish.** Whole Spices and Coffee have proper
atmospheric brand art; the other seven have pack shots, which sit oddly beside
them. The real fix is still the two generated category images noted under
Storefront imagery. `cat-honey-comb.png` and `packs-three-up.png` remain orphaned.

### The accountant's monthly sheet — built 8 Oct

`scripts/gst_monthly_summary.py`. Quotation 02B promises "a one-page GST and HSN
summary you can hand to your accountant each month"; it did not exist.

Shopify's order export has **no HSN column** — HSN lives in our `compliance`
metafields — so the script joins the export to `catalogue/malnad-catalogue.csv`
**on SKU**, which was verified to match variant-for-variant in the live store.
Output is the HSN-wise table GSTR-1 wants: HSN, rate, quantity, taxable value,
CGST/SGST/IGST, total.

Three things it surfaces rather than smoothing over:

1. **The 10%-vs-5% defect appears on every run** until Settings → Taxes and
   duties is fixed, as tax-at-declared-rate against tax-as-Shopify-computed and
   the gap between them. Tested against the real order #1001: it reproduces
   ₹52.38 correct against ₹100.00 charged.
2. **The intra/inter split comes from the SHIPPING province**, not billing —
   under IGST s.10 the place of supply for goods is where delivery ends.
3. **Delivery is its own line**, because `taxShipping` is false and delivery on a
   taxable supply is normally a composite supply at the principal rate.

A product sold but absent from the catalogue gets **no HSN**, so it is reported
under "NEEDS ATTENTION" rather than silently dropped — that is the failure mode
if somebody adds a product in Shopify without telling us. Refunded and voided
orders are **excluded, not netted**, because the export cannot say which month
the refund belongs to.

Fixture at `fixtures/orders-export-sample.csv`, whose first order is order #1001
with its real figures.

### Owner's manual — written 8 Oct

`owner-manual.html` → `Malnad-Products-Owner-Manual.pdf`, 8 pages. Reuses the
quotation's stylesheet verbatim so the handover pack reads as one family; the
print variant inlines 58 woff2 files, built by the same approach as
`quotation-malnad-print.html`.

Twelve sections, written for Dheeraj and Dhanush rather than for us: what they
have · the order-day routine · **what must be printed on every pack** · changing
a price · the eight-item checklist for adding a product · taking something off
sale · counter sales as draft orders · refunds · the monthly export for the
accountant · **six things not to touch** · payments and where they stand · a
symptom-to-cause table.

Three sections exist because of findings in this file and would not be in a
generic manual:

- **Section 03** is the per-package declaration duty, stated as the biggest open
  risk in the shop, with the rubber-stamp suggestion as the cheap close. It also
  says plainly that resold sealed goods keep the maker's declarations.
- **Section 10** is the list of settings that quietly break things: Magic
  Shipping, the `Updated copy of…` theme, Republish Cart, deleting instead of
  drafting, COD, and test mode.
- **Section 05** leads with the **Active-but-not-published trap**, which cost us
  a day twice.

Payments are described in steady state with a dated note saying the website is
under Razorpay review, so the manual does not go stale the day approval lands.
JTACS is named as **"Jnanottam" only** and there are **no fill-in blanks**, per
the standing instructions.

### THE REAL ANSWER — MAGIC HAS TWO FLOWS, AND WE HAD THE WRONG ONE. 8 Oct ~17:00

**Razorpay support (Sushil, after Syed was pushed), in writing:**

> **1. Public App** — *"a completely self-serve onboarding process. In this setup,
> **orders are not processed through Magic Checkout**. Instead, after the
> customer's address is verified via OTP, they are **redirected to the Shopify
> checkout page** to complete their purchase."* Example: `nutrova.com`.
>
> **2. Private App** — *"does not follow a self-serve process and requires the
> development of a custom app that is exclusive to your store… the Magic Checkout
> will handle address and payment processes, and the Shopify redirection will no
> longer occur."* Needs the **Shopify Collab code and Shopify URL**. Example:
> `myborosil.com`.

**THAT IS WORD FOR WORD WHAT THIS STORE DOES.** OTP → address → redirect to
Shopify's checkout. **It was never broken.** We installed the public app from the
Shopify app store, and the public app is an address collector by design.

**SO THE SECTION BELOW IS WRONG AND IS SUPERSEDED.** I concluded at 16:35 that it
was "a Razorpay-side defect, not a configuration error". It is neither — it is a
**product tier**. That was the eighth wrong call on this integration, and the only
reason the right answer surfaced is that Jnanottam kept the support chat open and
pushed past two vague replies from the first agent.

**Everything the earlier sections eliminated was still worth eliminating** — the
embed, the scopes, the customization, the sales channel, Platform Settings, the
deactivation test. None of it was the cause, but the deactivation test is exactly
what forced support to explain the two flows. Keep those records.

**ACTION TAKEN 8 Oct: the public app is UNINSTALLED**, on Sushil's instruction,
and Razorpay's team is building the private app. Verified from the Admin API
immediately after:

| Check | Result |
|---|---|
| `appInstallations` | **Razorpay app gone.** Only Shopify Messaging and the Claude connector remain |
| **Shipping** | **INTACT — both profiles, 4 zones each, 7 rates each. 28 + 28.** The real risk, since that app held `write_shipping` |
| Products | 57, untouched |

**ONE ORPHAN LEFT BEHIND.** The live theme's `config/settings_data.json` still
reads 8082 bytes / `c6b03740…` and still carries the app block
`shopify://apps/razorpay-cod-magic-checkout/blocks/magicx-script/…` with
`disabled: false`, pointing at an app that no longer exists. Shopify ignores app
blocks whose app is gone, so it renders nothing — but **mention it to Razorpay
before the private app is installed**, because a stale block can confuse a fresh
install.

**THE COLLABORATOR CODE — scope it.** The private app needs a Shopify Collab code,
which gives Razorpay's engineers access to the client's store. It does **not**
consume a staff seat (Basic allows 2). **Grant Themes, Apps and Orders; not
Customers, not Finances, not Settings.** It is Dhanush's data, so Dheeraj should
be told a Razorpay engineer has scoped access for the build.

**THE FEE QUESTION IS NOW ANSWERABLE AND STILL UNANSWERED:** with the private app
owning the whole checkout, does **Shopify's 2% third-party fee** still apply? If
it disappears, Magic is worth ~1.5% net. If it does not, Magic is 0.5% for a
nicer address form. Put it to them before accepting the build.

**Until the private app lands, the store sells exactly as before** — Shopify
checkout → Razorpay Secure, ~4% all-in. **Do not gate the handover on the private
app.**

### SUPERSEDED by the section above — the conclusion here was wrong

### SETTLED 8 Oct 16:35 — MAGIC CANNOT COMPLETE A PAYMENT ON THIS ACCOUNT

**The decisive test, and it is conclusive.** With the Razorpay gateway
deactivated in Shopify → Settings → Payments, a checkout taken through Magic's
modal reached Shopify's checkout and showed:

> **"This store can't accept payments right now."** — Pay now greyed out.

**Magic offered no payment method of its own.** So on this store Magic Checkout is
purely an address-collection front end: it takes a mobile number, an OTP and an
address, then hands the customer to Shopify's checkout, where **Razorpay Secure**
takes the money. The gateway was reactivated immediately; the store was without a
payment method for about two minutes and has never taken a real order, so nothing
was lost.

**SHOPIFY'S OWN CHECKOUT NAMES THE CULPRIT.** The Payment section reads
**"Razorpay Secure (UPI, Card, Int'l Card, Apple Pay)"** with *"You'll be
redirected to Razorpay Secure to complete your purchase"*, and Pay now goes to
`api.razorpay.com/v1/checkout/hosted` — byte for byte the same page reached at
15:25 **before Magic was enabled at all**. Razorpay **Secure** is a different
product from Magic Checkout, and Secure is what is running.

**So Syed's FIRST answer was right and his second was wrong.** *"You have
integrated the API key, and the Shopify store has been linked, so it is
redirecting to the Shopify store"* describes exactly what happens. *"There is no
scenario where Shopify prevents Magic Checkout from completing the checkout"* is
contradicted by the store's own behaviour with the gateway removed.

**EVERYTHING A MERCHANT CAN DO HAS NOW BEEN TRIED. Do not re-chase any of it:**

| Checked | Result |
|---|---|
| **Platform Settings** (the documented store-ID step) | **Does not exist in this account — live OR test.** Confirmed by reading the live sidebar: Control Center · Loyalty · Checkout… · COD Setup · RazorpayID… · RTO Reduction… · Delivery Statuses · Shipping Setup · Order Settings · Upload… |
| Payment customization *"Hides COD payment method for Non MagicX shipping methods"* | **Deleted. No change.** Razorpay's own documented step. |
| App embed | Enabled and persisted — verified in `config/settings_data.json`, not the toggle |
| App scopes | 41, every one Magic needs |
| Website registration | Approved 8 Oct |
| Live mode, `Enable Magic Checkout` | On |
| Magic Checkout sales channel | **Does not exist** — `publications` returns only Online Store and Point of Sale |
| Gateway deactivated | **Magic offered nothing** |

**CONCLUSION: it is a Razorpay-side defect, not a configuration error.** The
escalation goes to `magic-checkout-support@razorpay.com` with the deactivation
test as the closing evidence. `docs/razorpay-magic-support-request.txt` carries
the full list.

**THE EMBED SHOULD BE OFF.** It costs **0.5% + 18% GST** (Razorpay support, in
writing) and buys nothing but an extra OTP step for the customer, who lands on the
same Shopify checkout either way. Turning it off is a strict improvement.

**WHAT THE STORE ACTUALLY RUNS ON, and it works:** Shopify checkout → Razorpay
Secure, at roughly **4% all-in** (Shopify's 2% third-party fee plus Razorpay's
transaction fee and GST). Order #1001 proved this route end to end in test. **The
handover does not change** — the store sells, the money lands, and Magic is a fee
optimisation sitting on Razorpay's ticket.

### MAGIC'S 0.5% IS ADDITIVE — the premise of the whole decision was wrong. 8 Oct

**Razorpay support, in writing, answering what fee applies:**

> *"Two charges will apply: one for the transaction along with 18% GST on the
> transaction fees, **and another** for using Magic Checkout, which is 0.5% plus
> 18% GST on the 0.5%."*

**So Magic Checkout's fee is an ADD-ON to the normal transaction fee, not a
replacement rate.** Every comparison in this file that reads "Magic ~0.65%
against ~4%" is wrong and was wrong from 17 Sep. The ~0.65% was never an
achievable all-in rate.

**What it actually costs, in the state the store is in right now:**

| | |
|---|---|
| Shopify third-party gateway fee (Basic) | 2% |
| Razorpay transaction fee | ~2% + 18% GST |
| **Magic Checkout** | **+0.5% + 18% GST** |
| | **~4.5%** |

**And Magic is not completing a single checkout**, so that 0.5% buys nothing. On
the ~₹14.35 lakh/year turnover implied by the quotation's ₹28,700 figure, it is
about **₹7,175/year for a feature that drops out before its own payment step**.
**Recommendation given and recorded: turn the embed off.** No function is lost,
the 0.5% stops, and the customer stops doing an OTP for nothing.

**THE ONE QUESTION THAT DECIDES WHETHER MAGIC IS EVER WORTH IT**, put to support
and still unanswered: **when Magic owns the full checkout, does Shopify's 2%
third-party gateway fee still apply?**

- **If it disappears** → Magic is worth ~1.5% net (2% saved, 0.5% paid), roughly
  **₹21,500/year**. Real, but half what the quotation costed. Worth fixing.
- **If it does not** → Magic is a pure 0.5% cost and should stay off permanently,
  and the original reason for choosing it evaporates.

**SUPPORT ALSO CONTRADICTED ITSELF, and it is worth recording how that was
handled.** Syed's first message: *"you have integrated the API key, and the
Shopify store has been linked, **so it is redirecting** to the Shopify store."*
His second: *"There is no scenario where Shopify prevents Magic Checkout from
completing the checkout process itself."* Both cannot hold. Accepting the first
would have sent us to deactivate the gateway for nothing; accepting the second
closes the ticket with the behaviour unexplained. **Pushing back on the
contradiction is what produced the fee answer**, which is the single most
valuable thing support has said.

**THE EVIDENCE THAT KILLS "IT IS DESIGNED THAT WAY".** Magic's own modal shows
its three steps across the top: **Contact › Address › Payment**. Contact and
Address complete; **Magic's Payment step never renders** and the customer is
dropped on Shopify's checkout. A product that intends to hand off after the
address step does not advertise a Payment step it never shows. So this is a
drop-out mid-flow, not a designed handoff — and that is the form the question to
support now takes.

**Q4 is still unanswered**: why Abandoned sessions reads All 0 for a session
taken through the modal to the address step and left.

### MAGIC — THE HANG IS FIXED, BUT IT DOES NOT OWN THE CHECKOUT. 8 Oct

**Read this before the section below it, which over-called the result.** At 15:32
I wrote "Magic Checkout works — closed after eleven days" on the strength of the
modal rendering. **That was my seventh wrong call on this integration** and it was
made from one screenshot, before following the flow to the end. The modal
rendering is necessary, not sufficient.

**WHAT ACTUALLY HAPPENS, 15:37:**

1. Magic's modal opens correctly — brand colour, right cart, right variant image.
2. Contact step: mobile, **OTP**. Works.
3. Address step. Works.
4. The customer is then dropped on **Shopify's own checkout**,
   `malnadproducts.in/checkouts/cn/<token>`, contact and address pre-filled from
   the modal. Payment completes from there.

**That URL is the exact marker used on 28 Sep to prove the Razorpay Secure
route.** So by this project's own established test, the order completes the
Shopify-gateway way at **~4% all-in, not Magic's ~0.65%**.

**CONFIRMED FROM RAZORPAY'S OWN DASHBOARD, 15:46.** Magic Checkout → **Abandoned
sessions** reads **All 0 · Open 0 · COD 0**, *"No abandoned sessions found"* —
fifteen minutes after a session was taken through the modal to the address step
and left. **Magic has no record of a checkout it supposedly ran.** That is the
strongest available evidence that it is not owning the session, and it cost
nothing to obtain. (Small caveat kept honest: Shopify's own abandoned checkouts
took ~10 minutes to register on 28 Sep, so a late arrival is not impossible.
Re-check before treating it as final.)

**Control Center is a settings hub, not a session log** — COD Configuration, RTO
Prediction, Checkout Settings, Customer Login with Razorpay, each with Configure
and User Manual. Nothing to read there. The screens that carry session data are
**Abandoned sessions** and **Analytics**, both under Insights.

**RULED OUT FOR FREE, from the Shopify side:** Razorpay's setup guide says to add
products to a *"Magic Checkout sales channel"*. `publications` on this store
returns exactly **two** — Online Store (`Publication/177970544753`) and Point of
Sale. **There is no Magic Checkout channel to publish to**, so that step cannot
be the cause and cannot be actioned. Put it to Razorpay rather than hunting for it.

**THE CONSEQUENCE THAT MATTERS COMMERCIALLY, AND IT IS NOT NEUTRAL.** If Magic is
not earning the fee difference, the embed is **worse than having it off**: the
customer now does an OTP step they did not have to do, and arrives at exactly the
same Shopify checkout they would have reached directly. That is friction with no
payoff. **Recommendation given: turn the embed off until Razorpay confirms the
fee, and turn it back on when they do.** Nothing is lost — the rate is already
~4% either way.

**`docs/razorpay-magic-support-request.txt` is rewritten for this question.** The
old one described a modal that never loaded, which no longer happens. The new one
asks the two questions that decide it — *is the handoff expected* and *which fee
applies* — plus why the session is unrecorded, the missing sales channel and the
missing Platform Settings screen, and lists everything already verified so support
cannot send us round the loop.

**TWO THINGS THE LIVE CHECKOUT DID SETTLE, FOR FREE:**

- **The 10% tax defect is live and charging.** Shopify's checkout showed
  *"Including ₹4.54 in taxes"* on a ₹50 item. `50 × 10/110 = 4.545`; correct at 5%
  inclusive is `50 × 5/105 = 2.38`. **Confirmed outside test mode**, over-declaring
  4.3% of goods value. Shipping is correctly untaxed — ₹4.54 is computed on goods
  alone, consistent with `taxShipping: false`.
- **Email is captured** (`jnanbelliappa135@gmail.com`). Shopify's checkout
  requires it, so while the flow ends there the Email Field concern is moot. It
  becomes live again only if Magic ever owns the whole flow.
- **Shipping right for the third time**: ₹50 goods + **₹40** = ₹90, the Karnataka
  0–0.5 kg band exactly.

---

### SUPERSEDED — written 15:32 before the flow was followed to the end

### MAGIC CHECKOUT WORKS — 8 Oct 15:32 IST. Closed after eleven days.

The modal **opens and fills**: a three-step Contact → Address → Payment flow on
`malnadproducts.in` itself, branded *Secured by Razorpay*, order summary showing
**Chekke (Cinnamon Bark), Qty 1 · 100 G, ₹50** with the correct variant pack
photograph. No redirect to Shopify's checkout. **It is intercepting.**

**THE 29 SEP DIAGNOSIS WAS RIGHT, and this confirms it from the storefront
rather than from the settings screens.** Magic's *Enable Magic Checkout* toggle
exists **only in live mode**. The storefront ran in test context, so Razorpay
resolved the store where Magic had no enabled configuration, returned nothing,
and the modal rendered its chrome and waited — with a clean console, because an
empty lookup is not an exception. Website approved → gateway live → it resolves.
**Nothing in the theme, the app, the scopes, the domain or the activation was
ever wrong.** Every one of those was checked and every one was a wrong call.

**Commercially this is the whole reason Magic was chosen:** ~0.65% against the
Shopify-gateway route's ~4% all-in, about **₹28,700/year** to the client. It is
also the thing Jnanottam said on 28 Sep he would not hand over without.

**Two things verified good from the modal itself:**
- **The panel is brand green, not Razorpay's `#528FF0` blue.**
- It reads **Malnad Spices**, the Razorpay account's business name — which
  matches the packer name and the FSSAI licence printed on the packs, so it is
  the right name to show. **Not** the shop-name mismatch finding; do not raise it.

**ONE REAL DEFECT STILL VISIBLE: the Contact step asks for a mobile number only.**
No email at that step, and `Email Field` was last read as **Optional** on
`/app/magic/settings/magicx-store-settings`. This store sends order confirmations
and dispatch notices **by email only** — no SMS app, by decision — so a customer
who completes checkout without an email gets **no confirmation at all** and is
reachable only by WhatsApp. Set it to **Mandatory**. Checking costs nothing:
continue to the Address step and look, no payment required.

**What remains on the payment chain:**

1. `Email Field` → Mandatory.
2. **One real paid order**, which is the only thing that proves settlement lands.
   It should be **Dhanush's or Dheeraj's money into their own bank**, not
   Jnanottam's — that is what the test exists to prove.
3. **Tax still computes at 10%**, not 5% — Settings → Taxes and duties, India
   country rate to 2.5%. 4.33% of goods value on every sale, out of the client's
   margin.
4. **Reconnect the Razorpay MCP connector** for the both-sides cross-check.

### RAZORPAY APPROVED THE WEBSITE — 8 Oct 15:10 IST

`https://malnadproducts.in` reads **✓ Approved** on
`dashboard.razorpay.com/app/website-app-settings/business-website-details`.
**Generate Key is enabled** and the dashboard Test Mode toggle is **off**. Trial
banner 69 Free* Days. The 24–48 hour clock that started 7 Oct 12:09 returned
inside 27 hours.

**This clears the root cause recorded on 29 Sep.** Live keys can now exist, so
the store can take real money for the first time.

**THE GATEWAY DID NOT ASK FOR KEYS — and that is expected, not a gap.**
Jnanottam unticked Shopify's test mode and reactivated
`01 Cards, UPI, NB, Wallets by Razorpay`; it asked for nothing. That provider
holds a **connection** to the Razorpay account rather than a stored Key ID and
Secret, so reactivating keeps it and the live/test choice is Shopify's own
checkbox. **No key was generated** — correct, because an unused live Key Secret
is a credential to look after for nothing.

**Whether the gateway is genuinely live is NOT yet proven.** A checkout reached
`api.razorpay.com/v1/checkout/hosted` at 15:25 for **₹90**, showing real UPI
apps, netbanking, wallets and a QR. **That appearance proves nothing** — the
28 Sep record already establishes that Razorpay's *test* checkout renders the
same chrome, and over-reading it was a logged wrong call. Do not repeat it.
Two free ways to settle it, neither needing a payment:

1. **Razorpay → Transactions, live mode.** Razorpay records an order the moment
   the hosted page opens, even unpaid. A ₹90 entry at ~15:25 in live mode settles
   it; present only in test mode means the connection is still on test
   credentials.
2. **The order record**, once anything is paid: `test` must read **false** on
   both the order and the transaction. Order #1001 reads `true`.

**Shopify saw nothing from that attempt** — still 1 order and 1 abandoned
checkout, both 28 Sep. Normal: abandoned checkouts take ~10 minutes to register
and an order only exists on payment.

**One thing it did prove.** ₹90 = **₹50 goods + ₹40 delivery**, and ₹40 is exactly
the Karnataka 0–0.5 kg band. **Weight-based shipping is correct on a live cart —
the third independent confirmation** (920 g → ₹55, 1,570 g → ₹85, now ≤0.5 kg →
₹40).

**THE MAGIC EMBED IS BACK ON — 8 Oct 15:31, verified from the file.**
`config/settings_data.json` reads **8082 bytes, md5
`c6b037400494325e780db39d1ce0a7f5`** — byte-identical to the pre-disable state,
so `disabled: false`. Same trap as both previous attempts: the editor's **Save
was greyed out**, which is ambiguous between "already saved" and "never
registered". **Only the file settles it.**

**MAGIC CAN BE TESTED WITHOUT PAYING.** The symptom was always a modal that
opened and hung. So: add to cart → Check out → if the modal **fills**, Magic
works; if it **hangs**, it does not. The answer arrives before the payment step.
If it hangs, set the embed back off and send
`docs/razorpay-magic-support-request.txt`.

**The Razorpay MCP connector is disconnected again** — no `fetch_*` tools in the
session, and the OAuth flow cannot run from a non-interactive container. Until
Jnanottam reconnects it in claude.ai connector settings, **Razorpay's side cannot
be read from here at all**, so every live/test question has to be answered off
his screen. Reconnecting it is what finally makes the both-sides cross-check
(Shopify order against Razorpay payment, by id and amount) possible.

**The end-to-end money test should be the client's, not Jnanottam's.** What needs
proving is that settlement lands in **Dhanush's** bank; ₹90 of Jnanottam's own
money does not prove that any better, and he said plainly he did not want to
spend it.

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
| `scripts/render_declarations_test.py` | **Renders the declarations block** and checks the gap treatment |
| `scripts/build_shipping_rates.py` | **Generates the 28 weight-based shipping rates** from eight numbers |
| `money-explained.html` | **How the money works** — client-facing, written for Dr. Dhanush |
| `Malnad-Products-How-The-Money-Works.pdf` | The same, 7 pages, for handover |
| `assets/qr/` | **QR codes for `malnadproducts.in`** — static, SVG and PNG, black and brand green |
| `owner-manual.html` | **The client's owner's manual** — how to run the shop, 12 sections |
| `Malnad-Products-Owner-Manual.pdf` | The same, 8 pages, for handover |
| `scripts/gst_monthly_summary.py` | **The accountant's monthly HSN sheet** from a Shopify order export |
| `catalogue/seo.py` | **All 68 SEO titles and meta descriptions** — source of truth, re-pushable |
| `catalogue/shopify-ids.json` | handle → Shopify gid for all 57 products and 9 collections |
| `fixtures/orders-export-sample.csv` | Order-export fixture built from the real order #1001 |
| `theme/` | Theme source we add to Horizon — see `theme/README.md` |
| `policies/` | Refund, shipping, terms, contact, legal notice — **paste by hand**, see below |
| `docs/store-setup.md` | What is left and who does it, in full |
| `docs/gst-classification.md` | **HSN per product and the 12 rate mismatches**, for the CA |
| `docs/your-steps.md` | **The same list in plain English, 8 numbered steps.** For Jnanottam |
| `docs/stage1-catalogue.md` | Metafield definitions and import procedure |
| `docs/product-photography.md` | Storefront palette and image direction |
| `docs/image-prompts.txt` | The three prompts, plain text |
| `catalogue/intake.md` | Intake log, 65 products, findings |
| `catalogue/extracted.md` | Everything read off the packs — brands, MRPs, findings |
| `catalogue/malnad-catalogue.csv` | **The working sheet** — 57 products, 63 rows, gaps left empty |
| `catalogue/gaps.md` | Generated: every outstanding field and who supplies it |
| `catalogue/tax-schedule.md` | Generated: HSN and GST per product — **applied**, 5% throughout |
| `catalogue/quantities.md` | Net quantity for all 65, from the catalogue names |
| `catalogue/descriptions.py` | **All 57 product descriptions** — source of truth, re-pushable |
| `catalogue/price-request-remaining.txt` | Sent: the 36 outstanding selling prices |
| `catalogue/client-message.txt` | Sent: the information-gap list |
| `catalogue/price-list-request.txt` | Drafted: the price-list request |
| `catalogue/pack-size-request.txt` | Drafted: pack sizes for the 9 unlabelled lines |
| `templates/catalogue-template.csv` | Now Claude's working format, not a client form |
| `build-plan.html`, `quotation.html` | **Superseded.** Custom build, and the earlier Ayurveda quotation. |

### WHERE FORM DATA LANDS — read from the live store 8 Oct

Asked where everything a customer types on the site ends up. **Exactly three
inputs exist**, and they go to three different places. Read from the theme and
the Admin API, not from memory.

| Input | Fields | Where it lands | Durable? |
|---|---|---|---|
| **Contact form**, `/pages/contact` | Name · **Email (required)** · Phone · Message | **An email only.** Nothing is stored in Shopify | **No** |
| **Footer newsletter**, "Word from the hills" | Email | A **customer record** with marketing consent. Admin → Customers | Yes |
| **Checkout** | Name · email · phone · delivery address | The **order** + a **customer record** | Yes |

**The contact form is the weak point, and it is the answer to the question.**
Horizon's `blocks/contact-form.liquid` uses `{% form 'contact' %}`, which
**emails and does not store**. Shopify has no admin list for built-in
contact-form submissions. It goes to the **sender email** on
**Settings → Notifications**, which is a *different* field from the store email
on Settings → General and **is not exposed in the Admin API**. Both addresses
that *are* readable — `shop.email` and `shop.contactEmail` — read
`drjhrnd5@gmail.com`, so that is almost certainly the destination, but
**Settings → Notifications is the one screen that settles it** and only
Jnanottam can see it. Shopify spam-filters the message body and prefixes
`[SPAM]` to the subject of anything flagged; flagged mail still arrives, so it
can land in Gmail's spam rather than vanish. **If nobody opens that inbox, the
enquiry is gone — there is no second copy.**

**The footer signup emails nobody.** Block `email_signup_crihX7`, type
`email-signup`, in `sections/footer-group.json`. It creates or updates a
customer with email-marketing consent. **0 customers** in the store, so it has
never been used — expected with no real traffic. No newsletter tool is
connected, so addresses just accumulate; Shopify Email is free to 10,000
sends/month if the list is ever wanted.

**THERE IS NO BULK-ORDER FORM.** Checked the live theme and the whole repo —
nothing. The contact form has four fields and none is about quantity, and no
page invites a bulk enquiry. Consistent with the quotation, which lists
**"wholesale or dealer pricing"** as explicitly out of scope. So a bulk enquiry
arrives today as a contact-form email into that Gmail, or on the two footer
phone numbers.

Two ways to add one, if asked:
- **Extra fields on the existing contact form** — product, quantity, delivery
  town. Any input named `contact[<id>]` arrives in the same email, labelled.
  Theme edit, so duplicate → edit → publish; live theme writes are blocked here.
- **Shopify Forms**, free Shopify app. Submissions are stored **in the admin**,
  not in an inbox, and it can email a notification too. **Preferred**, precisely
  because it removes the single-inbox failure above.

**Nothing records who merely visited.** No Google Analytics, no Search Console,
no Search & Discovery. The only trace of a customer is a signup, an abandoned
checkout (Orders → Abandoned checkouts; one, 28 Sep, ₹685) or an order.

### ABOUT PAGE WAS DESCRIBING A RETIRED BEHAVIOUR — fixed 8 Oct

Found while answering the above. The live About page said:

> *"Where a pack does not carry one of those, the page says 'Not printed on this
> pack'. We would rather show you a gap than a number we cannot stand behind."*

**The theme has not done that since 16 Sep.** The client's instruction was that
an undisclosed field is simply not mentioned; `show_gaps` is **off** and blank
rows are omitted entirely. So a customer reading the About page was told to
expect a notice the product pages never show — and it is exactly the kind of
inconsistency a payments reviewer picks up.

Rewritten through `pageUpdate` on `Page/112875372657` and verified:

> *"Nothing on a product page is worked out, estimated or filled in for you. If a
> figure is on the pack it is on the page, and if it is not on the pack the page
> does not carry that line at all."*

Same promise, accurate to what the theme does. **`storefront-design.html` still
shows the old laterite "Not printed on this pack" rows** and remains out of step
with the theme on that one point — it is a mockup, so this is cosmetic, but do
not treat it as the reference for that row.

### QR code for the storefront — made 8 Oct, and it is STATIC on purpose

Dr. Dhanush asked for a QR code for `malnadproducts.in` that is free and lasts
for life. **The trap in that request is real**: most free QR generators hand out a
**dynamic** code that encodes *their* domain and redirects to yours. It is free
until the trial ends or the company folds, and then every QR printed on a pack, a
board or a van stops working. Nobody reprints packaging.

**So these are STATIC.** The URL is encoded directly in the pattern. No third
party, no redirect, no account, no expiry. It works for exactly as long as
`malnadproducts.in` does, and it cannot be switched off by anyone.

Generated with `segno`, error correction **H (30%)** so a scuffed sticker or a
rain-marked board still scans. Version 4, 41×41 modules.

| File | For |
|---|---|
| `malnadproducts-qr-black.svg` | **Print.** Vector — scales to a hoarding without softening |
| `malnadproducts-qr-green.svg` | The same in brand `#1F4034`, for anything designed |
| `malnadproducts-qr-black.png` | 1640×1640 — WhatsApp, posters, anyone wanting a raster |
| `malnadproducts-qr-green.png` | 1640×1640, brand green |

**Both were decoded back with OpenCV and return exactly
`https://malnadproducts.in`** — checked rather than assumed, because a QR printed
on packaging that encodes the wrong thing is not a defect you can patch.

**Rules for whoever prints it:** keep the white margin around it (it is already
in the files — do not crop); never print it smaller than about 2 cm square;
dark-on-light only, never inverted; and if a logo is ever dropped in the middle,
re-test the scan, because the H error correction allows it but only just.

### How the money works — client document, 8 Oct

`money-explained.html` → `Malnad-Products-How-The-Money-Works.pdf`, 7 pages, same
stylesheet as the quotation and the owner's manual so the handover pack reads as
one family.

Written for Dr. Dhanush, not for us. Ten sections: the short version · how a
customer pays · **one ₹1,055 order followed from Monday to Wednesday** · what is
deducted · when it reaches the bank · what he actually has to do · refunds ·
counter sales · GST and the accountant's sheet · when it starts.

Four things it is careful about:

1. **The two fees are deducted in different ways**, which is the part people get
   wrong. Razorpay's comes **out of each payment** before the bank; Shopify's is
   **billed monthly** like a phone bill. The document says plainly not to expect
   them to reconcile in the bank statement.
2. **No invented fee figures.** The Razorpay rate on this account was never read,
   so the document points at the dashboard, where every payment shows its exact
   fee, instead of printing a number that might be wrong.
3. **Settlement timing is Razorpay's published T+2 working days**, with the real
   caveats — Sundays, bank holidays and the 2nd and 4th Saturdays do not count,
   payments are batched into one deposit, and **the account's own dashboard is the
   figure to rely on**.
4. **It names the last open gate honestly**: no real money has gone through yet,
   so the chain is not proven. It asks him to buy one ₹50–80 pack from his own
   shop and watch it land — framed as paying himself for certainty.

Magic Checkout is mentioned in one sentence as a background fee improvement that
**changes nothing about how he is paid**. No jargon, no ticket history.

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
