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
| **Razorpay Magic Checkout** | Shopify adds 2% on Basic because Shopify Payments is unavailable in India. Magic Checkout is ~0.65% and currently falls outside that fee. Saves ~₹28,700/year. Flagged to the client as a gap in Shopify's rules, not a guarantee. |
| **Prepaid only** | Client instruction. Also removes COD refusal losses entirely. |
| **WhatsApp community on the free Business App** | Communities only exist on the Business App; the API cannot run one, and a number moved to the API loses Communities permanently. API is priced as a separate optional upgrade, triggered by the 256-contact broadcast cap. |
| **Owner dashboard included at no charge** | Listed at ₹8,000 then discounted to zero, so the client sees the value. Total stays ₹38,000. |
| **Offline sales as real Shopify draft orders** | Not a dashboard field. This way stock decrements, a GST invoice is raised, and the website cannot sell what was already sold at the estate gate. Draft orders work on Basic and on the Shopify phone app. |
| **Dashboard reads the Admin API, read-only** | Scopes `read_orders`, `read_products`, `read_customers` only. No write scope, no payout scope. Free on Basic. |
| **OPEN 16 Sep — dashboard write access** | Jnanottam asked whether the dashboard can add products, remove products and enter tracking numbers. All three are possible, but they need write scopes, which reverses the read-only decision above and the promise in `build-runbook.html` Stage 4. Recommended split: **tracking entry yes** (`write_fulfillments` only, genuinely repetitive, low blast radius); **product add/remove via Shopify's own free admin app**, unless it is built as a guided form that enforces the `compliance` metafields, the category tag and the `Malnad delivery` profile — a naive add-product form would silently create products with no declarations and no shipping. Awaiting his call. |
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
`policies/` and pasted by hand. That is the one hard blocker on the Razorpay
prerequisite list.

**`deliveryProfileUpdate` cannot touch zones at all, and says nothing.** It
accepts `zonesToCreate`, `zonesToUpdate`, a zone rename and a method rename,
returns `userErrors: []`, and changes nothing. Its top-level fields *do* work —
`zonesToDelete` and `variantsToAssociate` both applied. **Use
`deliveryProfileCreate` to build zones**; that works completely, weight
conditions and all. This cost a round trip where the only zone was deleted and
could not be recreated on the default profile, leaving the shop shipping
nowhere until a new profile was made.

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

**Known trap:** the default **General profile now has no zones**, so a product
added later lands there and shows **no delivery option at checkout**. Recorded
in `docs/your-steps.md`. It cannot be fixed from here — zones cannot be added to
the default profile through the API.

**Origin does not need modelling — client answer 16 Sep.** Asked whether
dispatching from Horanadu or from Kalasa changes the charge: *"5rs + -"*. About
five rupees either way, so a single origin is correct and a second location
group would be false precision. The existing rounding already absorbs it: rates
round **up** to the nearest ₹5 and each band charges at its **top** weight.

**Still outstanding: the eight numbers.** A base and a per-kg figure for each of
the four zones, off the courier's rate card. That is the only input
`scripts/build_shipping_rates.py` needs to replace all 28 rates.

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

### Store readiness check — 16 Sep

What is actually in the store, read from the Admin API, not assumed:

| | State |
|---|---|
| Theme | **Live theme is still stock Horizon.** Our build is in the unpublished `Malnad Spices — build` — publishing it is Jnanottam's |
| Shop name | ~~"My Store"~~ **renamed to "Malnad Products" 16 Sep** |
| Active products | ~~**0.** All 57 are draft~~ **all 57 ACTIVE and on the Online Store channel, 16 Sep** |
| Prices | ~~₹0.00 on all 63~~ **all 63 priced 16 Sep** |
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
| `scripts/render_declarations_test.py` | **Renders the declarations block** and checks the gap treatment |
| `scripts/build_shipping_rates.py` | **Generates the 28 weight-based shipping rates** from eight numbers |
| `theme/` | Theme source we add to Horizon — see `theme/README.md` |
| `policies/` | Refund, shipping, terms, contact — **paste by hand**, see below |
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
