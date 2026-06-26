# Asset library (image catalog)

One row per real asset, populated by `asset-ingest` (`/ingest`). The source of record for which
images exist, what they show, and where they may be used. The subject-marketing packs and the
design/email gates read this to resolve a "real asset required" slot. A generated image of a
real person never gets a row here, so the catalog cannot return a fabricated likeness.

Columns: id | slug | placement | description | colors (hex) | dims | faces_present | rights | usage | alt text

| id | slug | placement | description | colors | dims | faces_present | rights | usage | alt |
|---|---|---|---|---|---|---|---|---|---|
| (seed: add rows with /ingest) | | | | | | | | | |

Placements: headshot, banner, post-image, logo, screenshot, product-shot, background.
Usage: ok-for-public | internal-only | needs-rights-check.

The Maharat instructor image catalogs are preserved at
`context/profiles/maharat/instructors/_IMAGE-CATALOG.md` and `_EMAIL-IMAGE-MANIFEST.md`.
