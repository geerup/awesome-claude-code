# Campaign Brief: [campaign name]

The only per-campaign input. Every variable the engine uses lives here. Facts about Maharat
live in `context/`. This file holds what changes campaign to campaign. Any field marked
ASSUMPTION is a placeholder the engine must not act on until Ahmed replaces it with a real
value. An agent that hits an ASSUMPTION on a field it needs stops at the human gate.

Naming: save as `briefs/YYYY-MM-short-name.md`. The filename is the `campaign_id` that every
artifact carries.

No em dashes, Western numerals, Arabic-first for any customer-facing text drafted here.

---

## 1. Identity

- campaign_id: [YYYY-MM-short-name, matches filename]
- name: [short human name]
- owner: Ahmed
- created: [YYYY-MM-DD]

## 2. Background and context

- why_now: [why this campaign exists now, the trigger or moment. If not stated, mark OPEN ITEM;
  do not invent a rationale]
- business_problem: [the problem this campaign is meant to solve, in plain words]
- prior_results: [what came before and how it did, link to the prior report-artifact if any,
  or "none" for a first run. Do not invent past numbers]

## 3. Entry point and objective

- entry_point: [paid acquisition | owned audience]
- objective: [the one outcome this campaign exists to produce]
- success_metric: [the single number stream 8 measures against. Must carry a target NUMBER
  and a date by which it is measured, for example "X qualified signups by YYYY-MM-DD". If the
  number or date is not yet known, mark it ASSUMPTION; do not invent one. A vague or
  unmeasurable metric ("more signups", "grow awareness") is not a value: flag it as an open
  item for Ahmed, never carry it silently and never fill it in]
- key_message: [provisional, single-minded proposition for this campaign, a brief-level anchor
  that strategy-lead refines into the stream 2 angle, not a hard input. If the brief has no
  steer yet, mark it OPEN ITEM for strategy-lead to originate; do not invent a claim or an
  offer here]

## 4. Audience

- audience: [who, in plain words]
- segments: [list, or "to be defined by strategy-lead from the owned data"]
- suppression: [who is excluded and why, for example already paying, unsubscribed]
- audience_size: [resolved at send time from live data; planning estimate here]

## 5. Offer (never invented, supplied here)

- product: [Masterclass | Skill Path | subscription | other]
- plan: [1 | 3 | 12 months, if a subscription]
- price: [ASSUMPTION until Ahmed confirms]
- promotion: [discount, trial, bundle, or none. ASSUMPTION until confirmed]
- offer_framing_notes: [any positioning the brief wants, optional]

## 6. Channels and gate

- channels: [email | whatsapp | meta | google | organic | landing page]
- signup_gate: [email | whatsapp | none]
- gate_platform: [name, or OPEN ITEM if not confirmed]

## 7. Budget and schedule

- budget: [amount and currency, or n/a for owned audience. ASSUMPTION until confirmed]
- target_cpa_or_roas: [if paid. ASSUMPTION until confirmed]
- start_date: [YYYY-MM-DD]
- end_date: [YYYY-MM-DD]
- send_window: [for lifecycle, the days or cadence]
- reporting_cadence: [when and how results are reviewed against success_metric after launch,
  for example "weekly readout to Ahmed", so streams 8 and 9 inherit the review rhythm. If not
  stated, mark OPEN ITEM; do not invent a cadence]

## 8. Creative direction (optional, brief-level)

- creative_direction: [any art direction the brief wants, or "creative-director to propose"]
- tone_descriptors: [a short campaign-specific adjective set that sits on top of the global
  brand voice, for example "more urgent than usual" or "celebratory". The global voice in
  CLAUDE.md and context/brand-voice.md still governs; this only names the campaign nuance.
  Optional, leave blank if the campaign carries the default voice]
- assets_available: [existing assets to reuse, or none]

## 9. Mandatories and constraints

- mandatories: [positive must-includes for this campaign. List the brand and legal items that
  every customer-facing asset must carry, for example logos, legal disclaimers, brand colors.
  If an item is required but the specifics are not yet supplied, mark it OPEN ITEM; do not
  invent a disclaimer, a logo lockup, or a color value]
- constraints: [negative must-nots and anything campaign-specific the engine must respect]
- open_items: [anything unresolved that downstream must account for]

## 10. Approvals

- approval_owner: Ahmed
- approval_status: [pending until each gated action is signed off, per action]
