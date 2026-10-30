# Getting malnadproducts.in onto Google — your steps

**16 October 2026.** Plain English. Everything here needs a browser login, so
it is yours to do. Everything that could be done from the API is already done
and is listed at the bottom so you know what not to repeat.

Nothing is blocking Google today. The store is public, the password page is off,
the domain is live with SSL, and all 57 products are published. Google simply
has not been told the site exists.

---

## Part 1 — the four that decide whether you appear at all

Do these in order. Together they are about 35 minutes.

### 1. Publish the new theme · 2 minutes

Online Store → Themes. Publish the one called:

> **SCHEMA — publish this one (16 Oct)**

It is a copy of the theme you are running now, with one thing added: the
hidden block of information that tells Google your prices, your pack sizes,
whether something is in stock, and that Malnad Products is a real shop in
Horanadu trading since 1999. Your site currently publishes none of that, which
is why a Google result for your products would show a bare title and nothing
else.

**Three things to know before you click:**

- Razorpay's checkout code is in it. I copied *their* theme, not ours, so Magic
  Checkout is untouched. I verified their file is present and unchanged.
- **Do not publish** `ZZ scratch — do NOT publish (has test files)` or
  `MAGIC TEST 9 Oct`. Those are mine, for testing, and both are junk.
- **If anything looks wrong, publish `Magic Checkout - Malnad Spices — build`
  again.** That is what you are on now and it comes back in seconds. Note this
  has changed — the old rollback, `Malnad Spices — build`, does **not** have
  Razorpay's code in it and would take the checkout down.

After publishing, **open the shop in a new incognito window** and put one item
through to the checkout. Not a normal reload — a stale checkout link and the
cached script both survive a reload, and that already cost us a round on
9 October.

### 2. Google Search Console, and submit the sitemap · 20 minutes

This is the one you said you have not done. Nothing about your Google position
can be measured until it is done, and it is also how you ask Google to come and
look.

Go to `search.google.com/search-console` and add a property. It will offer
several ways to prove you own the site. **Choose the one called "Domain"** — it
asks you to add a TXT record wherever you bought `malnadproducts.in`. Pick that
one rather than the HTML tag option, for two reasons: it covers
`malnadproducts.in`, `www.malnadproducts.in` and every future subdomain in one
go, and it does not require editing the theme.

Google may take up to 15 minutes to see the record. If Verify fails, wait and
press it again rather than starting over.

Once verified, find **Sitemaps** and submit:

```
sitemap.xml
```

Shopify writes that file itself and keeps it current — you never edit it. It
lists all 57 products, the collections and the pages.

Then use **URL Inspection** at the top, paste in `https://malnadproducts.in`,
and press **Request indexing**. That puts the homepage in the queue immediately
instead of waiting to be found.

*If you would rather use the HTML tag method, send me the tag and I will put it
into the theme before you publish it — do not paste it into the live theme by
hand.*

### 3. The homepage title and description · 10 minutes

Your homepage currently has no title and no description of its own, so Google
shows just the words "Malnad Products" and nothing underneath. It is the single
cheapest improvement on the whole site and it cannot be done through the API.

Shopify admin → **Online Store → Preferences**. Paste these in exactly:

**Title**

```
Malnad Products — Spices, Coffee & Estate Goods from Horanadu
```

**Description**

```
Buy Malnad spices, coffee, tea and estate goods direct from Horanadu,
Chikkamagaluru. Weighed and packed the day you order. Delivered across India.
Trading since 1999.
```

This also fixes something else. That same description is what WhatsApp,
Facebook and Instagram show when anyone shares a link to the shop. Right now
they show the two words "Malnad Products". WhatsApp is this business's main
channel, so this is worth more here than on a typical store.

### 4. Install Shopify Search & Discovery · 2 minutes

Shopify App Store → search "Search & Discovery" → install. It is **free** and
made by Shopify.

Two reasons. It adds filters to the nine category pages, which they do not have
today, and the quotation promises "search and filters" — so this is a scope item
that is not yet built, not just an SEO nicety. It also improves the shop's own
search box, which is where a customer who knows what they want actually goes.

---

## Part 2 — makes you appear better · this week

### 5. Google Business Profile

`business.google.com`. Free. This is what puts the shop in Google Maps and in
the box on the right-hand side when somebody searches your name.

You already have every single thing it asks for and publish none of it: the
trading name, the address at Devaramane, two phone numbers, the FSSAI licence
number, and trading since 1999. For a physical shop in Horanadu this is
probably worth more than anything else on this page, because almost nobody else
is competing for those local searches.

It will want to post a letter or ring the shop to confirm the address, so start
it early — the verification is the slow part.

### 6. Google Analytics · 15 minutes

Shopify admin → Online Store → **Preferences** has a Google Analytics box.
Create a GA4 property at `analytics.google.com` and connect it.

This does not help you rank. It tells you whether any of the above worked. At
the moment nothing on the site is measuring anything at all, so there is no way
to answer "did Google send us anybody this week".

---

## Part 3 — tidying · 5 minutes, optional

### 7. Delete the leftover themes

Online Store → Themes. There are six, which is four too many. Safe to delete:

- `MAGIC TEST 9 Oct — do not publish yet`
- `ZZ scratch — do NOT publish (has test files)`
- `Malnad Spices — build` — **only after** step 1 has been running happily for
  a few days. It is the old rollback and has no Razorpay code in it.

**Keep** `Horizon` (the untouched original) and whichever theme is live.

### 8. Delete the "Home page" collection

Products → Collections → **Home page**. Delete it, or set it to not be
available on the Online Store.

Shopify creates this with every store. It holds one product, nothing on your
site links to it, and because it is published it sits in your sitemap as a page
whose heading literally reads "Home page" — competing with your real homepage.
I could not remove it from here; the connector blocks unpublishing. I have given
it a sensible title and description so it is not garbage in the meantime, but
deleting it is the real fix.

---

## What to expect, honestly

- **Your own name first.** Searching "malnad products" or "malnadproducts.in"
  should start working within a few days to about two weeks of step 2. That is
  the easy one — nobody else is competing for your name.
- **Local searches next.** "malnad spices horanadu", "marati moggu online",
  "nellikai powder", "sikakai powder" — weeks, and step 5 matters more than
  anything else for these. These are the searches worth having, because the
  competition is thin.
- **General searches are a long game.** "buy black pepper online", "buy almonds"
  — months, and against national sellers spending money on it. Do not judge the
  work by these.
- **Nobody can promise a position.** Anyone who does is selling something. What
  can be promised is that the site is technically correct and that Google has
  everything it needs, which after Part 1 it will.
- **Two to three days** is Shopify's own figure for a change being picked up
  once you are verified. Before you are verified, it could be never.

---

## Already done — do not redo these

Finished from the API this week, all verified by reading the store back:

| | |
|---|---|
| **SEO titles and descriptions** | All 57 products, 10 collections, both pages. Every one was empty before, so Google was reading bare product names |
| **Alt text on all 70 pack photographs** | 64 were blank. This is how Google Images finds "marati moggu" and "sikakai" |
| **Collection images** | All nine, with real alt text |
| **Price, stock and business information for Google** | Written and staged — step 1 publishes it |
| **The "Home page" collection** | Given a real title and description. Step 8 is the proper fix |
| **Checked and found fine** | Password page off · domain and SSL correct · canonical tags on every page · all 57 products published to the storefront · no false "free shipping" or "free returns" text anywhere |

Two things I deliberately did **not** do, so you are not surprised later:

- **No `robots.txt` change.** Nothing is blocking Google, so editing that file
  is all risk and no gain. It is the one file that can take a site off Google
  completely.
- **No `llms.txt`.** This is the new file that ChatGPT and similar are meant to
  read. Shopify will not serve a file from the root of the domain without an
  extra app, so it genuinely cannot be done on this plan. Treat anyone selling
  it to you as mistaken.

Full technical audit, with scores and the reasoning: `docs/seo-audit-2026-10-16.md`.

---

## Still open from before — not SEO, but still open

Not part of this list, so it does not get lost:

1. **Tax is computing at 10%, not 5%.** Settings → Taxes and duties, set the
   India country rate to **2.5%**, leaving the per-state IGST rows at 5%.
   Shopify applies the country rate to CGST *and* SGST separately, so 5% becomes
   10%. The customer pays the same either way — the difference comes out of
   Dhanush's margin at filing. It is about 4.3% of goods value on every sale,
   and both real orders show it.
2. **Magic Checkout's email field is Optional, and should be Mandatory.** Order
   #1002 had no email at all, so Shopify had nothing to send a confirmation to.
   This store confirms and dispatches by email only.
3. **Magic Checkout's colour is Razorpay blue**, should be `#1F4034`. It is the
   screen every customer pays on.
4. **One real purchase from the website.** Money *has* now reached the bank —
   ₹100 credited 27 October and ₹160 credited 29 October, both with real Axis
   Bank reference numbers, and a further ₹160 taken on 30 October. So Razorpay
   paying out is settled and no longer a worry. What is still untested is an
   order placed **on the website** and paid for: the two orders Shopify holds
   are one test and one cash-on-delivery that was cancelled. One ₹50–80 pack
   bought from the shop itself is all that is left to prove.
