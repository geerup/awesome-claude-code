---
name: segmentation-logic
description: Define the trigger and branch logic for lifecycle messaging: who gets which message when, the engagement branches, and suppression. Use before sequencing any flow to fix the audience it runs on. Triggers on "who gets which email," "the engagement branches," "segmentation logic," "suppression rules," "the send conditions." Sub-skill of 07-lifecycle-messaging, owned by lifecycle-architect.
---

# Segmentation logic (stream 7 sub-skill)

Defines the audience logic behind a lifecycle flow: the entry trigger, the segments, the
engagement branches, the inter-message timing conditions, and the suppression set. It does
not order the messages or write copy. It fixes who is eligible, who branches where, and who
is excluded, so the flow sub-skill can sequence against a known audience.

Owner: lifecycle-architect. Mode: reasoning. Follows `sops/07-lifecycle-nonpayer-email.md`.

## When to use

- Before `nonpayer-email-flow` or `onboarding-sequence`, to resolve the audience and rules.
- The brief or strategy-artifact defines segments that need branch and suppression logic.

## Inputs

- The `strategy-artifact`: the segments, their definitions and sizes, the angle.
- The active `briefs/` file: send window, cadence, and the suppression rules.
- The owned-audience data source (for resolving segment and audience size at send time).

If a segment size or a suppression source is not in the data or the brief, flag it as needed
at send time. Do not invent a segment size.

## Steps

1. Resolve segments from the strategy-artifact. Typical non-payer cuts: never-engaged vs
   lapsed-engaged, prior single-class interest vs none, recency of last open. Use the data;
   do not invent sizes.
2. Define the entry trigger: the condition that puts a contact into the flow.
3. Define the engagement branches: openers and clickers nudge toward the offer; non-openers
   get a subject-line retry, not a louder pitch. State each branch condition plainly.
4. Define inter-message timing: delays between messages, kept inside the brief send window.
5. Set suppression: exclude all paying contacts (about 5,000), anyone unsubscribed, and
   hard-bounced addresses. Confirm the suppression source at build. Suppression is not
   optional and is stated explicitly.
6. Set engagement-decay suppression and the sunset rule. A contact who has not opened or
   clicked in roughly 90 to 180 days, or who has gone through 3 to 4 flow attempts without
   re-engaging, runs a short sunset flow (1 to 3 emails, no more than 3) and is then
   suppressed. Sunsetting protects sender reputation and deliverability, and it keeps the
   list to consenting, engaged contacts, which is also sound PDPL and consent hygiene. The
   exact window resolves against the brief and the data; do not invent it.
7. Hand the logic to the flow sub-skill, which orders the messages against it.

## Output

A segmentation-logic block that the flow consumes and that informs the lifecycle-package:

```
entry_trigger    the condition that enters a contact into the flow
segments         each: name, definition, size (or resolve-at-send), source
branches         engagement branch conditions (opened, clicked, not-opened)
timing           inter-message delays, inside the send window
suppression      who is excluded and why (paying, unsubscribed, hard-bounced), source
sunset_rule      engagement-decay condition (no open or click in roughly 90 to 180 days, or
                 3 to 4 attempts), the 1 to 3 email sunset flow, then suppress
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and the suppression rule.
- The flow's copy runs the gate stack downstream: skill eval, `arabic-copy-qa`,
  `brand-qa-reviewer`, per `runtime/verification.md`.

## Hard rules

- Suppression is not optional. No paying contact, unsubscribe, or hard bounce is eligible.
- The sunset rule is not optional. Engagement-decayed contacts (no open or click in roughly
  90 to 180 days, or 3 to 4 attempts) run a 1 to 3 email sunset, then are suppressed. This
  protects deliverability and strengthens consent and PDPL hygiene.
- Do not invent segment sizes or the sunset window. Resolve from live data and the brief.
- Never put personal or sensitive data in a tracking URL parameter.
- No em dashes, no tatweel, Western numerals. Empowering, never deficit-framed.
