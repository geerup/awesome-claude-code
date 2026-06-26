---
description: Research a tool, platform, competitor, or framework before the engine builds or adopts anything. Runs research-scout plus build-vs-buy-eval. Proposes, never adopts.
---

# /research

Borrow before inventing. Before the engine builds a workflow or adopts a tool, check whether
something already does the job, and weigh it. This command runs `research-scout` with the
`build-vs-buy-eval` skill. It proposes. It never adopts: adoption is Ahmed's call and lands
as a `settings.json` change.

## What to do

1. Frame the question: what capability is needed, for which stream, under what constraints
   (English-first, GCC data residency, budget, expected volume).
2. Research candidates. For any generative tool, Arabic capability is the decisive filter.
   Test real Arabic output (no tatweel, Western numerals, RTL-safe) before recommending.
   Default to Claude for Arabic copy.
3. Run the shortlist through `skills/build-vs-buy-eval`.
4. Write a readout to `references/` and give a clear recommendation plus the open items that
   block a final decision.

## The standing open item

The email and WhatsApp platform decision. First confirm any incumbent platform before
evaluating a switch. See `references/2026-06-email-whatsapp-platform-research.md`. Block the
lifecycle send wiring until the platform is named and approved.

## Rules

- Propose only. Never wire or adopt a tool. Approved tools go to `settings.json` by Ahmed.
- No em dashes, Western numerals. Keep readouts factual and sourced.

$ARGUMENTS
