# Benchmark: SEO and content

How the Maharat SEO and content-marketing skills compare to current, reputable real-world
frameworks for SEO content briefs, search-intent mapping, on-page SEO, technical SEO audits,
editorial calendars, and content distribution. Reviewed June 2026. This is a benchmark and a
recommendation set only. No skill file was edited.

## Sources reviewed (web)

- Content Harmony, How to Write SEO-Focused Content Briefs in 8 Easy Steps:
  https://www.contentharmony.com/blog/how-to-build-content-briefs/
- First Page Sage, SEO Best Practices for 2026:
  https://firstpagesage.com/seo-blog/seo-best-practices/
- Crawl Compass, On-Page SEO Checklist 2026 (titles, intent, entities, links):
  https://crawlcompass.com/blog/on-page-seo-checklist
- DebugBear, Technical SEO Checklist, The Complete Guide for 2026:
  https://www.debugbear.com/blog/technical-seo-checklist
- Digital Applied, Technical SEO Audit Checklist 2026 (200+ items):
  https://www.digitalapplied.com/blog/technical-seo-audit-checklist-200-items
- Content Marketing Institute, Editorial Calendar Tools and Templates:
  https://contentmarketinginstitute.com/ai-content-creation-tools/editorial-calendar-tools-and-templates-to-help-you-master-your-content-to-do-list
- Backlinko, Content Calendar Template for 2026:
  https://backlinko.com/templates/marketing/content-calendar
- Digital Applied, Content Calendar Template 2026, Strategy and Planning:
  https://www.digitalapplied.com/blog/content-calendar-template-2026-strategy-planning

Note: several of these sources serve bot-protected pages, so the detail below is drawn from
the indexed summaries of each, cross-checked across more than one source before it was used.

## Best-in-class elements

What the current frameworks converge on:

SEO content brief
- A brief carries: target keyword, primary intent, secondary intent, audience and funnel
  stage, key subtopics, title tag, page title, meta description, internal linking targets,
  and one CTA (Content Harmony, Averi, DeepSeeds).
- The brief is the contract a writer authors against, so the writer hits a target rather
  than a blank page.

Search-intent mapping
- Four classic intents: informational, navigational, commercial investigation, transactional.
- A fifth is now called out in 2026 sources: generative AI intent, where being cited in an
  AI answer can matter more than ranking first (First Page Sage, Gravitas, SeekLab).
- Group queries by topic and meaning first, not exact-match wording, because engines lean on
  semantics and entities. Assign each cluster to one page type, its internal links, and the
  next step. Intent should also drive what you fix first in crawl, indexing, links, and schema.

On-page SEO
- One H1 matching the topic, logical H2 and H3 hierarchy with related phrases.
- Title under about 60 characters, meta description about 150 to 160 characters.
- Schema is treated as expected, not optional: Article, FAQ, How-To, Breadcrumb where the
  content truly fits.
- Internal links: roughly 5 to 10 contextual links per 2,000 words, descriptive anchor text,
  spreading authority across the site.
- Entity-rich content and one clear intent per page are the spine of the 2026 checklist.

Technical SEO audit
- Crawlability and indexation are audited before content, because most ranking issues trace
  back there.
- Key templates are index,follow, self-canonical, returning 200.
- XML sitemaps contain only canonical 200 URLs and are submitted in Search Console. The
  indexed count should roughly match the canonical URL count, a gap over about 30 percent
  warrants investigation.
- Canonical, hreflang, sitemap, and internal links must all agree on the preferred URL.
- For multi-country or multi-language sites, correct hreflang is stressed, and wrong hreflang
  is worse than none.
- Core Web Vitals 2026 field thresholds at the 75th percentile: LCP at or under 2.5s, INP at
  or under 200ms, CLS at or under 0.1. INP has replaced the older FID metric.
- Audit on a quarterly cadence to catch regressions.

Editorial calendar
- A calendar row captures status, owner, primary keyword, cluster, channel, CTA, repurpose
  plan, and a success metric.
- Plan across horizons: annual themes, quarterly pillars, monthly briefs, weekly production.
- Themes map to strategy and demand, not filler.

Content distribution and repurposing
- One cornerstone or source piece is atomized into many formats: newsletter, social posts,
  carousels, short video, with a named owner per derivative and a stated sequence.
- The repurpose plan is decided at planning time, not after publish, and is tracked on the
  calendar row itself.

## Our coverage

Our skills already cover the large majority of the above.

SEO stream
- `skills/seo/SKILL.md` routes keyword, on-page, and technical work and assembles the
  `seo-package` (keyword_map, on_page_specs[], technical_findings[], content_briefs[]).
- `skills/seo/keyword-and-intent-research/SKILL.md` and its template
  `keyword-and-intent-research/templates/keyword-and-intent-map.md`: clusters with one primary
  query, supporting queries, intent tag (informational, navigational, commercial,
  transactional), priority high or medium or low, and maps_to a page or article. Arabic and
  English side by side, RTL noted.
- `skills/seo/on-page-optimization/SKILL.md` and
  `on-page-optimization/templates/on-page-spec.md`: one intent per page, title, meta, H1 and
  H2 and H3 outline, internal links with anchor text and a reason, and schema types
  (Organization, Course, FAQ, Breadcrumb) constrained to brief-traceable fields.
- `skills/seo/technical-seo/SKILL.md` and
  `technical-seo/templates/technical-seo-audit.md`: crawlability, speed, indexation, sitemaps,
  hreflang (reciprocal, correctly coded), RTL correctness, canonicalization. Findings carry
  severity and a concrete fix, plus an hreflang map and RTL checks per priority page.
- `sops/seo.md`: the same stream as a reasoning SOP, markets and languages from the brief, a
  live site change gated at the human gate.

Content-marketing stream
- `skills/content-marketing/SKILL.md` routes calendar, brief, and distribution work and
  assembles the `content-package`.
- `skills/content-marketing/editorial-calendar/SKILL.md` and its template: items with theme,
  angle_link, seo_cluster, primary query (ar, en), format, target_date, owner, status, plus a
  stated cadence with a realism note. Every theme maps to the angle and an SEO cluster.
- `skills/content-marketing/article-brief/SKILL.md` and its template: one target query, one
  intent, H1 and H2 and H3 outline, internal links with reason, exactly one CTA, language plan.
- `skills/content-marketing/content-distribution/SKILL.md` and its template: one source angle
  carried across derivatives (email, organic-social, other), each with CTA, owner, language,
  routing notes, plus a stated sequence.
- `sops/content-marketing.md`: the same stream as an SOP, routing each piece to the signup
  gate with no PII in tracking, publishing gated.

Handoff
- `runtime/handoff-contract.md` defines `seo-package` (keyword_map, on_page_specs,
  technical_findings, content_briefs, open_items) and `content-package` (editorial_calendar,
  article_briefs, distribution_plan, open_items), each in the common QA envelope.

## Gaps and missing elements (prioritized)

1. Generative AI / answer-engine intent is not represented. Our keyword map recognizes four
   intents (informational, navigational, commercial, transactional). The 2026 sources add a
   fifth, generative AI intent, and treat AI-answer citation as a distinct goal. Neither
   `keyword-and-intent-research` nor `on-page-optimization` accounts for it. High priority,
   because it changes which queries are worth chasing and how a page is structured.

2. No measurable Core Web Vitals thresholds. `technical-seo` lists speed as an audit area but
   names no targets. The current standard is concrete: LCP at or under 2.5s, INP at or under
   200ms, CLS at or under 0.1, at the 75th percentile of field data, INP having replaced FID.
   Our speed findings cannot be scored pass or fail without these. High priority, cheap to add.

3. No indexation gap heuristic. Sources call out the indexed-versus-canonical gap (investigate
   above roughly 30 percent) and the index,follow plus self-canonical plus 200 baseline. Our
   indexation step says compare crawlable to indexed but gives no threshold or template
   baseline. Medium priority.

4. On-page brief has no explicit length guidance or internal-link density. Sources give title
   under about 60 characters, meta about 150 to 160, and roughly 5 to 10 internal links per
   2,000 words. Our on-page template says title within shown length and lists internal links
   but sets no count or character guidance, so two authors can produce very different specs.
   Medium priority. Note: any character or RTL length rule must respect Arabic, where visual
   width and pixel truncation differ from a raw character count.

5. Editorial calendar lacks a success-metric field and a horizon view. Best-in-class rows
   carry a per-item success metric, and planning runs annual, quarterly, monthly, weekly. Our
   calendar item has theme, cluster, format, date, owner, status, but no success metric and no
   explicit horizon layering above the single window. Medium priority. The stream does carry a
   campaign success_metric upstream in the strategy-artifact, so this is a per-item gap, not a
   total absence.

6. Article brief carries no secondary intent or subtopic-coverage field. Sources brief primary
   plus secondary intent and key subtopics or entities to cover. Our article-brief is one
   target query and one intent by design (a deliberate single-intent discipline), with an
   outline standing in for subtopics. Worth a conscious decision: keep the single-intent rule
   but consider an explicit entities or subtopics-to-cover line. Low to medium priority.

7. Distribution plan has no per-derivative success or tracking measure and no AI-surface
   format. Sources tie repurposing to a measure and increasingly to AI surfaces and
   newsletters. Our plan routes and sequences well but does not attach a measure per
   derivative. Low priority.

## Where ours is stronger

The engine is materially ahead of the generic frameworks on the dimensions that matter for
Maharat.

- English-first with English in parallel, treated as a first-class requirement, not a localize
  later afterthought. Every SEO and content skill states English-first, English in parallel, and
  explicitly forbids a literal translation that ignores how Arabic speakers phrase a search.
  The generic sources are English-default and treat other languages as an add-on.

- Hreflang and RTL are built into the technical audit as named, checked areas with a dedicated
  hreflang map and RTL checks block (`technical-seo/templates/technical-seo-audit.md`), with
  reciprocity and correct language and region codes verified, and mixed AR plus EN plus
  numerals direction tested. Most generic checklists mention hreflang in passing and never
  mention RTL at all.

- No invented claims is a hard, repeated rule, not advice. Every SEO and content skill forbids
  inventing an offer, price, Skill Path title, or instructor name to justify a query, a tag, a
  theme, or a schema field, and forbids implying certificate accreditation anywhere. Schema
  fields are constrained to brief-traceable values. Generic templates happily invent filler.

- Briefs are routed to copywriters, not written in place. The seo-specialist and
  content-marketer brief and route, and copywriter-ar and copywriter-en author. This separation
  keeps a single quality bar on the words and is stronger than the typical brief-and-write-it
  workflow.

- Brand and language QA on public copy is mandatory and ordered. Any customer-facing string
  (title, meta, query phrasing, theme, CTA) runs skill eval, then `arabic-copy-qa` or
  `english-copy-qa`, then `brand-qa-reviewer`, with a fail being a hard stop that returns to the
  author. The handoff contract enforces a qa envelope before any artifact crosses a boundary,
  and publishing or any live site change is gated at the human gate. Generic frameworks have no
  equivalent gate.

- Campaign-agnostic by construction. Targets, offers, and prices are read from the brief,
  never hard-coded, with stop-and-ask when the brief is silent. The generic templates bake in
  examples that teams then ship by accident.

## Recommendations (prioritized, tied to sources)

1. Add generative AI / answer-engine intent as a recognized intent. In
   `keyword-and-intent-research/SKILL.md` and `templates/keyword-and-intent-map.md`, extend the
   intent tag set to include a generative or answer-engine value, and add a one-line note on
   when a cluster is worth pursuing for AI-answer citation rather than rank. Mirror it in
   `on-page-optimization` so a page targeting that intent is structured to be quotable
   (clear definitional answers, FAQ schema). Tie to First Page Sage and SeekLab, which call
   generative AI intent the fastest growing 2026 intent. Highest impact, keep the no-invented
   claims and English-first rules intact.

2. Add concrete Core Web Vitals thresholds to `technical-seo`. In the SKILL speed step and the
   audit template, state LCP at or under 2.5s, INP at or under 200ms, CLS at or under 0.1 at
   the 75th percentile of field data, and note INP has replaced FID. This makes a speed finding
   scoreable as high, medium, or low against a number instead of a judgment. Tie to DebugBear
   and Digital Applied. Low effort, high clarity, Western numerals only.

3. Add an indexation baseline and gap heuristic to `technical-seo`. State the index,follow plus
   self-canonical plus 200 baseline for key templates, that sitemaps carry only canonical 200
   URLs, and that an indexed-versus-canonical gap above roughly 30 percent is investigated. Tie
   to Digital Applied and DebugBear. Add a recommended quarterly audit cadence note. Low effort.

4. Add length and internal-link guidance to `on-page-optimization`, framed Arabic-safe. Suggest
   a title around 60 characters and a meta around 150 to 160 as English guidance, with an
   explicit caveat that Arabic length is judged on rendered width and pixel truncation, not raw
   character count, and that RTL truncation is checked. Suggest roughly 5 to 10 contextual
   internal links per long article with descriptive anchors. Tie to Crawl Compass and the
   on-page 2026 checklists. Keep it as guidance, not a hard cap, so the no-stuffing and
   empowering-tone rules still win.

5. Add a per-item success metric and an optional horizon view to `editorial-calendar`. Add a
   success_metric field to the calendar item (tied back to the strategy-artifact
   success_metric, not invented), and a short note that themes can be layered annual,
   quarterly, monthly, weekly when the window is long. Tie to Backlinko and CMI. Medium effort.

6. Decide consciously on secondary intent and subtopics in `article-brief`. Keep the
   one-target-query, one-intent discipline, which is a genuine strength, but consider adding an
   optional entities or subtopics-to-cover line so the writer covers the topic fully without
   splitting intent. Tie to Content Harmony and Averi brief templates. Low to medium effort.

7. Optional: add a per-derivative measure and an AI-surface format to `content-distribution`.
   Allow a measure per derivative and recognize newsletter and AI-answer surfaces as repurpose
   targets alongside email and organic-social. Tie to CMI and Digital Applied distribution
   guidance. Low priority.

Every recommendation above is an addition or a parameter, none of them touch the four
non-negotiable principles, the no-invented-claims guardrails, the English-first and RTL rules,
or the two gates. All edits, if approved, are Ahmed's call per CLAUDE.md.
