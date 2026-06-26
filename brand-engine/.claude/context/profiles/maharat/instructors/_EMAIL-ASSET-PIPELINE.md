# Email asset pipeline (the GitHub-to-Ortto source-to-serve map)

The source of truth for how each instructor email image moves from its origin to a live, servable
email `img src`. The architecture is Ahmed's: GitHub is the SOURCE of truth, Ortto is the SERVE
host. The committed bytes under `assets/email/<slug>/` are the canonical source, and the live email
`img src` is the Ortto serve URL once the same bytes are uploaded to the Ortto CDN.

This file is the human-readable companion to the machine-readable map
`context/instructors/email-asset-pipeline.json`. The map is the source of truth for the per image
serve URL and status; the script `scripts/email_asset_pipeline.py` reads and writes it; the renderer
`scripts/email_render.py` resolves an image src to its Ortto serve URL when the map marks it
`served`; and the gate `skills/email-asset-qa` blocks any send while a header is not on an approved
host.

House style on this file: no em dash, no en dash, no tatweel, Western numerals only.

## Why this exists (the host problem, stated once)

- The repo is private, so a GitHub raw URL will not render in an email client. GitHub is the source
  of truth, not the serve host.
- A raw CloudFront cover (`dt92b02v6m7lx.cloudfront.net`) is the verified design proof, but it is a
  hotlink-protected object: a different fetch path can return 403, and it is not an approved email
  host per `runtime/email-module-map.md` and `skills/email-asset-qa`.
- A Google Drive link is not hot-linkable in email at all.

So the bytes are committed to GitHub (the source of record, diffable, reviewable) and then uploaded
to the Ortto CDN (the approved serve host: `m.autopilotapp.com`, `ic.autopilotapp.com`). The live
`img src` is the Ortto URL. Until then, the renderer previews on the CloudFront proof and the asset
gate blocks the send.

## The pipeline

Three steps, each needing a different access, run in the environment that has it:

1. Fetch sources into the GitHub folders. Download every CloudFront class cover into its
   `github_path` under `assets/email/<slug>/`, and pull every Drive body portrait into the same
   folders. Needs an OPEN NETWORK for the covers (curl to CloudFront) and DRIVE ACCESS for the
   portraits (the Drive MCP). Covers: `python3 scripts/email_asset_pipeline.py fetch-covers`.
   Portraits: an agent calls `mcp__Google_Drive__download_file_content` and writes the decoded bytes
   to the `github_path` (a script cannot call the MCP, so this is an agent step, documented below).
2. Commit. The fetched bytes under `assets/email/` ARE committed: they are the GitHub source of
   truth. (`assets/email/` is tracked, not gitignored, unlike the `assets/instructors/` Drive byte
   cache. `scripts/image_catalog_check.py` allows committed binaries under `assets/email/` and only
   forbids them under `assets/instructors/`.)
3. Upload to Ortto and record serve URLs. Upload each committed `github_path` to the Ortto serve CDN
   and write the returned URL back into the map as `ortto_serve_url` with status `served`. Needs
   ORTTO API access (an `ORTTO_API_KEY` and the upload endpoint, supplied as environment variables,
   never inlined). `python3 scripts/email_asset_pipeline.py upload-ortto`. The real Ortto API call
   is a TODO gated on Ahmed's adoption of Ortto upload access; the interface and the map write-back
   are implemented, no endpoint or key is invented.

After step 3, `scripts/email_render.py` automatically resolves that image's src to its Ortto serve
URL (the map is the source of truth), and `skills/email-asset-qa` passes the header on the
host-and-render check. Before step 3, the src stays on the CloudFront proof for preview and the gate
blocks the send.

## What this sandbox completed, and what is pending its environment

This locked-egress sandbox completed the STRUCTURE, the MAP, the SCRIPT, and ONE PROOF image:

- Structure: per-instructor source folders `assets/email/<slug>/` for every instructor in the
  manifest, committed and tracked (the `.gitignore` keeps `assets/email/**` tracked even if a
  broader assets ignore is added; the instructor cache and font binaries stay ignored).
- Map: `email-asset-pipeline.json` (machine-readable) and this file (human-readable), one row per
  image (header EN cover, header AR cover, body portrait) for every instructor and class, language
  matched from the corrected `_EMAIL-IMAGE-MANIFEST.md`.
- Script: `scripts/email_asset_pipeline.py` with `status`, `fetch-covers`, and `upload-ortto`.
- One proof image: the Drive-to-GitHub path is proven with one real, rights-cleared Bassam studio
  portrait committed under `assets/email/bassam-fattouh/` (see "Proof" below).

Pending its environment (each needs the access the sandbox lacks):

- Cover fetch (OPEN NETWORK): the egress here is locked, a direct curl to CloudFront returns 403.
  `fetch-covers` fails gracefully per item with the egress-blocked notice and changes nothing. Run
  it in CI or locally where the network is open to pull the 13 cover URLs into `assets/email/`.
- The other Drive portraits (DRIVE ACCESS): only Bassam's proof image is fetched here (one heavy
  Drive fetch, to avoid context overflow). The remaining body portraits are pulled by an agent via
  the Drive MCP in a Drive-access run, into their `github_path`.
- Ortto upload (ORTTO API): Ortto upload access is not available here, so every `ortto_serve_url`
  is `pending`. `upload-ortto` reports the ready-to-upload queue and stops, inventing no endpoint.
  Run it once Ahmed adopts Ortto upload access and the `_upload_one_to_ortto` TODO is implemented.

## Proof of the Drive-to-GitHub path

The intended proof image was Bassam's on-brand near-black #141414 body portrait
`15052024_BassamBG_141414.png` (Drive fileId `1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR`). Its Drive
metadata reports 22.8 MB (about 30 MB base64), which overflows the sandbox context. So, per the
documented fallback, the already-cached, rights-cleared Bassam studio portrait
`assets/instructors/bassam-fattouh/MAHARAT_III0507.jpg` (a real Maharat asset, Canon EOS R5,
4107x6158) was copied to `assets/email/bassam-fattouh/MAHARAT_III0507.jpg` as the live proof that an
image lands committed under `assets/email/`. Its row is marked `fetched` in the map, with the
substitution noted. The on-brand `15052024_BassamBG_141414.png` is fetched in the open-network or
Drive-access run and replaces the `github_path`.

How the Drive portraits are fetched (the agent step, since a script cannot call the MCP):

1. Read each `drive:<fileId>` source and its `github_path` from the map.
2. For each, an agent calls `mcp__Google_Drive__download_file_content` with that `fileId` (PNG and
   JPG return base64 directly; check `get_file_metadata` for size first, large files are fetched one
   at a time to avoid context overflow).
3. Decode the base64 and write the bytes to the `github_path` under `assets/email/<slug>/`.
4. Set the row status to `fetched`, commit, then run `upload-ortto` to stage to Ortto.

## Status vocabulary (the map's `status` field)

- `pending-fetch`: the source is known, the bytes are not yet in `github_path`.
- `fetched`: the bytes are committed under `github_path` (the GitHub source of truth).
- `pending-ortto`: fetched, but not yet uploaded to the Ortto serve CDN.
- `served`: `ortto_serve_url` is live on an approved Ortto host. The only send-ready state.
- `blocked`: carries a `blocked_reason` and never advances. Used for salam's intended cover
  (dakak-cover.png, dead 403) and mona (no verified header, no hero-grade portrait), consistent with
  `_EMAIL-IMAGE-MANIFEST.md`. Salam's active header (the interim SD_PLANS banner) is NOT blocked: it
  is `pending-fetch` like the other CloudFront covers.

Any state other than `served` is a send-blocking state for `skills/email-asset-qa`.

## Per instructor and class (one row per image)

Language matching, from the corrected `_EMAIL-IMAGE-MANIFEST.md`: LEFTGRADIENT / EN-PAGE is the
English page header, RIGHTGRADIENT / AR-PAGE is the Arabic page header, and a neutral cover
(LEFTRIGHTGRADIENT, NOGRADIENT, or a class still) serves both pages. Body portraits are the on-brand
#141414 Drive exports where they exist. Every CloudFront cover here was verified servable at source
server-side on 2026-06-18 (the manifest is the record); CloudFront is the design proof, the serve
host is Ortto.

| slug | class | image | source | github_path | status |
|---|---|---|---|---|---|
| bassam-fattouh | Makeup | header (neutral) | CF BF_CLASSCOVER_LEFTRIGHTGRADIENT.JPG | assets/email/bassam-fattouh/BF_CLASSCOVER_LEFTRIGHTGRADIENT.JPG | pending-fetch |
| bassam-fattouh | Makeup | body | drive 1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR (15052024_BassamBG_141414.png) | assets/email/bassam-fattouh/MAHARAT_III0507.jpg | fetched (proof substitution) |
| bassam-fattouh-bridal | Bridal | header (EN) | CF BFBRIDAL_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp | assets/email/bassam-fattouh-bridal/BFBRIDAL_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp | pending-fetch |
| bassam-fattouh-bridal | Bridal | header (AR) | CF BFBRIDAL_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp | assets/email/bassam-fattouh-bridal/BFBRIDAL_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp | pending-fetch |
| bassam-fattouh-bridal | Bridal | body | drive 1rB5d_qon2DNCn5AU0GXm1SeY1gczqK1H (bridal class still) | assets/email/bassam-fattouh-bridal/250501_CH09_BRIDAL_.00_01_02_24.Still001.png | pending-fetch |
| ragheb-alama | Music | header (neutral) | CF RA_CLASSCOVER_DESKTOP_01_NOGRADIENT.webp | assets/email/ragheb-alama/RA_CLASSCOVER_DESKTOP_01_NOGRADIENT.webp | pending-fetch |
| ragheb-alama | Music | body | drive 1zcOPrkscCaqYZbRfvu_uZH3RoeWbqL97 (04032024_RaghebBG_141414.png) | assets/email/ragheb-alama/04032024_RaghebBG_141414.png | pending-fetch |
| kosai-khauli | Acting | header (neutral) | CF 02_240222_BEGINNINGS.00_03_55_10.Still001-02.webp | assets/email/kosai-khauli/02_240222_BEGINNINGS.00_03_55_10.Still001-02.webp | pending-fetch |
| kosai-khauli | Acting | body | drive 1d8J0UPHnw7Z9ZZHYNSheo26ri_FtCCN9 (04032024_KosaiBG_141414.png) | assets/email/kosai-khauli/04032024_KosaiBG_141414.png | pending-fetch |
| rahma-riad | Digital career | header (EN) | CF RR_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp | assets/email/rahma-riad/RR_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp | pending-fetch |
| rahma-riad | Digital career | header (AR) | CF RR_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp | assets/email/rahma-riad/RR_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp | pending-fetch |
| rahma-riad | Digital career | body | drive 1-NgbV23l0tkPKL7zrNoiCvZjx7g5N6YH (18092024_RahmaBG_141414_IMG1.png) | assets/email/rahma-riad/18092024_RahmaBG_141414_IMG1.png | pending-fetch |
| toufic-kredieh | Business | header (EN) | CF TK_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp | assets/email/toufic-kredieh/TK_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp | pending-fetch |
| toufic-kredieh | Business | header (AR) | CF TK_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp | assets/email/toufic-kredieh/TK_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp | pending-fetch |
| toufic-kredieh | Business | body | drive 13qCpVNKKOYmGIkYPlFqW4tZayWlIfDKo (TouficBG_141414_3922.png) | assets/email/toufic-kredieh/TouficBG_141414_3922.png | pending-fetch |
| cedric-haddad | Styling | header (EN) | CF CH_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp | assets/email/cedric-haddad/CH_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp | pending-fetch |
| cedric-haddad | Styling | header (AR) | CF CH_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp | assets/email/cedric-haddad/CH_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp | pending-fetch |
| cedric-haddad | Styling | body | drive 16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX (Maharat-Cedric-173.jpg) | assets/email/cedric-haddad/Maharat-Cedric-173.jpg | pending-fetch |
| elda-choucair | Marketing | header (EN) | CF EC_CLASSCOVER_DESKTOP_01_EN-PAGE.webp | assets/email/elda-choucair/EC_CLASSCOVER_DESKTOP_01_EN-PAGE.webp | pending-fetch |
| elda-choucair | Marketing | header (AR) | CF EC_CLASSCOVER_DESKTOP_01_AR-PAGE.webp | assets/email/elda-choucair/EC_CLASSCOVER_DESKTOP_01_AR-PAGE.webp | pending-fetch |
| elda-choucair | Marketing | body | drive 1v5uTO-8RRyOgRB1EbfJa5aT6lSpPwdmw (C08-maharat-1038.jpg) | assets/email/elda-choucair/C08-maharat-1038.jpg | pending-fetch |
| salam-dakkak | Cooking | header-intended-dead | CF dakak-cover.png (DEAD, 403, og:image type) | assets/email/salam-dakkak/dakak-cover.png | blocked (dead cover) |
| salam-dakkak | Cooking | header (active, interim) | CF SD_PLANS_BOTTOMGRADIENT.jpg (interim banner, plans-page image, not a dedicated class cover) | assets/email/salam-dakkak/SD_PLANS_BOTTOMGRADIENT.jpg | pending-fetch (stage to Ortto) |
| salam-dakkak | Cooking | body | drive 1jqvpgEQIjTbqwHIt-zw9TmmZr57v75qB (11032024_SalamBG_141414.png) | assets/email/salam-dakkak/11032024_SalamBG_141414.png | pending-fetch |
| mona-ataya | Entrepreneurship | header | none captured (no class page) | assets/email/mona-ataya/HEADER-NOT-SOURCED.txt | blocked (no verified header) |
| mona-ataya | Entrepreneurship | body | drive 1_nBXBQxesxf8Iec0Jkvdgh-LIXD8o0vH (maharat-1849.JPG, LOWRES) | assets/email/mona-ataya/maharat-1849.JPG | blocked (no hero-grade portrait) |

### Portrait instructor-card images (the "our other classes" ClassCardGrid)

These are the maharat.com instructor-grid portraits (the `*_HOMEPORTRAIT_BOTTOMGRADIENT*` and
`*BG_141414-BOTTOM-GRADIENT*` variants), the text-free on-brand near-black portrait each ClassCardGrid
card uses. The instructor name and the page-cleared Teaches subject are a LIVE HTML overlay in the
email (never baked into the image). Each portrait was verified servable server-side on CloudFront
2026-06-18 (a server-side fetch returned WEBP image bytes or a "cannot process image/webp"; both mean
servable). Like every other email asset, each portrait stages to the Ortto CDN before any send; the
renderer previews on the CloudFront proof until then.

| slug | class | image | source | github_path | status |
|---|---|---|---|---|---|
| bassam-fattouh | Makeup | card portrait | CF BF_HOMEPORTRAIT_BOTTOMGRADIENT_Fixed.webp | assets/email/bassam-fattouh/BF_HOMEPORTRAIT_BOTTOMGRADIENT_Fixed.webp | pending-fetch |
| bassam-fattouh-bridal | Bridal | card portrait | CF BFBRIDAL_HOMEPORTRAIT_BOTTOMGRADIENT_RECOLORED.webp | assets/email/bassam-fattouh-bridal/BFBRIDAL_HOMEPORTRAIT_BOTTOMGRADIENT_RECOLORED.webp | pending-fetch |
| cedric-haddad | Styling | card portrait | CF CH_HOMEPORTRAIT_BOTTOMGRADIENT.webp | assets/email/cedric-haddad/CH_HOMEPORTRAIT_BOTTOMGRADIENT.webp | pending-fetch |
| elda-choucair | Marketing | card portrait | CF EC_HOMEPORTRAIT_BOTTOMGRADIENT.webp | assets/email/elda-choucair/EC_HOMEPORTRAIT_BOTTOMGRADIENT.webp | pending-fetch |
| ragheb-alama | Music | card portrait | CF 05032024_RaghebBG_141414-BOTTOM-GRADIENT-01.webp | assets/email/ragheb-alama/05032024_RaghebBG_141414-BOTTOM-GRADIENT-01.webp | pending-fetch |
| kosai-khauli | Acting | card portrait | CF 04032024_KosaiBG_141414-BOTTOM-GRADIENT-01.webp | assets/email/kosai-khauli/04032024_KosaiBG_141414-BOTTOM-GRADIENT-01.webp | pending-fetch |
| rahma-riad | Digital career | card portrait | CF RR_HOMEPORTRAIT_BOTTOMGRADIENT.webp | assets/email/rahma-riad/RR_HOMEPORTRAIT_BOTTOMGRADIENT.webp | pending-fetch |
| toufic-kredieh | Business | card portrait | CF TK_HOMEPORTRAIT_BOTTOMGRADIENT.webp | assets/email/toufic-kredieh/TK_HOMEPORTRAIT_BOTTOMGRADIENT.webp | pending-fetch |
| salam-dakkak | Cooking | card portrait | CF 11032024_SalamBG_141414-BOTTOM-GRADIENT-02.webp | assets/email/salam-dakkak/11032024_SalamBG_141414-BOTTOM-GRADIENT-02.webp | pending-fetch |

Note on the portrait cards versus the salam and mona headers: the portrait card is a SEPARATE asset
from the email header. Mona remains blocked on her own class-cover header (above); salam's active
header is the interim SD_PLANS banner (pending-fetch, stage to Ortto). Their portrait-card image
(used when another instructor's email lists them as an "other class") is a real, servable, text-free
grid portrait, so it stages through this pipeline like the rest. The ClassCardGrid never lists the
email's own instructor, so a header issue does not block a portrait card appearing in someone else's
email.

Header notes, consistent with `_EMAIL-IMAGE-MANIFEST.md`:

- salam-dakkak: the intended class cover `dakak-cover.png` is dead (403, the og:image type). The
  build's active header is the verified `SD_PLANS_BOTTOMGRADIENT.jpg`, treated like the other
  CloudFront covers (stage to Ortto before send). It is an INTERIM banner (the plans-page image, not
  a dedicated class cover) until a real Salam class cover is produced. Flag for Ahmed.
- mona-ataya: no `masterclass-pages.md`, so no in-page class cover was captured or verified, and no
  approved-host header is confirmed. Mona also has no retouched or on-brand portrait set (LOWRES
  selects only), so no hero-grade body image exists. Capturing a class-page cover and producing a
  hero-grade portrait are the preconditions before any Mona email build. Flag for Ahmed.

## How it connects

- `scripts/email_asset_pipeline.py`: the driver. `status` (default) reports per image
  present-on-disk vs missing and served vs pending; `fetch-covers` pulls the CloudFront covers into
  `assets/email/` (open network); `upload-ortto` stages each committed asset to Ortto and writes the
  serve URL back into the map (gated on adoption).
- `scripts/email_render.py`: resolves an image src to its `ortto_serve_url` when the map marks it
  `served`, else falls back to the CloudFront cover for the design proof. All pending today, so the
  rendered output is unchanged; the src flips to Ortto per image as each row is served.
- `skills/email-asset-qa`: the asset gate. Blocks any send while a header is not on an approved
  Ortto host. The pipeline map is the source of truth for the serve URL, and any state other than
  `served` (pending-fetch, fetched, pending-ortto, blocked) is a send-blocking state.
- `context/instructors/_EMAIL-IMAGE-MANIFEST.md`: the upstream record of which cover and which
  portrait fills each slot, and the verified-servable finding. This pipeline carries those sources
  through to the GitHub source of truth and the Ortto serve URL.
