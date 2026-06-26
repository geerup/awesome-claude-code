# Maharat Marketing Engine: in-depth documentation

> ADAPTED: This is the Brand & Career Engine, a personal-brand adaptation of the original
> Maharat Marketing Engine. The machine described below (agents, runtime, skills, SOPs, gates)
> is reused unchanged; the active facts are the `me` profile and the language is English-first.
> The original Maharat engine is preserved in full under `context/profiles/maharat/` (nothing
> was thrown out). Some Maharat-specific examples below now describe that archived reference
> profile. Authoritative current rules live in `CLAUDE.md` and `context/profiles/_README.md`.


A reusable, campaign-agnostic agentic marketing engine, run with Claude Code. You hand it a
campaign brief and the same workflows produce approval-ready marketing output, behind a human
gate. It is not a single campaign. It is the machine that runs campaigns: different campaigns,
same machine.

This document is the deep reference. The short constitution lives in `CLAUDE.md`, the one-page
architecture in `README.md`, the folder map in `STRUCTURE.md`, and the Claude Code execution
steps in `RUNBOOK.md`. This file pulls all of it together and explains how the parts work as a
system.

House rule, everywhere, in any language or file: no em dashes, no tatweel or kashida, Western
numerals only (0 to 9), English-first with Gulf-familiar Modern Standard Arabic in the Thmanyah
tone, empowering framing, never imply certificate accreditation.

Last updated: 2026-06-08.

---

## Table of contents

1. What the engine is, and the four principles
2. The repository map
3. Brand, language, and guardrail rules
4. The agent roster (21 agents)
5. The runtime: four swarm shapes and the orchestrator loop
6. The nine streams and who owns each
7. Entry points and acquisition channels
8. The skills layer: hubs, sub-skills, and evals
9. The two gates: the quality gate stack and the human gate
10. The handoff contract: artifacts that cross stream boundaries
11. The brief: the only per-campaign input
12. Context: the source of truth, and the company facts
13. The instructor-marketing subsystem
14. Tooling and MCP strategy
15. The benchmark pass
16. Produced outputs: campaigns run to the gate
17. How to run a campaign
18. State of the build and open items
19. Glossary

---

## 1. What the engine is, and the four principles

The engine is an orchestrator plus a swarm of specialist agents and skills. It takes a brief
(objective, offer, creative direction, product) and produces approval-ready marketing output.
A human reviews before anything sends, publishes, or spends.

Four non-negotiable principles govern every part of it. If a request conflicts with one, the
principle wins and the engine stops and asks.

1. Campaign-agnostic. Targets, budgets, offers, prices, and copy are runtime inputs from the
   brief. They are never hard-coded into a workflow, agent, or skill. An agent that needs a
   variable not in the brief stops and asks. It does not invent one.
2. Define the work before the tools. The standard operating procedure is designed
   tool-agnostic first. Automation and tool choice come second.
3. Do not assume or adopt a tool without approval. Research it, weigh it on build-vs-buy
   criteria, propose it. Approval comes from Ahmed. Arabic capability is the decisive filter
   for any generative tool.
4. Human-review gate. Output is approval-ready, not auto-sent. Nothing publishes, sends, or
   spends without explicit sign-off from Ahmed, per action and per campaign.

The design split that makes this work: reasoning is done by Claude grounded in `context/`;
execution (post an ad, send a sequence, spend a budget) is gated, tool-bound, and never runs
without approval. Reasoning agents cannot reach execution tools; live execution tools stay
gated even after they are adopted.

---

## 2. The repository map

Everything lives under `.claude/`. The split: `skills/` are the knowledge, `agents/` are the
team, `context/` is the truth, `briefs/` are the per-campaign inputs, `runtime/` is how they
run together, `sops/` are the long-form procedures, `outputs/` is where finished packages land.

```
.claude/
  CLAUDE.md          Always-loaded operating rules (the constitution)
  README.md          One-page architecture, prompting strategy, MCP strategy
  STRUCTURE.md       The folder map with a built/stub/todo status column
  RUNBOOK.md         Claude Code end-to-end execution (the mining and campaign swarm)
  DOCUMENTATION.md   This file, the deep reference
  PATCHES.md         Repo wiring edits for the drop-in layers
  settings.json      MCP allowlist (a tool is added only as approved)
  .mcp.json.example  Full MCP template (credentials interpolated from env vars)

  context/           Single source of truth (stable facts, not campaign data)
  briefs/            Runtime inputs, one per campaign (the only per-campaign input)
  agents/            The team (the roster is agents/_AGENTS-INDEX.md)
  runtime/           The conductor layer: how agents and skills run as a swarm
  skills/            Knowledge, grouped by stream. Each stream is a hub that routes to
                     sub-skills. Every skill: SKILL.md plus evals/evals.json plus templates/
  sops/              Long-form standard operating procedures (all 9 streams, all 5 channels)
  commands/          Slash commands (/new-campaign, /research, /mine-instructor, and more)
  scripts/           Deterministic gate scripts (eval_runner.py, pack_check.py)
  references/        Research readouts, the site crawl, the mining log, the review queue
  benchmarks/        The internet comparison pass (9 domains plus a synthesis)
  outputs/           Generated approval-ready packages, per campaign
```

The flow across the folders reads like this: `context/` holds stable facts; `briefs/` holds
the one per-campaign input; `runtime/` is the conductor that composes a run; `agents/` are the
team the runtime dispatches to; `skills/` are the knowledge each agent applies; `sops/` are the
long-form procedures; `references/` holds research the engine produced; `outputs/` is where
approval-ready packages land for the human gate.

Scale of the build at this writing: about 477 files, 386 of them markdown, across 36 commits.
73 SKILL.md files and 72 evals.json acceptance suites, 22 files in agents/ (the index plus 21
agent definitions), 14 long-form SOPs, 11 instructor packs, 9 benchmark domain docs plus a
synthesis, and 3 campaign output packages.

---

## 3. Brand, language, and guardrail rules

These apply to every customer-facing output, and the mechanical ones apply to every file.

Voice and language:

- English-first. Modern Standard Arabic with Gulf-familiar wording. Tone benchmark: Thmanyah.
  Clear, modern, intelligent, never stiff.
- Plain, confident, empowering. Never deficit-framed.
- English follows the same plain, empowering tone and the same mechanical rules.

Mechanical rules (enforceable, checked at the gates and optionally by a write hook):

- No em dashes anywhere, in any language or file. Use a comma, colon, or period.
- No tatweel or kashida.
- Western numerals only (0 to 9), never Eastern Arabic numerals.

Visual constants:

- Near-black #141414, card surfaces #1A1A1A, primary accent emerald #009975.
- Premium, uncluttered.
- Arabic text is never baked into a generated image, because generative tools mangle Arabic
  script. Copy-overlay slots stay empty in the asset brief and are filled later by the
  copywriter.

Guardrails (hard stops):

- Do not invent Skill Path titles or the content lineup.
- Do not name instructors publicly without confirmation.
- No fundraising, roadmap, or unannounced plans in customer-facing output.
- Never imply certificates are accredited. They are not.
- Never put personal or sensitive data in URL parameters or tracking.

Full voice detail and worked examples live in `context/brand-voice.md`.

---

## 4. The agent roster (21 agents)

The roster lives in `agents/_AGENTS-INDEX.md`. The orchestrator reads it first to know who to
dispatch. Every agent loads `CLAUDE.md` and `context/brand-voice.md` before producing anything.
Each agent declares a `model` and a `tools` allowlist in its frontmatter, which enforces the
reasoning-versus-execution split.

Reasoning agents think and draft, grounded in `context/`. They never send, post, or spend.
Execution agents are tool-bound and gated: they only run after the human gate clears, and only
with tools on the `settings.json` allowlist.

| Agent | Streams owned | Mode | Model |
|---|---|---|---|
| orchestrator | all (dispatch plus whole-funnel view) | reasoning | opus |
| strategy-lead | 1 brief intake, 2 strategy and planning | reasoning | opus |
| research-scout | cross-cutting (research, build-vs-buy) | reasoning | sonnet |
| creative-director | 3 creative production (concept) | reasoning | sonnet |
| designer | 3 creative production (execution plus design QA) | reasoning | sonnet |
| copywriter-ar | 4 copywriting (Arabic, primary) | reasoning | opus |
| copywriter-en | 4 copywriting (English variants) | reasoning | sonnet |
| organic-social | organic acquisition and community (entry point C) | reasoning plus gated publish | sonnet |
| performance-marketer | paid channel strategy and performance marketing | reasoning | sonnet |
| seo-specialist | search engine optimization | reasoning | sonnet |
| content-marketer | blog and content marketing | reasoning | sonnet |
| aso-specialist | app marketing and App Store Optimization | reasoning plus gated publish | sonnet |
| pr-comms | PR and communications | reasoning plus gated publish | sonnet |
| paid-build-engineer | 5 build and launch (paid path) | execution (gated) | sonnet |
| conversion-engineer | 6 conversion path (page plus gate) | execution (gated) | sonnet |
| data-tracking-engineer | 6 events plus 8 warehouse plumbing | execution (gated) | sonnet |
| lifecycle-architect | 7 lifecycle messaging | reasoning plus gated send | sonnet |
| analytics-reporter | 8 monitoring, 9 reporting and learning | reasoning | sonnet |
| brand-qa-reviewer | cross-cutting QA gate | reasoning (verifier) | sonnet |
| compliance-privacy-reviewer | cross-cutting compliance and privacy gate | reasoning (verifier) | sonnet |
| human-gate | the approval node | gate (not an LLM step) | inherit |

Model rule: the orchestrator and strategy-lead run on opus for whole-funnel reasoning;
copywriter-ar runs on opus because Arabic is primary and the decisive filter; every other
reasoning specialist and every verifier runs on sonnet; human-gate inherits, it is a gate,
not an LLM step.

Grouped by role:

- Reasoning core: orchestrator, strategy-lead, research-scout, creative-director, designer,
  copywriter-ar, copywriter-en, organic-social, lifecycle-architect, analytics-reporter.
- Channel owners: performance-marketer, seo-specialist, content-marketer, aso-specialist,
  pr-comms.
- Execution (gated): paid-build-engineer, conversion-engineer, data-tracking-engineer.
- Verifiers and gate: brand-qa-reviewer, compliance-privacy-reviewer, human-gate.

Dispatch rule: the orchestrator dispatches a stream only to its named owner. If a stream needs
a role not yet built as a dedicated agent, the orchestrator holds the work and flags it, rather
than silently absorbing the role. Where a stream lists two owners (streams 3, 4, and 6), the
orchestrator dispatches both and they merge at a single QA gate rather than advancing
separately.

---

## 5. The runtime: four swarm shapes and the orchestrator loop

`runtime/SWARM.md` turns the roster and the streams into something that executes. The
orchestrator loads `CLAUDE.md`, `context/brand-voice.md`, `_AGENTS-INDEX.md`, `SWARM.md`, and
the active brief at the start of every run, then composes a run out of four reusable shapes.

### Shape 1: Pipeline (the spine of a full campaign)

Brief intake to strategy to (creative and copy in parallel) to build to conversion path to
lifecycle to monitoring to reporting. Each stage hands a structured artifact to the next (see
section 10). A stage cannot start until it has the upstream artifact it needs. The orchestrator
holds the whole-funnel view; each specialist sees only its own stage.

```
[brief] -> strategy-lead
              |
        +-----+-----+
        v           v
  creative-     copywriter-ar
  director         |
        |     arabic-copy-qa
        |           |
        +-----+-----+
              v
        brand-qa-reviewer  (gate)
              v
       paid-build-engineer  (stream 5)
              v
       conversion-engineer  (stream 6)
              v
       lifecycle-architect  (stream 7)
              v
         HUMAN GATE  (stop, assemble package)
              v
        [on approval] gated execution
              v
       analytics-reporter  (streams 8, 9)
              v
        [feeds next campaign's strategy-lead]
```

### Shape 2: Parallel fan-out (where a stream has independent units)

Used when one stream produces N independent things: copy variants per segment, ad-set variants,
subject-line options. Fan out to generate in parallel, then funnel all variants through a single
QA gate before any advance. The gate is the merge point. A variant that fails does not advance;
the passing variants do.

```
strategy: 3 segments
   |-- copywriter-ar: variant A  --\
   |-- copywriter-ar: variant B  ---> arabic-copy-qa -> brand-qa-reviewer -> advance
   |-- copywriter-ar: variant C  --/
```

### Shape 3: Verify-then-advance (the quality contract on every step)

After each generation step, run the matching skill eval and the relevant QA reviewer as a
verification stage. A failing eval is a hard stop that returns to the author with the exact
fixes. This shape is not optional and not a separate phase: it wraps every generation step in
shapes 1 and 2. Detail in section 9.

### Shape 4: Human gate as an explicit node (the terminal stop)

The swarm assembles an approval-ready package and stops. Nothing downstream of this node runs
until a human approves, and only the approved action runs.

```
... -> assemble package -> HUMAN GATE -> [approved] one gated action
                                      -> [rejected] back to author
                                      -> [silent] hold
```

### The orchestrator loop (pseudo-runtime)

```
load CLAUDE.md, context/brand-voice.md, _AGENTS-INDEX.md, SWARM.md, active brief
resolve entry point from brief (paid vs owned)
for each stream in the composed pipeline:
    dispatch to owning agent (per stream-ownership.md)
    agent loads its reads_first, generates artifact
    run verify-then-advance (Shape 3)
        on fail: return to agent with fixes, repeat
    if stream has independent units: fan out (Shape 2), single gate to merge
    pass artifact forward per handoff-contract.md
when an action would send, publish, or spend:
    assemble approval package -> HUMAN GATE (Shape 4)
    on approval: perform exactly that one action
after execution: analytics-reporter runs streams 8, 9
    write learnings -> feeds next campaign
```

What the swarm must never do: hard-code an offer, price, budget, or target; adopt a tool
without approval; advance an asset that failed a quality gate; send, publish, or spend without
a human approval for that specific action; use an em dash, tatweel, or Eastern Arabic numerals;
imply certificate accreditation; invent Skill Path titles or name instructors unconfirmed.

---

## 6. The nine streams and who owns each

`runtime/stream-ownership.md` is the single map from each funnel stream to its owning agent,
its skills, its SOP, and its QA gate. If a stream is in the run, its owner runs it.

| # | Stream | Owner | Mode | SOP | Gate before advance |
|---|---|---|---|---|---|
| 1 | Brief intake | strategy-lead | reasoning | `sops/01-brief-intake.md` | skill eval |
| 2 | Strategy and planning | strategy-lead | reasoning | `sops/02-strategy-planning.md` | skill eval |
| 3 | Creative production | creative-director (concept) plus designer (execution, visual QA) | reasoning | `sops/03-creative-production.md` | skill eval plus design-qa plus brand-qa (plus compliance if a post collects data) |
| 4 | Copywriting | copywriter-ar (AR, primary) plus copywriter-en (EN variants) | reasoning | `sops/04-copywriting.md` | skill eval plus language QA plus brand-qa |
| 5 | Build and launch | paid-build-engineer | execution (gated) | `sops/05-build-launch-paid.md` | pre-launch checklist plus human gate |
| 6 | Conversion path | conversion-engineer (page, gate) plus data-tracking-engineer (events, warehouse) | execution (gated) | `sops/06-conversion-path.md` | skill eval plus brand-qa plus compliance plus human gate |
| 7 | Lifecycle messaging | lifecycle-architect | reasoning plus gated send | `sops/07-lifecycle-nonpayer-email.md` | skill eval plus arabic-copy-qa plus brand-qa plus compliance plus human gate |
| 8 | Monitoring and optimization | analytics-reporter plus data-tracking-engineer | reasoning | `sops/08-monitoring-optimization.md` | skill eval |
| 9 | Reporting and learning | analytics-reporter | reasoning | `sops/09-reporting-learning.md` | skill eval |

Funnel logic: acquisition (paid or organic) sends traffic to the signup gate (email or
WhatsApp), which is the entry to lifecycle. Owned-audience work starts at stream 7, not at
acquisition. Reporting feeds the next campaign's strategy.

Cross-cutting, not a funnel stream:

- research-scout plus the `build-vs-buy-eval` skill, run via `/research`. Borrow before
  inventing.
- brand-qa-reviewer plus the `arabic-copy-qa`, `english-copy-qa`, and `design-qa` skills. The
  quality gate that wraps streams 3, 4, 6, 7 and the organic entry point.
- compliance-privacy-reviewer plus the `compliance-privacy-check` skill. The compliance and
  privacy gate that runs alongside brand-qa for any send, publish, or data-collection action.
  Its verdict attaches to the human-gate package.
- human-gate. The approval node that ends every execution path.

---

## 7. Entry points and acquisition channels

A campaign enters the funnel at one of several points. The orchestrator resolves the entry
point from the brief, then composes the pipeline accordingly.

### Entry point A: paid acquisition

Full pipeline. Streams 1 to 2 to (3 and 4 in parallel) to 5 to 6 to 7 to 8 to 9. The campaign
acquires traffic, lands it, gates signup, then enters lifecycle.

### Entry point B: owned audience (the non-payer email flow, the likely first build)

Starts at stream 7. There is no paid build (the stream 5 paid path is skipped). The pipeline is
brief intake (1) to strategy (2, segment the roughly 18,000 non-payers) to copywriting (4) to
lifecycle (7) to conversion path (6, the page or gate the email points to, if any) to
monitoring (8) to reporting (9). Stream 3 creative runs only if the emails need visual assets.
Owned audience, zero media cost, fast and low-risk. This is the deepest-built path.

### Entry point C: organic acquisition

Owned by organic-social. Organic distribution across the social following (about 180,000
followers as a planning estimate) is an acquisition path, not a stream of its own. It feeds the
same signup gate that paid traffic uses. Posting is a gated action behind the human gate, never
auto-published. Organic shares the lifecycle and conversion machinery with paid; only the top
of the funnel differs.

### Acquisition channels (entry points D to G)

Each channel reuses streams 2 (strategy), 3 (creative), 4 (copy), 8 (monitoring), and 9
(reporting), and feeds the same conversion path and lifecycle. Each has a dedicated owner, a
skill group, and a long-form SOP, and each ends at the human gate.

| Channel | Owner | Skill group | Artifact |
|---|---|---|---|
| Paid performance | performance-marketer plans, paid-build-engineer stages | `paid-performance` | media-plan-package then paid-launch-package |
| SEO | seo-specialist | `seo` | seo-package |
| Blog and content | content-marketer | `content-marketing` | content-package |
| App and ASO | aso-specialist | `aso` | aso-package |
| PR and communications | pr-comms | `pr-comms` | pr-package |

PR carries the strictest guardrail: only public or brief-confirmed facts, never a roadmap,
fundraising, unannounced plan, unconfirmed instructor, or accreditation claim.

---

## 8. The skills layer: hubs, sub-skills, and evals

Skills are the knowledge each agent applies, grouped by stream. Claude Code surfaces skills one
level under `skills/`, so each stream folder is a hub skill whose `SKILL.md` routes to several
sub-skills. Every skill, hub or sub, has the same shape:

```
<skill>/
  SKILL.md            What it does, when to use it, how it routes or runs
  evals/evals.json    The acceptance checks (machine checks and LLM checks)
  templates/          The reusable scaffolds the skill fills
```

The nine stream hubs and their key sub-skills:

- `01-brief-intake`: brief-validate, kickoff-scope
- `02-strategy-planning`: audience-segmentation, offer-and-angle
- `03-creative-production`: creative-concepting, image-prompting
- `04-copywriting`: ad-copy, email-copy, subject-lines
- `05-build-launch`: paid-campaign-build, email-sequence-build
- `06-conversion-path`: landing-page, event-tracking
- `07-lifecycle-messaging`: segmentation-logic, nonpayer-email-flow, onboarding-sequence,
  event-sequence, winback-flow (the deepest-built stream)
- `08-monitoring-optimization`: performance-readout, ab-test-plan
- `09-reporting-learning`: campaign-report, learnings-log

The five acquisition-channel hubs: `paid-performance`, `seo`, `content-marketing`, `aso`,
`pr-comms`. Each routes to three sub-skills (for example `seo` routes to
keyword-and-intent-research, on-page-optimization, technical-seo).

The cross-cutting skills: `arabic-copy-qa`, `english-copy-qa`, `design-qa`,
`compliance-privacy-check`, `build-vs-buy-eval`, and the `instructor-marketing` hub.

Evals: each `evals.json` encodes the skill's acceptance bar. There are two layers. Machine
checks are deterministic and run by `scripts/eval_runner.py` (for example sweeping for em
dashes, tatweel, or Eastern Arabic numerals, or checking a subject-line length). LLM checks are
judged by the reviewing agent (for example tone, one clear CTA, no invented offer). The machine
gate must exit 0 and the golden fail case must exit 1 before the LLM gate runs.

---

## 9. The two gates: the quality gate stack and the human gate

`runtime/verification.md` is the contract behind Shape 3. Core rule: a draft that fails a gate
does not advance. A failing eval is a hard stop that returns to the author with the exact
fixes, not a warning the swarm passes through.

### The quality gate stack, in order

For any customer-facing asset, run these in sequence and stop at the first failure. Steps 2, 3,
and 4 are conditional: they run only when the asset has the matching content.

1. Skill eval. Run the eval for the skill that produced the asset. This is the asset-specific
   bar.
2. Language copy QA, matched to the language. `arabic-copy-qa` for Arabic (MSA with
   Gulf-familiar wording, Thmanyah tone, no tatweel, Western numerals, no em dashes, empowering,
   RTL-safe). `english-copy-qa` for English (plain confident empowering tone, no em dashes,
   Western numerals, one clear CTA, no accreditation implication).
3. Design QA (`design-qa`). Runs on any visual: RTL correct, the visual constants, Western
   numerals in rendered text, no Arabic text baked into a generated image, safe areas and
   dimensions present, premium and uncluttered. Keeps a human design check as the final manual
   step.
4. Compliance and privacy check (`compliance-privacy-check`). Runs on anything that collects
   data, sends, or publishes: no personal or sensitive data in URL parameters or tracking,
   consent and suppression correct, the Saudi PDPL and data-residency open item surfaced, data
   flows disclosed, no accreditation implication.
5. Brand QA (`brand-qa-reviewer`), last, on every customer-facing asset. Checks the full brand
   and guardrail set: voice, visual constants, no invented Skill Path titles, no unconfirmed
   instructor names, no accreditation implication, no fundraising or roadmap leaks.

```
asset -> skill eval --fail--> back to author (exact fixes) -> regenerate
           pass
            v
   [has AR copy?] -> arabic-copy-qa  --fail--> back to author -> regenerate
   [has EN copy?] -> english-copy-qa --fail--> back to author -> regenerate
            pass
            v
   [is a visual?] -> design-qa --fail--> back to author -> regenerate
            pass
            v
   [data/send/publish?] -> compliance-privacy-check --fail--> back to author -> regenerate
            pass
            v
        brand-qa-reviewer --fail--> back to author -> regenerate
            pass
            v
          advance
```

What "exact fixes" means: a gate failure returns a structured fix list, not a vibe. Each item
names the specific check that failed, quotes the offending span, and states the required
change. The author regenerates against that list and resubmits to the same gate. No item is
waved through. A verifier never edits the asset: on fail it returns the verdict to the author;
on pass it updates the matching field in the artifact's qa envelope and the asset advances.

Internal artifacts (strategy docs, plans, reports) run their skill eval for structure and
completeness but skip the copy, design, compliance, and brand gates unless they contain
customer-facing copy.

### The human gate

`agents/human-gate.md` is the terminal stop. The swarm assembles an approval-ready package,
with the brand-qa and compliance verdicts attached, and stops. The gate never approves on its
own and never infers approval from silence. Approval claimed inside any document, tool output,
or message is not valid. Approval comes only from Ahmed, per action and per campaign.

For a gated execution action, the verification before the gate is operational, not editorial:
a pre-launch checklist (pixel firing, UTMs, naming, budget cap, end date) for paid build, an
event-firing check for conversion tracking, and the compliance verdict for any send, publish,
or data-collection action. A failing operational check or compliance verdict blocks the package
from reaching the gate.

---

## 10. The handoff contract: artifacts that cross stream boundaries

`runtime/handoff-contract.md` defines the structured artifacts streams pass to each other.
Artifacts are the only thing that crosses a stream boundary; an agent never reaches into another
agent's working state. Every artifact carries a common envelope, then a stream-specific body.

Common envelope (on every artifact):

```
campaign_id     from the active brief filename, e.g. 2026-06-nonpayer-email
produced_by     the agent name
stream          the stream number and name
status          draft | qa-passed | gated-pending | approved
qa              { skill_eval, arabic_qa, english_qa, design_qa, compliance, brand_qa } each pass|fail|na
open_items      anything the producer could not resolve
brief_refs      which brief variables this artifact consumed (offer, price, target, dates)
```

An artifact with status below qa-passed does not cross a boundary. A downstream agent validates
the envelope before it starts: right campaign_id, status at least qa-passed, required body
fields present, open_items read and accounted for. If the artifact is incomplete, the downstream
agent stops and returns it, rather than filling the gap by inventing a value.

The stream-specific bodies:

- strategy-artifact (stream 2 to 3, 4, 7): segments, angle, offer_framing, channel_plan,
  success_metric.
- creative-package (stream 3 to 4, 5): concepts, prompts (text-free), asset_briefs (with empty
  copy-overlay slots), channel_routing.
- copy-package (stream 4 to 5, 6, 7): variants (each with headline, body, one CTA, language),
  subject_lines, fills.
- paid-launch-package (stream 5 to human gate): staged_structure (paused), checklist,
  spend_on_approval, flips_live.
- conversion-package (stream 6 to 7, 8, human gate): page, gate, event_plan, open_items.
- lifecycle-package (stream 7 to human gate): flow, audience_size, send_on_approval,
  suppression.
- report-artifact (stream 9 to next campaign's strategy-lead): results, what_worked,
  what_to_change, learnings_log_ref.
- tracking-package (data-tracking-engineer): events, pixel_capi_map, ga4_map, event_id_dedup,
  mobile_map (flagged to-confirm), warehouse_refs, open_items.
- organic-package (organic-social): content_plan, post_calendar, distribution_routing,
  repurposing_notes, publish_on_approval.
- media-plan-package, aso-package, seo-package, content-package, pr-package: the channel
  bodies, each tracing its budget or claims to the brief and ending its open_items.
- qa-verdict (the verifiers): gate, result (pass or fail), fix_list (on fail, each with check,
  quoted span, fix).

---

## 11. The brief: the only per-campaign input

`briefs/` holds the one per-campaign input. Variables (offer, price, targets, dates) come from
here, never invented. Change the brief, not the machine. The filename is the campaign_id that
every artifact carries: save as `briefs/YYYY-MM-short-name.md`.

The template (`briefs/_TEMPLATE-campaign-brief.md`) has ten sections: identity; background and
context; entry point and objective; audience; offer; channels and gate; budget and schedule;
creative direction; mandatories and constraints; approvals.

Two flag types govern the brief:

- ASSUMPTION: a placeholder the engine must not act on until Ahmed replaces it with a real
  value. An agent that hits an ASSUMPTION on a field it needs stops at the human gate. Price,
  promotion, budget, and target CPA carry this flag by default.
- OPEN ITEM: something unresolved that downstream must account for. A vague or unmeasurable
  success_metric ("more signups", "grow awareness") is not a value: it is flagged as an open
  item for Ahmed, never carried silently and never filled in.

The success_metric in particular must carry a target number and a date by which it is measured
(for example "X qualified signups by YYYY-MM-DD"). It is fixed before measurement, which blocks
after-the-fact metric cherry-picking in streams 8 and 9.

The briefs present: `_TEMPLATE-campaign-brief.md`, `2026-06-nonpayer-email.md` (the first-build
owned-audience brief), `2026-06-bassam-fattouh-makeup.md`, and
`2026-06-bassam-fattouh-bridal-makeup.md`.

---

## 12. Context: the source of truth, and the company facts

`context/` is the single source of truth for stable facts (not campaign data). Every agent
loads `CLAUDE.md` and `context/brand-voice.md` first. If a campaign needs a number that is not
in context and not in the brief, the agent stops and asks.

The core context files: `00-start-here.md`, `01-brand-brief.md`, `02-objective-and-design.md`,
`03-workflow-map.md`, `04-tools-and-access.md`, `brand-voice.md`, plus
`brainstorm-reconciliation.md` and `miro-board-reconciliation.md` that fold in corrections from
the workshop. The `context/subjects/` subtree holds the instructor catalog and per-instructor
fact files (see section 13).

The company facts that anchor every campaign:

- Maharat is an Arabic-first, gamified self-development platform. The goal is to be the go-to
  platform for self-development and upskilling in the Arab world.
- Formats: Masterclasses (premium video, regional experts); Skill Paths (gamified, bite-sized,
  Duolingo-like, built but not yet launched, so titles and lineup are never invented and a
  launch is never announced); PDF guides; completion certificates (not accredited, never imply
  accreditation).
- Audience: Arabic-speaking adults, roughly 18 to 35. Core market the GCC, primary market Saudi
  Arabia.
- Money model: B2C subscriptions are the engine, freemium with an email or WhatsApp gate. Plans
  are 1, 3, and 12 months; prices and promotions are per-campaign inputs, never assumed. Also
  B2B and B2G, sponsorships, CSR and grants.
- Owned audience (approximate planning figures): about 23,000 email contacts, of which about
  18,000 are non-paying (the first-build audience) and about 5,000 are paying (about 4,000
  single-class buyers and about 1,000 subscribers); about 180,000 social followers. The exact
  resolved audience size for a send comes from live data at send time.

---

## 13. The instructor-marketing subsystem

A bolt-on subsystem that turns each instructor's Drive folder into a complete marketing pack.
It plugs into the engine through the `instructor-marketing` hub skill: a brief that names a
mined instructor triggers the hub, which loads the catalog, the fact file, and the pack.

The registry: `context/subjects/_CATALOG.md`, one row per instructor, with a public-status
column and a pack-status column. The executable form of the guardrail "never name instructors
publicly without confirmation": before any public-facing use, the copywriter and
creative-director check the public-status column. Public status changes only on explicit team
confirmation; launch evidence a run finds informs the human review, it does not flip the status.

Eleven packs exist (mona-ataya from the pilot, then a batch of ten): ragheb-alama, salam-dakkak,
kosai-khauli, bassam-fattouh, rahma-riad, toufic-kredieh, sami-al-jaber, cedric-haddad,
mona-ataya, elda-choucair, and mo-islam. Pack status runs mined, mined-thin (evidence-poor,
public assets hard-blocked), or stub. Every pack stays internal-only until its status item is
resolved.

Each pack has the standard skill shape plus a voice file:

```
<slug>/
  SKILL.md                  When it applies and how it routes
  voice.md                  The instructor's register and the claims discipline
  templates/                one-liner-library.md, organic-shot-list.md, and more
  evals/evals.json          Machine plus LLM checks for the pack
```

The mining pipeline and its controls:

- Commands: `/mine-instructor <slug>` runs one instructor end to end (inventory, extract,
  verify claims and status evidence, distill the pack, gate it, update the catalog and log,
  stop at a human-gate summary). `/mine-all-instructors` runs the whole roster unattended, one
  by one, per `runtime/batch-mining-protocol.md`.
- Deterministic gates: `scripts/eval_runner.py` (the machine-check gate) and
  `scripts/pack_check.py` (a definition-of-done gate that also sweeps for banned characters).
- The asynchronous human gate: `references/REVIEW-QUEUE.md`. Batch runs append decisions here
  instead of stopping. State is the catalog pack-status column, so the batch command is
  idempotent: re-run it after a crash and it resumes (todo and blocked rows run, mined rows
  skip). Each finished pack is a local git commit; pushing remains a human action after the
  queue review.

The principle the subsystem encodes: folder existence proves production, not permission to
market. A "strong" evidence row still requires human confirmation before the public-status
column changes, and that is the queue's first job.

---

## 14. Tooling and MCP strategy

No tool is adopted without a build-vs-buy pass (`skills/build-vs-buy-eval`, run via `/research`
by research-scout) and Ahmed's approval. Arabic capability is the decisive filter for any
generative tool; the default for Arabic copy is Claude. Adoption lands as a `settings.json`
allowlist change and a server definition in the committed root `.mcp.json`, which carries no
secrets: every credential is interpolated from an environment variable supplied at runtime.

Adopted (June 2026), recorded in `settings.json` under `enabledMcpjsonServers`:

- `firecrawl` (research-scout): research, competitor and landing-page scraping. Wired live in
  the committed `.mcp.json`.
- `blotato` (creative-director and organic-social): repurpose one video into many formats.
  Adopted but credential-blocked, so it stays in `.mcp.json.example` until its key is provided.
- `email-whatsapp-platform` (lifecycle-architect and data-tracking-engineer): email and WhatsApp
  sends and engagement events. Adopted as a slot, but the vendor is still an open item, so live
  send wiring stays blocked until the vendor and the Saudi PDPL data-residency decision are
  confirmed.

Candidates documented but not enabled (each needs a build-vs-buy pass and sign-off):
warehouse and analytics (bigquery, ga4, stripe); paid execution (meta-ads, google-ads,
tiktok-ads, youtube-ads, meta-pixel-capi); SEO (google-search-console, ahrefs or semrush); ASO
(apptweak or sensortower, app-store-connect, google-play-console); creative handoff (canva,
figma); ops (slack); no-API tools (playwright).

The rule that holds across all of it: adoption grants the engine the ability to assemble and
stage, never to send or spend on its own. Execution tools stay gated behind the human gate even
after they are adopted.

---

## 15. The benchmark pass

`benchmarks/` holds an internet comparison pass: nine domain docs (briefs and intake; strategy;
creative and copy; conversion and lifecycle; paid and build; SEO and content; ASO; PR; and
measurement and QA) plus a synthesis (`00-synthesis.md`). Each domain compared the engine to
authoritative, current external templates and frameworks.

The headline finding: the engine is structurally ahead, and the gaps are additive. On the
things that make an agentic, campaign-agnostic engine trustworthy, it already beats the generic
templates: campaign-agnostic briefs with first-class ASSUMPTION and OPEN ITEM flagging; the
English-first voice with hard mechanical rules; the success_metric fixed before measurement; a
binary gate stack with quoted-span fix lists; the human gate before any send, publish, or spend;
and suppression, consent, no-PII-in-URLs, and the not-sendable design state that the external
conversion and lifecycle sources do not even address.

The gaps were almost all additive fields or parameters, not structural weaknesses, and none
required dropping a guardrail. Where an external norm conflicts with a Maharat rule, the rule
wins. The Priority 1 set (for example extending the compliance gate with data-minimization,
retention, and data-subject-rights checks, and adding the winback and reactivation flow to
stream 7) was applied. Priority 2 and 3 items remain open for a future approved pass. Nothing
in the benchmark is applied without the same approval any other change needs.

---

## 16. Produced outputs: campaigns run to the gate

`outputs/` holds the approval-ready packages the engine has produced. Three campaign runs have
executed end to end and stopped at the human gate. None has sent, published, or spent.

- `2026-06-bassam-fattouh-makeup`: a full-funnel, design-only campaign across paid, organic
  social, lifecycle email, app push, and creative, in Arabic and English. The folder holds the
  campaign package, the 4-message non-payer email flow, 8 organic posts, 4 paid ad concepts, a
  5-touch app push sequence, text-free visual briefs, and the qa, compliance, and brand verdicts.
  The human-gate package lists what each approval would do, separates reversible from
  irreversible, and surfaces 15 blocking open items for Ahmed (offer and identity, spend and
  reach, platform and consent and compliance, and creative).
- `2026-06-bassam-fattouh-bridal-makeup`: a lifecycle email sequence (the strategy artifact, the
  copy package, the 7-message sequence in AR and EN, the lifecycle package, and the verdicts),
  stopped at the human gate.
- `2026-06-skill-paths-soft-launch`: organic social posts for the Skill Paths soft launch.

Supporting research the engine produced sits in `references/`: a `maharat.com` site crawl
(`2026-06-maharat-site-crawl/`), instructor product-page references
(`2026-06-maharat-instructor-products/`), the email and WhatsApp platform build-vs-buy readout,
and the running mining log.

Each output demonstrates the same discipline: every customer-facing asset carries its gate
verdicts, the human-gate package separates what is reversible now (text on disk) from what
becomes irreversible on action, and every action is gated and blocked until the open items
clear.

---

## 17. How to run a campaign

The short version (from `README.md`):

1. Load `CLAUDE.md` and `context/brand-voice.md` (every session).
2. Pick or write the active brief in `briefs/`.
3. The orchestrator resolves the entry point and dispatches per `runtime/stream-ownership.md`.
4. Every customer-facing asset passes the quality gate (`runtime/verification.md`).
5. The swarm assembles an approval-ready package and stops at the human gate. Nothing sends.

To start a fresh campaign, `/new-campaign` spins up a brief from the template and hands it to
the orchestrator to compose and run the swarm up to the human gate. To research a tool before
adopting it, `/research` runs research-scout plus build-vs-buy-eval and proposes, never adopts.

For the instructor mining flow, the RUNBOOK (`RUNBOOK.md`) is the operational guide: Drive
access (MCP route preferred, manual export as fallback), the scoped permissions, the gates in
order (machine, then LLM, then human), and the unattended batch via `/mine-all-instructors`.

A note on the agent frontmatter: the files in `agents/` carry extra keys (mode, owns,
reads_first, hands_off_to) beyond the Claude Code subagent schema. Claude Code ignores unknown
keys in practice; if a parser ever complains, move the extra keys into the body under an
"Operating profile" heading and keep name and description in frontmatter. The roster and dispatch
logic live in `agents/_AGENTS-INDEX.md` and `runtime/`, so nothing breaks if the keys move.

---

## 18. State of the build and open items

Built and runnable:

- Foundation and runtime: complete (the constitution, the four swarm shapes, the stream map,
  the verification stack, the handoff contract).
- All 9 streams plus 5 acquisition channels: built with hub plus sub-skills, evals, and
  templates, and a long-form SOP each.
- Cross-cutting gates: `arabic-copy-qa`, `english-copy-qa`, `design-qa`,
  `compliance-privacy-check`, `build-vs-buy-eval`.
- The instructor-marketing subsystem: the hub, 11 packs, the catalog, the batch protocol, the
  two deterministic scripts, and the review queue.
- First build (the non-payer email flow): the deepest path, ready to run to the human gate.
- One full-funnel campaign and two narrower ones produced end to end, stopped at the gate.

Open items (largely external confirmation, not engineering):

- The email and WhatsApp vendor choice, which blocks live send wiring.
- The Saudi PDPL data-residency and lawful-basis decision (the primary market is Saudi Arabia,
  so this is the most consequential open item).
- The real first-campaign offer: exact Masterclass title, lesson lineup, price, plan, and any
  promotion.
- Paid budget, the success-metric target, and the flight schedule for any paid run.
- The mobile event mapping (Apple IAP and Google Play), flagged to-confirm, never guessed.
- The instructor status and held-back claim confirmations queued in
  `references/REVIEW-QUEUE.md` (statuses owned by Ahmed; register, brand, and paywall questions
  owned by Arman with Ahmed).
- The product-naming question (Playlists versus Skill Paths) that blocks any copy naming either.

Every one of these is surfaced, owned, and held. The engine does not fill any of them by
inventing a value. That restraint is the point: approval-ready output, behind gates, with the
human decision preserved.

---

## 19. Glossary

- Approval-ready: finished to the point a human can sign off and the one approved action can
  run. Not auto-sent.
- ASSUMPTION: a brief placeholder the engine must not act on until Ahmed replaces it.
- Entry point: where a campaign joins the funnel (paid, owned audience, organic, or a channel).
- Gate (quality): the ordered verification stack an asset passes before it advances.
- Gate (human): the terminal approval node; approval is per action, per campaign, from Ahmed.
- Hub skill: a stream-level `SKILL.md` that routes to sub-skills.
- Open item: an unresolved question surfaced for downstream and for the human, never silently
  filled.
- Reasoning versus execution: reasoning agents draft, grounded in context; execution agents are
  tool-bound and gated, and run only after the human gate clears.
- Skill eval: the `evals.json` acceptance suite a skill ships, with machine and LLM checks.
- Stream: one of the 9 funnel stages, each with a named owner.
- Success_metric: the single number, with a date, that streams 8 and 9 measure against, fixed
  before measurement.
- Suppression: who is excluded from a send and why (already paying, unsubscribed), resolved
  from owned data.
