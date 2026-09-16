# Razorpay video KYC — how to get it done with the client 400 km away

## The thing that unblocks this

**The video call is between the client and a Razorpay officer. You are not on it,
and you do not need to be in the room.**

RBI's Video-based Customer Identification Process (V-CIP) exists precisely so the
customer does *not* travel. It is the regulator's remote-onboarding route,
introduced in January 2020 and extended in May 2021 to cover proprietors of
proprietorship firms and authorised signatories. The Razorpay officer is on
Razorpay's side of the call. Distance between you and the client is irrelevant to
it.

So the task is not "get to the client". It is **"get the client ready to spend
five minutes alone on a video call"**.

## What cannot be delegated

The client must be the face and the voice. It is his PAN, his Aadhaar, his
proprietorship. Nobody can sit the call for him, and the process geotags him to
prove he is physically in India. Someone local can hold the phone; they cannot
answer for him.

**Do not put the merchant account in your name or JTACS's name to route around
this.** Settlement has to land in the client's bank, he holds the FSSAI licence,
and running a payment account for someone else's business is a straight
compliance breach — frozen settlements at best, PMLA exposure at worst. Not worth
discussing further.

## Switching gateway will not help

V-CIP is an **RBI requirement on every payment aggregator**, not a Razorpay
policy. Cashfree, PayU, Instamojo, PhonePe all run the same check. Shopping
around costs a week and arrives at the same video call. Stay with Razorpay.

---

## Proposal 1 — coach him through it remotely (do this first)

1. **Book the slot** from the Razorpay dashboard for a time you are both free.
2. **Call him 15 minutes before.** Walk the checklist below, item by item, while
   he physically puts each thing on the table in front of him.
3. **Hang up.** He takes the Razorpay call alone. It runs about five minutes.
4. **Call him back** to confirm it completed.

That is the whole intervention. Most failed video KYCs fail on preparation, not
on the call.

## The pre-flight checklist

Go through this on the phone with him *before* the slot, not during.

**In his hand, originals, not photocopies**
- [ ] PAN card — the physical card, held up to the camera
- [ ] Aadhaar card
- [ ] The phone that receives his **Aadhaar-linked OTP** — this is the one people
      get wrong. If Aadhaar is linked to an old number he no longer uses, the
      process stops dead and cannot be recovered on the call.

**The setup**
- [ ] Sitting near a window, face well lit, no strong backlight
- [ ] On **WiFi**, not estate mobile data. A dropped call means rebooking.
- [ ] Quiet room, phone propped or held steady
- [ ] Plain background, no cap, no sunglasses

**The things that cause rejection**
- [ ] Name spelled **identically** on PAN, Aadhaar and the settlement bank
      account. Any mismatch — an initial, a middle name, "R." vs "R" — is the
      single most common rejection.
- [ ] Face still recognisable against an old PAN photograph
- [ ] Business name and address consistent with the FSSAI licence and, if he is
      registered, the GST certificate
- [ ] He can state his own business details out loud without reading them off a
      screen — he will be asked

**After**
- [ ] Settlement bank account added and verified on the dashboard
- [ ] He knows not to share the live API keys with anyone, including you, over
      chat

---

## Proposal 2 — batch one visit, if coaching stalls

We are currently blocked on the client for a lot more than KYC:

| Blocked on him | What it needs |
|---|---|
| Price list | 63 selling prices, 49 MRPs |
| Back-of-pack photos | the nine syrups and squashes |
| Pack sizes | the nine bare tubs and bags |
| Nellikai label | one sharp close-up |
| Diabeat decision | the dosage claim on the label |
| Banana stem squash | is the Sugarless bottle a separate product |
| Video KYC | five minutes |

**One day with him clears every row of that table.** If the coaching call does
not land in the first attempt, the trip is not a defeat — it is the cheapest way
to close Stage 1 and Stage 3's gate together, and it stops the drip of one
question at a time over WhatsApp.

Go with: a phone on a tripod, the pack-size list, the price-list request, and a
camera for the back labels.

---

## Meanwhile: Stage 3 is not actually blocked

**Test mode needs no KYC at all.** Razorpay issues `rzp_test_` keys immediately
on signup, before activation, and test mode processes simulated transactions with
no real money.

So the whole test-mode half of Stage 3 runs today:

- Razorpay app installed in Shopify
- Test keys entered
- The full 16-row test matrix in Section 04 of the runbook, end to end
- COD confirmed off
- Magic Checkout verified as the default path

What waits for KYC is only the second half — live keys, the live rupee-value
matrix, the real refund, and the settlement landing in the bank. By the time KYC
clears, everything testable is already tested, and the live run becomes a
re-run of a matrix we already know passes rather than a first attempt.
