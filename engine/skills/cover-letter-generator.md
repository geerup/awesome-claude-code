# cover-letter-generator (v1)

Governed by M00. Used by: A05. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import.

## Purpose
Write a cover letter as a case study: one verified case, chosen for the role's sharpest requirement, argued in executive register and staged to the gate.

## Method
1. Read the A02 requirements map; pick the single requirement the letter must win.
2. Select exactly one case from master.json that proves it; one case per letter, no exceptions.
3. Structure: the company's problem as read from the JD, the case (context, decision, verified outcome), the bridge to their situation.
4. Set naming by region: "Ahmed (San) El Sanhoury" Western and global, "Ahmed El Sanhoury" MENA; note the recruiter-routed or network-referred path in the opening.
5. Trim to one page equivalent; every sentence carries a role-specific noun, a verified number, or a single framing line.
6. Attach the honest fit note, run the banned-list sweep, stage to the gate unsent.

## Rules
- One case per letter; a second story is a defect, never added for safety.
- Every metric traces to data/master.json or it does not appear; scope-and-outcome language beats invented numbers.
- Maharat case letters state approval-ready and dev-handoff-ready; the gate is framed as judgment, never as a limitation.
- Canonical case letters use the exact scope line and never imply GTM ownership; pipeline is always "influenced".
- No cold-portal letters for companies over 50 people; channel is verified before drafting.

## Eval cases

### E1
**Input:** Draft letter cites "grew organic reach 5x at Canonical".
**Expected:** Flagged; corrected to the master.json figure, 3M grown 3x organically, or replaced with scope-and-outcome language.
**Fail if:** The invented 5x figure survives.

### E2
**Input:** Draft letter stacks the Canonical community case and the Maharat systems case.
**Expected:** Reduced to the one case that best matches the role's sharpest requirement; the other cut.
**Fail if:** Two cases remain in the letter.

### E3
**Input:** Target role is a governed-AI marketing leadership post; letter uses the Maharat case.
**Expected:** System described in the agentic register with scale numbers as scope proof and the human-approval gate as the judgment credential.
**Fail if:** Any live performance figure or banned-word register appears.

### E4
**Input:** Letter addressed for a cold application to a 300-person company's portal.
**Expected:** Drafting refused on channel grounds; flagged to A00 with the banned-channel rule cited.
**Fail if:** The letter is produced for the banned channel.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
