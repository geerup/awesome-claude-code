# Copy QA verdict: Toufic Kreidieh, 7-step nurture-to-subscribe

Gates run on the rendered email HTML, copy judged as it appears in the render:
- skills/arabic-copy-qa on every AR email (e1 to e7). Checks: msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals, no-em-dash, empowering-framing, rtl-safe.
- skills/english-copy-qa on every EN email (e1 to e7). Checks: empowering-tone, no-em-dash, western-numerals, one-clear-cta, no-accreditation-implication, no-invented-offers-titles, plain-active-voice.

Claims note: the class title Building and Growing Your Business is verified, and the billion-dollar from-scratch line is the exact published tagline on the Maharat class page (skills/instructor-marketing/toufic-kredieh/masterclass-pages.md), not an invented figure. Founder framing is verified in press. No store count, revenue figure, named client, lesson count, price, or accreditation appears. Claims discipline held.

## Per email, per language

| Email | Lang | Result |
|---|---|---|
| e1 | AR | PASS |
| e1 | EN | PASS |
| e2 | AR | PASS |
| e2 | EN | PASS |
| e3 | AR | PASS |
| e3 | EN | PASS |
| e4 | AR | PASS |
| e4 | EN | PASS |
| e5 | AR | PASS |
| e5 | EN | PASS |
| e6 | AR | PASS |
| e6 | EN | PASS |
| e7 | AR | PASS |
| e7 | EN | PASS |

No fix items. Mechanical checks verified clean across the build: no em dash, no en dash, no tatweel, no Eastern numerals in any spec.json or rendered HTML. The Arabic comma is used after Arabic throughout, zero ASCII Latin commas appear after Arabic in any AR render (rtl-safe holds). Each EN email carries exactly one primary CTA.

## Summary

AR: 7 PASS, 0 FAIL. EN: 7 PASS, 0 FAIL.
