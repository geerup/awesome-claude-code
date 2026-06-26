# seo-package: 2026-06-elda-choucair-marketing

Internal artifact. Not customer-facing. Specs and briefs only. No final copy ships from here.
Copywriters author the final Arabic and English text and run the full gate stack.
No em dashes, no tatweel, Western numerals only. Arabic-first throughout.

---

## Envelope

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: seo-specialist
- stream: search engine optimization
- status: qa-passed
- qa:
  - skill_eval: pass (all sub-skill checks satisfied, see section 6)
  - brand_qa: na (internal spec artifact; customer-facing copy authored downstream and gated)
- brief_refs: objective, pages_in_scope (AR and EN class pages, confirmed URLs), languages (Arabic
  primary, English parallel), geos (GCC, primary Saudi Arabia), offer (Masterclass "Elda Choucair,
  Teaches Marketing" as subscription hook, Chapter 1 free, PDF cheatsheet lead magnet), segments
  (persona-1 data-driven-marketers, persona-2 self-taught-builders, persona-3 skilled-but-stuck-
  executors), angle ("marketing is decision architecture"), instructor (Elda Choucair, CEO Omnicom
  Media Group MENA, naming allowed for this published class)
- open_items: see section 5

---

## 1. Keyword and intent research (keyword_map)

### Methodology note

All Arabic queries are RTL. Priorities are relative (high, medium, low) based on intent value,
relevance to the angle and segments, and feasibility for a specialist platform page. Exact search
volume is NOT stated here. Volume figures require a keyword research tool (Ahrefs or SEMrush with
Arabic corpus). See open_items. All keywords are head (H) or long-tail (LT) as labelled.

---

### Cluster 1: learn-marketing-arabic (AR primary, class page)

```
cluster_name:      learn-marketing-arabic
primary_query_ar:  تعلم التسويق بالعربي   [RTL]   (H)
primary_query_en:  learn marketing in Arabic   (H)
supporting_queries:
  - ar: كورس تسويق بالعربي        intent: commercial      type: H
  - ar: دورة تعليمية تسويق        intent: commercial      type: H
  - ar: تعلم التسويق اون لاين     intent: commercial      type: H
  - en: Arabic marketing course   intent: commercial      type: H
  - en: marketing course in Arabic intent: commercial     type: H
intent:            commercial
priority:          high
maps_to:           https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
notes:             Head terms with meaningful Gulf-market search demand. "بالعربي" phrasing is
                   common in GCC search behaviour vs formal MSA "باللغة العربية". Both variants
                   worth covering in copy and headings. EN variant targets expats and bilingual
                   Gulf professionals.
```

---

### Cluster 2: marketing-decision-architecture (AR primary, class page + content)

```
cluster_name:      marketing-decision-architecture
primary_query_ar:  كيف يتخذ الناس قرارات الشراء   [RTL]   (LT)
primary_query_en:  how people make buying decisions   (LT)
supporting_queries:
  - ar: علم اتخاذ القرار في التسويق         intent: informational    type: LT
  - ar: استراتيجية التسويق وسلوك المستهلك   intent: informational    type: LT
  - ar: التسويق القائم على القرار            intent: informational    type: LT
  - ar: هندسة القرار في التسويق             intent: generative       type: LT
  - en: decision-based marketing strategy     intent: informational    type: LT
  - en: consumer decision making marketing    intent: informational    type: H
  - en: marketing decision architecture       intent: generative       type: LT
intent:            informational, with generative sub-cluster for AI-answer citation
priority:          high
maps_to:           class page (primary) + content brief CB-01
notes:             "هندسة القرار في التسويق" and "marketing decision architecture" are low-volume
                   but topically on-angle and well-suited for AI-answer citation (generative
                   intent). An answer engine queried for "what is decision architecture in
                   marketing" could cite a well-structured Maharat page. Structure the class page
                   and CB-01 article to be self-contained and definition-led for this sub-cluster.
                   The EN phrase "decision-based marketing" has more existing search supply but
                   lower differentiation; the angle-specific phrasing is the defensible position.
```

---

### Cluster 3: online-marketing-courses-gulf (AR primary, class page)

```
cluster_name:      online-marketing-courses-gulf
primary_query_ar:  كورسات تسويق اون لاين السعودية   [RTL]   (LT)
primary_query_en:  online marketing courses Saudi Arabia   (LT)
supporting_queries:
  - ar: دورات تسويق اون لاين الخليج         intent: commercial    type: LT
  - ar: افضل كورس تسويق عبر الانترنت        intent: commercial    type: LT
  - ar: تعلم التسويق الرقمي اون لاين        intent: commercial    type: H
  - ar: منصة تعليمية تسويق السعودية         intent: navigational  type: LT
  - en: online marketing course Gulf          intent: commercial    type: LT
  - en: best Arabic marketing course online   intent: commercial    type: LT
intent:            commercial
priority:          high
maps_to:           https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
notes:             "السعودية" and "الخليج" geo-qualifiers signal high commercial intent and
                   align with the primary Saudi Arabia market. These are the queries where
                   the class page competes most directly against generic course platforms (Udemy,
                   Coursera, Jeel). The differentiator in titles and meta should be Elda's
                   seniority and the decision-first angle, not a feature list. Do not invent
                   duration, lesson count, or certification status.
```

---

### Cluster 4: elda-choucair-navigational (AR and EN, class page)

```
cluster_name:      elda-choucair-navigational
primary_query_ar:  إلدا شقير   [RTL]   (H)
primary_query_en:  Elda Choucair   (H)
supporting_queries:
  - ar: إلدا شقير تسويق                  intent: navigational    type: LT
  - ar: إلدا شقير أومنيكوم               intent: navigational    type: LT
  - ar: إلدا شقير محاضرة                 intent: informational   type: LT
  - en: Elda Choucair marketing          intent: navigational    type: LT
  - en: Elda Choucair Omnicom MENA       intent: navigational    type: LT
  - en: Elda Choucair Maharat class      intent: navigational    type: LT
  - en: Elda Choucair teaches marketing  intent: navigational    type: LT
intent:            navigational
priority:          high
maps_to:           https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
                   and https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
notes:             Naming confirmed for this published class. These navigational queries are
                   won by having the class page correctly titled and indexed so Maharat ranks for
                   her name plus marketing signals. The "Elda Choucair, Teaches Marketing" title
                   and the AR "إلدا شقير، تعلّم التسويق" are already on-page; confirming correct
                   indexation and schema is the key technical action.
```

---

### Cluster 5: marketing-strategy-fundamentals-arabic (AR primary, content)

```
cluster_name:      marketing-strategy-fundamentals-arabic
primary_query_ar:  مبادئ استراتيجية التسويق   [RTL]   (H)
primary_query_en:  marketing strategy fundamentals   (H)
supporting_queries:
  - ar: كيف اعمل استراتيجية تسويقية       intent: informational   type: LT
  - ar: اساسيات التسويق للمبتدئين         intent: informational   type: LT
  - ar: مفاهيم التسويق الحديث             intent: informational   type: LT
  - ar: الفرق بين التسويق والمبيعات       intent: informational   type: H
  - en: how to build a marketing strategy   intent: informational   type: LT
  - en: marketing fundamentals for beginners intent: informational  type: H
  - en: marketing vs sales difference       intent: informational   type: H
intent:            informational
priority:          medium
maps_to:           content brief CB-02
notes:             High informational intent and a natural entry into the class for persona-2
                   self-taught builders ("shipped but met silence"). An article or guide page
                   targeting this cluster can funnel to the class page via internal linking.
                   "اساسيات التسويق للمبتدئين" has broad demand but high competition; the
                   Maharat angle (decision-first, senior Arab voice) is the differentiation.
```

---

### Cluster 6: branding-and-positioning-arabic (AR primary, content)

```
cluster_name:      branding-and-positioning-arabic
primary_query_ar:  كيف ابني علامة تجارية قوية   [RTL]   (LT)
primary_query_en:  how to build a strong brand   (LT)
supporting_queries:
  - ar: استراتيجية بناء العلامة التجارية   intent: informational   type: LT
  - ar: تمييز العلامة التجارية             intent: informational   type: LT
  - ar: كيف اجعل الناس يهتمون بمنتجي      intent: informational   type: LT
  - ar: قصة العلامة التجارية               intent: informational   type: H
  - en: brand positioning strategy          intent: informational   type: LT
  - en: how to make people care about your product intent: informational type: LT
  - en: brand storytelling for founders     intent: informational   type: LT
intent:            informational
priority:          medium
maps_to:           content brief CB-03
notes:             "كيف اجعل الناس يهتمون بمنتجي" maps directly to persona-2 self-taught
                   builders' pain ("shipped, met silence"). The "make people care" hook from
                   the strategy angle threads through the content here and to the class page.
                   "brand storytelling for founders" is a strong EN signal for the B2B-adjacent
                   professional cut.
```

---

### Cluster 7: marketing-data-and-conversion (AR primary, content)

```
cluster_name:      marketing-data-and-conversion
primary_query_ar:  لماذا لا تتحول البيانات الى مبيعات   [RTL]   (LT)
primary_query_en:  why data-driven marketing fails to convert   (LT)
supporting_queries:
  - ar: تحسين معدل التحويل في التسويق      intent: informational   type: LT
  - ar: البيانات التسويقية واتخاذ القرار   intent: informational   type: LT
  - ar: الفانل التسويقي لا يعمل            intent: informational   type: LT
  - ar: تحسين القمع التسويقي               intent: informational   type: LT
  - en: data driven marketing not converting  intent: informational  type: LT
  - en: marketing funnel not converting       intent: informational  type: H
  - en: beyond data marketing judgment        intent: generative     type: LT
intent:            informational, with generative sub-cluster
priority:          medium
maps_to:           content brief CB-04
notes:             Maps to persona-1 data-driven marketers' exact pain ("clean funnel, no
                   conversion"). "لماذا لا تتحول البيانات الى مبيعات" is long-tail with direct
                   commercial proximity; a well-structured Arabic article targeting this is also
                   positioned to be cited by AI answer engines for the "why does my marketing
                   funnel not work" type of query (generative intent).
```

---

### Cluster 8: self-development-platform-arabic (AR primary, navigational/commercial)

```
cluster_name:      self-development-platform-arabic
primary_query_ar:  منصة تطوير الذات بالعربي   [RTL]   (H)
primary_query_en:  Arabic self-development platform   (H)
supporting_queries:
  - ar: افضل تطبيق تعلم مهارات عربي       intent: commercial    type: H
  - ar: منصة مهارات عربية               intent: navigational   type: H
  - ar: تعلم مهارات جديدة اون لاين        intent: commercial    type: H
  - en: Maharat platform                   intent: navigational  type: H
  - en: learn skills in Arabic online       intent: commercial   type: H
intent:            commercial
priority:          medium
maps_to:           https://www.maharat.com/ (home, not the class page)
notes:             This cluster serves Maharat brand visibility broadly, not just this class.
                   Included because SEO for this campaign feeds the broader subscription funnel.
                   The class page should link back to the home or category (/business/) for
                   crawlability. The "منصة مهارات عربية" query is a direct navigational signal
                   worth owning correctly.
```

---

### Summary: keyword priority by segment

| Cluster | Priority | Personas served | Intent type |
|---|---|---|---|
| learn-marketing-arabic | high | all 3 | commercial |
| marketing-decision-architecture | high | all 3 | informational + generative |
| online-marketing-courses-gulf | high | all 3 | commercial |
| elda-choucair-navigational | high | all 3 (aware) | navigational |
| marketing-strategy-fundamentals-arabic | medium | persona-2, persona-3 | informational |
| branding-and-positioning-arabic | medium | persona-2 | informational |
| marketing-data-and-conversion | medium | persona-1 | informational + generative |
| self-development-platform-arabic | medium | all 3 | commercial |

Note: no table cell contains an invented offer, price, Skill Path title, or lesson count.

---

## 2. On-page optimization specs (on_page_specs[])

Two pages in scope: the Arabic class page and the English class page. One intent per page. Specs
only. The copywriters (copywriter-ar, copywriter-en) author all final customer-facing copy from
these specs and run the full gate stack.

For clarity, COPY-SLOT is used to mark where the copywriters fill in the final text. The
bracketed guidance after each slot is a structural brief, not final copy.

---

### Page spec 1: Arabic class page

```
url:              https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
cluster:          learn-marketing-arabic (primary) + elda-choucair-navigational (secondary signal)
primary_query_ar: تعلم التسويق بالعربي   [RTL]
primary_query_en: n/a for this page (the EN page is the hreflang alternate)
intent:           commercial
language:         Arabic, RTL

title_ar:         COPY-SLOT [Lead with "تعلم التسويق" or a close variant; include "إلدا شقير"
                  (confirmed naming). Within 55-60 characters. No price, plan, lesson count, or
                  accreditation. Tone: confident, empowering. No tatweel, Western numerals only.
                  Example structure (not final copy): "تعلم التسويق مع إلدا شقير, مهارات تبقى
                  معك", but copywriter-ar should produce the final wording to brand voice.]

meta_ar:          COPY-SLOT [Plain, empowering, under 150 characters. Echo the "20 years" and
                  "decision architecture" angle. No mention of price, lesson count, plan, or
                  accreditation. No invented claims. Should drive click for someone searching
                  "كورس تسويق بالعربي" or "تعلم التسويق اون لاين". Example shape: surface who
                  she is (CEO, Omnicom MENA), what the class gives (frameworks, way of thinking),
                  no outcomes promise. Copywriter-ar finalises against brand-voice.md.]

headings:
  h1:             COPY-SLOT [One H1, matches "تعلم التسويق" intent. Echo the class title
                  "إلدا شقير، تعلّم التسويق" closely or exactly, since that is the confirmed
                  public title and the navigational anchor. RTL correct.]
  h2:
    - COPY-SLOT [Section: who Elda is and her credentials. Source: CEO Omnicom MENA, 20 years
                 experience. No invented claims. No "100 brands", no Cannes, no spend figures.]
    - COPY-SLOT [Section: what the class addresses thematically, the "decision architecture"
                 frame. Thematic only, no lesson list. No invented module titles.]
    - COPY-SLOT [Section: the free first chapter offer (confirmed). CTA direction toward
                 "ابدأ المشاهدة" or the Start Watching URL.]
    - COPY-SLOT [Section: the broader Maharat platform context, to support internal links.]
  h3:
    - COPY-SLOT [Sub-section under credentials: her industry positioning in the Arab market.]
    - COPY-SLOT [Sub-section under class content: what kind of thinking the class builds,
                 not a list of lessons.]

internal_links:
  - anchor_text:  COPY-SLOT ["صفحة مهارات التسويق" or similar]
    target_url:   https://www.maharat.com/ar/class/business/
    why:          Category page, crawlability and topical breadcrumb

  - anchor_text:  COPY-SLOT ["ابدأ المشاهدة مجانا" or similar, for Chapter 1 free]
    target_url:   https://member.maharat.com/ar/class/elda-choucair-teaches-marketing
    why:          Primary conversion CTA, confirmed URL

  - anchor_text:  COPY-SLOT [Maharat homepage brand anchor]
    target_url:   https://www.maharat.com/ar/
    why:          Breadcrumb / site hierarchy

  - anchor_text:  COPY-SLOT [Link to a planned content article, once published: e.g. an article
                  on "هندسة القرار في التسويق" or "مبادئ استراتيجية التسويق" from CB-01 or CB-02]
    target_url:   [to be assigned when content articles are published]
    why:          Topical authority link; content article links back to class page

schema:
  type:           Course
  fields:
    name_ar:      "إلدا شقير، تعلّم التسويق"   [confirmed page title]
    name_en:      "Elda Choucair, Teaches Marketing"   [confirmed page title]
    description:  COPY-SLOT [brief from the confirmed tagline: "تعلّم التسويق من أبرز القيادات
                  في العالم العربي، بخبرة في بناء علامات تجارية مؤثرة وصياغة استراتيجيات شكّلت
                  قطاعات كاملة." Copywriter finalises to <= 160 chars]
    provider:
      type:       Organization
      name:       "Maharat"
      url:        "https://www.maharat.com"
    instructor:
      type:       Person
      name_ar:    "إلدا شقير"
      name_en:    "Elda Choucair"
      jobTitle_ar: "الرئيسة التنفيذية، أومنيكوم ميديا جروب، الشرق الأوسط وشمال أفريقيا"
      jobTitle_en: "CEO, Omnicom Media Group MENA"
    inLanguage:   ar
    url:          "https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing"

  Note on schema constraints: do NOT add numberOfLessons, duration, coursePrerequisites,
  price, offers, or any field not supported by a confirmed brief value. No
  educationalCredentialAwarded claim. No accreditation type. Completion certificate exists
  but is not accredited; do not include in schema.

notes:
  - One clear commercial intent. The navigational Elda queries are served by correct titling
    and indexation, not a separate intent split.
  - Price and plan are ASSUMPTION fields in the brief. No offer price in title, meta, or schema
    until confirmed.
  - Tatweel check: the confirmed AR class title "إلدا شقير، تعلّم التسويق" contains a shadda
    (not tatweel) in "تعلّم" which is correct Arabic grammar, not tatweel (U+0640). This is
    safe. Confirm in build that no tatweel characters are introduced in any on-page text.
```

---

### Page spec 2: English class page

```
url:              https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
cluster:          online-marketing-courses-gulf (primary) + elda-choucair-navigational
primary_query_ar: n/a for this page (the AR page is the hreflang alternate)
primary_query_en: online marketing courses Saudi Arabia / learn marketing from Arab expert
intent:           commercial
language:         English, LTR

title_en:         COPY-SLOT [Lead with "Elda Choucair Teaches Marketing" (confirmed public title)
                  as the anchor. Within 55-60 characters. No price, no lesson count, no
                  accreditation. Confident and empowering. Example structure (not final copy):
                  "Elda Choucair Teaches Marketing, Maharat" using the confirmed title + brand.]

meta_en:          COPY-SLOT [Under 150 characters. Surface: who she is (CEO, Omnicom MENA),
                  the angle (think like a decision architect, not a tactics follower), first
                  chapter free. No lesson count, no price, no accreditation. Plain and
                  empowering. Copywriter-en finalises against brand-voice.md.]

headings:
  h1:             COPY-SLOT [Echo or match the confirmed EN class title "Elda Choucair,
                  Teaches Marketing". One H1.]
  h2:
    - COPY-SLOT [Section: Elda's credentials and seniority in Arab marketing. CEO, Omnicom
                 MENA, decades of experience. No held-back claims. No invented claims.]
    - COPY-SLOT [Section: the "decision architecture" angle, what the class teaches
                 thematically. No lesson list.]
    - COPY-SLOT [Section: how to start, Chapter 1 free, CTA toward Start Watching URL.]
    - COPY-SLOT [Section: Maharat platform context, internal link anchor.]
  h3:
    - COPY-SLOT [Credentials sub-section: her regional track record, confirmed claims only.]
    - COPY-SLOT [Class content sub-section: the thinking it builds, thematic not tactical.]

internal_links:
  - anchor_text:  COPY-SLOT ["Business and Marketing classes on Maharat" or similar]
    target_url:   https://www.maharat.com/en/class/business/
    why:          Category page, crawlability and topical breadcrumb

  - anchor_text:  COPY-SLOT ["Start watching for free" or similar, Chapter 1 free CTA]
    target_url:   https://member.maharat.com/en/class/elda-choucair-teaches-marketing
    why:          Primary conversion CTA, confirmed URL

  - anchor_text:  COPY-SLOT [Maharat homepage brand anchor]
    target_url:   https://www.maharat.com/en/
    why:          Breadcrumb / site hierarchy

  - anchor_text:  COPY-SLOT [Link to a published EN content article, once available, e.g. on
                  "decision architecture in marketing" or "marketing strategy fundamentals"
                  from CB-01 or CB-02 EN versions]
    target_url:   [to be assigned when content articles are published]
    why:          Topical authority link; article links back to class page

schema:
  type:           Course
  fields:
    name_en:      "Elda Choucair, Teaches Marketing"   [confirmed page title]
    name_ar:      "إلدا شقير، تعلّم التسويق"   [confirmed page title]
    description:  COPY-SLOT [from confirmed EN tagline: "Learn marketing from one of the Arab
                  world's most respected leaders, with decades of experience shaping iconic brands
                  and industry-defining strategies." Copywriter finalises]
    provider:
      type:       Organization
      name:       "Maharat"
      url:        "https://www.maharat.com"
    instructor:
      type:       Person
      name_en:    "Elda Choucair"
      name_ar:    "إلدا شقير"
      jobTitle_en: "CEO, Omnicom Media Group MENA"
    inLanguage:   en
    url:          "https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing"

  Note: same schema constraints as the AR page. No numberOfLessons, duration, price, offers,
  or educationalCredentialAwarded. Certificates are not accredited.

notes:
  - The EN page is not a translation of the AR page; it is a parallel page in English serving
    the bilingual Gulf professional cut and international searchers. The tone and angle match
    but the page is written by copywriter-en from this spec independently.
  - Price and plan are ASSUMPTION fields. Do not add to schema or copy until confirmed.
```

---

## 3. Technical SEO checklist (technical_findings[])

### Access and verification note

No Search Console access, crawl tool access, or live CrUX/PageSpeed data is available in this
run. All findings below are specced from the known URL structure, page architecture facts in the
brief and masterclass-pages.md, standard Arabic-first bilingual site patterns, and the
observable URL scheme. All speed and indexation findings are flagged as "to verify" pending tool
access. No finding is assumed verified without data.

---

### Findings

```
- area:          hreflang
  issue:         Hreflang implementation for AR and EN class page alternates is unverified.
                 The URL structure (maharat.com/ar/... and maharat.com/en/...) is the correct
                 pattern for language subdirectory hreflang. Whether the <link rel="alternate"
                 hreflang="ar"> and <link rel="alternate" hreflang="en"> tags are actually
                 present in the <head> of both pages, and whether they are reciprocal, is not
                 confirmed without a crawl or live page inspection.
  severity:      high
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    - https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  fix:           In the page template, confirm that both pages carry:
                 AR page head: <link rel="alternate" hreflang="ar" href="https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing">
                 AR page head: <link rel="alternate" hreflang="en" href="https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing">
                 EN page head: <link rel="alternate" hreflang="en" href="https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing">
                 EN page head: <link rel="alternate" hreflang="ar" href="https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing">
                 Also add x-default pointing to the EN page (or the AR page if Arabic is the
                 primary commercial market, which it is here; confirm with conversion-engineer).
                 Reciprocity is required: both pages must declare both alternates.

- area:          hreflang
  issue:         Region code handling for Saudi Arabia is unspecified. For the primary Saudi
                 market, "ar-SA" is a valid and recommended hreflang refinement alongside "ar"
                 (which covers all Arabic speakers). Using only "ar" is the safe default and
                 serves the whole Arabic-speaking market. Using "ar-SA" in addition can sharpen
                 targeting for Saudi searchers but requires the alternate URL set to match
                 exactly.
  severity:      medium
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  fix:           Decision for conversion-engineer: either use "ar" only (serves all Arabic, simpler)
                 or add an "ar-SA" alternate pointing to the same AR URL if Saudi-specific
                 targeting is the priority. Do not mix "ar" and "ar-SA" pointing to different pages.
                 Recommend: use "ar" as the primary alternate, and add "ar-SA" only if a Saudi-
                 specific page variant exists or is planned. Confirm at the human gate.

- area:          rtl
  issue:         RTL rendering correctness of the Arabic class page is unverified without a
                 live render check. The URL scheme and site history suggest RTL is implemented,
                 but specific risk areas exist: (a) the "إلدا شقير، تعلّم التسويق" title with
                 a comma, (b) any mixed AR + EN inline content (her EN job title "CEO, Omnicom
                 Media Group MENA" appearing inline within Arabic text), and (c) any numerals
                 that may appear in page UI (ratings, chapter counts, etc).
  severity:      high
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  fix:           conversion-engineer to run a live render check on the AR page confirming:
                 (1) dir="rtl" set at <html> or <body> level for the AR page.
                 (2) Mixed AR + EN inline text uses Unicode bidi isolation where needed (e.g.
                 <span dir="ltr"> or the bidi-isolation CSS for EN inline segments).
                 (3) All displayed numerals are Western (0 to 9), not Eastern Arabic digits.
                 (4) No tatweel characters introduced in any CMS or rendering pipeline.

- area:          rtl
  issue:         The Arabic title tag and meta description must be rendered RTL-correctly in
                 the browser tab and in search result snippets. SERP rendering of Arabic titles
                 depends on the browser and Google's snippet engine interpreting the text
                 direction correctly. A title tag that starts with an LTR character (e.g. a
                 Roman letter or Western numeral) may cause direction flip in the snippet.
  severity:      medium
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  fix:           Ensure the AR title tag begins with an Arabic character, not a Latin or
                 numeral character. The "إلدا شقير" opening character is Arabic and correct.
                 If the title spec produces any variant starting with a Latin character,
                 reorder to put the Arabic word first.

- area:          crawlability
  issue:         Robots.txt rules and crawl access for the class page templates are unverified.
                 If the /ar/class/ or /en/class/ paths are disallowed in robots.txt (e.g. to
                 block the member subdomain or logged-in states) the class pages may not be
                 crawlable.
  severity:      high
  affected_urls:
    - https://www.maharat.com/ar/class/business/
    - https://www.maharat.com/en/class/business/
  fix:           Inspect https://www.maharat.com/robots.txt. Confirm:
                 (1) /ar/class/ and /en/class/ paths are not disallowed.
                 (2) The member subdomain (member.maharat.com) is handled separately; the
                 Start Watching URLs are behind a login and should be disallowed or noindexed
                 to avoid indexing gated content. The public class pages (www.maharat.com/ar/
                 and /en/) must be fully crawlable.

- area:          crawlability
  issue:         Internal link depth to the class pages is unknown. If the AR and EN class
                 pages are not linked from at least the category page (/ar/class/business/ and
                 /en/class/business/) and ideally from a hub or homepage section, they may
                 receive low crawl priority and slower indexation.
  severity:      medium
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    - https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  fix:           Confirm that the category pages /ar/class/business/ and /en/class/business/
                 link to the Elda class page. When content articles are published (from content
                 briefs CB-01 to CB-04), each should include a contextual internal link back to
                 the class page. See on_page_specs internal_links above.

- area:          indexation
  issue:         Indexation status of both class pages (AR and EN) is unverified without Search
                 Console access. The pages were published Feb 2026 (per the brief background)
                 and should be indexed by now, but canonical and index directives are unconfirmed.
  severity:      high
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    - https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  fix:           Run a "site:" check or Search Console coverage report to confirm:
                 (1) Both pages return a 200 status.
                 (2) Both pages carry <meta name="robots" content="index,follow"> or have no
                 blocking robots meta.
                 (3) Both pages carry a self-referencing canonical tag.
                 (4) Neither page is marked noindex accidentally.
                 Resolve in Search Console. See open_items for the access dependency.

- area:          sitemaps
  issue:         Whether the AR and EN class page URLs are included in the XML sitemap is
                 unverified. A missing sitemap entry delays discovery and indexation, especially
                 for newly-published pages.
  severity:      medium
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    - https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  fix:           Inspect the sitemap (likely https://www.maharat.com/sitemap.xml or a
                 localized variant). Confirm:
                 (1) Both the AR and EN class page URLs are listed.
                 (2) The sitemap carries only canonical 200 URLs (no redirect targets, noindex,
                 or non-canonical entries).
                 (3) The sitemap is submitted in Google Search Console.
                 If the pages are missing, add them and resubmit. The member.maharat.com
                 Start Watching URLs (gated content) should NOT be in the sitemap.

- area:          speed
  issue:         Core Web Vitals field data for the class pages is unverified without PageSpeed
                 Insights or CrUX access. The pages serve a high-quality cover image (WebP
                 format, CloudFront CDN, confirmed), which is a good base, but LCP, INP, and
                 CLS scores for the AR page template specifically are unknown.
  severity:      medium
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    - https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  fix:           Run PageSpeed Insights (mobile and desktop) on both class page URLs.
                 Score against:
                   LCP: at or under 2.5s at the 75th percentile (field)
                   INP: at or under 200ms at the 75th percentile (field) [INP has replaced FID]
                   CLS: at or under 0.1 at the 75th percentile (field)
                 The CloudFront-served WebP cover image is a good signal for LCP. Likely risk:
                 CLS shifts from any dynamic content loading (user state, pricing panels, etc).
                 The RTL template may have layout-shift risk distinct from the LTR EN template.
                 Confirm and report measured values. Flag to conversion-engineer for resolution.

- area:          canonical
  issue:         Canonical tag implementation is unverified. The AR and EN pages must each
                 carry a self-referencing canonical, and they must NOT cross-canonicalize to
                 each other (the AR page must not canonical to the EN page or vice versa).
  severity:      high
  affected_urls:
    - https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    - https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  fix:           Confirm in source:
                 AR page canonical: <link rel="canonical" href="https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing">
                 EN page canonical: <link rel="canonical" href="https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing">
                 Each page is its own canonical. They are linked via hreflang, not via canonical.
```

---

### Hreflang map (priority pages)

```
- page:          https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  alternates:
    - lang: ar   href: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    - lang: en   href: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
    - lang: x-default   href: [confirm with conversion-engineer: AR for GCC-primary, EN for
                                international default. Recommend AR as primary default for this
                                campaign's Saudi-first market, but flag for Ahmed to confirm.]
  reciprocal:    to verify (flagged, see finding above)
  notes:         Region code "ar-SA" is an optional refinement. Recommend resolving this at
                 the human gate. The base "ar" implementation is correct and sufficient.

- page:          https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  alternates:
    - lang: en   href: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
    - lang: ar   href: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    - lang: x-default   href: [same as above, confirm]
  reciprocal:    to verify
  notes:         Confirm that the EN page does not accidentally carry hreflang="en-US" or
                 "en-GB" without the generic "en" tag also present.
```

---

### RTL checks (priority pages)

```
- page:          https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  direction:     to verify (expected correct given site architecture, but unconfirmed)
  numerals:      to verify (Western numerals required in all UI)
  mixed_content: to verify (risk: inline EN job title "CEO, Omnicom Media Group MENA" in AR
                 text; and any rating or chapter-count numerals)
  notes:         See finding under rtl area above. conversion-engineer to run live render check.

- page:          https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  direction:     LTR, expected correct
  numerals:      Western, expected correct
  mixed_content: expected safe (EN page is LTR, no AR content injection expected)
  notes:         Confirm that the EN page does not render any AR text in an LTR container
                 without bidi isolation, e.g. if the instructor Arabic name appears on the EN page.
```

---

### Indexation baseline and gap

```
baseline:        index,follow + self-canonical + 200 status for both class page URLs
sitemap_rule:    sitemaps carry only canonical 200 URLs; Start Watching member.maharat.com
                 URLs are gated and must not appear in the public sitemap
indexed_count:   unknown (no Search Console access)
canonical_count: 2 (the two class page URLs, AR and EN)
gap:             unknown pending verification
cadence:         quarterly technical audit recommended after initial fix confirmation
```

---

## 4. Content briefs for content-marketer (content_briefs[])

Four briefs follow. Arabic-first. The content-marketer routes Arabic article authorship to
copywriter-ar and English to copywriter-en. These are SEO-informed briefs. All final text is
authored by the copywriters and runs the full gate stack (arabic-copy-qa or english-copy-qa,
then brand-qa-reviewer) before publishing.

No final copy is written here. No lesson list, price, plan, or held-back claim appears in any brief.

---

### CB-01: Decision architecture as a marketing framework (AR primary)

```
brief_id:         CB-01
campaign_id:      2026-06-elda-choucair-marketing
cluster:          marketing-decision-architecture
primary_query_ar: كيف يتخذ الناس قرارات الشراء   [RTL]
primary_query_en: how people make buying decisions
intent:           informational + generative (AI-answer citation priority)
priority:         high
segments_served:  persona-1-data-driven-marketers (primary), all 3 (secondary)
angle_tie:        "marketing is decision architecture": the article introduces the idea that
                  marketing's real job is to shape the conditions for a decision in your favour,
                  not to optimise for clicks or impressions. This is the class's central
                  intellectual frame.

suggested_structure:
  - Lead with a clear, self-contained definition of decision architecture in marketing.
    This section must be structured for AI-answer citation: a 2 to 3 sentence definition
    that an answer engine can quote accurately. No vague language, no hype.
  - H2: what decision architecture means in practice (concrete examples from published,
    factual marketing thinking. No invented case studies or invented brand examples.)
  - H2: why marketers focused on data and funnels miss the decision layer (connects to
    persona-1 pain: "clean funnel, no conversion")
  - H2: the questions that change how you see a campaign (connects to "better questions
    beat more data" angle)
  - H2: how to develop sharper marketing judgement (empowering framing, routes toward the
    class page as a structured learning resource)
  - FAQ section (3 to 5 questions): use question-led headings for generative intent.
    Example question shapes (not final copy): "ما هي هندسة القرار في التسويق?",
    "كيف يتخذ المستهلك قرار الشراء?", "لماذا تفشل الحملات التسويقية القائمة على البيانات؟"
    Copywriter-ar writes the questions and answers.

internal_link_targets:
  - class page AR: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    (contextual anchor within the body, e.g. when naming Elda or the class)
  - class page EN: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
    (in the EN version, if published)
  - CB-02 article (when published): for the "marketing strategy fundamentals" connection

content_type:     long-form article, 800 to 1200 words, AR primary, EN parallel version
languages:        Arabic (copywriter-ar) primary; English (copywriter-en) parallel
tone:             Thmanyah-adjacent: clear, modern, intelligent, not academic. Empowering.
guardrails:       No invented lesson list or module titles. No Cannes reference, no spend
                  figures, no "100 brands" claim. Elda may be named as the instructor with
                  her confirmed credentials (CEO Omnicom MENA, decades of experience) when
                  citing the class as the learning resource. No accreditation claim.
                  No price or plan in the article.
```

---

### CB-02: Marketing strategy fundamentals for Arabic-speaking professionals (AR primary)

```
brief_id:         CB-02
campaign_id:      2026-06-elda-choucair-marketing
cluster:          marketing-strategy-fundamentals-arabic
primary_query_ar: مبادئ استراتيجية التسويق   [RTL]
primary_query_en: marketing strategy fundamentals
intent:           informational
priority:         medium
segments_served:  persona-2-self-taught-builders (primary), persona-3-skilled-but-stuck-executors
angle_tie:        Strategy is the layer above tools. This article addresses the gap between
                  "I know the tools" and "I know where to point them." Connects to persona-3
                  ("strategy over features") and persona-2 ("make people care").

suggested_structure:
  - Intro: the difference between executing tactics and building strategy. Empowering, not
    a lecture. The reader is capable; the article adds the frame they are missing.
  - H2: what a marketing strategy actually decides (vs what an execution plan decides)
  - H2: the 3 questions a strong marketing strategy must answer (do not invent specific
    proprietary frameworks; keep to widely established strategic thinking)
  - H2: why self-taught builders and skilled executors hit the same wall (connects to both
    persona-2 and persona-3 without naming the personas or being patronising)
  - H2: how to move from tactics to strategic thinking (empowering arc, routes to the class)
  - Brief closing link to the class page, framed as a structured way to build this thinking.

internal_link_targets:
  - class page AR: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  - CB-01 article (once published): for the "decision architecture" connection
  - CB-03 article (once published): for the "branding and positioning" connection

content_type:     article, 600 to 900 words, AR primary, EN parallel version
languages:        Arabic (copywriter-ar) primary; English (copywriter-en) parallel
tone:             Plain, confident, intelligent. Empowering, never deficit-framed.
guardrails:       Same as CB-01. No invented examples, no lesson list, no accreditation,
                  no price or plan. Do not overstate Elda's claims beyond confirmed credentials.
```

---

### CB-03: How to build a brand people care about (AR primary)

```
brief_id:         CB-03
campaign_id:      2026-06-elda-choucair-marketing
cluster:          branding-and-positioning-arabic
primary_query_ar: كيف ابني علامة تجارية قوية   [RTL]
primary_query_en: how to build a strong brand
intent:           informational
priority:         medium
segments_served:  persona-2-self-taught-builders (primary)
angle_tie:        The "make people care" hook for persona-2. A shipped product that meets
                  silence is a positioning and story problem, not a quality problem. This
                  article reframes the problem empoweringly and routes toward the class.

suggested_structure:
  - Intro: you built something good. The market silence is not a verdict on the quality.
    It is a question about the story. (Empowering framing, not deficit.)
  - H2: what positioning actually is (a decision about whose life to be part of, not a tagline)
  - H2: why branding fails when it starts from the product, not the decision
  - H2: the role of brand story in a decision (not storytelling-as-narrative, but how
    a story shapes the conditions for a choice)
  - H2: how to start building a brand that people choose (practical, non-prescriptive framing;
    routes to the class as a structured way to learn the thinking)
  - FAQ section (2 to 3 questions for generative intent): e.g. "ما الفرق بين التسويق
    والعلامة التجارية?", "كيف اجعل الناس يهتمون بمنتجي?"

internal_link_targets:
  - class page AR: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  - CB-02 article (once published): for the "strategy fundamentals" connection

content_type:     article, 700 to 1000 words, AR primary, EN parallel version
languages:        Arabic (copywriter-ar) primary; English (copywriter-en) parallel
tone:             Empowering, with the "make people care" urgency. Clear, not academic.
guardrails:       Same standing constraints. No invented brand case studies or invented
                  regional examples without verifiable public facts. No accreditation,
                  no price, no lesson list.
```

---

### CB-04: Why your marketing funnel is clean but no one buys (AR primary)

```
brief_id:         CB-04
campaign_id:      2026-06-elda-choucair-marketing
cluster:          marketing-data-and-conversion
primary_query_ar: لماذا لا تتحول البيانات الى مبيعات   [RTL]
primary_query_en: why data-driven marketing fails to convert
intent:           informational + generative (AI-answer citation priority for the "funnel
                  not converting" query cluster)
priority:         medium
segments_served:  persona-1-data-driven-marketers (primary)
angle_tie:        "Better questions beat more data." The article identifies the decision gap
                  that lives between a clean funnel and an actual purchase. Pain-first entry,
                  empowering resolution.

suggested_structure:
  - Lead with a clear, self-contained answer: why a technically correct funnel can produce
    zero conversions. Structured for AI-answer citation.
  - H2: the assumption most data-driven marketers make about why people do not buy
  - H2: what is actually happening at the decision point (the decision layer below the data)
  - H2: the questions that change how you read your funnel data
  - H2: how to build the judgment that sits above the dashboard (empowering arc, routes
    toward the class as the structured resource for this thinking)
  - FAQ section: question-led H3s for generative intent. e.g. "لماذا لا يعمل الفانل
    التسويقي؟", "ما الذي يجعل المستهلك يشتري في نهاية المطاف؟"

internal_link_targets:
  - class page AR: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  - CB-01 article (once published): for the "decision architecture" connection

content_type:     article, 700 to 1000 words, AR primary, EN parallel version
languages:        Arabic (copywriter-ar) primary; English (copywriter-en) parallel
tone:             Pain-aware but empowering. Speak to someone who is capable and stuck, not
                  to someone who has failed. The problem is the frame, not the person.
guardrails:       Same standing constraints. No held-back claims, no accreditation, no price.
                  Do not promise that the class will fix conversion rates. Promise clearer
                  thinking and sharper judgment.
```

---

## 5. Open items

```
1. Search Console access not granted. Indexation count, query data, coverage reports, and
   hreflang validation are all blocked without it. Proceed with the plan from available data;
   block the live verification steps; surface at the human gate for Ahmed to grant access.

2. Keyword volume data requires a keyword research tool with Arabic corpus (Ahrefs or SEMrush).
   Priority rankings in this package are intent-based, not volume-based. Exact search volumes
   are marked "to verify" throughout. The tool has not been approved; this is an open item for
   Ahmed. Do not adopt without build-vs-buy review and approval per CLAUDE.md principle 3.

3. Crawl tool not approved. Robots.txt, internal link depth, redirect chains, and live hreflang
   tags are unverified without an approved crawl tool (e.g. Screaming Frog or similar). Firecrawl
   MCP is documented in the agent's tools allowlist but gated. Flag at the human gate.

4. PageSpeed Insights and CrUX data not retrieved. Core Web Vitals scores for both class pages
   are marked "to verify." Conversion-engineer to run PageSpeed Insights directly on both URLs
   and report results against the thresholds: LCP 2.5s, INP 200ms, CLS 0.1 at the 75th
   percentile (field data, mobile).

5. x-default hreflang target: Arabic (primary Saudi market) vs English (international default).
   Confirm with conversion-engineer and Ahmed at the human gate before implementation.

6. "ar-SA" hreflang refinement: whether to add a Saudi-specific alternate alongside the generic
   "ar" alternate. Confirm at the human gate. Recommend "ar" only unless a Saudi-specific URL
   variant exists or is planned.

7. Sitemap inspection: whether both class page URLs (AR and EN) are currently in the XML sitemap
   is unverified. Conversion-engineer to inspect and add if missing, then resubmit in Search
   Console.

8. Internal link depth to class pages: whether the category pages /ar/class/business/ and
   /en/class/business/ currently link to the Elda class page is unverified. Conversion-engineer
   to confirm and add if missing.

9. Content article publishing schedule: the internal link plan in on_page_specs assumes future
   content articles from CB-01 to CB-04. Those target_urls are marked [to be assigned when
   content articles are published]. The on-page specs must be updated once URLs are confirmed.

10. Price, plan, and promotion fields in the brief are marked ASSUMPTION. No price, plan name,
    or promotion appears in any title, meta, schema, or content brief. These fields must be
    confirmed before copywriters can write any pricing section or CTA that names a cost or term.

11. Formal catalog status confirmation for Elda: still pending per the brief. The published class
    page is sufficient to name her for this class; this is carried forward from strategy-artifact
    as an open item for the human gate.
```

---

## 6. Skill eval self-check

Checks run against the skill eval criteria for seo, keyword-and-intent-research, on-page-
optimization, and technical-seo:

- keyword map leads Arabic-first and traces to segments and angle: pass
- all queries tagged with one intent including generative where applicable: pass
- clusters have primary query and priority: pass
- RTL noted for Arabic queries: pass
- no invented offer, price, Skill Path title, instructor name: pass (Elda named, confirmed)
- no accreditation implication: pass
- one clear intent per page in on_page_specs: pass
- title and meta specs in AR and EN, Arabic-first, RTL noted: pass
- schema fields trace to brief only, no invented claims: pass
- no price or lesson count in schema: pass
- no schema educationalCredentialAwarded or accreditation: pass
- technical findings cover crawlability, speed, indexation, sitemaps, hreflang, RTL, canonical: pass
- Core Web Vitals thresholds stated (LCP 2.5s, INP 200ms, CLS 0.1, INP replaces FID): pass
- indexation baseline stated, sitemap rule stated: pass
- hreflang AR and EN reciprocity specified: pass
- each finding has severity and concrete fix: pass
- no assumed findings, missing access flagged as open items: pass
- no crawl or speed tool adopted without approval: pass
- content briefs route to content-marketer (who routes to copywriter-ar and copywriter-en): pass
- no final copy written here: pass
- no em dash anywhere: pass
- no tatweel: pass (note on shadda in "تعلّم" documented; shadda is correct grammar, not tatweel)
- Western numerals only: pass

Overall: qa-passed.

---

## Handoff

- content_briefs (CB-01 through CB-04): to content-marketer, who routes Arabic authorship to
  copywriter-ar and English to copywriter-en. All authored copy runs arabic-copy-qa or
  english-copy-qa then brand-qa-reviewer before publishing.
- on_page_specs (AR and EN class pages): to conversion-engineer for the RTL-correct page build.
  All customer-facing copy in the specs is a COPY-SLOT. Copywriters author and gate the final text.
- technical_findings: to conversion-engineer for resolution of hreflang tags, RTL render checks,
  canonical tags, sitemap inclusion, and robots.txt verification.
- open_items 1, 6, and 11: to human gate for Ahmed to resolve (Search Console access, hreflang
  x-default and ar-SA decision, catalog status confirmation).
- keyword_map: to analytics-reporter for streams 8 and 9 as the query baseline for organic
  search performance tracking.

This agent performed no live site action. Nothing was published.
