# content-package: 2026-06-elda-choucair-marketing

Internal planning artifact. Not customer-facing. Briefs and routing only. No final copy ships
from here. Copywriter-ar authors all Arabic articles. Copywriter-en authors all English articles.
Both run the full gate stack before any article publishes.
No em dashes, no tatweel, Western numerals only. Arabic-first throughout.

---

## Envelope

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: content-marketer
- stream: blog and content marketing
- status: draft (copy QA pending: article_briefs[] route to copywriter-ar and copywriter-en,
  who run arabic-copy-qa / english-copy-qa then brand-qa-reviewer on all authored copy;
  this package advances to qa-passed once those gates clear)
- qa:
  - skill_eval: pass (see section 5 self-check below)
  - brand_qa: na (internal planning artifact; customer-facing copy authored downstream)
- brief_refs: objective, channels (lifecycle email, organic social, content and blog, SEO),
  cadence (4 articles over the 2-week flight window, Arabic-first, English parallel),
  schedule (proposed flight 2026-06-08 to 2026-06-21, ASSUMPTION, confirm at human gate),
  offer (Masterclass "Elda Choucair, Teaches Marketing", Chapter 1 free, PDF cheatsheet),
  angle ("marketing is decision architecture"), segments (3 personas), constraints (all
  held-back claims excluded, no lesson list, no price, no accreditation)
- open_items: see section 4

---

## 1. Editorial calendar

### Calendar overview

4 Arabic-primary articles publishing across and around the 2-week paid flight.
English parallel versions publish concurrently (same day or within 24 hours) where the
EN copywriter is ready. Cadence: 1 article every 3 to 4 days, staggered to allow organic
social repurposing before the next article drops. SEO value compounds beyond the flight;
the articles are designed for sustained organic discovery, not only the 2-week window.

Proposed flight: 2026-06-08 to 2026-06-21 (ASSUMPTION, pending Ahmed confirmation).
Publish dates below are relative to that proposed start. All dates are planning estimates
and adjust when the start date is confirmed.

Publishing property: the Maharat blog (URL pattern TBD, blocked on blog platform
confirmation, see open_items). Articles link to the AR and EN class pages (confirmed URLs).

---

### Calendar items

```
item:            CAL-01
brief_ref:       CB-01
theme_ar:        هندسة القرار: ما يفوته معظم المسوّقين في فهم كيف يشتري الناس
theme_en:        Decision architecture: what most marketers miss about how people actually buy
angle_link:      "marketing is decision architecture"; the article introduces the central
                 intellectual frame of the class. It is the entry point to the whole content
                 program and the anchor for AI-answer citation.
seo_cluster:     marketing-decision-architecture
primary_query_ar: كيف يتخذ الناس قرارات الشراء   [RTL]
primary_query_en: how people make buying decisions
intent:          informational + generative
funnel_stage:    awareness / top-of-funnel (introduces the "decision architecture" frame
                 to searchers who do not yet know Maharat or the class)
segments_served: persona-1-data-driven-marketers (primary), all 3 (secondary)
language:        Arabic (copywriter-ar), English parallel (copywriter-en)
format:          long-form article, 800 to 1200 words AR, EN parallel
target_date:     Day 2 of flight, proposed 2026-06-09 (publishes early in flight so the
                 paid and organic traffic can find it; SEO value accrues post-flight)
owner:           copywriter-ar (AR), copywriter-en (EN), routed from this brief
status:          planned
note:            This is the highest-priority article for SEO and AI-answer citation.
                 Publish at the start of the flight so it is indexed before the flight closes.
```

```
item:            CAL-02
brief_ref:       CB-04
theme_ar:        القمع نظيف، والبيانات متوفرة. فلماذا لا يشتري أحد؟
theme_en:        Your funnel is clean and the data is there. So why is no one buying?
angle_link:      "Better questions beat more data"; addresses persona-1's exact pain from
                 the inside, using the pain-question entry style consistent with the strategy angle.
seo_cluster:     marketing-data-and-conversion
primary_query_ar: لماذا لا تتحول البيانات الى مبيعات   [RTL]
primary_query_en: why data-driven marketing fails to convert
intent:          informational + generative
funnel_stage:    awareness / consideration (pain-first, validates the reader's frustration
                 then reframes toward the decision layer; routes to class page)
segments_served: persona-1-data-driven-marketers (primary)
language:        Arabic (copywriter-ar), English parallel (copywriter-en)
format:          article, 700 to 1000 words AR, EN parallel
target_date:     Day 5 of flight, proposed 2026-06-12
owner:           copywriter-ar (AR), copywriter-en (EN), routed from this brief
status:          planned
note:            Paired thematically with CB-01: CB-01 introduces the frame, CB-04 applies
                 it to the exact pain persona-1 is living. Internal link CB-04 to CB-01.
```

```
item:            CAL-03
brief_ref:       CB-03
theme_ar:        بنيت شيئا حقيقيا، والسوق لا يعرف أنه موجود. ليس مشكلة جودة، بل مشكلة قرار.
theme_en:        You built something real and the market does not know it exists. That is not
                 a quality problem. It is a decision problem.
angle_link:      "make people care"; targets persona-2 (self-taught builders) and reframes
                 market silence from a quality verdict to a positioning and story question.
seo_cluster:     branding-and-positioning-arabic
primary_query_ar: كيف ابني علامة تجارية قوية   [RTL]
primary_query_en: how to build a strong brand
intent:          informational
funnel_stage:    awareness / consideration (persona-2 entry; connects the "make people care"
                 hook to the class as a structured way to learn brand thinking)
segments_served: persona-2-self-taught-builders (primary)
language:        Arabic (copywriter-ar), English parallel (copywriter-en)
format:          article, 700 to 1000 words AR, EN parallel
target_date:     Day 8 of flight, proposed 2026-06-15
owner:           copywriter-ar (AR), copywriter-en (EN), routed from this brief
status:          planned
note:            The EN parallel here has good B2B-adjacent SEO pull ("brand storytelling
                 for founders"). Coordinate with organic-social for repurposing, as this
                 theme performs well as a short post or quote card.
```

```
item:            CAL-04
brief_ref:       CB-02
theme_ar:        الفرق بين معرفة أدوات التسويق وامتلاك استراتيجيته
theme_en:        The difference between knowing the marketing tools and owning the strategy
angle_link:      "strategy over features"; addresses persona-3 (skilled-but-stuck executors)
                 and persona-2 together on the gap between tool mastery and strategic direction.
seo_cluster:     marketing-strategy-fundamentals-arabic
primary_query_ar: مبادئ استراتيجية التسويق   [RTL]
primary_query_en: marketing strategy fundamentals
intent:          informational
funnel_stage:    consideration / intent (later in the flight; by this point the class has
                 been in front of the audience for a week; this article deepens the case for
                 learning the thinking layer above the tools)
segments_served: persona-3-skilled-but-stuck-executors (primary), persona-2 (secondary)
language:        Arabic (copywriter-ar), English parallel (copywriter-en)
format:          article, 600 to 900 words AR, EN parallel
target_date:     Day 11 of flight, proposed 2026-06-18
owner:           copywriter-ar (AR), copywriter-en (EN), routed from this brief
status:          planned
note:            Publishes toward the end of the flight when lifecycle is at peak. Internal
                 link to CB-01 (decision architecture) and CB-03 (brand thinking) to build
                 topical depth. Useful as a lifecycle link from the non-payer flow as a
                 "here is what the class teaches" primer.
```

### Cadence note

4 articles across 11 days (roughly 1 every 2 to 3 days) is a sustained but achievable cadence
for a 2-week flight when the copywriters are working from complete briefs. Arabic articles are
primary; English parallels publish same-day or within 24 hours. This cadence supports
organic-social repurposing between drops. SEO search value for all 4 articles compounds
beyond the 14-day flight; the calendar plants content that serves the class page for months,
not only the flight window.

---

## 2. Article briefs (CB-01 to CB-04, expanded)

Each brief routes Arabic to copywriter-ar and English to copywriter-en.
No final copy is written here. The copywriters author from these briefs and run the gate stack:
arabic-copy-qa (Arabic), english-copy-qa (English), then brand-qa-reviewer.

---

### Article brief: CB-01-AR / CB-01-EN

```
id:               CB-01
calendar_ref:     CAL-01
campaign_id:      2026-06-elda-choucair-marketing
language_primary: Arabic (route to copywriter-ar)
language_parallel: English (route to copywriter-en)
target_date:      2026-06-09 (proposed, confirm with start date)

working_title_direction_ar:
  "هندسة القرار: الطريقة التي يتخذ بها الناس قرارات الشراء, وكيف تصنع لهم قرارهم أنت"
  (not final; copywriter-ar produces the final Arabic title to brand-voice.md.
  The direction: lead with the concept name, then the "make them decide" promise. No colon-
  after-concept is mandatory; copywriter-ar judges the rhythm.)

working_title_direction_en:
  "Decision architecture in marketing: how people actually decide, and how you shape that decision"
  (not final; copywriter-en produces the final EN title. Same shape: concept first, promise second.)

persona_served:   persona-1-data-driven-marketers (primary). All 3 personas (secondary).
segment_pain_addressed:
  Primary: "clean funnel and full dashboards that still do not convert."
  Secondary: the shared need for clearer marketing judgement across all 3 personas.

search_intent:    informational + generative (AI-answer citation priority)
target_query_ar:  كيف يتخذ الناس قرارات الشراء   [RTL]
target_query_en:  how people make buying decisions
seo_cluster:      marketing-decision-architecture
supporting_queries_to_address:
  ar: علم اتخاذ القرار في التسويق, هندسة القرار في التسويق
  en: decision-based marketing strategy, marketing decision architecture

angle_tie:
  "Marketing is decision architecture." This article is the intellectual entry point for the
  whole content program. It introduces the idea that marketing's job is to shape the conditions
  for a decision in the audience's favour, not to optimise clicks or impressions. This is the
  class's central frame. The article does not promise revenue or conversion lift; it promises
  a sharper way of thinking about why people decide.

proposed_outline_ar (H1 to H3, direction only; copywriter-ar finalises):
  H1: [matches primary query intent, e.g. "كيف يتخذ الناس قرارات الشراء؟ دليل المسوّق الذكي"]
  H2-1: ما هي هندسة القرار في التسويق؟
    (self-contained, definition-first. 2 to 3 sentences. Structured for AI-answer citation.
    No vague language. Define the concept, not the buzz.)
  H2-2: لماذا لا تكفي البيانات والقمع التسويقي
    (connects to persona-1 pain. The funnel is clean; something is missing at the decision
    step. The missing layer is the decision frame, not more data.)
  H2-3: الأسئلة التي تغيّر طريقة قراءتك للحملة
    (the "better questions beat more data" pivot. Empowering: the reader already has the
    tools; this adds the question set that changes what the tools reveal.)
  H2-4: كيف تطوّر حكمك التسويقي
    (empowering arc toward action. Routes to the class page as a structured resource for
    building this thinking. Name Elda and the class in this section with her confirmed
    credentials: CEO of Omnicom Media Group MENA, 20 years of experience.)
  H3-FAQ: 3 to 5 question-headed subsections for generative intent.
    Question shapes (not final copy, copywriter-ar writes the questions and answers):
    "ما هي هندسة القرار في التسويق؟", "كيف يتخذ المستهلك قرار الشراء؟",
    "لماذا تفشل الحملات التسويقية القائمة على البيانات؟"

proposed_outline_en (parallel, copywriter-en writes independently from this direction):
  H1: [matches EN primary query, "how people make buying decisions" intent]
  H2-1: What decision architecture actually means in marketing
  H2-2: Why data and funnels alone do not drive the decision
  H2-3: The questions that change how you read a campaign
  H2-4: How to build sharper marketing judgment
  H3-FAQ: 3 to 5 question-led subsections matching the AR FAQ intent

internal_links:
  - anchor_direction: name Elda and the class when citing it as the structured resource
    target_url_ar: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    target_url_en: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
    placement: H2-4 (the empowering arc section; contextual, not a banner)
  - anchor_direction: link to CB-02 article (marketing strategy fundamentals) once published
    target_url: [to be assigned on publish]
    placement: within the body or closing section, topical connection
  - anchor_direction: link to CB-04 article (funnel not converting) once published
    target_url: [to be assigned on publish]
    placement: H2-2 (the data and funnel section; companion piece)

cta:
  One CTA per article. Arabic version points to the AR class page and/or the
  member Start Watching URL. English version points to the EN equivalents.
  CTA direction (not final copy): invite the reader to explore the class as the structured way
  to learn this thinking. Surface the Chapter 1 free offer. Do not mention price, plan, or
  promotion (all ASSUMPTION fields, unconfirmed).
  CTA_url_ar: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
              and/or https://member.maharat.com/ar/class/elda-choucair-teaches-marketing
  CTA_url_en: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
              and/or https://member.maharat.com/en/class/elda-choucair-teaches-marketing
  Signup gate note: new readers landing from organic search route via the class page to the
  signup gate (email or WhatsApp, per the brief). No PII in any tracking parameter.

word_count:       800 to 1200 words (AR), EN parallel at similar length
tone:             Thmanyah-adjacent: clear, modern, intelligent. Empowering, not academic.
                  Sharp, contrarian register consistent with Elda's voice direction.

guardrails_for_copywriters:
  - No invented lesson list, module titles, or curriculum specifics.
  - No Cannes Grand Prix reference, no spend figures, no "100 brands" claim.
  - Elda may be named with confirmed credentials only: CEO of Omnicom Media Group MENA,
    20 years of experience ("20 years in one class" is approved phrasing).
  - No accreditation claim. Completion certificate exists but is not accredited; do not
    imply or state otherwise.
  - No price, plan name, or promotion in the article copy.
  - Promise frameworks and clearer thinking, never revenue or growth outcomes.
  - Empowering framing throughout: the hero is the reader building judgement; Elda is
    the guide. No deficit framing.
  - No em dashes, no tatweel, Western numerals only, RTL-correct for the Arabic version.

route_to:
  copywriter-ar: Arabic article
  copywriter-en: English article (parallel, independent authoring, not a translation)
gate_stack: arabic-copy-qa (AR), english-copy-qa (EN), then brand-qa-reviewer for each
```

---

### Article brief: CB-04-AR / CB-04-EN

```
id:               CB-04
calendar_ref:     CAL-02
campaign_id:      2026-06-elda-choucair-marketing
language_primary: Arabic (route to copywriter-ar)
language_parallel: English (route to copywriter-en)
target_date:      2026-06-12 (proposed)

working_title_direction_ar:
  "القمع نظيف، والبيانات جاهزة. فلماذا لا يشتري أحد؟"
  (direction: open with the reader's exact reality as a question. Validation first,
  then the reframe. Copywriter-ar produces the final title.)

working_title_direction_en:
  "Your funnel is clean and the data is there. So why is no one buying?"
  (same shape in EN. Copywriter-en produces the final.)

persona_served:   persona-1-data-driven-marketers (primary)
segment_pain_addressed:
  "A clean funnel and full dashboards that still do not convert. Chasing more data
   instead of a better question."

search_intent:    informational + generative (AI-answer citation for "funnel not converting")
target_query_ar:  لماذا لا تتحول البيانات الى مبيعات   [RTL]
target_query_en:  why data-driven marketing fails to convert
seo_cluster:      marketing-data-and-conversion
supporting_queries_to_address:
  ar: الفانل التسويقي لا يعمل, البيانات التسويقية واتخاذ القرار
  en: marketing funnel not converting, beyond data marketing judgment

angle_tie:
  "Better questions beat more data." Pain-first entry: the article acknowledges the
  reader's exact reality (clean funnel, no result) and reframes it as a decision-layer gap,
  not a data gap. The resolution is clearer thinking, not more tracking. Routes empoweringly
  toward the class as the structured resource. Does not promise conversion improvement.

proposed_outline_ar (direction only; copywriter-ar finalises):
  H1: [matches primary query intent]
  H2-1: الجواب المباشر: لماذا يفشل القمع رغم أنه نظيف
    (self-contained answer, 2 to 3 sentences, structured for AI-answer citation.)
  H2-2: الافتراض الخاطئ الذي يصنعه معظم المسوّقين القائمين على البيانات
    (the assumption that more data or better metrics will solve a decision-layer problem)
  H2-3: ما الذي يحدث فعلاً عند نقطة القرار
    (the decision layer: the gap below the dashboard that data cannot see alone)
  H2-4: الأسئلة التي تغيّر طريقة قراءتك لبيانات القمع
    (the "better questions" pivot. Empowering, not prescriptive.)
  H2-5: كيف تبني الحكم الذي يجلس فوق الداشبورد
    (routes toward the class; name Elda with confirmed credentials in this section)
  H3-FAQ: 2 to 3 question-led subsections for generative intent.
    Shapes: "لماذا لا يعمل الفانل التسويقي؟", "ما الذي يجعل المستهلك يشتري في النهاية؟"

proposed_outline_en (parallel, independent):
  H1: [matches EN query intent]
  H2-1: The direct answer: why a technically correct funnel can convert zero
  H2-2: The assumption data-driven marketers make
  H2-3: What is actually happening at the decision point
  H2-4: The questions that change how you read your funnel data
  H2-5: How to build the judgment that sits above the dashboard
  H3-FAQ: 2 to 3 question-led subsections

internal_links:
  - anchor_direction: cite the class and Elda in H2-5 as the structured learning resource
    target_url_ar: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    target_url_en: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
    placement: H2-5
  - anchor_direction: link to CB-01 article (decision architecture) once published
    target_url: [to be assigned on publish]
    placement: H2-3 or H2-4, topical companion piece

cta:
  One CTA. Direction: invite the reader to explore the class as the place to build the
  judgment above the dashboard. Surface Chapter 1 free. No price, plan, or promotion.
  CTA_url_ar: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  CTA_url_en: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
  Signup gate note: same as CB-01. No PII in tracking parameters.

word_count:       700 to 1000 words (AR), EN parallel
tone:             Pain-aware but empowering. Speak to someone capable and stuck, not to
                  someone who has failed. The problem is the frame, not the person.

guardrails_for_copywriters: same as CB-01 (no lesson list, no held-back claims, no
  accreditation, no price, no revenue promise, empowering framing, RTL-correct AR).

route_to:
  copywriter-ar: Arabic article
  copywriter-en: English article
gate_stack: arabic-copy-qa (AR), english-copy-qa (EN), then brand-qa-reviewer
```

---

### Article brief: CB-03-AR / CB-03-EN

```
id:               CB-03
calendar_ref:     CAL-03
campaign_id:      2026-06-elda-choucair-marketing
language_primary: Arabic (route to copywriter-ar)
language_parallel: English (route to copywriter-en)
target_date:      2026-06-15 (proposed)

working_title_direction_ar:
  "بنيت شيئا يستحق. السوق لم يلتفت بعد. هذه ليست مشكلة جودة."
  (direction: open empoweringly. Validate the builder's effort. Reframe silence as a
  positioning question, not a quality verdict. Copywriter-ar produces the final title.)

working_title_direction_en:
  "You built something worth knowing about. The market has not noticed yet. That is a
   positioning problem, not a quality problem."
  (Copywriter-en produces the final EN title.)

persona_served:   persona-2-self-taught-builders (primary)
segment_pain_addressed:
  "Shipped a real product and met silence; capable maker, but the market does not care yet."

search_intent:    informational
target_query_ar:  كيف ابني علامة تجارية قوية   [RTL]
target_query_en:  how to build a strong brand
seo_cluster:      branding-and-positioning-arabic
supporting_queries_to_address:
  ar: كيف اجعل الناس يهتمون بمنتجي, استراتيجية بناء العلامة التجارية, قصة العلامة التجارية
  en: brand storytelling for founders, how to make people care about your product

angle_tie:
  "Make people care." Market silence is not a verdict on the product's quality; it is a
  gap in the story that shapes the conditions for a decision. The article reframes the
  "shipped but silent" reality as a solvable positioning and story question, not a failure.
  Routes empoweringly to the class as the structured way to learn this thinking.

proposed_outline_ar (direction only; copywriter-ar finalises):
  H1: [matches "كيف ابني علامة تجارية قوية" intent]
  H2-1: ما هو التمييز فعلاً؟ (ليس شعاراً، بل قراراً)
    (positioning as a decision about whose life to become part of, not a tagline or logo)
  H2-2: لماذا تفشل العلامات التجارية حين تبدأ من المنتج لا من القرار
    (the product-first vs decision-first frame; no case studies invented; use widely
    understood framing)
  H2-3: دور قصة العلامة في صناعة القرار
    (not narrative storytelling as a concept, but how a story shapes the conditions for
    a choice; connects to "decision architecture" without being redundant with CB-01)
  H2-4: كيف تبدأ في بناء علامة تجارية يختارها الناس
    (practical, non-prescriptive empowering arc; routes to the class with Elda's
    confirmed credentials)
  H3-FAQ: 2 to 3 questions.
    Shapes: "ما الفرق بين التسويق والعلامة التجارية؟", "كيف اجعل الناس يهتمون بمنتجي؟"

proposed_outline_en (parallel, independent):
  H1: [matches "how to build a strong brand" intent]
  H2-1: What positioning actually decides (it is not a tagline)
  H2-2: Why branding fails when it starts from the product, not the decision
  H2-3: How brand story shapes the conditions for a choice
  H2-4: How to start building a brand people actively choose
  H3-FAQ: 2 to 3 question-led subsections (e.g. "What is the difference between
           marketing and branding?", "How do you make people care about your product?")

internal_links:
  - anchor_direction: name the class and Elda as the structured resource in H2-4
    target_url_ar: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    target_url_en: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
    placement: H2-4
  - anchor_direction: link to CB-02 article (strategy fundamentals) once published
    target_url: [to be assigned on publish]
    placement: H2-1 or H2-2, topical connection

cta:
  One CTA. Direction: invite the reader to explore the class as the structured way to
  learn how to build a brand people choose. Surface Chapter 1 free. No price or plan.
  CTA_url_ar: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  CTA_url_en: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing

word_count:       700 to 1000 words (AR), EN parallel
tone:             Empowering with "make people care" urgency. Clear, warm, not academic.
                  The reader is a capable builder; the article adds the frame, not the skill.

guardrails_for_copywriters:
  - No invented brand case studies or invented regional examples. Use widely established
    positioning thinking; do not fabricate examples.
  - Same standing guardrails as CB-01: no lesson list, no held-back claims, no accreditation,
    no price, no revenue promise, empowering framing throughout.

route_to:
  copywriter-ar: Arabic article
  copywriter-en: English article
gate_stack: arabic-copy-qa (AR), english-copy-qa (EN), then brand-qa-reviewer
```

---

### Article brief: CB-02-AR / CB-02-EN

```
id:               CB-02
calendar_ref:     CAL-04
campaign_id:      2026-06-elda-choucair-marketing
language_primary: Arabic (route to copywriter-ar)
language_parallel: English (route to copywriter-en)
target_date:      2026-06-18 (proposed)

working_title_direction_ar:
  "الفرق بين معرفة أدوات التسويق وامتلاك استراتيجيته"
  (direction: plain and direct. States the gap the article addresses. Copywriter-ar
  may adjust for rhythm and brand voice.)

working_title_direction_en:
  "The difference between knowing the marketing tools and owning the strategy"
  (Copywriter-en produces the final.)

persona_served:   persona-3-skilled-but-stuck-executors (primary), persona-2 (secondary)
segment_pain_addressed:
  Primary: "Mastered the tools but growth has stalled; effort at the feature level, no movement."
  Secondary: "Capable maker who needs the strategy layer above the product."

search_intent:    informational
target_query_ar:  مبادئ استراتيجية التسويق   [RTL]
target_query_en:  marketing strategy fundamentals
seo_cluster:      marketing-strategy-fundamentals-arabic
supporting_queries_to_address:
  ar: كيف اعمل استراتيجية تسويقية, مفاهيم التسويق الحديث, الفرق بين التسويق والمبيعات
  en: how to build a marketing strategy, marketing fundamentals for beginners

angle_tie:
  "Strategy over features." The article addresses the gap between knowing how to use the
  tools and knowing where to point them. The reader is skilled; the missing layer is the
  strategic judgement that decides what to do with the skill. Empowering: tools plus
  judgement, not tools replaced by something else.

proposed_outline_ar (direction only; copywriter-ar finalises):
  H1: [matches "مبادئ استراتيجية التسويق" intent]
  H2-1: ما الفرق بين الاستراتيجية التسويقية وخطة التنفيذ؟
    (a clear, practical distinction; the article is the answer to the reader's real
    confusion, not a lecture on theory)
  H2-2: الأسئلة الثلاثة التي تجيب عليها الاستراتيجية القوية
    (do not invent proprietary frameworks; use widely established strategic thinking
    to give the reader a concrete handle on "what strategy actually decides")
  H2-3: لماذا يصطدم المنفّذون المهرة والبنّاؤون المستقلون بنفس الحائط
    (connects both personas without naming them as segments; the common wall is the
    missing strategy layer, not a personal failure)
  H2-4: كيف تنتقل من التنفيذ إلى التفكير الاستراتيجي
    (empowering arc; routes to the class with Elda's confirmed credentials;
    this is where the piece closes with purpose, not a hard sell)

proposed_outline_en (parallel, independent):
  H1: [matches "marketing strategy fundamentals" intent]
  H2-1: What a marketing strategy actually decides versus what an execution plan decides
  H2-2: The 3 questions a strong marketing strategy must answer
  H2-3: Why skilled executors and self-taught builders hit the same wall
  H2-4: How to move from tactics to strategic thinking

internal_links:
  - anchor_direction: name Elda and the class as the structured resource in H2-4
    target_url_ar: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
    target_url_en: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing
    placement: H2-4
  - anchor_direction: link to CB-01 article (decision architecture) once published
    target_url: [to be assigned on publish]
    placement: H2-1 or H2-4, topical connection
  - anchor_direction: link to CB-03 article (brand and positioning) once published
    target_url: [to be assigned on publish]
    placement: H2-2, the "where to point the tools" connection

cta:
  One CTA. Direction: invite the reader to explore the class as the structured way to
  build the strategy layer above the tools. Surface Chapter 1 free. No price or plan.
  CTA_url_ar: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
  CTA_url_en: https://www.maharat.com/en/class/business/elda-choucair-teaches-marketing

word_count:       600 to 900 words (AR), EN parallel
tone:             Plain, confident, intelligent. Empowering, never a lecture. The reader
                  is skilled; the article adds the frame they have not yet built.

guardrails_for_copywriters: same as CB-01 and CB-03. No invented frameworks beyond
  widely established strategic thinking. No lesson list, held-back claims, accreditation,
  price, or revenue promise.

route_to:
  copywriter-ar: Arabic article
  copywriter-en: English article
gate_stack: arabic-copy-qa (AR), english-copy-qa (EN), then brand-qa-reviewer
```

---

## 3. Content distribution plan

### Distribution overview

Each article feeds 2 downstream streams:
1. Organic-social: repurposing into post or quote card(s), routed to organic-social agent.
2. Lifecycle: one article linked per email touch in the non-payer flow, routed to
   lifecycle-architect.

Distribution is routed and briefed here. Final social captions and email copy are authored
by the relevant copywriter and run their own gate stack before any post or send. Nothing
publishes, posts, or sends without the human gate clearing each piece.

No distribution tool is adopted or wired here without approval per CLAUDE.md principle 3.
The CMS and blog platform are open items (see section 4). Articles are distributed once
published on the blog property.

---

### Article CB-01 distribution

```
source:           CB-01 article (decision architecture)
article_date:     2026-06-09 (proposed)

derivatives:

  format:         organic-social post (Arabic primary, EN parallel)
  angle_carried:  "Marketing is decision architecture." Lead with the myth-flip or pain-
                  question hook from the strategy angle. The post is a compressed version
                  of the H2-1 or H2-3 section (the concept or the better-questions pivot).
                  Not a summary; a standalone provocation that earns a click to the article.
  cta:            link to the published article; article carries the class page CTA.
  language:       Arabic primary. EN parallel as a second post (same day or next day).
  owner:          organic-social (briefs the caption to copywriter-ar / copywriter-en)
  timing:         Day 2 of flight (same day as article publish or day after)
  format_notes:   Consider a quote card visual using a key one-liner from the article
                  (rights-cleared layout; no generated image of Elda). Route the visual
                  brief to creative-director if a new asset is needed; reuse published
                  cover image and text overlay where possible.
  routing_notes:  organic-social agent briefs this from the article; copywriter produces
                  caption; arabic-copy-qa then brand-qa-reviewer; then human gate before post.

  format:         lifecycle email link (AR non-payer flow)
  angle_carried:  The "decision architecture" frame as the intellectual hook for the
                  class. Link to the article as a value-add in an early non-payer touch.
                  The article deepens the case before the class CTA appears.
  cta:            article link (leading to the class page CTA within the article)
  language:       Arabic
  owner:          lifecycle-architect (links to this article from the appropriate email
                  in the non-payer sequence; copywriter-ar authors any surrounding copy)
  timing:         Aligned with the lifecycle flow, not a standalone send. Day 3 to 4 of
                  flight (after article indexes).
  routing_notes:  lifecycle-architect decides placement in the flow; arabic-copy-qa then
                  brand-qa-reviewer on any new email copy around the link.
```

---

### Article CB-04 distribution

```
source:           CB-04 article (funnel not converting)
article_date:     2026-06-12 (proposed)

derivatives:

  format:         organic-social post (Arabic primary, EN parallel)
  angle_carried:  Pain-question hook: validate the "clean funnel, no result" reality in
                  1 to 2 lines, then the reframe ("not a data problem, a decision problem").
                  The post earns the click by naming the reader's exact experience.
  cta:            link to the published article
  language:       Arabic primary, EN parallel
  owner:          organic-social
  timing:         Day 5 (same day as publish or day after)
  format_notes:   This theme is highly shareable with the data-literate professional
                  audience. A text-forward post performs well here; no image required,
                  but a quote card option is available if creative can turn it fast.

  format:         lifecycle email link (AR non-payer flow)
  angle_carried:  "Your funnel may be clean but the decision layer is missing." Links
                  directly to persona-1 pain. Place in the mid-flight lifecycle touch
                  for recently-active non-payers who have already seen the class intro.
  cta:            article link
  language:       Arabic
  owner:          lifecycle-architect
  timing:         Day 6 to 7 of flight (mid-flight lifecycle beat)
  routing_notes:  lifecycle-architect decides placement. This article pairs well with the
                  PDF cheatsheet send (if lifecycle uses the cheatsheet as a touch).
```

---

### Article CB-03 distribution

```
source:           CB-03 article (build a brand people care about)
article_date:     2026-06-15 (proposed)

derivatives:

  format:         organic-social post (Arabic primary, EN parallel)
  angle_carried:  "Make people care" hook for persona-2 builders. Opening line validates
                  the "built it, met silence" reality; second line reframes empoweringly
                  ("that is not a quality verdict; it is a story gap").
  cta:            link to the published article
  language:       Arabic primary. EN parallel (the EN version has strong B2B-adjacent
                  appeal on the "brand storytelling for founders" thread; coordinate with
                  organic-social on LinkedIn distribution for the EN version).
  owner:          organic-social
  timing:         Day 8 (same day as publish or day after)
  format_notes:   High visual potential. A quote card with a key one-liner (e.g. the
                  myth-flip on product quality vs story) works well for this theme.
                  Route to creative-director if a new asset is commissioned; reuse the
                  published class cover image with text overlay as a first option.

  format:         lifecycle email link (AR non-payer flow)
  angle_carried:  "Make people care" as the persona-2 entry. Link to the article for
                  non-payers who match the self-taught builder profile. Can be used as a
                  late-flight lifecycle touch before the final class CTA.
  cta:            article link
  language:       Arabic
  owner:          lifecycle-architect
  timing:         Day 9 to 10 of flight
  routing_notes:  lifecycle-architect places this where the persona-2 segment sits in
                  the flow; may overlap with or follow the PDF cheatsheet touch.
```

---

### Article CB-02 distribution

```
source:           CB-02 article (marketing strategy fundamentals)
article_date:     2026-06-18 (proposed)

derivatives:

  format:         organic-social post (Arabic primary, EN parallel)
  angle_carried:  "Strategy over features" for persona-3 executors. Opening: name the
                  gap (know the tools, growth has stalled) without deficit framing. The
                  post positions the article as the next step, not a fix.
  cta:            link to the published article
  language:       Arabic primary, EN parallel
  owner:          organic-social
  timing:         Day 11 (same day as publish or day after; close to flight end, so the
                  organic-social post is the reach booster as paid winds down)
  format_notes:   This is the most "primer" in feel of the 4 articles. A list-style post
                  (e.g. "3 questions a marketing strategy must answer") could perform
                  well as the social derivative; the caption routes to the article for depth.

  format:         lifecycle email link (AR non-payer flow)
  angle_carried:  "The strategy above the tools": link to this article as a late-flight
                  lifecycle touch. Works well as a "here is what the class teaches" signal
                  for persona-3 non-payers who have received the early flow but not converted.
  cta:            article link (class CTA is within the article)
  language:       Arabic
  owner:          lifecycle-architect
  timing:         Day 11 to 12 of flight (late-flight; pairs with the final lifecycle CTA)
  routing_notes:  This is the last content touch before the flight closes. lifecycle-
                  architect may pair it with the strongest class CTA in the sequence.
```

---

### Signup gate routing summary

Every article, social post, and lifecycle email in this plan ultimately routes the reader
to the AR or EN class page, and from there to the Start Watching (signup/paywall) URL.

```
all articles:
  AR reader path: article CTA -> maharat.com/ar/class/business/elda-choucair-teaches-marketing
                  -> member.maharat.com/ar/class/elda-choucair-teaches-marketing (signup gate)
  EN reader path: article CTA -> maharat.com/en/class/business/elda-choucair-teaches-marketing
                  -> member.maharat.com/en/class/elda-choucair-teaches-marketing (signup gate)

social posts: link to the published article; article carries the class CTA.
lifecycle emails: link to the article for value; article carries the class CTA.

tracking parameter rule: no PII, no sensitive data in any URL parameter. UTM parameters
  (source, medium, campaign) are acceptable for attribution; copywriter or lifecycle-
  architect appends them per the tracking plan. No personal identifier in the URL.
```

---

## 4. Open items

```
1. BLOG PLATFORM (BLOCKING for publish). The Maharat blog URL pattern and CMS platform are
   not confirmed in the brief. Article URLs for internal linking (CB-01 to CB-04) are marked
   [to be assigned on publish]. Nothing publishes until the platform is named and Ahmed
   approves. Surface at the human gate. This also blocks the SEO package's open item 9
   (content article URLs for the on_page_specs internal link plan).

2. FLIGHT START AND END DATE (ASSUMPTION). Proposed 2026-06-08 to 2026-06-21. All publish
   dates in this calendar are offsets from that proposed start. Confirm at the human gate
   before briefing the copywriters with final due dates.

3. PRICE, PLAN, AND PROMOTION (ASSUMPTION, from brief). No price, plan name, or promotion
   appears in any article brief or CTA direction here. Copywriters must not add any until
   confirmed. These fields carry forward from the strategy-artifact open items.

4. GATE PLATFORM AND SIGNUP FLOW (OPEN ITEM, from brief). The email and WhatsApp CRM
   platform is unconfirmed (Ortto vs HubSpot). Lifecycle email distribution of the articles
   is designed here but nothing sends until the platform is named. The lifecycle-architect
   owns the send; this plan hands the article links and timing direction.

5. ARTICLE URLS (BLOCKED on item 1). Internal link targets within and between articles are
   marked [to be assigned on publish]. The SEO on_page_specs internal link plan also depends
   on these URLs. Once the blog platform is confirmed and URLs are assigned, this package
   and the seo-package on_page_specs must be updated.

6. COPY QA STATUS (PENDING). All 4 AR articles and 4 EN articles are routed to the
   copywriters from this package. This content-package status is draft until:
   (a) copywriter-ar produces all 4 AR articles and they pass arabic-copy-qa and brand-qa-reviewer.
   (b) copywriter-en produces all 4 EN articles and they pass english-copy-qa and brand-qa-reviewer.
   Only then does this package advance to qa-passed.

7. FORMAL CATALOG STATUS FOR ELDA (OPEN ITEM, carried from strategy-artifact and seo-package).
   The published class page is sufficient to name her in these articles. Formal team
   confirmation is pending. Surface at the human gate.

8. SOCIAL POST VISUAL ASSETS. The distribution plan notes quote card opportunities for
   CB-01, CB-03, and CB-04. Reuse the published rights-cleared cover images with text
   overlay as the first option. If new assets are commissioned, route to creative-director.
   No generated image of Elda. Rights-cleared imagery only.

9. EN PARALLEL TIMING. All 4 EN articles are flagged as same-day or within 24 hours of
   the AR publish. If copywriter-en capacity does not support this, the EN articles shift
   by up to 2 days without affecting the Arabic calendar. Confirm at the human gate.

10. WHY-NOW AND LIFECYCLE COORDINATION. The article link timing in the distribution plan
    is proposed relative to the flight. lifecycle-architect may adjust placement within the
    flow; this plan defers to lifecycle on send sequencing once the article is published.
```

---

## 5. Skill eval self-check

Checks run against the content-marketing, editorial-calendar, article-brief, and
content-distribution eval criteria:

- incoming envelope validated: strategy-artifact qa-passed, seo-package qa-passed,
  brief confirms objective, channels (lifecycle email, organic social, blog), cadence
  (2-week flight), offer (Masterclass, Chapter 1 free, PDF cheatsheet): pass
- campaign_id present and correct on envelope and all briefs: pass
- calendar leads Arabic-first, themes trace to strategy angle and seo keyword map: pass
- each calendar item carries angle_link, seo_cluster, format, target_date, owner, status: pass
- all 4 articles route to copywriter-ar (AR) and copywriter-en (EN): pass
- no final copy written in this package: pass
- each article brief carries target_query (AR and EN), intent, outline, internal_links, cta: pass
- one target query and one intent per article (CB-01 informational+generative counted as
  one intent with a generative sub-cluster, per seo-package precedent; not a multi-intent split): pass
- one CTA per article brief, pointing to class page and/or signup gate URL: pass
- internal link targets identified; [to be assigned on publish] flagged for unconfirmed URLs: pass
- distribution plan repurposes each article into organic-social and lifecycle formats: pass
- each derivative carries angle_carried and cta; routes to the producing owner: pass
- no distribution tool adopted or wired without approval: pass
- signup gate routing summary present, no PII in tracking parameters noted: pass
- open items section present, all blockers surfaced: pass
- no invented lesson list, module titles, curriculum specifics: pass
- no held-back claims (no "100 brands", no spend figures, no Cannes): pass
- no price, plan, or promotion in any brief or CTA direction: pass
- no accreditation claim anywhere: pass
- Elda named with confirmed credentials only (CEO Omnicom MENA, 20 years experience): pass
- promise direction: frameworks and clearer thinking, never revenue or growth outcomes: pass
- empowering framing throughout, no deficit-framing in any theme, outline, or CTA direction: pass
- no em dashes anywhere in this file: pass
- no tatweel anywhere: pass
- Western numerals only: pass
- RTL noted for all Arabic article briefs and queries: pass

Overall skill eval: pass.

---

## 6. Handoff

```
article_briefs[] (CB-01, CB-02, CB-03, CB-04, AR and EN):
  -> copywriter-ar: all 4 Arabic articles
  -> copywriter-en: all 4 English articles
  Each authored article runs: arabic-copy-qa or english-copy-qa, then brand-qa-reviewer.
  No article publishes until the gate stack clears.

distribution_plan:
  -> organic-social: 4 social derivatives (one per article), Arabic primary with EN parallels.
     organic-social briefs the captions from the distribution_plan; copywriters author captions;
     arabic-copy-qa / english-copy-qa, then brand-qa-reviewer, before any post.
  -> lifecycle-architect: 4 article link touch-points for the non-payer email flow.
     lifecycle-architect places these in the flow sequence; copywriter-ar authors any
     surrounding email copy; arabic-copy-qa then brand-qa-reviewer before any send.

seo coordination:
  -> seo-specialist: once articles are published and URLs are confirmed, the seo-package
     on_page_specs internal link slots (marked [to be assigned]) are updated with the
     actual article URLs. SEO and content-marketer coordinate on this.

open items 1, 2, 3, 4, 7:
  -> human gate (Ahmed) for resolution before any publish, send, or spend.

publish action:
  Nothing in this package publishes, posts, or sends without explicit sign-off from Ahmed
  per action and per campaign, via the human gate. Silence is not approval.
```
