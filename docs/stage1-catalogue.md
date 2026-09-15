# Stage 1 — Catalogue and compliance data

Needs **no credentials**. Runs in parallel with Razorpay KYC and Meta verification.

## The pipeline

```
catalogue sheet (client fills)
      │
      ├─ validate_catalogue.py      refuses to pass incomplete or illegal data
      │
      ├─ build_shopify_import.py    → build/shopify-import.csv, everything Status=draft
      │
      ├─ test import (2 products)   proves the metafield columns land
      ├─ full import (all products) still draft
      │
      └─ audit_live_products.py     standing check that nothing live is incomplete
```

## How the compliance guarantee actually works

**Shopify does not natively refuse to publish a product with an empty metafield.**
Metafield validation rules constrain *values*, not presence. Anyone claiming the
platform blocks it is wrong. The guarantee is real, but it comes from four
mechanisms we build, not from Shopify:

1. **`validate_catalogue.py` will not produce an import** while any declaration
   is missing. Exit code 1, no file written.
2. **Everything imports as `Status: draft`, `Published: FALSE`.** A human has to
   deliberately publish, and by then the data is already complete.
3. **The product template renders the declarations block from the metafields**, so
   a missing one is visible on the page rather than silently absent.
4. **`audit_live_products.py` catches drift** — a product added by hand in admin
   later, or a metafield cleared by accident. Run before launch and weekly after.
   Exits non-zero, so it can gate a release.

## Metafield definitions to create

Shopify admin → **Settings → Custom data**. Create under **Products** and
**Variants** respectively. Namespace is `compliance` throughout.

### Products → Add definition

| Name | Key | Type |
|---|---|---|
| Packer name | `compliance.packer_name` | Single line text |
| Packer address | `compliance.packer_address` | Multi-line text |
| Country of origin | `compliance.country_of_origin` | Single line text |
| Consumer care name | `compliance.care_name` | Single line text |
| Consumer care phone | `compliance.care_phone` | Single line text |
| Consumer care email | `compliance.care_email` | Single line text |
| FSSAI licence number | `compliance.fssai_licence` | Single line text |
| HSN code | `compliance.hsn_code` | Single line text |
| GST rate | `compliance.gst_rate` | Decimal |
| Ingredients | `compliance.ingredients` | Multi-line text |
| Storage instructions | `compliance.storage` | Multi-line text |
| Estate | `compliance.estate` | Single line text |
| Altitude (ft) | `compliance.altitude_ft` | Integer |
| Harvest month | `compliance.harvest_month` | Single line text |
| Roast level | `compliance.roast_level` | Single line text |

### Variants → Add definition

These differ between a 250 g and a 1 kg pack, so they belong on the variant, not
the product. Putting them on the product is the most common way a compliant-looking
store ends up declaring the wrong net quantity.

| Name | Key | Type |
|---|---|---|
| Net quantity | `compliance.net_quantity` | Single line text |
| MRP | `compliance.mrp` | Decimal |
| Date of manufacture | `compliance.mfg_date` | Single line text |
| Best before | `compliance.best_before` | Single line text |

Tick **"Store in storefront"** (storefront access) on every one, or the theme
cannot render them.

## MRP is not the compare-at price

Shopify's *Compare at price* is a marketing field — it renders as a struck-through
"was" price. **MRP is a legal declaration.** They are different things and
conflating them is a trap:

- `compliance.mrp` (variant metafield) — always set, always the real MRP.
- `Variant Compare At Price` — set **only** when the selling price is genuinely
  below MRP, so the discount is honest.

The builder does exactly this: compare-at is written only when `MRP > selling price`.

## Import order

1. **Upload images to Shopify Files first.** The CSV references images by
   filename; if they are not uploaded, the import silently skips them.
2. **Test import with two products.** This is a gate, not a formality — it proves
   the `product.metafields.*` and `variant.metafields.*` columns actually land
   before 30 products are loaded on an unverified assumption.
3. Check on the two test products: both option levels correct, metafields
   populated on product *and* variant, status draft, inventory policy `deny`.
4. Only then import the rest.

## Running it

```sh
python3 scripts/validate_catalogue.py  templates/catalogue-template.csv
python3 scripts/build_shopify_import.py <filled-sheet.csv> build/shopify-import.csv
python3 scripts/audit_live_products.py  <products_export.csv>
```

`fixtures/catalogue-filled-sample.csv` is a worked example that passes validation —
useful for testing the pipeline before the client's real sheet arrives.

## Inventory policy

Every variant is written with `Variant Inventory Policy: deny`. Shopify will
refuse to sell a variant once stock reaches zero. This is what stops the website
selling coffee already sold at the estate gate, and it is set at import rather
than left to a default.
