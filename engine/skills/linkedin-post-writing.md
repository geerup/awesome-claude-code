# linkedin-post-writing (v1)

Governed by M00. Used by: A18.

## Purpose
Write LinkedIn-native short-form posts that serve the positioning sentence for one named audience, with a hook that earns the read without hype.

## Method
1. Take the calendar brief: one pillar, one audience, one proof source in data/master.json. Refuse briefs missing any of the three.
2. Write the hook first: one specific, true line that creates a question in the reader's head. Hook without hype; no exclamation bait, no fake stakes.
3. Build the body in executive register: short paragraphs, one formulation per idea, every sentence carrying a role-specific noun, a verified number, or a single framing line.
4. Place numbers as proof inside the argument, never as the headline. The claim leads; the number backs it.
5. Describe the agentic work verbatim as "multi-agent content and campaign pipelines with human-approval gates." Frame the gate as judgment.
6. Close with one line that lands the positioning sentence's idea for the named audience. No engagement-bait questions.
7. Self-check against brand.json banned tokens and framings, then submit to machine pass, R01, R02, R03, and the gate.

## Rules
- Fact gate: every metric traces to data/master.json or it does not appear.
- Maharat systems: approval-ready and dev-handoff-ready only. No ROAS, revenue lift, or live figures. Scale numbers prove scope only.
- Every banned character, word, construction, and framing in brand.json applies in full: no em dashes, no banned vocabulary, no banned contrast constructions, no bullets opening with the banned verbs.
- Social proof: 3M grown 3x organically at Canonical; 10M+ career combined only. Pipeline "influenced." Headcount never leads.
- One pillar, one audience per post.

## Eval cases

### E1
**Input:** A draft opens "Our AI engine is already printing 5x ROAS."
**Expected:** Flag and rewrite: the engine is approval-ready and dev-handoff-ready; use scale numbers (21 agents, 4 swarm patterns, 73 skills) and the gate as the judgment story.
**Fail if:** Any live performance figure survives in the post.

### E2
**Input:** A draft hook reads "3M! 3x! Here's how we CRUSHED organic growth."
**Expected:** Rewrite to a specific, calm hook; keep the number inside the body as proof for the claim.
**Fail if:** The number stays in the headline or hype punctuation remains.

### E3
**Input:** A post for CMOs drifts into recruiter language about availability and title.
**Expected:** Flag the audience drift; hold the post to one audience with content shaped for CMO concerns.
**Fail if:** The post ships addressing two audiences.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
