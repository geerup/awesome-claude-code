# On-page spec template

One block per page. One clear intent per page. English-first, English in parallel, RTL noted.
All example values are illustrative only. Replace them. Do not invent offers, prices, Skill
Path titles, or instructor names in a title, meta, or schema field. If the page needs one and
the brief is silent, stop and ask. Never imply certificate accreditation.

## Page spec block

```
url:            <the page this spec governs>
cluster:        <the keyword_map cluster this page serves>
primary_query_ar: <single Arabic intent, RTL>
primary_query_en: <single English intent>
intent:         informational | navigational | commercial | transactional
title_ar:       <title tag, Arabic, query-led, within shown length>
title_en:       <title tag, English, query-led>
meta_ar:        <meta description, Arabic, plain and empowering>
meta_en:        <meta description, English, plain and empowering>
headings:
  h1:           <one H1 that matches intent>
  h2:           [<h2>, <h2>]
  h3:           [<h3>]
internal_links:
  - anchor_text: <anchor>   target_url: <url>   why: <related cluster or page>
schema:         <type, e.g. Organization | Course | FAQ | Breadcrumb>, fields: <only brief-traceable values>
notes:          <intent conflict resolved, value blocked on the brief>
```

## Illustrative example (replace before use)

```
url:            /learn-a-new-skill
cluster:        learn-a-new-skill
primary_query_ar: كيف اتعلم مهارة جديدة
primary_query_en: how to learn a new skill
intent:         informational
title_ar:       كيف تتعلم مهارة جديدة، خطوة بخطوة
title_en:       How to Learn a New Skill, Step by Step
meta_ar:        مسار واضح يبني مهارة تبقى معك، بخطوة واحدة كل يوم.
meta_en:        A clear path that builds a skill you keep, one step a day.
headings:
  h1:           كيف تتعلم مهارة جديدة
  h2:           [ابدأ بخطوة واحدة, اختر مسارك]
  h3:           [نصائح لوقتك المزدحم]
internal_links:
  - anchor_text: المسارات   target_url: /skill-paths   why: related cluster
schema:         FAQ, fields: question and answer pairs only, no invented claims
notes:          none
```

## Checklist before handoff

- One clear intent per page, one primary query.
- Title and meta in Arabic and English, English-first, RTL noted.
- Headings outline matches the intent, one H1.
- Internal links carry anchor text and a reason.
- Schema fields trace to the brief, no invented claims or titles.
- No em dash, no tatweel, Western numerals only.
- No accreditation implication anywhere.
- Any value blocked on the brief is flagged, not invented.
