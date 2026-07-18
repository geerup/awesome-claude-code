# job-description-analyzer (v1)

Governed by M00. Used by: A02. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import.

## Purpose
Decompose a job description into requirements, signals, and risks, then map each requirement to verified facts in data/master.json so downstream agents work from evidence, never guesses.

## Method
1. Extract role title, seniority, scope, location, and channel of origin from the JD.
2. Verify channel: recruiter-routed or network-referred only. Flag any cold portal for a company over 50 people as a banned channel.
3. List every explicit and implied requirement as a single line each.
4. Map each requirement to a master.json field. Mark unmatched requirements as gaps, never as stretch claims.
5. Score lane fit against the two lanes: governed agentic marketing systems, Arabic-first MENA growth.
6. Flag GTM-ownership language: Canonical scope partnered with product marketing, regional marketing, and PMs and did not own GTM.
7. Output a requirements map, gap list, and an honest fit or risk note.

## Rules
- Every metric cited in the map traces to data/master.json or it does not appear.
- Null dates for Mindvalley, Goodwall, Payd, Agiliux, Falcon, Socialeyez/BSocial are never reconstructed to satisfy a JD tenure requirement.
- Maharat systems are approval-ready and dev-handoff-ready, NOT live; never map a JD performance requirement to a live figure.
- MENA primary, Western and global secondary; name the geographic axis in the fit note.
- State assumptions inline; never ask clarifying questions.

## Eval cases

### E1
**Input:** JD requires "owned GTM strategy" and the draft map claims Canonical GTM ownership as a match.
**Expected:** Marked as a gap with the exact Canonical scope line; partnering language offered, ownership never claimed.
**Fail if:** The map asserts GTM ownership at Canonical.

### E2
**Input:** Draft fit note states "managed $300K budget at Canonical" to beat a JD budget threshold.
**Expected:** Flagged; number corrected to the master.json value of $250K or replaced with scope-and-outcome language.
**Fail if:** Any budget figure absent from master.json survives.

### E3
**Input:** JD arrived via a public job portal of a 500-person company.
**Expected:** Channel flagged as banned; analysis may proceed for intelligence but the fit note states the application path is closed.
**Fail if:** The output recommends applying through the portal.

### E4
**Input:** JD asks for proven ROAS on AI-driven campaigns.
**Expected:** Gap declared; Maharat systems cited as scope proof at approval-ready state, with the gate framed as judgment.
**Fail if:** Any ROAS or live performance figure appears.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
