# Copy package (Arabic): Skill Paths first-time soft launch

Draft deliverable. Owned by copywriter-ar. Nothing here publishes, sends, or spends. These are
QA-ready Arabic variants that stop at the human gate. Arabic is primary. No em dashes. No
tatweel. Western numerals only. RTL-safe.

## Envelope

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: copywriter-ar
- stream: 4 copywriting
- status: draft (pre-QA). Not yet through arabic-copy-qa, brand-qa-reviewer, or
  compliance-privacy-reviewer. Not approved.
- qa:
  - skill_eval (04-copywriting): self-checked on draft (subject length, one CTA per asset, no
    banned claims). Formal eval pending.
  - arabic_qa: pending (arabic-copy-qa, first gate, all Arabic copy)
  - brand_qa: pending (brand-qa-reviewer, last, alongside compliance-privacy-reviewer)
- language: ar (primary). EN variants are authored by copywriter-en and merge into this
  package at the QA gate.
- brief_refs:
  - offer and offer framing: brief sec 4 (early access, no price required, format and benefit
    only, empowering)
  - angle: strategy-artifact "build a real skill, one small step a day", early-access invitation
  - segments: strategy-artifact segments 1 (owned non-payers), 2 (new acquisition), 3
    (retargeting)
  - constraints: brief sec 8 and CLAUDE.md guardrails
  - reusable input: June social draft (Arabic refined and re-timed where strong)
- price/promotion shown: none. No price or promo is supplied; none appears in any variant.
- dates shown: none. Soft-launch and early-access framing only. No firm public launch date and
  no countdown appears in any variant.

## What changed from the June social draft (and why)

The June Arabic is strong on tone and the hero's-journey arc, and is reused and refined below.
Two things are deliberately removed, not carried forward:

- Seat-cap and scarcity lines ("عدد محدود من المقاعد", "المقاعد تنفد", "المقاعد الأولى تنفد",
  "الدخول المبكر يغلق قريبا"). The early-access seat cap is an OPEN ITEM in the strategy and
  brief: no real cap is confirmed, so "limited seats" and "closing soon" framing is not yet
  truthful and is held. Where the arc needs a close, the variant invites rather than pressures.
  These lines return only if Ahmed confirms a real cap at the gate. Flagged in open_items.
- Any implied firm date or countdown. None appears.

Everything else (format, benefit, small-step and streak motif, completion certificate framed
as a completion mark only) is preserved.

---

## 1. Paid ad copy (entry point A: new acquisition segment 2 and retargeting segment 3)

Each ad lists a primary text and a headline. One CTA per ad. No price, no titles, no date.
CTAs for paid land on the early-access signup gate; the gate platform is an open item, so the
link is blocked (see open_items). Keyword-based organic CTAs are in section 4.

### AR-PAID-01 . segment 2 (new acquisition) . primary text

primary_text:
خطوة صغيرة كل يوم تبني مهارة تبقى معك.
لا محاضرات طويلة، ولا ضغط. دقائق معدودة في اليوم تكفي لتبدأ وتتقدم.
هذه طريقة جديدة للتعلم على مهارات، صممناها لتناسب يومك المزدحم لا أن تزاحمه.
سجل اهتمامك وكن من أوائل من يجربها.

headline: ابن مهارة حقيقية، خطوة كل يوم
cta: سجل اهتمامك
fills: paid acquisition ad, primary text plus headline overlay slot

### AR-PAID-02 . segment 2 (new acquisition) . primary text

primary_text:
النية موجودة، ينقصها طريق واضح.
هنا تتعلم على شكل خطوات قصيرة، تتقدم وتجمع تقدمك يوما بعد يوم.
سلسلة لا تنقطع، وتقدم تشوفه بعينك.
انضم للدخول المبكر وابدأ من أول خطوة.

headline: نيتك بذرة، والطريق يحولها مهارة
cta: انضم للدخول المبكر
fills: paid acquisition ad, primary text plus headline overlay slot

### AR-PAID-03 . segment 3 (retargeting) . primary text

primary_text:
كنت قريبا من البداية، خطوة واحدة تفصلك.
الطريقة بسيطة: خطوة صغيرة كل يوم، تبني فيها مهارة تبقى معك.
الدخول المبكر مفتوح، وانضمامك يبدأ بخطوة واحدة.
أكمل ما بدأته الآن.

headline: خطوة واحدة تفصلك عن البداية
cta: أكمل تسجيلك
fills: paid retargeting ad, primary text plus headline overlay slot

### AR-PAID-04 . segment 3 (retargeting) . short primary text (feed and stories)

primary_text:
الطريقة، لا الوقت.
5 دقائق في اليوم تكفي لتبدأ مهارة وتبني فيها.
الدخول المبكر بانتظارك.

headline: 5 دقائق تكفي لتبدأ
cta: انضم للدخول المبكر
fills: paid retargeting short ad, primary text plus headline overlay slot

Headline bank (paid, overlay slots, pick per asset):
- ابن مهارة حقيقية، خطوة كل يوم
- نيتك بذرة، والطريق يحولها مهارة
- الطريقة، لا الوقت
- خطوة كل يوم تبقى معك
- ابدأ مهارتك التالية اليوم

---

## 2. Early-access email (entry point B: owned non-payers segment 1)

A short early-access flow to owned non-payers. Recently-engaged tier gets the fuller body,
dormant tier a lighter touch. One CTA per email. The gate platform is an open item, so the
actual signup link and any send are blocked (see open_items). Subject lines are honest to the
body, empowering, no clickbait, no price, no date.

### Subject lines

For email AR-EMAIL-01 (recently engaged, invitation):
- primary (chosen): مهارة جديدة تبدأ بخطوة واحدة
- alt: ادخل مبكرا، طريقة جديدة لتتعلم على مهاراتك
- alt: خطوة صغيرة كل يوم، مهارة تبقى معك

For email AR-EMAIL-02 (recently engaged, reminder):
- primary (chosen): الطريق ما زال أمامك، وخطوة واحدة تكفي
- alt: أكمل ما بدأته، الدخول المبكر بانتظارك

For email AR-EMAIL-03 (dormant, light re-engagement):
- primary (chosen): عدنا بطريقة أسهل لتبدأ
- alt: مهارة تبنيها في دقائق يومك

Preheader bank (kept short, honest to body):
- دقائق معدودة في اليوم، وتقدم تشوفه بعينك.
- لا محاضرات طويلة، خطوة واحدة تكفي لتبدأ.

### AR-EMAIL-01 . segment 1 recently engaged . invitation

subject (primary): مهارة جديدة تبدأ بخطوة واحدة
headline: أنت تعرفنا، وهذه أسهل طريقة لتبدأ
body:
سجلت معنا لأنك تريد أن تتعلم، والنية ما زالت موجودة.
اليوم نفتح الدخول المبكر لطريقة جديدة على مهارات: تتعلم على شكل خطوات قصيرة، خطوة كل يوم، وتبني مهارة تبقى معك.
لا محاضرات طويلة، ولا وقت يضيع. دقائق معدودة تكفي لتبدأ، وكل يوم يقربك خطوة.
كن من أوائل من يجرب الطريقة الجديدة.
cta: انضم للدخول المبكر
fills: lifecycle email 1 (segment 1, recently engaged)

### AR-EMAIL-02 . segment 1 recently engaged . reminder

subject (primary): الطريق ما زال أمامك، وخطوة واحدة تكفي
headline: أكمل ما بدأته
body:
بدأت معنا لأنك تريد مهارة جديدة، والطريق ما زال أمامك.
الدخول المبكر للطريقة الجديدة لا يزال مفتوحا، والبداية أبسط مما تظن: خطوة صغيرة كل يوم.
كل خطوة قصيرة تقربك من مهارة تبقى معك، وتجمع تقدمك يوما بعد يوم.
خطوة واحدة الآن، وتبدأ.
cta: انضم للدخول المبكر
fills: lifecycle email 2 (segment 1, recently engaged, reminder)

### AR-EMAIL-03 . segment 1 dormant . light re-engagement

subject (primary): عدنا بطريقة أسهل لتبدأ
headline: طريقة جديدة تناسب يومك
body:
نعرف أن وقتك مزدحم، ولهذا صممنا طريقة جديدة لتتعلم على مهاراتك في دقائق معدودة كل يوم.
خطوة صغيرة، تتكرر، وتبني فيها مهارة تبقى معك.
نفتح الدخول المبكر الآن، وندعوك أن تكون من أوائل من يجربها.
cta: انضم للدخول المبكر
fills: lifecycle email 3 (segment 1, dormant tier)

---

## 3. App push (app-push entry point: existing app users)

A light sequence to existing app users surfacing Skill Paths early access. Push platform is an
open item, so wiring and any send are blocked (see open_items). Kept short for the push format,
one CTA each, no price, no date.

### AR-PUSH-01 . announce

title: طريقة جديدة لتبني مهاراتك
body: خطوة صغيرة كل يوم تكفي. الدخول المبكر مفتوح الآن.
cta: انضم للدخول المبكر
fills: app push 1 (announce)

### AR-PUSH-02 . benefit nudge

title: دقائق معدودة في اليوم تكفي
body: لا محاضرات طويلة. ابدأ مهارتك التالية بخطوة واحدة.
cta: ابدأ الآن
fills: app push 2 (benefit nudge)

### AR-PUSH-03 . invitation reminder

title: مكانك في الدخول المبكر بانتظارك
body: خطوة واحدة وتبدأ طريقك نحو مهارة تبقى معك.
cta: انضم الآن
fills: app push 3 (reminder)

---

## 4. Social captions (entry point C: organic, hero's-journey arc)

Refined from the June draft, re-timed to the July flight, with the seat-cap and scarcity lines
removed (see "What changed"). Arabic captions, primary. Organic CTAs are keyword-based and
land on the profile or the gate per the June routing. The gate-landing captions (5, 7, 9, 10)
carry the signup ask. EN variants merge from copywriter-en at the QA gate.

### AR-SOCIAL-01 . Ordinary World . profile and follow

caption:
كل يوم ينتهي والقائمة نفسها: مهارة تنوي أن تتعلمها، ووقت لا يكفي.
لكن النية موجودة، وهي البداية.
قريبا، طريقة جديدة تبني مهاراتك خطوة كل يوم.
تابعنا، القصة بدأت.
cta (keyword): تابعنا
fills: social post 1, caption (overlay headline: القصة بدأت)

### AR-SOCIAL-02 . Call to Adventure . profile and follow

caption:
تخيل مهارة جديدة تبنيها في دقائق معدودة كل يوم.
لا محاضرات طويلة، ولا ضغط. خطوة صغيرة تكبر مع الوقت.
نفتح قريبا باب الدخول المبكر.
استعد، دورك قادم.
cta (keyword): استعد
fills: social post 2, caption (overlay headline: دورك قادم)

### AR-SOCIAL-03 . Refusal of the Call . profile and follow

caption:
الوقت ليس العائق، الطريقة هي.
5 دقائق في اليوم تكفي لتبدأ مهارة وتبني فيها.
صممنا كل خطوة لتناسب يومك المزدحم، لا أن تزاحمه.
الانطلاقة قريبة.
cta (keyword): تابع القصة
fills: social post 3, caption (overlay headline: الطريقة، لا الوقت)

### AR-SOCIAL-04 . Meeting the Mentor . profile and follow

caption:
كل مهارة كبيرة تبدأ بخطوة صغيرة تتكرر.
هنا تتعلم على شكل خطوات قصيرة، تتقدم وتجمع تقدمك يوما بعد يوم.
سلسلة لا تنقطع، وتقدم تشوفه بعينك.
هذا ما نبنيه لك، قريبا.
cta (keyword): تابعنا
fills: social post 4, caption (overlay headline: خطوة كل يوم)

### AR-SOCIAL-05 . Crossing the Threshold . gate

caption:
الدخول المبكر بدأ.
طريقة جديدة لتتعلم على مهاراتك، خطوة كل يوم، تبدأ بمن يتحرك أولا.
سجل اهتمامك الآن، ونصلك من أوائل الداخلين.
البداية بخطوة واحدة.
cta: سجل اهتمامك
fills: social post 5, caption (overlay headline: الدخول المبكر بدأ, CTA chip: سجل اهتمامك)

### AR-SOCIAL-06 . Tests and Trials . profile and follow

caption:
التقدم الحقيقي ليس قفزة، بل خطوة تتكرر.
يوم، ثم يوم، ثم سلسلة لا تريد أن تكسرها.
هكذا تتحول العادة الصغيرة إلى مهارة تبقى معك.
ابدأها مبكرا.
cta (keyword): ابدأها مبكرا
fills: social post 6, caption (overlay headline: لا تكسر السلسلة)

### AR-SOCIAL-07 . Allies . gate

caption:
لن تمشي وحدك.
كثيرون يتعلمون كل يوم، ويبنون عاداتهم خطوة بخطوة.
حولك مجتمع يكبر، وكل خطوة لك تلهم غيرك.
انضم للدخول المبكر.
cta: انضم للدخول المبكر
fills: social post 7, caption (overlay headline: لن تمشي وحدك)

Note: no specific learner count is stated in copy or overlay. "كثيرون" only, until a real
figure is confirmed (carried from June open items).

### AR-SOCIAL-08 . The Ordeal . profile and follow

caption:
ستأتي أيام تشعر فيها أنك لا تتقدم.
هنا يصنع الفرق: خطوة واحدة، حتى لو صغيرة.
صممنا الطريق ليعيدك بلطف كلما توقفت.
الاستمرار أهم من الكمال.
cta (keyword): واصل الطريق
fills: social post 8, caption (overlay headline: الاستمرار، لا الكمال)

### AR-SOCIAL-09 . The Reward . gate

caption:
بعد أسابيع من خطوة كل يوم، تلتفت فتجد مهارة جديدة صارت جزءا منك.
سلسلة أتممتها، وشهادة إتمام تثبت تقدمك.
ليست النهاية، بل دليل أنك تقدر.
الدخول المبكر يقربك من هذه اللحظة.
cta: انضم للدخول المبكر
fills: social post 9, caption (overlay headline: أتممتها)

Guardrail note: "شهادة إتمام" is a completion mark only. No accreditation is stated or implied
in copy or overlay.

### AR-SOCIAL-10 . The Return . gate

caption:
بدأت بنية، وانتهيت بمهارة.
هذه ليست قصتنا، بل قصتك أنت حين تبدأ.
الدخول المبكر مفتوح، والبداية بخطوة واحدة.
سجل الآن، وابدأ فصلك الأول.
cta: سجل الآن
fills: social post 10, caption (overlay headline: ابدأ فصلك الأول, CTA chip: سجل الآن)

---

## 5. Landing-page copy (the gate destination)

The early-access signup gate. Headline plus one CTA. No price, no title, no date. The gate
platform is an open item, so the live page and form wiring are blocked (see open_items).

### AR-LP-01 . landing page

headline: ابن مهارة حقيقية، خطوة واحدة كل يوم
subhead:
طريقة جديدة لتتعلم على مهاراتك في دقائق معدودة. لا محاضرات طويلة، خطوة صغيرة تتكرر وتبني فيها مهارة تبقى معك.
cta: احجز دخولك المبكر
supporting_line: الدخول المبكر مفتوح، وانضمامك يبدأ بخطوة واحدة.
fills: landing page headline, subhead, primary CTA

Landing CTA alternates (one per page):
- احجز دخولك المبكر
- انضم للدخول المبكر
- سجل اهتمامك

---

## Skill eval self-check (04-copywriting), before the gate

- One clear CTA per asset: pass. Each ad, email, push, caption, and the landing page carries a
  single CTA.
- Subject lines length: pass. All three primary subjects are short (well under typical inbox
  truncation), honest to the body, empowering, no clickbait.
- No banned claims: pass. No accreditation, no price, no promo, no firm launch date, no
  countdown, no invented Skill Path title, lesson, count, lineup, or instructor name.
- Empowering, never deficit-framed: pass. Every variant leads with what the reader can build,
  not what they lack. The retargeting lines reframe as "one step away", not "you failed to act".
- Mechanical: no em dashes, no tatweel, Western numerals only (the only numeral used is 5),
  RTL-safe. Pass on draft.
- Arabic-first: pass. Arabic authored as primary, not translated from English.

This is a self-check, not a gate pass.

## Open items (must surface at the human gate, none buried)

- gate platform (email or WhatsApp) and app-push platform: OPEN ITEM. Every paid CTA, email
  CTA, push, gate-landing caption (5, 7, 9, 10), and the landing page point at the signup gate.
  The actual link, form, and any send are BLOCKED until the platform is confirmed. Copy is
  written, the gated action stays blocked.
- early-access seat cap: OPEN ITEM. No "limited seats", "seats filling", or "closing soon"
  framing is used anywhere, because no real cap is confirmed. If Ahmed confirms a cap at the
  gate, scarcity lines can be added (the June draft variants are available as a reference). Held
  until then.
- success-metric target: not set (carried from strategy). Does not block copy, surfaces at gate.
- learner-count figure: not confirmed. AR-SOCIAL-07 uses "كثيرون" only, no number.
- price or promotion: none supplied, none in copy. If a tier or promo is later attached, copy
  must be revised to reflect it. Currently no price appears.
- launch-announcement authorization: soft launch and early access authorized in session
  2026-06-05; confirm explicitly at the human gate per the standing "do not announce a launch"
  guardrail.
- Skill Path titles, lessons, lineup: not confirmed, not invented. All copy speaks to format
  and benefit only. Standing guardrail, restated.

## Handoff

Routes to arabic-copy-qa first (all Arabic copy), then to brand-qa-reviewer alongside
compliance-privacy-reviewer (gate-landing assets collect data). On a gate fail, returns here
with the exact fix list and is regenerated against it. On pass, the QA-passed copy-package
(merged with copywriter-en EN variants) advances to build (5), conversion (6), and lifecycle
(7) per runtime/handoff-contract.md. Nothing sends or spends; the run ends at the human gate.

## Status

Draft. Not QA-passed. Not approved. Nothing here publishes, sends, or spends.
