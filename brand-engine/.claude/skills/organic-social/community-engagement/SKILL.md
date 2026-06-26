---
name: community-engagement
description: On-brand reply and engagement guidance for the community across the owned social accounts, with empowering tone and clear escalation rules for sensitive or compliance-touching messages. Use to decide how the team responds in comments and DMs once content is live, and when to route a message to the compliance-privacy-reviewer. Triggers on "community engagement," "reply to comments," "how do we respond," "handle the DMs," "engagement guidance," "what do we say back." Sub-skill of organic-social, owned by organic-social.
---

# Community Engagement (organic-social sub-skill)

Sets how the community is handled around live posts: the on-brand reply patterns, the tone,
and the escalation rules for anything sensitive or compliance-touching. It does not publish
posts and it does not approve a public reply on its own. It produces the guidance the team
and the human gate work from. Replies that go out are a gated action, like any publish.

Owner: `organic-social`. Mode: reasoning for the guidance, gated for any public reply.
Feeds the `organic-package` assembled by the `organic-social` hub.

## When to use

- The `organic-social` hub routes here after the content plan to set how comments and DMs
  are handled around the posts.
- The community needs reply guidance that stays on brand and empowering.
- A message touches compliance, privacy, accreditation, an unannounced plan, or a sensitive
  topic and the team needs to know when to escalate.

## Inputs

- The `strategy-artifact` (stream 2): the angle and segments, so replies stay on message.
- The active `briefs/` file: the owned accounts in scope and the campaign window.
- `context/brand-voice.md`: the voice the replies must match.
- The escalation path to the `compliance-privacy-reviewer` for anything that collects data,
  touches PDPL, or risks an accreditation or unannounced-plan claim.

If a needed variable is absent from both brief and context, stop and ask. Do not invent an
account, an offer, a price, a target, a Skill Path title, the content lineup, or an
instructor name in any reply or guidance.

## Steps

1. Restate the angle from the strategy-artifact so every reply pattern reinforces it and
   introduces no new message.
2. Set the tone: empowering never deficit-framed, plain and confident, Thmanyah benchmark,
   English-first with the English following the same spirit.
3. Build the reply patterns by message type: a question, a compliment, a complaint, a
   pricing or offer question, a "where do I start" question. For each, give the on-brand
   shape of the reply and what it must not claim.
4. Set the escalation rules. Any message that touches data collection, PDPL or privacy, an
   accreditation question, an instructor name, fundraising, a roadmap, or an unannounced plan
   escalates to the `compliance-privacy-reviewer` before any public reply. Sensitive or
   distressed messages escalate to a human, not an auto-reply.
5. Set what never goes in a reply: no promise of accreditation, no unannounced plan or launch
   date, no invented Skill Path title or instructor name, no offer or price not confirmed in
   the brief, no personal or sensitive data echoed back in a public thread.
6. Note that any public reply is a gated action. The guidance is approval-ready; replies go
   out only with sign-off, per the human gate. Hand the guidance to the hub for assembly.

## Output

Use `templates/community-engagement-guide.md`. The shape:
- tone (the empowering, on-brand voice for replies, tied to the angle),
- reply_patterns (by message type, with the on-brand shape and what not to claim),
- escalation_rules (what routes to the compliance-privacy-reviewer and what routes to a human),
- never_say (the hard-stop list for any reply).

Internal guidance that feeds the `organic-package`. It does not cross a boundary on its own.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and completeness.
- Any Arabic reply or template copy runs the gate stack: skill eval, `arabic-copy-qa` on
  Arabic, then `brand-qa-reviewer`, per `runtime/verification.md`.
- A compliance-touching reply attaches the `compliance-privacy-reviewer` verdict before it
  reaches the human gate. A public reply is a human-gate action.

## Hard rules

- The guidance never approves a public reply on its own. A reply is a gated action; nothing
  goes out without the human gate. Silence is not approval.
- Escalate anything sensitive or compliance-touching to the `compliance-privacy-reviewer`
  before replying, and route distressed messages to a human.
- Never promise accreditation. Never mention an unannounced plan, a roadmap, fundraising, or
  a launch date. Never name an instructor without confirmation.
- Never invent a Skill Path title, the content lineup, an offer, a price, or a target.
  Missing, stop and ask.
- Never echo personal or sensitive data back into a public thread or a tracking parameter.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.
