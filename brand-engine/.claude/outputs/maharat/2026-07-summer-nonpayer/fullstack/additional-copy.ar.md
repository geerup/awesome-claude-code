# Additional copy package (AR): Summer of Skills, the four deferred deliverables

Arabic-primary copy for campaign_id 2026-07-summer-nonpayer. Authored by copywriter-ar. This
file carries the four Arabic copy deliverables the gates flagged as "still to produce":
onboarding O1 to O3, the three missing organic gap captions, the signup-gate consent copy, and
the Arabic press release. It is the companion to copy-package.ar.md (the canonical AR copy,
ids E1 to E5, S1 to S8, AD-*, PUSH-*, LP-*) and continues its id schemes. Reasoning only.
Nothing here sends, publishes, or spends.

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: copywriter-ar
- stream: 4 copywriting
- status: draft
- qa:
  - skill_eval: pending (04-copywriting, plus email-copy for onboarding, subject-lines for the
    onboarding subjects, ad-copy register for captions; the consent copy is checked for one clear
    action and the four required disclosure elements)
  - arabic_qa: pass (self-run mechanical scan, copywriter-ar, 2026-06-12, pre-gate). Full scan
    clean across every section of this file:
    - no em dash and no en dash anywhere (commas, colons, periods only);
    - no tatweel or kashida (U+0640) in any Arabic string;
    - Western numerals only (the only digits used are 3, 7, 2023, 200000, 1.5, 100, all Western;
      no Eastern Arabic-Indic digit U+0660 to U+0669 anywhere);
    - one clear CTA or one clear action per asset (each onboarding email one CTA, each caption
      one CTA, each consent line one action point to the policy plus one opt-out instruction,
      the press release carries no CTA as a press asset and ends on a clean destination URL);
    - empowering throughout, never deficit-framed (onboarding leads with "you are in" and what
      the reader will build; the last-call register is absent here because these are
      post-conversion and acquisition assets);
    - gendered reader address held: inclusive plural for onboarding (mixed new-subscriber base),
      inclusive plural for the breadth and poll captions, feminine retained only where a beauty
      or styling field leads; the acting caption uses plural or masculine per the acting posture
      in copy-package.ar.md;
    - title pattern "[الاسم] يعلّم/تعلّم [الموضوع]" agrees with the instructor gender where a class
      title is referenced.
    This is a self-run pre-gate pass. It still routes to arabic-copy-qa as the gate of record,
    and the consent copy routes to compliance-privacy-reviewer first.
  - compliance: pending (compliance-privacy-reviewer). Required for section 3, the gate-consent
    copy (GATE-CONSENT-EMAIL-AR, GATE-CONSENT-WHATSAPP-AR), before any live gate use, per
    conversion-package sections 3.2 and 3.3 and compliance-verdict Open Item 5. The press release
    distribution (section 4) also routes to compliance-privacy-reviewer per pr-package section 5.
  - brand_qa: pending (brand-qa-reviewer, last, alongside compliance-privacy-reviewer)
- entry_points: B owned audience (onboarding, post-conversion lifecycle), C organic social
  (gap captions), 6 conversion path (gate consent), PR and comms (press release). These four
  deliverables feed four different downstream packages, mapped in the fills and routing note.
- open_items: see the per-section open items and the consolidated list at the end. None buried.
- brief_refs:
  - offer_framing: value-led, breadth-led, the free first chapter as the low-friction try
    (strategy s.4.2). No price, promotion, or plan length in any onboarding body, caption, or
    press paragraph.
  - price: ASSUMPTION, not stated anywhere in this file (strategy s.4.2, s.6).
  - promotion: ASSUMPTION, posture value-led, none stated or implied (strategy s.4.2, s.6).
  - plan: ASSUMPTION, no plan length stated in any body (strategy s.4.2, s.6).
  - instructors: naming confirm-at-gate for the seven, cleared page-sourced facts only. Section
    2 names Kosai Khauli (acting): "one of the biggest names in the Arab world, teaching the
    fundamentals of acting and expression" (kosai-khauli/profile.md, live class page 2026-06-05,
    cleared). Section 4 names all seven with their cleared lines, each flagged confirm-at-gate.
    The four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam) are never
    named and appear only inside "والمزيد عبر مجالات عديدة".
  - excluded (NOT used anywhere): Toufic's Brands For Less name and the $10,000-garage detail;
    Elda's Omnicom, Forbes, Cannes, and the 900-plus and 1000-plus figures. Also excluded: the
    "bootstrapped" / funding fact from the catalog (public, but a funding reference, so out per
    the no-fundraising guardrail). Co-founder names are carried as a confirm-at-gate option in
    the boilerplate, not asserted (pr-package open item 8).
  - AR spelling note: this file holds to the AR spellings already QA-passed in copy-package.ar.md
    (سلام دقاق, إلدا شقير, قصي خولي, بسام فتوح, راغب علامة, توفيق كريديه, سيدريك حداد), not the
    working transliterations in _CATALOG.md, for cross-asset consistency. If official campaign
    assets confirm a different spelling, swap it in.

## Angle served (locked, inherited)

"هذا الصيف، اختر مجالك وابنِ مهارة حقيقية مع نخبة من يصنعون المعيار." Breadth-led, value-led,
empowering. The onboarding extends it past the conversion: now you are in, the breadth is the
ongoing reason to keep going. The captions close the three open organic gaps on the same angle.
The consent copy is plain and honest, not a sales surface. The press release tells the breadth
story on public, cleared facts only.

---

## 1. Onboarding (post-conversion) . entry B lifecycle . segment: new subscribers . ids ONBOARD-O1 to O3

Post-conversion welcome sequence for contacts who fire subscription_start and exit the non-payer
flow (lifecycle-package section 5). Three touches: O1 immediate, O2 day 3, O3 day 7. Cadence is
ASSUMPTION, confirm with Ahmed (lifecycle open item 7). Each carries a subject (primary plus one
alternative), a preheader, a body of two to four short lines, and one clear CTA. Inclusive plural
address, because the new-subscriber base is mixed and the value is breadth-led. No price, no plan
length, no promotion in any body. The plan is already chosen at this point; onboarding never
re-sells it. No chapter count or lesson title stated. Named instructors are not used in the
onboarding bodies, so no confirm-at-gate dependency sits inside the welcome flow; the breadth is
referenced by field only.

### ONBOARD-O1 . trigger: subscription_start (fires immediately) . goal: welcome and orient, "you are in"
- audience: new subscribers, all. send_trigger: event-based, on subscription_start.
- ONBOARD-SUBJECT-O1 (primary): أهلاً بك، أنت الآن جزء من مهارات
- ONBOARD-SUBJECT-O1-alt: وصولك مفتوح، فلنبدأ مهارتك الأولى
- ONBOARD-PREHEADER-O1: اختر مجالك الأول وابدأ بدرس قصير اليوم، كل المجالات بين يديك.
- ONBOARD-BODY-O1:
أهلاً بك في مهارات.
وصولك أصبح مفتوحاً، وكل المجالات بين يديك الآن، تتعلمها من نخبة يصنعون المعيار.
ابدأ بالمجال الذي يشدّك أكثر، ودرس أول قصير يفتح لك الطريق.
كل خطوة تقرّبك من مهارة تبقى معك.
- ONBOARD-CTA-O1: ابدأ مهارتك الأولى
- language: ar
- gender: inclusive plural.
- note: a welcome, not a receipt. Orients to the breadth and invites the first session in a field
  of the subscriber's choice (lifecycle O1 direction). No price or plan; the subscription is
  already active.

### ONBOARD-O2 . trigger: day 3 after subscription_start . goal: first progress nudge, pick a field, momentum
- audience: new subscribers, day 3. send_trigger: time-based, 3 days after subscription_start.
- ONBOARD-SUBJECT-O2 (primary): خطوة واحدة تصنع البداية
- ONBOARD-SUBJECT-O2-alt: اختر مجالك، وابنِ زخمك الأول
- ONBOARD-PREHEADER-O2: درس قصير واحد يكفي لتشعر بالفرق، والمجال الذي تختاره هو نقطة انطلاقك.
- ONBOARD-BODY-O2:
كل مهارة كبيرة تبدأ بخطوة صغيرة.
اختر مجالاً واحداً يهمّك، وابدأ بدرسه الأول، فالبداية الواضحة تصنع الزخم.
حين تنهي درسك الأول، يصبح الثاني أقرب وأسهل.
أنت تملك الوقت هذا الصيف، فلنحوّله إلى تقدّم حقيقي.
- ONBOARD-CTA-O2: تابع من حيث بدأت
- language: ar
- gender: inclusive plural.
- note: first-session momentum framing. If first-session data is available the platform may
  acknowledge progress; copy is written to work whether or not that data is present (lifecycle O2
  direction). Empowering, skill-momentum, never "you have not started yet."

### ONBOARD-O3 . trigger: day 7 after subscription_start . goal: habit formation, a small step a day, breadth ahead
- audience: new subscribers, day 7. send_trigger: time-based, 7 days after subscription_start.
- ONBOARD-SUBJECT-O3 (primary): درس قصير كل يوم، مهارة تكبر معك
- ONBOARD-SUBJECT-O3-alt: مجال جديد بانتظارك حين تكون جاهزاً
- ONBOARD-PREHEADER-O3: العادة الصغيرة تصنع المهارة الكبيرة، وأمامك مجالات عديدة لتكتشفها.
- ONBOARD-BODY-O3:
المهارة لا تُبنى دفعة واحدة، بل بدرس قصير كل يوم.
خصّص دقائق ثابتة لمجالك، وستفاجئك المسافة التي تقطعها في أسبوع.
وحين تتقن مجالك الأول، هناك مجالات عديدة أخرى تنتظرك، كلها ضمن اشتراكك.
الطريق أمامك واسع، وأنت تختار وجهته.
- ONBOARD-CTA-O3: اكتشف مجالاً جديداً
- language: ar
- gender: inclusive plural.
- note: habit-formation and breadth-ahead framing (lifecycle O3 direction). Surfaces a second
  field as a discovery prompt. References breadth by field only, no cleared instructor name needed
  inside onboarding, so no naming dependency. Not salesy, practical and confident.

---

## 2. Organic gap captions . entry C organic . segment: new acquisition . ids SOCIAL-S9 to S11

The three gaps flagged in organic-package (open items table and input validation): no dedicated
AR variant for the acting field (T2-ACT, used by ORG-S-05 and ORG-S-18), the interactive-poll
story (T7, used by ORG-S-02 and ORG-S-16), or the free-chapter entry-point story (T3, used by
ORG-S-11). Canonical organic captions run S1 to S8 in copy-package.ar.md, so these continue the
series as S9, S10, S11. Caption plus one CTA each. No price, no promo, no plan length, no chapter
count. The poll is a participation post and carries a soft tap-prompt, not a hard conversion CTA,
per the T7 brief.

### SOCIAL-S9 . acting (Kosai Khauli) . fills: ORG-S-05 (feed), ORG-S-18 (Reel) . closes the T2-ACT gap
أحد أبرز الأسماء في العالم العربي يفتح لك باب التمثيل.
هذا الصيف، تعلّم أساسيات التمثيل والتعبير مع قصي خولي، وكيف تحوّل الإحساس إلى أداء يُقنع.
ابدأ بالدرس الأول مجاناً، واكتشف الممثّل في داخلك.
- SOCIAL-CTA-S9: شاهد الدرس المجاني
- language: ar
- gender: plural or masculine (acting is not a beauty or styling category, matching the AD-ACTING-1
  posture in copy-package.ar.md).
- facts: cleared, page-sourced only (kosai-khauli/profile.md, live class page 2026-06-05): "one of
  the biggest names in the Arab world, teaching the fundamentals of acting and expression." No
  chapter count, no lesson title, no private-work or filmography detail. Naming confirm-at-gate; if
  not cleared at the gate, the post drops to the unnamed breadth without rewriting the angle.
- note: title pattern reference if a display title is needed is "قصي خولي يعلّم التمثيل" (يعلّم,
  masculine, agreeing with the instructor).

### SOCIAL-S10 . interactive poll story (T7) . fills: ORG-S-02, ORG-S-16 . closes the poll gap
أي مهارة ستبني هذا الصيف؟
صيف واحد يكفي لتبدأ مهارة تبقى معك، فأخبرنا من أين تبدأ.
صوّت لمجالك، وشاهد ما يختاره الآخرون.
- on-screen poll prompt (sticker, not baked into the art): أي مهارة ستبني هذا الصيف؟
- poll options (sticker text, one per field, the seven cleared fields): الموسيقى . الطبخ . التمثيل
  . المكياج . الأعمال . التنسيق . التسويق
- SOCIAL-CTA-S10 (soft, story tap-prompt, not a hard conversion CTA): اختر مجالك
- language: ar
- gender: inclusive plural (platform-level participation post).
- note: participation post, the goal is signal and warm-audience data, not conversion (T7 brief).
  No external destination on this post; it routes to no gate. No baked poll text in the art; the
  options live in the interactive sticker. The four non-nameable instructors are not surfaced; the
  options are fields, not people. The "والمزيد عبر مجالات عديدة" breadth is implied by the seven
  field options and is not a poll choice.

### SOCIAL-S11 . free-chapter entry-point story (T3) . fills: ORG-S-11 . closes the free-chapter story gap
المجال الذي طالما أردت إتقانه، تبدأه اليوم بخطوة واحدة.
لا حاجة لخبرة سابقة، ولا للبحث في مصادر متفرقة.
درس أول مجاني، من نخبة يصنعون المعيار، في المجال الذي تختاره.
الخطوة الأولى مجانية، وبين يديك الآن.
- SOCIAL-CTA-S11: ابدأ درسك المجاني
- language: ar
- gender: inclusive plural (entry-point story serving the whole breadth).
- note: low-friction try, one free lesson, pick a field (T3 brief). Routes to the signup gate via
  the story link sticker. No price or plan. Echoes the live-site accessibility line "ليس هناك أي
  خبرة سابقة مطلوبة" in spirit without copying it verbatim.
- open_item: lands on the signup gate (link sticker); gate_platform unconfirmed, gated action
  blocked, surfaces at the human gate. No personal data in the URL.

---

## 3. Gate-consent copy . entry 6 conversion path . ids GATE-CONSENT-EMAIL-AR, GATE-CONSENT-WHATSAPP-AR

The consent line shown before submit at the signup gate (conversion-package sections 3.2 and 3.3).
Each variant states who collects the data (مهارات / Maharat), the purpose, a visible link to the
privacy policy (clear placeholder, no invented URL), and the opt-out mechanism (unsubscribe for
email, a clear stop word for WhatsApp). Concise and plain, not a sales surface, one clear action
point. No PII is collected beyond email or phone plus an optional first name, and the copy says no
more than that. These route to compliance-privacy-reviewer and then arabic-copy-qa before any live
gate use; the WhatsApp variant additionally depends on the consent-logging mechanism
(compliance-verdict Open Item 2) which is not copy and not authored here.

### GATE-CONSENT-EMAIL-AR . email gate variant (conversion-package section 3.2)
بالمتابعة، أنت توافق على أن تتواصل معك مهارات عبر البريد الإلكتروني برسائل عن المنصة والمجال الذي تختاره. نستخدم بريدك الإلكتروني واسمك الأول إن أضفته فقط لهذا الغرض. يمكنك إلغاء الاشتراك في أي وقت عبر الرابط في أسفل كل رسالة. اطّلع على [سياسة الخصوصية] لمعرفة كيف نحمي بياناتك.
- slot: GATE-CONSENT-AR (email variant), conversion-package section 2.3 consent line and 3.2.
- language: ar
- elements present, mapped to the compliance requirement (conversion-package 3.2 a to d):
  - (a) who and purpose: "تتواصل معك مهارات ... برسائل عن المنصة والمجال الذي تختاره" (controller
    named: مهارات; purpose: platform and chosen-field messages).
  - data minimization stated: "نستخدم بريدك الإلكتروني واسمك الأول إن أضفته فقط لهذا الغرض" (email
    plus optional first name only, the exact fields the gate collects, nothing more).
  - (c) opt-out: "يمكنك إلغاء الاشتراك في أي وقت عبر الرابط في أسفل كل رسالة" (unsubscribe via the
    link in every message).
  - (b) visible policy link: "[سياسة الخصوصية]" as a clear placeholder for the live link, shown
    inline before submit, never hidden behind a scroll or collapse.
- placeholder: "[سياسة الخصوصية]" binds to the live Maharat privacy-policy URL at build. No URL is
  invented here. The live policy must be confirmed to cover PDPL elements (compliance-verdict Open
  Item 9) before this link is relied on.
- note: visible before submit (conversion-package 2.4 checklist, compliance-verdict Open Item 5).
  Plain, one action (read the policy) plus one standing opt-out instruction. No PII in any URL.

### GATE-CONSENT-WHATSAPP-AR . WhatsApp gate variant (conversion-package section 3.3)
بالمتابعة، أنت توافق على أن تراسلك مهارات عبر واتساب برسائل عن المنصة والمجال الذي تختاره. نستخدم رقمك واسمك الأول إن أضفته فقط لهذا الغرض. لإيقاف الرسائل في أي وقت، أرسل كلمة "إيقاف". اطّلع على [سياسة الخصوصية] لمعرفة كيف نحمي بياناتك.
- slot: GATE-CONSENT-AR (WhatsApp variant), conversion-package section 3.3.
- language: ar
- elements present, mapped to the WhatsApp requirement (conversion-package 3.3 a to e):
  - (a) explicit WhatsApp reference: "تراسلك مهارات عبر واتساب" (names the channel as WhatsApp, not
    a generic "messages from Maharat"), controller named مهارات, purpose stated.
  - data minimization stated: "نستخدم رقمك واسمك الأول إن أضفته فقط لهذا الغرض" (phone plus optional
    first name only).
  - (b) stop mechanism: "لإيقاف الرسائل في أي وقت، أرسل كلمة \"إيقاف\"" (a clear Arabic stop word,
    إيقاف).
  - visible policy link: "[سياسة الخصوصية]" inline before submit.
- placeholder: "[سياسة الخصوصية]" binds to the live Maharat privacy-policy URL at build. The stop
  word "إيقاف" must match what the WhatsApp platform actually honors; confirm the exact keyword
  with the platform at wiring (it may also accept an English "Stop").
- note: visible before submit (conversion-package 3.3 c). The consent must be logged with a
  timestamp and consent-text version at submission (conversion-package 3.3 d, compliance-verdict
  Open Item 2); that logging is a mechanism, not copy, and is owned by conversion-engineer and
  lifecycle-architect under compliance-privacy-reviewer, not authored here. No PII in any URL.
- open_item: gate_platform unconfirmed; the WhatsApp variant is used only if WhatsApp is the
  confirmed gate. Both variants stay blocked from live use until compliance-privacy-reviewer
  clears them and the platform is named.

---

## 4. Press release (AR) . PR and comms . id PR-RELEASE-AR

The Arabic press release, drafted to the pr-package section 3 brief. Arabic is primary, not a
translation. Headline, dateline placeholder, lead, body (the campaign, the breadth across the
seven named cleared fields, the free first chapter, the value-led summer framing), a clearly
marked quote placeholder, and a boilerplate on public press facts only. All seven instructor names
are flagged confirm-at-gate inline. Excluded entirely: the four non-nameable instructors, Toufic's
Brands For Less and garage detail, Elda's Omnicom/Forbes/Cannes/figures, any price, any promotion,
any accreditation claim, any roadmap or Skill Paths reference, and the catalog's "bootstrapped" /
funding fact (public, but a funding reference, so out per the no-fundraising guardrail). No CTA, as
a press asset; it ends on a clean destination URL.

### PR-RELEASE-AR

العنوان:
مهارات تطلق "صيف المهارات": سبعة مجالات مع نخبة من يصنعون المعيار، والدرس الأول مجاني

العنوان الفرعي:
الموسيقى، الطبخ، التمثيل، المكياج، الأعمال، التنسيق، والتسويق، كلها على منصة واحدة هذا الصيف.

سطر التاريخ والمكان:
[المدينة]، [التاريخ]:

الفقرة الافتتاحية (الخبر):
أطلقت مهارات، المنصة العربية الأولى للتطوير الذاتي، حملتها الصيفية "صيف المهارات"، داعيةً المتعلمين في العالم العربي إلى بناء مهارة حقيقية هذا الصيف في مجال يختارونه. تجمع الحملة سبعة مجالات على منصة واحدة، الموسيقى والطبخ والتمثيل والمكياج والأعمال والتنسيق والتسويق، يقدّمها نخبة من الخبراء في العالم العربي. ويبدأ كل صف من هذه الصفوف بدرس أول مجاني، فالخطوة الأولى في متناول الجميع.

الفقرة الثانية (المجالات والخبراء، الأسماء confirm-at-gate قبل التوزيع):
يتعلّم المشتركون من نخبة يصنعون المعيار في مجالاتهم، كلٌّ في صفّه المنشور على المنصة:
- راغب علامة [confirm-at-gate]: أربعون عاماً في عالم الموسيقى، يشارك للمرة الأولى طريقه نحو احتراف الموسيقى.
- سلام دقاق [confirm-at-gate]: أفضل طاهية في الشرق الأوسط، وصاحبة مطعم بيت مريم الحائز على نجمة ميشلان، تعلّم الطبخ الشامي.
- قصي خولي [confirm-at-gate]: أحد أبرز الأسماء في العالم العربي، يعلّم أساسيات التمثيل والتعبير.
- بسام فتوح [confirm-at-gate]: أحد أبرز خبراء المكياج وأكثرهم طلباً في المنطقة، يعلّم فن المكياج.
- توفيق كريديه [confirm-at-gate]: بنى عملاً بمليارات الدولارات من الصفر، يعلّم بناء الأعمال وتنميتها.
- سيدريك حداد [confirm-at-gate]: مصمم إطلالات يثق به ألمع نجوم العالم العربي، يعلّم التنسيق الشخصي.
- إلدا شقير [confirm-at-gate]: من أبرز قادة التسويق في العالم العربي، بخبرة عقود في صناعة علامات تجارية أيقونية، تعلّم التسويق.
وإلى جانب هذه الصفوف، تضم المنصة المزيد عبر مجالات عديدة.

الاقتباس (placeholder، موافقة المتحدّث مطلوبة قبل التوزيع):
[QUOTE: SPOKESPERSON NAME, approval required before distribution]

الفقرة الثالثة (الوصول):
تتوفّر صفوف "صيف المهارات" عبر اشتراك في مهارات على maharat.com، حيث يمكن للمتعلمين أن يبدؤوا بالدرس الأول المجاني في أي مجال، ثم يتابعوا عبر المجالات كلها. تمنح مهارات شهادة إتمام مخصصة باسم المتعلم توثّق رحلته.

نبذة عن مهارات (boilerplate، حقائق عامة فقط):
مهارات منصة عربية أولاً للتطوير الذاتي في العالم العربي، تقدّم صفوفاً احترافية (Masterclasses) من نخبة الخبراء في المنطقة، وخطط اشتراك للمتعلمين الناطقين بالعربية في الخليج والعالم العربي. انطلقت المنصة عام 2023، وجذبت أكثر من 200000 متابع على منصات التواصل وأكثر من 1.5 مليون زائر فريد لموقعها، بمستخدمين في أكثر من 100 دولة. تمنح مهارات شهادات إتمام، وهذه الشهادات غير معتمدة.

سطر التواصل الإعلامي:
[MEDIA CONTACT NAME], [MEDIA CONTACT EMAIL]

- language: ar
- facts and sourcing:
  - platform facts from _CATALOG.md (Entrepreneur, Aug 2025) and pr-package section 2: Arabic-first
    self-development platform, launched 2023, masterclasses from regional experts, 200000-plus
    social followers, 1.5 million-plus unique visitors, users in 100-plus countries. These public
    figures are carried but are themselves confirm-at-gate per pr-package; they are public press
    facts, used as the boilerplate baseline.
  - per-instructor lines are the cleared, page-sourced credentials from pr-package section 3 and
    the profiles; Kosai Khauli's line is from kosai-khauli/profile.md (live class page 2026-06-05).
    Each name carries an inline [confirm-at-gate] flag that the gate owner removes on clearance or
    that triggers a field-only descriptor if a name is not cleared at distribution.
  - certificate framed as "شهادة إتمام مخصصة باسم المتعلم ... غير معتمدة" (the live-site "شهادة مخصصة
    باسمك" pattern), never accredited.
- excluded, confirmed absent:
  - the four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam): not named;
    only "المزيد عبر مجالات عديدة".
  - Toufic: no Brands For Less, no $10,000-garage detail; only "بنى عملاً بمليارات الدولارات من الصفر".
  - Elda: no Omnicom, no Forbes, no Cannes, no 900-plus or 1000-plus figures; only "من أبرز قادة
    التسويق في العالم العربي، بخبرة عقود في صناعة علامات تجارية أيقونية".
  - no price, no promotion, no plan length.
  - no accreditation claim.
  - no Skill Paths, no roadmap, no unannounced plans.
  - no "bootstrapped" or any funding or investor reference (public, but excluded per the
    no-fundraising guardrail and the explicit task instruction).
- open_items:
  - co-founder naming in the boilerplate (Arman Khederlarian, Bassem Jamaleddine): deliberately NOT
    asserted in the draft above; pr-package open item 8 carries it as confirm-at-gate. If approved,
    add "أسّسها عام 2023 [co-founder names]" to the boilerplate; if not, the boilerplate stands as
    written without naming individuals.
  - dateline [المدينة]، [التاريخ]: placeholder; no date distributed without Ahmed's confirmation
    (schedule ASSUMPTION, pr-package open item 3 and 4).
  - quote: placeholder only; approval required before distribution (pr-package open item 2).
  - media contact line: placeholder; replaced by the approved contact before distribution
    (pr-package open item 7, compliance-verdict Open Item 11).
  - the public figures (200000-plus, 1.5 million-plus, 100-plus) are confirm-at-gate per pr-package;
    confirm before distribution.

---

## Fills and routing note (which downstream package each section feeds)

| Section | New ids | Feeds (downstream package) | Binds to |
|---|---|---|---|
| 1. Onboarding | ONBOARD-O1, O2, O3 (subject primary + alt, preheader, body, CTA each) | lifecycle-package section 5 (onboarding O1 to O3 shape) | lifecycle O1 immediate, O2 day 3, O3 day 7 message slots |
| 2. Gap captions | SOCIAL-S9 (acting), SOCIAL-S10 (poll), SOCIAL-S11 (free-chapter story) | organic-package post calendar | S9 to ORG-S-05 and ORG-S-18; S10 to ORG-S-02 and ORG-S-16; S11 to ORG-S-11 |
| 3. Gate consent | GATE-CONSENT-EMAIL-AR, GATE-CONSENT-WHATSAPP-AR | conversion-package section 7 signup gate | GATE-CONSENT-AR slot, email variant (3.2) and WhatsApp variant (3.3) |
| 4. Press release | PR-RELEASE-AR | pr-package press_release_ref (section 3 brief) | the AR press release asset, body paragraphs 1 to 3, boilerplate, contact line |

Routing of record:
- Onboarding (section 1): copywriter-ar draft, then arabic-copy-qa, then brand-qa-reviewer
  alongside compliance-privacy-reviewer. Advances the lifecycle onboarding flow to qa-passed only
  when O1 to O3 carry arabic-copy-qa and brand-qa pass (lifecycle section 5, gate package item 1).
  Onboarding does not send until the subscription platform is named and Ahmed approves the
  onboarding sequence separately (lifecycle section 8).
- Gap captions (section 2): copywriter-ar draft, then arabic-copy-qa, then brand-qa. On pass, the
  organic post calendar unblocks ORG-S-05, ORG-S-18 (acting), ORG-S-02, ORG-S-16 (poll), and
  ORG-S-11 (free-chapter story), which were carried as open items (organic-package open items
  table). Nothing publishes; the organic package stops at the human gate.
- Gate consent (section 3): routes to compliance-privacy-reviewer first (the consent disclosure is
  the compliance-critical element), then arabic-copy-qa, then brand-qa. The consent line is not
  used in any live gate until compliance-privacy-reviewer clears it, arabic-copy-qa passes, and the
  gate platform is confirmed (compliance-verdict Open Item 5, conversion-package section 7).
- Press release (section 4): copywriter-ar draft, then arabic-copy-qa, then brand-qa, with
  compliance-privacy-reviewer on distribution and journalist-data handling (pr-package section 5,
  compliance-verdict Open Item 11). The EN counterpart, if in scope, is authored by copywriter-en
  and merges at the same gate. Nothing distributes until the date, the quote, the names, and the
  contact line are confirmed at the human gate.

## Consolidated open items (carried, none buried)

- gate_platform OPEN ITEM: SOCIAL-S11 (story link sticker) and both gate-consent variants land on
  or describe the signup gate; gated action blocked until the email, WhatsApp, and signup-gate
  platforms are confirmed. The WhatsApp consent variant is used only if WhatsApp is the confirmed
  gate.
- consent compliance review: GATE-CONSENT-EMAIL-AR and GATE-CONSENT-WHATSAPP-AR route to
  compliance-privacy-reviewer before any live use (compliance-verdict Open Item 5). The WhatsApp
  consent-logging mechanism (timestamp and consent-text version) is a separate, non-copy
  dependency owned downstream (compliance-verdict Open Item 2).
- privacy-policy link: "[سياسة الخصوصية]" in both consent variants is a placeholder for the live
  URL, bound at build; the live policy must be confirmed to cover PDPL elements
  (compliance-verdict Open Item 9). No URL invented. No PII in any URL.
- WhatsApp stop word: "إيقاف" must match the keyword the WhatsApp platform honors; confirm at wiring.
- per-instructor public-naming confirm-at-gate (the seven): every named reference in SOCIAL-S9
  (Kosai Khauli) and in the press release uses cleared, page-sourced facts only and carries
  confirm-at-gate. If a name is not cleared at the gate, SOCIAL-S9 drops to the unnamed breadth and
  the press release substitutes a field-only descriptor (pr-package section 4).
- four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam): never named;
  not surfaced anywhere in this file. Confirmed across all four sections.
- excluded verify-before-public-use facts: Toufic's Brands For Less and garage detail, Elda's
  Omnicom/Forbes/Cannes/900-plus/1000-plus, not used anywhere.
- excluded funding reference: the catalog "bootstrapped" / funding fact is public but excluded per
  the no-fundraising guardrail; absent from the press release.
- co-founder naming (press boilerplate): carried as confirm-at-gate, not asserted in the draft
  (pr-package open item 8).
- press public figures (200000-plus, 1.5 million-plus, 100-plus countries): carried as
  confirm-at-gate per pr-package; confirm before distribution.
- dateline, quote, media-contact line in the press release: placeholders; none distributed without
  Ahmed's confirmation (pr-package open items 2, 3, 4, 7).
- price ASSUMPTION: no price in any onboarding body, caption, consent line, or press paragraph.
- promotion ASSUMPTION: none stated or implied anywhere.
- plan ASSUMPTION: no plan length in any body.
- cadence ASSUMPTION: onboarding O1 immediate, O2 day 3, O3 day 7 are proposed; confirm with Ahmed
  (lifecycle open item 7).
- gendered address: inclusive plural across onboarding, the poll, and the free-chapter story;
  plural or masculine on the acting caption per the acting posture. Flagged for arabic-copy-qa to
  confirm the split holds per surface.
- no personal or sensitive data in any URL or tracking parameter on any gate-landing CTA or in the
  press-release destination URL.

## Pre-handoff checklist

- one clear CTA or action per asset: yes. Each onboarding email one CTA; each caption one CTA (the
  poll carries a soft tap-prompt by design, not a hard conversion CTA); each consent line one
  policy-link action plus one standing opt-out instruction; the press release carries no CTA as a
  press asset and ends on a clean destination URL.
- no em dash or en dash anywhere: yes. No tatweel or kashida: yes. Western numerals only: yes (the
  only digits used are 3, 7, 2023, 200000, 1.5, 100, all Western).
- empowering, never deficit-framed: yes. Onboarding leads with "you are in" and what the reader
  will build; the captions lead with the field and the free first step; no shaming, no "you have
  not started."
- no invented offer, price, promotion, plan length, Skill Path title, lesson, count, quote, or
  instructor name: yes. Cleared, page-sourced credibility facts only. The press quote is a marked
  placeholder. No accreditation implication anywhere.
- instructor-naming discipline: SOCIAL-S9 (Kosai Khauli) and the seven names in the press release
  carried confirm-at-gate with cleared facts only; the four non-nameable instructors never named;
  Toufic's and Elda's verify-before-use facts excluded; the funding reference excluded.
- consent copy completeness: each variant names the controller (مهارات), the purpose, a visible
  policy-link placeholder, the data minimization (email or phone plus optional first name only),
  and the opt-out (unsubscribe for email, the stop word إيقاف for WhatsApp). Routed to
  compliance-privacy-reviewer first.
- Arabic-first MSA with Gulf-familiar wording, Thmanyah tone, RTL-safe: yes. Gendered address by
  category applied and flagged.

Status: draft. Self-run arabic_qa pass recorded above (2026-06-12, pre-gate). This file now routes
per section: arabic-copy-qa on all four sections; compliance-privacy-reviewer first on the
gate-consent copy and on press distribution; then brand-qa-reviewer last. On a gate fail the
affected section returns here with the exact fix list and is regenerated against it. On pass, the
four deliverables advance to their downstream packages (lifecycle onboarding, organic calendar,
conversion gate, pr-package press_release_ref) per the routing note. Nothing sends, publishes, or
spends.
