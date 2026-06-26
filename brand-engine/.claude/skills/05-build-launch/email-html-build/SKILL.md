---
name: email-html-build
description: Assemble QA-passed copy and asset-QA-passed images into the slotted, brand-correct email HTML for stream 5, assembled and never sent. Use when an approved lifecycle flow and its copy must become live-component email builds on the Maharat email standard, triggers on "build the email HTML," "assemble the email," "slotted email build," "rebuild the emails to the standard," "live components email." Sub-skill of 05-build-launch, owned by paid-build-engineer plus designer, execution mode and gated.
---

# Email HTML Build (stream 5 sub-skill)

Assembles QA-passed copy (bound by `data-copy-id`) and `email-asset-qa`-passed images into the
slotted component HTML defined by the two anchor docs: `context/profiles/maharat/email-design-system.md` (the
visual standard, the 12+1 core component library plus the 3 multi-instructor digest modules, the
tokens, the themes) and `runtime/email-module-map.md` (the slot, role, lang, and copy-id contract,
and the gate routing).
The output is one self-contained, RTL-correct, brand-correct email per language, built from live
modules, never a flat image. It is assembled, never sent. Going live is a human-gate decision.

To assemble a fresh mockup from an archetype (multi-instructor-digest, occasion-promo,
personal-voice-launch, meet-the-instructor, gifting, single-class), use the `/email-mockup` command
(`commands/email-mockup.md`): it composes from these same blocks and the slot contract, renders via
`scripts/email_render.py`, and stops at the gate stack. A worked example is in
`examples/multi-instructor-digest/`.

Owner: paid-build-engineer (assembly) plus designer (the visual and component decisions). Mode:
execution (gated).

## The one rule everything serves

Every line of copy is a live HTML text slot bound to a QA-passed `copy-package` variant by
`data-copy-id` and tagged `data-lang`. Every image is text-free, `data-slot="element"`, with
descriptive `alt`. An image-only send (copy baked into a picture) is a hard fail. See
`runtime/email-module-map.md`.

## Precondition: header image first (gate-zero)

No email HTML is generated for an instructor until `context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md`
provides a verified header image for that instructor and class. The order is fixed:
header-image-first, then build, then gate review, then regenerate on feedback. A build started
without a verified header is wrong by construction: `email-asset-qa` blocks it at check 0
(header-image-present-and-servable). The header `src` must be the manifest's verified header on an
approved Ortto host, never the og:image variant (`*_CLASS_PAGE_*` / `*_RIGHTGRADIENT.JPG`, which
403s and renders as broken alt text). A raw `dt92b02v6m7lx.cloudfront.net` cover is verified at
source but is not an approved email host: stage it to the Ortto CDN or prove it with an inbox
send-test before the build. If the manifest header status is `pending` or `BLOCKED`, stop and
resolve the header before building.

## When to use

- A QA-passed `lifecycle-package` (stream 7) and `copy-package` (stream 4) need to become the
  slotted email HTML on the Maharat email standard.
- The simplistic image-or-flat emails of an earlier build must be rebuilt as live components.

## Inputs

- The QA-passed `copy-package`: every variant by id, the routing key being `data-copy-id`. Copy is
  never written into the template by hand.
- The `email-asset-qa`-passed assets: every image module hosted on the approved Ortto CDN,
  text-free, rights-cleared, with its `alt`.
- `context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md`: the verified header image for the instructor and
  class. The header is the precondition (gate-zero); without a `verified` header on an approved
  host, the build does not start.
- The two anchor docs: `context/profiles/maharat/email-design-system.md` and `runtime/email-module-map.md`.
- The active `briefs/` file and the lifecycle flow: which email sits where, the CTA destination,
  the theme (dark default, light for transactional and lifecycle only).

If any copy slot's `data-copy-id` is not QA-passed, or any image is not `email-asset-qa`-passed,
the build does not proceed on it. Return it to its gate.

## What it assembles: the component library, slotted

A built email composes from the 12+1 core components in `context/profiles/maharat/email-design-system.md`, plus the
3 multi-instructor digest modules for a multi-instructor or catalog email, each carrying the slot
attributes from `runtime/email-module-map.md`
(`data-ortto-module`, `data-slot`, `data-role`, `data-lang`, `data-copy-id`, `data-link-slot`):

- LogoBar (image element), Hero (image element, text-free; any headline is a live slot over it),
  SectionHeading (eyebrow + headline copy slots), BodyCopy (copy slot), the single Button (copy
  slot label + `data-link-slot`), PromoLine, Divider (structural), ListBlock (copy slot),
  ClassCardGrid (image elements, status-cleared instructors only or omit), FeatureImage,
  EventDetails (copy slot), BillingNotice (copy slot), Footer (social icon elements + structural
  www, sender identity, unsubscribe).
- The multi-instructor digest modules (the extension set, used only for the multi-instructor
  format): LessonCardGrid (the in-body offer grid, per card a text-free portrait element plus
  `card-headline`, `card-credential`, and a quiet `card-cta` secondary link), IssueIndex (a
  numbered "in this issue" copy slot), and MemberWin (a real, consented testimonial copy slot that
  leads into the single Button). The angle method is `context/profiles/maharat/multi-instructor-angles.md`; a
  named instructor's card is dropped unless catalog-status-confirmed and page-cleared.

Build rules carried into every email:
- Brand fonts via the Ortto-hosted custom-fonts CSS in the head, the ar2 reference pattern:
  `Lyon Arabic Display` and `Acumin Pro` linked from
  `accounts-api-us.ortto.app/-/settings/custom-fonts.css`. Arabic stack
  `'Lyon Arabic Display','29LT Azer',Tahoma,Arial,sans-serif`, English `'Acumin Pro',Arial,sans-serif`.
  No font binary is embedded or committed.
- Brand constants only: paper `#141414`, panel `#1A1A1A`, emerald `#009975`. The pending gold
  `#C4963C` and panel `#1c1c1c` stay out of customer-facing email until Ahmed signs off.
- One primary CTA per email, an MSO VML roundrect for Outlook plus a non-mso pill, label near-black
  `#141414` on emerald (about 5:1, clears WCAG AA), never white on emerald at normal weight.
- `dir="rtl"` for Arabic, `dir="ltr"` for English. Dark theme is the marketing default.
- Sender identity and an unsubscribe link in every email; the unsubscribe href is the platform
  merge tag wired at send.

## Steps

1. Confirm the header first (gate-zero). Look up the instructor and class in
   `context/profiles/maharat/instructors/_EMAIL-IMAGE-MANIFEST.md` and confirm a `verified` header on an approved
   Ortto host. If the header is `pending` or `BLOCKED`, stop and resolve it before building. No
   header, no build.
2. Validate both package envelopes: right campaign_id, status at least qa-passed, required fields
   present. If incomplete, return.
3. Lay out the email from the component library per the flow's job for this message. One primary
   CTA. Theme by send type (dark default).
4. Place the header first, from the manifest's verified header on the approved Ortto host, as the
   Hero `data-slot="element"` with descriptive `alt`. Text-free; any headline is a live copy slot
   over it.
5. Bind every copy slot to its `data-copy-id` and set `data-lang`. No free copy is written here.
   Mirror the approved copy text exactly.
6. Place every other image module as `data-slot="element"` with its approved-CDN `src` and
   descriptive `alt`. Text-free only. The ClassCardGrid carries status-cleared instructors with
   rights-cleared covers, or it is omitted and flagged.
7. Wire the CTA `data-link-slot` to the confirmed destination, no personal or sensitive data in
   the URL. Add the MSO VML fallback.
8. Run the house-style sweep on the built HTML. Hand the assembled build to the gate stack below.
   The build is assembled, not sending.

## The gate order (every built email)

The build is one asset with many slots. The gates run per `runtime/verification.md`, routed by
slot, and stop at the first failure:

1. Skill eval: this skill's `evals/evals.json` (structure, every copy slot bound to a
   `data-copy-id`, one primary `cta`, slot attributes well formed, brand fonts via Ortto CSS,
   brand constants only, house-style sweep clean).
2. Language copy QA, per copy slot by `data-lang`: `arabic-copy-qa` for Arabic slots,
   `english-copy-qa` for English slots. A copy slot whose `data-copy-id` is not QA-passed blocks
   the build.
3. Asset and visual QA: `email-asset-qa` on every `data-slot="element"` image module.
4. Accessibility QA: `accessibility-qa` on the email render.
5. Compliance and privacy: `compliance-privacy-check` on the send, suppression, links, unsubscribe.
6. Brand QA: `brand-qa-reviewer`, last, on the whole assembled email.
7. Human gate: nothing sends without Ahmed, per action and per campaign.

## Output

The slotted email HTML (one self-contained file per email per language), plus the build spec
(`emails.spec.json` or equivalent), an `index.html` preview sheet, and a README that states the
source of truth, the asset and CDN caveats, and the open items. Wrapped in the common envelope
(campaign_id, produced_by, stream, status, qa, open_items, brief_refs). See `templates/` and
`runtime/handoff-contract.md`.

## Build path: MJML or hand-built, same slotted output

Authored in MJML (the component library under `mjml/`) and compiled to the Ortto-slotted table
HTML, or hand-built to the same slotted output. Either path produces the same module map and
passes the same gates. The committed slotted HTML is the source of truth; `npx mjml` compiles the
MJML to match it. See `mjml/README.md`. MJML is a local compiler, an approved build dependency
(Ahmed approved 2026-06-17), not an MCP server, so it is not in `settings.json`.

## Hard rules

- Assembled, not sent. The build never sends and never schedules a live send on its own.
- Live text, never image-only. Every word is a live copy slot bound to a `data-copy-id`; every
  image is text-free with descriptive alt. Copy is never invented or rewritten here.
- Brand constants only (`#141414`, `#1A1A1A`, `#009975`); the gold and off-panel are pending and
  stay out. Brand fonts only (Lyon Arabic Display, 29LT Azer, Acumin Pro), via the Ortto CSS, no
  binary committed.
- One primary CTA per email (MSO VML + non-mso pill), near-black label on emerald for AA. Sender
  identity and unsubscribe in every email. No personal or sensitive data in any link.
- A copy slot not QA-passed, or an image not `email-asset-qa`-passed, blocks the build. Never
  imply accreditation.
- No em dashes, no en dashes, no tatweel, Western numerals only, swept on every built file.

## How it connects

Consumes the `copy-package` (stream 4) by `data-copy-id` and the `email-asset-qa`-passed assets,
produces the slotted build for the gate stack above, and hands the assembled, not-sending package
to the human gate. The lifecycle-architect designs the flow; this skill builds the HTML for it.
