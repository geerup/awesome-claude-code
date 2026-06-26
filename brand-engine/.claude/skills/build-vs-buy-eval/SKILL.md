---
name: build-vs-buy-eval
description: Cross-cutting skill run via /research by research-scout. Use to weigh a tool, platform, or framework before the engine builds or adopts anything, triggers on "build or buy," "is there a tool for this," "research the platform," "should we adopt," "/research." Reasoning only. Checks for an existing framework or tool first, scores candidates on a fixed set of criteria where Arabic capability is the decisive filter for any generative tool, and proposes with a clear recommendation and the open items that block a final decision. It never adopts or wires a tool: adoption is Ahmed's call and lands as a settings.json allowlist change.
---

# Build vs Buy Eval (cross-cutting)

Borrow before inventing. Owned by `research-scout`, reasoning mode, run via the `/research`
command. Before the engine builds a workflow or adopts a tool, this skill checks whether an
existing framework, platform, or tool already does the job, scores the candidates, and
proposes. It never adopts.

## Purpose

Turn an open tool or capability question into a sourced, scored recommendation: what the
capability is, which candidates exist, how each scores on the fixed criteria, and the clear
recommendation plus the open items that block a final decision. A recommendation is not an
adoption.

## When to use

- The `/research` command is invoked.
- An open tool or platform item needs deciding (for example the email and WhatsApp platform,
  per `context/04-tools-and-access.md`).
- Before adopting any MCP or external tool, or before building a workflow from scratch.

## Inputs

- The capability question: what is needed, for which stream, under what constraints.
- `context/04-tools-and-access.md`: the existing stack and the MCP candidates to trial.
- `context/brand-voice.md`: the Arabic and mechanical rules a generative tool must clear.
- For generative tools, a real Arabic output sample to test (no tatweel, Western numerals,
  RTL-safe).

## Steps

1. Frame the capability: what job, which stream, the constraints (English-first, GCC data,
   budget, volume). Note what the brief and context already say.
2. Check for an existing framework or tool first. Borrowing beats building.
3. Apply the Arabic gate to any generative tool: a candidate that cannot produce clean Arabic
   (no tatweel, Western numerals, RTL-safe) is ruled out regardless of its other strengths.
   This is the decisive filter, scored and applied before the rest.
4. Score the shortlist on the fixed criteria (see the scorecard): Arabic capability (decisive,
   for generative tools), fit to the SOP, GCC and PDPL data fit, cost vs volume, integration
   effort, lock-in and exit, maturity and support. Before scoring, set a weight and a must-have
   versus nice-to-have flag (MoSCoW-style) per criterion, then take a weighted total. A
   candidate that fails any must-have criterion is ruled out regardless of total. Arabic
   capability stays the existing hard gate, applied before weighting, and a fail rules a
   generative candidate out regardless of weight, flag, or weighted total.
5. Recommend one path: buy a named candidate, build, or hold pending an open item. State the
   open items that block a final decision.
6. Run the skill eval for structure and completeness.

## Output

Use `templates/build-vs-buy-scorecard.md`. The shape:
- capability and constraints,
- existing-tool check,
- the scored shortlist (Arabic gate flagged for generative tools),
- a single recommendation (buy named / build / hold),
- open items that block the decision.

The output is a research readout (for example in `references/`) and a recommendation to
strategy-lead and the orchestrator. It is a proposal, not an adoption.

## Hard rules

- Propose, never adopt or wire a tool. Adoption is Ahmed's call and lands as a `settings.json`
  allowlist change made by a human, not by this skill.
- For generative tools, Arabic capability is the decisive filter. Test real Arabic output
  before recommending. Default to Claude for Arabic copy.
- Borrow before inventing: check for an existing tool before proposing to build.
- Keep readouts factual and sourced. No em dashes, no tatweel, Western numerals only.
