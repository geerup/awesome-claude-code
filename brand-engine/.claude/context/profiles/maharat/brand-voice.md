# brand-voice.md: how Maharat sounds and looks

Loaded by every agent before it produces anything customer-facing. This is the voice
`arabic-copy-qa` and `brand-qa-reviewer` check against. It is a source of truth, not a
campaign input. Campaign variables (offer, price, target) never live here.

---

## The one-line identity

Maharat is an Arabic-first, gamified self-development platform. The goal is to be the
go-to platform for self-development and upskilling in the Arab world. The voice should
sound like that: modern, intelligent, confident, and unmistakably Arabic-first.

## Tone benchmark: Thmanyah

Clear, modern, intelligent, never stiff. Think of a smart friend who respects the reader.
Not academic, not corporate, not hype. Confident without shouting.

## Voice rules

- Arabic-first. Modern Standard Arabic with Gulf-familiar wording. The Arabic is primary;
  English follows the same spirit, it is not a translation afterthought.
- Plain and confident. Short sentences. Concrete nouns. Active voice.
- Empowering, never deficit-framed. Speak to what the reader can become, not what they lack.
  Write "تعلم مهارة جديدة" framing, not "you are behind, fix yourself" framing.
- Respect the reader's intelligence. No condescension, no over-explaining, no hype words.

### Empowering vs deficit-framed, worked

- Deficit: "Stop wasting your potential. You are falling behind."
- Empowering: "You already have the drive. Here is the path that turns it into a skill."

- Deficit (AR): "لا تضيع وقتك، أنت متأخر."
- Empowering (AR): "خطوة واحدة كل يوم تبني مهارة تبقى معك."

## Hard mechanical rules (these are gate checks, not preferences)

- No em dashes anywhere, in any language. Use a comma, a colon, or a period. This applies
  to Arabic and English, to copy and to internal files.
- No tatweel or kashida (the Arabic letter-stretching character, Unicode U+0640). Never.
- Western numerals only: 0 1 2 3 4 5 6 7 8 9. Never Eastern Arabic numerals (the
  Arabic-Indic digits, Unicode U+0660 to U+0669).
- RTL must render correctly. Arabic copy is right-to-left. Mixed AR and EN or numerals must
  not break direction. Test any rendered asset.

## Visual constants

- Near-black background: #141414
- Card surfaces: #1A1A1A
- Primary accent, emerald: #009975
- Premium, uncluttered. Generous space. The accent is a highlight, not a flood.

## Content guardrails (the brand can be sued or embarrassed if these slip)

- Do not invent Skill Path titles or the content lineup. If a title is needed and not
  confirmed in the brief or context, stop and ask. Do not guess a plausible one.
- Do not name instructors publicly without confirmation.
- No fundraising talk, no roadmap, no unannounced plans in customer-facing output.
- Never imply certificates are accredited. Maharat issues completion certificates. They are
  not accredited. Do not say or imply otherwise.

## What the platform offers (for accurate copy, not for inventing specifics)

- Masterclasses: premium video from regional experts.
- Skill Paths: gamified, bite-sized, Duolingo-like. Built but not yet launched. Do not
  announce a launch date or invent titles.
- PDF guides and completion certificates (not accredited).
- Plans: 1, 3, and 12 months. Prices and promotions are per-campaign inputs, never assumed.

## Audience to keep in mind while writing

Arabic-speaking adults roughly 18 to 35. Core market the GCC, primary market Saudi Arabia.
Write for a smart, busy adult who wants to grow and has many demands on their time.

## Evidence from the live Arabic site (folded in 2026-06)

Drawn from the current www.maharat.com Arabic copy. Full corpus in
`references/2026-06-maharat-ar-copy/01-ar-website-copy.md`, full analysis in the same folder's
`02-brand-voice-and-tone-manual.md`. These confirm and sharpen the rules above with how the brand
actually speaks, with verbatim evidence.

Voice, confirmed by the site:
- Positioning lines to keep: "تعلّم من نخبة العرب", "منبر للعرب، من قبل العرب", and the mission
  "تثقيف وترفيه وإلهام العالم العربي". Emotional anchor: "التعلّم يجب أن يكون ملهمًا، لا مرهقًا".
- Empowering, never deficit: skill and beauty are confidence and self-expression
  ("التعبير عن الذات", "احتفلوا بأجسامكم وأحبّوها كما هي"), never correction.
- Accessible: "ليس هناك أي خبرة سابقة مطلوبة", "خطوة بخطوة".

How the brand speaks about instructors (the authors):
- Title pattern: "[الاسم] يعلّم/تعلّم [الموضوع]", the verb agrees with the instructor's gender.
- Authority is always anchored to a concrete proof (years, award, company value, fame), never vague.
- Chapter 1 is always free and titled "الماهر" or "الماهرة". The instructor is a generous guide who
  shares journey and even vulnerability (a recurring "الصحة النفسية أولوية" thread).
- Do not name an instructor's private clients or brand-line specifics in copy.

How the brand speaks about the product:
- Taxonomy: صفوف (full masterclasses, about 2 to 3 hours, in فصول and فصول فرعية) and قوائم مهارات
  (short, curated playlists for fast, focused learning).
- The completion certificate is "شهادة مخصصة باسمك" to document the journey, never accredited. This
  matches the guardrail above and is how the live site frames it.
- Price is value-led and monthly-equivalent: "احصل على وصول غير محدود، بأقل من $7 شهرياً (تدفع سنوياً)".

Lexicon to use: نخبة العرب، خطوة بخطوة، وصول غير محدود، حصري، استكشف، اكتشف، حوّل، أتقن، التعبير عن
الذات، الثقة بالنفس، العقول الفضولية. Gendered reader address by category: feminine for beauty and
style, masculine or plural elsewhere.

To reconcile (live site vs this doc, for Ahmed):
- Plans: the live site shows a 6-month ($50) and a 12-month ($75) subscription plus single-class
  lifetime purchase, while this doc lists "1, 3, and 12 months". Prices stay per-campaign inputs;
  confirm the real plan set before any plan-specific copy.
- Numerals: the live site is mostly Western but the FAQ slips into Eastern Arabic-Indic digits in a
  couple of places. Western numerals remain the standard here; the manual flags every live instance.
