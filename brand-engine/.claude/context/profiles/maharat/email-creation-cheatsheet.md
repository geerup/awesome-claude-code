# Email creation cheatsheet

The one-stop, practical reference for building and shipping a Maharat instructor email, with
the gotchas we hit baked in so the next build is fast and clean. The deep specs are
`context/email-design-system.md` (visual standard), `runtime/email-module-map.md` (the slot
contract), `context/instructors/_EMAIL-IMAGE-MANIFEST.md` (headers), and
`outputs/_EMAIL-SET-TARGETING-PLAN.md` (sends). No em dashes, Western numerals.

## The one canonical build system

There is one email build system, and this is its map. The spec-driven slotted renderer
(`scripts/email_render.py`, reading a campaign `spec.json` into the `data-ortto-module` /
`data-slot` / `data-role` / `data-lang` / `data-copy-id` contract, gated by the stack below,
output under `outputs/<campaign>/`) is it. A second, config-driven generator once lived in
`runtime/email-build/` (a `generate.py` fed by `brand.json` plus per-instructor and per-campaign
JSON). It was retired in the de-dup: it emitted the same slot contract but without the
`data-copy-id` QA binding the module map requires, and its instructor configs still carried the
broken og:image hero this cheatsheet warns against. Its one durable asset, the Ortto draft-push
runbook, is folded into the Ortto section below. A config-driven front-end that emits a `spec.json`
for `email_render.py` is a fine future convenience, but it stays one renderer, not two.

Per-instructor image source-of-record is three coordinated files, not duplicates:
`_EMAIL-IMAGE-MANIFEST.md` is the build registry (which verified-servable header fills which slot,
gate-zero), `<slug>/photos.md` is the email-ready CDN index plus the historical-send mapping
(`editor_image` UUIDs to the archive), and `<slug>/assets.md` is the Drive high-res portrait masters
for design pulls. The archive of real past sends lives in `references/ortto-email-archive/`, with its
45-email audit and copy export in `references/`.

## Build a campaign in four steps

1. Write the spec: `outputs/<campaign>/email-7step/<slug>/spec.json` (or `email-html/emails.spec.json`).
   Each email carries subject, preheader, headline, body, one cta, and per-slot copy. Header goes
   in `hero_image`, the bottom row in `class_cards`.
2. Render: `python3 .claude/scripts/email_render.py <spec.json>`. Stdlib only, campaign-agnostic.
   The committed HTML is the source of truth; the MJML library compiles to match it.
3. Sweep: `python3 .claude/scripts/house_style_sweep.py <files>`. Must be clean.
4. Gates, in order: `email-html-build` eval, then `arabic-copy-qa` or `english-copy-qa` per slot by
   `data-lang`, then `email-asset-qa` on every image module, then `accessibility-qa`, then
   `compliance-privacy-check`, then `brand-qa-reviewer`, then the human gate. Nothing sends on its own.

## Format rules (quick)

- Colors: paper `#141414`, panel `#1A1A1A`, emerald `#009975` only. NO gold `#C4963C`, NO `#1c1c1c`
  (both pending Ahmed). Ortto's brand book has drift (`#1b1b1b` bg, `#008970` button): use the
  constitution values, not the brand book.
- Fonts via Ortto-hosted CSS: Lyon Arabic Display + 29LT Azer (AR), Acumin Pro (EN). Lyon and Acumin
  are already on Ortto; 29LT Azer is NOT uploaded yet, so AR body falls back to Tahoma until it is.
- `dir="rtl"` for AR, `ltr` for EN. One primary CTA per email: near-black `#141414` label on emerald
  (about 5:1 AA, never white on emerald), MSO VML roundrect plus a non-mso pill.
- Live text, never image-only. No Arabic baked into any image. Sender identity and unsubscribe in
  every email. No em dash, no tatweel, Western numerals.
- Footer sender (the real PO box): "Maharat for Education, P.O Box 77983, Abu Dhabi, United Arab
  Emirates" / "مهارات للتعليم، ص.ب 77983، أبوظبي، الإمارات العربية المتحدة". Unsubscribe and
  view-in-browser are handled by Ortto: unsubscribe is the merge tag `{{ urls.unsubscribe }}` (verified
against the archived sends, and the token `update_asset_mail` validates), and Maharat sends carry no
view-in-browser link, so none is emitted.

## Images (this is where the time went)

- HEADER is gate-zero: no email HTML without a verified-servable header. The header is the real
  class cover, language-matched: `LEFTGRADIENT` / `EN-PAGE` = English page, `RIGHTGRADIENT` /
  `AR-PAGE` = Arabic page; a `NOGRADIENT` or `LEFTRIGHTGRADIENT` neutral cover serves both.
- DO NOT use the og:image variant (`*_CLASS_PAGE_*`, `*_RIGHTGRADIENT.JPG` as the page og:image). It
  returns 403 and renders as broken alt text. That was a real bug.
- The "our other classes" bottom row is PORTRAIT cards: the text-free `*_HOMEPORTRAIT_BOTTOMGRADIENT`
  or `*_BG_141414-BOTTOM-GRADIENT` portrait as a standard image with the instructor name and
  "Teaches X" as a LIVE HTML caption beneath it (a plain img plus live text, no background image and
  no VML), language-matched, three OTHER classes, never the email's own. The overlay-on-background
  technique was dropped because Ortto's BeeFree editor discards the card background image on import,
  collapsing the cards to text; a standard img plus caption survives the editor and the send.
- The autopilot numbered images (`1_7.png`, `2_7.png`, `3_6.png`) are NOT per-instructor covers, they
  are generic carousel art (`2_7.png` is the multi-instructor "مواجهة التحديات" cover). Do not use
  them as headers. Use the real class covers from `masterclass-pages.md` / the manifest.
- Hosts: the Ortto CDN (`m.autopilotapp.com`, `ic.autopilotapp.com`) and getbee (social icons) are
  the approved hosts. CloudFront class covers render but are not an approved email host (stage to
  Ortto before send). Google Drive links are NOT hot-linkable in email. The repo is private, so its
  raw GitHub URLs do not render in an inbox either.
- Always VERIFY a candidate image is servable before using it: a server-side fetch that errors
  "cannot process image/*" or returns image bytes (JFIF, EXIF, RIFF/WEBP, PNG) is servable; a 403,
  404, or `<Error>AccessDenied` is not. The manifest records the verified header per instructor.
- This sandbox cannot download images (egress is locked) and cannot upload to Ortto via the MCP.
  Cover bytes are fetched where the network is open; Drive bytes via the Drive MCP; Ortto-CDN
  hosting is a drag-drop in Ortto's Asset Library (the MCP has no image-upload tool).

## Claims and status

- Only page-cleared facts plus `voice.md` verified-safe beliefs. Held-back claims stay out (for
  example Elda's Omnicom or Forbes figures), every credibility line traces to a published tagline.
- Instructor public status is `unconfirmed` in `_CATALOG.md` for the whole roster (strong launch
  evidence, but the flip is Ahmed's explicit call). This is the standing brand-qa send block.

## Ortto: what works and what bites (the integration learnings)

- The Ortto MCP (`mcp__Claude__*`) READS the account and DRAFTS assets. It cannot send and cannot
  delete (by design), and exposes no image-upload tool. Sending is a human action in Ortto.
- `get_brand_book` confirmed the account (US region, Lyon and Acumin uploaded). Arabic survives
  Ortto: the render test preserved RTL, fonts, and Western numerals.
- `create_asset` runs the HTML through BeeFree (HTML to JSON): it MUTATES the HTML (not byte-faithful)
  and TIMES OUT at about 60s on large slotted emails; VML-heavy card HTML can return a 500. So if you
  push: ONE email at a time, verify with `list_assets` after a timeout (the create often committed
  server-side anyway), accept BeeFree normalization. Do NOT fan out parallel push agents, they spawn
  sub-agents and clutter the account, and there is no delete to clean up.
- Pushing a draft (the proven runbook): `create_asset(name, subject, mail_html)` one email at a time,
  name it `[INTERNAL DRAFT] ...` so it is never mistaken for a live campaign, then verify the first
  with `get_asset_html` before pushing the rest. Bee guesses image heights at import (width and
  `height:auto` still render) and can split a heading row into a heading plus a spacer, neither
  blocking. `update_asset_meta` REPLACES the whole meta set, it does not merge: always pass `subject`,
  `preview_text` (the preheader), `from_name`, and `from_email` together, or the omitted ones clear.
  A draft is not a send and not a spend, so it sits inside the read-plus-draft scope. (Proven
  2026-06-16: Bassam msg-1 EN as draft `6a3156d8e42f559c4fa00950`.)
- The committed HTML stays the source of truth; Ortto drafts are a derived, editable copy.

## Targeting and sends (it all lives in Ortto)

- Primary non-payer audience: `Created Account - NonPaying`, about 13,281 emailable (the brief's
  18,000 was an over-estimate). Suppress payers (`bol:cm:paying = true`), Unsubscribed (3,891),
  Bounced (4,992), Internal Team, BOT, Test.
- Per instructor: `str:cm:classid`, or the per-instructor "Not Paid - <Instructor>" segments (the
  `Not Paid - Rahma` audience is the precedent). AR vs EN: `str::language`. Geo: `geo::country`.
- The 7-step is an Ortto journey: entry on the per-class non-payer segment, E1 on entry, E2 to E7 on
  a 2 to 3 day cadence with open and click branches, exit when `bol:cm:paying` flips true, a
  failed-payment branch on `bol:cm:hasfailedpayment`. Conversion is the `paying` transition, read via
  `get_email_report`. Full detail in `outputs/_EMAIL-SET-TARGETING-PLAN.md`.

## Standing open items before any live send

Ortto adoption (region or Saudi PDPL call, scoped key, settings.json allowlist), the roster public
status confirmation, the image staging to the Ortto CDN, and the per-class `classId` values. The
human gate signs off per action and per campaign, inside Ortto.
