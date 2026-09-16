# GST — answered at 5%, and the twelve places that disagrees with the HSN

**The client's answer, 16 Sep.** *"All meterials r 5%"*, split
*"2 1/2 cgst and 2 1/2 sgst"*, and to your instant-coffee follow-up,
*"Same sir"*.

**Applied in full.** All 57 products and all 63 catalogue rows now carry
`GST Rate = 5` and an HSN code. `compliance.gst_rate = 5.0` and
`compliance.hsn_code` are set on every product in Shopify, verified by reading
all 57 back. The instant coffee's earlier 18% has been reversed. Nothing is
blank and nothing is guessed at a rate any more.

The rate is his call and it stands. This document is the record of where it
sits awkwardly, because you are the CA and an HSN/rate mismatch is exactly what
gets picked up at filing.

---

## The twelve where the heading normally carries more than 5%

These are not errors. They are places where the code I assigned and the rate he
gave describe different things, and an invoice shows both.

| Product | HSN | Heading is | Usual rate |
|---|---|---|---|
| Swad Instant Coffee | 2101 | Extracts and essences of coffee | 18% |
| Nisarga Amla Health Drink | 2106 | Food preparations n.e.s. | 18% |
| Nisarga Banana Stem Squash | 2106 | " | 18% |
| Nisarga Jamun Squash | 2106 | " | 18% |
| Suruchi's Ginger Lime Syrup | 2106 | " | 18% |
| Suruchi's Grapes Syrup | 2106 | " | 18% |
| Suruchi's Jamboo Syrup | 2106 | " | 18% |
| Suruchi's Sugarless Jamboo Syrup | 2106 | " | 18% |
| Hallimane Kokam Syrup | 2106 | " | 18% |
| Suruchi's Diabeat | 2106 | " | 18% |
| Antuvala (Soapnut) Powder | 3401 | Soap and surface-active preparations | 18% |
| Sikakai (Shikakai) Powder | 3305 | Preparations for use on the hair | 18% |

Two of those are worth separating out:

- **Instant coffee.** 2101 is right — it *is* an extract, not roasted bean, and
  that is why it is not 0901 with the other two coffees. It is the single
  largest exposure in the catalogue and the one line I would put back to him in
  writing.
- **The nine syrups and squashes.** Nine products at 2106 is the largest block.
  The competing reading is 2202, flavoured waters — but a concentrate sold for
  dilution generally sits in 2106, which is why they are there. Neither
  heading gets you to 5%.
- **The two hair powders** are not food at all, which is the whole reason they
  have their own storefront section. A 5% rate on a hair preparation is the
  odd one out in an otherwise food catalogue.

## The masala blends — the 5-vs-12 question, answered 5%

The six Swad powders are at **HSN 0910**, and that is the code that agrees with
his answer: 0910 91 is *mixtures of two or more spices*, and mixtures of spices
sit with spices.

The competing reading is **2103 90**, mixed condiments and mixed seasonings, at
12%. What decides it is whether the blend contains anything that is not a spice
— dal, salt, tamarind, oil. Bisibele bath and puliyogare powders very commonly
do.

**None of the six packs prints an ingredients list**, so I cannot settle it from
the photographs, and I am not going to assume. If you want it settled, one
question to him — *what goes into the bisibele bath and puliyogare powders
besides spices?* — decides all six.

## Settled, and comfortable at 5%

| Product | HSN | |
|---|---|---|
| Filter and Nice coffee | 0901 | Roasted coffee. If chicory is blended in, this moves |
| Malnad Chai, Sanjivni, QTF | 0902 | Tea |
| The 17 whole spices | 0904–0910 | By spice |
| Chia, sabja, magaz, pumpkin | 1207 | Oil seeds, chapter 12 |
| Flax | 1204 | Linseed has its own heading |
| Sunflower | 1206 | Its own heading |
| Badam, pista | 0802 | Nuts |
| Raisins | 0806 | Dried grapes |
| Dates, special dates | 0804 | |
| Nellikai powder, mixed dry fruits | 0813 | Dried fruit. 1106 30, flour of dried fruit, is arguably more precise for the powder — same rate either way |
| Soapnut, whole | 1404 | **Unprocessed** plant material, which is why it sits apart from the two powders above |
| The three coconut oils | 1513 | Edible coconut oil |

**One note on the oils that is my own doing.** The descriptions I wrote say the
oil is used *"for cooking, for the tempering pan, and for hair, the way it has
always been used here."* The client has since confirmed *"Coconut oil is for
both"*, so the sentence is accurate. But website copy marketing an oil for hair
is the evidence that argues for 3305 rather than 1513 — the Supreme Court
settled small retail packs in favour of edible oil *unless the pack is labelled
and marketed as a hair preparation*. The packs say nothing; our copy does. Say
the word and I take "and for hair" out of all three.

**Diabeat is still separate and still the worst item in the catalogue**, for the
reason already on record — its label names a condition and prints a dosage. If
its maker holds an ayurvedic licence it is arguably chapter 3004, not 2106, at a
different rate again. That question is not resolved by the 5% answer.

---

## CGST + SGST is only half of it

He gave the split as **2½ CGST + 2½ SGST**. That is correct for a sale inside
Karnataka.

The store ships to all 36 states and union territories. Every sale outside
Karnataka is **IGST at 5%** — same total, one line instead of two. Shopify
handles that split itself once the rates are configured; it is not something the
catalogue carries. Worth saying only so nobody is surprised by an invoice
showing IGST.

---

## Still needs your decision: GST on delivery

`taxShipping` is currently **false**, so delivery is treated as carrying no GST.

Delivery charged by the supplier on a taxable supply is normally part of the
value of that supply, taxable at the principal rate. **My reading is that this
should be `true`.**

Because prices are GST-inclusive, switching it **does not change what the
customer pays** — it changes how the invoice splits the tax between goods and
freight. Low risk, better decided before the first real order.

**There is no Admin API mutation for it** — verified against the full mutation
list; the only `shop*` mutations are locale, policy and resource feedback. It is
one checkbox in **Settings → Taxes and duties**, by hand.

---

## And the thing that actually taxes a customer

The `compliance.gst_rate` metafield is **ours**. It feeds the accountant's export
and the declarations panel — it is not what Shopify charges on.

The rate that appears on a customer's invoice comes from
**Settings → Taxes and duties**, and that is still unconfigured. Until it is set
to 5%, every order is taxed at whatever default is sitting there, whatever the
metafield says.

With one flat rate across the whole catalogue this is now a simple job: a single
India rate of 5%, no per-collection overrides needed. It is a screen only you
can reach.
