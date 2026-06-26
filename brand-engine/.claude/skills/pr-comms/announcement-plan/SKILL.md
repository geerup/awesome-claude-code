---
name: announcement-plan
description: Set what a campaign can say publicly and what must stay out, and produce the guardrail_check that gates any announcement. Use first in any PR work to fix the announcement boundary before a release or outreach is drafted. Triggers on "announcement plan," "what can we say publicly," "what must stay out," "guardrail check," "PR boundary," "approve the announcement." Sub-skill of pr-comms, owned by pr-comms.
---

# Announcement Plan (pr-comms sub-skill)

Fixes the boundary of a public announcement before any release or outreach is written: what
may be said, what must stay out, and why. It produces the `guardrail_check`, the pass or fail
that gates any announcement in the campaign. It does not write the release and does not
distribute. It rules on what is sayable.

Owner: `pr-comms`. Mode: reasoning. Feeds the `pr-package` assembled by the `pr-comms` hub.
This runs first; nothing else in PR proceeds until the boundary is set and the guardrail
check passes.

## When to use

- The `pr-comms` hub routes here first, before the press release or the media list.
- A campaign needs a ruling on what can be announced publicly.
- A draft release or pitch needs the guardrail check before it advances.

## Inputs

- The `strategy-artifact` (stream 2): the angle, offer framing, channel_plan.
- The active `briefs/` file: the announcement objective, what is confirmed public, the
  approved spokesperson, the window.
- The standing guardrails in `CLAUDE.md`, `context/brand-voice.md`, and
  `context/01-brand-brief.md`.

If a fact is not confirmed public in the brief or context, it is not sayable. Do not promote
an unconfirmed fact to sayable by assuming it. Never invent a Skill Path title, the content
lineup, an instructor name, an offer, a price, or a target.

## Steps

1. Restate the announcement objective and the angle from the strategy-artifact. The boundary
   serves the objective; it does not soften the guardrails to reach it.
1a. State the news hook: a one-line "why this is news now," drawn only from the sayable set.
   The hook is the reason a journalist cares, a real milestone, launch, or data point already
   public or confirmed. It stays inside the boundary and is never forced; no newsjacking and no
   inventing a moment that is not real. A sayable announcement with no genuine hook is flagged
   as weak, not just passed, so the team can strengthen the hook or reconsider the timing.
2. List the sayable set: every fact that is already public or confirmed in the brief. Each
   item carries its source (public-already or brief-confirmed). Nothing enters this list on
   assumption.
3. List the hold-out set: everything that must stay out. This always includes unannounced
   plans, roadmap, fundraising, unconfirmed instructor names, unconfirmed Skill Path titles or
   content lineup, and any accreditation implication. Each hold-out item becomes an open item
   for the package.
4. Rule on the spokesperson and quote source: only an approved spokesperson may be quoted, and
   the quote is an open item until approved. Do not attribute a quote that is not confirmed.
5. Produce the `guardrail_check`: pass only if the proposed announcement draws solely from the
   sayable set and nothing from the hold-out set leaks in. A single hold-out leak is a fail
   that returns the draft with the exact offending span.
6. Hand the boundary and the guardrail check to the hub for assembly into the `pr-package`.
   Run the skill eval.

## Output

Use `templates/announcement-plan.md`. The shape:
- announcement_objective (restated from the brief and strategy-artifact),
- news_hook (one line, why this is news now, drawn only from the sayable set, flagged weak when
  there is no genuine hook, no forced newsjacking),
- sayable_set (each fact with its source: public-already or brief-confirmed),
- hold_out_set (unannounced plans, roadmap, fundraising, unconfirmed names and titles,
  accreditation, each becoming an open item),
- spokesperson_and_quote (the approved source, quote approval as an open item),
- guardrail_check (pass or fail, with the offending span on fail).

Internal plan that feeds the `pr-package`. It does not cross a boundary on its own.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and completeness.
- The guardrail check is the gate that any announcement passes before a release or outreach
  advances. The full release then runs the copy QA gates, compliance, and
  `brand-qa-reviewer`, per `runtime/verification.md`. Distribution is a human-gate action.

## Hard rules

- The plan rules on what is sayable; it never writes the release and never distributes.
- The news hook is drawn only from the sayable set and never forced. A sayable announcement
  with no genuine hook is flagged as weak, not silently passed. No newsjacking, no invented
  moment.
- PR hard rule: unannounced plans, roadmap, fundraising, and unconfirmed instructor names are
  always in the hold-out set. Only what is already public or confirmed in the brief is
  sayable. In doubt, it stays out and becomes an open item.
- Never invent a Skill Path title, the content lineup, an instructor name, an offer, a price,
  or a target. Missing, stop and ask.
- No accreditation claims. A completion certificate is never described as accredited.
- A quote is attributed only to an approved spokesperson; quote approval is an open item.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.
