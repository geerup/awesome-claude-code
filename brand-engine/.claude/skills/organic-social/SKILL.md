---
name: organic-social
description: Hub for organic social acquisition, owned by organic-social, the zero-media-cost entry point C that grows reach across the owned social accounts and feeds the signup gate then lifecycle. Use to plan organic content, schedule a post calendar, and run on-brand community engagement. Routes to organic-content-plan and community-engagement, and assembles the organic-package. Triggers on "organic social," "content plan," "post calendar," "what should we post," "community engagement," "reply to comments," "repurpose the video," "grow the social following."
---

# Organic Social Acquisition (hub)

Entry point C. Owns the organic side of acquisition: the content plan and post calendar
across the owned social accounts, and the on-brand community engagement that turns reach into
signups. Owner: `organic-social`. Mode: reasoning for the plan, gated for any publish. This
hub does not write captions and does not publish. It validates inputs, routes to the right
sub-skill, and assembles the `organic-package`.

Organic acquisition lands traffic on the signup gate (email or WhatsApp), which is the entry
to lifecycle (stream 7). The owned social audience is a real asset and a zero-media-cost
channel.

## When to use

- A brief with `entry_point: organic social` (or a channel_plan that includes owned social).
- The campaign needs an organic content plan, a post calendar, or community engagement
  guidance.
- The orchestrator dispatches organic social (per `runtime/stream-ownership.md`).

## Sub-skills (routing)

- `organic-content-plan`: the content plan and post calendar, mapped to the strategy angle
  and segments, with the channel mix across the owned accounts and a repurposing map that
  turns one asset into many formats. Use first; it sets what gets posted and when.
- `post-templates`: the reusable post-format scaffolds (story engagement sequence, countdown
  or launch story, value carousel, myth-buster carousel, skills roundup carousel, quote
  inspiration carousel), extracted and normalized from the team's organic copy doc. Use once
  the content plan calls a format and needs its proven beat-by-beat structure.
- `community-engagement`: on-brand reply and engagement guidance for the community, with the
  escalation rules for sensitive or compliance-touching messages. Use for how the team
  responds in comments and DMs once content is live.

Route: content plan first to fix what gets posted, then `post-templates` to scaffold each
chosen format, then community engagement for how the community is handled around it. All feed
the same `organic-package`.

## Inputs

- The `strategy-artifact` (stream 2): segments, the angle, offer framing, channel_plan,
  success_metric.
- The active `briefs/` file: objective, the owned social accounts in scope, posting cadence,
  the campaign window.
- Captions and copy are routed to `copywriter-en` (English-first, the default author) and, only
  when a brief sets Arabic in scope, `copywriter-ar`, never written here. Visual assets come
  from `creative-director` and the designer. Video repurposing (one video into many formats)
  uses Blotato, gated and added on approval.
- `context/profiles/maharat/organic-social-style.md`: the voice-in-practice, the formatting legend, the
  bilingual convention, the engagement and CTA mechanics, and the reconciliation of the source
  organic copy doc against the engine hard rules. Read alongside `brand-voice.md`.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the gap
with an invented value. Never invent an offer title, the content lineup, a subject, a price,
or a target.

## Steps

1. Validate the incoming envelope: right campaign_id, strategy-artifact present with the
   angle, segments, and success_metric, open_items read. If incomplete, return it.
2. Route to `organic-content-plan` to build the content plan, the post calendar, the channel
   mix, and the repurposing map.
3. Route to `community-engagement` for the reply and escalation guidance around the posts.
4. Route captions to `copywriter-en` (default), or to `copywriter-ar` when a brief sets Arabic
   in scope; route assets to `creative-director` and the designer. Sequence QA-passed copy
   variants by id; do not write copy here.
5. Set `distribution_routing`: which post goes to which account and segment, and where the
   click lands (the signup gate, the entry to lifecycle).
6. Assemble the `organic-package` and stop at the human gate. Posting is one gated action;
   nothing publishes without explicit sign-off.

## Output: the organic-package

```
content_plan          the angle-to-content map: themes, formats, and the segment each serves
post_calendar         ordered posts, each with date, account, format, and a copy variant ref
distribution_routing  which post goes to which owned account and segment, and the gate it lands
publish_on_approval   one plain sentence of what publishing does and to which accounts
repurposing_notes     how one asset becomes many formats across the channel mix
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs), per `runtime/handoff-contract.md`.

## How this connects to the contract and gates

- Consumes: `strategy-artifact` (stream 2), QA-passed captions from `copywriter-ar` and the
  English copywriter, assets from `creative-director`.
- Produces: the `organic-package`. It feeds the signup gate (stream 6) then lifecycle
  (stream 7), and its reach data feeds monitoring (stream 8).
- Gate before advance: skill eval, then `arabic-copy-qa` on all Arabic captions, then
  `brand-qa-reviewer`, then the human gate for any publish, per `runtime/verification.md`.

## Hard rules

- The hub plans and routes; it never writes captions and never publishes. Every post
  references a QA-passed copy variant by id.
- Posting is a gated action. Nothing publishes without the human gate. Approval is per
  publish action and per campaign. Silence is not approval.
- Never invent a Skill Path title, the content lineup, an instructor name, an offer, a price,
  or a target. Missing, stop and ask.
- No accreditation claims, no fundraising, roadmap, or unannounced plans in any post.
- Never put personal or sensitive data in a tracking URL parameter.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.
