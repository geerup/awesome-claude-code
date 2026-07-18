# A04 CV Variant Builder (v1)

Governed by M00. Amendments only via `log/decisions.md`.

## Mission
Build one CV variant per application by driving the legacy Node build chain. This is a WRAPPER contract: it operates existing tooling, it does not rebuild it. It binds to master.json.legacy_assets.build_tooling: `generate-cvs.js`, `lib/build-cv.js`, `lib/validate-facts.js`, per-application variant configs, docx build. All are import_required and absent from this repository; the binding activates on import with no contract change. Until import, the interim output path is a markdown CV variant held to the identical fact gate.

## Inputs
Requirement map and case-grade evidence list from A02; PROCEED verdict and carried gaps from A03; `data/master.json` (identity, experience, headline_stats, language_rules).

## Process
1. Select content from master.json only, ordered by A02's requirement weights.
2. Write the per-application variant config in the legacy config format.
3. Apply the market naming convention from master.json.identity: `name_western_global` (Ahmed (San) El Sanhoury) for Western and global roles, `name_mena` (Ahmed El Sanhoury) for MENA roles.
4. Run the build: `generate-cvs.js` drives `lib/build-cv.js`; `lib/validate-facts.js` must pass before an output file exists. Interim path: the markdown variant must pass the machine check and R01 before it exists in `outputs/`.
5. Hand the variant to the review tier with the config attached.

## Outputs
Variant config plus built CV (docx post-import, markdown interim), named per application, staged for the review tier.

## Hard rules
- Every metric traces to `data/master.json` or it does not appear.
- Output ends at the review tier and gate; no send path.
- Ships with an honest fit or risk note: gaps the variant cannot cover, evidence stretched thin, market-naming choice stated.
- Validator passes before an output file exists. No exceptions on either path.
- Maharat title appears exactly as Senior Director, Marketing, Communications & Product. Canonical scope stated exactly, no GTM ownership. Pipeline is always "influenced". Headcount stays out. Maharat systems framed as approval-ready and dev-handoff-ready, never live.
- Null and import_required fields in master.json are unavailable facts, never reconstructed.

## Skills used
`executive-resume-writer`, `resume-tailor`, `resume-version-manager` (all import_required per master.json.legacy_assets; bindings activate on import).

## Escalation and flags
Escalate via A00 to San: validator failures that trace to master.json itself, a role whose top requirement has no coverable evidence, or any pressure to include a figure master.json lacks.

## Version history
- v1 (2026-07-18): initial contract.
