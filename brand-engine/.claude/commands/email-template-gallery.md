---
description: Build the full gallery of email template mockups in one run, one slotted HTML mockup per archetype (multi-instructor-digest, occasion-promo, personal-voice-launch, meet-the-instructor, gifting, single-class), assembled into one combined preview sheet. Uses the same primitives, blocks, Ortto section ids, and rules as /email-mockup. Nothing sends. Usage - /email-template-gallery [campaign-id-or-mock]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3 .claude/scripts/email_render.py:*), Bash(python3 .claude/scripts/house_style_sweep.py:*), Bash(python3 .claude/scripts/eval_runner.py:*)
---

# /email-template-gallery

Build the whole library of email template mockups in one pass, one mockup per archetype, into a
single combined preview sheet so the set can be reviewed side by side. This is `/email-mockup` run
across every buildable archetype at once. It is the design-review companion: assemble, render,
preview. It never sends; going live is a human-gate decision and a separate staging step.

It invents nothing. With a campaign-id it uses that campaign's QA-passed `copy-package`; with `mock`
it uses clearly-labeled MOCK placeholders (and placeholder instructors that are NOT real catalog
entries). A mockup is labeled MOCKUP and INTERNAL DRAFT and is never presented as real or sent.

Load first: `commands/email-mockup.md` (the four layers, the block-to-Ortto-section-id table, the
rules, all reused here), then `context/profiles/maharat/email-design-system.md`, `runtime/email-module-map.md`,
`context/profiles/maharat/multi-instructor-angles.md`, `skills/04-copywriting/email-copy/templates/newsletter-patterns.md`,
`skills/07-lifecycle-messaging/templates/sequence-standards.md`,
`skills/05-build-launch/email-html-build/SKILL.md`. The renderer is `scripts/email_render.py`.

## The one move that makes this a gallery

`scripts/email_render.py` writes one `index.html` preview that shows every entry in a spec's
`emails[]` array. So a gallery is ONE `spec.json` whose `emails[]` carries one entry per archetype
(each with its own `modules` order). Render it once, and the `index.html` is the combined gallery.
No new renderer code, no per-archetype folders.

## The archetypes to emit (one entry each, skip the gated one)

Build these, in this order, reusing the recipes in `commands/email-mockup.md` (Layer 3). Emit
Arabic and English for the digest (to show RTL and LTR), English for the rest, unless the run asks
for both languages throughout.

| id | archetype | modules order | the point it demonstrates |
|---|---|---|---|
| `g1-digest` | multi-instructor-digest | `issueindex`, `body`, `lessoncards`, `memberwin` | the "3 ways to X" digest, IssueIndex, the 3-card LessonCardGrid, MemberWin |
| `g2-promo` | occasion-promo | `body`, `lessoncards` | one email of the urgency-ladder sale, the lineup as cards |
| `g3-voice` | personal-voice-launch | `body` (letter ending in the signature line) | the instructor's first-person launch |
| `g4-meet` | meet-the-instructor | `body`, `list` | the announcement plus "what you will learn" |
| `g5-gift` | gifting | `body` | give-a-membership to existing members |
| `g6-class` | single-class | `body`, `list`, `classcards` | the 7-step style single-instructor email |

Do NOT emit a contest or sweepstakes entry. It is compliance-gated (Saudi PDPL, contest law,
eligibility, entry-data handling) and not buildable until `compliance-privacy-reviewer` clears it.

## Rules (same as /email-mockup, do not relax for a gallery)

- One primary CTA per entry. In the digest, per-card LessonCardGrid links are quiet secondaries,
  never a second pill.
- Brand constants and fonts only. No em dashes, no tatweel, Western numerals. Empowering, never
  deficit-framed. Never imply accreditation.
- Every named instructor is catalog-status-confirmed and every credential page-cleared, or the card
  is dropped. Co-taught (two instructors, one class) is one Hero plus BodyCopy, not a grid.
- No invented offer, price, discount, date, Skill Path title, instructor, or catalog count. In a
  mock run, placeholders are labeled MOCK and carry no fabricated numbers.

## Steps

1. Resolve the source from "$ARGUMENTS": a campaign-id (its QA-passed copy) or `mock`.
2. Write one gallery spec: `outputs/<campaign-or-mock>/mockups/gallery/spec.json`. Set `status`
   (MOCKUP for a mock run) and `campaign_title`. Add one `emails[]` entry per archetype above,
   each with `id`, `lang`, `subject`, `preheader`, `headline`, `cta {label,url}`, its `modules`
   order, and the block fields it needs. Reuse the per-archetype field shapes from
   `commands/email-mockup.md`.
3. Render once: `python3 .claude/scripts/email_render.py <spec.json>`. The `index.html` it writes
   is the combined gallery.
4. Sweep: `python3 .claude/scripts/house_style_sweep.py <dir>/*.html`. Must be clean.
5. Eval: run the `email-html-build` eval (`scripts/eval_runner.py` on its `evals.json`) over the
   rendered entries.
6. Report the gallery path (open `index.html`), the gate stack that still applies before any send,
   and state plainly that this is a mockup gallery and nothing sends.

## Output

A single `index.html` previewing every template, plus the per-entry slotted HTML and the
`spec.json` recipe. A worked example gallery is in
`skills/05-build-launch/email-html-build/examples/gallery/`. To regenerate one template in
isolation, use `/email-mockup <archetype>`.
