---
name: pr-comms
description: Hub for public relations and communications, owned by pr-comms. Use when a campaign needs an announcement, a press release, a media list and outreach plan, or a guardrail check on what can be said publicly. Routes to press-release, media-list-outreach, and announcement-plan, and assembles the pr-package. Triggers on "press release," "announcement," "media list," "press outreach," "what can we say publicly," "PR plan," "media relations."
---

# PR and Communications (hub)

Owns the public relations side of a campaign: the announcement plan that fixes what may be
said and what must stay out, the press release, and the media list and outreach plan. Owner:
`pr-comms`. Mode: reasoning for the plan, gated for any distribution or publish. This hub does
not write final copy and does not distribute. It validates inputs, routes to the right
sub-skill, and assembles the `pr-package`.

PR carries the heaviest guardrail load in the engine. Public statements can embarrass or
expose the brand. The hub enforces one hard rule above all: nothing in any PR output names an
unannounced plan, a roadmap, fundraising, or an unconfirmed instructor. Only what is already
public or confirmed in the brief may appear. When in doubt, it stays out and becomes an open
item.

## When to use

- A brief with a public announcement in scope, or a channel_plan that includes PR.
- The campaign needs a press release, a media list, an outreach plan, or a ruling on what can
  be said publicly.
- The orchestrator dispatches PR and communications (per `runtime/stream-ownership.md`).

## Sub-skills (routing)

- `announcement-plan`: the guardrail check first. Fixes what can be said and what must stay
  out, and produces the `guardrail_check` that gates any announcement. Use first; nothing
  else runs until the announcement boundary is set.
- `press-release`: the English-first press release built only from public or brief-confirmed
  facts, with quote approval tracked as an open item. Use after the announcement plan clears.
- `media-list-outreach`: the target media list and the outreach plan, with no mishandling of
  personal data. Outreach is a gated action. Use after the release is drafted.

Route: announcement plan first to set the boundary, then the press release inside that
boundary, then the media list and outreach to distribute it. All three feed the same
`pr-package`.

## Inputs

- The `strategy-artifact` (stream 2): the angle, segments, offer framing, channel_plan.
- The active `briefs/` file: the announcement objective, what is confirmed public, the
  approved spokesperson and quote source, the window.
- Final copy is routed to `copywriter-ar` (English-first) and the English copywriter, never
  written here. The release runs the copy QA gates before it is package-ready.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the gap
with an invented value. Never invent a Skill Path title, the content lineup, an instructor
name, an offer, a price, or a target.

## Steps

1. Validate the incoming envelope: right campaign_id, strategy-artifact present with the angle
   and channel_plan, open_items read. If incomplete, return it.
2. Route to `announcement-plan` to set what can be said and what must stay out, and to produce
   the `guardrail_check`. No release or outreach proceeds until this clears.
3. Route to `press-release` to draft the English-first release inside the announcement
   boundary, with quote approval as an open item.
4. Route to `media-list-outreach` to build the target media list and the outreach plan, with
   no personal data mishandled and outreach marked as a gated action.
5. Route final copy to `copywriter-ar` and the English copywriter; run the copy QA gates,
   compliance, then brand QA. Reference QA-passed copy by id; do not write copy here.
6. Assemble the `pr-package` and stop at the human gate. Distribution and publishing are gated
   actions; nothing sends or publishes without explicit sign-off.

## Output: the pr-package

```
announcement_plan   what can be said and what must stay out, with the campaign window
press_release_ref   the QA-passed release reference, English-first, public facts only
media_list          target outlets and contacts, with no personal data mishandled
guardrail_check     the pass or fail that gates any announcement, with the items held out
publish_on_approval one plain sentence of what distribution does and to whom
open_items          quote approval, spokesperson confirmation, anything held out, and more
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs), per `runtime/handoff-contract.md`.

## How this connects to the contract and gates

- Consumes: `strategy-artifact` (stream 2), QA-passed copy from `copywriter-ar` and the
  English copywriter.
- Produces: the `pr-package`. It assembles an approval-ready package and stops at the human
  gate. Distribution feeds outreach only after sign-off.
- Gate before advance: skill eval, then `arabic-copy-qa` on Arabic copy and `english-copy-qa`
  on English copy, then `compliance-privacy-check` for outreach and data handling, then
  `brand-qa-reviewer`, then the human gate for any distribution or publish, per
  `runtime/verification.md`.

## Hard rules

- The hub plans and routes; it never writes final copy and never distributes. Every public
  line references a QA-passed copy variant by id.
- Distribution and publishing are gated actions. Nothing sends or publishes without the human
  gate. Approval is per distribution action and per campaign. Silence is not approval.
- PR hard rule: never name an unannounced plan, a roadmap, fundraising, or an unconfirmed
  instructor. Only what is already public or confirmed in the brief may appear. In doubt, it
  stays out and becomes an open item.
- Never invent a Skill Path title, the content lineup, an instructor name, an offer, a price,
  or a target. Missing, stop and ask.
- No accreditation claims anywhere in any release, pitch, or quote.
- Never put personal or sensitive data in a tracking URL parameter, and never mishandle a
  journalist's personal contact data.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.
