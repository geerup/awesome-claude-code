# Decisions log

Binding amendments, overrides, and stated assumptions. Newest first. Format: date, type (AMENDMENT | OVERRIDE | ASSUMPTION | FLAG), scope, files touched.

## 2026-07-18, ASSUMPTION, Contract skeleton standardized on the full section list
A01 to A23 carry Mission / Inputs / Process / Outputs / Hard rules / Skills used / Escalation and flags / Version history. A00 and R01 to R03 keep the shorter governance skeleton they were seeded with; harmonizing them is a v2 amendment if San wants strict parity. Other standing calls: A08 defines a stall as no transition since the last weekly digest (a day-count threshold would be an invented number; San sets one when ready); A16 pitches ride the P02 review tier via A00; the weekly Arabic slot is encoded in both A17 and A22 with P03 controlling.
Files: engine/agents/*.

## 2026-07-18, FLAG, Arabic name rendering unconfirmed
أحمد السنهوري used in arabic-001 and the arabic-adaptation skill; a subagent draft had الصنهوري, standardized to السنهوري. San confirms or corrects; correction patches all files in one pass.
Files: engine/skills/arabic-adaptation.md, engine/outputs/gated/content-week-001/arabic-001.md, engine/data/master.json.

## 2026-07-18, FLAG, Build-session review cycle ran as designed
The tier-one machine pass flagged 77 items on the first proof-run sweep: 75 tokenizer false positives (agent IDs and pack names read as metrics), fixed in machine_check.py, and 2 real defects, fixed by the writers: post-001 named a banned live-metric term while denying it, and the cover letter misstated the 3M/3x figure as an endpoint claim. Final sweep: clean.
Files: engine/evals/machine_check.py, engine/outputs/gated/content-week-001/post-001.md, engine/outputs/gated/application-001/*.

## 2026-07-18, ASSUMPTION, Host repository is not the career-system project
M00 was run against a fork of `awesome-claude-code`, which contains none of the referenced legacy assets (no master.json sources, no Node CV build chain, no 19-skill config, no portfolio surfaces, no case study files). Treated as the fresh-repo path per M00's own run instruction. `engine/` built at repo root. All absent assets recorded in `master.json.legacy_assets` and `master.json.gaps`; wrapper contracts (A04, A12, A13, A19, A20) name their bindings and activate on import without contract changes.
Files: engine/* (initial build).

## 2026-07-18, FLAG, Phase 0 approval pending
The two source master.json files were unavailable, so the merge preserves both schema structures and populates only M00-documented facts. `master.json` carries status PENDING_SAN_APPROVAL. All proof-run outputs sit in `outputs/gated/` and nothing leaves the gate until San approves the schema and the outputs. Import of per-role wins, products, dates for Mindvalley/Goodwall/Payd/Agiliux/Falcon/Socialeyez is the first post-approval task; dates were left null rather than reconstructed (prior date errors created multi-file patch debt).
Files: engine/data/master.json.

## 2026-07-18, ASSUMPTION, Phase 1 proof run uses a marked sample JD
A01's live channels (recruiter-routed, network-referred) produce no real posting inside this build session. The proof run processes a synthetic JD clearly marked SAMPLE in `outputs/gated/application-001/`. Mechanism is proven end to end; first real application replaces it on arrival.
Files: engine/outputs/gated/application-001/*.
