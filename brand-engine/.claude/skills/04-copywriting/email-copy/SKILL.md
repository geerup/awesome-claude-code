---
name: email-copy
description: Write English-first email body copy for lifecycle and campaign messages, one clear CTA per email. Use when drafting an email body, triggers on "write the email," "email body," "lifecycle message," "nonpayer email." Produces copy-package variants[] for the gate stack and the lifecycle flow.
---

# Email copy (sub-skill of 04-copywriting)

Writes the body of a customer-facing email: an opening that earns the read, a short middle
that lands the angle, and exactly one clear CTA. English-first, in the active brand voice. Pairs
with `subject-lines` for the same message. Assembled into the `copy-package` by the 04 hub.

## Purpose

Give each lifecycle message a body that respects a busy reader's time and moves them to one
action. Built to drop into the lifecycle flow (stream 7) as a copy variant the flow
references.

## When to use

- A lifecycle or campaign email needs its body written (for example, the non-payer flow).
- An email variant per segment is needed to test angle or framing.

## Inputs

- `strategy-artifact`: segment, angle, offer_framing.
- The brief: offer, price, promotion, only when the email shows them.
- `context/brand-voice.md`: voice and the hard mechanical rules.
- The lifecycle context, if known: where this email sits in the flow.

## Steps

1. Anchor the email to one job: the single thing this message must move the reader to do.
2. Open with a line that respects the reader and earns the next line. No hype, no shame.
3. Write a short body, two to four short lines. Concrete, active, empowering.
4. Write exactly one clear CTA. One action, one link intent. Never two competing buttons.
5. Tag language ar or en. Arabic is primary.
6. Produce one variant per segment, or two when the angle is being tested.
7. Note which subject_lines belong to this email and which asset_brief slot it fills.

## Output

`copy-package` variants[], each:

```
id        e.g. email-nonpayer-v1
segment   the strategy-artifact segment name
headline  the in-body lead line (the subject line is carried in subject_lines[])
body      two to four short lines
cta       exactly one
language  ar | en
```

See `templates/email-copy.md`.

## Email standards (anatomy, timing, triggers)

The standards every single email is written to. They are synthesized from the canonical
onboarding, welcome, and webinar sequence sources. Hold them as the bar; the English-first
Thmanyah voice stays primary over any of them.

Anatomy of one email:
- Exactly one clear CTA. One action, one link intent. A second link is at most a quiet
  secondary, never a competing button.
- Subject line 20 to 60 characters, with a mobile band of roughly 30 to 40, and the key word
  front-loaded inside the first 30 (the angle lands before truncation). The subject set is
  authored in `subject-lines`; write the body so it keeps the subject's promise.
- A deliberate preheader of about 40 to 90 characters that adds a promise, not a repeat of the
  subject. Set on purpose as earned inbox-preview space, never left to spill body text.
- Plain, confident, empowering body. Short and scannable, two to four short lines.
- Personalization only where it is real and consented. Never fake a personal field, never put
  personal or sensitive data in a URL parameter or tracking.

Send timing and triggers:
- The welcome or first email fires within about 5 minutes of the entry event, the moment the
  contact is warmest.
- Subsequent emails favor a morning local send, about 8 AM to 10 AM in the contact's market.
- Prefer BEHAVIOR-TRIGGERED sends (respond to what the contact did or did not do: opened,
  clicked, started, completed, lapsed) layered on a TIME-BASED foundation, so the sequence
  still moves when no behavior fires.
- Cadence is every 2 to 3 days in a welcome window, never daily.

Objective fit:
- The email's single CTA and its angle must serve the objective of the sequence it belongs to,
  for that sequence's audience (relationship, activation, attendance, conversion, reactivation,
  or win back). An onboarding email that sells instead of activating is off-objective even when
  it is well written. Name the pattern and objective before writing, and check the CTA against
  it. The success signal is the objective metric (for onboarding, activation rate, not opens).
- Read the pattern this email belongs to in
  `skills/07-lifecycle-messaging/templates/sequence-standards.md` (welcome, onboarding, event,
  nonpayer, winback) and write the CTA to that pattern's objective and audience.

## Optional structures to reach for

These are tools to test a draft against, not mandatory structure. The English-first Thmanyah
voice stays primary. Reach for one when it sharpens the email, drop it when it fights the voice.

- The 4 Us, a checklist for the lead line and the in-body hook. Is it Useful (Useful first),
  Urgent, Unique, and Ultra-specific? Test the line against it, do not force all four in.
- PAS (Problem, Agitate, Solution), an optional structure for pain-aware, bottom-funnel
  emails such as a non-payer nudge. Name the problem without shaming the reader, the
  empowering rule still holds.
- AIDA (Attention, Interest, Desire, Action), an optional structure for cold, top-funnel
  emails that move a stranger from notice to one action.
- The 4 Cs (Clear, Concise, Compelling, Credible), a final pass on the email before it advances.

## Multi-instructor and catalog emails

When the email features two or more instructors, or the catalog as a whole (a Skill Path, a themed
roundup, an occasion sale, a "picked for you" recommendation), write it as a multi-instructor email
per `context/profiles/maharat/multi-instructor-angles.md`. The shape:

- A hero umbrella line: one reader outcome that unifies the lineup, never "meet our instructors."
- Per-instructor LessonCardGrid copy, each card three short copy slots: an outcome-first headline
  (what the reader will be able to do), a "with [Name], [one page-cleared credential]" line, and a
  quiet secondary link label (for example "start learning").
- Optional IssueIndex labels (a numbered "in this issue") and a MemberWin (one real, consented
  testimonial plus a short bridge line into the CTA).
- One primary CTA still holds. The single pill is the join or the offer; every per-card link is a
  quiet secondary text link, never a second pill. So a one-clear-CTA email and a multi-card digest
  are not in conflict: the digest has one primary and several quiet secondaries.

Each credential traces to a page-cleared fact and each named instructor is catalog-status-confirmed
(`context/profiles/maharat/instructor-packs`), or that card is dropped. No invented Skill Path title, lineup,
occasion, catalog count, discount, or accreditation claim. These map to the build modules in
`context/profiles/maharat/email-design-system.md` and render via `scripts/email_render.py`.

## Hard rules

- One clear CTA per email. No em dashes. No tatweel or kashida. Western numerals only.
- Never invent an offer, price, Skill Path title, or instructor name. If the email needs one
  and the brief is silent, stop and ask.
- Never imply certificate accreditation. Empowering, never deficit-framed.

## How it connects

Feeds the 04 hub's copy-package variants[]; subject lines come from `subject-lines`. Every
email runs the gate stack matched to its language: skill eval, then `arabic-copy-qa` for an
Arabic variant or `english-copy-qa` for an English variant, then `brand-qa-reviewer`, per
`runtime/verification.md`. A bilingual message runs each variant through its own language gate.
Only qa-passed copy advances to the lifecycle flow (stream 7) or build (stream 5).
