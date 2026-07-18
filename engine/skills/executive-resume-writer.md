# executive-resume-writer (v1)

Governed by M00. Used by: A04. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import. Wraps the legacy build chain (generate-cvs.js, lib/build-cv.js, lib/validate-facts.js) once imported.

## Purpose
Write the master executive resume: Senior Director level, positioning-led, every line traceable to master.json, built to survive R01, R02, R03 review and reach the gate clean.

## Method
1. Read master.json and brand.json in full before drafting.
2. Open with the positioning sentence recast for the resume summary; one lane named, one framing line only.
3. Build experience entries: Maharat 2025 to Present first, Canonical 2022 to 2025 second; null-dated roles appear without dates until import.
4. Write bullets on verified facts: budgets per role, the Maharat systems at approval-ready and dev-handoff-ready state, Canonical scope stated exactly.
5. Place social proof: 3M grown 3x organically under Canonical; 10M+ only as a career combined line in the summary.
6. Run the banned-list sweep from brand.json; trim every padded sentence; attach the risk note and stage to the gate.

## Rules
- Every metric traces to data/master.json or it does not appear. No estimates, no rounding.
- Title invariant: Senior Director, Marketing, Communications & Product, Maharat. Never abbreviated, never downgraded.
- Canonical scope: led marketing communications, content marketing, and social media campaigns; partnered with product marketing, regional marketing, and PMs; did not own GTM.
- No bullet opens with Boosted, Achieved, or Delivered; no em dash characters; headcount stays out.
- Naming per audience: "Ahmed (San) El Sanhoury" Western and global, "Ahmed El Sanhoury" MENA.

## Eval cases

### E1
**Input:** Draft bullet reads "Managed $500K budget and 12-person team at Canonical".
**Expected:** Flagged; budget corrected to the master.json $250K, team size removed entirely.
**Fail if:** The invented budget or any headcount lead survives.

### E2
**Input:** Draft Maharat bullet claims "system now runs live campaigns with measurable ROAS".
**Expected:** Rewritten to approval-ready and dev-handoff-ready state; scale numbers cited as scope proof; gate framed as judgment.
**Fail if:** Any live-state or performance figure remains.

### E3
**Input:** Draft fills the Falcon entry with dates "2016 to 2018" for visual completeness.
**Expected:** Dates removed; entry ships undated with an import note in the risk note.
**Fail if:** Any reconstructed date appears for a null-dated role.

### E4
**Input:** Draft summary opens with "Results-driven marketing leader with a proven track record".
**Expected:** Rewritten to the positioning register with a role-specific noun and verified proof.
**Fail if:** Generic filler survives the trim pass.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
