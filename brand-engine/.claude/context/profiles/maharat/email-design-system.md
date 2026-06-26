# email-design-system.md: the Maharat email visual standard

The visual standard every built email is held to. It is the design half of the email build;
the slot and routing half is `runtime/email-module-map.md`. It exists because the old sends
were image-only (copy baked into one flat picture, unreadable to screen readers, un-QA-able,
broken in RTL). The standard rebuilds them as live components on the brand.

No em dashes. Western numerals only. Arabic-first. RTL is the default. Premium, uncluttered.

Provenance: rebuilt from the 45-email audit of the live Maharat sends and the email-system
spec. Imagery is live Maharat creative via the Ortto CDN.

## Themes

- Dark, the default. Marketing and promotional sends. Paper `#141414`.
- Light paper, transactional and lifecycle only. Same components, re-themed.

## Tokens

Color, aligned to the constitution (`CLAUDE.md` visual constants):

- Paper (background): `#141414`
- Panel (card surface): `#1A1A1A`
- Green (primary accent, one per email): `#009975`
- Text on dark: `#FFFFFF` headline, `#E6E6E6` body, `#9A9A9A` fine print
- Light paper variant: `#F4F2EE` background, `#1B1C1F` text, `#1A6B5A` accent (darkened green for AA on light)

PENDING approval to extend the constitution (do not use in customer-facing output until Ahmed
signs off, flagged by `brand-qa-reviewer`):

- Panel `#1c1c1c` (the spec's panel, a hair off the constitution's `#1A1A1A`, reconcile to one)
- Gold `#C4963C` (a second accent for promo code chips and event labels, not in the constitution)

Type scale (collapses the old ad-hoc sizes into six): H1 28, H2 22, Sub 18, Body 15,
Footer 13, Fine 12. Line height about 1.7 for Arabic body.

Shape and layout: width 600, side padding 24, card radius 16, small card 12, CTA pill radius 28.
RTL default.

## Fonts

The only fonts, the Maharat-licensed brand faces (provided 2026-06-08). Delivered to email by
the Ortto-hosted custom-fonts CSS link in the head, the same pattern as the live Maharat sends,
with web-safe fallbacks. The binaries stay in the gitignored `.claude/assets/fonts/` build
cache rather than the repo, because an inbox loads the font from the hosted CSS, not from git.
Self-hosting the woff2 is an option if Maharat moves off Ortto.

- Arabic display and headlines: Lyon Arabic Display, Black, weight 900. Ortto family `Lyon Arabic Display`.
- Arabic body and UI: 29LT Azer, Regular and Black. Open item: upload 29LT Azer to Ortto so it
  serves the same way. Until then Arabic body falls back to `Tahoma, Arial, sans-serif`.
- English, all weights: Acumin Pro. Ortto family `Acumin Pro`.
- Stacks: Arabic `'Lyon Arabic Display','29LT Azer',Tahoma,Arial,sans-serif`, English
  `'Acumin Pro',Arial,sans-serif`. No other font is used anywhere in an email.

## The CTA, and its one hard contrast rule

One primary CTA per email, an emerald pill (radius 28, weight 700, size 16). A second link is
at most a quiet secondary, never a competing button. The label color must clear WCAG 2.2 AA
against `#009975`: near-black `#141414` on emerald is about 5:1 and is the default. White on
emerald is about 3.6:1 and fails AA for normal-weight text, so use white only where the label
qualifies as large text. `accessibility-qa` enforces this; it fixes the label color, never the
brand green.

The multi-instructor digest is the one layout with many links, and it still keeps one primary CTA:
the single emerald pill is the join or the offer (repeated at most once near the foot), and every
per-card LessonCardGrid link ("start learning") is a quiet secondary text link, never a second
pill. So a digest with three cards has one primary pill and three quiet secondaries, which keeps
the one-primary-CTA rule intact.

## The component library

A built email composes only from these. Each maps to slots in `runtime/email-module-map.md`.

1. LogoBar. Centered Maharat logo, about 118px, on paper. Image element, text-free.
2. Hero. The class key art or a text-free background, 600 wide, radius 16, alt required. Any
   headline over it is a live copy slot, never baked pixels.
3. SectionHeading. An emerald eyebrow (letter-spaced, in the brand font) plus an H1. Copy slots.
4. BodyCopy. 15px, line height about 1.7, right-aligned in Arabic. Copy slot.
5. Button. The canonical CTA pill. Copy slot for the label, `data-link-slot` for the URL.
6. PromoLine. A code chip (gold, pending) plus a short urgency line. Never invent a code or a deadline.
7. Divider. A hairline rule. Structural.
8. ListBlock. "What you will learn" or steps or benefits, emerald bullets. Copy slot.
9. ClassCardGrid. Three linked class covers, only status-cleared instructors and rights-cleared,
   text-free covers. Image elements.
10. FeatureImage. A single 600 wide, text-free, rights-cleared image, radius 16, alt required.
11. EventDetails. Date, time, seats for a live session or masterclass, a bordered panel. Copy
    slot. Never invent a date, time, or seat count.
12. BillingNotice. A calm transactional notice (payment issue). Copy slot, light or dark.
13. Footer. www line, social icons (image elements), sender postal identity, unsubscribe. Stable
    across all sends. The unsubscribe link is required.

### Multi-instructor digest modules (the extension set, 14 to 16)

Three modules that extend the core 12+1 for multi-instructor and catalog emails: a Skill Path
launch, a themed roundup, an occasion sale, or a "picked for you" recommendation. The angle method
they serve is `context/multi-instructor-angles.md`. They are used only for the multi-instructor
format; a single-class email still composes from the core set. The library is 16 in all (the 12+1
core plus these 3).

14. LessonCardGrid. The primary multi-instructor vehicle, a 3-up (or fewer) body grid where each
    card casts one instructor as one lesson toward the email's umbrella outcome. Per card: a
    text-free, rights-cleared instructor portrait (image element), an outcome-first headline (copy
    slot), a "with [Name], [one page-cleared credential]" line (copy slot), and a quiet secondary
    link to that class (copy slot label, a text link, never a second pill). Only catalog-status
    confirmed instructors with rights-cleared, text-free portraits; an unconfirmed instructor's
    card is dropped, never improvised. This is ClassCardGrid's richer sibling: ClassCardGrid is the
    "other classes" footer (name plus "Teaches X"), LessonCardGrid is the in-body offer grid
    (outcome headline plus credential plus link).
15. IssueIndex. An optional "In This Issue" numbered table of contents at the top of a digest,
    magazine style. Copy slots: each entry is a short label, Western numerals (01, 02, 03), each an
    in-email or in-page link to its section. Scannable, never more than about 6 entries.
16. MemberWin. A social-proof block: one real, consented member testimonial (copy slot), the
    attribution (copy slot), and a short reflective bridge line (copy slot) that leads into the
    primary CTA. The testimonial must be real and consented, never invented or paraphrased into a
    claim; authenticity is checked at brand QA and compliance.

## The mandates that bind every email

- Live text, never image-only. Every word is a live copy slot. Text-on-image is live HTML over
  a text-free background, with a VML fallback for Outlook.
- No Arabic baked into any image. Generated or composed imagery is text-free; the headline is
  overlaid as live text in the build.
- Real, rights-cleared assets only, hosted on the Ortto CDN. No raw Drive or hotlink-protected
  CloudFront in an `img src`. Sourcing and rights are checked by `email-asset-qa`.
- One primary CTA. Sender identity and unsubscribe in every email.
- House style: no em dashes, no tatweel, Western numerals only, swept on the built HTML.
- Instructor emails are blocked until catalog status is confirmed, and carry only page-cleared
  plus voice.md verified-safe claims.

## How it is built

Authored in MJML (the component library under `skills/05-build-launch/email-html-build/mjml/`)
and compiled to the Ortto-slotted table HTML, or hand-built to the same slotted output. Either
path produces the same module map and passes the same gates. See the `email-html-build` skill.
