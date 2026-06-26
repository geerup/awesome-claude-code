# Maharat mobile design brief (for Claude design)

Paste this whole file into Claude and ask it to design the screens in section 7. It is
self-contained: design system, directives, RTL rules, screen specs, web parity, and the hard
constraints. Output is mockups for review, not production. Anything taken forward still runs
design-qa, the copy QA gates, compliance-privacy-check, and brand-qa-reviewer, then the human gate.

Provenance: the directives in section 5 are distilled from a 2026-06-08 benchmark of MasterClass and
Mindvalley (see INDEX.md in this folder). The visual system is Maharat's own, not theirs.

---

## 0. Paste-and-go prompt

> You are designing the Maharat product UI. Maharat is an Arabic-first, gamified self-development
> platform: premium video masterclasses from regional experts plus bite-sized, gamified Skill Paths.
> Use the design system in section 4 exactly (copy the CSS token block verbatim). Follow every rule in
> section 3. Design Arabic-first and RTL as the primary, with an English LTR mirror. Deliver each screen
> in section 7 as a self-contained, responsive, dark-theme HTML artifact at a 390x844 mobile frame, plus a
> component sheet. All imagery is text-free placeholders, Arabic is live text. Western numerals only, no em
> dashes, no tatweel.

---

## 1. Product and audience

- Product: Maharat, an Arabic-first, gamified self-development and upskilling platform.
- Two content types: premium video masterclasses from regional experts, and gamified, bite-sized Skill
  Paths (a daily, Duolingo-style habit). Also PDF guides and completion certificates (not accredited).
- Audience: Arabic-speaking adults roughly 18 to 35, core market the GCC, primary market Saudi Arabia.
  Smart, busy, mobile-first, growth-minded.
- Voice: modern, intelligent, confident, empowering, never deficit-framed. Benchmark tone Thmanyah.
- Two surfaces, same system: the native app (Expo, React Native) and the mobile web (server-driven HTMX
  plus Selmer). Design once, note the web differences in section 8.

## 2. What we are designing for

A dark, cinematic, premium, uncluttered product where the media is the interface and emerald is a single
highlight, not a flood. The structural reference is a disciplined dark editorial system. The behavioral
spine is a daily micro-learning loop with streaks and resume. Both rendered in Maharat's emerald-on-near-
black skin, Arabic-first.

## 3. Non-negotiable constraints (these are gate checks)

- No em dashes anywhere, in any language. Use a comma, a colon, or a period.
- Western numerals only (0 to 9), even in Arabic UI. Never Eastern Arabic digits. Use tabular figures for
  counters, timers, prices, and streaks.
- No tatweel or kashida, no letter-spacing on Arabic, no all-caps Arabic (Arabic has no case).
- Arabic-first and RTL is the primary design. English LTR is the mirror. See section 6.
- Fixed brand colors do not change: canvas #141414, card surface #1A1A1A, accent emerald #009975. Emerald
  is a highlight, not a flood. Everything else in the palette is derived and marked pending design-qa.
- Do not bake Arabic text into images. Generative tools mangle Arabic script. Imagery is text-free, Arabic
  sits as live text over it.
- Do not invent Skill Path titles or a content lineup. Use bracketed placeholders like [Skill Path title].
- Do not name instructors. Use [Instructor name, pending confirmation] with a text-free portrait.
- Never imply a certificate is accredited. The label is "completion certificate" or "شهادة إتمام" only.
- Prices, plan lengths, discounts, and guarantees are inputs, not assumptions. Use [price] and [offer]
  placeholders.
- All sample copy in this brief is placeholder for layout only and is subject to the Arabic and English
  copy QA gates.

---

## 4. Design system (renderable tokens)

Copy this token block into the artifact and use the variables everywhere. Derived values (anything that is
not one of the three fixed brand colors) are a starting point and are subject to design-qa.

```css
:root {
  /* color, fixed brand constants */
  --canvas:#141414;          /* app background */
  --surface:#1A1A1A;         /* cards, sheets */
  --emerald:#009975;         /* primary accent, highlight not flood */

  /* color, derived (pending design-qa) */
  --surface-2:#202020;       /* elevated: menus, raised cards */
  --surface-3:#262626;       /* pressed state on a surface */
  --border:#2A2A2A;          /* hairline dividers and outlines */
  --emerald-pressed:#00805F; /* primary button pressed */
  --emerald-tint:#2EBF98;    /* emerald for small text/icons, higher contrast on dark */
  --text-primary:#FFFFFF;    /* headings, high emphasis */
  --text-body:#EDEDED;       /* body copy */
  --text-secondary:#A8A8A8;  /* captions, metadata */
  --text-disabled:#6E6E6E;   /* disabled and placeholder only */
  --error:#E5484D;
  --warning:#E6A23C;
  --scrim: linear-gradient(180deg, rgba(20,20,20,0) 0%, rgba(20,20,20,0.85) 100%);

  /* radius */
  --radius-sm:10px; --radius-md:12px; --radius-lg:16px; --radius-xl:24px; --radius-pill:999px;

  /* spacing, 4-based */
  --space-1:4px; --space-2:8px; --space-3:12px; --space-4:16px; --space-5:20px;
  --space-6:24px; --space-8:32px; --space-10:40px; --space-12:48px; --space-16:64px;
  --gutter:20px;

  /* motion */
  --dur-fast:120ms; --dur:200ms; --dur-slow:300ms; --ease-out:cubic-bezier(0.2,0,0,1);

  /* type */
  --font-ar:"IBM Plex Sans Arabic","Tajawal","Noto Kufi Arabic",system-ui,sans-serif;
  --font-en:"Inter","Helvetica Neue",Arial,system-ui,sans-serif;
}
```

### Color contrast (already checked against #141414 canvas)

- emerald #009975 as text or icon on canvas: about 5.1 to 1, passes AA for normal text.
- emerald-tint #2EBF98 on canvas: about 7.9 to 1, use it for small accent text and icons.
- text-secondary #A8A8A8 on canvas: about 7.8 to 1.
- white label on an emerald button fill: about 3.6 to 1. Treat the label as large UI (16px or more,
  weight 600). If a label must be smaller, switch the label color to #141414 (about 5.8 to 1).

### Typography scale (mobile, size / line-height / weight)

Arabic takes slightly taller line-height. Headings: no letter-spacing, no all-caps, no tatweel.

- Display (hero): 36 / 46 / 700 (Arabic 34 / 48). May go to 40 on large phones.
- H1: 28 / 36 / 700
- H2: 22 / 30 / 600
- H3: 18 / 26 / 600
- Body-L: 17 / 28 / 400
- Body: 15 / 24 / 400
- Label and Button: 15 / 20 / 600
- Caption: 13 / 18 / 400
- Eyebrow: 12 / 16 / 600, letter-spacing allowed on Latin only.

Font note: IBM Plex Sans Arabic and Inter are renderable placeholders so the design is consistent now. The
final Arabic display face is an open licensing decision and is not settled by this brief.

### Elevation, icons, targets, motion

- Elevation by surface step, not heavy shadow. Depth is #1A1A1A then #202020 plus a 1px #2A2A2A border.
  A floating CTA or sheet may use one soft shadow: 0 8px 24px rgba(0,0,0,0.4).
- Icons: line style, 24px default, 20px dense, 28px in the tab bar, stroke about 1.75. Active state emerald.
- Touch targets: 44px minimum.
- Motion: 120ms press feedback, 200ms standard, 300ms screen and sheet. Ease-out on enter. Honor the OS
  reduce-motion setting. On native, fire a haptic on lesson completion and streak increment.

### Core components

- Button, primary: fill --emerald, label white at 15px or more weight 600, height 52, radius --radius-md,
  full width for a screen CTA. Pressed --emerald-pressed. Disabled fill --surface, label --text-disabled.
- Button, secondary: transparent fill, 1px --border, label --text-body, height 52, radius --radius-md.
  Pressed fill --surface-2.
- Button, text: label --emerald-tint, no fill.
- Bottom tab bar: fill --canvas, 1px top --border, 4 tabs (Today, Library, Skill Paths, Profile), active
  icon and label --emerald, inactive --text-secondary, height 56 plus safe area. Order mirrors in RTL.
- App bar: transparent over media or --canvas, leading title or back chevron. Chevron flips in RTL.
- Class card (portrait): 3 by 4 text-free image, radius --radius-lg, bottom --scrim, title H3 white,
  [Instructor name, pending confirmation] caption --text-secondary. Optional emerald progress bar pinned to
  the bottom edge.
- Rail: horizontal list, leading section title, trailing "See all" that flips in RTL, card width about 150
  to 160, gap --space-3, snap scrolling.
- Today card (wide): 16 by 9 text-free thumbnail, emerald progress ring or bar, resume label, one CTA.
- Skill Path node: compact card or node with locked, available, and completed states. Completed shows an
  emerald check. Progress label "[n] of [n]" with Western numerals.
- Streak chip: icon plus "[n] days" or "[n] أيام", Western numerals, emerald or neutral.
- Plan card: --surface, radius --radius-lg, plan length placeholder, [price], optional emerald "most
  popular" badge, selected state 2px emerald border. No accreditation language.
- Input: fill --surface, radius --radius-md, height 52, label and placeholder --text-secondary, focus
  border --emerald, text aligned to the start (right in Arabic). OTP uses segmented boxes, Western numerals.
- Chip and filter: pill, unselected 1px --border with --text-body, selected --surface-2 with a 1px emerald
  border and --emerald-tint label, so emerald stays a highlight.
- Testimonial card: --surface, radius --radius-lg, quote Body-L, [Member name] and [result], text-free
  avatar. Swipeable.
- Progress: linear height 4 to 6, track --border, fill --emerald, radius pill. Ring for course percent. In
  RTL the fill grows from the right.
- Badge: "New" or "جديد", "Coming soon" or "قريبا", --emerald-tint on a subtle surface.
- Sheet and modal: --surface, top radius --radius-xl, grabber, scrim rgba(0,0,0,0.6).

---

## 5. Design directives (what to do on every screen)

1. One promise, one screen, one action. One dominant emerald CTA per view. Do not stack competing buttons
   above the fold.
2. Make the daily loop the home. The default tab is Today: next step, daily goal, streak, and resume.
   Short and finishable beats long and abandoned.
3. Lead with experts and outcomes, not the brand. Full-bleed portraits and concrete results carry the
   screen. Use placeholders for unconfirmed names.
4. Let the media be the interface. Edge-to-edge text-free imagery and video on a quiet dark field. Minimal
   chrome, generous space.
5. Support multi-modal learning. Every lesson offers an audio-only mode and a download for offline. Show
   resume state that follows the learner across devices.
6. Browse by aspiration in fast horizontal rails, named by goal and by state (New, Continue, Popular),
   mapped to the real categories in section 7.4.
7. Free entry, then one clear membership unlock. Let people sample before the wall, then present one plan
   decision with honest pricing placeholders.
8. Sell outcomes through short, swipeable transformation stories in the Maharat voice.
9. Fast first paint, then progressive disclosure. Skeletons over spinners. Defer below-the-fold media.
10. Thumb-first controls. The primary action sits in the thumb zone, often a sticky bottom CTA, with 44px
    targets.
11. Motion and haptics as restrained feedback: progress fills, streak increments, card press, screen
    transitions. Never decoration.

---

## 6. RTL and Arabic-first rules

Design Arabic-first and RTL as the primary artifact. Produce the English LTR version as a true mirror.

- Set dir="rtl" and --font-ar for Arabic, dir="ltr" and --font-en for English.
- Use logical properties (inset-inline-start, margin-inline, padding-inline, text-align:start). Never hard
  left or right.
- Mirror the layout: horizontal rails scroll from the right, "See all" and trailing affordances move to the
  left, back and forward chevrons and arrows flip, the bottom tab order mirrors.
- Progress and streak fills grow from the right in RTL.
- Vertical scrims over media are unchanged. Any side or diagonal gradient flips so the Arabic title stays in
  the legible corner.
- Media scrubber: keep the time axis left to right (the play head tracks content time), but mirror the
  surrounding controls and labels. This is a known exception, flag it for design-qa.
- Numerals stay Western in both directions. Times like 12:30 and counts like 20 do not localize to Eastern
  digits.
- Bidi safety: Arabic mixed with a Latin brand name or a number must not break direction. Test every screen.
- No tatweel to justify or pad a line. Let Arabic wrap naturally.

---

## 7. Screens to design

For each screen, design the Arabic RTL version first, then the English LTR mirror. Show the noted states.
All sample copy is placeholder, pending the copy QA gates.

### 7.1 Onboarding and hero

- Purpose: state the promise and start the journey in one screen.
- Layout, top to bottom: full-bleed text-free image or muted autoplay reel with a bottom scrim, app
  wordmark small at top, oversized Display headline, one supporting line, primary CTA, a quiet secondary
  "Log in" link, optional 3-dot pager if multi-slide.
- Placeholder copy AR: headline "خطوة كل يوم، ومهارة تبقى معك", support "دروس قصيرة، ونتائج تدوم", CTA
  "ابدأ الآن", secondary "تسجيل الدخول". EN: "A step a day builds a skill that stays", "Short lessons,
  lasting results", "Start now", "Log in".
- States: single and 3-slide variants.
- Motion: headline and CTA fade and rise on enter.

### 7.2 Signup gate

- Purpose: low-friction account creation by email or WhatsApp OTP (both are in the stack).
- Layout: dark, compact. Segmented toggle for Email or WhatsApp, the matching input, primary continue CTA,
  Apple and Google sign-in buttons, a short privacy line. For OTP, a segmented 4 to 6 box input, Western
  numerals, resend timer.
- Placeholder copy AR: "سجل بالبريد أو واتساب", CTA "متابعة". EN: "Sign up with email or WhatsApp",
  "Continue".
- States: empty, focus, error, OTP entry, loading.
- Guardrail: no personal data in any visible URL or tracking note on the mockup.

### 7.3 Home, Today (default tab)

- Purpose: the daily habit surface. The most important screen.
- Layout, top to bottom: greeting plus streak chip, "today's goal" line with a small ring (for example 20
  minutes), a wide Continue card (resume with progress), the next Skill Path step as a prominent node, then
  a "Recommended for you" rail and a "New this week" rail.
- Placeholder copy AR: "اليوم", "هدف اليوم: 20 دقيقة", streak "7 أيام متتالية", "تابع التعلم", "الخطوة
  التالية". EN: "Today", "Today's goal: 20 minutes", "7 day streak", "Continue learning", "Next step".
- States: new user (no streak, no resume, show a starter), mid-journey (streak and resume), goal-met
  (celebratory check), loading skeletons.
- Motion: streak increment with haptic, progress ring fill.

### 7.4 Browse and Library

- Purpose: explore the catalog by aspiration.
- Layout: search field at top, a row of category chips, then stacked rails: "Continue", "Popular now",
  "New", and one rail per category. Each rail is portrait class cards.
- Categories (real site taxonomy, safe to use): Acting (التمثيل), Business (الأعمال), Cooking (الطبخ),
  Music (الموسيقى), Design and style (التصميم والستايل).
- States: default, search active with suggestions, empty search result.
- RTL: rails scroll from the right, chips start from the right.

### 7.5 Category listing

- Purpose: all classes in one category.
- Layout: category title and short intro, a sort or filter control, a 2-column grid of portrait class cards
  (or a comfortable list). Sticky compact header on scroll.
- States: default, filtered, "Coming soon" badge on unreleased items, loading skeleton grid.

### 7.6 Class and masterclass detail

- Purpose: convince and start.
- Layout, top to bottom: cinematic header image or trailer with play, title H1, [Instructor name, pending
  confirmation] with a text-free portrait chip, quick meta (lessons count, total time, level) in Western
  numerals, a sticky primary CTA "Start watching" or "Continue", tabbed or stacked sections for About,
  Lessons (a numbered list with durations and lock or done states), what you get (includes a completion
  certificate, never accredited), and a testimonial rail.
- Placeholder copy AR: "ابدأ المشاهدة", "نبذة", "الدروس", "يتضمن شهادة إتمام". EN: "Start watching",
  "About", "Lessons", "Includes a completion certificate".
- States: not started, in progress (resume and progress bar), completed (certificate available), locked
  behind membership (paywall CTA).

### 7.7 Lesson player

- Purpose: watch or listen, online or offline.
- Layout: full-bleed video with a bottom control bar (play and pause, scrubber with emerald fill, current
  and total time in Western numerals, captions toggle, speed, fullscreen), and a top bar with back and a
  download-for-offline icon. Below the player when not fullscreen: lesson title, an Audio-only toggle, a
  chapters or lessons list, and a notes affordance.
- Audio-only mode: a distinct compact layout, large artwork, transport controls, background-play affordance.
- Placeholder copy AR: "صوت فقط", "تحميل للمشاهدة دون اتصال", "الفصول". EN: "Audio only", "Download for
  offline", "Chapters".
- States: playing, paused, buffering, downloaded badge, offline mode, error.
- RTL: mirror the chrome, keep the time axis left to right per section 6.

### 7.8 Skill Path overview and step

- Purpose: the gamified, bite-sized daily learning unit.
- Layout, overview: a vertical path of nodes with locked, available, and completed states, an overall
  progress bar, and the current step highlighted. Layout, step: one short lesson or exercise, a clear single
  action, immediate feedback, and a completion state that advances the path and bumps the streak.
- Placeholder copy AR: feature label "مسارات المهارة", "الخطوة 3 من 10", "أكملت الخطوة". Use [عنوان المسار]
  for any specific path title. EN: "Skill Paths", "Step 3 of 10", "Step complete", "[Skill Path title]".
- States: locked, available, in progress, complete, path finished.
- Motion: node-to-node advance, completion check, streak bump, all with haptics on native.

### 7.9 Plans and paywall

- Purpose: one clear membership decision.
- Layout: a short value recap or 3 benefit lines, plan cards for the 1, 3, and 12 month options with [price]
  placeholders and an emerald "most popular" badge on one, a selected state, one primary CTA, a risk-reversal
  line as [offer], and small print. A testimonial or logos strip is optional.
- Placeholder copy AR: "اختر خطتك", plans "شهر / 3 أشهر / 12 شهر", "الأكثر اختيارا", CTA "اشترك الآن". EN:
  "Choose your plan", "1 month / 3 months / 12 months", "Most popular", "Subscribe now".
- States: default, plan selected, loading checkout, error.
- Guardrail: no accreditation claim, no invented price, no fundraising or roadmap copy.

### 7.10 Profile, progress, downloads

- Purpose: identity, progress, and offline library.
- Layout: header with avatar and name, stats row (streak, minutes learned, classes completed) in Western
  numerals, sections for My progress, Downloads (offline list with size and delete), Certificates
  (completion certificates), and Settings (language Arabic and English, notifications, account).
- Placeholder copy AR: "تقدمي", "التنزيلات", "الشهادات", "الإعدادات", "اللغة". EN: "My progress",
  "Downloads", "Certificates", "Settings", "Language".
- States: empty downloads, downloaded items, certificate earned versus locked.

### Reusable: testimonial block

A swipeable rail of testimonial cards (section 4). Empowering, concrete, never deficit-framed. Use on
onboarding, class detail, and the paywall. Arabic-first, [Member name] and [result] placeholders.

---

## 8. Mobile web parity (HTMX 4 plus Selmer)

Same tokens, same look, server-driven. The web is SSR-first for SEO and slow connections, then HTMX adds
the interactive bits. Keep the JavaScript payload near the stack's small HTMX baseline.

- Render the same dark system and component set. Reuse the shared cross/templates/ components, notably the
  Video Player and the Pricing Card, so web and app stay visually identical.
- SSR the above-the-fold of every screen, then lazy-load rails and below-the-fold blocks with HTMX
  hx-trigger="revealed". Use server-rendered skeletons.
- Map interactions to HTMX: Today's "continue learning" and the catalog rails are hx-get fragments, plan
  selection and signup submit are hx-post, the player swaps a poster for the embed on intent.
- Every HTMX fragment carries the correct dir attribute so a fragment swapped into an RTL page does not
  revert to LTR. Keep one i18next key set shared with the app to avoid copy drift.
- What is app-only and should degrade gracefully on web: offline downloads, push or daily reminders, and
  heavy animation and haptics. Audio playback and cross-device resume stay on web. Where a feature is
  app-only, the web shows the value and points to the app rather than faking it.
- Frame the web mockups at the same 390px mobile width, and note the reflow to a wider breakpoint (for
  example 768px and up) where rails get more cards and detail pages gain a side column.

## 9. What to deliver

- A self-contained, responsive, dark-theme HTML artifact per screen in section 7, at a 390 by 844 mobile
  frame. Note behavior at 360px (small) and 430px (large).
- For the priority screens (7.1, 7.3, 7.4, 7.6, 7.7, 7.9), deliver both an Arabic RTL version (primary) and
  an English LTR mirror.
- A component sheet artifact showing buttons, cards, tab bar, inputs, chips, progress, plan card, and the
  testimonial card in their states.
- Use the section 4 CSS token block verbatim. Imagery is text-free placeholder blocks or stock, Arabic is
  live text. Western numerals, no em dashes, no tatweel.
- Call out the key states on each screen: empty, loading skeleton, locked or paywalled, completed, offline,
  and error.

## 10. Quick guardrail recap for copy and content

- Empowering, never deficit-framed. Short, confident Arabic, Gulf-familiar, Thmanyah tone.
- Placeholders, not inventions: [Skill Path title], [Instructor name, pending confirmation], [price],
  [offer], [Member name], [result].
- "Completion certificate" only, never accredited.
- No fundraising, roadmap, or unannounced plans.
- Numerals Western, no em dashes, no tatweel, RTL correct. These are gate checks, not preferences.
