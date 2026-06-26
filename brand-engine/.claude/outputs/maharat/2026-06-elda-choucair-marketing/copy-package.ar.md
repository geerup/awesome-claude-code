# copy-package.ar.md

النسخة العربية، وهي الأساس. الإنجليزية تكتب بشكل منفصل بواسطة copywriter-en على المسار نفسه،
والمجموعتان تندمجان عند بوابة جودة واحدة. كل الكلمات هنا موجهة للعميل، بصوت ماهرات، عربية فصحى
حديثة بنبرة ثمانية، وبصوت إلدا شقير: حاد، مناقض للسائد، بإيقاع من شطرين (اعتقاد شائع، ثم القلب).
البطل هو المتعلم الذي يكسب وضوح القرار، وإلدا هي الدليل، والخصم دائما هو الاستراتيجية الآمنة
المنسية، لا القارئ أبدا.

## Envelope

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: copywriter-ar
- stream: 4 copywriting (Arabic variants, primary)
- status: draft
- qa:
  - skill_eval: self-checked against 04-copywriting, email-copy, subject-lines, ad-copy evals.json
  - arabic_copy_qa: pending (next gate)
  - brand_qa: pending (runs after arabic-copy-qa, alongside compliance-privacy-reviewer)
  - english_copy_qa: na (Arabic package; EN sibling carries its own)
- brief_refs: objective, segments (3 personas + owned-recency cut for E5), instructor
  (Elda Choucair, claims 1, 2, 6, 7), lead_magnet (Chapter 1 free + marketing-campaign PDF
  cheatsheet), class URLs (AR confirmed), offer_framing_notes, mandatories, constraints
  (held-back claims 4 and 5). Price, plan, promotion: ASSUMPTION, no number in any copy.
  No lesson list, duration, lesson count, or discount invented.
- open_items: see the final section. Lead blocker for the conversion CTA specifics: price,
  plan, and promotion are ASSUMPTION; the subscribe CTA in E4 and the landing CTA stay
  generic (no number, no plan name) until confirmed.

Held-back, verified absent from every unit below: "worked with 100 plus brands", any dollar
or spend figure (claim 4), the Cannes reference (claim 5). Promise is frameworks and clearer
thinking only, never revenue or growth. No accreditation implication anywhere. Verified title
used only: "إلدا شقير، تعلّم التسويق".

URLs used (confirmed, AR):
- Class page AR: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing
- Start Watching AR (Chapter 1, member): https://member.maharat.com/ar/class/elda-choucair-teaches-marketing

---

## A. LIFECYCLE EMAIL FLOW (E1 to E5) - the focus

Pattern: NON-PAYER (owned non-payers, registered, never purchased), per sequence-standards.md.
Objective: first subscription. Arc: hook (E1), persona value led by the PDF cheatsheet (E2),
the senior voice and why it differs from free content (E3), the decision moment with a soft
subscribe CTA (E4), an empowering last call and warm re-entry for the never-engaged (E5).

One clear CTA per email. No price, no plan name, no discount, no lesson count anywhere.
Chapter 1 free and the marketing-campaign PDF cheatsheet are the confirmed hooks, used as
stated. Send timing follows the morning local 8 AM to 10 AM standard except the entry email.

---

### E1: Hook, "marketing is decision architecture" + watch Chapter 1 free

- id: email-e1-hook
- segment: all three personas (shared angle, the entry message of the flow)
- language: ar
- sequence: nonpayer
- objective: conversion (entry email of the non-payer flow; one action: start Chapter 1 free)
- send_trigger: time-based, the entry message of the flow, fires within about 5 minutes of
  flow entry while the contact is warmest; the rest of the arc sends morning local 8 AM to 10 AM
- subject_ref: subj-e1

Subject line A (primary): التسويق ليس قائمة تكتيكات، بل هندسة قرار
  - length: 42 characters; mobile band ok; key word "التسويق" front-loaded in first 30
Subject line B: درس واحد يغير طريقة تفكيرك في التسويق
Preheader: صف إلدا شقير على ماهرات. الفصل الأول مجاني، ابدأ من فكرة واحدة تبقى معك.
  - length: about 70 characters; adds a promise, does not repeat the subject

Body:
معظم الجهد التسويقي يذهب إلى التنفيذ: الإعلان، القمع التسويقي، البيانات، المحتوى.
ومع ذلك يبقى شيء ناقص. ليس جهدا أكثر، بل طبقة مختلفة.

التسويق هندسة قرار. أن تفهم كيف يختار الناس فعلا، وأن تبني كل شيء حول تلك اللحظة. لا حول الانطباع، بل حول القرار.

قادت إلدا شقير أكثر من 20 سنة من أعقد العمل التسويقي في المنطقة، بصفتها الرئيسة التنفيذية لمجموعة أومنيكوم ميديا في الشرق الأوسط وشمال إفريقيا. صفها على ماهرات يلخص ذلك في شيء واحد: طريقة التفكير التي تقف فوق التكتيكات.

الفصل الأول مجاني. بلا التزام، فقط الدرس الأول.

CTA: شاهد الفصل الأول مجانا
URL: https://member.maharat.com/ar/class/elda-choucair-teaches-marketing

---

### E2: Persona value, led by the PDF cheatsheet (3 persona-tuned sends)

One email, tuned per persona. The marketing-campaign PDF cheatsheet is the entry hook for all
three; the promise is tuned to each persona's pain. One CTA each: get the cheatsheet.
send_trigger for all three: behavior-triggered, fires about 2 to 3 days after E1 on the branch
"opened or clicked E1 but has not started Chapter 1", layered on the time-based foundation.
objective: conversion (the cheatsheet moves the persona toward starting the class).

---

#### E2-P1: Data-driven marketers (tuned line: better questions beat more data)

- id: email-e2-p1-datadriven
- segment: persona-1-data-driven-marketers
- language: ar
- sequence: nonpayer
- objective: conversion
- send_trigger: behavior-triggered, about 2 to 3 days after E1 on "opened E1, not started"
- subject_ref: subj-e2-p1

Subject line A (primary): قمعك التسويقي نظيف، فلماذا لا أحد يشتري؟
Subject line B: لا تنقصك بيانات أكثر، بل أسئلة أفضل
Preheader: حمّل ملخص الحملة التسويقية، ثم شاهد كيف تفكر إلدا في القرار لا في المؤشر.

Body:
لوحاتك ممتلئة والمؤشرات في مكانها، لكن القرار لا يحدث. (data-driven tuned line)
المشكلة غالبا ليست في كمية البيانات، بل في السؤال الذي تطرحه عليها.

البيانات تكشف ما حدث، لا الخطوة التالية. السؤال الأفضل هو ما يحول الرقم إلى قرار.

أعددنا لك ملخص الحملة التسويقية: صفحة عملية تساعدك تنتقل من قراءة المؤشر إلى بناء القرار. وهي مدخلك إلى طريقة تفكير إلدا في الصف.

CTA: احصل على الملخص التسويقي
URL: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing

---

#### E2-P2: Self-taught builders (tuned line: make people care)

- id: email-e2-p2-builders
- segment: persona-2-self-taught-builders
- language: ar
- sequence: nonpayer
- objective: conversion
- send_trigger: behavior-triggered, about 2 to 3 days after E1 on "opened E1, not started"
- subject_ref: subj-e2-p2

Subject line A (primary): بنيت منتجا رائعا، فلماذا الصمت؟
Subject line B: المهارة التي لا يعلمها أحد: أن تجعل الناس تهتم
Preheader: حمّل ملخص الحملة التسويقية، وابدأ تحول منتجك إلى قصة يختارها الناس.

Body:
لم يصمت السوق لأن منتجك ضعيف، بل لأن أحدا لا يعرف بعد لماذا يهمه. (self-taught builder tuned line)
قضيت شهورا تبني، ودقائق تكتب النص. والناس يرون النص أولا.

المهارة الناقصة ليست ميزة جديدة، بل أن تجعل الناس تهتم. أن تحول ما بنيته إلى قصة يختارونها.

أعددنا لك ملخص الحملة التسويقية: نقطة بداية عملية لتروي منتجك بوضوح. وهي مدخلك إلى طريقة تفكير إلدا في الصف.

CTA: احصل على الملخص التسويقي
URL: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing

---

#### E2-P3: Skilled-but-stuck executors (tuned line: strategy over features)

- id: email-e2-p3-stuck
- segment: persona-3-skilled-but-stuck-executors
- language: ar
- sequence: nonpayer
- objective: conversion
- send_trigger: behavior-triggered, about 2 to 3 days after E1 on "opened E1, not started"
- subject_ref: subj-e2-p3

Subject line A (primary): تتقن الأدوات، فلماذا توقف النمو؟
Subject line B: لا تنقصك ميزة جديدة، بل استراتيجية أقوى
Preheader: حمّل ملخص الحملة التسويقية، وابنِ الطبقة التي تقف فوق إتقان الأدوات.

Body:
تعرف الأدوات وأطلقت الحملات، لكن النمو توقف عند حد. (skilled-but-stuck tuned line)
الجهد كله عند مستوى الميزة، والحركة لا تحدث.

ما ينقص ليس أداة جديدة، بل الاستراتيجية التي تقرر إلى أين توجه الأدوات. التسويق هو الفرق بين أن تُشاهد وأن تُختار.

أعددنا لك ملخص الحملة التسويقية: صفحة عملية تنقلك من التنفيذ إلى الاتجاه. وهي مدخلك إلى طريقة تفكير إلدا في الصف.

CTA: احصل على الملخص التسويقي
URL: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing

---

### E3: The senior voice, why it differs from free content

- id: email-e3-seniorvoice
- segment: all three personas (shared credential message)
- language: ar
- sequence: nonpayer
- objective: conversion (moves the contact from free content to this senior frame; CTA: start Chapter 1)
- send_trigger: behavior-triggered, about 2 to 3 days after E2 on "engaged but not started";
  layered on the time-based foundation
- subject_ref: subj-e3

Subject line A (primary): خبرة 20 سنة في صف واحد
  - length: 22 characters; key word "خبرة 20 سنة" front-loaded
Subject line B: ما لا يمنحه لك المحتوى المجاني
Preheader: ليست نصائح متفرقة، بل طريقة تفكير من أعلى مستوى تسويقي في المنطقة.

Body:
المحتوى المجاني وفير: منشورات ومقاطع ونصائح بلا نهاية. لكنه نادرا ما يعطيك طريقة تفكير متكاملة.

الفرق هنا هو الصوت. أكثر من 20 سنة على رأس أعقد العمل التسويقي في المنطقة، بصفة إلدا شقير الرئيسة التنفيذية لمجموعة أومنيكوم ميديا في الشرق الأوسط وشمال إفريقيا، ملخصة في صف واحد.

ليست نصيحة اليوم، بل إطار يبقى معك: كيف يقرر الناس، وكيف تبني كل شيء حول تلك اللحظة.

ابدأ بالفصل الأول مجانا، واحكم بنفسك على الفرق.

CTA: شاهد الفصل الأول مجانا
URL: https://member.maharat.com/ar/class/elda-choucair-teaches-marketing

---

### E4: The decision moment, soft CTA toward subscribing

- id: email-e4-decision
- segment: all three personas (shared decision message)
- language: ar
- sequence: nonpayer
- objective: conversion (soft, empowering nudge toward a subscription; generic plan reference, no price)
- send_trigger: behavior-triggered, about 2 to 3 days after E3 on "started Chapter 1 or
  downloaded the cheatsheet, not yet subscribed"; layered on the time-based foundation
- subject_ref: subj-e4

Subject line A (primary): ماذا ستفكر وتفعل بشكل مختلف؟
Subject line B: من فكرة واحدة إلى طريقة عمل كاملة
Preheader: أكمل الصف، واجعل هندسة القرار طريقتك في كل حملة قادمة.

Body:
بعد الفصل الأول، يتغير شيء بسيط: تتوقف عن سؤال "كيف أصل لأكبر عدد؟" وتبدأ بسؤال "كيف يقرر الناس، وكيف أجعل قرارهم أنا؟"

هذه ليست حملة واحدة، بل طريقة تنظر بها إلى كل قرار تسويقي بعدها.

أكمل الصف مع اشتراكك في ماهرات، وحوّل هذه الفكرة إلى طريقة عمل ثابتة. تتعلم على وقتك، خطوة بعد خطوة.

CTA: أكمل الصف باشتراكك
URL: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing

Note: this CTA is intentionally generic (no price, no plan name, no promotion). It stays an
open item until price/plan/promotion are confirmed. See open items.

---

### E5: Last call, warm re-entry for never-engaged

- id: email-e5-lastcall
- segment: owned-recency-cut (tuned for never-engaged across personas 1 to 3)
- language: ar
- sequence: nonpayer (closing message; warm re-entry for the never-engaged tier per the recency cut)
- objective: conversion (a warm, empowering last touch; one low-friction action: start Chapter 1 free)
- send_trigger: behavior-triggered, near the end of the flight on "never engaged across the
  flow"; warm re-entry, not a hard deadline; layered on the time-based foundation
- subject_ref: subj-e5

Subject line A (primary): فكرة واحدة قد تغير طريقة تسويقك
Subject line B: الفصل الأول ما زال بانتظارك، مجانا
Preheader: لا ضغط ولا موعد نهائي، فقط درس واحد يبدأ متى ما كنت جاهزا.

Body:
ربما لم يكن الوقت مناسبا، وهذا طبيعي تماما.

الفكرة التي يبدأ بها هذا الصف بسيطة وتبقى معك: التسويق هو كيف يختارك الناس. وأفضل طريقة لتختبرها هي الفصل الأول، وهو مجاني.

بلا التزام، ابدأ من حيث أنت، ومتى ما كنت جاهزا.

CTA: شاهد الفصل الأول مجانا
URL: https://member.maharat.com/ar/class/elda-choucair-teaches-marketing

Note: empowering last call by design. No hype phrasing like "آخر فرصة", no false deadline.

---

## B. PAID AD COPY (3 concepts, one per persona) - Meta / Instagram

Sized for Meta and Instagram feed. Each concept: primary text, headline, one CTA. Arabic-first,
Elda hook patterns. No price, no spend figure, no lesson count. CTA button maps to Meta's
standard "Learn More" intent ("اعرف المزيد") routing to the class page, except where the free
chapter is the action ("شاهد الآن"). fills map to the creative-package ad slots once staged.

---

### AD-1: Data-driven marketers (hook: pain-question + myth-flip)

- id: ad-p1-datadriven-v1
- segment: persona-1-data-driven-marketers
- language: ar
- cta: اعرف المزيد
- fills: meta-feed-1x1.primary_text, meta-feed-1x1.headline (creative-package, when staged)

Primary text:
قمعك التسويقي نظيف، والمؤشرات في مكانها، ومع ذلك لا أحد يشتري.
المشكلة ليست في كمية البيانات، بل في السؤال الذي تطرحه. البيانات تكشف ما حدث، لا الخطوة التالية.
في صف "إلدا شقير، تعلّم التسويق" تتعلم كيف تحول الرقم إلى قرار، من رئيسة تنفيذية بخبرة أكثر من 20 سنة في المنطقة. الفصل الأول مجاني.

Headline: لا تنقصك بيانات أكثر، بل أسئلة أفضل

---

### AD-1b: Data-driven marketers (alt hook: credential-drop, for test)

- id: ad-p1-datadriven-v2
- segment: persona-1-data-driven-marketers
- language: ar
- cta: شاهد الآن
- fills: meta-feed-1x1.primary_text, meta-feed-1x1.headline (creative-package, when staged)

Primary text:
خبرة أكثر من 20 سنة على رأس التسويق في المنطقة، ملخصة في صف واحد.
البيانات تريك الماضي، لكن القرار يحتاج سؤالا أفضل. تعلم كيف تقرأ ما بين الأرقام، لا أن تجمع المزيد منها.
ابدأ بالفصل الأول من صف إلدا شقير، مجانا.

Headline: التسويق هندسة قرار، لا لوحة مؤشرات

---

### AD-2: Self-taught builders (hook: provocation + direct-promise)

- id: ad-p2-builders-v1
- segment: persona-2-self-taught-builders
- language: ar
- cta: اعرف المزيد
- fills: meta-feed-1x1.primary_text, meta-feed-1x1.headline (creative-package, when staged)

Primary text:
منافسك ليس أفضل منك، هو فقط يروي قصته أفضل.
قضيت شهورا تبني المنتج، ودقائق تكتب النص التسويقي، والناس يرون النص أولا.
في صف "إلدا شقير، تعلّم التسويق" تتعلم كيف تجعل الناس تهتم، وكيف تحول ما بنيته إلى قصة يختارونها. الفصل الأول مجاني.

Headline: لا تفشل لأن منتجك ضعيف، بل لأن أحدا لا يعرف به

---

### AD-2b: Self-taught builders (alt hook: pain-question, for test)

- id: ad-p2-builders-v2
- segment: persona-2-self-taught-builders
- language: ar
- cta: شاهد الآن
- fills: meta-feed-1x1.primary_text, meta-feed-1x1.headline (creative-package, when staged)

Primary text:
أطلقت منتجك، وانتظرت، فجاء الصمت. فلماذا؟
لأن أفضل القصص تكسب، لا أفضل الأفكار. والمهارة التي لا يعلمها أحد هي أن تجعل الناس تهتم.
ابدأ بالفصل الأول من صف إلدا شقير، الرئيسة التنفيذية لمجموعة أومنيكوم ميديا، مجانا.

Headline: اجعل الناس تهتم بما بنيته

---

### AD-3: Skilled-but-stuck executors (hook: myth-flip + everything-is-marketing)

- id: ad-p3-stuck-v1
- segment: persona-3-skilled-but-stuck-executors
- language: ar
- cta: اعرف المزيد
- fills: meta-feed-1x1.primary_text, meta-feed-1x1.headline (creative-package, when staged)

Primary text:
السوق لا يكافئ أفضل منتج، بل المنتج الذي يعرف كيف يتكلم.
تتقن الأدوات وأطلقت الحملات، لكن النمو توقف عند حد. ما ينقص ليس ميزة جديدة، بل استراتيجية أقوى.
في صف "إلدا شقير، تعلّم التسويق" تتعلم الطبقة التي تقف فوق الأدوات: التسويق هو الفرق بين أن تُشاهد وأن تُختار. الفصل الأول مجاني.

Headline: لا تنقصك ميزة، بل استراتيجية

---

### AD-3b: Skilled-but-stuck executors (alt hook: direct-promise, for test)

- id: ad-p3-stuck-v2
- segment: persona-3-skilled-but-stuck-executors
- language: ar
- cta: شاهد الآن
- fills: meta-feed-1x1.primary_text, meta-feed-1x1.headline (creative-package, when staged)

Primary text:
في هذا الصف تتعلم كيف يتخذ الناس قراراتهم، وكيف تجعل قرارهم أنت.
الأدوات تنفذ، لكن الاستراتيجية تقرر إلى أين توجهها. هذه هي الطبقة التي تحرك النمو من جديد.
ابدأ بالفصل الأول من صف إلدا شقير، مجانا، واحكم بنفسك.

Headline: من إتقان الأدوات إلى وضوح الاتجاه

---

## C. ORGANIC SOCIAL CAPTIONS (4 posts for the owned following)

For the owned ~180,000 following. Each post routes to the class page (the signup gate / class
page). One clear CTA per post. Arabic-first, Elda voice. No price, no spend figure, no lesson
count. Lead with the hook, not the brand. (Posting is a gated action; nothing auto-publishes.)

---

### POST-1: Myth-flip (broad, decision-architecture angle)

- id: post-1-mythflip
- segment: all personas (broad owned reach)
- language: ar
- cta: ابدأ بالفصل الأول مجانا عبر الرابط في الملف الشخصي
- routes_to: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing

Caption:
السوق لا يكافئ أفضل منتج، بل المنتج الذي يعرف كيف يتكلم.

التسويق ليس قائمة تكتيكات، بل هندسة قرار: أن تفهم كيف يختار الناس، وأن تبني كل شيء حول تلك اللحظة.

في صف "إلدا شقير، تعلّم التسويق" تتعلم هذه الطريقة في التفكير من رئيسة تنفيذية بخبرة أكثر من 20 سنة في المنطقة.

ابدأ بالفصل الأول مجانا عبر الرابط في الملف الشخصي.

---

### POST-2: Pain-question (data-driven persona lean)

- id: post-2-painquestion
- segment: persona-1-data-driven-marketers (lean)
- language: ar
- cta: شاهد الفصل الأول مجانا، الرابط في الملف الشخصي
- routes_to: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing

Caption:
كل شيء جاهز: البيانات والقمع التسويقي والمؤشرات. فلماذا لا أحد يشتري؟

لأن البيانات تكشف ما حدث، لا الخطوة التالية. ما يصنع الفرق هو سؤال أفضل، لا بيانات أكثر.

هذا ما يعلمه صف "إلدا شقير، تعلّم التسويق": كيف تحول الرقم إلى قرار.

شاهد الفصل الأول مجانا، الرابط في الملف الشخصي.

---

### POST-3: Provocation (self-taught builder lean)

- id: post-3-provocation
- segment: persona-2-self-taught-builders (lean)
- language: ar
- cta: ابدأ بالفصل الأول مجانا عبر الرابط في الملف الشخصي
- routes_to: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing

Caption:
منافسك ليس أفضل منك، هو فقط يروي قصته أفضل.

تبني المنتج في شهور، وتكتب النص في دقائق. والناس يرون النص أولا.

المهارة الناقصة ليست ميزة جديدة، بل أن تجعل الناس تهتم. تعلمها في صف "إلدا شقير، تعلّم التسويق".

ابدأ بالفصل الأول مجانا عبر الرابط في الملف الشخصي.

---

### POST-4: Credential-drop (broad, senior-voice angle)

- id: post-4-credential
- segment: all personas (broad owned reach)
- language: ar
- cta: شاهد الفصل الأول مجانا، الرابط في الملف الشخصي
- routes_to: https://www.maharat.com/ar/class/business/elda-choucair-teaches-marketing

Caption:
خبرة أكثر من 20 سنة مع أكبر العلامات في المنطقة، ملخصة في صف واحد.

إلدا شقير، الرئيسة التنفيذية لمجموعة أومنيكوم ميديا في الشرق الأوسط وشمال إفريقيا، تعلمك كيف يقرر الناس، وكيف تبني تسويقك حول تلك اللحظة.

ليست نصائح متفرقة، بل طريقة تفكير تبقى معك.

شاهد الفصل الأول مجانا، الرابط في الملف الشخصي.

---

## D. LANDING PAGE COPY BLOCKS

For the class / conversion page (RTL). Hero, subhead, 3 value blocks, one primary CTA. No
price (price/plan/promotion are ASSUMPTION). Arabic-first, Elda voice.

- id: lp-elda-marketing
- segment: all personas (the shared landing experience)
- language: ar

LP-hero (headline):
التسويق هندسة قرار

LP-subhead:
تعلّم كيف يختار الناس، وكيف تبني كل شيء حول تلك اللحظة. أكثر من 20 سنة من خبرة إلدا شقير في صف واحد. الفصل الأول مجاني.

LP-value-1 (the senior voice):
صوت من أعلى مستوى
خبرة إلدا شقير، الرئيسة التنفيذية لمجموعة أومنيكوم ميديا في الشرق الأوسط وشمال إفريقيا، أكثر من 20 سنة من أعقد العمل التسويقي في المنطقة، ملخصة بوضوح.

LP-value-2 (frameworks, not tactics):
طريقة تفكير، لا قائمة تكتيكات
تتعلم إطارا يبقى معك: كيف يقرر الناس، ولماذا تكسب أفضل القصص لا أفضل الأفكار. وضوح في الحكم، لا نصائح متفرقة.

LP-value-3 (start free):
ابدأ بلا التزام
الفصل الأول مجاني، وملخص الحملة التسويقية بانتظارك. اختبر الفرق بنفسك قبل أي خطوة.

LP-primary-CTA: شاهد الفصل الأول مجانا
URL: https://member.maharat.com/ar/class/elda-choucair-teaches-marketing

Note: the page presents no price, plan name, or promotion. Any subscribe / pricing block and
its CTA wording stay an open item for conversion-engineer until price/plan/promotion are
confirmed. The free-chapter CTA above is the confirmed, low-friction primary action.

---

## subject_lines[] (paired sets, for the email assets)

Each set: several options, exactly one primary, with the deliberate preheader. Paired by
email_ref. Western numerals only, no em dash, no tatweel.

- id: subj-e1
  email_ref: email-e1-hook
  options:
    - text: التسويق ليس قائمة تكتيكات، بل هندسة قرار    language: ar    primary: true
    - text: درس واحد يغير طريقة تفكيرك في التسويق        language: ar    primary: false
    - text: كيف يختارك الناس؟ ابدأ من هنا                language: ar    primary: false
  primary: التسويق ليس قائمة تكتيكات، بل هندسة قرار
  preheader: صف إلدا شقير على ماهرات. الفصل الأول مجاني، ابدأ من فكرة واحدة تبقى معك.

- id: subj-e2-p1
  email_ref: email-e2-p1-datadriven
  options:
    - text: قمعك التسويقي نظيف، فلماذا لا أحد يشتري؟    language: ar    primary: true
    - text: لا تنقصك بيانات أكثر، بل أسئلة أفضل          language: ar    primary: false
    - text: حوّل المؤشر إلى قرار                          language: ar    primary: false
  primary: قمعك التسويقي نظيف، فلماذا لا أحد يشتري؟
  preheader: حمّل ملخص الحملة التسويقية، ثم شاهد كيف تفكر إلدا في القرار لا في المؤشر.

- id: subj-e2-p2
  email_ref: email-e2-p2-builders
  options:
    - text: بنيت منتجا رائعا، فلماذا الصمت؟              language: ar    primary: true
    - text: المهارة التي لا يعلمها أحد: أن تجعل الناس تهتم    language: ar    primary: false
    - text: حوّل منتجك إلى قصة يختارها الناس            language: ar    primary: false
  primary: بنيت منتجا رائعا، فلماذا الصمت؟
  preheader: حمّل ملخص الحملة التسويقية، وابدأ تحول منتجك إلى قصة يختارها الناس.

- id: subj-e2-p3
  email_ref: email-e2-p3-stuck
  options:
    - text: تتقن الأدوات، فلماذا توقف النمو؟            language: ar    primary: true
    - text: لا تنقصك ميزة جديدة، بل استراتيجية أقوى      language: ar    primary: false
    - text: الفرق بين أن تُشاهد وأن تُختار              language: ar    primary: false
  primary: تتقن الأدوات، فلماذا توقف النمو؟
  preheader: حمّل ملخص الحملة التسويقية، وابنِ الطبقة التي تقف فوق إتقان الأدوات.

- id: subj-e3
  email_ref: email-e3-seniorvoice
  options:
    - text: خبرة 20 سنة في صف واحد                      language: ar    primary: true
    - text: ما لا يمنحه لك المحتوى المجاني                language: ar    primary: false
    - text: ليست نصائح متفرقة، بل طريقة تفكير            language: ar    primary: false
  primary: خبرة 20 سنة في صف واحد
  preheader: ليست نصائح متفرقة، بل طريقة تفكير من أعلى مستوى تسويقي في المنطقة.

- id: subj-e4
  email_ref: email-e4-decision
  options:
    - text: ماذا ستفكر وتفعل بشكل مختلف؟                language: ar    primary: true
    - text: من فكرة واحدة إلى طريقة عمل كاملة            language: ar    primary: false
    - text: اجعل هندسة القرار طريقتك                    language: ar    primary: false
  primary: ماذا ستفكر وتفعل بشكل مختلف؟
  preheader: أكمل الصف، واجعل هندسة القرار طريقتك في كل حملة قادمة.

- id: subj-e5
  email_ref: email-e5-lastcall
  options:
    - text: فكرة واحدة قد تغير طريقة تسويقك              language: ar    primary: true
    - text: الفصل الأول ما زال بانتظارك، مجانا            language: ar    primary: false
    - text: ابدأ من حيث أنت، متى ما كنت جاهزا            language: ar    primary: false
  primary: فكرة واحدة قد تغير طريقة تسويقك
  preheader: لا ضغط ولا موعد نهائي، فقط درس واحد يبدأ متى ما كنت جاهزا.

---

## fills (which asset_brief slots each unit fills)

The creative-package asset_briefs are not yet in hand at this stream, so ad and landing fills
name the intended slot by convention; conversion-engineer, paid-build, and creative confirm the
exact slot ids when the creative-package lands.

- Emails E1 to E5 and their subject sets: consumed by lifecycle-architect (stream 7) into the
  non-payer flow; no creative-overlay slot (email body, not an image overlay).
- AD-1/1b, AD-2/2b, AD-3/3b: fill meta-feed-1x1.primary_text and .headline per concept; map to
  story 9x16 and reel variants in build by reusing the same primary_text and headline.
- POST-1 to POST-4: organic captions for organic-social; route to the class page; no overlay slot.
- LP-hero, LP-subhead, LP-value-1/2/3, LP-primary-CTA: fill the conversion page copy blocks for
  conversion-engineer (stream 6).

---

## Open items (carried to the human gate)

1. PRICE, PLAN, PROMOTION (ASSUMPTION, blocking the conversion CTA specifics). No number, plan
   name, or discount appears anywhere in this package. The subscribe CTA in E4 ("أكمل الصف
   باشتراكك") and the landing page's subscribe/pricing block stay generic until Ahmed confirms
   price, plan structure (1/3/12 vs class/6/12), and whether any promotion exists. The
   free-chapter CTA is the confirmed primary action meanwhile.
2. GATE / CRM PLATFORM (OPEN ITEM, blocking send). The email platform is unconfirmed (Ortto vs
   HubSpot, Arabic RTL concern). The flow copy is written and ready, but nothing sends until the
   platform is named. Surfaced for lifecycle-architect and the human gate.
3. SUCCESS-METRIC TARGET AND DATE (ASSUMPTION). Not supplied; not a copy variable, but it gates
   measurement of this flow. Carried forward.
4. CREATIVE-PACKAGE ASSET_BRIEF SLOT IDS. Not yet in hand. Ad and landing fills name slots by
   convention; exact slot ids confirmed when the creative-package lands (creative, paid-build,
   conversion-engineer).
5. CTA LINK TARGETS AT THE GATE. CTAs point to the confirmed class page and member Chapter 1
   URLs. The eventual subscribe/checkout target depends on the plan and platform decisions
   above; that link stays an open item for conversion-engineer.
6. FORMAL CATALOG STATUS FOR ELDA (OPEN ITEM). Naming her for this published class is allowed
   (public class page). Formal catalog confirmation still pending; surfaced at the human gate.
7. EN MERGE. The EN variants (copy-package.en.md, copywriter-en) merge with this Arabic package
   at the single QA gate; this package is the primary.

---

## Pre-handoff self-check (against the evals)

- 04-copywriting / email-copy / subject-lines / ad-copy skill evals: self-checked.
- One clear CTA per email and per ad variant. Subject sets each carry several options with
  exactly one primary and a deliberate preheader (40 to 90 chars) that adds a promise.
- Primary subjects front-load the key word; E1 (42 chars) and E3 (22 chars) sit in band, others
  hold the mobile-justified bar.
- At least two ad variants per persona (v1 + v2).
- No em dash, no tatweel, Western numerals only, RTL-safe Arabic.
- No invented price, plan, promotion, lesson list, duration, lesson count, or instructor claim.
  Verified title only. No accreditation implication.
- Held-back absent: no "100 plus brands", no spend/dollar figure, no Cannes.
- Empowering throughout; the villain is the safe forgettable strategy, never the reader.
- Next gate: arabic-copy-qa, then brand-qa-reviewer alongside compliance-privacy-reviewer.
