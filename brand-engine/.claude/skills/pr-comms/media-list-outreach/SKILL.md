---
name: media-list-outreach
description: Build the target media list and the outreach plan for a campaign, with no mishandling of journalist personal data. Use after the release is drafted, to plan who to reach and how. Outreach is a gated action; nothing sends without the human gate. Triggers on "media list," "press outreach," "who do we pitch," "outreach plan," "journalist list," "media relations." Sub-skill of pr-comms, owned by pr-comms.
---

# Media List and Outreach (pr-comms sub-skill)

Builds the target media list and the outreach plan for a campaign: which outlets and
contacts to reach, the angle for each, and the sequence of the pitch. It handles journalist
contact data carefully and never mishandles or exposes it. It plans outreach; it does not
send. Outreach is a gated action behind the human gate.

Owner: `pr-comms`. Mode: reasoning for the plan, gated for any outreach. Feeds the
`pr-package` assembled by the `pr-comms` hub. This runs after the press release is drafted.

## When to use

- The `pr-comms` hub routes here after the press release is drafted.
- A campaign needs a target media list and an outreach plan.
- The team needs the pitch sequence and the data-handling rules before any outreach.

## Inputs

- The drafted, QA-passed `press-release` reference and its open items.
- The cleared `announcement-plan`: the sayable set and the hold-out set, so the pitch stays
  inside the boundary.
- The `strategy-artifact` (stream 2): the angle, segments, channel_plan.
- The active `briefs/` file: the target markets (GCC, primary Saudi Arabia), the window, any
  named outlets or contacts that are confirmed.

If the target markets, the window, or a contact source are not in the brief, stop and ask. Do
not invent an outlet, a contact, a journalist email, an offer, a price, or a target.

## Steps

1. Confirm the press release is drafted and the announcement boundary is set. The pitch draws
   only from the sayable set; nothing held out leaks into a pitch.
2. Build the target media list: outlets and named contacts mapped to the target markets and
   the angle. Each entry carries the outlet, the contact role, the relevance to the angle, and
   the contact channel. Do not invent a contact; flag any contact source that is not confirmed.
3. Handle data carefully: a journalist's personal contact data is handled on a need-to-know
   basis, never echoed into a tracking parameter, a public thread, or a shared link, and never
   exposed beyond the outreach. Surface the Saudi PDPL and data-residency open item when
   relevant. Route to `compliance-privacy-reviewer` for the data-handling check.
4. Plan the outreach sequence: the order of contact, the angle per outlet, the embargo or
   timing if any, and the follow-up cadence. Each pitch references the QA-passed release and a
   QA-passed pitch copy variant by id; the pitch copy is written by the copywriters, not here.
   Brief the pitch shape for the copywriters: under about 100 words, beat-specific,
   personalized to the reporter's prior coverage, one clear ask, and a tested subject line. An
   off-beat or generic pitch is rejected at high rates, so relevance to the reporter's beat is
   non-negotiable. The pitch still runs the full copy QA, compliance, and brand gates.
4a. Handle any embargo as opt-in, not a label. An embargo is valid only once the journalist
   agrees in advance, so ask first: send a short interest note, record the journalist's opt-in,
   and only then share the full release. Marking a release "embargoed" without a recorded
   opt-in is not binding and raises leak risk. When an embargo is agreed, mark the embargo line
   (date, time, timezone) at the top of the release and repeat it in the pitch subject and
   body. Keep embargo lists small and trusted, on the order of 5 to 10 beat reporters; every
   extra recipient raises leak risk. Carry "embargo not yet agreed by recipient" as a distinct
   open item, separate from "embargo not confirmed."
5. Mark outreach as a gated action: nothing sends without the human gate. State one plain
   sentence of what distribution does and to whom.
6. Hand the media list and the outreach plan to the hub for assembly into the `pr-package`.
   Run the skill eval.

## Output

Use `templates/media-list-and-outreach.md`. The shape:
- media_list (outlets and contacts mapped to the markets and angle, no invented contacts),
- data_handling (need-to-know, no personal data mishandled, PDPL open item when relevant),
- outreach_plan (order, angle per outlet, timing, follow-up, pitch copy variant refs, pitch
  shape note, embargo opt-in status per recipient),
- distribution_note (outreach is a gated action, one plain sentence of what it does),
- open_items (contact source not confirmed, PDPL and data-residency, embargo not confirmed,
  embargo not yet agreed by recipient).

Internal plan that feeds the `pr-package`. It does not cross a boundary on its own.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and completeness.
- Pitch copy runs the gate stack: skill eval, then `arabic-copy-qa` on Arabic and
  `english-copy-qa` on English, then `compliance-privacy-check` for the data handling and the
  send, then `brand-qa-reviewer`, per `runtime/verification.md`. Outreach is a human-gate action.

## Hard rules

- The plan plans outreach; it never writes pitch copy and never sends. Every pitch references
  a QA-passed copy variant by id.
- Outreach is a gated action. Nothing sends without the human gate. Approval is per outreach
  action and per campaign. Silence is not approval.
- A journalist's personal contact data is need-to-know, never mishandled, never echoed into a
  tracking parameter or a public thread, never exposed beyond the outreach.
- The pitch draws only from the sayable set. PR hard rule: no unannounced plan, roadmap,
  fundraising, or unconfirmed instructor name in any pitch.
- The pitch is under about 100 words, beat-specific, personalized to the reporter's prior
  coverage, with one clear ask and a tested subject line. Relevance to the beat is required.
- An embargo is opt-in only. It is valid only after the journalist agrees in advance and the
  opt-in is recorded; the full release is shared only then. Marking "embargoed" without a
  recorded opt-in is not binding. Keep embargo lists small, 5 to 10 trusted beat reporters.
- Never invent an outlet, a contact, a Skill Path title, the content lineup, an instructor
  name, an offer, a price, or a target. Missing, stop and ask.
- No accreditation claims in any pitch.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.
