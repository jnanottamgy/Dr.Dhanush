# What is left, and who does it

Stage 2 is built. This is the list of things the Shopify connector cannot do,
so they need Jnanottam in a browser, plus the decisions that are the client's.

Everything here was checked against the live store on 16 Sep, not assumed.

---

## 1. Rename the shop — 30 seconds, fixes five things at once

**Settings → Store details → Store name.** It is still **"My Store"**.

This one field is worth doing first because it feeds:

- the header wordmark on every page of the theme;
- the browser tab title;
- order confirmation and shipping emails;
- the **privacy policy body**, which is Shopify's maintained template and renders
  `{{ shop_name }}` literally — today it reads *"My Store operates this store"*;
- the checkout header.

Set it to **Malnad Spices**.

There is no Admin API mutation for the shop name on any plan, so this cannot be
scripted. It is not a connector limitation.

## 2. Paste the four policies — Razorpay will not activate without them

**Settings → Policies.** The connector has `read_legal_policies` but **not**
`write_legal_policies`, so these cannot be pushed from here. The text is written
and ready in this repository:

| Policy | File | Status in store |
|---|---|---|
| Refund and returns | `policies/refund.html` | **missing** |
| Shipping | `policies/shipping.html` | **missing** |
| Terms of service | `policies/terms.html` | **missing** |
| Contact information | `policies/contact.html` | **missing** |
| Privacy | — leave Shopify's | present, and it is the maintained template |

Paste each file's contents into the matching box. Shopify's policy editor takes
HTML — use the `<>` source view, not the rich text view, or the markup shows as
text.

**Leave the privacy policy alone.** Shopify maintains that template and updates
it as privacy law changes. Replacing it with our own writing would be a
downgrade. It only needs the shop rename in step 1 to read correctly.

Once pasted, the footer policy list fills in by itself — that block is already
in the theme and renders whatever policies exist.

### Terms we chose, and you may want to change

None of these came from the client; they are conventional for Indian food retail
and are flagged so he can overrule any of them in one line.

| Term | What we wrote |
|---|---|
| Window to report damage or a wrong item | **48 hours** from delivery |
| Refund turnaround once accepted | **5 to 7 working days** |
| Dispatch time | **2 to 3 working days** |
| Delivery time after dispatch | **3 to 7 working days** |
| Who pays return delivery | **Us**, where the fault is ours or the courier's |
| Opened food packs | **Not returnable** unless defective |
| Jurisdiction | **Chikkamagaluru, Karnataka** |

## 3. The shipping rate is ₹379 and will kill every order

**Settings → Shipping and delivery.**

The India zone charges a flat **₹379**. That is Shopify's placeholder, not a
decision — the international zone was on ₹1,800 before it was deleted.

Six of the seeds sell at ₹140. A ₹379 delivery charge on a ₹140 bag is more than
twice the goods. Nobody completes that checkout. **This is the single most
commercially dangerous setting in the store right now.**

It needs the client's real courier rates. Not something to invent from here.

While in that screen, two cosmetic fixes the API silently refuses — it accepts
the mutation, returns no error, and changes nothing:

- zone name **"Domestic"** → *India*
- method name **"मानक"** → *Standard delivery*

"मानक" is Hindi for "standard" and is what a customer sees at checkout on an
otherwise English store.

## 4. Prices — 36 variants across 33 products are ₹0.00

These cannot be published; a draft at ₹0 that goes live is orderable for free.
All of them are packs that print no MRP, so the figure has to come from the
client. They carry the `needs-price` tag.

- all **18 whole spices**
- all **9 syrups and squashes**
- **4 coffees** — Swad filter and nice, both sizes
- Malnad Chai 1 kg · Sanjivni 1 kg · Badam 500 g
- Aaradhya coconut oil, both sizes · Kalpatharu

The `needs-price` tag was stale on 13 products that had since been priced. That
is now corrected, so the tag is again a true worklist: **46 tagged before,
33 now**, matching the 33 products that actually contain a ₹0 variant.

## 5. GST — 5% on all 57, applied. Shopify's own tax settings are not.

Client answer 16 Sep: *"All meterials r 5%"*, *"2 1/2 cgst and 2 1/2 sgst"*, and
*"Same sir"* for instant coffee. Applied to all 57 products and all 63 rows —
`compliance.gst_rate = 5.0` plus an HSN code on every product, verified by
reading all 57 back. The instant coffee's 18% is reversed. The 5%-vs-12% masala
question is answered 5%.

**The metafield does not drive checkout tax.** That comes from
**Settings → Taxes and duties**, still on Shopify's default, and there is no
Admin API mutation for it. One flat India rate of 5% — a small manual job now
that the whole catalogue is one rate.

**`taxShipping` is still `false`.** Delivery on a taxable supply normally carries
the principal rate. Prices are tax-inclusive so switching it does not change what
the customer pays, only the invoice split. Jnanottam's call.

**Twelve products sit in headings that normally carry more than 5%** — instant
coffee at 2101, the nine syrups at 2106, and the two hair powders at 3401/3305.
The rate is the client's and it stands; the mismatch is recorded in
`docs/gst-classification.md` rather than reconciled behind his back.

## 6. Publishing

- **57 products are DRAFT.** Setting them ACTIVE was refused by the connector as
  a real-world transaction, so publishing is manual — and should not happen until
  the prices in step 4 exist.
- **The theme is unpublished**, by design. `Malnad Spices — build`. Preview it
  from Online Store → Themes → ⋯ → Preview.

## 7. Nice to have, not blocking

- `hero-canopy.png` is **1240 × 826**. It is a full-bleed hero, so it will look
  soft on a wide desktop screen. An upscale before launch would help.
- Two categories still borrow a pack photograph where the others have a
  landscape: **Oils** and **Dry Fruits & Nuts**. The card falls back to the first
  product's pack photo, so nothing is broken or empty — it just reads
  differently from the nature shots beside it.
- No social accounts exist. Horizon's footer shipped with links pointing at
  facebook.com and instagram.com themselves; those are removed. Add the block
  back when there are real handles.
