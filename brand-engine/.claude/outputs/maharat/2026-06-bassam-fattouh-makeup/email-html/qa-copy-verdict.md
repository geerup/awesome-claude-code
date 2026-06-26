# Copy QA verdict: Bassam Fattouh Teaches Makeup, email-html slotted build

Build: outputs/2026-06-bassam-fattouh-makeup/email-html (e1 to e4)
Gates run on the rendered HTML copy slots (preheader, eyebrow, headline, body, list, cta):
- skills/arabic-copy-qa on every AR email (e1 to e4), 7 checks: msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals, no-em-dash, empowering-framing, rtl-safe.
- skills/english-copy-qa on every EN email (e1 to e4), 7 checks: empowering-tone, no-em-dash, western-numerals, one-clear-cta, no-accreditation-implication, no-invented-offers-titles, plain-active-voice.

Reviewed: the visible copy as it appears in the rendered HTML. Source of truth: emails.spec.json.

## Result by email and language

| email | lang | result |
|-------|------|--------|
| e1 | ar | PASS |
| e1 | en | PASS |
| e2 | ar | PASS (after fix, see below) |
| e2 | en | PASS |
| e3 | ar | PASS |
| e3 | en | PASS |
| e4 | ar | PASS |
| e4 | en | PASS |

## Fix applied

One AR email failed on first pass and was fixed at the source, then re-rendered clean.

e2.ar, check: msa-gulf-familiar (reader-address coherence). The email addressed the reader in the feminine while e1, e3, and e4 in the same sequence address the reader in the masculine, and the feminine headline and body sat next to a masculine CTA (shahid al-dars al-awwal) inside the same email. Mixed gender address breaks the register and the sequence's coherent reader address.

Fix items in the skill's shape:

- { check: "msa-gulf-familiar", span: "المكياج الذي تتقنينه بنفسك يوفر وقتك، ويعطيك ثقة في كل مناسبة.", fix: "make the address masculine to match the rest of the sequence: تتقنينه becomes تتقنه" }
- { check: "msa-gulf-familiar", span: "ابدئي متى ما ناسبك، وتقدّمي على راحتك.", fix: "masculine imperatives: ابدئي becomes ابدأ, وتقدّمي becomes وتقدّم" }
- { check: "msa-gulf-familiar", span: "لوك تصنعينه بنفسك، لا تنتظرينه من أحد", fix: "subject line to masculine: تصنعينه becomes تصنعه, تنتظرينه becomes تنتظره" }
- { check: "msa-gulf-familiar", span: "خطوة واحدة تفصلك عن مكياج تتقنينه", fix: "subject alt to masculine: تتقنينه becomes تتقنه" }

Source edited: outputs/2026-06-bassam-fattouh-makeup/email-html/emails.spec.json (emails[2], the e2 AR block: subject, subject_alts[1], headline, body[1]). Re-rendered with email_render.py. The renderer reported house-style clean and e2.ar now reads consistently masculine across headline, body, and CTA, matching e1, e3, and e4.

No other copy was rewritten.

## Notes (passing, recorded for the record)

- After the fix, reader address is masculine and coherent across all 4 AR emails.
- Empowering framing holds: skill, time saved, and confidence framing (maharah tabni 3alayha, yu3tik thiqah, al-maharah la tubna bil-ta'jil bal bi-khutwah tabda'uha al-yawm), never deficit or shame.
- Claims discipline held. The class title in the copy ("Bassam Fattouh Teaches Makeup") matches the published title, and "one of the region's leading or most sought-after makeup artists" is supported by the published tagline and profile. No client names, brand lines, awards, lesson counts, prices, or accreditation language appear.
- Mechanical checks clean on the re-rendered files: no em dash, no en dash, no tatweel, Western numerals only, verified by a full glyph scan.
- RTL-safe: no ASCII punctuation adjacent to Arabic; the Arabic comma is used throughout.
- Each EN email carries exactly one primary CTA. The "More classes on Maharat" line is a section heading for the see-also class-cards module, not a competing call to action.

## Summary

AR: 4 PASS (1 fixed then passed), 0 FAIL outstanding.
EN: 4 PASS, 0 FAIL.
