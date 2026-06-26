# EdTech mobile design benchmark: MasterClass and Mindvalley, 2026-06-08

Reference research, not approved design. It reads two premium edtech platforms with the
Firecrawl MCP, extracts their mobile design systems and information architecture, and
translates the durable patterns into design principles Maharat can build on the 2026 tech
stack. Owner: research-scout (Firecrawl is its tool). Anything built from this still runs the
quality gates (design-qa, the copy QA gates, compliance-privacy-check, brand-qa-reviewer) and
the human gate. Nothing here is approved, and none of the borrowed palettes or fonts override
Maharat's fixed visual constants.

## Envelope

- sources: https://www.masterclass.com and https://www.mindvalley.com (home, the public marketing surface)
- captured: 2026-06-08
- method: firecrawl_scrape with mobile:true, formats markdown + branding + summary, render wait 4s
- tool: Firecrawl MCP, owner research-scout
- raw evidence: raw/masterclass-branding.json, raw/mindvalley-branding.json (design tokens + summary, as extracted, logo data-uri stripped)
- target stack: Maharat Tech Stack 2026 (the uploaded brief). Two mobile-facing surfaces are in scope:
  1. Mobile V2, the native app: Expo SDK 54, React Native 0.81.5, React 19.1, TypeScript 5.9, Zustand 5, TanStack Query 5, React Native Paper 5, Reanimated 4, Shopify FlashList 2, expo-video/expo-image, react-native-iap 15, i18next + RTL via I18nManager.
  2. Member and Public-Pages, the mobile web: Clojure + Ring + Luminus backends, server-driven UI via HTMX 4 + Selmer templates, shared components in cross/templates/ (Video Player, Pricing Card), SSR first paint + progressive enhancement.
- scope (confirmed 2026-06-08): both surfaces are in scope, the native Mobile V2 app and the Member and Public-Pages mobile web. The request said "a web app," the stack and source material are mobile-first, and the owner confirmed both. The mapping covers both.
- status: raw research and synthesis. Not qa-passed. Does not cross a stream boundary as-is.

## Guardrail notes

- Borrow patterns, not skins. MasterClass and Mindvalley palettes, fonts, and button shapes are
  recorded as evidence, not as targets. Maharat's visual constants are fixed: near-black #141414,
  card surfaces #1A1A1A, emerald accent #009975, premium and uncluttered. The accent is a highlight,
  not a flood.
- Neither source is Arabic or RTL. Every layout pattern below must be mirrored, not copied. See the
  RTL and Arabic-first section, which is the part the sources cannot teach.
- No em dashes, no tatweel or kashida, Western numerals only, in any mockup or copy that comes out of
  this. These are gate checks, not preferences.
- Do not invent Skill Path titles, name unconfirmed instructors, or imply accredited certificates in
  any mockup built from these principles. Prices and plan offers are brief inputs, never assumed.

---

## 1. What the two platforms actually do (the evidence)

Design tokens are from Firecrawl's branding extraction (confidence about 0.92 each). They are
the source's choices, recorded for analysis, not recommendations for Maharat.

### MasterClass (the closest structural reference for Maharat)

- Color scheme: dark. Background true black #000000. Primary CTA crimson #E32652, a single hot accent
  on an otherwise black-and-white field. Secondary accent acid yellow #DCFF00, used sparingly.
- Type: editorial. Body Sohne, headings Sohne Schmal (a condensed display cut). h1 at 52px, h2 at 20px,
  body 16px. The oversized condensed headline carries the whole hero.
- Spacing and shape: base unit 10, small border radius 4px, primary buttons 8px, no shadows. Inputs are
  transparent with no radius, closer to an underline than a box. Restrained, premium, content-first.
- Personality (extracted): professional, medium energy, audience "individuals seeking online education
  and skill development."
- IA and mobile patterns, in scroll order: aspirational hero ("LEARN FROM THE BEST, BE YOUR BEST"),
  "what is in every membership," expert grid ("Meet the world's best, new classes every month"),
  an inspiration or audio module, "Popular now," "Coming soon," career and team value props, member
  testimonials, sample classes, FAQ, app-store badges (iOS, Android, Amazon).
- Multi-modal learning, stated on the page: audio-only lessons, download and watch offline, watch on
  desktop, TV, or mobile.

### Mindvalley (the closest behavioral reference for Maharat)

- Color scheme: light. Background white. Primary brand purple #7A12D4, accent lavender #BA62FD,
  secondary slate #292D38. Pill buttons (border radius 999px), large 16px radius elsewhere, base unit 4.
  Built on Tailwind.
- Type: Sharp Grotesk family, large headings (h1 40px, h2 36px). Friendly, rounded, modern.
- Personality (extracted): modern, medium energy, audience "individuals seeking personal development."
- IA and mobile patterns: repeated "A better you" promise, "begin your journey today," "100+ programs,"
  "1,000+ customised tracks," cross-device line ("mobile, desktop and Apple Vision Pro"), advanced
  programs and certification tiers, a heavy wall of transformation testimonials, FAQ, app download.
- The daily-ritual spine: "20 minutes a day," "20-minute micro-coaching sessions each day,"
  "Mindvalley Daily," "micro-learning methodology," push-button audios, meditations, mood elevation.
  A free app with a membership that unlocks the full library.

### The overlap that matters for edtech mobile

Both, independently, converge on the same mobile playbook: one aspirational promise per screen, one
dominant CTA, experts or outcomes as the trust unit, video and audio as the interface, a low-friction
free entry that opens into a paid library, and multi-modal access (audio-only, offline, cross-device).
Mindvalley adds the daily micro-learning loop. That overlap is the spine of the principles below, and it
maps cleanly onto Maharat: premium video masterclasses (the MasterClass register) plus gamified,
bite-sized Skill Paths (the Mindvalley register).

---

## 2. The principles, with how to build each on the stack

Each principle states what the sources do, why it holds for edtech on mobile, the Maharat adaptation
inside the brand, and the concrete build on both surfaces.

### P1. One promise, one screen, one action

- Observed: both heroes are a single oversized headline plus one primary CTA. MasterClass "Get" and
  "View Plans," Mindvalley "Become a Member." No competing actions above the fold.
- Why for edtech mobile: the first screen sells a transformation, not a feature list. On a phone there is
  room for exactly one decision.
- Maharat adaptation: an empowering Arabic-first headline (Thmanyah register, never deficit-framed), one
  emerald #009975 CTA on near-black. The accent stays a highlight.
- Build, native: a Hero component, React Native Paper Button for the CTA, react-native-safe-area-context
  so the headline clears the notch, Reanimated 4 for a calm entrance.
- Build, web: an SSR hero in cross/templates/ so it paints instantly for SEO and slow connections, one
  Selmer CTA partial, progressive enhancement after.

### P2. The daily micro-learning loop is the home screen

- Observed: Mindvalley builds the whole product around "20 minutes a day," "Mindvalley Daily," and
  micro-coaching sessions. The daily habit is the product, not a feature.
- Why for edtech mobile: retention on mobile is a habit, not a catalog. A short, finishable daily unit and
  a visible streak beat a long course someone never returns to. This is exactly Maharat's gamified,
  bite-sized Skill Paths model.
- Maharat adaptation: a "today" surface as the default tab: the next bite-sized step, a daily goal, a
  streak, and resume-where-you-left-off. Gamified and empowering, with Western numerals throughout.
- Build, native: Zustand 5 for daily-progress and streak state, react-native-mmkv (encrypted) so the
  streak survives offline and cold starts, FlashList 2 for the lesson feed, Reanimated 4 + expo-haptics
  for the progress fill and the streak-increment moment. A daily reminder needs push, which is not in the
  documented stack: flag expo-notifications as a proposed addition (tool adoption is Ahmed's call).
- Build, web: a "continue learning" fragment served by the Member app over HTMX (hx-get on load), the same
  progress data, no streak push on web. Position the daily reminder and offline streak as native-app value.

### P3. Experts and outcomes are the trust unit, not the brand

- Observed: MasterClass leads with instructor portraits ("Meet the world's best"). Mindvalley leads with
  transformation stories. Neither leads with itself.
- Why for edtech mobile: people buy the teacher and the result. Full-bleed faces and concrete outcomes
  carry more weight on a small screen than logos or copy.
- Maharat adaptation: cinematic, instructor-forward class cards and outcome-led testimonials, in Arabic
  first. Guardrail: do not name an instructor in any mockup without confirmation, and never imply
  accreditation. Use placeholders until a name is confirmed in a brief.
- Build, native: expo-image (priority load and disk cache) for portraits, expo-linear-gradient for a
  bottom scrim so the Arabic title stays legible over the image, FlashList grid.
- Build, web: the shared class-card and testimonial partials in cross/templates/, responsive images,
  HTMX to lazy-load rows below the fold.

### P4. Let the media be the interface (cinematic, content-first, dark)

- Observed: MasterClass runs a true-black, near-chromeless field so full-bleed video thumbnails are the UI.
  Minimal borders, no shadows, generous black space.
- Why for edtech mobile: video and imagery are the content. A dark, quiet frame makes premium artwork pop
  and reduces cognitive load on a phone. This is already Maharat's native register.
- Maharat adaptation: near-black #141414 canvas, #1A1A1A cards, edge-to-edge media, emerald used only for
  the active and primary states. Premium and uncluttered, generous space.
- Build, native: React Native Paper themed to a Maharat dark theme (map MD3 tokens to #141414 surface,
  #1A1A1A elevated, #009975 primary), expo-video for autoplay-muted preview reels, expo-image for stills,
  FlashList for the rails.
- Build, web: the shared Video Player component (already in cross/templates/), dark Selmer layout, HTMX to
  swap a poster for the player on intent rather than shipping every player upfront.

### P5. Multi-modal access: audio-only, offline, cross-device

- Observed: MasterClass states audio-only lessons, download and watch offline, and watch on desktop, TV, or
  mobile. Mindvalley pushes audio tracks, meditations, and mobile plus desktop plus Vision Pro.
- Why for edtech mobile: GCC and Saudi learners study on the move, on commutes, on metered data, in
  eyes-free moments. Audio mode, offline download, background playback, and resume across devices are
  retention features, not extras.
- Maharat adaptation: an audio-only toggle on lessons, download-for-offline, background audio, and resume
  state that follows the learner from phone to web. Frame offline and audio as the native app's edge.
- Build, native: expo-video for combined video and audio playback, file download to the device with
  react-native-mmkv for offline metadata and progress, TanStack Query with a persisted cache for
  catalog-while-offline, expo-secure-store already holds the MMKV key. Confirm background-audio config in
  the Expo build.
- Build, web: HTMX and SSR cannot deliver true offline, so the web surface keeps cross-device resume and
  audio playback and points power users to the app for downloads.

### P6. Browse by aspiration, in fast horizontal rails

- Observed: both organize the library into scannable, themed rows. MasterClass "Popular now," "Coming
  soon," trending categories. Mindvalley 100+ programs and 1,000+ customised tracks by goal.
- Why for edtech mobile: a phone rewards short, swipeable, goal-named rows over a dense grid or a deep menu.
- Maharat adaptation: horizontal rails named by aspiration, mapped to the real catalog taxonomy from the
  site (acting, business, cooking, music, design-style) plus states like "new" and "continue." Do not
  invent Skill Path titles for these rails.
- Build, native: FlashList 2 horizontal carousels (it is built for this and keeps scroll at 60fps),
  Zustand for filter state, TanStack Query for the catalog.
- Build, web: HTMX hx-get fragments per rail from the Member or Public-Pages backend, shared Selmer rail
  partial, lazy-load on reveal.

### P7. Free entry, then a single clear membership unlock

- Observed: Mindvalley's app is free with a membership that unlocks the library, MasterClass shows one plan
  CTA, transparent pricing, and a 30-day guarantee. The paywall is honest and singular.
- Why for edtech mobile: let people sample and feel value before the wall, then present one plan decision
  with risk reversal. Multiple plan choices on a phone kill conversion.
- Maharat adaptation: a browse-and-sample tier, then one clear plan CTA. Plans exist at 1, 3, and 12 months,
  but the specific price, discount, and any guarantee are brief inputs and must not be hard-coded into a
  screen. Never imply the completion certificate is accredited.
- Build, native: react-native-iap 15 (StoreKit and Play Billing). Note the known open item: the Apple IAP
  and Google Play purchase-to-warehouse mapping is to-confirm for data-tracking-engineer.
- Build, web: the shared Pricing Card component, plan data from the backend, never literals in the template.

### P8. Sell outcomes through transformation stories

- Observed: Mindvalley devotes a long section to member testimonials phrased as life change. MasterClass
  runs "See what our members are saying."
- Why for edtech mobile: outcome proof converts better than feature copy, and short story cards swipe well
  on a phone.
- Maharat adaptation: a swipeable testimonial rail in the Maharat voice: empowering, concrete, never
  deficit-framed ("step by step you built a skill that stays with you," not "you were behind"). Arabic first.
- Build, native: FlashList carousel, expo-image for the member photo, the copy QA gate on every quote.
- Build, web: shared testimonial partial, HTMX paging for more stories.

### P9. Fast first paint, then progressive disclosure

- Observed: both marketing pages are long but lead with a clear above-the-fold and reveal the rest on
  scroll. Heavy media loads behind placeholders.
- Why for edtech mobile: perceived speed is retention. On mobile data, the first screen must paint fast and
  the rest must defer.
- Maharat adaptation: skeletons over spinners, lazy media, deferred below-fold rows, and on web a real SSR
  first paint for SEO and slow connections, which is exactly what the HTMX plus Selmer architecture is for.
- Build, native: expo-image placeholders and progressive loading, FlashList windowing, TanStack Query for
  cache-first reloads, Reanimated for content settle.
- Build, web: SSR the above-the-fold, then HTMX hx-trigger="revealed" to load rails as they enter view,
  keeping the JS payload near the stack's 14kb HTMX baseline.

### P10. Thumb-first controls, one dominant button, big targets

- Observed: every primary action is large, high-contrast, and singular. MasterClass 8px radius, Mindvalley
  a full pill. Both keep the CTA unmistakable.
- Why for edtech mobile: the action must sit in the thumb zone and be tappable without precision. One
  button should obviously win.
- Maharat adaptation: a sticky bottom CTA on key screens, emerald primary, large targets (44px minimum),
  one dominant action per view. Pick one consistent corner radius that reads premium rather than playful:
  a moderate radius is recommended over MasterClass's near-square or Mindvalley's full pill, but the final
  value is a design-qa decision against the brand.
- Build, native: React Native Paper Button sized for touch, react-native-safe-area-context for the thumb
  zone and home indicator, a sticky footer container.
- Build, web: a sticky CTA bar in the shared template, HTMX for the submit, server-rendered states.

### P11. Motion and haptics as feedback, restrained and premium

- Observed: both platforms are restrained with motion. It signals quality rather than decorating.
- Why for edtech mobile: motion should confirm progress and reward completion, the core of a gamified loop,
  without draining battery or attention. Overdone motion reads cheap.
- Maharat adaptation: Reanimated for progress fills, streak increments, card press, and screen transitions,
  plus expo-haptics on lesson completion and streak milestones for tactile gamification. Honor the OS
  reduce-motion setting.
- Build, native: Reanimated 4 with react-native-worklets (and react-native-nitro-modules already in the
  stack), expo-haptics for the reward moments.
- Build, web: keep web motion to light CSS transitions on HTMX swaps (hx-swap settle timing), no heavy
  animation, parity of meaning not of mechanism.

---

## 3. RTL and Arabic-first: the part the sources cannot teach

MasterClass and Mindvalley are LTR and English. Every pattern above must be mirrored and re-typeset for
Arabic. This is Maharat's differentiator and the highest-risk area, because it is invisible in the
benchmarks.

- Mirror the layout, do not copy it. Horizontal rails scroll from the right, progress fills from right to
  left, back and forward icons and chevrons flip, the primary CTA and the thumb zone move to match. Use
  logical start and end, never hard-coded left and right. Configure with I18nManager (supportsRTL and
  forcesRTL) and React Native's writingDirection. React Native Paper honors RTL when configured.
- Flip directional media. The expo-linear-gradient scrim over a portrait and any directional gradient must
  flip so the Arabic title stays in the legible corner. A gradient tuned for an LTR overlay will fight RTL
  text.
- Typography is not a font swap. MasterClass's effect comes from a condensed Latin display cut. Do not apply
  a Latin condensed face to Arabic. Maharat needs a premium Arabic typeface with a real display weight to
  carry the oversized hero. Selecting and licensing that face is an open item and an asset and tool decision,
  so it needs approval, not a default.
- Numerals and characters: Western numerals only, even in Arabic UI. The i18next number formatting must not
  localize to Eastern Arabic digits. No tatweel or kashida to fake justification or fill a line.
- Bidi safety: mixed Arabic with Latin brand names or numerals must not break direction. Test every rendered
  screen, native and web. This is a design-qa check, not an assumption.
- Web specifics: every HTMX fragment must carry the correct dir attribute, and the shared cross/templates/
  components must be dir-aware so a fragment swapped into an RTL page does not revert to LTR. i18next is the
  shared en and ar source on both surfaces (flat JSON on mobile per the stack), so keep one key set across
  native and web to avoid drift.

---

## 4. Borrow patterns, not skins: the reconciliation

| Dimension | MasterClass | Mindvalley | What Maharat takes |
| --- | --- | --- | --- |
| Palette | dark, crimson + acid | light, purple + lavender | neither. Fixed: #141414, #1A1A1A, emerald #009975 |
| Register | cinematic, editorial, premium | friendly, daily, transformational | MasterClass's dark premium frame + Mindvalley's daily loop |
| Type | condensed Latin display | rounded Latin grotesque | a premium Arabic display face (open item), borrow the scale and hierarchy only |
| Buttons | 8px, hot accent | full pill | one consistent premium radius, emerald as a highlight not a flood |
| Spine | expert authority + library | daily micro-learning habit | both: masterclasses (authority) + Skill Paths (daily habit) |

The short version: build MasterClass's cinematic dark discipline as the structure, run Mindvalley's daily
micro-learning loop as the behavior, and render all of it in Maharat's emerald-on-near-black skin, Arabic
first and RTL correct.

Direction confirmed 2026-06-08. This is the approved structural direction for the build. It is a
direction, not approved screens: every asset built from it still runs the gates and the human gate.

## 5. Stack mapping at a glance

| Principle | Mobile V2 (Expo / React Native) | Member and Public-Pages (HTMX / Selmer) |
| --- | --- | --- |
| P1 one promise | Paper Button, safe-area, Reanimated hero | SSR hero in cross/templates/, one CTA partial |
| P2 daily loop | Zustand + MMKV streak, FlashList, haptics, (propose expo-notifications) | HTMX "continue learning" fragment |
| P3 experts and outcomes | expo-image + linear-gradient scrim, FlashList | shared card and testimonial partials |
| P4 media as UI | Paper dark theme, expo-video, expo-image | shared Video Player, HTMX load-on-intent |
| P5 multi-modal | expo-video audio mode, offline download, TanStack persisted cache | cross-device resume, app for offline |
| P6 aspirational rails | FlashList horizontal, Zustand filters, React Query | HTMX hx-get rail fragments |
| P7 free then unlock | react-native-iap (IAP-to-warehouse open item) | shared Pricing Card, plan data from backend |
| P8 transformation stories | FlashList carousel, copy QA on quotes | testimonial partial, HTMX paging |
| P9 fast then reveal | expo-image placeholders, FlashList windowing, React Query | SSR above-fold, hx-trigger="revealed" |
| P10 thumb-first CTA | Paper Button, safe-area sticky footer | sticky CTA bar partial, HTMX submit |
| P11 motion and haptics | Reanimated 4 + worklets, expo-haptics | light CSS transitions on HTMX swaps |

## 6. Open items and what was not captured

- In-product learning UI not captured. Both sources gate the lesson player, course detail, and progress
  dashboard behind login, so this read is of the public marketing surface only. The strongest mobile
  learning patterns (player controls, chapter list, notes, quiz, progress) need an authenticated capture or
  a design pass from the feature list. Flag if you want that pursued.
- RTL and Arabic-first approach confirmed 2026-06-08. The Arabic display typeface itself is still
  unresolved: it is an asset and licensing decision and needs an actual selection before build, not just
  approval of the approach.
- A daily push reminder for P2 implies expo-notifications, which is not in the documented stack.
  Acknowledged 2026-06-08 to carry forward as a proposed addition, final adoption is Ahmed's call and a
  settings change.
- The Apple IAP and Google Play purchase-to-warehouse mapping (P7) is the known data-tracking open item.
  Acknowledged 2026-06-08, carried forward to data-tracking-engineer.
- All of the above are reference inputs. Any screen built from them runs design-qa (RTL, visual constants,
  Western numerals, no Arabic baked into generated images), the copy QA gate, compliance-privacy-check, and
  brand-qa-reviewer, then stops at the human gate.
