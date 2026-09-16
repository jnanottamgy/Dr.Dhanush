# Brand images received 15 Sep 2026

| File | Slot | Status |
|---|---|---|
| `hero-canopy.png` | Homepage hero | Composition good — **needs upscale to 2560×1440** |
| `story-trunk-pepper-vine.png` | Estate story band | Good, 2:3 — crop to 4:5 |
| `cat-coffee-cherries.png` | Category: Coffee | Good — **crop landscape to 3:4 portrait** |
| `cat-spices-pepper-vine.png` | Category: Spices | Good, correct portrait |
| `cat-honey-comb.png` | Category: Honey | **ORPHANED — there is no honey in the catalogue.** No slot for it |
| `packs-three-up.png` | Category: Gift / product | **AI-processed — never use.** The gift category is also gone |

## Resolution

Everything is 1024–1240 px on the long edge. That is fine for category cards at
their rendered size, and **too soft for the full-bleed hero**, which spans the
whole viewport and will look blurred on any modern laptop. Upscale the hero 2×
or regenerate it larger before launch.

## The pack image is not a transcription source

`packs-three-up.png` has been through a generative tool. Zooming in, the
consumer-care phone number is two numbers run together and the batch and date
boxes disagree between the two packs. Exactly the failure the rules warn about.

**Raw, unprocessed back-of-pack photographs are still needed** for every product
before any declaration goes onto a listing.


## Placed in the mockup — 16 Sep

Four of the six are now in `storefront-design.html`, embedded as JPEG data URIs
sized to their rendered slot:

| Slot | Image |
|---|---|
| Hero | `hero-canopy.png` |
| Story band | `story-trunk-pepper-vine.png` |
| Category: Coffee & Tea | `cat-coffee-cherries.png` |
| Category: Spices | `cat-spices-pepper-vine.png` |

**Two category slots are filled with pack photographs as a stand-in** — Oils &
Syrups and Dry Fruits & Seeds. They read as studio product shots next to two
atmospheric nature shots, and the row does not hold together. Two more
atmospheric images are needed: a coconut/oil subject and a dry-fruit subject,
same treatment as the coffee cherries and the pepper vine.

Everything else on the page uses the **real pack photographs** from
`assets/packs/`. The hero still wants an upscale before launch.
