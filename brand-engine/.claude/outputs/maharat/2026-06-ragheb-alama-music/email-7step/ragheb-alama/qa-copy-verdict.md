# Copy QA verdict: Ragheb Alama music and performance, 7 step email sequence

Gates run on rendered HTML:
- skills/arabic-copy-qa on every AR email (e1.ar to e7.ar). Checks: msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals, no-em-dash, empowering-framing, rtl-safe.
- skills/english-copy-qa on every EN email (e1.en to e7.en). Checks: empowering-tone, no-em-dash, western-numerals, one-clear-cta, no-accreditation-implication, no-invented-offers-titles, plain-active-voice.

Copy judged as it appears in the rendered HTML. Claims checked against context/instructors/ragheb-alama/profile.md. Cleared page-sourced facts: "40 years of experience in the music industry" and "teaches, for the first time, how to pursue a career in music" (live class page, 2026-06-05). No price, no lesson or chapter count, no named clients, no awards appear in copy.

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

- The two credibility claims used, "40 سنة من الخبرة" / "40 years of experience" and "لأول مرة ... كيفيّة ممارسة مهنة الموسيقى" / "for the first time ... how to pursue a career in music", are both cleared page-sourced facts. The number 40 is written in Western numerals everywhere it appears (e1, e2, e5, e7, AR and EN).
- No held-back claim leaked: no award, no named collaborator beyond the song titles already on the live class page, and song titles are not used in the email copy itself.
- rtl-safe: no ASCII-comma-after-Arabic and no direction-breaking punctuation anywhere in this build.
- Tone is empowering and Thmanyah-clear: "أنت أقرب مما تظن", "امنح صوتك وأداءك المساحة التي يستحقها", "كل درس يقربك من صوتك وأدائك". Never deficit-framed.
- Gendered reader address is masculine and neutral (ابدأ، شاهد، أكمل، اشترك), correct for the music category.
- One clear CTA per email. No accreditation implication. No invented titles. Class title matches the published course. Western numerals only.

## Summary

- AR: 7 PASS, 0 FAIL.
- EN: 7 PASS, 0 FAIL.
