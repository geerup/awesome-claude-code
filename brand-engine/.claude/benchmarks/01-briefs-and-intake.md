# Benchmark: briefs and intake

Internal benchmark, not customer-facing. Compares our campaign brief template and our
stream 1 intake skills against authoritative real-world brief, creative-brief, and project
intake templates. The goal is to find concrete gaps and concrete strengths, then propose
specific edits. No em dashes, Western numerals only, no tatweel.

Scope of the comparison on our side:
- `briefs/_TEMPLATE-campaign-brief.md` (the per-campaign input template)
- `briefs/2026-06-nonpayer-email.md` (the first real brief, used as a worked example)
- `skills/01-brief-intake/SKILL.md` (the intake hub)
- `skills/01-brief-intake/brief-validate/SKILL.md` and its `templates/brief-validation-report.md`
- `skills/01-brief-intake/kickoff-scope/SKILL.md` and its `templates/kickoff-scope.md`
- `runtime/handoff-contract.md` (the common envelope and the strategy-artifact)

Date: 2026-06-03.

---

## Sources reviewed (web)

- [Asana, Creative Briefs: What To Include (with Template) 2026](https://asana.com/resources/how-write-creative-brief-examples-template). Seven-part creative brief: objective, audience, messaging, deliverables, timeline, budget, success metrics.
- [HubSpot, How to Write a Creative Brief in 11 Simple Steps](https://blog.hubspot.com/marketing/creative-brief). Step-by-step brief build: background, objectives, audience, message, tone, deliverables, distribution, stakeholders, timeline.
- [Smart Insights, How to define SMART marketing objectives (with RACE KPIs)](https://www.smartinsights.com/goal-setting-evaluation/goals-kpis/define-smart-marketing-objectives/). Objectives must be Specific, Measurable, Achievable, Relevant, Time-bound, each tied to a KPI and a target.
- [Digital Marketing Institute, What are SMART Objectives in Digital Marketing?](https://digitalmarketinginstitute.com/blog/what-are-smart-objectives-in-digital-marketing). SMART framework applied to digital campaign goals.
- [Meltwater, How to Create a Marketing Campaign Brief Template](https://www.meltwater.com/en/blog/marketing-campaign-brief-template). Campaign brief fields: name, objective, audience, key message, channels, assets, timeline, budget and allocation, stakeholders and owners, approval flow, KPIs, reporting cadence.
- [monday.com, Brand brief templates (2026)](https://monday.com/blog/marketing/brand-brief-template/). Five essential elements: clear objectives, audience with segments, budget, timeline, metrics. Keep the brief to one or two pages.
- [SEOptimer, Project Intake Form Best Practice for Agencies](https://www.seoptimer.com/blog/project-intake-form/). Intake captures the basics before kickoff so the first meeting is strategy, not data collection: contact and stakeholders, goals and deliverables, budget and timeline, industry-specific fields such as brand guidelines and assets.
- [Paperform, Agency Creative Project Brief Intake Form Template](https://paperform.co/templates/agency-creative-project-brief-intake-form/). Intake captures stakeholder details, approval workflows, communication preferences, file sharing, and milestone definitions.

---

## Best-in-class elements

The fields and sections that the strongest brief, creative-brief, and intake templates above
converge on:

1. Identity and ownership. Campaign name, owner or lead, key dates, single source of truth.
2. Background and context. Why this campaign exists now, the business problem, what came before.
3. Objective as a SMART goal. Specific, Measurable, Achievable, Relevant, Time-bound. Not "increase sales" but "increase X by Y percent by date Z" (Smart Insights, Digital Marketing Institute).
4. Success metrics and KPIs with explicit targets, plus a primary metric distinguished from secondary ones (Meltwater, Smart Insights).
5. Target audience with segments, broken by demographics, behavior, psychographics, and funnel stage (monday.com, HubSpot).
6. Single-minded key message and supporting points, kept consistent across every asset (Meltwater, HubSpot).
7. Tone and voice descriptors, a few adjectives that fix the attitude (Asana, HubSpot).
8. Channels and tactics with a justification for each channel, so trade-offs are explicit (Meltwater).
9. Deliverables and required assets, with dimensions, versions, and format specs (Asana, creative-brief consensus).
10. Timeline with milestones: approval dates, production start, launch, review (Asana, Meltwater).
11. Budget, including channel-level allocation, not just a single number (Meltwater, monday.com).
12. Stakeholders, roles, and an explicit approval flow or sign-off chain (Meltwater, Paperform, HubSpot kickoff).
13. Reporting cadence: when and how performance is reviewed after launch (Meltwater).
14. Mandatories and constraints: legal, brand, regulatory must-haves and must-not-says.
15. Format discipline. One to two pages, because long briefs stop being read (monday.com).
16. Intake-specific: communication preferences, file-sharing or asset-handoff method, and a kickoff agenda that turns the brief into a shared starting point (Paperform, SEOptimer, HubSpot kickoff playbook).

---

## Our coverage

Our brief template and intake skills already cover most of the best-in-class list, and in a
few places more rigorously than the public templates.

- Identity and ownership. `_TEMPLATE-campaign-brief.md` section 1: campaign_id (doubles as the artifact key), name, owner, created date. Strong.
- Objective. Section 2 carries entry_point, objective, and success_metric with a target. Present, though the objective is prose, not a forced SMART structure (see gaps).
- Success metric. Section 2 success_metric names "the single number stream 8 measures against, with target," and the strategy-artifact in `handoff-contract.md` carries success_metric forward to stream 8. A clean primary-metric discipline.
- Audience and segments. Section 3: audience, segments, suppression, audience_size (with a planning-estimate vs resolve-at-send-time distinction). Suppression is a field most public templates omit. Strong.
- Offer. Section 4: product, plan, price, promotion, framing notes, all guarded as never-invented. This is a Maharat-specific addition beyond generic templates.
- Channels and gate. Section 5: channels, signup_gate, gate_platform.
- Budget and schedule. Section 6: budget, target_cpa_or_roas, start_date, end_date, send_window.
- Creative direction. Section 7: creative_direction, assets_available.
- Constraints and notes. Section 8: constraints, open_items.
- Approvals. Section 9: approval_owner, approval_status, per-action sign-off.
- Intake process. `01-brief-intake/SKILL.md` routes validate then scope. `brief-validate` walks the template field by field and classifies each as PRESENT, ASSUMPTION, OPEN ITEM, or MISSING, recorded in `templates/brief-validation-report.md`. `kickoff-scope` chooses entry point, active streams, funnel path, and out-of-scope, recorded in `templates/kickoff-scope.md`. This is a genuine intake gate, stronger than a static form.
- Handoff. `runtime/handoff-contract.md` defines the common envelope (campaign_id, produced_by, stream, status, qa, open_items, brief_refs) and the strategy-artifact (segments, angle, offer_framing, channel_plan, success_metric).

---

## Gaps and missing elements

Prioritized. Each is a concrete field or section, not a vague theme.

High:

1. No SMART structure on the objective. Section 2 objective is free prose. Best practice (Smart Insights, Digital Marketing Institute) forces Specific, Measurable, Achievable, Relevant, Time-bound. The nonpayer brief shows the cost: the objective is clear but the success_metric is an ASSUMPTION with no number, so there is no measurable target at intake. A SMART check would surface this immediately.
2. No background or context field. Every strong brief (HubSpot, Meltwater) opens with why-now: the business problem and what came before. Our template jumps straight to objective. Without it, strategy-lead in stream 2 has no rationale to anchor the angle, and the next campaign's learnings (report-artifact) have nowhere to land at intake.
3. No explicit key message or single-minded proposition field at brief level. Section 7 covers creative direction, but the core message and supporting points are deferred entirely to the stream 2 angle. Public templates put a provisional key message in the brief so the objective and the message are checked against each other early.
4. No stakeholders or roles field beyond owner and approver. Meltwater, Paperform, and the HubSpot kickoff playbook all capture who reviews, who is consulted, who signs off, and communication preferences. Our template has owner (Ahmed) and approval_owner (Ahmed) only. For a single-approver engine this is partly by design, but reviewers and consulted parties are still uncaptured.

Medium:

5. No reporting cadence field. Meltwater lists it as core. We have success_metric and stream 8/9 own measurement, but the brief never states when results are reviewed. Adding a reporting_cadence field in section 6 or section 9 closes the loop the public templates close.
6. No tone-and-voice descriptors at brief level. Asana and HubSpot want a few adjectives per campaign. Our brand voice is global (CLAUDE.md, brand-voice.md), so the campaign-specific nuance is the gap, for example "more urgent than usual" or "celebratory." offer_framing_notes partly absorbs this but does not name tone.
7. No deliverables-and-specs list at brief level. The creative-package and copy-package carry asset specs downstream, but the brief itself does not enumerate expected deliverables and counts. Asana and the creative-brief consensus put a deliverables list in the brief so scope is visible before production. kickoff-scope decides which streams run but not the asset count.
8. No mandatories field distinct from constraints. Section 8 constraints mixes hard legal or brand must-haves with campaign notes. Best practice separates positive mandatories (must include X) from negative constraints (must not say Y). Our guardrails live in CLAUDE.md but are not echoed as a brief-level mandatories checkbox.

Low:

9. No one-to-two-page length note in the template. monday.com stresses brevity. Our template is field-based and naturally short, so this is minor, but a stated length ceiling protects it.
10. No file-sharing or asset-handoff method field. assets_available names what exists but not where it lives or how it is handed over. Intake templates (Paperform) capture this; for us it is low because handoff is internal artifacts.
11. No kickoff agenda artifact. kickoff-scope produces a run plan, which is close, but it is a scope decision, not the shared kickoff agenda the HubSpot playbook describes. Low, because our run is agentic, not a client meeting.

---

## Where ours is stronger

Our system beats the public templates on the things that matter most for an agentic,
campaign-agnostic engine:

- Explicit ASSUMPTION and OPEN ITEM flagging. No public template has a first-class concept for "this is a placeholder, do not act on it." Ours does, at the field level, and it rides forward into the validation report, the kickoff scope, and the handoff envelope's open_items. The nonpayer brief shows it working: price, promotion, schedule, and success target are all flagged, not silently filled.
- No-invented-values discipline. brief-validate's core job is stop-and-ask on any MISSING needed variable, never invent. Public templates assume a human fills the blanks; ours enforces that a blank stays a blank until Ahmed supplies the value. This is the campaign-agnostic principle made operational.
- English-first and RTL constraints baked in. The brief, the validation report, and the kickoff scope all carry the no em dash, no tatweel, Western numerals rules. Generic templates are language-blind.
- A real verification envelope. handoff-contract.md gives every artifact a qa block (skill_eval, arabic_qa, english_qa, design_qa, compliance, brand_qa) and a status that must reach qa-passed before it crosses a boundary. No public brief template carries a structured QA state with the artifact.
- Stop-and-ask as a hard rule, not a suggestion. Across the intake hub and both sub-skills, a missing needed variable halts the run at the human gate. Public templates have no enforcement; they are documents, not gates.
- Suppression as a first-class field. Section 3 suppression (who is excluded and why) is standard in lifecycle practice but absent from almost every generic campaign-brief template.
- Planning-estimate vs resolve-at-send-time distinction on audience_size. The brief carries an estimate and the lifecycle-package resolves the exact number later. Public templates treat audience size as one static value.

---

## Recommendations

Specific edits, prioritized, each tied to a source. These are proposals for the brief
template and the intake skills. Per the engine rules, no template or skill file is edited
here; this doc only recommends.

High:

1. Add a SMART check to brief-validate and a SMART hint to section 2 of the brief template. In `brief-validate/SKILL.md`, add a step that tests objective and success_metric against Specific, Measurable, Achievable, Relevant, Time-bound, and flags a non-measurable objective the same way a MISSING field is flagged. In the template, annotate success_metric to require a number and a date. Tied to [Smart Insights](https://www.smartinsights.com/goal-setting-evaluation/goals-kpis/define-smart-marketing-objectives/) and [Digital Marketing Institute](https://digitalmarketinginstitute.com/blog/what-are-smart-objectives-in-digital-marketing).
2. Add a Background and context section to `_TEMPLATE-campaign-brief.md`, before Objective: why now, the business problem, what came before, link to the prior report-artifact if any. Add a matching row to the validation report table. Tied to [HubSpot](https://blog.hubspot.com/marketing/creative-brief) and [Meltwater](https://www.meltwater.com/en/blog/marketing-campaign-brief-template).
3. Add a key_message field (provisional, single-minded) to section 2 or a new "Message" section, so the angle in stream 2 has a brief-level anchor to refine rather than originate. Mark it refinable by strategy-lead, not a hard input. Tied to [Meltwater](https://www.meltwater.com/en/blog/marketing-campaign-brief-template) and [HubSpot](https://blog.hubspot.com/marketing/creative-brief).

Medium:

4. Add a reporting_cadence field to section 6 or section 9, naming when results are reviewed against success_metric, so streams 8 and 9 inherit the review rhythm from the brief. Tied to [Meltwater](https://www.meltwater.com/en/blog/marketing-campaign-brief-template).
5. Add campaign-level tone descriptors to section 7 (a short adjective set that sits on top of the global brand voice), and have arabic-copy-qa and english-copy-qa read them. Tied to [Asana](https://asana.com/resources/how-write-creative-brief-examples-template) and [HubSpot](https://blog.hubspot.com/marketing/creative-brief).
6. Split section 8 into mandatories (must include) and constraints (must not), and echo the CLAUDE.md guardrails as a brief-level mandatories checklist so each guardrail is acknowledged per campaign. Tied to the creative-brief consensus on mandatories ([Asana](https://asana.com/resources/how-write-creative-brief-examples-template)).
7. Add a deliverables list field, expected assets and counts, to the brief or to kickoff-scope, so scope is visible before stream 3 and stream 4 run. Tied to [Asana](https://asana.com/resources/how-write-creative-brief-examples-template).

Low:

8. Add a stakeholders and reviewers field to section 9, even if most rows are Ahmed today, so consulted and informed parties have a home. Tied to [Paperform](https://paperform.co/templates/agency-creative-project-brief-intake-form/) and [Meltwater](https://www.meltwater.com/en/blog/marketing-campaign-brief-template).
9. State a one-to-two-page ceiling in the template header. Tied to [monday.com](https://monday.com/blog/marketing/brand-brief-template/).
10. Add an asset-handoff or source-location note to assets_available in section 7. Tied to [SEOptimer](https://www.seoptimer.com/blog/project-intake-form/) and [Paperform](https://paperform.co/templates/agency-creative-project-brief-intake-form/).
