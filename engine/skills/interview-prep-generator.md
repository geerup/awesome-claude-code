# interview-prep-generator (v1)

Governed by M00. Used by: A06. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import.

## Purpose
Build an interview pack for a specific role: STAR stories drawn from master.json, likely questions from the A02 requirements map, and spoken answer lines calibrated to San's delivery.

## Method
1. Ingest the A02 requirements map and gap list for the target role.
2. Select STAR stories only from facts in master.json; each story cites its source field.
3. Write spoken answer lines as short declarative sentences, 7 to 13 words average.
4. Script the Maharat systems story at its true state: approval-ready and dev-handoff-ready, with the human-approval gate framed as judgment.
5. Prepare gap responses: name the gap plainly, bridge to verified adjacent strength. Candor over diplomacy.
6. Add likely pushback questions with one-line counters, then stage the pack to the gate.

## Rules
- Every metric spoken aloud traces to data/master.json or it does not appear in a script.
- Canonical scope stated precisely in any GTM question: partnered with product marketing, regional marketing, and PMs; did not own GTM.
- Pipeline is always "influenced" in every answer, never "sourced" or "generated".
- No answer leads with team size; headcount stays out of stories.
- Roles with null dates in master.json get no dated anecdotes until import.

## Eval cases

### E1
**Input:** Draft STAR story claims "cut CAC 30% at Mindvalley".
**Expected:** Flagged; no such figure exists in master.json; story rebuilt on scope-and-outcome language or dropped.
**Fail if:** The 30% figure survives in any script line.

### E2
**Input:** Draft answer runs long: "So what I essentially did in that particular situation was take full ownership of the entire go-to-market motion across every region simultaneously."
**Expected:** Rewritten into short declarative lines averaging 7 to 13 words, with the GTM ownership claim removed.
**Fail if:** Sentence length ignores the spoken calibration or GTM ownership stands.

### E3
**Input:** Interviewer question in the pack: "What results did the Maharat agent system produce?"
**Expected:** Scripted answer states approval-ready and dev-handoff-ready, cites scale numbers as scope proof, frames the gate as judgment.
**Fail if:** Any live performance figure or "live in production" claim appears.

### E4
**Input:** Question targets pipeline contribution at a prior role.
**Expected:** Answer uses "influenced" for all pipeline language.
**Fail if:** "Sourced" or "generated" appears in a pipeline answer.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
