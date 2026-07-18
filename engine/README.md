# San Engine

Governed multi-agent system for Ahmed (San) El Sanhoury. Four domains: career growth, personal brand, content production, and the technical portfolio (Domain T, added by logged amendment 2026-07-18). `M00.md` is the master contract; Domain T runs on its own `tech-portfolio/CLAUDE.md` with the human gate and honesty rule shared.

## Layout
```
M00.md              master contract, governs everything below
data/master.json    canonical facts, single source of truth (status: PENDING_SAN_APPROVAL)
data/brand.json     voice rules, banned list, positioning, pillars, audiences
agents/             27 versioned contracts: A00 coordinator, A01-A10 career, A11-A16 brand, A17-A23 content, R01-R03 review tier
skills/             knowledge files, each with 3+ eval cases; failing skills are blocked
pipelines/          P01 application, P02 brand refresh, P03 content week
evals/              machine_check.py (tier one) and llm-qa-rubric.md (tier two)
outputs/gated/      packs waiting at the human-approval gate
log/decisions.md    binding amendments, overrides, stated assumptions
```

## Governance in one paragraph
Every output passes the machine pass (`python3 evals/machine_check.py <file>`), then LLM QA review by R01, R02, R03 (reviewers surface defects only; writers fix; a second review confirms), then stops at the gate. Nothing publishes, sends, submits, or spends without San's explicit yes, logged in `log/decisions.md`. No auto-send path exists in this codebase.

## Current state (2026-07-18)
- master.json at v1.2.0, APPROVED_TO_BUILD; CV and 50-stat dashboard imported; all conflicts ruled by San (CV authoritative); gated packs SAN APPROVED, publishing manual by San.
- Standing rules live in `master.json.standing_rules`. One open input: relocation or remote stance for MENA-market roles.
- Domain T (`tech-portfolio/`) integrated: 12-repo catalog, A24 contract, Phase 0 inventory in STATUS.md awaiting San's owner choice and source files; BUILD repos scaffoldable on request.
- Still import_required: the Node CV build chain, 8 legacy skill configs, portfolio HTML surfaces, linkedin-copy.md, the seven case study files.

## First actions for San
1. Set the relocation/remote stance (feeds A03 and A09).
2. Domain T: choose the GitHub owner and supply source files for homelab/uconsole, or say the word to scaffold the BUILD repos now.
3. Import the remaining source-project assets named in `master.json.legacy_assets`.
