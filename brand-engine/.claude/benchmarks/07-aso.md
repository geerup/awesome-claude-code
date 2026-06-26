# Benchmark: app store optimization

Internet benchmark for the Maharat ASO stream. It pulls authoritative real-world ASO frameworks
(App Store and Google Play guidelines plus recognized ASO practitioners), compares them to our
skills, and lists prioritized recommendations. It does not edit any skill file. It is a reference.

Scope checked against our files: `skills/aso/SKILL.md`, `skills/aso/aso-keyword-research/`,
`skills/aso/store-listing-optimization/`, `skills/aso/store-creative-and-experiments/` (each
SKILL.md plus template), `sops/aso.md`, and the `aso-package` block in
`runtime/handoff-contract.md`.

---

## Sources reviewed (web)

- Apple Developer, Product Page Optimization and App Store Connect help on PPO tests:
  [developer.apple.com/app-store/product-page-optimization](https://developer.apple.com/app-store/product-page-optimization/),
  [App Store Connect: overview of PPO tests](https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization/)
- Apple Developer, Ratings, reviews, and responses:
  [developer.apple.com/app-store/ratings-and-reviews](https://developer.apple.com/app-store/ratings-and-reviews/),
  and SKStoreReviewController:
  [developer.apple.com/documentation/storekit/skstorereviewcontroller](https://developer.apple.com/documentation/storekit/skstorereviewcontroller)
- Google Play Console, Store listing experiments:
  [play.google.com/console/about/store-listing-experiments](https://play.google.com/console/about/store-listing-experiments/)
- AppTweak, ASO strategy and best practices, custom product pages, reviews, and Arabic and Hebrew
  localization:
  [ASO best practices](https://www.apptweak.com/en/aso-blog/app-store-optimization-aso-best-practices),
  [ASO strategy framework](https://www.apptweak.com/en/aso-blog/aso-strategy),
  [guide to custom product pages](https://www.apptweak.com/en/aso-blog/guide-to-custom-product-pages-cpp),
  [the 2026 guide to app store reviews](https://www.apptweak.com/en/aso-blog/app-store-reviews),
  [localize your ASO in Hebrew and Arabic](https://www.apptweak.com/en/aso-blog/why-you-should-localize-your-aso-in-hebrew-arabic)
- MobileAction, PPO A/B testing, Play store listing experiments, and how to respond to reviews:
  [product page optimization](https://www.mobileaction.co/blog/product-page-optimization/),
  [Google Play store listing experiments](https://www.mobileaction.co/blog/google-play-store-listing-experiments/),
  [how to respond to app store reviews](https://www.mobileaction.co/guide/how-to-respond-to-app-store-reviews/)
- AppFollow, ASO ranking factors, screenshots best practices, and review management:
  [ASO ranking factors](https://appfollow.io/blog/aso-ranking-factors),
  [ASO screenshots best practices](https://appfollow.io/blog/aso-screenshots-best-practices)
- TheAppLaunchpad and AppScreenshotStudio, screenshot and preview-video conversion guidance:
  [App Store screenshot guidelines 2026](https://theapplaunchpad.com/blog/app-store-screenshot-guidelines/),
  [App Store preview videos 2026 conversion guide](https://appscreenshotstudio.com/blog/app-store-preview-videos-the-2026-conversion-guide)
- RespectASO and Adapty, custom product pages in 2026:
  [custom product pages guide 2026](https://respectaso.com/blog/custom-product-pages-app-store-guide-2026/)

---

## Best-in-class elements

What strong ASO practice, and the platform owners themselves, treat as the standard.

1. Two stores, two ranking models. App Store ranks on the title, the subtitle, and a separate
   hidden keyword field. Google Play has no keyword field; it ranks on the title, the short
   description, and the full description text. Best practice treats the two as different machines,
   not one listing translated twice. (AppTweak, AppFollow)

2. Field character limits and indexing rules. App Store title and subtitle are about 30 characters
   each; the keyword field is 100 characters, comma separated, no spaces, no repeats across fields,
   and no stop words like "app" or "the" that Apple indexes automatically. Google Play title is
   30 characters, short description 80, full description 4000, with a recommended primary keyword
   density near 2 to 3 percent and no stuffing. (AppTweak, Apple, Google)

3. Keyword research as relevance, volume, difficulty. Score every candidate term on relevance to
   the app, search volume, and difficulty or chance to rank, then prioritize. Read competitor
   listings to find gaps to own. (AppTweak ASO strategy framework)

4. Localization beats translation, and culturalization beats both. Localized creatives and metadata
   outperform translated ones because user motivation changes by market. For Arabic and MENA,
   RTL-correct rendering, linguistic brevity, and culturally native wording are explicit
   requirements, not polish. AppTweak supports Arabic keyword research specifically. (AppTweak
   Arabic localization, yellowHEAD, Contentech)

5. Screenshots carry the conversion. The first 1 to 3 screenshots drive most install decisions;
   about 90 percent of users never scroll past the third. Communicate value in under 2 seconds,
   show real in-app UI (Apple expects actual UI), use high-contrast and on-brand color, and provide
   3 to 8 screenshots at current base device sizes. Google Play caption text should occupy no more
   than about 20 percent of a screenshot. (TheAppLaunchpad, AppFollow, AppTweak)

6. Preview video as a silent film. App preview videos are 15 to 30 seconds, autoplay muted in
   search, and can lift install conversion 15 to 30 percent paired with strong screenshots. They
   must work with captions and no sound, and the poster frame should match the first screenshot so
   click-through does not tank. (AppScreenshotStudio, AppTweak)

7. One variable per experiment, run for full weekly cycles. App Store Product Page Optimization
   (PPO) tests up to 3 treatments against the original, changing only icon, screenshots, or app
   previews, and runs up to 90 days. Google Play store listing experiments test one asset at a
   time (icon, screenshots, video, text), with at least 7 days to cover weekday and weekend traffic.
   Never test two attributes at once. (Apple, Google Play Console, MobileAction)

8. Custom Product Pages alongside PPO. As of 2026 Apple allows up to 70 Custom Product Pages, each
   with its own screenshots, previews, promotional text (170 characters), and, since mid 2025, its
   own assigned keywords so a CPP can surface in organic search. Recommended workflow: use PPO to
   find a winning creative, then deploy it as a CPP for the audience that responded best. (Apple,
   RespectASO, Adapty, AppTweak)

9. Ratings and reviews are a ranking input, not just sentiment. Apps below 3.5 stars rank for far
   fewer top keywords; lifting rating drives downloads. Both stores weigh overall rating, review
   velocity, and sentiment. On Google Play, developer responses are indexed, so replies double as
   an ASO tactic. Best practice replies fast (the 72-hour norm is now table stakes), prioritizes
   fresh reviews, and mines review text for product and messaging signal. (AppFollow, AppTweak,
   MobileAction, ASO World)

10. Prompt for reviews in-app, the right way. Apple's SKStoreReviewController is the official
    in-app rating prompt; Apple caps it at 3 prompts per user per 365 days and may suppress it.
    Best practice triggers the prompt after a positive moment, never mid-task. (Apple)

11. Icon as a ranked conversion asset. The app icon is a first-impression and a testable variable
    in both PPO and Play experiments; strong practice treats it as part of the creative test set.
    (AppFollow, Apple, Google)

---

## Our coverage

Where our skills already meet the bar, with file citations.

- Two-stores, two-languages model is explicit. `skills/aso/aso-keyword-research/SKILL.md` (the "two
  stores, two languages" section) states App Store ranks on title, subtitle, and a separate keyword
  field, and Google Play ranks on title and description with no keyword field. The template
  `skills/aso/aso-keyword-research/templates/aso-keyword-research.md` carries the same field
  weighting reminder.
- Field character limits are encoded. `skills/aso/store-listing-optimization/SKILL.md` lists App
  Store title and subtitle about 30 chars, keyword field about 100 chars comma separated, and
  Google Play title 30, short description 80, full description carries ranking weight. The
  `store-listing.md` template has limit columns per field.
- Keyword research scored on relevance, volume, difficulty. `aso-keyword-research/SKILL.md` steps 3
  to 5 record relevance, volume signal, and difficulty signal per term, plus a competitor read with
  "gaps to own," then prioritizes. The template mirrors this with a keyword map, competitor read,
  and prioritized-targets tables.
- Localization is first-class and English-first. Every skill states English-first with English on its
  own terms, never a translation afterthought, and ties locale scope to the brief
  (`skills/aso/SKILL.md` step 5, `aso-keyword-research/SKILL.md`, `store-listing-optimization/SKILL.md`).
  `sops/aso.md` calls for parallel AR and EN localization and RTL-correct rendering.
- Screenshot and preview direction, mapped to benefit and segment.
  `skills/aso/store-creative-and-experiments/SKILL.md` directs the screenshot set and preview video
  per store and locale, each mapped to a benefit and segment, with overlay slots. The template adds
  a dimensions and safe-area column and visual constants.
- One-variable experiments tied to the success metric. `store-creative-and-experiments/SKILL.md`
  names App Store PPO and Google Play store listing experiments, requires one hypothesis and one
  variable each, a success_metric-tied metric, and a decision rule, and forbids changing more than
  one variable. The template has a one-variable experiment table.
- Reviews response policy with escalation. `store-creative-and-experiments/SKILL.md` sets on-brand
  AR and EN reply templates and escalation for bug, refund, privacy, safety, or legal reviews, and
  forbids exposing a reviewer's personal data. The template enumerates themes and actions.
- Gated publish and the human gate throughout. `skills/aso/SKILL.md`, `sops/aso.md`, and the
  `aso-package` block in `runtime/handoff-contract.md` all treat any store publish or experiment
  launch as a gated action; silence is not approval.
- Text-free generation with overlay in build, and brand and compliance hard rules (no accreditation,
  no invented Skill Path titles or instructor names, no em dashes, no tatweel, Western numerals)
  are repeated in every skill and template.

## Gaps and missing elements

Prioritized. P1 is a real-world standard we do not name and that would change the work product.

- P1. Custom Product Pages are absent. No skill or template mentions Apple CPPs, the 70-page limit,
  per-CPP keywords (live since mid 2025), the 170-character promotional text, or the PPO-then-CPP
  workflow. This is a 2026 standard and a direct match to our segment-mapped screenshot direction.
  Files: `store-creative-and-experiments/SKILL.md`, `store-listing-optimization/SKILL.md`.
- P1. Experiment run-length and traffic discipline are unstated. We require one variable but never
  state the minimum read window. Real-world rule: at least 7 days on Play to cover the weekly cycle,
  up to 90 days on Apple PPO, with a 3-treatment cap on PPO. Our template has a decision rule column
  but no read-window or treatment-count guidance. File: `store-creative-and-experiments/SKILL.md`
  and its template.
- P1. The App Store keyword-field mechanics are under-specified. We say "comma separated, no wasted
  spaces" but do not encode: no stop words Apple already indexes ("app," "the"), no word repeated
  across title, subtitle, and keyword field (waste), and singular-versus-plural and cross-field
  combination rules. File: `store-listing-optimization/SKILL.md` and `store-listing.md`.
- P2. Ratings and reviews as a ranking input is not stated. Our reviews policy is about replies and
  escalation, but never states that rating, review velocity, and sentiment feed store ranking, that
  Google Play indexes developer responses (so AR and EN reply wording is itself an ASO lever), or a
  response-time target. File: `store-creative-and-experiments/SKILL.md`.
- P2. No in-app review-prompt guidance. SKStoreReviewController and the Play in-app review API, the
  3-prompts-per-365-days cap, and "prompt after a positive moment" are absent. This is the engine
  that raises rating velocity that ASO then benefits from. File: `store-creative-and-experiments/SKILL.md`.
- P2. Screenshot conversion heuristics are not encoded. We map screenshots to benefit and segment
  but never state the first-3-screenshots rule, value-in-2-seconds, real-UI requirement, Play's
  20-percent caption-area limit, or the 3-to-8 count. File: `store-creative-and-experiments/SKILL.md`
  and its template.
- P2. Preview-video specifics missing. No 15-to-30-second length, no silent-autoplay and captions
  rule, no poster-frame-matches-first-screenshot rule, no conversion-lift expectation. The template
  has a preview-video row but no spec guidance. File: `store-creative-and-experiments/SKILL.md`.
- P3. App icon is not called out as a tested creative asset. It appears once in `sops/aso.md`
  ("screenshots, the preview video, and the icon") but the creative skill's experiment list and
  screenshot table do not treat the icon as a first-class testable variable. File:
  `store-creative-and-experiments/SKILL.md`.
- P3. Google Play feature graphic and the 1024 x 500 spec are absent from the creative template,
  which lists screenshots and preview video but not the mandatory Play feature graphic. File:
  `store-creative-and-experiments/templates/store-creative-and-experiments.md`.
- P3. Keyword-density guidance for the Google Play full description (about 2 to 3 percent primary)
  is not stated, though we correctly note the full description carries ranking weight. File:
  `store-listing-optimization/SKILL.md`.

## Where ours is stronger

Where the engine goes beyond the generic best-in-class playbook.

- English-first localization, not a bolt-on. The web sources treat Arabic and RTL as a market to
  "expand into." Our skills make Arabic the primary field with English on its own terms across every
  field and signal, with RTL correctness and Gulf-familiar wording as hard rules, tied to the brief
  locale scope and never guessed.
- Text-free generated images with overlay added in build. No generic ASO guide enforces this. We
  forbid baking Arabic (or any) text into a generated image and add overlays in the build, which is
  the correct way to keep RTL rendering, kerning, and Western numerals correct in Arabic creative.
- One-variable experiment discipline as a hard rule, not a tip. Sources recommend single-asset
  tests; we make it a non-negotiable with a hypothesis, a single variable, a success_metric-tied
  metric, and a decision rule, enforced by skill eval.
- No invented Skill Path titles, lineup, instructor names, offers, or prices, plus no accreditation
  implication, in every store field, creative, and review reply. Generic ASO advice has no such
  guardrail; ours is enforced through copy QA, compliance, and brand QA gates.
- Store-publish and experiment-launch are gated behind an explicit human gate, per change and per
  campaign, with silence never counting as approval. The web playbooks assume the practitioner just
  ships; our engine stages and stops.
- Every customer-facing store asset runs a defined gate chain (skill eval, arabic-copy-qa or
  english-copy-qa, design-qa, compliance-privacy-check, brand-qa-reviewer) before it can advance,
  which no external ASO source formalizes.

## Recommendations

Specific, prioritized, each tied to a source. Edits only; no skill file is changed by this doc.

1. P1. Add Custom Product Pages to `store-creative-and-experiments/SKILL.md` and the listing skill.
   State the PPO-then-CPP workflow, the 70-page limit, per-CPP keywords (mid-2025), and 170-char
   promotional text, and add a CPP row to the creative template mapping each CPP to a segment and an
   assigned keyword set. Source: Apple, AppTweak custom product pages guide, RespectASO.
2. P1. Encode experiment run-length and treatment limits in `store-creative-and-experiments/SKILL.md`
   and its template: minimum 7 days on Play to cover a weekly cycle, up to 90 days and 3 treatments
   on Apple PPO, single asset per test. Add a "read window" column next to the decision rule.
   Source: Google Play Console, Apple App Store Connect, MobileAction.
3. P1. Tighten the App Store keyword-field rules in `store-listing-optimization/SKILL.md` and the
   `store-listing.md` template: no Apple-indexed stop words ("app," "the"), no word repeated across
   title, subtitle, and keyword field, exploit singular-or-plural and cross-field combinations, and
   add a Google Play full-description primary-keyword density of about 2 to 3 percent. Source:
   AppTweak ASO best practices.
4. P2. Add a "reviews as a ranking input" note and a response-time target to
   `store-creative-and-experiments/SKILL.md`: rating, velocity, and sentiment feed ranking; Google
   Play indexes developer responses so AR and EN reply wording is an ASO lever; target fast replies
   on fresh reviews. Source: AppFollow, AppTweak reviews guide, MobileAction.
5. P2. Add an in-app review-prompt line: trigger SKStoreReviewController (iOS) and the Play in-app
   review API after a positive moment, respect the 3-prompts-per-365-days cap, never interrupt a
   task. File: `store-creative-and-experiments/SKILL.md`. Source: Apple SKStoreReviewController.
6. P2. Encode screenshot and preview heuristics in the creative skill and template: first 3
   screenshots carry the decision, value in under 2 seconds, real in-app UI, Play caption area under
   about 20 percent, 3 to 8 screenshots; preview video 15 to 30 seconds, silent with captions,
   poster frame matching the first screenshot. Source: TheAppLaunchpad, AppFollow,
   AppScreenshotStudio.
7. P3. Name the app icon as a first-class tested creative asset in the experiment and screenshot
   tables, and add the Google Play feature graphic (1024 x 500, localized) to the creative template.
   Source: AppFollow, Google Play screenshot and feature-graphic guidance.
