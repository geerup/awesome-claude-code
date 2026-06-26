# Paid campaign structure template

Everything staged paused. Each ad set maps to one creative variant and one copy variant by id.
Every budget, target, schedule, and geo traces to the brief. Missing means stop and ask. All
example values are illustrative only. Replace them. Do not invent budgets, targets, titles,
names, offers, or prices.

## Campaign block

```
campaign:
  name:        <naming-convention name>
  objective:   <from the brief>
  status:      PAUSED
  budget:      <from the brief, with currency>          # never assumed
  bid:         <bid strategy from the brief>             # never assumed
  target:      <CPA or ROAS from the brief>              # never assumed
  schedule:    <start and end date from the brief>       # never assumed
  geo:         <from the brief, GCC, primary Saudi>       # never assumed
```

## Ad set block (repeat per ad set)

```
ad_set:
  name:        <naming-convention name>
  status:      PAUSED
  targeting:   <audience definition from the brief or strategy>
  placements:  <Meta, Instagram, Google, YouTube as the brief allows>
  creative_ref: <creative-package concept or asset id>
  copy_ref:     <copy-package variant id>
  ads:
    - name: <ad name>  status: PAUSED  creative_ref: <id>  copy_ref: <id>
```

## Tracking block

```
pixel_or_capi: <events: page_view, gate_view, submit, confirm>
utms:          <source, medium, campaign, no personal or sensitive data>
naming:        <convention applied across campaign, ad sets, ads>
```

## Pre-launch checklist

```
- pixel firing:                    pass | fail
- live test event in events manager: pass | fail
- conversion event correct:        pass | fail
- conversion location correct:     pass | fail
- utms consistent:                 pass | fail
- naming applied:                  pass | fail
- budget cap set:                  pass | fail
- end date set:                    pass | fail
- audience geo correct:            pass | fail
- audience demographics correct:   pass | fail
- bid strategy confirmed:          pass | fail
- bid amount confirmed:            pass | fail
- creative spell-check:            pass | fail
- video captions present:          pass | fail | n/a
# search only:
- negative keywords present:       pass | fail | n/a
- match types set:                 pass | fail | n/a
- ad assets / extensions added:    pass | fail | n/a
```

A failing check blocks the package from the gate. Search-only items are n/a on non-search
channels. The bid strategy and amount, geo, and demographics each trace to the brief, never
assumed.

## Checklist before handoff

- Everything PAUSED. No spend, no go-live.
- Every budget, bid, target, schedule, geo traces to the brief. Missing means stop and ask.
- Each ad set mapped to one creative variant and one copy variant by id.
- No personal or sensitive data in UTMs. No accreditation implication.
- Pre-launch checklist fully passes before the gate.
- No em dash, no tatweel, Western numerals only.
