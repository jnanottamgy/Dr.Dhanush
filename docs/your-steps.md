# Your steps — Malnad Spices store

**All 57 products are LIVE as of 16 Sep** — active and on the Online Store
channel, every one with a real price. The catalogue side is finished.

What is left needs a browser login, so only you can do it. **The two that
actually stand between you and a working shop are 4 and 6.** Do them in this
order.

---

## 1. ~~Change the store name~~ — DONE

The store is now **Malnad Products**, not "My Store".

**One thing to decide, not urgent.** The packs, the FSSAI licence and the
packer name all say **MALNAD SPICES**. The shop says *Malnad Products*, and the
new domain would be `malnadproducts.in`. A customer holding a pack will type
what is printed on it. Whichever you make the main address,
`malnadspices.in` should be added to the same store as a second domain so it
redirects instead of dying.

---

## 2. Check the shipping rates — 10 minutes

The courier charges by distance and by weight, so a single flat rate could
never have worked. That is now built properly.

- Go to **Settings → Shipping and delivery**
- Open the profile called **Malnad delivery**

You will see **four zones**, each with **seven weight steps**:

| Weight | Karnataka | South & West | Rest of India | North East & islands |
|---|---|---|---|---|
| up to 0.5 kg | ₹40 | ₹60 | ₹80 | ₹110 |
| 0.5 – 1 kg | ₹55 | ₹80 | ₹105 | ₹145 |
| 1 – 2 kg | ₹85 | ₹120 | ₹155 | ₹215 |
| 2 – 3 kg | ₹115 | ₹160 | ₹205 | ₹285 |
| 3 – 5 kg | ₹175 | ₹240 | ₹305 | ₹425 |
| 5 – 10 kg | ₹325 | ₹440 | ₹555 | ₹775 |
| 10 – 20 kg | ₹625 | ₹840 | ₹1055 | ₹1475 |

**These numbers are a starting shape, not real tariffs.** They are built from
just eight figures — a base price and a per-kilo price for each of the four
zones. Send me the courier's actual rate card and I will regenerate the whole
table from those eight numbers in one go. Or change them yourself in this
screen; it is the same thing, just slower.

Two things worth knowing:

- **Shopify already knows what everything weighs.** Every pack has a shipping
  weight on it — a 100 g packet of pepper counts as 140 g with its wrapper, a
  700 ml syrup bottle as 1,025 g. So the basket weight adds up by itself and
  the customer is shown the right band automatically.
- **Each band charges at its top weight.** A 1.2 kg parcel pays the 2 kg price.
  That is on purpose. Under-charging postage loses money quietly on every
  single order, and you would not notice until the accounts.

**One thing to watch.** When you add a *new* product later, Shopify puts it in
the **General profile**, which has no rates. That product would show no
delivery option at checkout. After adding anything new, open
**Settings → Shipping** and move it into **Malnad delivery**.

I could not avoid this: Shopify's API let me create this profile but refuses to
add zones to the General one — it accepts the request, reports success, and
changes nothing. If you would rather have it all in the General profile, you
can rebuild these four zones there by hand and then delete Malnad delivery.

## 3. Paste in the four policies — 10 minutes

- Go to **Settings → Policies**

You will see five boxes. Four of them are empty.

For each one below, open the file, copy everything in it, and paste it into
the matching box.

| Box in Shopify | File to copy from |
|---|---|
| Refund policy | `policies/refund.html` |
| Shipping policy | `policies/shipping.html` |
| Terms of service | `policies/terms.html` |
| Contact information | `policies/contact.html` |

**Important:** in each box, click the **`<>`** button first (it says "Show
HTML" or similar). Paste into that view. If you paste into the normal view you
will see the code as text on the website.

**Do not touch the Privacy policy box.** It already has Shopify's own text in
it. Shopify keeps that text up to date as the law changes. Ours would be worse.

**Why this matters:** Razorpay will not switch your account on until these are
published. This is on their checklist.

---

## 4. Publish the website — THE BIG ONE

**The products are live but the website is still Shopify's stock theme.**
Everything we built — the brand colours and fonts, the home page, the category
sections, and the declarations box on every product page — sits in a theme
that is not switched on yet. Right now a visitor sees our products on a plain
default shop.

- Go to **Online store → Themes**
- Find **Malnad Spices — build**
- Click **⋯ → Preview** and have a look first. Open a couple of product pages
  and check the declarations box at the bottom looks right — that is the one
  thing I have never been able to see rendered.
- When you are happy: **⋯ → Publish**

Tell me anything you want changed and I will change it before you publish.

I cannot publish a theme from my side — Shopify blocks it, which is the right
way round for a thing this final.

---

## 5. ~~Prices~~ — DONE

**All 63 pack sizes are priced.** The client sent the last of them on 16 Sep.
Nothing is at ₹0.00 and the `needs-price` tag is gone from every product — I
checked all 63 one by one before publishing anything, precisely so nothing went
live orderable for free.

---

## 6. GST — set the rate in Shopify (only you can)

**The catalogue side is done.** Dr. Dhanush answered 5% on everything, so all
57 products now carry a rate and an HSN code, and the instant coffee's earlier
18% has been reversed. Nothing is blank.

**But that does not tax anybody.** The rate I set lives in our own field, for
the accountant. What a customer is actually charged comes from
**Settings → Taxes and duties**, and it is still on Shopify's default. There is
no way to set it through the API — it is a screen only you can open.

With one flat rate across the whole catalogue it is a small job: **India, 5%.**
Prices are already tax-inclusive, so this changes how the invoice splits the
figure, not what the customer pays.

While you are on that screen: **"Charge tax on shipping" is currently off.**
Delivery on a taxable supply normally carries the same rate. My reading is it
should be on. Again it does not change what the customer pays, only the invoice
split. Your call — you are the CA.

**Three things I would put back to him in writing**, all in
`docs/gst-classification.md` with the reasoning:

1. **Instant coffee.** It is an extract, HSN 2101, which normally attracts 18%.
   It is the largest single exposure in the catalogue.
2. **The nine syrups and squashes**, at HSN 2106, also normally 18%. Nine
   products is the biggest block.
3. **The two hair powders** — soapnut and sikakai. They are not food at all,
   and their headings normally attract 18%.

The rate stands as he gave it. I have recorded the mismatch rather than quietly
changing either side of it.

---

## 7. ~~Publish the products~~ — DONE 16 Sep

All 57 are **active and on the Online Store channel**. Shopify had blocked this
before; it went through this time.

Worth knowing, because it is a trap: making a product "active" is only half of
it. All 57 went active and were still on **zero sales channels** — invisible on
the shop, with nothing on screen to say so. They had to be put on the Online
Store channel as a separate step. If you ever add a product by hand, check the
**Sales channels** box on the product page actually says Online Store.

---

## 8. Razorpay — the last thing between you and taking money

**There is no payment provider connected.** A customer can browse, add to
basket, and reach checkout — and then not be able to pay.

Two parts, in order:

1. **KYC.** The video call is between Dr. Dhanush and a Razorpay officer. You
   do not need to be in the room and he does not need to travel. It cannot be
   delegated — his face, his PAN, his Aadhaar. The account goes in **his**
   name, never yours or JTACS's: settlement has to land in his bank and he
   holds the FSSAI licence. Full playbook in `docs/razorpay-kyc.md`.
2. **Connect it.** Test mode needs no KYC at all, so the whole test half can
   run now with `rzp_test_` keys.

**Do not paste live keys into a chat with me.** Put them straight into Shopify
on a screen-share.

---

## Small things, not urgent

- The big photo on the home page is a bit small (1240 pixels wide). It will
  look slightly soft on a large screen. Worth replacing before launch.
- Two categories, **Oils** and **Dry Fruits & Nuts**, show a pack photo instead
  of a nature photo. Nothing is broken, it just looks different from the rest.
- There are no Instagram or Facebook accounts yet, so I removed those links
  from the footer. Shopify had them pointing at instagram.com and facebook.com
  themselves, which would have sent customers to the wrong place. Tell me when
  the accounts exist and I will put them back.
- The checkout page will look like a plain Shopify checkout. Styling it needs
  Shopify **Plus**, which is a much more expensive plan. Razorpay Magic
  Checkout replaces that page anyway, and that one can be styled on Razorpay's
  side.
