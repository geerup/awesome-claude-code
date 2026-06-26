# Web design spec

Fills the `design_spec` field of the `web-design-package`. Build-ready and responsive. Copy
comes from the QA-passed copy-package by variant id. No free copy here. RTL-correct at every
breakpoint, on brand, one primary action per view.

## Envelope reference

```
campaign_id   <from the active brief filename>
produced_by   web-designer
stream        6 conversion path (web design)
status        draft | qa-passed | gated-pending | approved
qa            { skill_eval: , brand_qa: , web_design_qa: }
brief_refs    <gate type, dimensions, direction>
```

## Components

| Component | Role | Notes |
|---|---|---|
| Hero | the offer and the primary action | one primary action |
| Section block | the angle | from the wireframe |
| Signup gate | capture | email or WhatsApp, platform OPEN ITEM |
| Primary action | one CTA | not two competing actions |

## Responsive system

- Grid: <columns>, gutters, margins.
- Breakpoints (mobile first): sm <width>, md <width>, lg <width>.
- Type scale: <scale>.

## Design tokens

- Color: background #141414, card surfaces #1A1A1A, primary accent emerald #009975 (highlight, not flood).
- Spacing: <scale>. Radius: <scale>.

## Interaction states

- default, hover, focus, active, disabled, loading, error for every interactive element.

## RTL and language (per breakpoint)

- Document direction: rtl at sm, md, and lg. Arabic copy is primary.
- Western numerals only (0 to 9). No Eastern Arabic numerals.
- Mixed Arabic, English, or numerals must not break direction at any width. Test each breakpoint.
- No em dashes, no tatweel.

## Accessibility

- Contrast meets the bar. Focus order logical. Semantic structure (headings, landmarks).
- Touch targets sized. Alt text slots present (filled in stream 4, not baked into imagery).

## Performance budget

- Fast first render. Minimal blocking assets. Image weight noted.
- Primary action visible without a scroll on mobile.

## Copy binding (no free text)

| Region | Bound copy variant id |
|---|---|
| Hero headline | copy-package/<variant-id> |
| Hero subhead | copy-package/<variant-id> |
| Primary action | copy-package/<variant-id> |

## Open items

- Build tool not approved: the design is ready, the build and wiring are blocked at the human gate.
- Copy region unbound: proceed with the design, mark the region for stream 4.

## Guardrails check before handing up

- One primary action per view. RTL correct at every breakpoint.
- Copy bound by id, never invented. No Arabic baked into imagery.
- No personal or sensitive data in URL parameters or tracking.
- No invented Skill Path title, instructor name, offer, or price. No accreditation implication.
