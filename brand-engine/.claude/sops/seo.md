# SOP: SEO

SEO stream. Owner: seo-specialist. Mode: reasoning. Turns a validated brief and strategy into
search visibility across Arabic and English: keyword and intent research, on-page
optimization, and the technical foundation (hreflang, RTL, crawlability). It assembles an
`seo-package` and hands content briefs to content-marketer and the copywriters. It does not
write final copy and it does not publish.

English-first, RTL-correct, no em dashes, no tatweel, Western numerals, no accreditation claims.

---

## Trigger

A brief with organic search in scope, or a channel_plan that includes SEO. SEO also feeds the
content-marketing stream, which depends on its keyword and intent map.

## Inputs

- The `strategy-artifact` (stream 2): the angle, segments, offer framing, channel_plan.
- The brief: the markets (GCC, primary Saudi Arabia), the languages (Arabic and English), the
  site or properties in scope, the window. If a market, language, or property is not in the
  brief, stop and ask.
- Keyword and search-intent data from the research tools and the search console.
- On-page copy and content are written by `content-marketer` and the copywriters, referenced
  by brief or variant id, never written here.

## Steps

1. Research keywords and search intent per language. Map each query cluster to an intent
   (informational, comparison, transactional) and to the segment it serves. Arabic and English
   are researched in parallel; Arabic is primary.
2. Build the keyword and intent map: clusters, priority, the page or content that should own
   each, and the gap where no page yet exists. The gaps become content briefs for
   content-marketer.
3. Plan on-page optimization: titles, meta descriptions, headings, internal links, and the
   schema markup per page. Each draws on the intent map; nothing claims an offer, price, or
   feature not confirmed in the brief or context. No accreditation implication in any tag.
4. Plan the technical foundation: hreflang for the Arabic and English alternates, RTL
   correctness, canonical tags, crawlability, the sitemap, and page speed. Flag any
   data-residency or platform open item; do not assume a platform.
5. Write content briefs for content-marketer: the target cluster, the intent, the angle tie,
   the on-page targets, and the internal links. The brief specifies the search target; the
   article is written downstream and runs its own copy QA and brand QA.
6. Assemble the `seo-package` and hand the content briefs to content-marketer and the
   copywriters. A live site change (publishing on-page or technical changes) is a gated action
   at the human gate.

## Output

An `seo-package` (wrapped in the common envelope, per `runtime/handoff-contract.md`):
- keyword_intent_map: clusters, intent, priority, the owning page, and the gaps.
- on_page_plan: titles, metas, headings, internal links, and schema per page.
- technical_plan: hreflang, RTL, canonicals, crawlability, sitemap, page speed.
- content_briefs: the briefs handed to content-marketer, each with cluster, intent, targets.
- open_items: property-access not confirmed, platform or data-residency to confirm.

## Quality bar

- The keyword and intent map covers Arabic and English, with Arabic primary, mapped to the
  segments and the angle.
- On-page tags and any customer-facing copy are QA-passed (skill eval, arabic-copy-qa for
  Arabic, english-copy-qa for English, then brand-qa-reviewer, per `runtime/verification.md`).
- Technical plan includes hreflang for AR and EN alternates and verified RTL correctness.
- No invented offer, price, offer title, content lineup, or an unverified claim in any tag or
  brief. No accreditation implication anywhere.
- A live site change is gated; nothing publishes to production before the human gate clears.

## Example output (shape, not real values)

```
keyword_intent_map:
  - { cluster, language (ar primary), intent, priority, owning_page or GAP, segment }
on_page_plan:
  - { page, title, meta_description, headings, internal_links, schema_type }
technical_plan: { hreflang: ar+en alternates, rtl: verified, sitemap, canonicals, speed }
content_briefs:
  - { cluster, intent, angle_tie, on_page_targets, internal_links } -> content-marketer
open_items: property-access-to-confirm, platform-to-confirm
```

## Review owner

Ahmed, at the human gate, for any live site change. Approval is per action. The seo-specialist
proposes and briefs; the on-page or technical change publishes only after the gate clears.

House rule: facts come from `context/`, variables come from the active brief. When both are
silent on something needed, stop and ask. Do not invent a value.
