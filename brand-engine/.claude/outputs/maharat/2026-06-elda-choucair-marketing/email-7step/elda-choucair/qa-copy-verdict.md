# Copy QA verdict: Elda Choucair marketing, 7 step email sequence

Gates run on rendered HTML:
- skills/arabic-copy-qa on every AR email (e1.ar to e7.ar). Checks: msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals, no-em-dash, empowering-framing, rtl-safe.
- skills/english-copy-qa on every EN email (e1.en to e7.en). Checks: empowering-tone, no-em-dash, western-numerals, one-clear-cta, no-accreditation-implication, no-invented-offers-titles, plain-active-voice.

Copy judged as it appears in the rendered HTML. Claims checked against context/instructors/elda-choucair/profile.md. The only cleared credibility line is "one of the Arab world's most respected marketing leaders, with decades of experience shaping iconic brands and industry-defining strategies" (live class page, 2026-06-05). The internal-doc figures (CEO Omnicom Media, 20+ years, leads 900+ professionals, 1000+ campaigns, Forbes 100 Most Powerful Businesswomen, Entrepreneur Top 50, Cannes Lions jury) are verify-before-public-use and must not appear in copy.

## Per email, per language

| Email | Lang | Result |
|---|---|---|
| e1 | ar | PASS |
| e2 | ar | PASS |
| e3 | ar | PASS |
| e4 | ar | PASS |
| e5 | ar | PASS |
| e6 | ar | PASS |
| e7 | ar | PASS |
| e1 | en | PASS |
| e2 | en | PASS |
| e3 | en | PASS |
| e4 | en | PASS |
| e5 | en | PASS |
| e6 | en | PASS |
| e7 | en | PASS |

## Fixes applied

None. No gate failed on any span.

## Notes on claims discipline (all clear)

- Elda is framed as "من أبرز القيادات التسويقية في العالم العربي، بخبرة في بناء علامات تجارية مؤثرة وصياغة استراتيجيات شكّلت قطاعات كاملة" / "one of the Arab world's most respected marketing leaders, with experience building iconic brands and shaping industry-defining strategies". This is the cleared page-sourced line. None of the held-back internal figures (Omnicom, the 900+, 1000+, Forbes, Entrepreneur, Cannes) leaked into any email.
- rtl-safe: e6.ar uses Arabic guillemets «...» around the two reframed questions. These are paired, direction-safe quotation marks, not ASCII punctuation after Arabic, so rtl-safe passes. No ASCII-comma-after-Arabic anywhere in this build.
- Tone is empowering, never deficit-framed: "ابدأ من فكرة واحدة تغير طريقة نظرك", "حوّل خبرتها إلى وضوح في قرارك", "تتعلم على وقتك". The "منافسك ليس أفضل منك" line reframes toward a learnable skill, not reader shame.
- Gendered reader address is masculine and neutral (ابدأ، شاهد، أكمل، اشترك), correct for the marketing category.
- One clear CTA per email. No accreditation implication. No invented titles. Class title matches the published course. Western numerals only.

## Summary

- AR: 7 PASS, 0 FAIL.
- EN: 7 PASS, 0 FAIL.
