# Reference: vizra-ai/claude-code-agents import evaluation (2026-06)

A research readout, not a decision. Produced via the `/research` path (research-scout plus
`build-vs-buy-eval`) in response to a request to import agents from
`github.com/vizra-ai/claude-code-agents` into the engine. It informs whether the engine
should adopt any of those agents, in whole or in part. The decision is Ahmed's and lands as a
`settings.json` and `agents/` change, made by a human, never by this readout.

No em dashes, Western numerals, factual and sourced. This is a proposal, not an adoption.

---

## The open item this addresses

Should the engine adopt agents from `vizra-ai/claude-code-agents`, the full set or a subset?
The request arrived as two `cp` commands (first `marketing/copywriter.md`, then "the rest").
A direct copy skips the adoption gate in principle 3 of `CLAUDE.md` and the `settings.json`
allowlist note, so it was held for evaluation rather than run.

## What the repo actually is

Source: `github.com/vizra-ai/claude-code-agents`, default branch `main`, read on 2026-06-08
via the GitHub git-trees API (full manifest) plus one full file read, `marketing/copywriter.md`.
59 agent files across 9 folders. Only the `marketing/` folder is in this engine's domain.

| Folder | Count | Domain | What they are |
|---|---|---|---|
| `architecture/` | 5 | software | api-designer, database-planner, feature-spec-writer, system-designer, tech-stack-advisor |
| `business/` | 6 | software/ops | business-model-analyzer, financial-planner, market-researcher, pricing-strategist, privacy-policy-writer, terms-writer |
| `code-quality/` | 6 | software | code-reviewer, documentation-writer, performance-optimizer, refactoring-expert, security-auditor, test-strategist |
| `communication/` | 6 | software | api-documenter, changelog-writer, presentation-builder, support-responder, team-communicator, technical-writer |
| `data/` | 5 | software | analytics-setup, dashboard-planner, data-visualizer, report-generator, sql-expert |
| `design/` | 8 | software/UI | brand-designer, color-specialist, design-system-builder, icon-designer, layout-designer, typography-expert, ui-designer, wireframe-creator |
| `devops/` | 5 | software | backup-planner, cost-optimizer, deployment-troubleshooter, error-investigator, monitoring-setup |
| `marketing/` | 7 | marketing | ad-copy-creator, blog-writer, copywriter, email-writer, landing-page-writer, seo-optimizer, social-media-creator |
| `product/` | 6 | software | accessibility-checker, competitor-researcher, feature-prioritizer, feedback-analyzer, user-story-writer, ux-reviewer |
| `research/` | 5 | software | best-practice-finder, library-evaluator, solution-architect, technology-researcher, trend-analyzer |

Read this way: 7 of 59 are marketing agents. The other 52 are a general software-engineering
pack (architecture, devops, code quality, data, product, UI design, technical communication,
research, business). They are built to help developers ship software, not to run an
Arabic-first marketing funnel.

## The incumbent: borrow before building, but here we already built

The borrow-before-building check is inverted in this case. The engine is not missing a
capability that needs a tool. It already has a complete, purpose-built 21-agent roster
(`agents/_AGENTS-INDEX.md`) with one named owner for every funnel stream and acquisition
channel, each grounded in `context/brand-voice.md`, wired to the quality gate, and Arabic-first.
So the real question is not "is there a tool for this," it is "does this external pack beat what
we already have for this brand." On the evidence below, it does not.

## The decisive filter: Arabic

For any generative, customer-facing candidate this is applied first, and a fail rules it out
regardless of every other column. All 7 marketing agents are customer-facing generative
agents. The one read in full, `marketing/copywriter.md`, fails on its face:

- English only, no Arabic anywhere. The body opens "You are a professional copywriter who
  helps developers create compelling marketing content." Wrong audience, wrong language.
- No Modern Standard Arabic, no Gulf-familiar wording, no Thmanyah tone, no RTL handling.
- No mechanical rules: nothing on em dashes, Western numerals, or tatweel.
- Approach step 4 is literally "create urgency and scarcity when appropriate." That is
  deficit and pressure framing, which the brand voice rules out ("plain, confident,
  empowering. Never deficit-framed").
- Runs on `haiku` and self-grants `Bash`, broader than the engine's reasoning-only copywriters
  (`Read, Write, Edit, Grep, Glob`).

The other 6 marketing agents (`ad-copy-creator`, `blog-writer`, `email-writer`,
`landing-page-writer`, `seo-optimizer`, `social-media-creator`) are the same family and the
same size class. The Arabic gate is recorded as fail for the marketing bucket. A full per-file
read would confirm rather than change this, see open items.

## Criteria weights and must-have flags

| Criterion | Weight (1 to 5) | Must-have / nice-to-have |
|---|---|---|
| Arabic (decisive, generative) | hard gate, above weighting | must-have (hard gate) |
| SOP fit (marketing domain, brand voice, QA-gate wiring) | 5 | must-have |
| GCC/PDPL data fit | 2 | nice-to-have (local files, no data egress) |
| Cost vs volume | 1 | nice-to-have (repo is free) |
| Integration effort | 2 | nice-to-have |
| Lock-in / exit | 1 | nice-to-have (plain markdown, no lock-in) |
| Maturity / support | 2 | nice-to-have |

## Scored shortlist (by bucket)

Scored 1 to 5 per criterion. A failed must-have rules the bucket out regardless of total. For
the generative buckets a failed Arabic gate is a hard no, applied before weighting.

| Candidate bucket | Arabic (decisive) | SOP fit | GCC/PDPL | Cost | Integration | Lock-in | Maturity | Must-have failed? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `marketing/` copy agents (copywriter, ad-copy-creator, email-writer, landing-page-writer) | fail | 1 | n/a | 5 | 4 | 5 | 2 | yes (Arabic + SOP fit) | Collide with copywriter-ar, copywriter-en, lifecycle-architect, conversion-engineer. No brand rules, no QA wiring, deficit framing present. |
| `marketing/` channel agents (blog-writer, seo-optimizer, social-media-creator) | fail | 1 | n/a | 5 | 4 | 5 | 2 | yes (Arabic + SOP fit) | Collide with content-marketer, seo-specialist, organic-social. Same generic, English, ungrounded shape. |
| Off-domain software-engineering agents (52, all other folders) | n/a | 1 | 2 | 5 | 4 | 5 | 3 | yes (SOP fit) | Not marketing capabilities. No place in a marketing engine. Would pollute the roster and the orchestrator's dispatch. |

## Where the marketing agents collide with the existing roster

Every stream they touch already has exactly one named, Arabic-first owner. Importing these
creates duplicate ownership and ambiguous routing, which the roster is explicitly designed to
avoid ("every stream and entry point has a named owner. No stream is silently held").

- `ad-copy-creator`, `copywriter`, `email-writer`, `landing-page-writer` -> `copywriter-ar`
  and `copywriter-en` (stream 4), with email also touching `lifecycle-architect` (stream 7)
  and landing pages also touching `conversion-engineer` (stream 6).
- `blog-writer` -> `content-marketer`.
- `seo-optimizer` -> `seo-specialist`.
- `social-media-creator` -> `organic-social`.

A note on the `design/` folder: `brand-designer`, `color-specialist`, and `typography-expert`
read as marketing-adjacent by name, but they are UI and product-design agents. They do not
carry the Maharat visual constants (#141414, #1A1A1A, emerald #009975) and would muddy the
brand-visual ownership that sits with `creative-director` and `designer`.

## Recommendation (one path)

Do not adopt, whole or in part. Keep the existing 21-agent roster.

Rationale: the 7 marketing agents fail the decisive Arabic gate and the SOP-fit must-have, and
they collide with owners the engine already has. The other 52 are software-engineering agents
with no role in a marketing engine. Nothing in the pack does a job the roster does not already
do better and on-brand for this audience. The honest build-vs-buy verdict is build/keep, which
here means the work is already built.

If a specific capability gap is ever identified (for example a customer-support responder, a
capability the roster does not currently own), the path is to spec a purpose-built Maharat
agent through the normal QA path, grounded in `brand-voice.md` and wired to the gates, not to
copy a generic English agent in. At most, a vizra file is reference inspiration, never a
drop-in.

This is a proposal. Adoption requires Ahmed's approval and a human-made change to
`settings.json` and `agents/`.

## Open items that block a final decision

- License compatibility. Resolved: the repo is MIT (Copyright Vizra AI, 2024). Reuse and
  adaptation are permitted, the only obligation is keeping the copyright and permission notice
  if a substantial portion is copied verbatim. No vizra text was copied into the engine.
- Sampling depth. This pass read the full 59-file manifest plus one agent file in full
  (`marketing/copywriter.md`). A full per-file read and a real Arabic-output test on each
  marketing agent is the next step only if Ahmed wants to pursue a specific candidate. It is
  expected to confirm, not overturn, the Arabic-gate fail.
- Capability gap. Four genuine gaps were identified and chosen to fill in the working session
  below: accessibility, competitor teardown, feedback and review mining, and trend scanning.
  See the decision log.

## Decision log (2026-06-08 working session)

Worked through the 59 agents one by one with the requester. Outcome:

- Dropped wholesale, no marketing relevance: `architecture` (5), `code-quality` (6),
  `devops` (5). 16 agents, not adopted.
- `marketing` (7): not adopted. Each collides with an existing Arabic-first owner
  (copywriter-ar, copywriter-en, content-marketer, seo-specialist, organic-social) and fails
  the Arabic and brand-voice gate.
- The other 36 (`design`, `business`, `communication`, `research`, `product`, `data`):
  reviewed individually. Most duplicate an existing owner; several breach a hard rule
  (`pricing-strategist` would invent price against principle 1; `financial-planner`,
  `business-model-analyzer`, `presentation-builder`, `feature-prioritizer` touch the
  fundraising and roadmap guardrail; `brand-designer` and `color-specialist` compete with the
  locked brand); the rest are out of domain. None adopted as a drop-in.
- Four genuine gaps chosen to fill, built as purpose-built Maharat work, not imports:
  1. Accessibility: new agent `agents/accessibility-reviewer.md`, the a11y gate on streams 6
     and 7, wired alongside design-qa, before brand-qa.
  2. Competitor teardown: new agent `agents/competitor-analyst.md`, cross-cutting, feeds
     strategy-lead.
  3. Feedback and review mining: extension of `analytics-reporter` (coordinating with
     aso-specialist and organic-social), with a no-personal-data rule on quoted verbatims.
  4. Cultural and market trend scanning: extension of `strategy-lead`, feeding content-marketer.
- Nothing from vizra was copied in. MIT permits using the files as reference while building the
  Maharat versions. The first set merged in PR #5. Follow-ups since implemented: the
  `accessibility-qa` skill is packaged (`skills/accessibility-qa/`, SKILL plus evals and
  fix-list) and wired into `runtime/verification.md`, `runtime/stream-ownership.md`, and the
  roster. The one-line accessibility entry on the `CLAUDE.md` gate list is still pending: the
  constitution edit is left to Ahmed, and the harness blocked it here as a self-modification.

## Capability fold pass (2026-06-08)

Swept the non-conflicting agents in design, marketing, business, communication, research,
product, and data, and folded each genuinely additive, non-conflicting capability into the
existing owner rather than adding agents. New folds this pass:
- `designer`: a reusable design-system and template kit (from design-system-builder).
- `conversion-engineer`: page wireframe, user flow, and conversion usability review (from
  wireframe-creator and ux-reviewer), distinct from the designer's visual and the a11y gate.
- `analytics-reporter`: dashboard and report-visualization specs (from dashboard-planner and
  data-visualizer).

Already covered by earlier work: accessibility (accessibility-reviewer), competitor teardown
(competitor-analyst), feedback and review mining (analytics-reporter), cultural and market
trends (strategy-lead). Skipped as conflict or pure duplicate: the marketing folder (owned by
the copywriters, content-marketer, seo-specialist, organic-social), pricing-strategist,
financial-planner, business-model-analyzer, presentation-builder, feature-prioritizer,
brand-designer, color-specialist, and the software-only agents. Customer support
(support-responder) is a new function with no owner to extend; it would need its own
Arabic-first agent if wanted, not a fold.

---

Envelope: campaign_id cross-cutting. produced_by research-scout plus build-vs-buy-eval, via
`/research`. stream cross-cutting research. status draft, proposal pending Ahmed. qa
build-vs-buy checklist self-check passed. brief_refs none, no active campaign brief. This
readout proposes, it does not adopt or wire anything.
