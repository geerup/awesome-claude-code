# Email sequence structure template

Assembled, not sending. Blocked on the email and WhatsApp platform OPEN ITEM until the platform
is confirmed and approved. Each message binds to a copy-package variant id and a subject line.
All example values are illustrative only. Replace them. Do not invent audiences, schedules,
titles, names, offers, or prices.

The structure assembles whichever pattern the lifecycle-package used, from
`skills/07-lifecycle-messaging/templates/sequence-standards.md` (welcome, onboarding, event,
nonpayer, winback). Carry each message's trigger, delay and cadence, audience, and suppression
through unchanged. Preserve the pattern's triggers and cadence; do not flatten them to fit the
platform.

## Pattern block

```
pattern:         welcome | onboarding | event | nonpayer | winback
objective:       <the pattern objective, from sequence-standards.md>
cadence:         <the pattern cadence, e.g. every 2 to 3 days in a welcome window, never daily>
```

## Platform block

```
platform:        <confirmed and approved platform name>    # blocked until confirmed
platform_status: confirmed | OPEN ITEM (build does not proceed until confirmed)
```

## Audience and suppression block

```
audience:        <resolved from lifecycle-package and brief>
audience_size:   <resolved count, e.g. ~18000 non-payers>
suppression:     <already paying, unsubscribed, excluded by the flow>
```

## Message block (repeat per message, in order)

```
message:
  order:        <1, 2, 3 ...>
  trigger_type: time-based | behavior-triggered
  trigger:      <entry event, prior-message completion, or the behavior: opened | clicked |
                started | completed | attended | no-show | lapsed | not-X>
  delay:        <time after trigger, e.g. 2 days; for the first welcome touch, within ~5 minutes>
  send_window:  <local send window, e.g. 8 AM to 10 AM, or the pattern override (event reminder)>
  audience:     <the audience or branch this message serves>
  copy_ref:     <copy-package variant id>
  subject_ref:  <paired subject_lines set id>
  status:       ASSEMBLED, NOT SENDING
  links:        <no personal or sensitive data in any link>
```

## Pre-handoff checklist (operational)

```
- platform confirmed:        pass | OPEN ITEM
- pattern triggers preserved: pass | fail
- cadence preserved:          pass | fail
- bindings resolved:          pass | fail
- suppression set:            pass | fail
- links clean (no PII):       pass | fail
```

## Checklist before handoff

- Assembled, not sending. No live send, no schedule on its own.
- Platform confirmed and approved, or stop on the OPEN ITEM.
- Pattern named, and every message's trigger (time-based or behavior-triggered) and cadence
  preserved from the sequence-standards pattern. No flattening to fit the platform.
- Each message bound to a copy variant id and a subject line. No invented copy.
- Suppression applied. No personal or sensitive data in links. No accreditation implication.
- No em dash, no tatweel, Western numerals only.
