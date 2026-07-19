# positioning-audit (v1)

Governed by M00. Used by: A11, R03.

## Purpose
Audit any output, in any domain, against the single positioning sentence and the two lanes, and name the drift precisely so the writer can fix it.

## Method
1. Read the full piece plus its calendar slot metadata (pillar, audience) before judging a single line.
2. Test the piece against the sentence: "Builds the systems that run marketing, not just the campaigns." Every claim must serve it or stay silent.
3. Confirm exactly one lane: governed agentic marketing systems, or Arabic-first MENA growth (rooted in Socialeyez and BSocial work from 2014). Two lanes in one piece is drift.
4. Confirm exactly one audience: recruiters, CMOs, founders, or MENA operators. A piece aimed at everyone is aimed at no one; flag it.
5. Check seniority signal: Senior Director level throughout. Flag junior tells: task lists without judgment, tool worship, effort framed as achievement.
6. Verify every metric against data/master.json. Verify Maharat systems appear only as approval-ready and dev-handoff-ready, never live.
7. Output PASS, or a FLAG list naming each drift and the rule it breaks. Surface defects only, never auto-fix.

## Rules
- Fact gate: every metric traces to data/master.json or it does not appear.
- Maharat systems are NOT live. No ROAS, revenue lift, or any live performance figure. Scale numbers (21 agents, 4 swarm patterns, 73 skills) prove scope only.
- Agentic register, verbatim: "multi-agent content and campaign pipelines with human-approval gates."
- Not auto-sending is a governance credential, framed as judgment.
- A11 holds the sole veto short of San. R03 flags that overlap A11's veto defer to A11.
- Banned tokens and constructions per brand.json apply to the audit note itself.

## Eval cases

### E1
**Input:** A LinkedIn post pitches both agentic systems and Arabic-first MENA growth to "leaders everywhere."
**Expected:** FLAG for two lanes in one piece and no single named audience; require one lane, one audience.
**Fail if:** The audit passes the piece or narrows it to one lane while leaving the audience unnamed.

### E2
**Input:** A portfolio blurb claims the Maharat engine "drives 4x ROAS across live campaigns."
**Expected:** FLAG as a fabricated live figure; require reframe to approval-ready and dev-handoff-ready scope with scale numbers only.
**Fail if:** Any live performance figure survives the audit.

### E3
**Input:** A bio reads "Managed a 14-person team executing weekly content tasks."
**Expected:** FLAG headcount lead and junior tell; require systems-level framing serving the positioning sentence.
**Fail if:** The audit rewrites the line itself instead of flagging it for the writer.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
