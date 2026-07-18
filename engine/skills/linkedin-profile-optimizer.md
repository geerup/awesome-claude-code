# linkedin-profile-optimizer (v1)

Governed by M00. Used by: A12. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import.

## Purpose
Produce headline, about, and experience copy for the ahmed-el-sanhoury profile that serves the positioning sentence and passes the fact gate, staged for San's approval.

## Method
1. Read master.json and brand.json; select audience emphasis from recruiters, CMOs, founders, MENA operators.
2. Draft the headline around the invariant title, Senior Director of Marketing and Communications, Maharat, plus one lane.
3. Write the about section: positioning first, then proof. Register for the agentic work: multi-agent content and campaign pipelines with human-approval gates.
4. Write experience entries only for roles with canonical dates: Canonical 2022 to 2025, Maharat 2025 to Present. Roles with null dates wait for import.
5. Place social proof: 3M grown 3x organically at Canonical; 10M+ as the career combined figure only, never per role.
6. Run the banned-list check from brand.json, attach the risk note, stage to the gate.

## Rules
- Every metric traces to data/master.json or it does not appear.
- Naming: "Ahmed (San) El Sanhoury" on the global profile surface; "Ahmed El Sanhoury" in MENA-targeted copy.
- Maharat systems are approval-ready and dev-handoff-ready, NOT live; scale numbers (21 agents, 4 swarm patterns, 73 skills) prove scope only.
- Not auto-sending is a governance credential; frame the gate as judgment.
- Headcount stays out; numbers are proof, never the headline.

## Eval cases

### E1
**Input:** Draft about section reads "drove 40% engagement lift at Maharat".
**Expected:** Flagged; no such figure exists in master.json and the systems are not live; replaced with scope-and-outcome language at approval-ready state.
**Fail if:** The 40% figure or any live performance claim survives.

### E2
**Input:** Draft experience bullet credits 10M+ audience to the Canonical role.
**Expected:** Flagged; 10M+ restored to career combined placement, Canonical carries 3M grown 3x organically.
**Fail if:** 10M+ remains attributed to a single role.

### E3
**Input:** Draft headline reads "Marketing Director at Maharat".
**Expected:** Corrected to the full invariant title, Senior Director of Marketing and Communications.
**Fail if:** The title is abbreviated or downgraded anywhere on the profile.

### E4
**Input:** Draft adds a Mindvalley entry with dates "2019 to 2021".
**Expected:** Dates removed; entry held until source import, since Mindvalley dates are null in master.json.
**Fail if:** Reconstructed dates appear for any null-dated role.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
