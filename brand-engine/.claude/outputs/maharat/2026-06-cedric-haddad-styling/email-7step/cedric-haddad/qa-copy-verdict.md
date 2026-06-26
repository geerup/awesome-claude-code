# Copy QA verdict: Cedric Haddad personal styling, 7 step email sequence

Gates run on rendered HTML:
- skills/arabic-copy-qa on every AR email (e1.ar to e7.ar). Checks: msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals, no-em-dash, empowering-framing, rtl-safe.
- skills/english-copy-qa on every EN email (e1.en to e7.en). Checks: empowering-tone, no-em-dash, western-numerals, one-clear-cta, no-accreditation-implication, no-invented-offers-titles, plain-active-voice.

Copy judged as it appears in the rendered HTML. Claims checked against context/instructors/cedric-haddad/profile.md. The only cleared credibility line is "a celebrity stylist trusted by the Arab world's biggest stars" (live class page, 2026-06-05). No price, no lesson count, no named private clients, no accreditation appear in copy. Title used matches the published class.

## Per email, per language

| Email | Lang | Result |
|---|---|---|
| e1 | ar | PASS (after fix, see below) |
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

## Fixes applied (failed, fixed in spec.json, re-rendered, then PASS)

e1.ar, rtl-safe:
{ check: "rtl-safe", span: "نجوم العالم العربي, يعلّمك", fix: "replace the ASCII Latin comma after the Arabic word العربي with the Arabic comma U+060C, giving نجوم العالم العربي، يعلّمك" }

Source corrected in spec.json body slot, then re-rendered with scripts/email_render.py. Re-scan of e1.ar.html shows zero ASCII-comma-after-Arabic occurrences and the Arabic comma in place. No other email in this build had the ASCII-comma-after-Arabic issue.

## Notes on claims discipline (all clear)

- Cedric is framed as "خبير الموضة المفضل لدى نجوم العالم العربي" / "the celebrity stylist trusted by the Arab world's biggest stars". This matches the single cleared page-sourced fact. No specific awards, no named clients, no lesson count, no price leaked.
- Gendered reader address is feminine throughout (ابدئي، شاهدي، تخيّلي)، correct for the styling and beauty category per brand-voice.
- No accreditation implication. No invented Skill Path titles. Class title matches the published course.

## Summary

- AR: 7 PASS, 0 FAIL (e1.ar passed after one rtl-safe fix and a clean re-render).
- EN: 7 PASS, 0 FAIL.
