# Elda Choucair, masterclass invite (test build)

Slotted Ortto email, AR and EN, built to exercise the email design system end to end.
Internal draft. Not for public send.

- `elda-masterclass-invite.ar.html` (RTL)
- `elda-masterclass-invite.en.html` (LTR)

## Status and gates

- Catalog status: `elda-choucair` is `unconfirmed`. The status gate means internal draft only.
  Public naming and the published title, tagline, and chapter list are cleared (profile.md plus
  Ahmed sign-off 2026-06-05). Sending stays blocked until the catalog status is confirmed.
- Gates still to run: pack eval, then `arabic-copy-qa` (AR) or `english-copy-qa` (EN), then
  `accessibility-qa` (email render), then `brand-qa-reviewer`, then the human gate.

## Components used (design system, 12-component library)

EmailShell, view-in-browser header, LogoBar, Hero (text-free background with live text overlay),
BodyCopy, SectionHeading, LearnList, Button (one primary), Divider, ClassCardGrid (author cards),
Footer (social icons, www, sender address, unsubscribe).

## Copy slots (what the binding gate reads, per language)

`preheader`, hero `headline` + `eyebrow`, `body`, learn `headline` + `list`, offer `body`,
`cta`, footer address `body`. Subject is the asset-level slot set in `create_asset`.

- AR subject: صف جديد على مهارات: إلدا شقير تعلّم التسويق
- EN subject: New on Maharat: Elda Choucair Teaches Marketing

## Text on images

Compliant interpretation: live HTML text over a text-free background image (hero), with an MSO
VML fallback for Outlook. No Arabic or English is baked into pixels. This keeps every word a
QA-able, translatable, accessible slot, which is the audit's number-one fix.

## Claims discipline

- Used (cleared): published title, the published tagline, the confirmed chapter themes, chapter 1
  free, and voice.md verified-safe beliefs.
- Held back (verify-before-public): CEO Omnicom, 20-plus-years, 900-plus, 1000-plus, Forbes,
  Cannes, 100-plus brands. Verified absent from both files.

## Image assets (wired from real sources)

Logo, class cover (hero), class cards, and social icons now point at the live Maharat CDN URLs
from the actual sends, so the template renders. The Drive holds the high-res masters for design
reuse: `06 - INSTRUCTOR PORTRAIT` (vertical and square), `01 - The Talent`, `LANDING PAGE COVER
PHOTO`, and the Elda master folder (Drive id 1IKVC5IScHzYV6EfBZTqn4tHfKPeclHfY). For a fully
text-free hero with a live title overlay, swap the cover for a text-free portrait.

## Asset reference

| Asset | Slot | Requirement |
|---|---|---|
| Maharat logo | LogoBar | brand-kit asset, ~118px |
| Hero background | Hero | text-free, rights-cleared Elda image. The published class cover has baked title text and pending rights, so it cannot be used as is. Generated likeness never allowed. |
| Class cards 1 to 3 | ClassCardGrid | rights-cleared, text-free; only status-cleared instructors (the rest of the roster is still `unconfirmed`) |
| 6 social icons | Footer | brand-kit icon set, 28px |

## Did we miss anything (addressed here, plus open items)

Addressed: alt text on every image, view-in-browser, sender-address line, mobile stacking,
Outlook VML button and background fallback, `{{ unsubscribe }}` and `{{ view_in_browser_url }}`
tokens, one primary CTA, the fixed type scale (28 / 22 / 18 / 14 / 13 / 12), and per-language
direction with `data-lang` on each slot.

Open items: the image assets above, full Outlook and dark-mode render testing, the catalog
status confirmation, and the Ortto round-trip (`create_asset` then inspect the derived
`mail_json`) to confirm the `data-ortto-module` blocks map as intended.

## Into Ortto

One `create_asset(name, subject, mail_html)` per language. The `data-ortto-module` blocks are
intended to land as the matching Ortto modules; the round-trip test confirms this before reliance.
Sending stays a gated action.
