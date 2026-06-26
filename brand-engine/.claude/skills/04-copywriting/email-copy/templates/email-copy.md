# Email copy template

One block per email variant. English-first. Exactly one clear CTA per email. Pair with a
subject_lines set (see the subject-lines sub-skill). All example copy is illustrative only.
Replace it. Do not invent offers, prices, Skill Path titles, or instructor names.

## Email block

```
id:        email-<segment>-<n>        # e.g. email-nonpayer-v1
segment:   <strategy-artifact segment name>
language:  ar | en
headline:  <in-body lead line>
body:      <two to four short lines>
cta:       <exactly one action>                 # one CTA only, no competing button
subject_ref: <which subject_lines set pairs with this email>
subject_len: <character count of the primary subject, 20 to 60, mobile 30 to 40>
preheader: <deliberate inbox-preview line, about 40 to 90 characters, adds a promise>
sequence:  <the pattern this email belongs to: welcome | onboarding | event | nonpayer | winback>
objective: <the sequence objective the CTA serves: relationship | activation | attendance | conversion | reactivation | winback>
send_trigger: <time-based <delay after entry event> | behavior-triggered <on opened | clicked | started | completed | not-X>>
fills:     <asset_brief slot id, if this email overlays a creative slot>
```

The `sequence` and `objective` come from the pattern in
`skills/07-lifecycle-messaging/templates/sequence-standards.md`. The single CTA must serve
that objective for that audience. The `send_trigger` states whether this email is time-based
(a delay after the entry event) or behavior-triggered (a response to what the contact did or
did not do), layered on the time-based foundation.

## Illustrative example (Arabic, replace before use)

```
id:        email-example-v1
segment:   example-segment
language:  ar
headline:  مهارتك القادمة على بُعد خطوة
body:      عدنا لك بمسار قصير يناسب وقتك.
           ابدأ بدرس واحد اليوم، وكمل على راحتك.
           كل خطوة تبني مهارة تبقى معك.
cta:       تابع رحلتك
subject_ref: subj-example
fills:     none
```

## Checklist before handoff

- One clear CTA, one action. No competing button.
- Subject length 20 to 60 characters, mobile band roughly 30 to 40, key word in the first 30.
- A deliberate preheader, about 40 to 90 characters, that adds a promise, not a repeat of the subject.
- Send-trigger stated: time-based (delay after entry event) or behavior-triggered (on what the contact did or did not do).
- The CTA serves the sequence objective for its audience (per sequence-standards.md).
- Body short, two to four short lines.
- No em dash, no tatweel, Western numerals only.
- Empowering, never deficit-framed. No accreditation implication.
- Every offer or price traces to the brief. Nothing invented.
- A subject_lines set is paired with this email.
