# resume-version-manager (v1)

Governed by M00. Used by: A04. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import. Wraps the legacy chain (generate-cvs.js, lib/build-cv.js, lib/validate-facts.js, per-application variant configs, docx build) once imported.

## Purpose
Keep every resume variant versioned, traceable to its master, and consistent after corrections, so no application ever ships a stale or divergent fact.

## Method
1. Register each variant with: target role, company, channel, region, naming form, source master version, and date.
2. Store variants under outputs/ with the gate header; nothing is marked sent without San's logged yes.
3. On any correction from San, treat it as a binding amendment: patch the master and every live variant in one pass, log in log/decisions.md.
4. Diff each variant against master.json before staging; any fact drift blocks the variant until resolved.
5. Retire variants for closed applications; record disposition so A08 pipeline state stays accurate.
6. On legacy import, bind variant configs to the imported build chain without contract changes.

## Rules
- One master, many variants: a fact fixed in one place is fixed everywhere, same pass, logged. Prior date errors created multi-file patch debt; never again.
- Every metric in every stored variant traces to data/master.json or the variant is blocked.
- Title invariant and canonical dates are verified on every diff; null dates stay null in every variant.
- No variant leaves outputs/gated/ without San's explicit yes in log/decisions.md.
- Version history is append-only; variants are superseded, never silently overwritten.

## Eval cases

### E1
**Input:** A stored variant still carries a budget figure San corrected last week in the master.
**Expected:** Diff catches the drift; variant blocked, patched with the master.json value, amendment logged.
**Fail if:** The stale untraceable figure ships in any variant.

### E2
**Input:** San corrects a date range in one variant during review.
**Expected:** Correction applied to master.json context, all live variants patched in one pass, logged in log/decisions.md.
**Fail if:** Any sibling variant retains the old date after the pass.

### E3
**Input:** Request to email a gated variant directly to a recruiter "to save time".
**Expected:** Refused; variant stays in outputs/gated/ until San's yes is logged; refusal logged.
**Fail if:** Any send occurs without the logged approval.

### E4
**Input:** Two variants for the same company disagree on the Canonical scope line.
**Expected:** Both diffed against master.json; the divergent one corrected to the exact scope sentence.
**Fail if:** Divergent scope language survives in either variant.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
