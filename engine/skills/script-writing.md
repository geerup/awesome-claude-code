# script-writing (v1)

Governed by M00. Used by: A21.

## Purpose
Write spoken-cadence scripts for video and interview settings: short declarative sentences a person can say on camera without sounding scripted.

## Method
1. Take the calendar brief: one pillar, one audience, one proof source in data/master.json.
2. Draft every line as speech. Short declarative spoken sentences, 7 to 13 words average. Read each line aloud; rewrite any line that trips.
3. Open on a specific true statement, never a hype claim. The first line earns the next ten seconds.
4. Carry one idea per beat. Cut every second formulation. A script beat holds a role-specific noun, a verified number, or one framing line.
5. Speak the agentic register verbatim where the work comes up: "multi-agent content and campaign pipelines with human-approval gates." Frame not auto-sending as judgment.
6. End on the positioning idea in plain speech, shaped for the named audience.
7. Run a cadence check: average words per sentence within 7 to 13, then submit to machine pass, R01, R02, R03, and the gate.

## Rules
- Fact gate: every spoken metric traces to data/master.json or it does not appear.
- Maharat systems: approval-ready and dev-handoff-ready, NOT live. No ROAS or revenue lines, ever. Scale numbers prove scope only.
- Sentence length is contract: 7 to 13 words average across the script.
- Social proof spoken correctly: 3M grown 3x organically at Canonical; 10M+ career combined only. Pipeline "influenced." Headcount never leads.
- Banned tokens per brand.json apply to spoken copy exactly as to written copy.

## Eval cases

### E1
**Input:** A script line reads "The engine already runs live campaigns and returns four times ad spend."
**Expected:** Flag; replace with approval-ready framing in spoken cadence, such as "I built it. Twenty-one agents. Nothing sends without my yes."
**Fail if:** Any live performance claim survives in the script.

### E2
**Input:** A draft beat runs 34 words across one sentence with three subordinate clauses.
**Expected:** Split into short declarative lines averaging 7 to 13 words; keep one idea per beat.
**Fail if:** The script averages outside 7 to 13 words per sentence.

### E3
**Input:** An interview script opens "I led a team of fifteen across four markets."
**Expected:** Flag the headcount lead; reopen on systems and judgment serving the positioning sentence.
**Fail if:** Team size leads any beat of the script.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
