---
name: keyword-and-intent-research
description: Arabic and English keyword and search-intent research, clustered and prioritized. Use when a campaign needs to know what its audience searches for, triggers on "keyword research," "search intent," "keyword clusters," "search volume," "what do they search for," "keyword map." Produces the seo-package keyword_map for on-page work and content briefs.
---

# Keyword and intent research (sub-skill of seo)

Finds the queries the Maharat audience actually searches, in Arabic and English, groups them
into clusters by topic and intent, and ranks them by priority. English-first. Feeds the
on-page specs and the content briefs. Assembled into the `seo-package` by the seo hub.

## Purpose

Give every page and article a real query to earn, with its intent understood, so on-page work
and content target demand instead of guesses. One machine, any campaign.

## When to use

- A campaign needs its keyword and intent landscape mapped before pages or articles are built.
- A content cluster needs a primary query and supporting queries with clear intent.

## Inputs

- The `strategy-artifact`: segments, angle, offer_framing (what the audience cares about).
- The brief: objective, target topics or pages.
- `context/brand-voice.md`: voice and the hard mechanical rules.
- Search data when available: search console, keyword tools (only approved tools).

## Steps

1. Seed from the strategy angle and segments: list the topics the audience searches around.
2. Expand each seed into Arabic and English queries. Arabic is primary, English in parallel,
   never a literal translation that ignores how Arabic speakers actually phrase a search.
3. Tag each query with intent: informational, navigational, commercial, transactional, or
   generative (answer-engine). Generative intent is the 2026 case where being cited in an AI
   answer matters more than ranking first. Flag a cluster as worth pursuing for AI-answer
   citation when the query is a definitional or how-to question an answer engine resolves
   inline, rather than one a searcher clicks through to satisfy.
4. Group queries into clusters, one clear primary per cluster plus supporting queries.
5. Prioritize each cluster by relevance to the offer, intent value, and feasibility.
6. Flag any query that would need an unconfirmed offer, price, or Skill Path title to serve,
   and stop and ask rather than inventing one.

## Output

The `seo-package` keyword_map:

```
clusters[]   each: cluster_name, primary_query (ar, en), supporting_queries[],
             intent (informational | navigational | commercial | transactional |
             generative), priority (high | medium | low), maps_to (page or article)
language     ar and en handled side by side, RTL noted for Arabic queries
notes        gaps, ambiguities, queries blocked on a missing brief value
```

See `templates/keyword-and-intent-map.md`.

## Hard rules

- English-first, English in parallel, correct RTL for Arabic queries. No em dashes. No tatweel.
  Western numerals only.
- Never invent an offer, price, Skill Path title, or instructor name to justify a query. If a
  cluster needs one and the brief is silent, stop and ask.
- Never imply certificate accreditation in any query framing or note.

## How it connects

Feeds the seo hub's keyword_map, which on-page-optimization and the content_briefs build from.
Runs the gate stack: skill eval, then `arabic-copy-qa` / `english-copy-qa` for any
customer-facing query phrasing, then `brand-qa-reviewer`, per `runtime/verification.md`.
