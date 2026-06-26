# Rubric scorecard: 2026-07-summer-bassam-led-sale (copy stage)

Pre-gate self-check against `rubric.evals.json`. This is the loop check before the formal gate
stack (arabic-copy-qa, english-copy-qa, email-asset-qa, accessibility-qa,
compliance-privacy-check, brand-qa-reviewer, human gate). Scored after one loop fix.

## Machine layer (eval_runner.py)
PASS. No em or en dash, no tatweel, Western numerals only, no exclamation marks, SUM30 present
in every sale email, all sale terms flagged "PLACEHOLDER, HELD". Exit 0.

## Loop fix applied (round 1)
- E2 AR named the free first lesson "الماهر", an unverified Arabic title. Only the English title
  "The Talent" is page-cleared. Per the no-invented-claims rule, the Arabic title was removed
  (E2 AR now says "الدرس الأول"); the cleared English "The Talent" is kept. Re-scored after fix.

## Loop revisions applied (round 2, requester feedback)
- E1 (both languages): removed all announcement framing ("first online class", "for the first
  time", "now on Maharat"). Reframed to the practical payoff (you create your own looks, the skill
  stays with you). New subject EN "A look you can do yourself" / AR "إطلالة تصنعينها بنفسك".
- E2 subject sharpened to EN "It is technique, not products" / AR "التقنية، لا المنتجات".
- E3 subject set to EN "Build Real Skills This Summer" / AR "ابنِ مهارات حقيقية هذا الصيف".
- E4 reframed from inventory ("the full library") to transformation: EN "Learn any skill, all
  summer" / AR "تعلّم أي مهارة، طوال الصيف", body now outcome-led.
- E5-E7 subjects tightened to the masterclass reference register (front-loaded, no filler):
  "Summer of Skills, your offer" / "Your summer offer ends tomorrow" / "Last day for the summer
  offer" and the AR equivalents.
Machine checks re-run after round 2: PASS (exit 0). All per-email and per-sequence checks re-scored
all-pass; scores below reflect the revised copy.

## Per-email (after fixes)

| Email | objective | one-cta | subject | preheader | body-len | empowering/premium | claims | sale | cta-dest |
|-------|-----------|---------|---------|-----------|----------|--------------------|--------|------|----------|
| E1 Bassam hook | 5 | pass | pass | pass | pass | 5 | pass | n/a | pass (class) |
| E2 Bassam why+free | 5 | pass | pass | pass | pass | 5 | pass | n/a | pass (class) |
| E3 platform breadth | 5 | pass | pass | pass | pass | 4 | pass | n/a | pass (classes) |
| E4 self-development | 4 | pass | pass | pass | pass | 4 | pass | n/a | pass (plans) |
| E5 sale announce | 5 | pass | pass | pass | pass | 4 | pass | pass | pass (plans) |
| E6 ending tomorrow | 5 | pass | pass | pass | pass | 4 | pass | pass | pass (plans) |
| E7 last day | 5 | pass | pass | pass | pass | 4 | pass | pass | pass (plans) |

## Per-sequence

| Check | score | note |
|-------|-------|------|
| arc-integrity (2/2/3) | 5 | clean act transitions, no repeated value |
| urgency-escalation | 5 | E5 announce < E6 ending tomorrow < E7 today; bodies shorten to E7 |
| bilingual-parity | pass | AR and EN carry the same promise; AR uses feminine address on E1-E2 (beauty hook), EN is neutral. Language-appropriate, not a divergence. |
| voice-consistency | 5 | one Thmanyah voice across all 14 |
| cadence-suppression-flags | pass | cadence + suppression in brief/strategy; all sale terms flagged open |

Result: all checks pass, every quality score >= 4. Copy is ready for human review.

## Items to confirm at review / human gate (not blocking the copy)
1. Sale terms are placeholders: 30 percent, code SUM30, close 2026-07-06. Confirm or replace.
2. Free first lesson: EN "The Talent" is cleared; AR omits a title (says "الدرس الأول"). Add the
   official Arabic title if one exists.
3. Entry plan not named (E4-E7 say "your plan" / "خطة الاشتراك"). Confirm which plan leads.
4. E3 names only the three cleared instructors (Cedric Haddad, Elda Choucair, Ragheb Alama),
   others folded into "and more". Add Salam Dakkak, Kosai Khauli, Toufic Kreidieh only if cleared.
5. Gendered-address consistency in AR (E1 headline mixes forms) is for arabic-copy-qa to confirm
   at the formal gate.
6. Build-stage items (next phase): SUM30 Latin code RTL render test; hero imagery for E3-E7
   (platform/sale) is an asset open item; CloudFront assets stage to Ortto CDN before send.
