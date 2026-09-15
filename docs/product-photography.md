# Product images — visual direction and prompts

## The store's visual direction

Pinned here so the photography and the theme come from **one** decision. The
storefront is built to these values, and the prompts below reference them.

| Role | Hex | Where it is used |
|---|---|---|
| Paper | `#F4F2ED` | Page background — a soft, slightly cool paper, not cream |
| Card | `#FFFFFF` | Product cards and catalogue images sit on this |
| Canopy | `#1F4034` | Primary brand colour — deep shade-grown green of the Western Ghats |
| Laterite | `#A4552F` | Accent only — the red soil of Malnad. Buttons, sale tags, never large areas |
| Ink | `#2A2D27` | Text |
| Muted | `#6E7268` | Secondary text, captions |

The mood: **shade-grown, monsoon, unhurried.** Cool green and damp earth rather
than the warm-cream-and-hessian look every artisanal food brand uses. Natural
light, real texture, nothing glossy or over-styled.

## White or brand background?

Both, deliberately:

- **Image 1 stays on pure white.** It is the catalogue shot. White is portable —
  it survives a theme change, and it is what Amazon and Flipkart require if the
  client ever lists there. On the site it sits inside a white product card
  against the paper background, which is the standard pattern and reads clean.
- **Images 2 to 4 carry the brand palette.** These are the ones that make the
  page feel like Malnad rather than a marketplace.

Shooting everything on the brand background would look seamless today and cost a
full reshoot the first time anything changes.

## The rule that matters

**Enhance the real photograph. Do not generate a new product.**

Use image-to-image (upload the client's photo, ask for a relight), never
text-to-image. If the tool redraws the label, invents packaging, or changes the
colour of what is inside the bag, the listing now misrepresents the product — for
a food business that is the exact Legal Metrology and FSSAI problem the whole
build is designed to avoid.

**The test:** a customer holds the pack next to the photo on their phone. They
should match.

**Check every output for mangled label text.** Image tools routinely garble
lettering on packaging — "ARABICA" comes back "ARAB1CA". Zoom in on every label
before accepting an image. This is the single most common failure.

Keep every original file. Never overwrite.

---

## Prompt A — catalogue shot (image 1, every product)

> Professional e-commerce product photograph. **Keep the product and its
> packaging, label, lettering, logo and colours exactly as in the source image —
> do not redesign, re-letter, translate or invent any packaging detail.**
> Re-light only: soft even diffused daylight from the upper left with gentle fill
> from the right, no harsh glare, no blown highlights, no glossy commercial
> sheen. Pure white seamless background (#FFFFFF). Product centred and upright,
> shot straight on at eye level, filling about 80% of the frame with even margin
> all round. Soft natural contact shadow directly beneath so it sits on the
> surface. Colour-accurate and true to the original. Sharp focus edge to edge,
> crisp detail on all label text. Square 1:1, 2048×2048, photorealistic,
> restrained and natural rather than glossy.
>
> Negative: no text changes, no invented or redrawn labels, no altered branding,
> no watermark, no props, no hands, no people, no extra products, no studio
> reflections, no oversaturation, no HDR, no illustration or cartoon style.

## Prompt B — lifestyle shot (image 2)

Carries the brand palette. This is the one that has to feel like the estate.

> Same product with **packaging, label and lettering unchanged from the source
> image**. Place it on a dark weathered wood surface, with a small natural
> scatter of loose `[coffee beans / black peppercorns / green cardamom pods]`
> beside it. Background is a soft warm-grey paper tone (#F4F2ED) falling into a
> gentle blur of deep green shade-canopy foliage (#1F4034) in the upper corners.
> A hint of red laterite earth tone (#A4552F) in the wood. Soft directional
> morning light from the left, slightly misty and diffused as after monsoon rain.
> Shallow depth of field. Muted natural colour, cool green rather than warm
> golden. Photorealistic, unstyled, square 1:1, 2048×2048.
>
> Negative: same as Prompt A, plus no burlap or hessian sacking, no rustic
> clichés, no scattered coffee cups, no warm orange colour grade.

## Prompt C — texture shot (image 3)

Safest of the three — no packaging in frame, so nothing can be misrepresented.

> Macro photograph of `[freshly roasted arabica coffee beans / whole black
> peppercorns / green cardamom pods]` filling the frame, shot from directly
> above on a soft paper-toned surface (#F4F2ED). Natural soft daylight, shallow
> depth of field, rich texture with visible natural variation. Muted cool-natural
> colour grade. No packaging, no text, no props. Photorealistic, square 1:1,
> 2048×2048.

## Prompt D — back of pack (image 4, the declarations panel)

Different job from the other three: this one exists to make **printed text
readable**, not to look good. Beautifying it is how the content gets destroyed.

> Correct and clarify this photograph of printed product packaging. **Do not
> alter, redraw, re-letter, re-space, translate, spell-correct or regenerate any
> text, number, code or symbol. Every character must remain exactly as
> photographed**, including the FSSAI licence number, batch code, dates, net
> quantity, MRP and consumer care details. Correct the perspective so the pack
> face is flat and square to the camera. Remove glare, hotspots and reflections
> from the plastic film or laminate. Even out uneven lighting across the panel.
> Increase sharpness and local contrast so small print becomes legible. Reduce
> noise without smoothing or softening letterforms. Neutral white balance, colour
> accurate. Crop tight to the pack face with a small even margin. Square 1:1,
> 2048×2048, photorealistic.
>
> Negative: redrawn text, regenerated text, altered numbers, corrected spelling,
> translated text, invented label detail, smoothed lettering, blurred small print,
> watermark, added graphics, stylised filter, warm colour grade.

### The trap

**Never transcribe declarations from a processed image.**

Generative tools rewrite text they cannot read cleanly, and they do it
confidently — a blurred `8` becomes a crisp `3`. On this panel that means the
FSSAI licence number, the batch code or the net quantity could come back subtly
wrong, and it would be transcribed onto the listing as a legal declaration.

So the back-of-pack photo does two separate jobs and needs two separate files:

| File | Goes to | Purpose |
|---|---|---|
| **Raw, untouched photo** | Claude | Reading the declarations |
| Processed version | The website | Image 4 on the product page |

If the raw photo is too blurred to read, **ask for a better photo**. Do not run
it through a tool and read the output.

### A safer option than AI for this one

A plain document-scanner app — the kind built into most phones — does perspective
correction, deglare and sharpening **without any generative redraw**. For a panel
of small legal print that is usually the better tool. Use AI here only if the
scanner app cannot rescue the photo.

---

## Image set per product

| Position | Image | Prompt | Background |
|---|---|---|---|
| 1 | Pack, straight on | A | Pure white |
| 2 | Pack in context on wood | B | Brand palette |
| 3 | Macro of the contents | C | Paper `#F4F2ED` |
| 4 | Back of pack, declarations panel | D | As photographed |

Image 4 is worth including wherever the label is readable — it shows the
declarations on the actual pack and reassures a careful buyer.

## Consistency beats perfection

Across thirty products, **the same framing, the same light direction, the same
crop** matters more than any single image being beautiful. A collection grid
where every product sits at a different size and angle looks amateur however good
the individual shots are. Run the same prompt, change only the product.

## File specs

- **Square, 2048 × 2048** — Shopify's recommended size
- JPEG or PNG, under 20 MB, under 20 megapixels
- Name files to match the catalogue: `mac-1.jpg`, `mac-2.jpg`, `mbp-1.jpg`
- First image in the list becomes the main one

## Variants

One image set per **product**, not per pack size — unless the packs genuinely
look different (a 1 kg sack versus a 250 g pouch). Where they do, shoot the
distinct ones and note which variant each belongs to.
