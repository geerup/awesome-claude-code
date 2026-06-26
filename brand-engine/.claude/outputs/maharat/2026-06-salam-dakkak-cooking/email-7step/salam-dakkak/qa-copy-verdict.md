# Copy QA verdict: Salam Dakkak, 7-step nurture-to-subscribe

Gates run on the rendered email HTML, copy judged as it appears in the render:
- skills/arabic-copy-qa on every AR email (e1 to e7). Checks: msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals, no-em-dash, empowering-framing, rtl-safe.
- skills/english-copy-qa on every EN email (e1 to e7). Checks: empowering-tone, no-em-dash, western-numerals, one-clear-cta, no-accreditation-implication, no-invented-offers-titles, plain-active-voice.

Class match: the copy matches the class, Levantine home cooking, the warm home recipes, technique, and kitchen confidence framing.

Claims note: the class title Teaches Levantine Home Cooking is verified. Best Female Chef in MENA, the restaurant Bait Maryam, Michelin award winning, secret recipes, and Over 20 recipes are all the exact published wording of the Maharat class page and homepage (skills/instructor-marketing/salam-dakkak/masterclass-pages.md), and the build held-back ledger keeps them to that wording: no Michelin star claim, no named award body, no income or restaurant-success promise. No price, plan, or accreditation appears. Claims discipline held.

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
| e5 | EN | PASS (after fix and re-render) |
| e6 | AR | PASS |
| e6 | EN | PASS |
| e7 | AR | PASS |
| e7 | EN | PASS |

## Fix applied (e5 EN), then re-rendered to PASS

On the first pass e5 EN failed one check. The fix was applied in spec.json (emails e5 EN body, third line) and the build was re-rendered clean before recording PASS.

{ check: "plain-active-voice", span: "Experience this deep, carried generously and simply into your own kitchen.", fix: "the sentence has no clear parse, Experience reads as a stray imperative with no main verb. Change the lead noun so the phrase reads plainly: Expertise this deep, carried generously and simply into your own kitchen." }

Result of the fix in the re-rendered e5 EN: "Expertise this deep, carried generously and simply into your own kitchen." No new claim introduced, the line mirrors the AR meaning (expertise of this depth, carried generously and simply to your kitchen).

No other fix items. Mechanical checks verified clean across the build: no em dash, no en dash, no tatweel, no Eastern numerals in any spec.json or rendered HTML. The Arabic comma is used after Arabic throughout, zero ASCII Latin commas appear after Arabic in any AR render (rtl-safe holds). The numeral 20 in the Over 20 recipes line is a Western numeral and is supported by the page. Each EN email carries exactly one primary CTA.

## Summary

AR: 7 PASS, 0 FAIL. EN: 7 PASS, 0 FAIL (e5 EN passed after one fix and a clean re-render).
