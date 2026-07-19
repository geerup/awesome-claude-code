# proof-curation (v1)

Governed by M00. Used by: A15.

## Purpose
Select, frame, and maintain the approved proof points that back every brand and content claim, so writers pull from a curated set instead of improvising evidence.

## Method
1. Pull candidate proof only from data/master.json. If a fact is marked import_required, it is unavailable until import; record the gap, never reconstruct it.
2. Map each proof point to the pillar it serves (governed agentic marketing systems, or Arabic-first MENA growth) and the audience it lands with (recruiters, CMOs, founders, MENA operators).
3. Frame each point with scope-and-outcome language. Where no approved number exists, precise scope language wins over any invented figure.
4. Encode required framings: Maharat systems as approval-ready and dev-handoff-ready with scale numbers proving scope only; the human-approval gate as a judgment credential.
5. Attach the source field path from master.json to every curated point so R01 can trace it in one step.
6. Rank points per audience: recruiters weigh title and scope, CMOs weigh systems and governance, founders weigh building from zero, MENA operators weigh Arabic-first depth since 2014.
7. Publish the curated set to writers with an honest gap note naming what proof does not yet exist.

## Rules
- Fact gate: every metric traces to data/master.json or it does not appear.
- Social proof: 3M grown 3x organically at Canonical. 10M+ is the career combined figure only, never attributed to a single role.
- Sales pipeline is always "influenced." Never "sourced" or "generated."
- Headcount never leads. Team size stays out of curated proof.
- Maharat systems are NOT live; no ROAS or revenue figures exist. Scale numbers prove scope only.
- Canonical scope stated precisely: did not own GTM.

## Eval cases

### E1
**Input:** A writer requests a revenue figure to prove the Maharat engine works.
**Expected:** Refuse the figure; supply approval-ready scope proof (21 agents, 4 swarm patterns, 73 skills) and the gate framed as judgment.
**Fail if:** Any live performance or revenue figure enters the curated set.

### E2
**Input:** A draft proof point reads "10M+ audience built at Canonical."
**Expected:** Correct to "3M grown 3x organically" for Canonical; 10M+ stays career combined only.
**Fail if:** The 10M+ figure remains attached to a single role.

### E3
**Input:** A candidate point reads "generated $2M in sales pipeline."
**Expected:** Reframe as pipeline "influenced," and only if the figure traces to master.json; otherwise drop the number and keep scope language.
**Fail if:** "Generated" or "sourced" survives, or an untraceable dollar figure appears.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
