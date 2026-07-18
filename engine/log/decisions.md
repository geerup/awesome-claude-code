# Decisions log

Binding amendments, overrides, and stated assumptions. Newest first. Format: date, type (AMENDMENT | OVERRIDE | ASSUMPTION | FLAG), scope, files touched.

## 2026-07-18, OVERRIDE, San ruled the open conflicts and approved the gate packs
San: "All good on suggestions proceed." Rulings applied: CV is authoritative over the dashboard wherever they conflict (Goodwall 2M members, growth via paid plus lifecycle); the "3x to 3M" shorthand stands with the precise 2,810,000+ stored alongside; Arabic rendering أحمد السنهوري confirmed; Director-title-acceptable-when-scope-is-senior is now a standing rule. All twelve gated pack files flipped to SAN APPROVED; publishing, sending, and submitting remain manual acts by San, no auto-send path exists. Still open: relocation or remote stance for MENA-market roles.
Files: engine/data/master.json (v1.2.0), engine/skills/arabic-adaptation.md, engine/outputs/gated/*.

## 2026-07-18, AMENDMENT, Domain T added: technical portfolio integrated
San: "include the out of scope." CLAUDE.md and PROJECTS.md committed verbatim under engine/tech-portfolio/ after passing their own sanitization scan (all pattern hits are the rulebook quoting its own scan patterns; no live secrets). A24 Tech Portfolio Agent wraps them. Domain T runs on CLAUDE.md's rules, not brand.json; shared law is the human gate and the honesty rule. Phase 0 inventory written to tech-portfolio/STATUS.md: owner choice and all source files still needed from San; BUILD-status repos (ansible-homelab, monitoring-stack, backup-restic) are scaffoldable in-session on San's word. M00 v2 should formalize the fourth domain; until then this entry is the authority.
Files: engine/tech-portfolio/*, engine/agents/A24-tech-portfolio-v1.md, engine/data/master.json.

## 2026-07-18, AMENDMENT, San approved the plan; source import pass 1 applied
San: "approve the plan and start working," with five files supplied. master.json bumped to v1.1.0, status APPROVED_TO_BUILD. Imported: Ahmed_El_Sanhoury__CV_5.pdf (all titles, dates, wins, skills, speaking, testimonials), careerstatsdashboard.html (50 source-verified stats, Sprout/Salesforce/Meltwater/YT Studio/GA4/LinkedIn exports), canonicalrolejoblisting.md (scope artifact). Gated packs remain individually PENDING SAN APPROVAL.
Files: engine/data/master.json, engine/data/brand.json.

## 2026-07-18, AMENDMENT, Title and base corrected from CV, patched in one pass
Title: Senior Director, Marketing, Communications & Product, Maharat (CV) replaces Senior Director of Marketing and Communications (M00). Base: Tallinn, Estonia (CV and dashboard) replaces the engine's wrong Dubai assumption; MENA stays the primary target market. One word from San reverses the title amendment.
Files: engine/data/master.json, engine/data/brand.json, outputs/gated/application-001/{cv-variant,jd-analysis,fit-verdict,outreach,cover-letter}.md, outputs/gated/brand-001/linkedin-profile-refresh.md, outputs/gated/content-week-001/longform-001.md.

## 2026-07-18, FLAG, Conflicts awaiting San's ruling (no output uses these until ruled)
1. Goodwall: CV says 2M members, dashboard says 1M; CV credits paid plus lifecycle, dashboard credits community over paid. 2. Canonical social shorthand "3x to 3M" vs Sprout-verified peak 2,810,000+; shorthand kept as San's own CV phrasing. 3. The reconstructed Canonical listing uses a different title than the CV; CV wins. Full list in master.json meta.conflicts.
Files: engine/data/master.json.

## 2026-07-18, FLAG, Out-of-scope holdings: technical portfolio project
CLAUDE.md and PROJECTS.md describe a separate public-repo portfolio (homelab, uConsole, monitoring, Tor tooling) for NOC/sysadmin/DevOps/SOC roles under san-media-tech. Outside M00's three domains; nothing built; files not committed here because they reference private infrastructure. Held for San's direction; relevant to A14 only as systems-builder evidence.
Files: engine/data/master.json (out_of_scope_holdings).

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
