# handoff-contract.md: the artifacts streams pass to each other

In a pipeline (Shape 1) each stage hands a structured artifact to the next. This file
defines those artifacts so a downstream agent always knows what it is receiving and an
upstream agent knows what it owes. Artifacts are the only thing that crosses a stream
boundary. An agent never reaches into another agent's working state.

Every artifact carries a common envelope, then a stream-specific body.

## Common envelope (on every artifact)

```
campaign_id     from the active brief filename, e.g. 2026-06-nonpayer-email
produced_by     the agent name
stream          the stream number and name
status          draft | qa-passed | gated-pending | approved
qa              { skill_eval, arabic_qa, english_qa, design_qa, web_design_qa, compliance, brand_qa } each pass|fail|na
open_items      anything the producer could not resolve (so downstream is not surprised)
brief_refs      which brief variables this artifact consumed (offer, price, target, dates)
```

An artifact with `status` below `qa-passed` does not cross a boundary. The QA block must
show the gates that apply to that stream (see `verification.md`).

## Stream-specific bodies

### strategy-artifact (stream 2 -> 3, 4, 7)
```
segments[]        each: name, size, definition, why
angle             the core message and its rationale
offer_framing     how the brief's offer is positioned (not the price itself unless shown)
channel_plan      which streams this campaign uses, and entry point (paid | owned)
success_metric    what stream 8 will measure against
```

### creative-package (stream 3 -> 4, 5)
```
concepts[]        each: id, description, rationale tied to angle
prompts[]         image or video prompts, text-free (no AR baked in)
asset_briefs[]    dimensions, safe areas, copy-overlay slots (empty, for copywriter-ar)
channel_routing   which concept goes to paid vs lifecycle
```

### copy-package (stream 4 -> 5, 6, 7)
```
variants[]        each: id, segment, headline, body, one CTA, language (ar | en)
subject_lines[]   for email assets, with the chosen primary flagged
fills             which asset_brief copy slots each variant fills
```

### paid-launch-package (stream 5 -> human gate)
```
staged_structure  campaign, ad sets, ads, targeting, placements, budget, schedule (paused)
checklist         pre-launch checks and their pass state
spend_on_approval the maximum spend this incurs if approved, with currency and window
flips_live        one plain sentence of what going live does
```

### web-design-package (stream 6 design -> conversion-engineer, brand gate, human gate)
```
information_architecture  pages and sections, order, the job of each
ux_flow                   click -> page -> signup gate -> lifecycle, the path and key states
wireframe                 region-level structure per page, one primary action per view
visual_direction          how the brand constants apply to the web surface (text-free imagery)
web_asset_brief           imagery needs, dimensions, safe areas, copy-overlay slots (empty, ar/en)
conversion_intent         the single primary action the page optimizes toward
design_spec               components, grid, breakpoints, type scale, tokens, states, RTL per
                          breakpoint, accessibility, performance budget, copy region -> variant id
web_design_qa             the web-designer's verdict: pass | fail with a fix-list
```
Produced by web-design-director (the direction fields) and web-designer (design_spec and
web_design_qa). conversion-engineer consumes it to fill the conversion-package page field.

### conversion-package (stream 6 -> 7, 8, human gate)
```
page              landing page spec or build ref, RTL-correct, realizing the web-design-package design_spec
gate              signup gate type (email | whatsapp) and platform wiring
event_plan        events: page_view, gate_view, submit, confirm, revenue (purchase or
                  subscription_start); pixel/capi and ga4 mapping, with event_id dedup
open_items        platform-not-confirmed, mobile-mapping-to-confirm, etc.
```

### lifecycle-package (stream 7 -> human gate)
```
flow              ordered messages, each with trigger, audience, channel, copy variant ref
audience_size     resolved from owned-audience data (e.g. ~18,000 non-payers)
send_on_approval  one plain sentence of what the send does and to how many
suppression       who is excluded and why (already paying, unsubscribed, etc.)
```

### report-artifact (stream 9 -> next campaign's strategy-lead)
```
results           metrics vs the strategy-artifact success_metric
what_worked       with evidence
what_to_change    concrete, for the next brief
learnings_log_ref where this was appended for reuse
```

### tracking-package (data-tracking-engineer, streams 6 and 8 -> conversion-engineer, analytics-reporter, human gate)
```
events            page_view, gate_view, submit, confirm, and a post-signup revenue event
                  (purchase or subscription_start), each with where it fires
pixel_capi_map    Meta Pixel and Conversions API mapping (revenue event maps to Meta Purchase)
ga4_map           GA4 event and parameter mapping (revenue event maps to GA4 purchase)
event_id_dedup    any event sent by both Pixel and CAPI carries one shared, non-identifying
                  event_id so Meta deduplicates it (no double-counting), the revenue event in particular
mobile_map        Apple IAP and Google Play mapping, flagged to-confirm (never guessed)
warehouse_refs    the BigQuery queries that read these for monitoring
open_items        platform-not-confirmed, mobile-mapping-to-confirm, access-not-granted
```

### organic-package (organic-social, entry point C -> conversion-engineer, human gate)
```
content_plan         themes and posts mapped to the strategy angle and segments
post_calendar        ordered posts: channel, format, asset ref, caption variant ref
distribution_routing which owned accounts, and what feeds the signup gate
repurposing_notes    how one asset becomes many formats
publish_on_approval  one plain sentence of what publishing does and where
```

### qa-verdict (verifiers: brand-qa-reviewer, compliance-privacy-reviewer, designer design-qa, web-designer web-design-qa)
```
gate              brand_qa | compliance | design_qa | web_design_qa | arabic_qa | english_qa
result            pass | fail
fix_list[]        on fail, each: { check, span (quoted), fix }. Empty on pass.
```
A verifier never edits the asset. On fail it returns the `qa-verdict` to the author; on pass
it updates the matching field in the artifact's `qa` envelope block and the asset advances.

### media-plan-package (performance-marketer -> paid-build-engineer, human gate)
```
channels            the paid channels in play (Meta, Google, TikTok, YouTube, etc.)
budget_split        allocation across channels, traced to the brief budget (never assumed)
audiences           audience strategy and targeting per channel
bid_strategy        bid approach and optimization goal per channel
flighting           schedule and pacing
success_metric_link the strategy-artifact success_metric this plan serves
spend_on_approval   the maximum spend this incurs if approved, currency and window
open_items          targets-not-confirmed, channel-access-not-granted, etc.
```

### aso-package (aso-specialist -> data-tracking-engineer, human gate)
```
store              title, subtitle, description, keyword field, localization (ar and en)
creatives          screenshot and preview specs, text-free for generated images
experiments        store A/B tests, one variable each
reviews_response_policy  on-brand reply guidance, escalation for compliance triggers
open_items         store-access-not-granted, asset-not-confirmed, etc.
```

### seo-package (seo-specialist -> content-marketer, conversion-engineer, human gate)
```
keyword_map        clusters and intent, Arabic and English, with priority
on_page_specs      per page: title, meta, headings, internal links, schema
technical_findings crawl, speed, indexation, sitemaps, hreflang, RTL
content_briefs     SEO-informed briefs handed to content-marketer and copywriters
open_items         access-not-granted, data-pending, etc.
```

### content-package (content-marketer -> copywriter-ar, copywriter-en, organic-social, human gate)
```
editorial_calendar themes and cadence mapped to the angle and SEO clusters
article_briefs     per article: target query, intent, outline, internal links, CTA
distribution_plan  how one piece is repurposed across email, organic, and other channels
open_items         lineup-not-confirmed, imagery-not-confirmed, etc.
```

### pr-package (pr-comms -> compliance-privacy-reviewer, brand-qa-reviewer, human gate)
```
announcement_plan  what can be said, and what stays out (no roadmap, fundraising, accreditation)
press_release_ref  the press release draft (copy authored by copywriter-ar or copywriter-en)
media_list         target media and the outreach plan
guardrail_check    confirmation that only public or brief-confirmed facts are used
publish_on_approval one plain sentence of what publishing or distributing does
open_items         quote-approval-pending, embargo-not-set, etc.
```

## The rule that makes handoffs safe

A downstream agent validates the envelope before it starts: right campaign_id, status at
least qa-passed, required body fields present, open_items read and accounted for. If the
artifact is incomplete, the downstream agent stops and returns it, rather than filling the
gap by inventing a value. Invented values are exactly what the brand and brief guardrails
exist to prevent.
