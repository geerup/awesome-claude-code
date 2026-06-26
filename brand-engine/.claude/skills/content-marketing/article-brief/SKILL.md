---
name: article-brief
description: Write an SEO-informed English-first article brief, target query, intent, outline, internal links, and CTA, for the copywriters to author from. Use when a planned article needs its brief before copy is written, triggers on "article brief," "content brief," "blog brief," "brief the article," "outline the article." Produces a content-package article_brief; the final copy is authored later by copywriter-ar or copywriter-en, not here.
---

# Article brief (sub-skill of content-marketing)

Writes the brief for a single article: the target query and intent, a heading outline, the
internal links, and the one CTA, so a copywriter can author it on target. English-first, with
the English equivalent in parallel. Assembled into the `content-package` by the
content-marketing hub. The article copy itself is authored later by the copywriters, not here.

## Purpose

Give each article one query to earn, one clear intent, a structured outline, and the links and
CTA it needs, so the copywriter writes to a target instead of a blank page. One machine, any
campaign.

## When to use

- A calendar item is ready to brief before copy is written.
- A copywriter needs a clear target query, intent, outline, and CTA for an article.

## Inputs

- The editorial_calendar item: theme, angle_link, seo_cluster.
- The `seo-package`: keyword_map cluster, on_page_specs[] for the matching page.
- The `strategy-artifact`: angle and offer_framing for positioning and the CTA.
- The brief: offer details only when the article shows them.
- `context/brand-voice.md`: voice and the hard mechanical rules.

## Steps

1. Set one target query and one intent for the article, from the assigned SEO cluster.
2. Write a heading outline: one H1 matching intent, H2 and H3 that structure the answer.
3. List internal links in and out, with anchor text, tied to related clusters and pages.
4. Set exactly one CTA, tied to the angle and the conversion path. No competing actions.
5. Note the language plan: English-first, English in parallel, RTL noted.
6. Flag any element that would need an unconfirmed offer, price, or Skill Path title, and stop
   and ask rather than inventing one.
7. Hand the brief to copywriter-ar and copywriter-en. Do not write the article copy here.

## Output

The `content-package` article_brief:

```
id             e.g. article-learn-a-skill
target_query   ar and en, the single query this article earns
intent         informational | navigational | commercial | transactional
outline        h1, h2[], h3[] matching intent
internal_links each: anchor_text, target_url, why
cta            exactly one, tied to the angle and conversion path
language_plan  ar-first, en in parallel, RTL noted
notes          values blocked on the brief, intent kept singular
```

See `templates/article-brief.md`.

## Hard rules

- One target query and one intent per article. One CTA. English-first, English in parallel,
  correct RTL. No em dashes. No tatweel. Western numerals only.
- This is a brief, not the copy. The article is authored by copywriter-ar or copywriter-en.
- Never invent an offer, price, Skill Path title, or instructor name. If the brief needs one
  and the source brief is silent, stop and ask. Never imply certificate accreditation.

## How it connects

Feeds the content-marketing hub's article_briefs[], handed to copywriter-ar and copywriter-en
for authoring. The authored copy then runs the gate stack: skill eval, then `arabic-copy-qa` /
`english-copy-qa`, then `brand-qa-reviewer`, per `runtime/verification.md`.
