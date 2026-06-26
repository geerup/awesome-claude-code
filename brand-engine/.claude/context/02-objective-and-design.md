# 02-objective-and-design: what we build and the principles

Background and thinking. The runnable spec is `runtime/`. This file explains the why.

## The objective

Build a reusable, campaign-agnostic agentic marketing engine. Not a one-off campaign. Any
future campaign is an input: hand the engine a brief and the same workflows produce
approval-ready work. Different campaigns, same machine.

End state: an orchestrator plus a swarm of specialist subagents and skills that take a brief
and produce approval-ready marketing output, with a human-review gate before anything sends
or spends.

## Design principles

1. Campaign-agnostic. Targets, budgets, offers, and copy are runtime inputs from the brief,
   never hard-coded into a workflow, agent, or skill.
2. Define the work before the tools. The ideal SOP is designed tool-agnostic first.
   Automation and tool choice come second.
3. Do not assume or adopt a tool without approval. Research, weigh on build-vs-buy criteria,
   propose. Approval comes from Ahmed.
4. Human-review gate. Output is approval-ready, not auto-sent. Nothing publishes, sends, or
   spends without explicit sign-off.

## The reasoning vs execution split

- Reasoning: strategy, copy, and creative direction, done by Claude grounded in `context/`.
- Execution: posting an ad, sending a sequence, publishing a page, writing tracking to prod.
  Gated, tool-bound, and never runs without approval.

## Build-vs-buy

Before adopting any tool, run it through `skills/build-vs-buy-eval`. Borrow before inventing:
`research-scout` checks for an existing framework or tool first. Arabic capability is the
decisive filter for any generative tool. Default to Claude for Arabic copy.

## Quality as a gate

`brand-qa-reviewer` runs on every customer-facing asset. Arabic copy passes `arabic-copy-qa`
first. Each skill ships an `evals/evals.json` that encodes its acceptance checks. A draft
that fails a gate does not advance. See `runtime/verification.md`.

## House rules

No em dashes, no tatweel, Western numerals, empowering framing, English-first, no accreditation
claims. These apply to every file and every output.
