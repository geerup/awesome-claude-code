---
name: email-asset-qa
description: The asset and visual quality gate for built emails, used by the email-asset-reviewer agent. Use to check every image module in an email build against the assets mandate before it advances, triggers on "asset check," "email image QA," "are these images rights-cleared," "is the hero CDN-hosted," "check the email visuals." Verifies rights clearance, approved Ortto-CDN hosting (not raw Drive or hotlink-protected CloudFront), text-free pixels, brand constants, dimensions and safe area, descriptive alt, and instructor catalog status and claims discipline, returning pass or a structured fix list.
---

# Email Asset QA (the asset and visual gate)

The asset and visual quality gate, used by the `email-asset-reviewer` agent. Runs on the image
modules of a built email: every cell marked `data-slot="element"`, the LogoBar, the Hero, any
FeatureImage, the ClassCardGrid covers, and the Footer social icons. A verifier, not an author:
it never edits the build, it returns pass, or fail with an exact fix list. The author regenerates
against the list and resubmits to this same gate.

## Purpose

Catch asset defects before the build advances toward brand QA and the human gate: an image that
is not rights-cleared, an `img src` hot-linked from Google Drive or a hotlink-protected CloudFront
object (a direct fetch can return 403), a cover with baked Arabic text, a color off the brand
constants, a wrong dimension or unsafe crop, a missing or filename `alt`, or an unconfirmed
instructor likeness. The brand palette, the CDN rule, and the no-baked-Arabic rule are fixed, so
this gate verifies the asset meets them, and fixes the asset or its hosting, never the rule.

## When to use

- Stream 7 lifecycle: every image module in an email build, after the language copy gates and
  alongside `accessibility-qa`, before `brand-qa-reviewer` and the human gate.
- Any built email with one or more `data-slot="element"` cells before it advances.

## Inputs

- The build under review: the slotted email HTML, or the spec and asset list for one.
- `context/profiles/maharat/email-design-system.md`: the visual constants, dimensions, and the assets mandate.
- `runtime/email-module-map.md`: which modules carry `element` slots and the approved-CDN rule.
- `context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md`: the source of truth for the verified-servable
  header per instructor and class, and which host it is approved on.
- `context/profiles/maharat/instructors/_EMAIL-ASSET-PIPELINE.md` and `email-asset-pipeline.json`: the GitHub-to-Ortto
  pipeline map is the source of truth for the serve URL per image; any status other than `served`
  (`pending-fetch`, `fetched`, `pending-ortto`, `blocked`) is a send-blocking state.
- `context/brand-voice.md` and `context/profiles/maharat/instructor-packs`: the palette and the instructor
  catalog status check.

## The checks

Run each on every `data-slot="element"` cell. Report every failing item, not just the first.
Check 0 runs first on the build as a whole, before the per-cell checks: it is gate-zero.

0. header-image-present-and-servable (HARD, blocks): the build has a hero or header image module,
   and its `src` is a verified-servable header on an approved host. Verify against
   `context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md`: the `src` matches that instructor and class's
   verified header (status `verified`), on an approved Ortto host (`m.autopilotapp.com`,
   `ic.autopilotapp.com`), or proven by an inbox send-test. Fail and block when the build has no
   hero or header image module at all, when the header `src` is the og:image variant
   (`*_CLASS_PAGE_*` / `*_RIGHTGRADIENT.JPG`, which 403s), when the header is not the manifest's
   verified header for that instructor and class, when the header status in the manifest is
   `pending` or `BLOCKED`, or when the header `src` is on a non-approved host (a raw CloudFront
   `dt92b02v6m7lx.cloudfront.net` object is verified-at-source but is not an approved email host;
   it must be staged to Ortto or send-tested first). A build that fails check 0 does not advance:
   the header is the precondition for the email build. This is the same finding as the Bassam fix
   in commit 6bf87a4 (the in-page CLASSCOVER is the header, never the og:image).
1. rights-cleared: every image is a real, rights-cleared Maharat asset, traceable to the catalog,
   the image map, or a published page. Fail on a generated portrait, stock, or unlicensed image.
2. approved-cdn-hosting: every `img src` (and any VML background `src`) is on the approved Ortto
   CDN (`m.autopilotapp.com`, `ic.autopilotapp.com`, `app-rsrc.getbee.io` for social icons). Fail
   on a raw Google Drive link or a hotlink-protected CloudFront object (for example
   `dt92b02v6m7lx.cloudfront.net`); the fix stages the bytes to the CDN or proves render with an
   inbox send-test. Note the documented 403 finding for the Bassam class cover.
3. text-free: no Arabic or English text is baked into any image. Fail on a cover with a baked
   title; the headline is a live copy slot over a text-free background.
4. brand-constants: any brand color in the asset matches the constitution (`#141414`, `#1A1A1A`,
   `#009975`). Fail on the pending gold `#C4963C` or panel `#1c1c1c` in a customer-facing asset
   until Ahmed signs off.
5. dimensions-and-safe-area: each module is the right width and aspect for its slot (Hero and
   FeatureImage 600 wide, ClassCardGrid a consistent 3-up, LogoBar about 118px, social icons
   about 28 to 30px), the subject inside a safe area. Fail on a wrong size or an unsafe crop.
6. descriptive-alt: every meaningful image carries real, descriptive `alt` text (Arabic for an
   Arabic build), never empty on a meaningful image, never the filename. Decorative spacers are
   marked decorative. Fail on a missing, empty, or filename `alt` for a meaningful image.
7. instructor-status-and-claims: any image picturing or naming an instructor is blocked until the
   catalog status is confirmed (`context/profiles/maharat/instructor-packs`), and carries only page-cleared,
   rights-cleared creative. Fail on an unconfirmed likeness or a held-back claim in the pixels or
   the alt text.

## Steps

1. Run check 0 first on the build as a whole: confirm a hero or header image module exists and its
   `src` is the manifest's verified header on an approved host. If check 0 fails, the build is
   blocked, return it now (the header is gate-zero, the rest of the review is moot without it).
2. Enumerate every `data-slot="element"` cell in the build (and any VML background `src`).
3. Run each remaining check against each one. For each failing check, capture the offending
   module, named by its `src` and role.
4. Decide the result: pass only when check 0 passes and every check passes on every module,
   otherwise fail. A spec-only review (no hosted asset yet) blocks final pass on the
   host-and-render checks (approved-cdn-hosting, the inbox send-test), flagged as open items.
5. Return the result in the shape below. Never edit the build.

## Output

- Pass: the build advances to `accessibility-qa` and `brand-qa-reviewer` (alongside
  `compliance-privacy-check`), then the human gate.
- Fail: a structured fix list, one item per failure:

```
{ check: <the failing check id>, element: "<the offending image module, src and role>", fix: "<the required change>" }
```

Example: `{ check: "text-free", element: "Hero, BF class cover with baked title", fix: "host a text-free variant and set the headline as a live copy slot over it" }`.

See `templates/email-asset-qa-fix-list.md`.

## Hard rules

- Never edit the build. Verify and route only.
- Header image is gate-zero. A build with no hero or header image module, or whose header `src` is
  not a verified-servable approved-host URL per `context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md`, is a
  hard fail that blocks. The manifest is the source of truth for verified headers. Never pass the
  og:image variant (`*_CLASS_PAGE_*` / `*_RIGHTGRADIENT.JPG`) as a header.
- Binary: pass and advance, or fail and return. No soft warnings that pass through.
- Never accept a raw Drive link or a hotlink-protected CloudFront object as an email `img src`,
  never accept baked Arabic, never adopt the pending gold or off-panel color, and never pass an
  unconfirmed instructor likeness. Fix the asset or its hosting, or escalate to `brand-qa-reviewer`
  and the human gate.
- A spec-only review blocks on the checks that need the hosted asset: approved-cdn-hosting and the
  inbox send-test.
- Email images come from the approved Ortto CDN. Passing the asset gate is not approval to send.
- No em dashes, no en dashes, no tatweel, Western numerals only, in this file and the fix list.

## How it connects

- Runs in the email gate stack after the language copy gates (`arabic-copy-qa`, `english-copy-qa`)
  and alongside `accessibility-qa`, before `brand-qa-reviewer`, per `runtime/verification.md` and
  `runtime/email-module-map.md`. On pass, the build advances, on fail it returns to the author
  (lifecycle-architect for the email, designer for the visual) with the fix list.
- Owned by the `email-asset-reviewer` agent.
