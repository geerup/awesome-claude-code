# Copy QA verdict: Bassam Fattouh Teaches Makeup, 7-step email sequence

Build: outputs/2026-06-bassam-fattouh-makeup/email-7step/bassam-fattouh
Gates run on the rendered HTML copy slots (preheader, eyebrow, headline, body, list, cta):
- skills/arabic-copy-qa on every AR email (e1 to e7), 7 checks: msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals, no-em-dash, empowering-framing, rtl-safe.
- skills/english-copy-qa on every EN email (e1 to e7), 7 checks: empowering-tone, no-em-dash, western-numerals, one-clear-cta, no-accreditation-implication, no-invented-offers-titles, plain-active-voice.

Reviewed: the visible copy as it appears in the rendered HTML.

## Result by email and language

| email | lang | result |
|-------|------|--------|
| e1 | ar | PASS |
| e1 | en | PASS |
| e2 | ar | PASS |
| e2 | en | PASS |
| e3 | ar | PASS |
| e3 | en | PASS |
| e4 | ar | PASS |
| e4 | en | PASS |
| e5 | ar | PASS |
| e5 | en | PASS |
| e6 | ar | PASS |
| e6 | en | PASS |
| e7 | ar | PASS |
| e7 | en | PASS |

No fixes required. No copy was rewritten.

## Notes (passing, recorded for the record)

- Reader address is masculine throughout all 7 AR emails, an acceptable default for the general makeup class per the brand gendered-address rule, and coherent email to email.
- Empowering framing holds: the copy speaks to what the reader builds and becomes (taqniyah tabqa ma3ak, qariban satasna3 lookak bi-nafsak wa-bi-thiqah, anta aqrab mimma tazunn), never deficit or shame.
- Claims discipline held. "One of the most sought-after makeup artists in the region" (AR: ahad ashhar al-khubara fil-3alam al-3arabi, akthar khubara al-makyaj talaban) is supported by the published class tagline and the instructor profile. No client names, brand lines, awards, lesson counts, prices, or accreditation language appear.
- Mechanical checks clean: no em dash, no en dash, no tatweel, Western numerals only, verified by a full glyph scan of the rendered HTML.
- RTL-safe: no ASCII punctuation adjacent to Arabic; the Arabic comma is used throughout.
- Each EN email carries exactly one primary CTA. The "More classes on Maharat" line is a section heading for the see-also class-cards module, not a competing call to action.

## Summary

AR: 7 PASS, 0 FAIL.
EN: 7 PASS, 0 FAIL.
