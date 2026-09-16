# Your steps — Malnad Spices store

Eight things need you. Nobody else can do them, because they need a browser
login. Everything else is done.

Do them in this order. Steps 1 to 4 take about 20 minutes together.
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

## 2. Put in the shipping charge — 3 minutes

**This is the important one. Do not skip it.**

- Go to **Settings → Shipping and delivery**
- Click on the **General profile**
- You will see a zone called **Domestic** with one rate at **₹379**

Three things to change here:

1. Change the **₹379** to your real delivery charge.
2. Rename the zone from **Domestic** to `India`
3. Rename the rate from **मानक** to `Standard delivery`

**Why this matters:** ₹379 is a fake number Shopify put there when the store
was made. Six of your seed packs sell at ₹140. If a customer buys one bag and
sees ₹379 delivery on top, they will close the page. Every order would be lost.

**मानक** is Hindi for "standard". Your store is in English, so the customer
sees one Hindi word at checkout. It looks like a mistake.

I tried to change these two names from my side. Shopify accepted the change,
said it worked, and then did nothing. So it has to be done by hand.

---

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
