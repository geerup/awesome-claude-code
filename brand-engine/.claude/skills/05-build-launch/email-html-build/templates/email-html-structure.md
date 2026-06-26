# Email HTML build structure (the slotted component template)

The shape of one built email. It composes from the 12+1 core components in
`context/profiles/maharat/email-design-system.md`, plus the 3 multi-instructor digest modules (the extension set:
LessonCardGrid, IssueIndex, MemberWin) for a Skill Path, a themed roundup, an occasion sale, or a
recommendation. Each carries the slot attributes from `runtime/email-module-map.md`. Copy is bound
by `data-copy-id`, never written here. Images are `data-slot="element"`, text-free, hosted on the
approved Ortto CDN. The committed slotted HTML is the source of truth; the MJML under `../mjml/`
compiles to match it.

This template names the banned glyph and Eastern numerals in words, so the template file itself
stays house-clean.

## Head (every email)

- `<html lang dir>`: `lang="ar" dir="rtl"` for Arabic, `lang="en" dir="ltr"` for English, plus
  the VML namespaces (`xmlns:v`, `xmlns:o`) for the Outlook roundrect.
- meta: charset utf-8, viewport, `color-scheme dark` and `supported-color-schemes dark` for the
  dark theme.
- Brand fonts via the Ortto-hosted custom-fonts CSS, the ar2 reference pattern:
  - `accounts-api-us.ortto.app/-/settings/custom-fonts.css?family=Lyon+Arabic+Display&k=...`
  - `accounts-api-us.ortto.app/-/settings/custom-fonts.css?family=Acumin+Pro&k=...`
  - Stacks: Arabic `'Lyon Arabic Display','29LT Azer',Tahoma,Arial,sans-serif`, English
    `'Acumin Pro',Arial,sans-serif`. No binary embedded or committed.
- A small `<style>` block: body background paper `#141414`, the 600 wide `.wrap`, the mobile
  media query (`.wrap` to 100%, `.px` side padding to 24), the list-marker helper.

## The slot attributes on every module-bearing cell

| Attribute | Example | Meaning |
|---|---|---|
| `data-ortto-module` | `paragraph` `heading` `text` `image` `button` `social` `divider` | the Ortto module type |
| `data-slot` | `copy` `element` `structural` | content kind and gate owner |
| `data-role` | `preheader` `eyebrow` `headline` `body` `list` `cta` `eventdetails` `billing` | the role |
| `data-lang` | `ar` `en` | the copy slot language, the copy-QA routing key |
| `data-copy-id` | `email-bassam-e1-headline-ar` | the QA-passed copy this slot renders |
| `data-link-slot` | the class URL | the CTA or linked-element destination, no personal data |

## Body order (compose from the library, one primary CTA)

1. Preheader: hidden `data-slot="copy" data-role="preheader"`, bound by `data-copy-id`.
2. View-in-browser: `data-slot="structural"`, the platform merge tag.
3. LogoBar: `data-ortto-module="image" data-slot="element"`, the autopilot CDN logo, ~118px,
   text-free, alt the brand name.
4. Hero: `data-ortto-module="image" data-slot="element"`, the class cover, 600 wide, radius 16,
   text-free, descriptive alt. Any headline over it is a live copy slot, never baked pixels.
5. SectionHeading: an emerald eyebrow (`data-role="eyebrow"`) plus the H1 (`data-role="headline"`),
   both copy slots bound by `data-copy-id`.
6. BodyCopy: `data-ortto-module="paragraph" data-slot="copy" data-role="body"`, bound by
   `data-copy-id`, right-aligned in Arabic, line height about 1.7.
7. Button: the single CTA. MSO VML roundrect for Outlook in an `[if mso]` block, plus the non-mso
   pill in `[if !mso]`. The pill cell carries `data-ortto-module="button" data-slot="copy"
   data-role="cta" data-lang data-link-slot`, label bound by `data-copy-id`, near-black `#141414`
   on emerald `#009975` (about 5:1, clears WCAG AA).
8. ListBlock (where the copy supports it): `data-ortto-module="text" data-slot="copy"
   data-role="list"`, emerald bullets, bound by `data-copy-id`.
9. Divider: `data-ortto-module="divider" data-slot="structural"`, a hairline rule.
10. ClassCardGrid (only status-cleared instructors with rights-cleared, text-free covers, else
    omit and flag): a heading copy slot plus a 3-up of `data-slot="element"` linked covers.
11. EventDetails (live session or masterclass only): `data-slot="copy" data-role="eventdetails"`,
    a bordered panel, bound by `data-copy-id`. Never invent a date, time, or seat count.
12. Footer: social icons (`data-ortto-module="social" data-slot="element"`, the getbee icon set),
    the www line (`data-slot="structural"`), the sender postal identity (a copy slot), and the
    unsubscribe link (`data-slot="structural"`, the platform merge tag). Required in every email.

## Multi-instructor digest modules (the extension set, used only for the multi-instructor format)

A digest email (a Skill Path, a themed roundup, an occasion sale, a recommendation) adds these
between the SectionHeading and the single Button. They render only when the spec supplies their
keys, so a single-class email never carries them. The angle method is
`context/profiles/maharat/multi-instructor-angles.md`.

- IssueIndex (`issue_index`): an optional numbered "In this issue" table of contents, right after
  the SectionHeading. A copy slot (`data-role="index"`), Western numerals (01, 02, 03), each entry
  a link to its section.
- LessonCardGrid (`lesson_cards`): the in-body offer grid, up to three cards. Each card is a cell
  carrying a text-free portrait (`data-slot="element"`) plus three copy slots:
  `data-role="card-headline"` (the reader outcome), `data-role="card-credential"` (the "with
  <Name>, <credential>" line), and `data-role="card-cta"` (a quiet secondary text link, never a
  second pill). Only catalog-status-confirmed instructors with rights-cleared, text-free portraits;
  an unconfirmed instructor's card is dropped before render.
- MemberWin (`member_win`): a social-proof block, late in the body. Copy slots: `data-role="quote"`
  (one real, consented testimonial), `data-role="body"` (the attribution), and `data-role="body"`
  (a short reflective bridge that leads into the single Button). The testimonial is real and
  consented, never invented.

The single primary CTA still holds: the one emerald pill is the join or the offer; every per-card
`card-cta` link is a quiet secondary text link. A three-card digest has one pill and three
secondaries.

## CTA: the one hard contrast rule

The label color must clear WCAG 2.2 AA against `#009975`. Near-black `#141414` on emerald is about
5:1 and is the default. White on emerald is about 3.6:1 and fails AA for normal-weight text. The
MSO VML `fillcolor` is `#009975`; the VML `center` label is the same near-black for parity.

## Theme

- Dark, the default. Marketing and promotional sends. Paper `#141414`, panel `#1A1A1A`.
- Light paper, transactional and lifecycle only: background `#F4F2EE`, text `#1B1C1F`, accent the
  darkened green `#1A6B5A` for AA on light. Same components, re-themed.

## The gate order (assembled, never sent)

skill eval, then `arabic-copy-qa` or `english-copy-qa` per copy slot by `data-lang`, then
`email-asset-qa` on every image module, then `accessibility-qa` on the render, then
`compliance-privacy-check`, then `brand-qa-reviewer`, then the human gate. The build never sends
on its own.

## House style

No em dash, no en dash, no tatweel, Western numerals only, swept on every built file with
`scripts/house_style_sweep.py` (the same FORBIDDEN set as `scripts/pack_check.py`).
