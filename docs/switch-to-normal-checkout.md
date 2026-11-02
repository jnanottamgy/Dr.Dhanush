# Turning off Magic Checkout — your steps

**2 November 2026.** Plain English. About 15 minutes in total.

**What you are doing, in one line:** turning off Razorpay's special checkout and
going back to Shopify's normal one, because the special one has been taking
money without creating orders.

Have your Shopify admin and your Razorpay dashboard open. Do these in order —
step 3 protects you from step 2 going wrong.

---

## 1. Message Razorpay first · 2 minutes

Reply on your existing ticket and say:

> We are going with the standard Razorpay gateway. Please stop work on the
> Magic Checkout private app.

**Why first:** their engineers were working inside your store three days ago —
they created a theme at 1:05pm while you were testing at 1:03pm. If they are
still working, they will undo whatever you do next.

---

## 2. Publish the new theme · 2 minutes

Shopify admin → **Online Store → Themes**. Find this one and press **Publish**:

> **NORMAL CHECKOUT — publish this (2 Nov)**

**What it is:** your website exactly as it looks today, with Razorpay's special
checkout taken out of it. It also includes the hidden information Google needs
about your prices and whether things are in stock — so this one click also
finishes a job that has been waiting since 16 October.

**Nothing changes about your products, photographs, prices, descriptions or
delivery charges.** I checked every one of those files against your live site
before building it.

**If anything looks wrong afterwards:** publish **`Magic Checkout - Malnad
Spices — build`** again. You are back where you started in seconds.

**Do not publish any of these** — they are test copies and two of them are mine:

- `ZZ scratch — do NOT publish (has test files)`
- `MAGIC TEST 9 Oct — do not publish yet`
- `Magic Checkout - Magic Checkout - Malnad Spices...`
- `SCHEMA — publish this one (16 Oct)` — now replaced by the one above

---

## 3. Check you can still take money · 1 minute · DO NOT SKIP

Shopify admin → **Settings → Payments**.

Look at **`01 Cards, UPI, NB, Wallets by Razorpay`**:

- It must **not** say *Inactive*.
- Test mode must **not** be ticked.

**Why this matters more than it sounds.** The last time an app was changed in
this store, this setting quietly switched itself off. The website carried on
looking perfectly normal and could not take a single rupee. Nobody noticed for
a day. Check it with your own eyes rather than assuming.

---

## 4. Test it · 3 minutes

**Open a new incognito window.** In Chrome: the three dots, top right → *New
Incognito window*.

**This part is not optional.** A normal window remembers the old checkout and
the old script, and it will show you the wrong answer. That exact mistake cost
us a whole round on 9 October.

Go to `malnadproducts.in`, add any one item, press **Check out**.

| | What you should see |
|---|---|
| **Right** | A **Shopify** page asking for your email, name and address. Then a Razorpay page to pay. |
| **Wrong** | A **Razorpay box popping up on top of your own website**, asking for your mobile number. |

**If it is wrong:** Shopify admin → Settings → Apps and sales channels → find
**`TcBzhyvGVSK9Q0 - MagicCheckout`** → **Uninstall**. Then **do step 3 again**,
because uninstalling an app is what switched the payment off last time. Then
test again in a fresh incognito window.

---

## 5. Buy one pack yourself · 5 minutes

Buy something small, **₹50–80**, using Dheeraj's or Dhanush's own UPI. Real
money, not a test.

Then look at **Shopify admin → Orders**. **The order must be sitting there.**

**Why this is the important one.** Money has reached the bank — ₹100 on
27 October and ₹160 on 29 October, both confirmed with real Axis Bank reference
numbers. And orders have existed in Shopify. But **never the two together**.
Something bought on the website, paid for, appearing as an order — that has
never once happened, and until it does the shop is not proven.

It costs nothing in the end: the money lands back in the same bank account in
about two working days.

---

## 6. Fix the tax · 2 minutes · worth more than everything above

Shopify admin → **Settings → Taxes and duties → India**.

The country rate says **5%**. Change it to **2.5%**. Leave the individual state
rows alone.

**Why.** Shopify applies the country rate **twice** — once as CGST and once as
SGST. So 5% becomes 10%, and you are declaring double the GST you actually owe.
The customer pays exactly the same either way. **The difference comes out of
Dhanush's own pocket at filing time** — about **₹4.30 on every ₹100 sold**.

Both real orders in the store show this happening. It is the most expensive
setting in the shop and it takes two minutes.

---

## What it costs you from now on

| | On every ₹100 you sell |
|---|---|
| **Today** | about **₹2** |
| **After about 16 December** | about **₹4.36** |

Razorpay is charging you **nothing at all** at the moment — they give new
businesses 90 days free on their fee, and I confirmed it from your own
settlements rather than from an advert: ₹100 came in and ₹100 reached the bank,
with no deduction. That runs out around **16 December**, or once you have sold
about ₹5 lakh, whichever comes first.

Shopify's ₹2 per ₹100 applies now and does not stop. That is their charge for
letting you use Razorpay instead of their own payment system, and it is part of
being on the Basic plan in India.

**What you stop paying:** Magic Checkout was adding about **50 paise on every
₹100** on top of everything else — for a checkout that was dropping orders.

---

## Two things still to do, after the steps

1. **Send me the three payments with no order.** ₹100 on 23 October, ₹160 on
   27 October, ₹160 on 30 October. Tell me what was bought and where it was
   going, and I will create the orders in Shopify so the bill and the GST exist.
   I will not guess at them.

2. **Anything sold off the website has to be typed in.** Counter sales, phone
   orders, WhatsApp orders — they go into Shopify as a **draft order**
   (Orders → Drafts → Create order). There are **none** in the store today, so
   this is not being done. Without it there is no invoice, no GST record, and
   the accountant's monthly sheet cannot see the sale.

**From now on the two should always match.** Every payment on your Razorpay
dashboard should have an order in Shopify. If one does not, something is wrong
that day — not at the end of the month.
