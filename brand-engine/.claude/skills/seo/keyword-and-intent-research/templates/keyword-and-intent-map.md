# Keyword and intent map template

One block per cluster. English-first, English in parallel. All example queries are
illustrative only. Replace them. Do not invent offers, prices, Skill Path titles, or
instructor names to justify a query. If a cluster needs one and the brief is silent, stop
and ask.

## Cluster block

```
cluster_name:     <short label for the topic cluster>
primary_query_ar: <the main Arabic query, RTL>
primary_query_en: <the main English query>
supporting_queries:
  - ar: <supporting Arabic query>   intent: informational | navigational | commercial | transactional | generative
  - en: <supporting English query>  intent: informational | navigational | commercial | transactional | generative
intent:           <dominant intent for the cluster, generative when AI-answer citation is the goal>
priority:         high | medium | low
maps_to:          <page URL or article brief id this cluster serves>
notes:            <gaps, ambiguities, or a value blocked on the brief>
```

## Illustrative example (replace before use)

```
cluster_name:     learn-a-new-skill
primary_query_ar: كيف اتعلم مهارة جديدة
primary_query_en: how to learn a new skill
supporting_queries:
  - ar: مهارات مطلوبة في سوق العمل   intent: informational
  - en: best skills to learn in 2026  intent: informational
intent:           informational
priority:         high
maps_to:          /skills-guide
notes:            none
```

## Checklist before handoff

- Arabic and English both present, English-first, not a literal translation.
- Every query tagged with one intent, including generative (answer-engine) where it applies.
- Each cluster has one primary query and a priority.
- RTL noted for Arabic queries.
- No em dash, no tatweel, Western numerals only.
- No invented offer, price, Skill Path title, or instructor name. No accreditation implication.
- Every cluster maps to a page or an article brief.
