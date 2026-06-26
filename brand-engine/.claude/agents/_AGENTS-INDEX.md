# Agent Index: the brand & career swarm

This file is the roster. It lists every agent, the stream(s) it owns, whether it
reasons or executes, and where its output goes. The orchestrator reads this first
to know who to dispatch. You read it to know who did what.

House rule, everywhere: English-first, no em dashes, empowering framing, verified
claims only, never imply a credential or accreditation not held. When a brief sets
Arabic in scope: no tatweel, Western numerals, RTL-safe.

Upstream of the roster sits the brand foundation (the 29 brand-building skills,
`skills/_BRAND-FOUNDATION.md`), run once as Stream 0. Two added skills, `asset-ingest`
(ingest, OCR, tag, mine your corpus) and `career-narrative` (engaging true career
stories), are used by the agents below.

## How to read the roster

- Reasoning agents think and draft, grounded in `context/`. They never send, post, or spend.
- Execution agents are tool-bound and gated. They only run after the human gate clears,
  and only with tools on the `settings.json` allowlist.
- Every agent loads `CLAUDE.md` and `context/brand-voice.md` before producing anything.
- Facts come from `context/`. Variables (offer, price, targets, dates) come from the
  active `briefs/` file. An agent that needs a variable not in the brief stops and asks,
  it does not invent one.

## The roster

Twenty-eight agents: the orchestrator, the specialists across the 9 funnel streams (including
the stream-6 web design layer, web-design-director and web-designer), the acquisition channel
owners (organic, paid performance, SEO, content, ASO, PR), the cross-cutting research,
competitor-analysis, verifier, accessibility, email-asset, and gate roles, and the optional
Arabic brand-voice copy set (brand-copywriter-ar plus the brand-voice-reviewer gate), which
activates only when a brief sets Arabic in scope. For a solo personal brand, the paid-execution
agents (paid-build-engineer, performance-marketer) and the warehouse/payments plumbing stay
reasoning-only until you opt into paid ads or a storefront (see `context/04-tools-and-access.md`).

| Agent | Streams owned | Mode | Model | Reads first | Hands off to |
|---|---|---|---|---|---|
| `orchestrator` | all (dispatch + whole-funnel view) | reasoning | opus | brief, `_AGENTS-INDEX`, `runtime/SWARM.md` | every specialist |
| `strategy-lead` | 1 brief intake, 2 strategy and planning | reasoning | opus | brief, `context/`, `02-strategy-planning` skills | creative + copy + lifecycle |
| `research-scout` | cross-cutting (research, build-vs-buy) | reasoning | sonnet | `commands/research`, `build-vs-buy-eval` | strategy-lead, orchestrator |
| `competitor-analyst` | cross-cutting (competitor teardowns, feed strategy) | reasoning | sonnet | `01-brand-brief`, brief, brand-voice | strategy-lead, research-scout, orchestrator |
| `creative-director` | 3 creative production (concept) | reasoning | sonnet | `03-creative-production` skills, brand-voice | designer, copywriters, brand-qa |
| `designer` | 3 creative production (execution + design check) | reasoning | sonnet | `03-creative-production` skills, `design-qa`, brand-voice | copywriters, paid-build, brand-qa |
| `copywriter-en` | 4 copywriting (English, primary) | reasoning | opus | `04-copywriting` skills, brand-voice | english-copy-qa then brand-qa |
| `copywriter-ar` | 4 copywriting (Arabic, only when brief sets Arabic in scope) | reasoning | sonnet | `04-copywriting` skills, brand-voice | arabic-copy-qa then brand-qa |
| `brand-copywriter-ar` | Arabic brand-voice copy (optional; only when Arabic in scope) | reasoning | sonnet | brand-voice, the AR brand-voice manual and corpus | arabic-copy-qa, brand-voice-reviewer, brand-qa |
| `organic-social` | organic acquisition and community (entry point C) | reasoning + gated publish | sonnet | brief, `01-brand-brief`, `organic-social` skill, brand-voice | conversion-engineer, brand-qa, human-gate |
| `performance-marketer` | paid channel strategy and performance marketing | reasoning | sonnet | `sops/paid-performance`, `paid-performance` skills | paid-build-engineer, data-tracking-engineer, analytics-reporter, human-gate |
| `seo-specialist` | search engine optimization | reasoning | sonnet | `sops/seo`, `seo` skills, brand-voice | content-marketer, conversion-engineer, analytics-reporter, human-gate |
| `content-marketer` | blog and content marketing | reasoning | sonnet | `sops/content-marketing`, `content-marketing` skills | copywriter-ar, copywriter-en, seo-specialist, organic-social, human-gate |
| `aso-specialist` | app marketing and App Store Optimization | reasoning + gated publish | sonnet | `sops/aso`, `aso` skills, brand-voice | data-tracking-engineer, analytics-reporter, human-gate |
| `pr-comms` | PR and communications | reasoning + gated publish | sonnet | `sops/pr-comms`, `pr-comms` skills, brand-voice | copywriters, compliance-privacy-reviewer, brand-qa, human-gate |
| `paid-build-engineer` | 5 build and launch (paid path) | execution (gated) | sonnet | `sops/05-build-launch-paid`, Meta/Google MCP | human-gate |
| `web-design-director` | 6 conversion path (web design direction) | reasoning | sonnet | `web-design` skills, brand-voice | web-designer, conversion-engineer, copywriters, brand-qa |
| `web-designer` | 6 conversion path (web design execution + web-design QA) | reasoning | sonnet | `web-design` skills, `web-design-qa`, brand-voice | conversion-engineer, brand-qa, copywriters |
| `conversion-engineer` | 6 conversion path (page + gate) | execution (gated) | sonnet | `sops/06-conversion-path`, GA4/Pixel MCP | data-tracking-engineer, analytics-reporter, human-gate |
| `data-tracking-engineer` | 6 events + 8 warehouse plumbing | execution (gated) | sonnet | `06`/`08` skills, GA4/BigQuery/CAPI MCP | analytics-reporter, human-gate |
| `lifecycle-architect` | 7 lifecycle messaging | reasoning + gated send | sonnet | `sops/07-lifecycle-nonpayer-email`, `07` skills | human-gate |
| `analytics-reporter` | 8 monitoring, 9 reporting and learning | reasoning | sonnet | `08`/`09` skills, BigQuery/GA4/Stripe MCP | strategy-lead (next campaign) |
| `brand-qa-reviewer` | cross-cutting QA gate | reasoning (verifier) | sonnet | brand-voice, every customer-facing asset | author (on fail) or next stage (on pass) |
| `brand-voice-reviewer` | cross-cutting brand-voice copy gate (the brand-voice copy set) | reasoning (verifier) | sonnet | brand-voice, the AR brand-voice manual and corpus, `brand-voice-qa` | author (on fail) or brand-qa (on pass) |
| `compliance-privacy-reviewer` | cross-cutting compliance and privacy gate | reasoning (verifier) | sonnet | `runtime/verification.md`, `compliance-privacy-check`, the data flow | author (on fail) or human-gate (on pass) |
| `accessibility-reviewer` | cross-cutting accessibility gate (pages, emails) | reasoning (verifier) | sonnet | brand-voice, `runtime/verification.md`, the asset | author (on fail) or next stage (on pass) |
| `email-asset-reviewer` | cross-cutting email asset and visual gate (stream-7 image modules) | reasoning (verifier) | sonnet | `context/profiles/maharat/email-design-system.md`, `runtime/email-module-map.md`, `runtime/verification.md`, the build | author (on fail) or next stage (on pass) |
| `human-gate` | the approval node | gate (not an LLM step) | inherit | the assembled approval package | the human (Ahmed) |

Model rule: orchestrator and strategy-lead run on opus for whole-funnel reasoning;
copywriter-en runs on opus because English is the primary language and the decisive copy
filter; copywriter-ar and brand-copywriter-ar run on sonnet and only when a brief sets Arabic
in scope; every other reasoning specialist and every verifier runs on sonnet; human-gate
inherits, it is a gate, not an LLM step.

## Stream coverage check

Every stream and entry point has a named owner. No stream is silently held by the orchestrator.

1 intake -> strategy-lead. 2 strategy -> strategy-lead. 3 creative -> creative-director
(concept) plus designer (execution and visual QA). 4 copy -> copywriter-ar (Arabic, primary)
plus copywriter-en (English variants). 5 build -> paid-build-engineer. 6 conversion ->
web-design-director and web-designer (web design) feeding conversion-engineer (page and gate)
plus data-tracking-engineer (events and warehouse).
7 lifecycle -> lifecycle-architect. 8 monitoring -> analytics-reporter plus
data-tracking-engineer (warehouse plumbing). 9 reporting -> analytics-reporter.
Entry point C organic acquisition -> organic-social, feeding the signup gate then lifecycle.

Acquisition channels (reuse streams 2, 3, 4, 8, 9, feed the conversion path): paid performance
-> performance-marketer (plans) plus paid-build-engineer (stages). SEO -> seo-specialist. Blog
and content -> content-marketer (briefs, routes copy to copywriter-ar and copywriter-en). App
and ASO -> aso-specialist. PR and communications -> pr-comms. Each owner plans and assembles an
approval-ready package and stops at the human gate; nothing publishes or spends without sign-off.

Cross-cutting: research-scout (borrow before inventing) plus `build-vs-buy-eval`;
competitor-analyst (competitor teardowns that feed strategy); brand-qa-reviewer plus
`arabic-copy-qa`, `english-copy-qa`, `design-qa`, and `web-design-qa` (the quality gate), with
`brand-voice-reviewer` plus `brand-voice-qa` as the deeper Arabic brand-voice gate;
accessibility-reviewer plus `accessibility-qa` (the accessibility gate on customer-facing pages
and emails, alongside design-qa); email-asset-reviewer plus `email-asset-qa` (the asset and visual
gate on stream-7 email image modules, every `data-slot="element"` cell); compliance-privacy-reviewer
plus `compliance-privacy-check` (the compliance and privacy gate); human-gate (sign-off).

## The two non-negotiable gates, on every path

1. Quality gate. Customer-facing asset runs its skill eval, then copy runs its language QA
   (`arabic-copy-qa` for AR, `english-copy-qa` for EN), visual assets run `design-qa` and web
   surfaces run `web-design-qa`, then `brand-qa-reviewer`. For anything that collects data, sends, or publishes,
   `compliance-privacy-reviewer` runs alongside brand-qa with `compliance-privacy-check`. A
   fail at any stage is a hard stop that returns to the author with exact fixes. It does not
   advance.
2. Human gate. The swarm assembles an approval-ready package, with the brand-qa and
   compliance verdicts attached, and stops. Nothing sends, publishes, or spends without
   explicit sign-off from Ahmed.
