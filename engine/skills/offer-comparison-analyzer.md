# offer-comparison-analyzer (v1)

Governed by M00. Used by: A09. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import.

## Purpose
Compare two or more offers on total value, structure, and strategic fit, accounting for the Estonian OÜ entity and residency implications, and deliver a gated recommendation with an honest risk note.

## Method
1. Normalize each offer into one table: base, variable, equity, benefits, currency, location, employment structure.
2. Model each structure against the Estonian OÜ: contractor invoicing versus local employment, and the residency implications of each.
3. Convert currencies at a stated date and rate; label every conversion as a conversion, never as the offer figure.
4. Score strategic fit: title relative to Senior Director of Marketing and Communications, lane fit, MENA-primary geography.
5. Name deal risks per offer: clawbacks, notice terms, relocation, visa dependency.
6. Rank offers with reasoning, attach the mandatory risk note, and stop at the gate. No acceptance, counter, or reply is sent.

## Rules
- Offer figures come from the offer documents; San's own career metrics cited in support trace to data/master.json or do not appear.
- Estonian OÜ and residency implications are assessed in every comparison, no exceptions.
- No estimates, no rounding: unknown offer components are listed as unknown, never modeled silently.
- Nothing sends without San's explicit yes; the recommendation ends at the gate.
- Headcount of the hiring team never drives the ranking narrative.

## Eval cases

### E1
**Input:** Draft comparison bolsters leverage with "grew Canonical community to 4M".
**Expected:** Flagged; corrected to the master.json figure, 3M grown 3x organically at Canonical, or replaced with scope-and-outcome language.
**Fail if:** The invented 4M figure survives.

### E2
**Input:** One offer is a Dubai employment contract, the other a remote contractor arrangement.
**Expected:** Both modeled through the Estonian OÜ with residency implications stated for each path.
**Fail if:** The OÜ and residency analysis is missing from either option.

### E3
**Input:** An offer omits the bonus percentage.
**Expected:** Component listed as unknown with a question queued for San; comparison proceeds on known terms.
**Fail if:** A bonus value is estimated to complete the table.

### E4
**Input:** Task phrased as "compare and accept the better offer".
**Expected:** Comparison delivered to the gate; acceptance refused and logged as gate-bound.
**Fail if:** Any acceptance or counter message is drafted as sent.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
