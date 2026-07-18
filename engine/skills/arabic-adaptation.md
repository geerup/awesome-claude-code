# arabic-adaptation (v1)

Governed by M00. Used by: A22.

## Purpose
Adapt approved-track pieces into native Gulf-register Arabic that carries the meaning and the positioning, as adaptation and never word-for-word translation.

## Method
1. Work only from approved-track pieces selected in the weekly calendar. Arabic is a first-class stream; every week ships at least one Arabic piece.
2. Extract the piece's core: one pillar, one audience (usually MENA operators), the proof points, and the line serving the positioning sentence.
3. Rebuild the piece in Gulf register from that core. Restructure hooks, idioms, and rhythm for how the audience actually reads and speaks. Example rendering of the positioning idea: "نبني الأنظمة اللي تدير التسويق، مو بس الحملات."
4. Keep every number exactly as it traces to data/master.json. Adaptation changes register and structure; it never touches figures. Example proof line: "مجتمع ٣ ملايين، نموّه أورجانيك ثلاث أضعاف في كانونيكال."
5. Use MENA naming throughout: "Ahmed El Sanhoury" (أحمد السنهوري, rendering pending San's confirmation, tracked in master.json.gaps), never the Western form with (San).
6. Anchor the piece in the Arabic-first MENA growth lane, rooted in Socialeyez and BSocial work from 2014, where the brief calls for it.
7. Submit the adaptation to the full review tier as a new asset: machine pass, R01, R02, R03, then the gate.

## Rules
- Adaptation, never word-for-word translation. Literal renderings are defects.
- Fact gate holds across languages: every metric traces to data/master.json or it does not appear.
- Maharat systems stay approval-ready and dev-handoff-ready in Arabic too. No live performance claims in any language.
- Gulf register, native. Modern Standard Arabic stiffness or Levantine and Egyptian colloquialisms are register defects.
- MENA naming: "Ahmed El Sanhoury." Social proof rules unchanged: 3M grown 3x organically at Canonical; 10M+ career combined only.

## Eval cases

### E1
**Input:** An adaptation renders an English post line by line, keeping English sentence order and idioms.
**Expected:** Flag as translation; rebuild from the core meaning in native Gulf register with a restructured hook.
**Fail if:** Word-for-word structure ships as an adaptation.

### E2
**Input:** The Arabic draft rounds "3M grown 3x" up to "أكثر من ٤ ملايين" for rhetorical effect.
**Expected:** Flag; restore the exact master.json figure. Numbers never change in adaptation.
**Fail if:** Any figure differs from its master.json source.

### E3
**Input:** An Arabic piece describes the Maharat engine as "يشتغل الحين ويحقق أرباح" (running now and generating returns).
**Expected:** Flag; reframe to approval-ready scope with the human-approval gate as the judgment story, in Gulf register.
**Fail if:** A live performance claim survives in the Arabic piece.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
