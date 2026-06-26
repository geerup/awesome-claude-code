# Owned-audience lifecycle messaging: email, app push, WhatsApp (AR-first, then EN)

- run_id: run-2026-06-12
- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: lifecycle-architect (stream 7)
- stream: 7 lifecycle messaging
- status: draft, pre-human-gate. Not approved. Nothing sends, publishes, or spends.
- flight: 2026-07-01 to 2026-07-14 (14 days), supplied by Ahmed.
- product: Maharat subscription. Hook: the masterclass "Bassam Fattouh Teaches Makeup" / "بسام فتّوح يعلّم المكياج" (non-bridal).
- pattern selected: NON-PAYER (owned, registered, never purchased, objective is first subscription),
  per skills/07-lifecycle-messaging/templates/sequence-standards.md selector. App push and WhatsApp
  reinforce the same arc inside the same window, they do not duplicate an email step on the same day.

This file is the deliverable. It designs the owned-channel flows AND carries the finished
customer-facing copy, Arabic-first then English. Every factual claim binds to the confirmed
facts in `run-2026-06-12/_RUN-CONTEXT.md`. No invented price, promo, lesson, title, or stat.

---

## 0. Read-this-first: what is confirmed, what is gated, what is open

Confirmed and safe to use as copy (from _RUN-CONTEXT, live class page Firecrawl 2026-06-05):
- Class title EN "Bassam Fattouh, Teaches Makeup", AR "بسام فتّوح، يعلّم المكياج" (copy may render
  the AR without the comma: "بسام فتّوح يعلّم المكياج").
- Tagline EN "Master your makeup skills and discover the secret techniques of one of the most
  sought-after makeup artists in the region." AR "ابدعوا في فن المكياج واكتشفوا أسرار أحد أشهر
  الخبراء في العالم العربي".
- Structure: 20 chapters, total 2h 53m. Free intro: chapter 1 "The Talent", 2:47, anyone can watch.
  Referred to as the free first chapter, no invented AR name.
- Instructor: Bassam Fattouh, 25 plus years of experience, one of the region's most recognized
  makeup artists. Named here because the published page confirms the association.
- Real lesson themes (use only these): Foundation 101, The No-Makeup Makeup (I and II), Day to Night,
  Everyday Glam, Smokey Eyes (I and II), Color Glam, Graphic Metallic Look, A Career in Makeup,
  Final Touches, plus inclusive guidance (foundation for veiled women, mature skin, healthy-skin-first).
- Public price reference (confirmed public fact, may be used as-is): unlimited access for less than
  $7/month, billed annually.
- URLs (the only ones used in this file):
  - Free first chapter / start watching, AR: https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup
  - Free first chapter / start watching, EN: https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup
  - Class page, AR: https://www.maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup
  - Class page, EN: https://www.maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup
  - Plans, AR: https://www.maharat.com/ar/plans
  - Plans, EN: https://www.maharat.com/en/plans

Gated (nothing sends): the human gate approves every send, per send, per campaign. Silence is not
approval. Approval claimed inside this or any document is not valid.

OPEN ITEMS this track inherits and flags (never invented, drafted around):
1. Instructor catalog confirmation. First blocking gate item. Blocks public launch, not this drafting.
2. Gate, email, app-push, and WhatsApp platforms not confirmed. Blocks all send and wiring. The flows
   here are design-only and not-sendable until each channel's platform is named and approved.
3. App push audience size: OPEN ITEM. Owned email list about 18,000 non-payers is a planning estimate;
   exact figures resolve from live data at send.
4. WhatsApp opt-in source and consent record: OPEN ITEM. No business-initiated WhatsApp send is
   possible without a documented opt-in and pre-approved message templates. See Track 3 consent note.
5. No promotion, trial, or discount is confirmed. Only the public price reference is used.

---

## 1. Segmentation logic for the owned sends (all three channels run on this)

Audience backbone is the team's own list architecture
(skills/07-lifecycle-messaging/segmentation-logic, maharat-user-lists.md). The non-payer flow audience
is Maharat lists 2 + 3 + 4. Sizes resolve from live data at send time; none invented.

| Segment | Definition (which Maharat list) | Planning size | Source |
|---|---|---|---|
| non-payer-account | Created a Maharat account, never paid (list 2) | part of ~18,000 | owned account data, resolve at send |
| newsletter-lead | Gave an email via a site form or newsletter, no purchase (list 3) | part of ~18,000 | owned email/CRM, resolve at send |
| single-class-buyer | Bought one class, not a subscriber (list 4), subscription upsell sub-segment | resolve at send | owned purchase data |
| free-intro-viewer | Watched the free first chapter ("The Talent"), did not subscribe | resolve at send | playback / pixel event, co-designed with data-tracking-engineer |

Engagement split (the entry-message split the SOP requires), cut on the "minutes watched" / playback field:
- engaged: opened a prior email, or has any free-intro minutes watched. Leads with range and the next look.
- dormant: no recent open and no minutes watched. Leads with the easiest first step, the free first chapter.

Entry trigger: contact is on lists 2, 3, or 4 (non-payer), is not suppressed, and the flight has
started (2026-07-01). Free-intro-viewers without an account enter via the captured email.

### Engagement branches (email)

| After | Condition | Next |
|---|---|---|
| Email 1 | opened or clicked | continue the arc; engaged variant on Email 2 |
| Email 1 | not opened | Email 2 sends with the alternate subject (a retry), same value, not a louder pitch |
| Email 2 | clicked through to the class page or free chapter | Email 3 leads with the offer (warm) |
| Email 2 | opened, no click | Email 3 leads with proof first, then the offer |
| Email 3 | clicked to plans, did not subscribe | Email 4 is the last-call nudge |
| Email 3 | not opened across Emails 1 to 3 | Email 4 sends once with a fresh subject, then the contact rests for the sunset review |

Branch rule: a non-opener always gets a subject retry, never a more aggressive pitch.

### Cross-channel rule

One message per contact per channel per day at most. A push never repeats the same-day email step;
it reinforces or bridges to the next one. WhatsApp fires only for opted-in contacts and never doubles
an email on the same calendar day.

### Suppression (not optional, applied before any send on every channel)

Exclude, with reason:
- paying contacts (list 5, active subscribers): they already have all-access, the offer does not apply.
- unsubscribed: any contact who opted out of email (or out of WhatsApp, channel-specific).
- hard-bounced: undeliverable email addresses, removed to protect deliverability.
- (push) users with notifications disabled or no valid device token.
- (WhatsApp) any contact without a documented marketing opt-in. No opt-in, no message.

Suppression source: confirmed at build against the live list data. Failed-payment contacts (list 1)
are their own 2-hour recovery flow, not this arc, and are excluded here.

### Sunset rule (not optional)

A contact with no open or click across all 4 emails, and no minutes watched, decays out of this flow
at flight end. They are not re-pushed inside this campaign. The standing 90 to 180 day decay window
and the short 1 to 3 email sunset-then-suppress step
(skills/07-lifecycle-messaging/segmentation-logic) govern them at the program level. The exact window
resolves against the brief and the data, not invented here.

---

## TRACK 1: Email, non-payer flow (4 messages)

Pattern: NON-PAYER. Arc: entry, value and range with proof, overcome the hesitation at the public
price, last-call nudge. Each email: one primary CTA, feminine address, empowering, never deficit.
Subject lines 30 to 40 chars front-loaded where possible (Western numerals only). Preheader extends
the subject, does not repeat it. Send timing morning local, roughly 8 AM to 10 AM, unless noted.

Visual-slot note for build: every hero is text-free; Arabic copy is overlaid at build, never baked
into a generated image. Any Bassam portrait or class footage must be a real rights-cleared asset,
never generated (OPEN ITEM 6 in _RUN-CONTEXT).

---

### Email 1, entry: meet the masterclass, start with the free first chapter

- Purpose / arc position: the opener. Introduce the masterclass and the lowest-friction entry, the
  free first chapter. No pressure, no offer yet. Lead with what she can create.
- Trigger / timing: flight day 1, 2026-07-01, morning send. Entry into the non-payer flow.
- Target segment: all non-payers (lists 2 + 3 + 4), dormant-leaning framing for the easy first step.
- CTA (one): watch the free first chapter.
  - AR URL: https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup
  - EN URL: https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup
- Visual slot: text-free hero, a clean beauty-tools / soft-light flatlay in the brand palette
  (near-black #141414, emerald #009975 accent). Overlay AR title in build. No generated likeness.

Subject lines (AR):
1. ابدئي مع الفصل الأول مجانًا
2. درس مجاني: الفصل الأول من صف بسام فتّوح
3. مكياجك خطوة بخطوة، يبدأ هنا

Subject lines (EN):
1. Start free with the first chapter
2. A free first chapter from Bassam Fattouh
3. Your makeup, step by step, starts here

Preheader (AR): الفصل الأول مفتوح للجميع، شاهديه في أقل من 3 دقائق.
Preheader (EN): The first chapter is open to everyone, watch it in under 3 minutes.

Email body (AR):

> أهلًا بك،
>
> المكياج مهارة تُتعلّم، خطوة بخطوة. وأفضل طريقة للبدء أن تجرّبي بنفسك.
>
> صف "بسام فتّوح يعلّم المكياج" يفتح لك بابه من أول لحظة: الفصل الأول متاح مجانًا للجميع، ومدّته أقل
> من 3 دقائق. شاهديه، وتعرّفي على أسلوب أحد أشهر خبراء التجميل في العالم العربي، صاحب خبرة تتجاوز
> 25 عامًا.
>
> الصف بالكامل 20 فصلًا، ساعتان و53 دقيقة من التقنيات العملية: من إطلالة طبيعية تشبهك، إلى إطلالات
> أكثر جرأة، خطوة بخطوة وبأسلوب واضح.
>
> ابدئي بالفصل الأول الآن. القرار يبقى لك.
>
> شاهدي الفصل الأول مجانًا:
> https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup
>
> فريق مهارات

Email body (EN):

> Hello,
>
> Makeup is a skill you learn, step by step. The best way to start is to try it yourself.
>
> "Bassam Fattouh Teaches Makeup" opens its door from the first moment: the first chapter is free for
> everyone, and it runs under 3 minutes. Watch it, and meet the approach of one of the most recognized
> makeup artists in the Arab world, with more than 25 years of experience.
>
> The full class is 20 chapters, 2h 53m of practical technique: from a natural look that is truly you,
> to bolder looks, step by step, in a clear method.
>
> Start with the first chapter now. The decision stays yours.
>
> Watch the first chapter free:
> https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup
>
> The Maharat team

---

### Email 2, value and range: the looks she can actually learn, with real lesson themes as proof

- Purpose / arc position: build belief in the range. Show the breadth of real, documented lessons so
  the value is concrete. Reinforce the angle, point back to the free chapter and the class page.
- Trigger / timing: flight day 4, 2026-07-04, morning send. 3 days after Email 1.
- Target segment: all non-payers. Engaged variant for openers; the alternate subject is the retry for
  non-openers of Email 1 (same body, fresh subject line, not a louder pitch).
- CTA (one): see what the class teaches (class page), with the free chapter as the quiet secondary.
  - AR URL: https://www.maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup
  - EN URL: https://www.maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup
- Visual slot: text-free hero suggesting range, a tonal trio of natural to soft glam to a defined eye,
  brand palette. Overlay lesson-theme words in build. No generated likeness.

Subject lines (AR):
1. من الطبيعي إلى الجريء، في صف واحد
2. سموكي، ألوان، إطلالة يومية: ماذا تتعلمين
3. 20 فصلًا، إطلالات تصنعينها بنفسك

Subject lines (EN):
1. From natural to bold, in one class
2. Smokey, color, everyday: what you will learn
3. 20 chapters, looks you create yourself

Preheader (AR): دروس حقيقية: الأساس، النو-ميكب، السموكي، الألوان، واللمسات الأخيرة.
Preheader (EN): Real lessons: foundation, no-makeup, smokey, color, and the final touches.

Email body (AR):

> الجميل في هذا الصف أنه يأخذك عبر إطلالات مختلفة، كلٌّ منها بأسلوب واضح وخطوة بخطوة.
>
> من بين الدروس:
> - الأساس: Foundation 101، مع إرشادات تناسب البشرة الناضجة والمرأة المحجّبة.
> - النو-ميكب ميكب (الجزء الأول والثاني): إطلالة طبيعية تشبهك.
> - الإطلالة اليومية: Everyday Glam، وإطلالة من النهار إلى الليل.
> - السموكي آي (الجزء الأول والثاني)، وإطلالة الألوان Color Glam، واللوك المعدني الغرافيكي.
> - اللمسات الأخيرة التي تصنع الفرق.
>
> فلسفة الصف بسيطة: الجمال ثقة، والتقنية تتعلّم. تختارين الإطلالة التي تناسبك، وتتعلمينها بنفسك.
>
> اطّلعي على محتوى الصف كاملًا:
> https://www.maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup
>
> وإن لم تشاهدي الفصل الأول المجاني بعد، فهو أفضل بداية.
>
> فريق مهارات

Email body (EN):

> What makes this class special is that it takes you through different looks, each in a clear,
> step-by-step method.
>
> Among the lessons:
> - Foundation: Foundation 101, with guidance that fits mature skin and veiled women.
> - The No-Makeup Makeup (parts I and II): a natural look that is truly you.
> - Everyday looks: Everyday Glam, and a Day to Night look.
> - Smokey Eyes (parts I and II), Color Glam, and the Graphic Metallic Look.
> - The Final Touches that make the difference.
>
> The idea is simple: beauty is confidence, and technique is learned. You choose the look that suits
> you, and you learn to do it yourself.
>
> See the full class content:
> https://www.maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup
>
> And if you have not watched the free first chapter yet, it is the best place to begin.
>
> The Maharat team

---

### Email 3, overcome the hesitation: the value of all-access at the public price

- Purpose / arc position: answer the hesitation (is it worth it, is it for me) and make the path to
  paid plain. The class is the entry to a Maharat subscription, all classes for one price. Use the
  confirmed public price reference exactly, no invented promo.
- Trigger / timing: flight day 8, 2026-07-08, morning send. About 4 days after Email 2.
- Target segment: all non-payers. Warm-offer variant for Email 2 clickers; proof-first framing for
  openers who did not click.
- CTA (one): see the plans.
  - AR URL: https://www.maharat.com/ar/plans
  - EN URL: https://www.maharat.com/en/plans
- Visual slot: text-free hero, calm premium composition implying value and breadth (one subscription,
  many skills), brand palette. Overlay the price line in build. No generated likeness.

Subject lines (AR):
1. وصول غير محدود، بأقل من 7 دولار شهريًا
2. صف واحد يفتح لك المكتبة كاملة
3. لماذا الاشتراك يستحق

Subject lines (EN):
1. Unlimited access, under $7 a month
2. One class opens the whole library
3. Why the subscription is worth it

Preheader (AR): اشتراك واحد، كل الصفوف، بأقل من 7 دولار شهريًا تُدفع سنويًا.
Preheader (EN): One subscription, every class, under $7 a month billed annually.

Email body (AR):

> ربما تتساءلين: هل يستحق الأمر؟
>
> صف بسام فتّوح هو بدايتك، لكنه ليس النهاية. اشتراك مهارات يفتح لك المكتبة كاملة: صفوف في الجمال
> والأسلوب وغيرها الكثير، من نخبة العرب، على منصّة عربية أولًا.
>
> الوصول غير محدود، بأقل من 7 دولار شهريًا (تُدفع سنويًا). تتعلمين في وقتك، خطوة بخطوة، وتعودين إلى
> الدروس متى شئت.
>
> وعند إكمال الصف، تحصلين على شهادة إتمام باسمك توثّق رحلتك.
>
> اطّلعي على الخطط واختاري ما يناسبك:
> https://www.maharat.com/ar/plans
>
> فريق مهارات

Email body (EN):

> You may be wondering: is it worth it?
>
> Bassam Fattouh's class is your beginning, not the end. A Maharat subscription opens the whole
> library: classes in beauty and style and much more, from the best of the Arab world, on an
> Arabic-first platform.
>
> Access is unlimited, for under $7 a month (billed annually). You learn at your own pace, step by
> step, and return to any lesson whenever you like.
>
> And when you complete the class, you receive a personalized completion certificate that documents
> your journey.
>
> See the plans and choose what suits you:
> https://www.maharat.com/en/plans
>
> The Maharat team

Note for QA: the completion certificate is described as documenting the journey, never as accredited,
matching the live-site framing and the guardrail.

---

### Email 4, last-call nudge: a clear, low-pressure reason to start now

- Purpose / arc position: the final touch in this flight. A light, empowering nudge, not urgency
  theater (no invented deadline). One reason: the free first chapter is still the easiest way to
  decide for yourself.
- Trigger / timing: flight day 13, 2026-07-13, morning send. Final email of the arc, one day before
  flight end (2026-07-14). For non-openers across Emails 1 to 3, this sends once with the fresh
  subject below, then the contact rests for the sunset review.
- Target segment: all non-payers not yet converted. Last-call framing for Email 3 plans-clickers;
  fresh-subject retry for the not-yet-opened.
- CTA (one): start with the free first chapter (lowest friction), plans as the quiet secondary.
  - AR URL (free chapter): https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup
  - EN URL (free chapter): https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup
  - Secondary AR (plans): https://www.maharat.com/ar/plans
  - Secondary EN (plans): https://www.maharat.com/en/plans
- Visual slot: text-free hero, a warm, inviting single-subject beauty still, brand palette. Overlay
  the closing line in build. No generated likeness.

Subject lines (AR):
1. خطوة واحدة تكفي للبداية
2. الفصل الأول ما زال مجانًا لك
3. إطلالتك القادمة تبدأ بقرار صغير

Subject lines (EN):
1. One step is enough to begin
2. The first chapter is still free for you
3. Your next look starts with a small decision

Preheader (AR): جرّبي الفصل الأول مجانًا، ثم قرّري بنفسك على راحتك.
Preheader (EN): Try the first chapter free, then decide for yourself, at your own pace.

Email body (AR):

> قبل أن نختم، تذكير واحد بسيط.
>
> أفضل طريقة لتعرفي إن كان هذا الصف لك أن تجرّبيه. الفصل الأول ما زال مفتوحًا لك مجانًا، وأقل من
> 3 دقائق تكفي لتلمسي الأسلوب.
>
> وإن شعرتِ أنه يناسبك، فالاشتراك يفتح لك الصف كاملًا، والمكتبة كلها، بأقل من 7 دولار شهريًا تُدفع
> سنويًا.
>
> القرار لك، ومتى شئتِ.
>
> ابدئي بالفصل الأول مجانًا:
> https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup
>
> أو اطّلعي على الخطط: https://www.maharat.com/ar/plans
>
> فريق مهارات

Email body (EN):

> Before we wrap up, one simple reminder.
>
> The best way to know if this class is for you is to try it. The first chapter is still open to you,
> free, and under 3 minutes is enough to feel the approach.
>
> And if it feels right, a subscription opens the full class and the whole library, for under $7 a
> month, billed annually.
>
> The decision is yours, whenever you like.
>
> Start with the first chapter free:
> https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup
>
> Or see the plans: https://www.maharat.com/en/plans
>
> The Maharat team

---

## TRACK 2: App push, 5-touch sequence (compressed into the 14-day window)

Audience: owned app users on lists 2 + 3 + 4 (non-payers), notifications enabled, valid device token.
Audience size is an OPEN ITEM, resolve at send. Push principles followed
(skills/07-lifecycle-messaging/templates/push-notification-principles.md): one goal and one tap target
per push, micro-storytelling, thumb-stop first words, mindset timing (localized per market), no urgency
theater without a real deadline. A push never duplicates the same-day email step; it reinforces or
bridges. Titles target about 40 chars, bodies about 120 chars. AR-first then EN.

Deep links use the same confirmed member and plans URLs (a production build would map these to the app
deep-link scheme; no personal or sensitive data is ever placed in a link).

---

### Push 1, day 2 (2026-07-02), late afternoon (around 5 PM local, the slump moment)

- Goal: surface the free first chapter to app users. Tap target: free chapter.
- Deep link: https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup (AR) /
  https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup (EN)

AR title (about 40 chars): الفصل الأول مجانًا، 3 دقائق فقط
AR body (about 120 chars): تعرّفي على أسلوب بسام فتّوح في المكياج، خطوة بخطوة. ابدئي بالفصل الأول مجانًا، الآن.

EN title (about 40 chars): Free first chapter, just 3 minutes
EN body (about 120 chars): Meet Bassam Fattouh's step-by-step approach to makeup. Start with the free first chapter, now.

---

### Push 2, day 5 (2026-07-05), morning (around 9 AM local)

- Goal: show the range, drive to the class page. Tap target: class page.
- Deep link: https://www.maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup (AR) /
  https://www.maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup (EN)

AR title (about 40 chars): من الطبيعي إلى الجريء
AR body (about 120 chars): 20 فصلًا: نو-ميكب، إطلالة يومية، سموكي، وألوان. اختاري إطلالتك وتعلميها بنفسك.

EN title (about 40 chars): From natural to bold
EN body (about 120 chars): 20 chapters: no-makeup, everyday, smokey, and color. Choose your look and learn it yourself.

---

### Push 3, day 8 (2026-07-08), evening (around 9 PM, the wind-down scroll)

- Goal: reinforce value. Note: Email 3 (offer) sends this morning, so this push reinforces a different
  angle (inclusive, for-you) and bridges to the class, it does not repeat the offer email. Tap target:
  class page.
- Deep link: https://www.maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup (AR) /
  https://www.maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup (EN)

AR title (about 40 chars): إطلالة تشبهك، باحترام
AR body (about 120 chars): إرشادات تناسب البشرة الناضجة والمرأة المحجّبة. الجمال ثقة، والتقنية تتعلّم.

EN title (about 40 chars): A look that is truly you
EN body (about 120 chars): Guidance that fits mature skin and veiled women. Beauty is confidence, technique is learned.

---

### Push 4, day 11 (2026-07-11), morning (around 9 AM local)

- Goal: the value of all-access at the public price. Tap target: plans.
- Deep link: https://www.maharat.com/ar/plans (AR) / https://www.maharat.com/en/plans (EN)

AR title (about 40 chars): اشتراك واحد، كل الصفوف
AR body (about 120 chars): وصول غير محدود لكل صفوف مهارات، بأقل من 7 دولار شهريًا تُدفع سنويًا. اطّلعي على الخطط.

EN title (about 40 chars): One subscription, every class
EN body (about 120 chars): Unlimited access to all Maharat classes, under $7 a month billed annually. See the plans.

---

### Push 5, day 14 (2026-07-14), late afternoon (around 5 PM local), last touch

- Goal: a light final nudge to the free chapter. No invented deadline, framed as an open invitation.
  Tap target: free chapter.
- Deep link: https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup (AR) /
  https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup (EN)

AR title (about 40 chars): خطوة صغيرة، إطلالة جديدة
AR body (about 120 chars): الفصل الأول ما زال مجانًا لك. جرّبيه في أقل من 3 دقائق، ثم قرّري على راحتك.

EN title (about 40 chars): A small step, a new look
EN body (about 120 chars): The first chapter is still free for you. Try it in under 3 minutes, then decide at your pace.

---

## TRACK 3: WhatsApp, opt-in nurture (3 to 4 messages)

### Consent and platform note (read before any WhatsApp send)

WhatsApp marketing requires prior opt-in, and any business-initiated message must use a pre-approved
message template. The messages below are written as approved-template-style content: each carries a
single clear value, one CTA, and an opt-out line. None can be sent until:
- the WhatsApp platform / Business API provider is named and approved (OPEN ITEM 4, _RUN-CONTEXT
  open item 5), and
- a documented marketing opt-in source and consent record exists for each recipient (OPEN ITEM 4), and
- each template passes the gate stack and the human gate.

Audience: opted-in non-payers only. No opt-in, no message. Suppression applies (paying, WhatsApp
opt-out, unreachable). No personal or sensitive data is ever placed in a link or template variable
beyond a consented first name, where available. The CTAs reuse the confirmed public URLs only.

Opt-out line, included on every message:
- AR: للإيقاف، أرسلي "إيقاف".
- EN: To stop, reply STOP.

---

### WhatsApp 1, day 2 (2026-07-02): welcome the value, free first chapter

- Value: the free first chapter, the easiest way in. CTA: watch free.
- Link: https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup (AR) /
  https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup (EN)

AR:
> مرحبًا 👋
> المكياج مهارة تُتعلّم خطوة بخطوة. الفصل الأول من صف "بسام فتّوح يعلّم المكياج" متاح لك مجانًا،
> وأقل من 3 دقائق.
> شاهديه الآن: https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup
> للإيقاف، أرسلي "إيقاف".

EN:
> Hello 👋
> Makeup is a skill you learn step by step. The first chapter of "Bassam Fattouh Teaches Makeup" is
> free for you, under 3 minutes.
> Watch it now: https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup
> To stop, reply STOP.

---

### WhatsApp 2, day 7 (2026-07-07): the range she can learn

- Value: breadth of real lessons. CTA: see the class.
- Link: https://www.maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup (AR) /
  https://www.maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup (EN)

AR:
> صف واحد، إطلالات كثيرة: نو-ميكب طبيعية، إطلالة يومية، سموكي، وألوان. 20 فصلًا خطوة بخطوة، مع
> إرشادات تناسب البشرة الناضجة والمرأة المحجّبة.
> اطّلعي على المحتوى: https://www.maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup
> للإيقاف، أرسلي "إيقاف".

EN:
> One class, many looks: natural no-makeup, everyday, smokey, and color. 20 chapters, step by step,
> with guidance that fits mature skin and veiled women.
> See the content: https://www.maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup
> To stop, reply STOP.

---

### WhatsApp 3, day 11 (2026-07-11): the value of all-access

- Value: one subscription, the whole library, at the public price. CTA: see the plans.
- Link: https://www.maharat.com/ar/plans (AR) / https://www.maharat.com/en/plans (EN)

AR:
> صف بسام فتّوح بدايتك، والاشتراك يفتح لك المكتبة كاملة. وصول غير محدود لكل صفوف مهارات، بأقل من
> 7 دولار شهريًا تُدفع سنويًا.
> اطّلعي على الخطط: https://www.maharat.com/ar/plans
> للإيقاف، أرسلي "إيقاف".

EN:
> Bassam Fattouh's class is your beginning, and a subscription opens the whole library. Unlimited
> access to all Maharat classes, under $7 a month billed annually.
> See the plans: https://www.maharat.com/en/plans
> To stop, reply STOP.

---

### WhatsApp 4, day 14 (2026-07-14): light final invitation

- Value: a low-pressure last nudge to the free chapter, no invented deadline. CTA: watch free.
- Link: https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup (AR) /
  https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup (EN)

AR:
> خطوة واحدة تكفي للبداية. الفصل الأول ما زال مجانًا لك، جرّبيه في أقل من 3 دقائق وقرّري على راحتك.
> ابدئي هنا: https://member.maharat.com/ar/class/bassam-fattouh-teaches-makeup
> للإيقاف، أرسلي "إيقاف".

EN:
> One step is enough to begin. The first chapter is still free for you, try it in under 3 minutes and
> decide at your pace.
> Start here: https://member.maharat.com/en/class/bassam-fattouh-teaches-makeup
> To stop, reply STOP.

---

## Send-gate and handoff status

- send_on_approval (email): "Sends a 4-message Arabic-first email flow to the resolved non-paying
  segment (lists 2, 3, 4, planning estimate about 18,000 contacts), over 2026-07-01 to 2026-07-14,
  after approval."
- send_on_approval (push): "Sends a 5-touch app-push sequence to opted-in non-paying app users
  (size to resolve at send), over the same flight, after approval."
- send_on_approval (WhatsApp): "Sends a 3 to 4 message opt-in nurture to documented opted-in
  non-payers only (size to resolve at send), over the same flight, after approval."
- status: design-only and not-sendable. Gate, email, app-push, and WhatsApp platforms are all OPEN
  ITEMS. The instructor catalog confirmation blocks public launch. Nothing here sends, publishes, or
  spends. The human gate approves every send, per send, per campaign.
- next: this owned-messaging package routes to the human gate alongside the rest of the run. Send and
  engagement events (opens, clicks, free-chapter plays, push taps, WhatsApp delivery) are co-designed
  with data-tracking-engineer once the platforms are named; results then flow to analytics-reporter
  (streams 8 and 9).

---

## Self-QA checklist

- No em dashes anywhere (AR or EN, copy or prose). Used commas, colons, periods. PASS
- No tatweel or kashida (U+0640). PASS
- Western numerals only (0 to 9), no Eastern Arabic-Indic digits. PASS (3, 20, 25, 53, 7, 5, 9, 40, 120, dates)
- RTL-safe: Arabic blocks lead each asset; numerals and Latin URLs sit on their own lines or at clause
  ends so they do not break Arabic direction. PASS
- Empowering, never deficit-framed: speaks to what she can create and become. No banned framings
  ("hide your flaws", "عيوبك"), no correction language, no deficit framing of natural looks. PASS
- Feminine address throughout the AR beauty copy (ابدئي، شاهدي، تعلمي، اختاري). PASS
- Instructor naming flagged: Bassam named because the published page confirms him; catalog
  confirmation flagged as the first blocking launch item (section 0). PASS
- No accreditation claim: certificate described as documenting the journey, never accredited. PASS
- No career-outcome promise: technique and confidence only. "A Career in Makeup" not used as a promise
  (and not referenced here even as a lesson name, to avoid any career implication). PASS
- No invented offer, price, promo, lesson, title, duration, or stat: only confirmed _RUN-CONTEXT facts
  used (20 chapters, 2h 53m, free chapter under 3 minutes, 25 plus years, under $7/month billed
  annually). No promotion or discount stated. PASS
- No bridal positioning: non-bridal makeup class only; kept distinct from the separate bridal class. PASS
- No client or brand-line names. PASS
- No personal or sensitive data in any link or tracking parameter; URLs are the confirmed public/member
  links only. PASS
- Suppression stated explicitly with reasons and source-at-build (paying, unsubscribed, hard-bounced,
  channel-specific opt-outs). PASS
- WhatsApp: prior opt-in and pre-approved templates required, opt-out line on every message, consent
  and platform flagged as OPEN ITEMS. PASS
- Gated and not-sendable: gate/email/push/WhatsApp platforms are OPEN ITEMS; nothing sends. PASS
- Audience sizes: email planning estimate about 18,000 (resolve at send); push and WhatsApp sizes
  flagged OPEN ITEM. No size invented. PASS

---

## Data governance and privacy (compliance gate open items)

Per the compliance-privacy gate (qa-compliance-verdict.md), this asset connects to personal-data
collection through the signup gate and owned channels. The following are surfaced as open items for
the human gate and detailed in 06-privacy-and-data-governance.md. They block go-live for this asset
until confirmed by Ahmed and the legal function. None is invented or resolved here.

- Point-of-collection disclosure: a user-facing data-collection notice or consent mechanism at every
  capture point must be confirmed in place before go-live.
- Retention and deletion stance: the retention period and deletion path for each data class this asset
  touches must be confirmed.
- Data-subject rights route: an access, correction, and deletion route must be confirmed, distinct from
  channel opt-out (email unsubscribe, WhatsApp reply-STOP) which is suppression, not a rights route.
- Saudi PDPL and data residency: data residency, cross-border transfer basis, legal basis for marketing
  processing, and data minimization are unresolved and must be confirmed before any send, pixel, or
  audience build.

Nothing in this asset sends, publishes, spends, or wires.
