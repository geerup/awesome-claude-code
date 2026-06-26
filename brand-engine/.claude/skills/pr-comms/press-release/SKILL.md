---
name: press-release
description: Draft the English-first press release for a campaign, built only from public or brief-confirmed facts, with quote approval tracked as an open item. Use after the announcement plan clears, to write the release inside the announcement boundary. Triggers on "press release," "draft the release," "write the press statement," "the announcement copy," "press statement." Sub-skill of pr-comms, owned by pr-comms.
---

# Press Release (pr-comms sub-skill)

Drafts the English-first press release inside the boundary the announcement plan set: only
public or brief-confirmed facts, no roadmap, no fundraising, no accreditation claim, no
unconfirmed instructor name. It structures the release and routes the language to the
copywriters; it does not invent facts and it does not distribute.

Owner: `pr-comms`. Mode: reasoning. Feeds the `pr-package` assembled by the `pr-comms` hub.
This runs only after `announcement-plan` clears its guardrail check.

## When to use

- The `pr-comms` hub routes here after the announcement plan sets the boundary.
- A campaign needs a press release drawn strictly from sayable facts.
- A release draft needs the structure and the sayable-only discipline before it goes to QA.

## Inputs

- The cleared `announcement-plan`: the sayable set, the hold-out set, the approved
  spokesperson, the guardrail_check result.
- The `strategy-artifact` (stream 2): the angle, offer framing, channel_plan.
- The active `briefs/` file: the announcement objective, what is confirmed public, the
  approved spokesperson and quote source, the window.
- Final Arabic copy is written by `copywriter-ar` and English by the English copywriter,
  referenced here by variant id, never written here.

If a fact is not in the sayable set, it does not enter the release. Do not promote an
unconfirmed fact by assuming it. Never invent a Skill Path title, the content lineup, an
instructor name, an offer, a price, or a target.

## Steps

1. Confirm the announcement plan cleared. If the guardrail_check is not a pass, stop and
   return to `announcement-plan`. No release is drafted on an open boundary.
2. Structure the release: headline, dateline, lead paragraph, body, the boilerplate "about
   Maharat," and the media contact. English-first; the English version follows the same facts
   and the same boundary, it is not a loose translation.
3. Fill the body from the sayable set only. Each claim traces to a sayable item. A claim with
   no sayable source is dropped, not softened.
4. Place the quote: attribute only to the approved spokesperson from the announcement plan.
   The quote text and its approval are an open item until confirmed. Do not attribute an
   unconfirmed quote.
5. Write the boilerplate from `context/01-brand-brief.md` stable facts only. No roadmap, no
   fundraising, no accreditation implication, no unannounced plan.
6. Route the Arabic copy to `copywriter-ar` and the English copy to the English copywriter.
   Reference QA-passed variants by id. Run the gate stack: copy QA, compliance, then brand QA.
7. Hand the release reference and its open items to the hub for assembly into the
   `pr-package`. Run the skill eval.

## Output

Use `templates/press-release.md`. The shape:
- headline and dateline (English-first),
- lead paragraph (the single sayable news, plain and empowering),
- body (each claim traced to a sayable item),
- quote (approved spokesperson only, approval as an open item),
- boilerplate (stable facts from the company brief, no roadmap or fundraising),
- media_contact (the named contact, no personal data mishandled),
- open_items (quote approval, spokesperson confirmation, anything held out).

Internal draft reference that feeds the `pr-package`. It does not cross a boundary on its own.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and completeness.
- The release runs the gate stack: skill eval, then `arabic-copy-qa` on Arabic copy and
  `english-copy-qa` on English copy, then `compliance-privacy-check`, then `brand-qa-reviewer`,
  per `runtime/verification.md`. Distribution is a human-gate action.

## Hard rules

- The release draws only from the sayable set. A claim with no sayable source is dropped.
- PR hard rule: never name an unannounced plan, a roadmap, fundraising, or an unconfirmed
  instructor. Only what is already public or confirmed in the brief may appear. In doubt, it
  stays out and becomes an open item.
- A quote is attributed only to an approved spokesperson; quote approval is an open item.
- Never invent a Skill Path title, the content lineup, an instructor name, an offer, a price,
  or a target. Missing, stop and ask.
- No accreditation claims. A completion certificate is never described as accredited.
- The hub never distributes the release on its own; distribution is a human-gate action.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.
