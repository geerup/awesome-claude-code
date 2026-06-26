# Maharat Marketing Engine

> ADAPTED: This is the Brand & Career Engine, a personal-brand adaptation of the original
> Maharat Marketing Engine. The machine described below (agents, runtime, skills, SOPs, gates)
> is reused unchanged; the active facts are the `me` profile and the language is English-first.
> The original Maharat engine is preserved in full under `context/profiles/maharat/` (nothing
> was thrown out). Some Maharat-specific examples below now describe that archived reference
> profile. Authoritative current rules live in `CLAUDE.md` and `context/profiles/_README.md`.


A reusable, campaign-agnostic agentic marketing engine, run with Claude. Hand it a campaign
brief and the same workflows produce approval-ready marketing output, behind a human gate.
Not a one-off campaign. Different campaigns, same machine.

House rule, everywhere, in any language or file: no em dashes, no tatweel or kashida,
Western numerals only, English-first, empowering framing, never imply certificate accreditation.

---

## Architecture

```
.claude/
  CLAUDE.md          Always-loaded operating rules (the constitution)
  README.md          This file
  settings.json      MCP allowlist (empty until Ahmed approves a tool)

  context/           Single source of truth (stable facts, not campaign data)
  briefs/            Runtime inputs, one per campaign (the only per-campaign input)
  agents/            The team (the roster is agents/_AGENTS-INDEX.md)
  skills/            Knowledge, grouped by stream. Each stream is a hub that routes to
                     sub-skills. Every skill: SKILL.md + evals/evals.json + templates/
  runtime/           The conductor layer: how agents and skills run as a swarm
  sops/              Long-form standard operating procedures for the deepest streams
  commands/          /new-campaign, /research
  references/        Research readouts
  outputs/           Generated artifacts per campaign
```

The split: `skills/` are the knowledge, `agents/` are the team, `context/` is the truth,
`briefs/` are the per-campaign inputs, `runtime/` is how they run together.

## How a run works (the prompting strategy)

- Orchestrator plus specialists. The orchestrator reads the brief, holds the whole-funnel
  view, and dispatches each stream to the specialist that owns it. Specialists know only
  their stream. See `agents/_AGENTS-INDEX.md` and `runtime/stream-ownership.md`.
- Reasoning vs execution split. Strategy, copy, and creative direction are reasoning,
  grounded in `context/`. Execution (post an ad, send a sequence) is gated, tool-bound, and
  never runs without approval.
- Context before generation. Every agent loads `CLAUDE.md` and `context/brand-voice.md`,
  plus its stream SOP or skill, before producing anything. Facts from `context/`, variables
  from the brief.
- Quality as a gate. `brand-qa-reviewer` runs on every customer-facing asset. Arabic copy
  passes `arabic-copy-qa` first. Each skill ships an `evals/evals.json`. A draft that fails
  a gate does not advance. See `runtime/verification.md`.
- Borrow before inventing. `research-scout` plus `build-vs-buy-eval` check for an existing
  framework or tool first.

The four swarm shapes (pipeline, parallel fan-out, verify-then-advance, human gate) are
specified in `runtime/SWARM.md`. The artifacts that cross stream boundaries are in
`runtime/handoff-contract.md`. The email path specifically, end to end (the streams, the owning
agent and skill for each, the spec-to-render build path, and the gate stack), is mapped with
clickable repo links in `runtime/email-pipeline-map.md`.

## MCP strategy

No tool is adopted without a build-vs-buy pass (`skills/build-vs-buy-eval`) and Ahmed's
approval. Arabic capability is the decisive filter for any generative tool; default to
Claude for Arabic copy. Approved MCP servers are listed in `settings.json`
`enabledMcpjsonServers` and defined in the committed root `.mcp.json`, which lists only
servers with valid runtime wiring and interpolates credentials from `${ENV_VAR}` so no secret
is committed (full template at `.claude/.mcp.json.example`). Candidates still under
consideration are in `settings.json` under `_mcp_candidates_pending_approval` and in
`context/04-tools-and-access.md`.

Adopted (June 2026): `firecrawl` (research-scout), `blotato` (creative-director and
organic-social), and the `email-whatsapp-platform` slot (lifecycle-architect and
data-tracking-engineer). Each still needs its runtime credentials, and the email and WhatsApp
vendor is still an open item, so its live send wiring stays blocked until the vendor and the
PDPL data-residency decision are confirmed. An Ortto REST send slot (`ortto-rest`, streams 5 and
7) sits in the allowlist as proposed (2026-06-16), inert until its wrapper is built and key
provisioned; sending stays governed by the per-campaign approval and `runtime/send-safeguards.md`.

Execution tools (Meta Ads, Google Ads, the email and WhatsApp platform) stay gated behind
the human gate even after they are adopted. Adoption grants the engine the ability to
assemble and stage, never to send or spend on its own.

## How to run

1. Load `CLAUDE.md` and `context/brand-voice.md` (every session).
2. Pick or write the active brief in `briefs/`.
3. The orchestrator resolves the entry point and dispatches per `runtime/stream-ownership.md`.
4. Every customer-facing asset passes the quality gate (`runtime/verification.md`).
5. The swarm assembles an approval-ready package and stops at the human gate. Nothing sends.

## First build

The non-payer email flow: `briefs/2026-06-nonpayer-email.md`. Owned audience, enters at
stream 7 (lifecycle), zero media cost. The deepest-built path. See
`sops/07-lifecycle-nonpayer-email.md`.

## Roster (28 agents)

- Reasoning: `orchestrator`, `strategy-lead`, `research-scout`, `competitor-analyst`,
  `creative-director`, `designer`, `copywriter-ar`, `copywriter-en`, `brand-copywriter-ar`,
  `organic-social`, `lifecycle-architect`, `analytics-reporter`, `web-design-director`,
  `web-designer`.
- Channel owners: `performance-marketer` (paid strategy), `seo-specialist`,
  `content-marketer` (blog), `aso-specialist` (app and ASO), `pr-comms`.
- Execution (gated): `paid-build-engineer`, `conversion-engineer`, `data-tracking-engineer`.
- Verifiers and gate: `brand-qa-reviewer`, `brand-voice-reviewer`, `compliance-privacy-reviewer`,
  `accessibility-reviewer`, `email-asset-reviewer`, `human-gate`.

The full roster, with the stream each owns, its mode, model, and handoffs, is in
`agents/_AGENTS-INDEX.md`.

Each agent declares a `model` and a `tools` allowlist in its frontmatter, which enforces the
reasoning-versus-execution split (reasoning agents cannot reach execution tools; live
execution MCP tools stay gated and documented in the body, never granted by default).

## Entry points and channels

- A, paid acquisition: `performance-marketer` plans the media, `paid-build-engineer` stages it.
- B, owned audience: the non-payer email flow, enters at stream 7, owner `lifecycle-architect`.
- C, organic acquisition: the ~180,000 followers, owner `organic-social`, zero media cost.
- SEO: `seo-specialist`. Blog and content: `content-marketer`. App and ASO: `aso-specialist`.
  PR and communications: `pr-comms`. Each reuses streams 2, 3, 4, 8, 9 and the conversion path.

## Status

- Foundation and runtime: complete.
- All 9 streams plus 5 acquisition channels: built with hub plus sub-skills, evals, and
  templates. Long-form SOPs for every stream (1 to 9) and every channel.
- Cross-cutting gates: `arabic-copy-qa`, `english-copy-qa`, `design-qa`, `web-design-qa`,
  `email-asset-qa`, `accessibility-qa`, `compliance-privacy-check`, `build-vs-buy-eval`.
- Email subsystem: the slotted live-component standard (`context/profiles/maharat/email-design-system.md` plus
  `runtime/email-module-map.md`), the spec-driven renderer (`scripts/email_render.py`), the
  house-style sweep, and the full gate stack. The straight line, with repo links, is in
  `runtime/email-pipeline-map.md`. The 7-step nurture-to-subscribe build exists for most of the
  roster under `outputs/`.
- Lead worked example: the Bassam Fattouh makeup 7-step (`outputs/2026-06-bassam-fattouh-makeup/`).
  14 enriched emails (AR and EN) passed the copy and brand gates and are staged as drafts in
  Ortto; the campaign waits at the human gate before the journey is wired and sent. Targeting and
  the send schedule are specified in the campaign folder.
- Instructor public status: bassam-fattouh, cedric-haddad, elda-choucair, and ragheb-alama are
  confirmed (owner, 2026-06-19); the rest of the roster stays unconfirmed until separately confirmed.
