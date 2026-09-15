# Product images — prompts and rules

## The rule that matters

**Enhance the real photograph. Do not generate a new product.**

Use image-to-image (upload the client's photo, ask for a relight), never
text-to-image. If the tool redraws the label, invents packaging, or changes the
colour of what's inside the bag, the listing now misrepresents the product — for
a food business that is the exact Legal Metrology and FSSAI problem the whole
build is designed to avoid.

**The test:** a customer holds the pack next to the photo on their phone. They
should match.

**Check every output for mangled label text.** Image tools routinely garble
lettering on packaging — "ARABICA" comes back "ARAB1CA". Zoom in on every label
before accepting an image. This is the single most common failure.

Keep every original file. Never overwrite.

---

## Prompt A — catalogue shot (use this for the main product image)

> Professional e-commerce product photograph. **Keep the product and its
> packaging, label, lettering, logo and colours exactly as in the source image —
> do not redesign, re-letter, translate or invent any packaging detail.**
> Re-light only: soft even diffused studio lighting from the upper left with
> gentle fill from the right, no harsh glare, no blown highlights. Pure white
> seamless background (#FFFFFF). Product centred and upright, shot straight on at
> eye level, filling about 80% of the frame with even margin all round. Add a
> soft natural contact shadow directly beneath the product so it sits on the
> surface. Colour-accurate and true to the original. Sharp focus edge to edge,
> crisp detail on all label text. Square 1:1, 2048×2048, photorealistic,
> commercial catalogue quality.
>
> Negative: no text changes, no invented or redrawn labels, no altered branding,
> no watermark, no props, no hands, no people, no extra products, no studio
> reflections, no oversaturation, no illustration or cartoon style.

## Prompt B — lifestyle shot (second or third image on the page)

> Same product with **packaging, label and lettering unchanged from the source
> image**. Place it on a weathered dark wood surface with a small scatter of
> loose `[coffee beans / black peppercorns / green cardamom pods]` beside it,
> arranged naturally. Soft directional morning light from the left. Shallow depth
> of field, background falling into a gentle blur of green Western Ghats foliage.
> Warm natural tone, slightly earthy. Photorealistic, square 1:1, 2048×2048.
>
> Negative: same as Prompt A.

## Prompt C — texture shot (safest, and genuinely sells produce)

No packaging in frame, so nothing can be misrepresented.

> Macro photograph of `[freshly roasted arabica coffee beans / whole black
> peppercorns / green cardamom pods]` filling the frame, shot from directly
> above. Natural soft daylight, shallow depth of field, rich texture, visible
> natural variation and detail. No packaging, no text, no props. Photorealistic,
> square 1:1, 2048×2048.

---

## What to shoot per product

| Position | Image | Prompt |
|---|---|---|
| 1 | Pack, straight on, white background | A |
| 2 | Pack in context on wood with loose product | B |
| 3 | Close macro of the contents | C |
| 4 | Back of pack showing the label, if legible | A, or the raw photo |

Image 4 is worth including where the label is readable — it shows the
declarations on the actual pack and builds trust with a careful buyer.

## File specs

- **Square, 2048 × 2048** — Shopify's recommended size
- JPEG or PNG, under 20 MB, under 20 megapixels
- Name files to match the catalogue: `mac-1.jpg`, `mac-2.jpg`, `mbp-1.jpg`
- Same crop and framing across all products, or the collection grid looks untidy

## Variants

One set of images per **product**, not per pack size — unless the packs look
genuinely different (a 1 kg sack versus a 250 g pouch). Where they do, shoot the
distinct ones and note which variant each belongs to.
