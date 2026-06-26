# Maharat Marketing Engine: folder structure

> ADAPTED: This is the Brand & Career Engine, a personal-brand adaptation of the original
> Maharat Marketing Engine. The machine described below (agents, runtime, skills, SOPs, gates)
> is reused unchanged; the active facts are the `me` profile and the language is English-first.
> The original Maharat engine is preserved in full under `context/profiles/maharat/` (nothing
> was thrown out). Some Maharat-specific examples below now describe that archived reference
> profile. Authoritative current rules live in `CLAUDE.md` and `context/profiles/_README.md`.


The complete `.claude/` scaffold for the engine, the reusable agentic marketing machine.
A campaign is an input: hand the engine a brief and the same workflows produce
approval-ready work, behind a human gate. This file is the map of the whole tree.

Legend for the status column:
- `built` exists on disk and is complete enough to use
- `stub` exists as a placeholder, needs filling
- `todo` named in the architecture, not yet created

House rule across every file: no em dashes, no tatweel, Western numerals, empowering
framing, English-first (Gulf-familiar MSA, Thmanyah tone), never imply accreditation.

---

## The tree

This is a curated map, not a file-by-file listing. Folders that hold many files show the
shape and a count rather than every entry.

```
.claude/
├── CLAUDE.md                     Always-loaded operating rules (principles, brand, guardrails)
├── README.md                     Architecture, prompting strategy, MCP strategy
├── DOCUMENTATION.md              In-depth engine documentation (the long-form companion to this map)
├── RUNBOOK.md                    Claude Code end-to-end execution runbook
├── PATCHES.md                    Repo wiring edits applied during the build
├── KICKOFF-PROMPT.md             The standing kickoff prompt for a run
├── DRIVE-CLOSEOUT.md             Drive mining closeout record
├── STRUCTURE.md                  This file: the map of the whole tree
├── settings.json                 Permissions, MCP allowlist (add tools only as approved)
├── .mcp.json                     Committed MCP config (env-var only) for cloud sessions
│
├── context/                      Single source of truth (stable facts, not campaign data)
│   ├── 00-start-here.md          What we are building, and why
│   ├── 01-brand-brief.md       Maharat: product, audience, money, owned audience
│   ├── 02-objective-and-design.md  What the engine delivers, campaign-agnostic principle
│   ├── 03-workflow-map.md        The 9 streams and the SOP template
│   ├── 04-tools-and-access.md    The stack, with WORKSHOP open items
│   ├── brand-voice.md            English-first voice, the no-em-dash house style, visual constants
│   ├── organic-social-style.md   The organic social voice and format guide
│   ├── brainstorm-reconciliation.md   Corrections folded in from the 5 brainstorm docs
│   ├── miro-board-reconciliation.md   Board-only specifics + the single-class-buyer correction
│   ├── mining-plan-v2.md         Operational instructor-mining plan (supersedes the two below)
│   ├── drive-content-mining-plan.md   Design history for Drive mining
│   ├── instructor-mining-plan.md      Design history for instructor mining
│   ├── findings-email-platform.md     Email platform findings (Ortto named)
│   ├── findings-payments-and-partnerships.md   Payments and partnerships findings
│   ├── instructors/              Instructor registry: _CATALOG.md + per-instructor fact files (22 files)
│   └── marketing-super-team/     Reference personas and AI super-team notes (7 files)
│
├── briefs/                       Runtime inputs, one per campaign (the only per-campaign data)
│   ├── _TEMPLATE-campaign-brief.md    The blank a new campaign fills
│   ├── 2026-06-nonpayer-email.md      Non-payer lifecycle brief
│   ├── 2026-06-bassam-fattouh-makeup.md
│   ├── 2026-06-bassam-fattouh-bridal-makeup.md
│   ├── 2026-06-elda-choucair-marketing.md
│   └── 2026-07-skill-paths-soft-launch.md
│
├── agents/                       The team: 25 specialists, one per role (full roster in _AGENTS-INDEX.md)
│   ├── _AGENTS-INDEX.md          The roster: every agent, its stream, mode, model, reads, handoffs
│   ├── orchestrator.md           Reads the brief, holds the whole-funnel view, dispatches
│   ├── strategy-lead.md          Streams 1 to 2: intake, strategy, planning
│   ├── research-scout.md         Cross-cutting: research, borrow-before-inventing, build-vs-buy
│   ├── competitor-analyst.md     Cross-cutting: competitor teardowns that feed strategy
│   ├── creative-director.md      Stream 3: creative concepts, image direction, asset briefs
│   ├── designer.md               Stream 3: visual execution + design-qa
│   ├── copywriter-ar.md          Stream 4: English-first copy (primary)
│   ├── copywriter-en.md          Stream 4: English variants
│   ├── paid-build-engineer.md    Stream 5 (paid path): stage campaigns, never spend ungated
│   ├── web-design-director.md    Stream 6: web design direction (IA, UX flow, wireframes)
│   ├── web-designer.md           Stream 6: build-ready responsive spec + web-design-qa
│   ├── conversion-engineer.md    Stream 6: landing page and signup gate
│   ├── data-tracking-engineer.md Stream 6 events + stream 8 warehouse plumbing
│   ├── lifecycle-architect.md    Stream 7: email and WhatsApp sequences
│   ├── analytics-reporter.md     Streams 8 to 9: monitoring, reporting, learnings
│   ├── organic-social.md         Entry point C: organic acquisition and community
│   ├── performance-marketer.md   Paid channel strategy and performance marketing
│   ├── seo-specialist.md         Search engine optimization (AR + EN)
│   ├── content-marketer.md       Blog and content marketing
│   ├── aso-specialist.md         App marketing and App Store Optimization
│   ├── pr-comms.md               PR and communications
│   ├── brand-qa-reviewer.md      Cross-cutting verifier: brand QA, runs last
│   ├── compliance-privacy-reviewer.md   Cross-cutting verifier: compliance and privacy gate
│   ├── accessibility-reviewer.md Cross-cutting verifier: accessibility gate (pages, emails)
│   └── human-gate.md             The approval node (Ahmed), terminal stop before any send or spend
│
├── runtime/                      The conductor: how the team runs together
│   ├── README.md                 Read order and where the layer fits
│   ├── SWARM.md                  The 4 swarm shapes + the orchestrator loop
│   ├── stream-ownership.md       The 9-stream to agent to skill to SOP map, both entry points
│   ├── verification.md           The QA gate stack as hard stops
│   ├── handoff-contract.md       The structured artifact schema each stream passes downstream
│   ├── batch-mining-protocol.md  The unattended instructor-mining run contract
│   └── routines-docs-sync.md     The weekly docs-sync cloud routine (prompt + form settings)
│
├── skills/                       Grouped by stream + cross-cutting. Each skill (hub or sub) has the
│   │                             same shape: SKILL.md + evals/evals.json + templates/.
│   ├── 01-brief-intake/          Hub + brief-validate, kickoff-scope
│   ├── 02-strategy-planning/     Hub + audience-segmentation, offer-and-angle
│   ├── 03-creative-production/   Hub + creative-concepting, image-prompting
│   ├── 04-copywriting/           Hub + ad-copy, email-copy, subject-lines
│   ├── 05-build-launch/          Hub + paid-campaign-build, email-sequence-build
│   ├── 06-conversion-path/       Hub + landing-page, event-tracking
│   ├── 07-lifecycle-messaging/   Hub + segmentation-logic, nonpayer-email-flow, onboarding-sequence, event-sequence, winback-flow, promo-sequence
│   ├── 08-monitoring-optimization/  Hub + performance-readout, ab-test-plan
│   ├── 09-reporting-learning/    Hub + campaign-report, learnings-log
│   ├── web-design/               Stream-6 design hub + web-experience-direction, web-design-spec
│   ├── arabic-copy-qa/           Quality gate: Arabic copy
│   ├── english-copy-qa/          Quality gate: English copy
│   ├── design-qa/                Quality gate: visual design
│   ├── web-design-qa/            Quality gate: web surfaces
│   ├── accessibility-qa/         Quality gate: WCAG 2.2 AA on pages and emails
│   ├── compliance-privacy-check/ Quality gate: PDPL, consent, suppression, tracking
│   ├── build-vs-buy-eval/        Cross-cutting: weigh any tool on the build-vs-buy criteria
│   ├── instructor-marketing/     Hub + per-instructor packs (voice, templates, evals)
│   ├── organic-social/           Channel hub: organic content plan + community engagement
│   ├── paid-performance/         Channel hub: media plan, audience and bidding, paid optimization
│   ├── seo/                      Channel hub: keyword research, on-page, technical SEO
│   ├── content-marketing/        Channel hub: editorial calendar, article brief, distribution
│   ├── aso/                      Channel hub: store keywords, listing, creatives and experiments
│   └── pr-comms/                 Channel hub: press release, media list, announcement plan
│
├── commands/                     Slash commands
│   ├── new-campaign.md           /new-campaign: spin up a brief and compose a run
│   ├── research.md               /research: research-scout + build-vs-buy-eval
│   ├── mine-instructor.md        /mine-instructor: mine one instructor into a pack
│   └── mine-all-instructors.md   /mine-all-instructors: the unattended mining batch
│
├── sops/                         Long-form standard operating procedures (14 files)
│   ├── 01-brief-intake.md to 09-reporting-learning.md   One per funnel stream
│   └── aso.md, content-marketing.md, paid-performance.md, pr-comms.md, seo.md   The channels
│
├── benchmarks/                   Internet comparison pass: 9 domain docs + 00-synthesis + README
│
├── scripts/                      Deterministic gate runners
│   ├── eval_runner.py            Machine-check gate
│   └── pack_check.py             Definition-of-done gate for instructor packs
│
├── skill-paths/                  Skill Paths subsystem agent contracts (M14) + shared protocol
│
├── references/                   Research outputs and readouts (~115 files): platform research,
│                                 site crawl, instructor products, EdTech benchmark, Ortto MCP
│                                 knowledge base, REVIEW-QUEUE, drive-raw source files
│
└── outputs/                      Generated artifacts, per campaign (approval-ready packages):
                                  bassam-fattouh-makeup, bassam-fattouh-bridal-makeup,
                                  elda-choucair-marketing, skill-paths-soft-launch
```

---

## How the folders relate

The flow of a run reads across the folders like this:

1. `context/` holds the stable facts. Every agent loads `CLAUDE.md` and `context/brand-voice.md`
   first, plus the relevant stream SOP or skill. Facts never come from anywhere else.
2. `briefs/` holds the one per-campaign input. Variables (offer, price, targets, dates)
   come from here, never invented. Change the brief, not the machine.
3. `runtime/` is the conductor. The orchestrator reads `SWARM.md` and `stream-ownership.md`,
   composes a run, and wraps every step in `verification.md` gates, passing `handoff-contract.md`
   artifacts between stages.
4. `agents/` are the team the runtime dispatches to. Each owns its stream and nothing else.
5. `skills/` are the knowledge each agent applies, grouped by stream and channel, each shipping
   its own `evals/evals.json` acceptance checks.
6. `sops/` are the long-form procedures: one per funnel stream (01 to 09) plus the five
   acquisition channels (aso, content-marketing, paid-performance, pr-comms, seo).
7. `commands/` are the slash commands that start a run or a mining batch.
8. `benchmarks/` hold the internet comparison pass, `scripts/` hold the deterministic gate
   runners, `skill-paths/` holds the Skill Paths M14 subsystem contracts.
9. `references/` holds research the engine produced (platform readouts, the site crawl,
   instructor products, the review queue, raw Drive source files).
10. `outputs/` is where approval-ready packages land, per campaign, for the human gate.

## State of the build (current, honest)

The engine is well past the original scaffold. Current totals on `main`:

- 25 agents in `agents/`. Full roster, modes, and model assignments live in `_AGENTS-INDEX.md`.
- 24 skill folders in `skills/`: the 9 funnel-stream hubs with their sub-skills, the
  `web-design` stream-6 design hub, 6 channel hubs (organic-social, paid-performance, seo,
  content-marketing, aso, pr-comms), 6 quality gates (arabic-copy-qa, english-copy-qa,
  design-qa, web-design-qa, accessibility-qa, compliance-privacy-check), build-vs-buy-eval,
  and instructor-marketing.
- 14 long-form SOPs in `sops/`: one per funnel stream (01 to 09) plus the five channels.
- 7 runtime files, 4 slash commands, 2 deterministic gate-runner scripts.
- 11 benchmark docs (the internet comparison pass) in `benchmarks/`.
- An instructor layer: the `context/profiles/maharat/instructors/` registry plus per-instructor packs under
  `context/profiles/maharat/instructor-packs/`, with mining tooling in `commands/` and `scripts/`.
- Real campaign work: 6 briefs in `briefs/` and approval-ready packages in `outputs/` for
  bassam-fattouh-makeup, bassam-fattouh-bridal-makeup, elda-choucair-marketing, and the
  skill-paths soft launch.

Named platform decision: Ortto is the email and MCP platform. See
`context/findings-email-platform.md` and `references/2026-06-ortto-mcp-knowledge-base.md`.

Still open (todo):
- Resolve the standing open items: PDPL data residency, send volume, the first-campaign offer
  where a brief still carries ASSUMPTION flags, and mobile event mapping.
- Unify the two eval encodings (the descriptive `checks` array in the stream skills vs the
  `machine_checks` regex layer that `scripts/eval_runner.py` runs, currently only present in
  the instructor-marketing packs).

## Discovery note

Claude Code surfaces skills one level under `skills/`, so each stream hub auto-registers
and routes to its sub-skills. Sub-skills are complete, self-contained packages invoked via
the hub or by path. Agents are referenced by the orchestrator per `agents/_AGENTS-INDEX.md`.
The board mirror of this runtime layer lives in the workshop Miro under the frame
"Runtime layer: agent roster and the 4 swarm shapes."

## Update 2026-06-04 (pilot A and runnability layer)

Added since this file was first written:
- `RUNBOOK.md` (Claude Code end-to-end execution), `PATCHES.md` (repo wiring edits)
- `context/profiles/maharat/instructors/` (_CATALOG.md registry + per-instructor fact files; mona-ataya mined)
- `context/mining-plan-v2.md` (operational mining plan + mining swarm; supersedes the
  two earlier mining plans for execution), `context/drive-content-mining-plan.md`,
  `context/instructor-mining-plan.md` (design history)
- `context/profiles/maharat/instructor-packs/` (hub + mona-ataya pack: SKILL.md, voice.md,
  templates/one-liner-library.md, templates/organic-shot-list.md, evals/evals.json
  with machine + llm check layers)
- `scripts/eval_runner.py` (deterministic machine-check gate, self-tested)
- `commands/mine-instructor.md` (the /mine-instructor slash command)
- `references/drive-extraction-log.md` (running mining record)
- Batch layer (2026-06-04): `runtime/batch-mining-protocol.md` (unattended run
  contract), `commands/mine-all-instructors.md` (the batch command),
  `scripts/pack_check.py` (deterministic definition-of-done gate),
  `references/REVIEW-QUEUE.md` (the asynchronous human gate)

## Update 2026-06-05 (web design layer)

Added a web design discipline in stream 6, the design layer that feeds conversion-engineer,
mirroring the stream-3 creative-director + designer pattern:
- `agents/web-design-director.md` (web design direction: information architecture, UX flow,
  wireframes, visual direction) and `agents/web-designer.md` (build-ready responsive spec plus
  the web-design-qa gate).
- `skills/web-design/` (hub) with sub-skills `web-experience-direction/` and `web-design-spec/`,
  plus `skills/web-design-qa/` (the web design gate), each with SKILL.md, evals/evals.json, and templates/.
- Wiring: `runtime/handoff-contract.md` (the web-design-package artifact and the web_design_qa
  verdict), `runtime/verification.md` (web-design-qa in the gate stack and the stream-6 map),
  `runtime/stream-ownership.md` and `runtime/SWARM.md` (the stream-6 design layer feeding the
  build layer), `agents/_AGENTS-INDEX.md` (two roster rows, the count, coverage, the QA list),
  `CLAUDE.md` (web-design-qa in the quality gate), and `agents/conversion-engineer.md` plus
  `skills/06-conversion-path/landing-page/SKILL.md` (the page now realizes the design_spec).

Eval-format note (a reconcile finding): the engine carries two eval encodings. The stream skill
evals use a descriptive `checks` array judged by the reviewing agent, while `scripts/eval_runner.py`
runs a separate `machine_checks` regex layer that currently exists only in the instructor-marketing
packs. The new web-design evals follow the descriptive `checks` convention of their stream-skill
siblings, so they are consistent with the rest of skills/. Unifying the two encodings is a separate,
reviewed change, not made here.

## Update 2026-06-10 (docs-sync: tree and state refreshed)

Ran the weekly docs-sync against `main`. Since the 2026-06-05 web-design update the engine grew:
- the five acquisition channels (paid-performance, seo, content-marketing, aso, pr-comms) with
  their agents, channel skill hubs, and long-form SOPs,
- two cross-cutting agents (competitor-analyst and accessibility-reviewer) plus the
  `accessibility-qa` gate,
- the Ortto email-and-MCP platform decision,
- `DOCUMENTATION.md` (the long-form companion to this map),
- the `benchmarks/` internet comparison pass,
- the `skill-paths/` M14 subsystem contracts,
- and real campaign outputs (bassam-fattouh makeup and bridal, elda-choucair, skill-paths
  soft launch).

This file's tree, the "How the folders relate" list, and "State of the build" were rebuilt to
match. `agents/_AGENTS-INDEX.md` was already current at 25 agents and was left unchanged.
