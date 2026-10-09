# Magic Checkout private app — the steps, 9 Oct

Razorpay has granted private-app collaboration access. Jnanottam's decision is
to follow their mail and see. This is that, ordered so the live store cannot
break.

**Live theme is `Malnad Spices — build`, id 146238865521. Never edit or publish
over it until the test passes.**

**Test theme is already made: `MAGIC TEST 9 Oct — do not publish yet`,
id 189064872049, UNPUBLISHED.** Byte-identical copy of live —
`config/settings_data.json` 8082 bytes, md5 `c6b037400494325e780db39d1ce0a7f5`.
That checksum is the baseline for verifying the embed save.

---

## 0. Clear the decoy theme (recommended)

Online Store -> Themes -> theme library -> `Updated copy of Malnad Spices —
build` -> three dots -> **Remove**.

It is Shopify's own auto-generated update copy, unpublished, holding nothing of
ours. It has been mistaken for the live theme twice. Deleting it leaves three
themes and no ambiguity. Theme deletion is blocked from the API, so this is a
browser step.

## 1. Theme duplicate — DONE, skip their Step 1

Their mail says to duplicate the current theme. It is done, from the right
source, named so it cannot be confused. **Do not duplicate anything else.**

## 2. Scope the collaborator access

Settings -> Users -> **Collaborators**. Razorpay's access should hold
**Themes, Apps and Orders** only.

Not Customers. Not Finances. Not Settings. It is Dr. Dhanush's business data and
Dheeraj should be told an engineer at Razorpay has scoped access for this build.
A collaborator does not consume a staff seat, so Basic's two staff logins are
unaffected.

## 3. The app — DO NOT INSTALL FROM THE SHOPIFY APP STORE

This is the step that decides whether this attempt is any different from the
last three weeks.

- **The app store listing is the PUBLIC app.** Installing it reproduces exactly
  what was uninstalled yesterday: OTP, address, then a redirect to Shopify's
  checkout.
- The private app is custom to this store. It arrives either because Razorpay's
  engineers install it themselves using the collaborator access, or from a
  direct install link they send. **Only those two routes.**

So: open Shopify -> Apps and look at what is there before installing anything.

Then record the app's **exact name**:

| What Apps shows | What it means |
|---|---|
| **"Razorpay COD & Magic Checkout"** | The public app. Same as before. Expect the redirect. |
| Anything else, named for this store | The private app. This is the one wanted. |

Either way, carry on to the test — the point is to see.

## 4. Enable the embed on the TEST theme only

Online Store -> Themes -> **`MAGIC TEST 9 Oct — do not publish yet`** -> three
dots -> **Edit**.

**Check the editor's title bar says MAGIC TEST before touching anything.** Not
the one with the Active badge.

Left panel, scroll to the bottom -> **App embeds** -> turn on the Magic Checkout
script embed -> **Save**.

- Only that one. Not `Login with Razorpay`, not `Razorpay Reviews`.
- **Press Save.** A missed Save cost three checkout tests in September.
- If Save is greyed out, that is ambiguous between "already saved" and "never
  registered". Say so and the file gets read instead of the toggle.

## 5. Razorpay dashboard, LIVE mode

Dashboard TEST toggle **off**. Magic Checkout -> Setup & Settings -> Checkout
Settings (`/app/magic/settings/magicx-store-settings`, the live-mode page):

| Setting | Set to | Why |
|---|---|---|
| Enable Magic Checkout | **ON** | Was already on |
| **Email Field** | **MANDATORY** | If Magic owns the whole checkout, Shopify never collects the email. This store sends order confirmations and dispatch notices by email only. Optional here means a customer buys and never hears anything |
| Theme Color | **#1F4034** | Brand green. Was last read as Razorpay's `#528FF0`. Check it |
| Mandatory OTP | leave **off** | Friction, and it guards saved-address reuse this store does not need |

**Save.**

### Two things on their Step 2 list to leave alone

- **COD + RTO — leave COD OFF.** Prepaid only, client instruction.
- **Shipping Setup -> Magic Shipping — leave OFF.** Its own warning: *"Enabling
  Magic Shipping will bypass all shipping configurations from any plugins on
  your E-commerce platform."* That discards 28 zone-and-weight rates proven
  right on three real carts (920 g -> ₹55, 1,570 g -> ₹85, <=0.5 kg -> ₹40).

Skip Coupons (never provisioned on this account) and Analytics (no GA4 property
exists yet — separate job).

## 6. Test on the PREVIEW. Do not publish yet.

Online Store -> Themes -> `MAGIC TEST 9 Oct` -> three dots -> **Preview**. That
serves the test theme on the real store, real app, without changing anything a
customer sees.

Add **Chekke (Cinnamon Bark), 100 g, ₹50** — the same item as the 8 Oct test, so
the figures compare. Expect **₹50 + ₹40 delivery = ₹90** (Karnataka 0–0.5 kg).

Click Check out and **watch the URL bar.**

### The decisive test, and it costs nothing

| What happens | Verdict |
|---|---|
| The Razorpay panel runs **Contact -> Address -> Payment** and the **Payment step actually renders** with UPI / card / netbanking, and the URL never contains `/checkouts/cn/` | **Private app works.** Magic owns the checkout |
| After OTP and address you land on `malnadproducts.in/checkouts/cn/<token>` | **Still the public app.** Same behaviour as the last three weeks |

One screenshot of the URL bar at the payment step settles it. The answer arrives
before any money is spent.

## 7. Only if the test passes — publish

Rename the theme first (it currently says "do not publish yet"), then
Online Store -> Themes -> **Publish**.

`Malnad Spices — build` then becomes unpublished. **Keep it. It is the rollback.**

**Rollback, one step:** Online Store -> Themes -> `Malnad Spices — build` ->
Publish. Back to exactly today's working store in seconds.

## 8. Then the real money test

One ₹50–80 pack paid with **Dhanush's or Dheeraj's own money**, because what
needs proving is that settlement lands in *their* bank.

For the both-sides cross-check — Shopify's order against Razorpay's payment
record, by id and amount — the **Razorpay MCP connector has to be reconnected**
in claude.ai connector settings. It is disconnected and the OAuth flow cannot
run from the container.

---

## What gets verified from the API at each gate

| After | Check |
|---|---|
| Step 4 | Test theme `config/settings_data.json` md5 against baseline `c6b03740…` / 8082 bytes |
| Step 3 | `appInstallations` — the app's exact title and handle, and its scope list against the 41 the public app held |
| Step 8 | The order record: `test` must read **false** on both the order and the transaction, and the gateway name on the transaction |

## Still worth sending in parallel, blocks nothing

`docs/razorpay-reply-21302014.txt` — the unanswered question that decides
whether Magic is worth anything: **when Magic owns the whole checkout, does
Shopify's 2% third-party gateway fee still apply?** If it does, Magic is a pure
0.5% + GST cost. If it does not, it is worth about 1.5% net.
