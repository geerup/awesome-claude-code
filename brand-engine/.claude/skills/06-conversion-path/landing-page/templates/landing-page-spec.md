# Landing page spec

Fills the `page` field of the `conversion-package`. Copy comes from the QA-passed
copy-package by variant id. No free copy here. RTL-correct, on brand, one clear CTA.

## Envelope reference

```
campaign_id   <from the active brief filename>
produced_by   conversion-engineer
stream        6 conversion path
status        draft | qa-passed | gated-pending | approved
qa            { skill_eval: , arabic_qa: , brand_qa: }
brief_refs    <offer, price, promotion only if shown on page>
```

## Layout

| Region | Bound copy variant id | Notes |
|---|---|---|
| Hero headline | copy-package/<variant-id> | one line, Arabic primary |
| Hero subhead | copy-package/<variant-id> | optional |
| Body block 1 | copy-package/<variant-id> | the angle, plain |
| Primary CTA | copy-package/<variant-id> | one CTA only |

Sections beyond these are added only when the offer needs them. Cut anything that does not
move the click.

## Visual constants

- Background: #141414
- Card surfaces: #1A1A1A
- Primary accent, emerald: #009975
- Generous space. The accent is a highlight, not a flood.

## RTL and language

- Document direction: rtl. Arabic copy is primary.
- Western numerals only (0 to 9). No Eastern Arabic numerals.
- Mixed Arabic, English, or numerals must not break direction. Test the rendered page.
- No em dashes, no tatweel.

## Performance

- Fast first render. Minimal blocking assets.
- Primary CTA visible without a scroll on mobile.

## Open items

- Gate platform not confirmed: the page is design-ready, the gate wiring is blocked until
  the email or WhatsApp platform is named and approved.

## Guardrails check before handing up

- One clear CTA, not two competing primary actions.
- No invented Skill Path title, instructor name, offer, or price.
- No implication that certificates are accredited.
