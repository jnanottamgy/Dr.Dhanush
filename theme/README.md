# Theme source — `Malnad Spices — build`

Files we add to the Horizon theme. Horizon itself is not vendored here; only
what we write lives in this folder, so a diff shows our changes and nothing
else.

Target theme: `Malnad Spices — build`, `gid://shopify/OnlineStoreTheme/146238865521`,
UNPUBLISHED. The live theme is never written to — the Shopify connector blocks
writes to the MAIN theme, which is also the right way round.

| File | What |
|---|---|
| `blocks/compliance-declarations.liquid` | The pack declarations panel |
| `snippets/compliance-row.liquid` | One declaration row, with the gap treatment |
| `assets/compliance-declarations.js` | Switches declarations with the selected pack |

## How these get into the theme

`themeFilesUpsert` accepts a body of type `URL`, and this repository is public,
so Shopify fetches each file straight off `raw.githubusercontent.com` rather
than us pasting file bodies through the connector. Same route the 70 pack
photographs took.

After pushing a change here, re-run the upsert so the theme picks it up —
Shopify copies the file at upsert time, it does not track the URL.

## Why the declarations block is built this way

Net quantity, MRP, packing date and best before are printed **per pack**: a
250 g and a 1 kg of the same product declare different figures. Horizon updates
variant-dependent blocks in place rather than re-rendering the section, so a
panel rendered only for the selected variant would keep showing the first pack's
net quantity after a customer switched size. Instead every variant's rows are
rendered server-side and `compliance-declarations.js` reveals the selected one.

A declaration that is not printed on the pack renders **"Not printed on this
pack."** It is never filled in, inferred, or carried across from another pack.
