# SOP: Content marketing

Content marketing stream. Owner: content-marketer. Mode: reasoning. Turns the SEO and
strategy work into an editorial plan, article briefs, and a distribution plan. It briefs and
sequences copy; it does not write final copy and it does not publish. Final copy is authored
by copywriter-ar (English-first) and copywriter-en and runs the copy QA and brand QA gates.

English-first, RTL-correct, no em dashes, no tatweel, Western numerals, no accreditation claims.

---

## Trigger

A brief with content marketing in scope, or a channel_plan that includes content. Content
marketing depends on the `seo-package` keyword and intent map and the content briefs it hands
over.

## Inputs

- The `strategy-artifact` (stream 2): the angle, segments, offer framing, channel_plan,
  success_metric.
- The `seo-package` content briefs from seo-specialist: the target clusters, intent, and
  on-page targets.
- The brief: the markets, the languages (Arabic and English), the publishing properties, the
  cadence, the window. If the cadence, properties, or window are not in the brief, stop and ask.
- Final copy is written by `copywriter-ar` and `copywriter-en`, referenced by variant id,
  never written here. Visual assets come from `creative-director` and the designer.

## Steps

1. Build the editorial calendar from the SEO content briefs and the angle: ordered articles,
   each with a date inside the window, the property, the language, the target cluster, and the
   segment it serves. Do not invent a cadence or a property; use the brief.
2. Write the article briefs for the copywriters: the working title, the target cluster and
   intent, the angle tie, the on-page targets from SEO, the internal links, and the CTA toward
   the signup gate. The brief specifies the article; it does not write it.
3. Route the article copy to `copywriter-ar` (English-first) and `copywriter-en`. Reference
   QA-passed variants by id. Each article runs the gate stack: skill eval, the language copy QA
   matched to its language, then brand-qa-reviewer.
4. Plan the distribution: where each article is published and how it is repurposed across the
   owned channels (organic social, email, the site). Repurposing reuses one article across
   formats; it does not restate a new message.
5. Set the routing to the signup gate: each piece carries a CTA to the gate (the entry to
   lifecycle), with no personal or sensitive data in any tracking parameter.
6. Assemble the `content-package` and stop at the human gate. Publishing is a gated action;
   nothing publishes without sign-off.

## Output

A `content-package` (wrapped in the common envelope, per `runtime/handoff-contract.md`):
- editorial_calendar: ordered articles, each with date, property, language, cluster, segment.
- article_briefs: the briefs handed to the copywriters, each with title, intent, targets, CTA.
- distribution_plan: where each article publishes and how it is repurposed across channels.
- routing_to_gate: how each piece routes the click to the signup gate.
- publish_on_approval: one plain sentence of what publishing does and where.
- open_items: property-access not confirmed, copy not yet QA-passed, asset not delivered.

## Quality bar

- Every article's copy is QA-passed (skill eval, arabic-copy-qa for Arabic, english-copy-qa
  for English, then brand-qa-reviewer, per `runtime/verification.md`). RTL renders correctly.
- The calendar maps to the SEO clusters, the strategy angle, the segments, and the
  success_metric.
- No invented offer, price, Skill Path title, content lineup, or instructor name in any brief
  or article. No accreditation implication anywhere.
- No personal or sensitive data in any tracking parameter in the routing.
- Publishing is gated; nothing publishes before the human gate clears.

## Example output (shape, not real values)

```
editorial_calendar:
  - { date (in window), property, language (ar primary), cluster, segment, brief_ref }
article_briefs:
  - { working_title, cluster, intent, angle_tie, on_page_targets, internal_links, cta_to_gate }
distribution_plan:
  - { article, primary_property, repurposed_into: [organic social, email, site] }
routing_to_gate: each piece -> signup gate (no PII in tracking parameters)
publish_on_approval: "Publishes the AR and EN articles to the properties in scope."
open_items: copy-qa-pending, property-access-to-confirm
```

## Review owner

Ahmed, at the human gate, for any publish. Approval is per publish action. The content-marketer
briefs and sequences; copy is authored by the copywriters and runs copy QA and brand QA before
it is package-ready. Publishing happens only after the gate clears. Silence is not approval.

House rule: facts come from `context/`, variables come from the active brief. When both are
silent on something needed, stop and ask. Do not invent a value.
