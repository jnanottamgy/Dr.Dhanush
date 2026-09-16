# HSN classification for the 34 unrated products

**What I have done and not done, and why.**

I have proposed an **HSN code** for every one of the 34. Classification is a
reasoning exercise — what is this thing, which chapter does it fall in — and the
chapter structure is stable. That work is below.

I have **not** filled in the GST rates, and this is a deliberate call rather than
laziness. Reasons, in order of how much they should worry you:

1. **India restructured the GST slabs.** I cannot verify from here which slabs
   are current today, and several of these items previously sat at 12% — a slab
   that may no longer exist. Writing a rate I cannot check against the live
   schedule is exactly the kind of plausible-looking wrong number this project
   has been avoiding all the way through.
2. **A wrong rate costs the client money, not just accuracy.** Under-collect and
   he pays the shortfall himself with interest and penalty. Over-collect and the
   excess still has to be deposited, and he is uncompetitive meanwhile.
3. **You have the current schedule at your firm.** Attaching a rate to a settled
   HSN is a lookup. Deciding the HSN is the part that takes judgement, and that
   part is done below.

Where the classification itself is genuinely contested I have said so and given
the reason, so you know where the time needs to go.

---

## Settled — classification is not in dispute

| Product | HSN | Reasoning |
|---|---|---|
| Chia Seeds | 1207 | Oil seeds and oleaginous fruits, chapter 12 |
| Sabja Seeds | 1207 | Basil seed, same chapter |
| Magaz Seeds | 1207 | Melon seed kernels |
| Pumpkin Seeds | 1207 | |
| Flax Seeds | 1204 | Linseed has its own heading |
| Sunflower Seeds | 1206 | Sunflower seed has its own heading |
| Badam (Almonds) | 0802 | Nuts, fresh or dried |
| Pista (Pistachios) | 0802 | |
| Hayat Raisins | 0806 20 | Dried grapes |
| Dates | 0804 10 | |
| Special Dates | 0804 10 | Same commodity, different grade |
| Soapnut (Whole) | 1211 | **Whole, unprocessed** plant material. Note this sits apart from the two powders below — processing them into a hair preparation moves the chapter |

## Contested — worth your time

### The six Swad masala blends
Bisibele bath · garam masala · palav · puliyogare · rasam · sambar

**Proposed HSN 2103 90** — mixed condiments and mixed seasonings.

The competing reading is chapter 0910 (spices) at the whole-spice treatment.
There are AAR rulings both ways. The mainstream position is that a *branded,
mixed* masala is a preparation under 2103 rather than a spice under 0910, and
these are branded and mixed. **This is the 5-vs-12 question already on record —
it is the same question, and it is the single biggest rate call in the catalogue
after instant coffee.**

### The nine syrups and squashes

**Proposed HSN 2106 90** — food preparations not elsewhere specified.

Competing reading is 2202 (waters and flavoured beverages). A *concentrate sold
for dilution* generally sits in 2106 rather than 2202, which is why I have put
them there. Applies to all nine.

**Diabeat is separate and worse.** Its own label calls it a *proprietory
preparation*. If the maker holds an ayurvedic licence for it, it is arguably
chapter 3004 rather than 2106, at a different rate entirely. This is the same
product already flagged as the most serious item in the catalogue for a different
reason. Do not let it ride on the syrup decision.

### The three coconut oils
Aaradhya · Kalpatharu · Shree Durga ghani-pressed

**Proposed HSN 1513 11** — coconut oil, edible.

This was contested for years — edible oil versus hair oil at chapter 3305 — and
the Supreme Court settled it in favour of edible oil for small retail packs
unless the pack is labelled and marketed as a hair preparation.

**One thing I have to flag, because it is my own doing.** The product
descriptions I wrote say the oil is *"for cooking, for the tempering pan, and for
hair, the way it has always been used here."* That is a true sentence about how
people here use it. But website copy marketing an oil for hair is exactly the
kind of evidence that argues for the 3305 classification. **If you want the
edible-oil position, tell me and I will take "and for hair" out of all three.**
I have left it alone because changing product copy to support a tax position is
your call, not mine.

### Antuvala (Soapnut) Powder and Sikakai Powder

**Proposed HSN 3305 90** — preparations for use on the hair.

Ground and sold specifically as a hair wash, so these are preparations rather
than raw plant material. Note the deliberate split from **whole** soapnuts above
at 1211 — same plant, different HSN, because one is processed for a purpose and
the other is not.

### Horanadu Nellikai Powder

**Proposed HSN 1106 30** — flour and meal of dried fruit.

Genuinely unclear. The pack says "HOME PRODUCT" and the powder is used both in
the kitchen and in hair care. If it is positioned as ayurvedic the chapter moves.
Our listing describes it as both uses, which does not help pin it down.

---

## Also needs your decision: GST on delivery

`taxShipping` is currently **false**, so delivery is treated as carrying no GST.

Delivery charged by the supplier on a taxable supply is normally part of the
value of that supply, which would make it taxable at the principal rate.
**My reading is that this should be `true`.**

Because prices are GST-inclusive, switching it **does not change what the
customer pays** — it changes how the invoice splits the tax between goods and
freight. Low risk to change, and better decided before the first real order.

**There is no Admin API mutation for it** — verified against the full mutation
list; the only `shop*` mutations are locale, policy and resource feedback. So it
is one checkbox in **Settings → Taxes and duties**, by hand.

---

## And the thing that actually taxes a customer

The `compliance.gst_rate` metafield is **ours**. It feeds the accountant's export
and nothing else — it is not shown on the product page, and **Shopify does not
use it to calculate tax**.

The rate that actually appears on a customer's invoice comes from
**Settings → Taxes and duties**. Until that is configured, every order will be
taxed at whatever default is sitting there, whatever our metafield says.

The nine collections line up closely with the rate groups — whole spices, masalas,
seeds, dry fruits, syrups, oils, home care — so per-collection tax overrides are
the natural way to set it up once the rates are decided.
