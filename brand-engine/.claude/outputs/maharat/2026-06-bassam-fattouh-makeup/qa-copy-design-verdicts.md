# QA verdicts: copy and design gates

campaign_id: 2026-06-bassam-fattouh-makeup. Verifier records, not authored content. Brand and
compliance verdicts are separate files (brand-qa-verdict.md, compliance-verdict.md). No em
dashes. Western numerals.

## arabic-copy-qa: PASS (after 1 round of fixes)

Scope: AR copy in 01-emails, 02-social-posts, 03-paid-ads, 04-app-notifications.

First pass failed on 2 dialect-drift items. Both fixed by the author and resubmitted:

| check | span (before) | fix applied |
|---|---|---|
| msa-gulf-familiar | "وشوف الفرق بنفسك" (E1) | changed to "واكتشف الفرق بنفسك" |
| msa-gulf-familiar | "خلّ مهارتك القادمة تبدأ من الآن" (social P8) | changed to "دع مهارتك القادمة تبدأ الآن" |

Re-run: all 7 checks pass (msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals,
no-em-dash, empowering-framing, rtl-safe). Verified mechanically: zero em dashes, zero tatweel,
zero Eastern Arabic numerals across the folder.

Advisory (not a gate check, surfaced for the human gate): the campaign mixes masculine and
feminine address across pieces (for example E1 masculine, E2 and social P6 feminine). Beauty
audience skews feminine. Decide one consistent stance or an intentional per-segment split.

## english-copy-qa: PASS

Scope: EN copy in the same four files. All 7 checks pass:
- empowering-tone: pass, empowering and plain, no deficit framing or hype.
- no-em-dash: pass.
- western-numerals: pass.
- one-clear-cta: pass, one primary CTA per email, ad, and push.
- no-accreditation-implication: pass, none present.
- no-invented-offers-titles: pass. Instructor named only via the public course page. No price
  stated. No invented lineup. Title is the working title from the supplied URL, flagged as an
  open item to confirm against the live page.
- plain-active-voice: pass.

## design-qa: PASS (spec-level)

Scope: 05-visual-briefs.md and the creative refs in 02 and 03. These are briefs, not rendered
assets. All 6 checks pass at spec level:
- rtl-correct: pass, briefs mandate RTL-correct AR overlays.
- visual-constants: pass, #141414, #1A1A1A, #009975, accent as a highlight.
- western-numerals-rendered: pass.
- no-baked-arabic-text: pass, headlines are build-time overlay slots, never baked in.
- safe-areas-dimensions: pass, formats and safe areas declared per asset.
- premium-uncluttered: pass.

Plus the instructor-likeness rule is explicitly handled: any Bassam Fattouh portrait or class
footage must be a real rights-cleared Maharat asset, never generated.

Standing requirement: rendered assets must re-pass design-qa and a human design check before
publish. If approved Bassam Fattouh imagery and the trailer are not available, asset V1 and the
YouTube trailer are blocked and the campaign leans on V2 and V3. This is an open item.
