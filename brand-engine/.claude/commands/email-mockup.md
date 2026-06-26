---
description: Build an approval-ready, slotted HTML email mockup from the engine's primitives, blocks, templates, Ortto section ids, and rules. Pick an archetype (multi-instructor-digest, occasion-promo, personal-voice-launch, meet-the-instructor, gifting, single-class), fill slots from QA-passed copy or clearly-marked MOCK placeholders, render, sweep, and run the build eval. Nothing sends. Usage - /email-mockup <archetype> [campaign-id-or-mock]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3 .claude/scripts/email_render.py:*), Bash(python3 .claude/scripts/house_style_sweep.py:*), Bash(python3 .claude/scripts/eval_runner.py:*)
---

# /email-mockup

Build one slotted, brand-correct, RTL-correct HTML email mockup for the archetype named in
"$ARGUMENTS", composed from the engine's primitives and blocks, laid out by a template, tagged
with the Ortto section ids, and held to the rules. The output is an approval-ready mockup: it is
assembled and rendered, it is never sent. Going live is a human-gate decision and a separate
staging step.

This command does not invent copy, offers, prices, Skill Path titles, or instructors. It renders
QA-passed copy when a campaign supplies it, or clearly-labeled MOCK placeholders when the run is a
structural mockup. A mockup is labeled MOCKUP and INTERNAL DRAFT and never presented as real.

Load first: `CLAUDE.md`, `context/brand-voice.md`, `context/profiles/maharat/email-design-system.md` (primitives and
blocks), `runtime/email-module-map.md` (the slot contract and Ortto section ids),
`context/profiles/maharat/multi-instructor-angles.md` (the angle for multi-instructor archetypes),
`skills/04-copywriting/email-copy/templates/newsletter-patterns.md` (the single-instructor launch
shapes), `skills/07-lifecycle-messaging/templates/sequence-standards.md` (the promo ladder),
`skills/05-build-launch/email-html-build/SKILL.md` and `templates/email-html-structure.md`, and
`context/profiles/maharat/email-creation-cheatsheet.md` (the build and Ortto runbook). The renderer is
`scripts/email_render.py`.

## The one rule everything serves

Every line of copy is a live HTML text slot bound to a `data-copy-id`. Every image is text-free
with descriptive alt. No Arabic baked into any image. One primary CTA per email. Sender identity
and unsubscribe in every email. An image-only send is a hard fail. See `runtime/email-module-map.md`.

## Layer 1: primitives (tokens, from email-design-system.md, do not redefine)

- Color: paper `#141414`, panel `#1A1A1A`, emerald `#009975` (one accent), text `#FFFFFF` /
  `#E6E6E6` / `#9A9A9A`. Light theme for transactional only. The gold `#C4963C` and `#1c1c1c` stay
  out (pending Ahmed).
- Type scale: H1 28, H2 22, Sub 18, Body 15, Footer 13, Fine 12. Arabic line height about 1.7.
- Shape: width 600, side padding 24, card radius 16, small card 12, CTA pill radius 28. RTL default.
- Fonts via the Ortto custom-fonts CSS: Lyon Arabic Display and 29LT Azer (AR), Acumin Pro (EN).
- CTA pill: near-black `#141414` label on emerald (about 5:1, clears AA), MSO VML plus a non-mso pill.

## Layer 2: blocks and their Ortto section ids

Each block maps to one Ortto module via `data-ortto-module`, carries a `data-slot`, and routes to a
gate. This is the contract that makes the mockup Ortto-editable and gate-traceable.

| Block | data-ortto-module | data-slot | data-role | gate |
|---|---|---|---|---|
| LogoBar | image | element | (none) | email-asset-qa |
| Hero | image | element | (none, text-free) | email-asset-qa |
| SectionHeading | heading / text | copy | eyebrow + headline | language copy QA |
| BodyCopy | paragraph | copy | body | language copy QA |
| Button (the one primary CTA) | button | copy | cta (+ data-link-slot) | language copy QA |
| PromoLine (only with a real code) | text | copy | body | language copy QA |
| Divider | divider | structural | (none) | house style |
| ListBlock | text | copy | list | language copy QA |
| ClassCardGrid (other classes) | image | element | (none, 3 covers) | email-asset-qa |
| FeatureImage | image | element | (none, text-free) | email-asset-qa |
| EventDetails | text | copy | eventdetails | language copy QA |
| BillingNotice | paragraph | copy | billing | language copy QA |
| Footer | social + structural | element + structural | (none) | email-asset-qa + house style |
| LessonCardGrid (multi-instructor) | image + text | element + copy | card-headline + card-credential + card-cta | email-asset-qa (portrait) + language copy QA |
| IssueIndex | text | copy | index | language copy QA |
| MemberWin | text | copy | quote + body | language copy QA |

The renderer emits all 16; a block renders only when its spec keys are present. Staging the
rendered mockup into Ortto (drafting via `create_asset`, mapping the audience and journey) is a
separate, gated step in `context/profiles/maharat/email-creation-cheatsheet.md`, never part of the mockup.

## Layer 3: templates (archetype recipes)

Pick the archetype from "$ARGUMENTS". Each is a `modules` order plus the spec keys it needs. The
header (logo, hero, eyebrow, headline), the one CTA, and the footer are always emitted. Angle and
copy come from the cited source, never invented here.

| Archetype | modules order (between heading and CTA) | key spec fields | angle source |
|---|---|---|---|
| `multi-instructor-digest` (the "3 ways to X" digest) | `issueindex`, `body`, `lessoncards`, `memberwin` | `issue_index[]`, `lesson_cards[]` (headline, credential, cta, portrait), `member_win` | `context/profiles/maharat/multi-instructor-angles.md` (umbrella outcome, the "3 X to Y" subject) |
| `occasion-promo` (one email of the sale ladder) | `body`, `lessoncards` (the lineup) | offer, discount, dates (from brief), `lesson_cards[]`, optional `promo.code` | `promo-sequence` + `multi-instructor-angles.md` |
| `personal-voice-launch` (the instructor's first-person letter) | `body` (multi-paragraph letter), `body` (signature line) | `body` as a list of paragraphs, signature from the instructor voice.md | `newsletter-patterns.md` + the instructor `voice.md` |
| `meet-the-instructor` (single-instructor announcement) | `body` (the benefit), `list` (what you will learn) | `body`, `list_items[]`, `list_title` | `newsletter-patterns.md` (class announcement) |
| `gifting` (give-a-membership, existing members) | `body` (the give offer), optional `promo` | offer and dates from brief, audience = existing members | `multi-instructor-angles.md` (gifting logic) |
| `single-class` (the 7-step style) | `body`, `list`, optional `classcards` | `body`, `list_items[]`, `class_cards[]` | the active brief and instructor pack |
| `contest` | NOT BUILDABLE | n/a | compliance-gated, see Rules below |

For a multi-instructor archetype, build each `lesson_cards[]` card as the rigid formula: an
outcome-first headline, a `with [Name], [one page-cleared credential]` line, and a quiet secondary
link. Co-taught (two instructors, one class) is NOT a LessonCardGrid: render it as one Hero plus
one BodyCopy that names both, never a grid of separate classes.

## Layer 4: rules (the gate and the brand)

- One primary CTA (the emerald pill). In a digest, per-card links are quiet secondary text links,
  never a second pill.
- Brand constants and fonts only. No em dashes, no tatweel, Western numerals only.
- Empowering, never deficit-framed. Never imply accreditation.
- Every named instructor is catalog-status-confirmed (`context/subjects/_CATALOG.md`) and every
  credential traces to a page-cleared fact or a voice.md verified-safe belief; else the card or the
  email is held back. A multi-instructor email multiplies this gate, every card must clear.
- No invented offer, price, discount, date, Skill Path title, instructor, or catalog count. A
  missing value is a stop-and-ask, or a clearly-labeled MOCK placeholder in a mockup run.
- `contest`: documented in `context/profiles/maharat/multi-instructor-angles.md` but NOT buildable here. A
  sweepstakes or prize needs Saudi PDPL, contest law, eligibility, and entry-data handling cleared
  by `compliance-privacy-reviewer` first. Refuse to build it until then.

## Steps

1. Resolve the archetype from "$ARGUMENTS" and the source: a campaign-id (use its QA-passed
   `copy-package` and brief) or `mock` (clearly-labeled placeholders, status MOCKUP).
2. Write the spec: `outputs/<campaign-or-mock>/mockups/<archetype>/spec.json`. Set `status`,
   `campaign_title`, and per email: `id`, `lang` (ar and en), `subject`, `preheader`, `headline`,
   `cta {label,url}`, the `modules` order for the archetype, and the block fields it needs. For a
   real campaign, every copy slot value is a QA-passed variant; for a mock, label placeholders MOCK.
3. Render: `python3 .claude/scripts/email_render.py <spec.json>`. It writes one slotted HTML per
   email per language plus an `index.html` preview.
4. Sweep: `python3 .claude/scripts/house_style_sweep.py <files>`. Must be clean (no em dash, no
   tatweel, Western numerals).
5. Eval: run the `email-html-build` eval (`python3 .claude/scripts/eval_runner.py` on the build
   eval) for structure, slot binding, and one primary CTA.
6. Report the mockup paths, the gate stack that still applies before any send (language copy QA,
   email-asset-qa, accessibility-qa, compliance-privacy-check, brand-qa-reviewer, human gate), and
   state plainly that this is a mockup and nothing sends.

## Example

`/email-mockup multi-instructor-digest mock` produces an AR and EN "3 ways to [outcome]" digest with
an IssueIndex, a 3-card LessonCardGrid (placeholders Instructor One, Two, Three), and a MemberWin,
one emerald CTA, rendered and swept. A worked example spec and its rendered output live in
`skills/05-build-launch/email-html-build/examples/multi-instructor-digest/`.
