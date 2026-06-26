# Insights: 7-step email patterns mined for "Summer of Skills" (Bassam-led summer sale)

Source: the nine reference 7-step nurture-to-subscribe sequences on branch
`claude/laughing-dijkstra-0cx0tv` (bassam-fattouh, bassam-fattouh-bridal, cedric-haddad,
elda-choucair, kosai-khauli, ragheb-alama, rahma-riad, salam-dakkak, toufic-kredieh). Every
example below is quoted verbatim from those specs. House style applies to this file too: no em
dashes, no tatweel, Western numerals.

These references are value-led nurture flows, not sale flows. They give us a tested skeleton,
voice, and claims discipline. The summer-sale layer (urgency, the offer, the deadline) is the one
thing they deliberately omit, so this doc both extracts the reusable spine and marks exactly where
a tasteful sale escalation slots in.

---

## 1. The narrative arc and per-email role pattern

Every one of the nine runs the identical 7-step spine. It is a slow-burn nurture, not a discount
blast. Steps 1 to 6 are watch-focused, step 7 is the only subscribe ask. One primary CTA per email.

| Step | Role | What it does | Module |
|---|---|---|---|
| E1 | Welcome / intro | Announce the class, name the instructor, one big idea. Invite to start. | body |
| E2 | Why this skill, why this instructor | Reframe the skill (method not products, presence is learned). Anchor authority. | body |
| E3 | What you will learn | The curriculum email. Carries the ListBlock of 4 to 5 named outcomes. | body + list |
| E4 | The free first lesson | Lower the ask to zero: watch lesson 1 free, no commitment. | body |
| E5 | Instructor credibility | The "who teaches you" email. The single strongest authority line. | body |
| E6 | Momentum / what you will be able to do | "Picture yourself after." Outcome and confidence. "Keep going." | body |
| E7 | The offer: subscribe | The only subscribe ask. Value close. CTA to subscribe / plans. | body |

The arc is psychologically ordered: curiosity (E1), reframe (E2), proof of substance (E3),
risk-free trial (E4), trust (E5), self-projection (E6), commitment (E7). E4 is the pivot: it is
the smallest possible ask and sits dead-center.

What changes per instructor is only the angle of E2 and E5, never the order. Examples of the E2
reframe: "Skill, not a pile of products" (Bassam), "Presence is a skill" (Kosai), "The kitchen is
a skill you master, not a secret you inherit" (Salam), "Building a company is no accident"
(Toufic), "Marketing is not a list of tactics, it is a way of thinking" (Elda).

For our Summer-of-Skills 7-mail mix (2 Bassam, 2 platform, 3 summer-sale), the spine maps cleanly:
the 2 Bassam emails take the E1/E2 and E5 roles (intro + authority), the 2 platform emails take
E3/E6 (what you get across the library + momentum), and the 3 sale emails layer the offer and
deadline onto the E4 (free taste), E7 (subscribe) roles plus one added urgency/last-call beat.

---

## 2. Subject-line patterns

Observed mechanics across all 9:
- Length. Short. AR subjects run roughly 3 to 7 words; EN roughly 3 to 7 words. Never a full
  sentence with punctuation. No subject in the set uses an exclamation mark.
- Front-loading. The payload word leads: the instructor name, the skill, or the benefit is in the
  first 1 to 2 words ("Bassam Fattouh, now on Maharat", "Presence is a skill", "صفك مع راغب علامة
  بدأ").
- Structure types that recur: (a) declaration of arrival ("His first-ever online class", "صفك في
  التمثيل بدأ"); (b) reframe / provocation ("Skill, not a pile of products", "Your rival tells a
  better story"); (c) plain promise of the free step ("Start free: The Talent", "الدرس الأول
  مجاناً"); (d) the close ("Unlock the full Masterclass", "اشترك وأكمل الصف كاملاً").
- Each email ships 1 primary subject plus 2 `subject_alts` for testing.

EN examples (real):
1. "His first-ever online class"
2. "Skill, not a pile of products"
3. "What 20 lessons cover"
4. "Start free: The Talent"
5. "He teaches it himself"
6. "A look you do yourself"
7. "Unlock the full Masterclass"
8. "Presence is a skill"
9. "Your rival tells a better story"
10. "Who is Salam Dakkak"
11. "He built it from scratch"
12. "One subscription opens it all"

AR examples (real):
1. "أول صف لبسام فتّوح، على مهارات"
2. "مهارة، لا كومة منتجات"
3. "ماذا ستتعلّم، درساً بدرس"
4. "الدرس الأول، مجاناً"
5. "يعلّمك بنفسه، خطوة بخطوة"
6. "إطلالة تصنعها بنفسك، لأي مناسبة"
7. "الصف كاملاً، باشتراك واحد"
8. "منافسك يروي قصته أفضل"
9. "المطبخ مهارة تتقن، لا سر يورث" (E2 headline-style, reused as subject register)
10. "من بنى شركة من الصفر"
11. "صفك مع راغب علامة بدأ"
12. "اشترك وأكمل رحلتك"

For the sale: the front-loaded benefit-first structure holds. A summer-sale subject should lead
with the offer or the season, not bury it: "Summer of Skills, your plan" reads better than
"Your plan, this summer." Keep the no-exclamation rule even on the sale.

---

## 3. Preheader patterns

Observed mechanics:
- Length. One short sentence, roughly 8 to 16 words. Always a full thought, often ends with a
  period.
- It never repeats the subject. It adds the next layer: the subject names the hook, the preheader
  delivers the promise or the proof or the scope.
- Common move: subject = the claim, preheader = the mechanism or the scale.

EN examples (subject then preheader, to show the add):
1. "His first-ever online class" -> "The artist you could never book now teaches you, step by
   step, 20 lessons from everyday looks to full glam." (adds scope + the "could never book" hook)
2. "What 20 lessons cover" -> "A real curriculum, every lesson named. Here is what you learn."
3. "Start free: The Talent" -> "Chapter 1 is called The Talent. It is free. No sign-up required
   to watch it." (adds the name + removes the friction)
4. "He teaches it himself" -> "One of the region's most sought-after artists, teaching his first
   online class himself, with nothing held back."
5. "Why learn from Toufic" -> "Success in business is a system and discipline, not luck. Learn it
   from someone who did it."
6. "Subscribe and finish strong" -> "Subscribe to Maharat and unlock Ragheb Alama's full class
   whenever you want."

AR examples:
1. "أول صف أونلاين لبسام فتّوح، 20 درساً تأخذك خطوة بخطوة."
2. "من تجهيز البشرة إلى الغلام المعدني، نظرة على المنهج."
3. "ابدأ بالدرس الأول من الصف مجاناً، بلا أي التزام."
4. "لأول مرة، راغب علامة يعلّم الموسيقى والأداء من خبرته الطويلة."
5. "النجاح في الأعمال نظام وانضباط، لا صدفة. تعلمه ممن طبّقه فعلاً."
6. "اشترك في مهارات وافتح صف راغب علامة كاملاً متى شئت."

For the sale: the preheader is where the urgency detail lives without shouting in the subject.
Pattern to copy: subject carries the offer name, preheader carries the deadline ("Offer ends
Sunday. The full library, one plan.").

---

## 4. Headline and body patterns

Opening hooks (the headline, E1 to E7). Two registers recur:
- The reframe / aphorism, especially E2: "The difference is the method, not the products."
  "Marketing is not a list of tactics, it is a way of thinking." "The kitchen is a skill you
  master, not a secret you inherit." AR: "المكياج الجميل ليس كومة منتجات، بل مهارة تطبيقها."
- The direct address / projection, especially E6: "Picture what you will be able to do."
  "Picture your kitchen after this class." AR: "تخيّلي نفسك بعد هذا الصف."

Body length and rhythm:
- Short. 2 to 3 sentences per paragraph, 2 paragraphs typical, 3 at most (E1 sometimes 3).
- Each email carries exactly one real, specific piece of value. The Bassam review doc names this
  as the rule: "Each email now carries one real, specific piece of value." Thin = seven variations
  of the same line, which the review flagged as the failure mode to avoid.
- Sentence rhythm is plain, active, declarative. Frequent two-beat closer: a longer setup sentence
  then a short imperative. "Learn it once. Save the time and the cost, every time after." "One
  step, no commitment." AR: "درس واحد يكفي لتعرف أن هذا ما تبحث عنه."

Empowering, never deficit framing. The reader is the agent, the skill is theirs to keep:
- "a look you create yourself, for any occasion" not "fix your look"
- "the skill stays with you" / "مهارة تبقى معك" recurs across nearly every sequence
- Bassam explicitly excludes the deficit line: the held-back claims note "The off-voice
  lipstick-as-facelift line from the source doc is excluded (correction framing)." The brand rule
  is "beauty as confidence, never correction." Salam: "from mystery into a skill in your own
  hands." Cedric: "It is about how you feel when you leave the house, sure of what you are
  wearing."

Authority anchored without name-dropping. The references never name a private client, brand, or
celebrity. Authority is anchored only to the page-cleared tagline or a public, page-supported fact:
- "one of the most sought-after makeup artists in the region" (Bassam, the page tagline)
- "the celebrity stylist trusted by the Arab world's biggest stars" (Cedric, generic, no names)
- "one of the biggest names in the Arab World" (Kosai)
- "more than 40 years on stage" (Ragheb, a public, countable fact)
- "built a billion-dollar business from scratch" (Toufic, page-supported)
- "the Best Female Chef in MENA ... her restaurant Bait Maryam is Michelin award winning" (Salam,
  kept exactly to page wording, "Michelin award winning" not "Michelin star")

The pattern: authority is a single concrete public fact, stated once, never a list. Bassam's
held-back note: "Authority is anchored to the page tagline only ... per the voice rule against
name-dropping."

---

## 5. The CTA ladder

The CTA verb escalates with intent across the 7 steps. It moves from "start watching" (low,
exploratory) to "subscribe" (high, commitment). The destination switches at E7.

EN ladder (the dominant pattern, Bassam):
- E1 "Start the class" -> E2 "See the class" -> E3 "Explore the class" -> E4 "Watch The Talent
  free" -> E5 "Watch the class" -> E6 "Keep going" -> E7 "See the plans"

Recurring verb shape across the set:
- E1: "Start watching" / "ابدأ المشاهدة" (begin)
- E2 to E3: "Watch the class" / "Explore the class" / "شاهد الصف" (engage)
- E4: "Watch the first lesson free" / "شاهد الدرس الأول مجاناً" (zero-risk trial, the only CTA
  with "free" in it)
- E5: "Watch the class" / "تعرّف على المعلّم" (trust)
- E6: "Keep going" / "Keep watching" / "واصلي المشاهدة" / "أكمل المشاهدة" (momentum, continuation
  verb, not a fresh start)
- E7: "Subscribe now" / "See the plans" / "Choose your plan" / "اشترك الآن" / "اختر خطتك" (commit)

CTA destinations:
- E1 to E6 point to the CLASS page (`/class/...`). They are watch CTAs.
- E7 points to the SUBSCRIBE step. Bassam (the most current decision) sends E7 to the PLANS page
  (`maharat.com/ar/plans`, `/en/plans`) because it is the subscribe step and the plans page carries
  the live price. The older builds (cedric, salam, ragheb, etc.) point E7 at the class page as the
  subscribe entry, with an open item to "confirm the subscribe or plan-picker destination at the
  human gate." Take the Bassam decision as the standard: E7 -> plans page.

For the sale: the ladder still works, but the 3 sale emails compress the high end. The free-trial
rung (E4 verb "Watch ... free") and the subscribe rung (E7 verb "Choose your plan") are the two we
build the offer on. A last-call email reuses the E7 commit verb with a deadline qualifier ("Claim
the summer plan" / "اختر خطتك قبل أن ينتهي العرض").

---

## 6. How premium tone is held

What these emails do NOT do (this is the discipline to copy):
- No exclamation marks. Not one across all 9 sequences, even on E1 and E7.
- No hype adjectives stacked. No "amazing," "incredible," "unbelievable." The strongest word used
  is "leading" or "most sought-after," and only once.
- No emoji, no all-caps, no "ACT NOW," no fake scarcity.
- No exclamation-stacked urgency. Where momentum is created it is quiet: "You are closer than you
  think." "Keep going, the best is still ahead." "أنت أقرب مما تظن."
- Short. White space and brevity carry the premium feel, not decoration.
- One idea, one CTA per email. Never two asks.

Urgency in the references is light and intrinsic, not deadline-driven. It comes from:
- the continuation verb at E6 ("Finish what you started" / "أكمل ما بدأته")
- the smallness of the next step ("One step is enough" / "خطوة واحدة تكفي")
- the free-first-lesson removing the reason to wait

Because none of the references carry a real promotion, deadline, or price (by design), there is no
example of tasteful sale urgency to quote. So, for the sale layer, the tasteful escalation that
stays in this voice would look like:
- A real, stated deadline, calm and specific, in the preheader and body, never the subject in
  caps: "The summer offer ends Sunday, 31 August." / "العرض ينتهي الأحد 31 أغسطس." Western
  numerals, a real date, no "HURRY."
- One last-call email, late in the 3 sale emails, that states the deadline once and reuses the
  empowering frame: "The skill stays with you. The summer price does not." Quiet contrast, not a
  countdown gif.
- Urgency as a single sentence, never the whole email. The body still leads with value (the
  library, the skill) and closes with the deadline.
- No invented scarcity ("only 50 spots"), no fake timers. Any deadline must be a real,
  campaign-confirmed date, the same way the references refuse to invent a promo code.

The hard rule from every spec: "PromoLine OMITTED: no real promo code or deadline exists for this
campaign, and the renderer never invents one. Add a real code to the spec to enable it." For our
sale this is exactly reversed: the deadline and code DO exist, so the PromoLine module is enabled,
but only with the real, confirmed values.

---

## 7. Held-back-claims discipline

What every sequence deliberately excludes, and how the copy works around it:

Excluded across the board:
- Price, plan tier, monthly figure. Bassam: "No price, plan, or monthly figure stated, per the
  campaign decision." The workaround: E7 closes on value ("the full class plus the growing
  library") and sends the reader to the plans page where the live price lives.
- Lesson, chapter, or recipe counts beyond what the page supports. Salam holds to "Over 20 recipes"
  because that is the only page-supported number, and excludes a named dish lineup.
- Awards and accreditation. Salam: "No named award body," "No Michelin star claim; kept to the
  page wording Michelin award winning," "No certificate or accreditation claim."
- Client, brand, celebrity names. Authority stays generic ("the Arab world's biggest stars").
- Testimonials, ratings, student counts. "No testimonial, rating, or student count."
- Launch dates, start dates, duration, income or career-outcome promises.

How the copy still lands without them:
- Name the free thing precisely when it is page-cleared: Bassam E4 names "chapter 1, The Talent"
  because the page supports it. Specificity comes from cleared facts, not invented numbers.
- Use a public, countable fact as the proof instead of a claim: "40 years on stage,"
  "billion-dollar business from scratch," "reached millions of followers."
- Frame the curriculum (E3) as named outcomes drawn from real lessons, not as counts or secrets:
  "the no-makeup makeup, day to night, everyday glam, the smokey eyes" (real lesson names), framed
  as what the learner will be able to do, "not as a secret revealed in the email."

For the sale: the only numbers we are allowed to state are the real, confirmed ones (the sale
price, the discount, the deadline date). Everything else stays held back. The price moves from
"on the plans page" to "in the email" ONLY because the sale makes a specific, confirmed number a
campaign fact. Confirm it at the human gate before it enters copy.

---

## 8. Module usage patterns

The build is a slotted live-component system (the "Elda reference standard"): every line is a live
HTML text slot bound to a `data-copy-id`, every image is text-free.

Module placement across the 7 steps:
- body (BodyCopy + SectionHeading): every email, E1 to E7.
- list (ListBlock, emerald-bullet "what you will learn"): E3 only. It is the one email that carries
  4 to 5 bullets of named outcomes. Every sequence does this.
- FeatureImage and PromoLine: available in the renderer, omitted in all 9 references. FeatureImage
  omitted because "no rights-cleared feature image staged." PromoLine omitted because no real code
  or deadline exists.
- ClassCardGrid: a global footer block, rendered at the bottom of every email (not in any single
  email's `modules` array). It is the cross-sell row.

E3 ListBlock examples (real, 5 items each):
- Bassam: "تجهيز البشرة وبناء قاعدة نظيفة قبل البدء ; اختيار الألوان التي تناسب درجة بشرتك ولون
  عينيك ; إطلالة المكياج بلا مكياج ... ; الغلام اليومي، والسموكي، والغلام الملوّن ; الإطلالة
  المعدنية، واللمسات النهائية"
- Toufic EN: "How to turn an idea into a business you can actually execute ; Building a strong
  foundation your business can grow on ; Making hard decisions with discipline and at the right
  time ; Strategies for growth and scale, as Toufic applied them ; Building the mindset of a
  founder who executes, not just imagines"

ListBlock items are parallel-structured (all start "How to ..." in EN, or all noun phrases in AR),
4 to 5 items, each a real outcome. Never a count, never a secret revealed.

For the sale: enable the PromoLine module on the sale emails (it carries the real code and
deadline). Keep the E3 ListBlock for the "what you get" email. The Bassam emails keep the standard
body + (one with) list shape.

---

## 9. The ClassCardGrid cross-sell convention

A fixed, reusable convention across all 9:
- Always 3 cards, always 3 OTHER instructors (never the email's own instructor). Bassam's grid is
  cedric / elda / ragheb; Cedric's is bassam / elda / ragheb; Salam's is bassam / ragheb / kosai.
- Each card is a text-free, on-brand near-black (#141414) PORTRAIT (the same image the maharat.com
  instructor grid uses), with an emerald accent rule, the instructor name, and the page-cleared
  "Teaches ..." subject phrase as a LIVE HTML overlay in the lower third, never baked into the
  image.
- Each card links to its language-matched class page.
- The grid title is campaign-stable: AR "شاهد أيضًا على مهارات", EN "More classes on Maharat".
- To change the 3 instructors, edit the spec's `class_cards`. The renderer never invents one.

For the sale: since this is Bassam-led, the grid on the Bassam emails should feature 3 OTHER
instructors (e.g. a platform-spanning trio across categories). On the platform/sale emails the grid
reinforces the breadth-of-library value that justifies the subscription. Pick a cross-category trio
so the cross-sell sells the platform, not one more class.

---

## 10. Do / Don't checklist for the new sequence

Do:
- Keep the 7-step spine. Map: 2 Bassam (intro + authority, E1/E2/E5 roles), 2 platform (what you
  get + momentum, E3/E6 roles), 3 sale (free taste, subscribe, last-call, built on E4/E7).
- One real, specific piece of value per email. No email is a restatement of the previous one.
- One primary CTA per email. Escalate the verb: start -> watch -> watch free -> keep going ->
  subscribe / claim.
- Front-load subjects (3 to 7 words, benefit or name first). Make the preheader add a new layer
  (the deadline, the scope, the proof), never repeat the subject.
- Anchor Bassam's authority to one public, page-cleared fact ("one of the most sought-after makeup
  artists in the region"), stated once.
- Keep bodies to 2 to 3 short paragraphs, plain active sentences, an empowering close.
- Put the E3-style ListBlock (4 to 5 parallel named outcomes) on the "what you get" platform email.
- Enable the PromoLine with the REAL, human-gate-confirmed code and deadline. State the price only
  if it is a confirmed campaign number.
- State any deadline as a real, specific date in Western numerals, calm, in the preheader and body.
- Use the 3-OTHER-instructors ClassCardGrid; pick a cross-category trio to sell the library.
- Send the subscribe CTA (E7-role sale email) to the plans page.

Don't:
- No em dashes, no tatweel, no Eastern Arabic numerals (this file and all copy).
- No exclamation marks, no all-caps, no emoji, no hype adjectives.
- No fake scarcity, no fake countdowns, no invented promo code or deadline. Real values only.
- No name-dropping clients, brands, or celebrities.
- No deficit / correction framing. The reader gains a skill, never fixes a flaw.
- No accreditation or certificate claim. No invented counts, awards, ratings, or testimonials.
- No two asks in one email. No subject that repeats in the preheader.
- No price in copy unless the sale price is a confirmed campaign fact cleared at the human gate.
- No personal or sensitive data in any URL or tracking parameter.
