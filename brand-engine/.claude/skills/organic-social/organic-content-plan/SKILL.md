---
name: organic-content-plan
description: Build the organic content plan and post calendar for a campaign, mapped to the strategy angle and segments, with a channel mix across the owned social accounts and a repurposing map that turns one asset into many formats. Use to decide what gets posted, where, and when. Triggers on "content plan," "post calendar," "what should we post," "the posting schedule," "repurpose the video," "channel mix." Sub-skill of organic-social, owned by organic-social.
---

# Organic Content Plan (organic-social sub-skill)

Turns the strategy angle and segments into a concrete content plan and a dated post calendar
across the owned social accounts, plus a repurposing map that gets the most out of every
asset. It does not write captions and does not publish. It decides what gets posted, to which
account, for which segment, and when.

Owner: `organic-social`. Mode: reasoning. Feeds the `organic-package` assembled by the
`organic-social` hub.

## When to use

- The `organic-social` hub routes here to set the content plan before community engagement.
- A campaign needs a post calendar mapped to its angle and segments.
- One source asset (for example a long video) needs a repurposing map into many formats.

## Inputs

- The `strategy-artifact` (stream 2): the angle, the segments and their definitions, offer
  framing, channel_plan, success_metric.
- The active `briefs/` file: the owned social accounts in scope, posting cadence, the campaign
  window, the objective.
- Source assets from `creative-director` and the designer (the master assets to repurpose).
- Captions are written by `copywriter-ar` and the English copywriter, referenced here by
  variant id, never written here.

If the accounts in scope, the cadence, or the window are not in the brief, stop and ask. Do
not invent a posting frequency, an account, an offer, a price, or a target. Never invent a
Skill Path title, the content lineup, or an instructor name.

## Steps

1. Restate the angle and segments from the strategy-artifact. The plan serves them; it does
   not introduce a new message.
2. Build the content plan: themes and formats mapped to the angle, each tied to the segment
   it serves. Formats are platform-native (for example short video, carousel, single image,
   story, text post).
3. Set the channel mix across the owned accounts in scope from the brief. Note where the same
   audience overlaps so the calendar does not over-post one segment.
4. Build the post calendar: ordered posts, each with date (inside the campaign window),
   account, format, the segment it serves, and a copy variant ref for the caption.
5. Build the repurposing map: take one master asset and route it into many formats and
   accounts. Video repurposing into clips and formats uses Blotato, which is gated and added
   on approval; while it is not approved, note the manual fallback. Note the slot but do not
   assume the tool is live.
6. Set distribution routing: which post lands the click on the signup gate (the entry to
   lifecycle), with no personal or sensitive data in any tracking parameter.
7. Hand the plan to the hub for assembly into the `organic-package`. Run the skill eval.

## Output

Use `templates/organic-content-plan.md`. The shape:
- content_plan (themes and formats mapped to the angle and segment),
- post_calendar (dated posts, each with account, format, segment, copy variant ref),
- channel_mix (the owned accounts in scope and how they split),
- repurposing_map (one asset into many formats, with the tool slot noted as gated),
- distribution_routing (which post lands on the signup gate).

Internal plan that feeds the `organic-package`. It does not cross a boundary on its own.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and completeness.
- The captions run the gate stack: skill eval, `arabic-copy-qa` on Arabic, then
  `brand-qa-reviewer`, per `runtime/verification.md`. Publishing is a human-gate action.

## Hard rules

- The plan sequences copy by variant id; it never writes captions and never publishes.
- Do not invent a posting cadence, an account, a Skill Path title, the content lineup, an
  instructor name, an offer, a price, or a target. Missing, stop and ask.
- Blotato video repurposing is gated and added on approval. Note the slot; do not assume it
  is live. Use the manual fallback until approved.
- No accreditation claims, no fundraising, roadmap, or unannounced plans.
- Never put personal or sensitive data in a tracking URL parameter.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.
