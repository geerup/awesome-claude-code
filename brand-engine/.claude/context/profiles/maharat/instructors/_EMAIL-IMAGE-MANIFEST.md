# Email image manifest (the per-instructor header and body registry)

The source of truth for which image fills which slot in a built instructor email, and the
gate-zero record of whether each instructor has a verified-servable header. No instructor
email HTML is generated until this manifest provides a verified header image for that
instructor and class. See `skills/05-build-launch/email-html-build/SKILL.md` (precondition)
and `skills/email-asset-qa/SKILL.md` (the header-image-present-and-servable hard check).

House style on this file: no em dash, no en dash, no tatweel, Western numerals only.

## Methodology

Each candidate URL was verified server-side with the firecrawl scrape tool (formats
["markdown"], proxy "basic"). The interpretation, fixed for this registry:

- If the fetch errors "cannot process ... image/*", or the body begins with image binary
  (JFIF, EXIF, RIFF/WEBP, PNG), the image IS servable. Recorded `verified`.
- If the fetch returns a 403 or 404, or an `<Error>AccessDenied</Error>` XML body, it is NOT
  servable. Recorded `BLOCKED`.
- A cover not yet fetched is `pending`, never guessed.

Re-verified 2026-06-18 (this correction). The headers are the per-class, language-matched
`*_CLASSCOVER_*` covers on `dt92b02v6m7lx.cloudfront.net`, read from each instructor's
`skills/instructor-marketing/<slug>/masterclass-pages.md` "Cover image" line (the in-page class
cover), cross-checked against `context/instructors/_IMAGE-CATALOG.md`. LEFTGRADIENT is the English
page, RIGHTGRADIENT is the Arabic page (the gradient falls toward the reading-start edge); a
language-neutral cover (LEFTRIGHTGRADIENT, NOGRADIENT, or a class still) serves both pages.

### Correction note, 2026-06-18 (the autopilot-header error, fixed)

The earlier registry listed the autopilot numbered images (`ic.autopilotapp.com/images/ap-maharat/`
`1_7.png`, `2_7.png`, `3_6.png`, and the named `توفيق كريدية.png`) as per-instructor headers and as
"approved-host" header sources. That was WRONG. Those images are generic Maharat carousel art, not
per-instructor class covers. Direct evidence: `2_7.png` renders as the multi-instructor "مواجهة
التحديات" carousel cover, not a Bassam class cover. They are removed below as header sources and as
any "approved-host header" claim. The correct, language-matched headers are the `*_CLASSCOVER_*`
variants, each verified servable server-side this session (see the per-instructor entries). Those
covers are on CloudFront, which is the design proof, not an approved email host: every one stages to
the Ortto CDN before any send. No instructor header is send-ready on an approved host yet.

## The host finding (why this manifest exists)

1. In-page class cover works at source. The `*_CLASSCOVER_*` variant on
   `dt92b02v6m7lx.cloudfront.net` (for example `BF_CLASSCOVER_LEFTRIGHTGRADIENT.JPG`) returns
   real image bytes to a server-side fetch. This is the correct header source.
2. The og:image variant 403s. The `*_CLASS_PAGE_*` / `*_RIGHTGRADIENT.JPG` og:image variant
   returns 403 AccessDenied and renders as broken alt text in an inbox. That was the bug fixed
   in commit 6bf87a4. Never use the og:image variant for a header.
3. CloudFront is not an approved email host. Per `runtime/email-module-map.md` and
   `skills/email-asset-qa`, an email `img src` must be on the approved Ortto CDN
   (`m.autopilotapp.com`, `ic.autopilotapp.com`, `app-rsrc.getbee.io` for social icons). A
   servable CloudFront cover proves the bytes exist and resolve, it is the design proof, but the
   header must still be staged to the Ortto CDN (or proven with an inbox send-test) before the
   build is send-ready. CloudFront in a raw `img src` is a hotlink-protected object that can 403
   on a different fetch path.
4. The autopilot CDN is an approved host, but its numbered images are NOT per-instructor headers.
   `ic.autopilotapp.com/images/ap-maharat/` is an approved Ortto host and renders reliably in email,
   and the Maharat logo `https://m.autopilotapp.com/maharat/logo/l_80b9b5a2-f18b-4bc7-a859-2cf899449f05.png`
   is verified servable there. BUT the numbered images on it (`1_7.png`, `2_7.png`, `3_6.png`, and
   the named `توفيق كريدية.png`) are generic Maharat carousel art, not per-instructor class covers,
   and must NOT be used as instructor headers. Evidence: `2_7.png` renders as the multi-instructor
   "مواجهة التحديات" carousel cover, not a Bassam class cover. They are servable, but servable-and-
   wrong: a correct header must be the instructor's own class cover. The per-class `*_CLASSCOVER_*`
   covers (point 1) are the correct headers; they are on CloudFront and still need Ortto staging.
5. Drive body images need hosting. The Google Drive instructor photography in
   `context/instructors/_IMAGE-CATALOG.md` (for example Bassam's on-brand #141414 portrait
   `15052024_BassamBG_141414`) is good body imagery, but Drive links are not hot-linkable in email.
   A Drive body image is BLOCKED until it is staged to the Ortto CDN or composed and hosted via
   Canva. Flagged per instructor as `needs-hosting`.

## Status vocabulary

- header_image status: `verified` (servable at source), `pending` (not fetched), `BLOCKED`
  (403/404 or no cover). The header is recorded per language where the cover is language-split:
  EN page (LEFTGRADIENT / EN-PAGE) and AR page (RIGHTGRADIENT / AR-PAGE). A language-neutral cover
  (LEFTRIGHTGRADIENT, NOGRADIENT, or a class still) is one image for both pages.
- send_ready: `yes` only when a verified-servable header sits on an approved email host (Ortto
  CDN) or is proven by an inbox send-test. `BLOCKED` otherwise, with the reason. A header that is
  verified servable only on CloudFront is `BLOCKED: stage header to Ortto CDN` because CloudFront
  is not an approved email `img src` host. As of 2026-06-18 NO instructor header is send-ready: all
  correct headers are CloudFront `*_CLASSCOVER_*` covers awaiting Ortto staging, and salam is
  additionally blocked on a dead cover. The autopilot numbered images are not headers (see the
  correction note), so they no longer make any instructor send-ready.
- body_image hosting: `needs-hosting` for any Drive id (stage to Ortto CDN or compose and host
  via Canva before use).
- Text overlay: a headline over a header is always a live HTML copy slot over a text-free image,
  never baked pixels, per `context/email-design-system.md`.

## The reconciliation rule, stated once

A header can be "verified servable" yet not "send-ready". Verified means the bytes resolve.
Send-ready means the verified header sits on an approved email host. The header is gate-zero:
the build does not start without a verified header, and it does not pass the asset gate or ship
without that header on an approved host.

---

## The registry

### bassam-fattouh, Teaches Makeup

- slug: bassam-fattouh
- class: Bassam Fattouh, Teaches Makeup (design-style)
- header_image (EN and AR, language-neutral): `https://dt92b02v6m7lx.cloudfront.net/BF_CLASSCOVER_LEFTRIGHTGRADIENT.JPG`
  - source: in-page class cover (masterclass-pages.md), the `_CLASSCOVER_LEFTRIGHTGRADIENT` variant,
    one image serving both pages
  - status: `verified` (server-side fetch returned Exif/JFIF image bytes, 2026-06-18)
- autopilot note: the previously listed `2_7.png` is NOT this class header. It is the generic
  multi-instructor "مواجهة التحديات" carousel cover (see the correction note). Removed as a header.
- body_image: `15052024_BassamBG_141414.png`, Drive fileId `1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR`,
  the on-brand near-black #141414 retouched portrait. Hosting: `needs-hosting` (Drive, stage to
  Ortto CDN or compose via Canva).
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: stage header to Ortto CDN`. The header (the real class cover) is verified
  servable on CloudFront only; CloudFront is not an approved email host. The earlier `yes` rested on
  `2_7.png`, which is not this class cover, so it is withdrawn.

### bassam-fattouh, Teaches Bridal Makeup

- slug: bassam-fattouh
- class: Bassam Fattouh, Teaches Bridal Makeup (design-style)
- header_image (EN page): `https://dt92b02v6m7lx.cloudfront.net/BFBRIDAL_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp`
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- header_image (AR page): `https://dt92b02v6m7lx.cloudfront.net/BFBRIDAL_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp`
  - source: in-page class cover (masterclass-pages.md), language-split
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- autopilot note: none. The `2_7.png` autopilot image is generic carousel art, not a bridal cover.
  Removed as a header source.
- body_image: bridal class has no studio portrait set; `_IMAGE-CATALOG.md` carries 64 bridal class
  stills under BANK OF STILLS (for example `250501_CH09_BRIDAL_.00_01_02_24.Still001.png`, fileId
  `1rB5d_qon2DNCn5AU0GXm1SeY1gczqK1H`). Hosting: `needs-hosting` (Drive). A studio portrait is
  preferable to a class still for a body image; flag.
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: stage header to Ortto CDN`. The header is verified servable on CloudFront
  only; no approved-host (Ortto) bridal header confirmed yet.

### ragheb-alama, Teaches Music and Performance

- slug: ragheb-alama
- class: Ragheb Alama, Teaches Music and Performance (music)
- header_image (EN and AR, language-neutral): `https://dt92b02v6m7lx.cloudfront.net/RA_CLASSCOVER_DESKTOP_01_NOGRADIENT.webp`
  - source: in-page class cover (masterclass-pages.md), NOGRADIENT serves both pages
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- autopilot note: none. No autopilot numbered image is a Ragheb header. Stage the CLASSCOVER to Ortto.
- body_image: `04032024_RaghebBG_141414.png`, Drive fileId `1zcOPrkscCaqYZbRfvu_uZH3RoeWbqL97`,
  on-brand #141414 portrait. Hosting: `needs-hosting` (Drive).
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: stage header to Ortto CDN`. Header verified servable on CloudFront only.

### salam-dakkak, Teaches Levantine Home Cooking

- slug: salam-dakkak
- class: Salam Dakkak, Teaches Levantine Home Cooking (cooking)
- class cover (intended): `https://dt92b02v6m7lx.cloudfront.net/dakak-cover.png`
  - status: `BLOCKED` (server-side fetch returned 403 AccessDenied, re-confirmed 2026-06-18). This
    cover does not resolve, the same failure mode as the og:image bug. It is DEAD.
- header_image (EN and AR, neutral): `https://dt92b02v6m7lx.cloudfront.net/SD_PLANS_BOTTOMGRADIENT.jpg`
  - status: `verified` (server-side fetch returned "cannot process image/jpeg", servable, 2026-06-18).
    This is the build's header, landscape (the right shape for a hero), serving both pages.
- FLAG (interim banner): `SD_PLANS_BOTTOMGRADIENT.jpg` is the plans-page image, not a dedicated
  class cover. It is an INTERIM banner used as Salam's header until a real Salam class cover is
  produced. The Drive portrait `11032024_SalamBG_141414` is the alternative cover source once
  hosted (note: that portrait is also the basis of Salam's other-classes grid card). Flag for Ahmed.
- autopilot note: the previously listed `3_6.png` is NOT this class header. It is generic carousel
  art (see the correction note). Removed as a header source.
- body_image: `11032024_SalamBG_141414.png`, Drive fileId `1jqvpgEQIjTbqwHIt-zw9TmmZr57v75qB`,
  on-brand #141414 portrait. Hosting: `needs-hosting` (Drive).
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `stage to Ortto before send` (the same as the other CloudFront covers, no longer
  fully BLOCKED). The header `SD_PLANS_BOTTOMGRADIENT.jpg` is verified servable on CloudFront only,
  which is the design proof and not an approved email host, so it stages to the Ortto CDN before
  send. Interim caveat: SD_PLANS is the plans-page image, not a dedicated class cover, until a real
  Salam class cover is produced. The intended cover dakak-cover.png is dead (403).

### kosai-khauli, Teaches Acting

- slug: kosai-khauli
- class: Kosai Khauli, Teaches Acting (acting)
- header_image (EN and AR, language-neutral): `https://dt92b02v6m7lx.cloudfront.net/02_240222_BEGINNINGS.00_03_55_10.Still001-02.webp`
  - source: in-page class cover (masterclass-pages.md), a text-free class still used as the page
    cover, serving both pages
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- autopilot note: the previously listed `1_7.png` is NOT this class header. It is generic carousel
  art (see the correction note). Removed as a header source.
- body_image: `04032024_KosaiBG_141414.png`, Drive fileId `1d8J0UPHnw7Z9ZZHYNSheo26ri_FtCCN9`,
  on-brand #141414 portrait. Hosting: `needs-hosting` (Drive).
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: stage header to Ortto CDN`. The class still header is verified servable on
  CloudFront only; CloudFront is not an approved email host. The earlier path rested on `1_7.png`,
  which is not this class cover, so it is withdrawn.

### rahma-riad, Teaches Building a Career in the Digital Age

- slug: rahma-riad
- class: Rahma Riad, Teaches Building a Career in the Digital Age (business)
- header_image (EN page): `https://dt92b02v6m7lx.cloudfront.net/RR_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp`
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- header_image (AR page): `https://dt92b02v6m7lx.cloudfront.net/RR_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp`
  - source: in-page class cover (masterclass-pages.md), language-split
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- autopilot note: none. No autopilot numbered image is a Rahma header. Stage the CLASSCOVER to Ortto.
- body_image: `18092024_RahmaBG_141414_IMG1.png`, Drive fileId `1-NgbV23l0tkPKL7zrNoiCvZjx7g5N6YH`,
  on-brand #141414 portrait. Hosting: `needs-hosting` (Drive).
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: stage header to Ortto CDN`. Header verified servable on CloudFront only.
  Note: Rahma is also `mined-thin` and the class existence itself is unconfirmed in
  `_CATALOG.md`; the catalog status check still gates the build.

### toufic-kredieh, Teaches Building and Growing Your Business

- slug: toufic-kredieh
- class: Toufic Kreidieh, Teaches Building and Growing Your Business (business)
- header_image (EN page): `https://dt92b02v6m7lx.cloudfront.net/TK_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp`
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- header_image (AR page): `https://dt92b02v6m7lx.cloudfront.net/TK_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp`
  - source: in-page class cover (masterclass-pages.md), language-split
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- autopilot note: the previously listed `توفيق كريدية.png` is NOT this class header. It is generic
  carousel art (see the correction note). Removed as a header source.
- body_image: `TouficBG_141414_3922.png`, Drive fileId `13qCpVNKKOYmGIkYPlFqW4tZayWlIfDKo`,
  on-brand #141414 portrait. Hosting: `needs-hosting` (Drive).
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: stage header to Ortto CDN`. The real class cover is verified servable on
  CloudFront only; CloudFront is not an approved email host. The earlier path rested on the autopilot
  named image, which is not this class cover, so it is withdrawn.

### cedric-haddad, Teaches Personal Styling

- slug: cedric-haddad
- class: Cedric Haddad, Teaches Personal Styling (design-style)
- header_image (EN page): `https://dt92b02v6m7lx.cloudfront.net/CH_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp`
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- header_image (AR page): `https://dt92b02v6m7lx.cloudfront.net/CH_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp`
  - source: in-page class cover (masterclass-pages.md), language-split
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- autopilot note: none. No autopilot numbered image is a Cedric header. Stage the CLASSCOVER to Ortto.
- body_image: no on-brand #141414 portrait set; best studio portrait is `Maharat-Cedric-173.jpg`,
  Drive fileId `16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX` (ROMARIO clean-retouched frame; the FACEAPP
  AI-edited twins are deliberately not catalogued). Hosting: `needs-hosting` (Drive).
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: stage header to Ortto CDN`. Header verified servable on CloudFront only.

### elda-choucair, Teaches Marketing

- slug: elda-choucair
- class: Elda Choucair, Teaches Marketing (business)
- header_image (EN page): `https://dt92b02v6m7lx.cloudfront.net/EC_CLASSCOVER_DESKTOP_01_EN-PAGE.webp`
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- header_image (AR page): `https://dt92b02v6m7lx.cloudfront.net/EC_CLASSCOVER_DESKTOP_01_AR-PAGE.webp`
  - source: in-page class cover (masterclass-pages.md), language-specific cover. The AR-PAGE cover
    is the one used in the Elda reference build.
  - status: `verified` (server-side fetch returned RIFF/WEBP image bytes, 2026-06-18)
- autopilot note: none. No autopilot numbered image is an Elda header. Stage the CLASSCOVERs to Ortto.
- body_image: no on-brand #141414 portrait set; best studio portrait is `C08-maharat-1038.jpg`,
  Drive fileId `1v5uTO-8RRyOgRB1EbfJa5aT6lSpPwdmw`. Hosting: `needs-hosting` (Drive).
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: stage header to Ortto CDN`. Both AR and EN headers are verified servable on
  CloudFront only. The existing Elda reference build (the ar2 file) already wires the AR-PAGE cover
  from CloudFront, so staging that one cover to Ortto unblocks the existing build.

### mona-ataya, Teaches Entrepreneurship

- slug: mona-ataya
- class: Mona Ataya, Teaches Entrepreneurship (entrepreneurship)
- header_image: `BLOCKED`. No `masterclass-pages.md` exists for Mona, so no in-page class cover URL
  was crawled or verified. `_CATALOG.md` records no launch evidence found in the pilot check.
- autopilot_fallback: none known.
- body_image: LOWRES jpg selects only (no retouched, no on-brand #141414 export); for example
  `maharat-1849.JPG`, Drive fileId `1_nBXBQxesxf8Iec0Jkvdgh-LIXD8o0vH`. Hosting: `needs-hosting`
  (Drive) AND quality flag: Mona has no retouched or on-brand portrait set (see `_IMAGE-CATALOG.md`
  open items), so a hero-grade body image does not yet exist. Flag for Ahmed.
- text_overlay: headline as a live copy slot over the text-free header, never baked.
- send_ready: `BLOCKED: no verified header`. No class cover captured and no approved-host image
  confirmed. Capturing Mona's class page cover (or staging an approved-host header) is the
  precondition before any Mona email build.

---

## Summary table

| slug | class | header (EN page / AR page) | header status | body image (Drive) | send_ready |
|---|---|---|---|---|---|
| bassam-fattouh | Makeup | BF_CLASSCOVER_LEFTRIGHTGRADIENT.JPG (neutral) | verified | 15052024_BassamBG_141414 (needs-hosting) | BLOCKED: stage to Ortto |
| bassam-fattouh | Bridal | BFBRIDAL_..._LEFTGRADIENT / RIGHTGRADIENT | verified | bridal class stills (needs-hosting) | BLOCKED: stage to Ortto |
| ragheb-alama | Music | RA_CLASSCOVER_..._NOGRADIENT (neutral) | verified | 04032024_RaghebBG_141414 (needs-hosting) | BLOCKED: stage to Ortto |
| salam-dakkak | Cooking | SD_PLANS_BOTTOMGRADIENT.jpg (interim banner; dakak-cover.png DEAD 403) | header verified (interim) | 11032024_SalamBG_141414 (needs-hosting) | stage to Ortto (interim banner) |
| kosai-khauli | Acting | 02_240222_BEGINNINGS...Still001-02.webp (neutral still) | verified | 04032024_KosaiBG_141414 (needs-hosting) | BLOCKED: stage to Ortto |
| rahma-riad | Digital career | RR_CLASSCOVER_..._LEFTGRADIENT / RIGHTGRADIENT | verified | 18092024_RahmaBG_141414_IMG1 (needs-hosting) | BLOCKED: stage to Ortto (and catalog status) |
| toufic-kredieh | Business | TK_CLASSCOVER_..._LEFTGRADIENT / RIGHTGRADIENT | verified | TouficBG_141414_3922 (needs-hosting) | BLOCKED: stage to Ortto |
| cedric-haddad | Styling | CH_CLASSCOVER_..._LEFTGRADIENT / RIGHTGRADIENT | verified | Maharat-Cedric-173 (needs-hosting) | BLOCKED: stage to Ortto |
| elda-choucair | Marketing | EC_CLASSCOVER_..._EN-PAGE / AR-PAGE | verified | C08-maharat-1038 (needs-hosting) | BLOCKED: stage to Ortto |
| mona-ataya | Entrepreneurship | none captured | BLOCKED | maharat-1849 LOWRES (needs-hosting, no hero-grade) | BLOCKED: no verified header |

Covers verified servable at source (CloudFront, 2026-06-18): 9 classes counting salam's interim
SD_PLANS banner (13 URLs counting the EN/AR language splits). The intended salam cover
dakak-cover.png is dead (403); the build uses the verified SD_PLANS_BOTTOMGRADIENT.jpg as an
interim banner (the plans-page image, not a dedicated class cover) and salam still needs a real
class cover produced. No cover captured: mona. The autopilot numbered images (1_7, 2_7, 3_6, named
Toufic) are generic carousel art, NOT headers, and are removed as header sources; only the Maharat
logo on m.autopilotapp.com remains a verified approved-host asset.

Send-ready today: NONE on an approved host. Every correct header is a CloudFront class cover
awaiting Ortto staging (CloudFront is not an approved email host). The old "yes" for bassam-fattouh
Makeup is withdrawn (it rested on `2_7.png`, which is not the class cover).
Header verified, needs Ortto staging (9): bassam-makeup, bassam-bridal, ragheb-alama, rahma-riad,
cedric-haddad, elda-choucair, toufic-kredieh, kosai-khauli, and salam-dakkak (the last on the
interim SD_PLANS banner; salam still needs a real dedicated class cover produced, dakak-cover.png is
dead). No verified header at all (1): mona-ataya.

All body images are Drive ids and are `needs-hosting`: none is email-ready until staged to the Ortto
CDN or composed and hosted via Canva. Mona additionally has no hero-grade (retouched or on-brand)
portrait.
