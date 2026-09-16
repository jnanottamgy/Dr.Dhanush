# Your steps — Malnad Spices store

Eight things need you. Nobody else can do them, because they need a browser
login. Everything else is done.

Do them in this order. Steps 1 to 4 take about half an hour together.
Steps 5 to 8 need the client.

---

## 1. Change the store name — 1 minute

Right now the store is called **"My Store"**.

- Go to **Settings → Store details**
- Find **Store name**
- Change it to: `Malnad Spices`
- Click **Save**

**Why this matters:** that one name shows up in six places — the top of every
page, the browser tab, the order emails, the checkout, and inside the privacy
policy. Today the privacy policy literally reads *"My Store operates this
store"*. Changing the name fixes all six at once.

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

## 4. Look at the new website — 5 minutes

- Go to **Online store → Themes**
- Find **Malnad Spices — build**
- Click the **⋯** button → **Preview**

Have a look at the home page. Tell me anything you want changed.

**One thing I could not check:** the product pages. Every product is still a
draft, so there is no product page to open yet. Once you put prices in
(step 5) and publish one product, please open it and check that the
declarations box at the bottom looks right.

---

## 5. Prices — needs the client

**36 pack sizes across 33 products still have no price.** They are all packs
that do not print an MRP, so only he knows the number.

- all 18 whole spices
- all 9 syrups and squashes
- 4 coffees (Swad filter and nice, both sizes)
- Malnad Chai 1 kg, Sanjivni 1 kg, Badam 500 g
- Aaradhya coconut oil (both sizes), Kalpatharu

In Shopify you can find them all at once: **Products**, then filter by the tag
**`needs-price`**.

**Why this matters:** a product with no price is sitting at ₹0.00. If it goes
live like that, a customer can order it for free.

---

## 6. GST rates — needs the client, and your own opinion

**34 of 57 products still have no GST rate.** I did not guess them.

The groups still open: the 6 Swad masala blends, nellikai powder, the 6 seeds,
the 6 dry fruits and nuts, the 9 syrups, the 3 oils, and the 3 washing and
hair-care items.

One to double-check: **instant coffee went in at HSN 2101 / 18%**. That is the
biggest single rate in the catalogue. Worth confirming.

---

## 7. Publish the products — after step 5

All 57 products are drafts. **Do not publish any of them until it has a price.**

I could not publish them from my side — Shopify blocked it as a real-world
action.

---

## 8. Publish the website — last

Only after steps 1 to 7. **Online store → Themes → Malnad Spices — build →
Publish.**

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
