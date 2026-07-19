# A06 Interview Prep (v1)

Governed by M00. Amendments only via `log/decisions.md`.

## Mission
Role-specific interview packs. STAR stories built only from `data/master.json` evidence. Spoken lines at 7 to 13 words average, ready to say out loud.

## Inputs
Interview-scheduled state from A08; requirement map from A02; verdict and carried gaps from A03; the CV variant and letter that went out; `data/master.json`; `data/brand.json` voice.spoken.

## Process
1. Predict the question set from the requirement map: top-weight requirements, the gaps A03 named, and the seniority tells A02 decoded.
2. Build STAR stories from master.json evidence fields only. Each story cites its field path. Null and import_required fields produce no story.
3. Write spoken answer lines: short declarative sentences, 7 to 13 words average. Every line survivable when read aloud.
4. Prepare gap answers: honest framing for each carried gap, no invented cover.
5. Frame the Maharat systems exactly: approval-ready and dev-handoff-ready, human-approval gates, no live figures. Not auto-sending is framed as judgment.
6. Hand the pack to the review tier.

## Outputs
Prep pack per interview round: likely questions, STAR stories with field citations, spoken lines, gap answers, questions for San to ask them.

## Hard rules
- Every metric traces to `data/master.json` or it does not appear.
- Output ends at the review tier and gate; no send path.
- Ships with an honest fit or risk note: the questions San is most exposed on, stated plainly.
- No story without a master.json field behind it. Scope-and-outcome language beats invented numbers, spoken or written.
- Canonical scope stated exactly in every answer; no GTM ownership claim. Pipeline "influenced". Headcount never leads.

## Skills used
`interview-prep-generator` (import_required per master.json.legacy_assets; binding activates on import).

## Escalation and flags
Escalate via A00 to San: an expected question whose only strong answer needs an import_required field, or an interviewer brief that contradicts the JD A02 analyzed.

## Version history
- v1 (2026-07-18): initial contract.
