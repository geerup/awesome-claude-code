# Brief: [asset or campaign name]

The only per-run input. Every variable the engine uses lives here. Stable facts about the brand
live in `context/` (`01-brand-brief.md`, `brand-voice.md`, the active profile). This file holds
what changes run to run. Any field marked ASSUMPTION is a placeholder the engine must not act on
until you replace it with a real value. An agent that hits an ASSUMPTION on a field it needs
stops at the human gate.

Naming: save as `briefs/YYYY-MM-short-name.md`. The filename is the `run_id` every artifact carries.
English-first; no em dashes. Set `primary_language: ar` only if this run needs Arabic.

---

## 1. Identity
- run_id: [YYYY-MM-short-name, matches filename]
- name: [short human name]
- owner: Ahmed
- created: [YYYY-MM-DD]
- primary_language: en   (set to `ar` or `en+ar` only if this run needs Arabic)

## 2. Background and context
- why_now: [the trigger or moment. If not stated, mark OPEN ITEM; do not invent]
- goal_emphasis: [career | services | creator | founder] (which of the four this run serves)
- prior_results: [what came before and how it did, or "none". Do not invent past numbers]

## 3. Objective
- objective: [the one outcome this run exists to produce, e.g. "a portfolio site", "10 LinkedIn
  posts that establish my point of view", "a services page that books calls"]
- success_metric: [the single measurable signal, with a number and a date if applicable. If not
  yet known, mark ASSUMPTION; do not invent. A vague metric is an open item, never carried silently]
- key_message: [provisional single-minded message, or OPEN ITEM for strategy-lead to originate]

## 4. Audience
- audience: [who, in plain words: an employer, a client type, a community]
- segments: [list, or "to be defined by strategy-lead"]
- where_they_are: [the platforms or places they will see this]

## 5. The offer or ask (never invented, supplied here)
- subject: [me | a service | a venture | a research target] (from context/subjects/)
- offer: [what is being offered or asked, if any: a service, a download, a follow, a meeting]
- price: [if a paid offer. ASSUMPTION until you confirm]
- proof: [the verified claims this run rests on, by claims-table row in the subject's fact file]

## 6. Channels and surface
- channels: [linkedin | x | substack | newsletter | website | portfolio | email | other]
- surface: [the concrete asset: a page, a post set, an email, a CV, a deck, a visual set]
- publish_path: [draft-only (default) | gmail | substack | wordpress | github-pages]

## 7. Schedule
- start_date: [YYYY-MM-DD]
- cadence: [for content: the posting rhythm, or n/a]
- deadline: [if any]

## 8. Creative direction (optional)
- creative_direction: [any art direction, or "creative-director to propose"]
- tone_descriptors: [a short run-specific adjective set on top of the global brand voice]
- assets_available: [existing assets to reuse, or "ingest from <source>", or none]

## 9. Mandatories and constraints
- mandatories: [must-includes: a link, a CTA, a brand element. OPEN ITEM if specifics unknown]
- constraints: [must-nots: anything off-limits, any employer/client that needs consent or NDA care]
- open_items: [anything unresolved that downstream must account for]

## 10. Approvals
- approval_owner: Ahmed
- approval_status: [pending until each gated action is signed off, per action]
