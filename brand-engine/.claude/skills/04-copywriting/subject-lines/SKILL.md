---
name: subject-lines
description: Write Arabic email subject lines, several options with one primary flagged, against a length and clarity bar. Use when an email needs subject lines, triggers on "subject lines," "email subject," "write the subject," "inbox preview." Produces the copy-package subject_lines[] for the gate stack.
---

# Subject lines (sub-skill of 04-copywriting)

Writes the subject lines for a customer-facing email: several distinct options, with one
flagged as the chosen primary. English-first, in the active brand voice. Pairs with `email-copy`
for the same message. Assembled into the `copy-package` by the 04 hub.

## Purpose

Earn the open without hype or shame. A subject line is the first promise the email makes, so
it must be clear, short enough to survive the inbox preview, and true to the body. Options
exist to test, the primary is the one to ship first.

## When to use

- An email body exists or is being written and needs subject lines.
- A subject test is planned and needs several real alternatives, not padding.

## Inputs

- `strategy-artifact`: segment, angle, offer_framing.
- The paired `email-copy` body, so the subject matches the promise the body keeps.
- The brief: offer, price, promotion, only when the subject states them.
- `context/brand-voice.md`: voice and the hard mechanical rules.

## Steps

1. Read the paired email body and name the one promise the subject must carry.
2. Write several options, three to five, each a real alternative angle on that promise.
3. Hold the length bar, mobile-justified: aim for roughly 30 to 40 characters, with the key
   word inside the first 30. About 80 percent of opens are on mobile, where iPhone shows
   roughly 33 to 35 characters, so a subject that runs long gets truncated.
4. Front-load the message. The angle lands in the first few words, before any truncation, not
   after a slow wind-up.
5. Hold the clarity bar: clear at a glance, no clickbait, no shame.
6. Keep each subject true to the body. A subject that overpromises fails the gate.
7. Flag exactly one option as the chosen primary. The rest are alternatives for testing.
8. Tag language ar or en. Arabic is primary.

## Output

`copy-package` subject_lines[], a set per email:

```
id        e.g. subj-nonpayer
email_ref the email variant id these subjects belong to
options[] each: text, language (ar | en), primary (true | false)
primary   the chosen option text, with exactly one option flagged primary true
preheader the inbox-preview line, set on purpose, roughly 40 to 90 characters, true to the body
```

The preheader is a deliberate deliverable, the inbox-preview text that shows after the
subject. Set it as earned extra space, not left to spill body text. Same mechanical rules
apply: no em dash, no tatweel, Western numerals only.

See `templates/subject-lines.md`.

## Hard rules

- Several options, exactly one flagged primary. No em dashes. No tatweel or kashida.
  Western numerals only.
- Hold the length and clarity bar. Short, clear, true to the body. No clickbait.
- Never invent an offer, price, Skill Path title, or instructor name. If a subject needs one
  and the brief is silent, stop and ask.
- Never imply certificate accreditation. Empowering, never deficit-framed.

## How it connects

Feeds the 04 hub's copy-package subject_lines[], paired by email_ref to an `email-copy`
variant. Every Arabic subject runs the gate stack: skill eval, then `arabic-copy-qa`, then
`brand-qa-reviewer`, per `runtime/verification.md`. Only qa-passed subjects advance.
