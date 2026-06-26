# Maharat Email Template Audit, Component Inventory

**Scope:** **45 distinct emails** (46 HTML files; one byte-level duplicate) covering Jan 2025 – Feb 2026, per `uploads/INDEX.md`, these collapse from 94 total Ortto sends. All are BEE/Ortto exports of Canva-built emails. Inventory only, no redesign.

**Brand system to map against:** dark bg `#141414` · primary green `#009975` · voice = "strategic operator, not motivational coach."

---

## STEP 1, Taxonomy

Section types used for classification. Extended from the starter set where templates forced it (▲ = added).

| Code | Section type | Definition |
|---|---|---|
| `LOGO` ▲ | Header / logo bar | Centered Maharat logo, ~118px, links home |
| `HERO` | Hero image | Full-width 590–600px banner image, top of body |
| `INTRO` | Intro / body copy block | Paragraph(s) of positioning copy, 14px |
| `IMG` | Image block | Standalone content image (feature still, single class card) |
| `CTA` | CTA button | Pill/rounded green button, one primary action |
| `PROMO` ▲ | Promo-code / urgency line | Code chip (EARLY20) + "valid 10 days / ends Mar 3" microcopy |
| `LEARN` | What-you'll-learn list | "You'll learn to:" heading + bullet text rows + "and so much more!" |
| `GRID` ▲ | Class / persona image grid | Row of linked class cards (3×190px) or "who is this for" personas |
| `STORY` ▲ | Positioning / story heading | Large heading restating instructor credibility ("built Brands For Less…") |
| `DIVIDER` ▲ | Divider | Hairline rule between sections |
| `TXN` ▲ | Transactional / account | Billing & account sends (payment failed, payment-method enabled), separate from marketing |
| `PARA` ▲ | Paragraph body (Era 3) | Structured `paragraph_block` editorial copy w/ inline images (Feb 2026 onward) |
| `FOOTER` | Footer | www.maharat.com line + social icon row + Unsubscribe |
| `PS` | P.S. / support line | (Not present as distinct block; closest = footer www line) |

*Not observed in any template: testimonial/story quote, author-bio block, true countdown timer (urgency is text-only), spacer (present once as structural `spacer_block`).*

---

## STEP 2, Inventory

Universal across all 10: body bg `#141414`, content width **600px**, button green `#009975`, font **Montserrat** (Verdana fallback), footer = www line + 6 social icons + Unsubscribe, image corner radius **8px**, direction **RTL** (9 AR / 1 mixed-EN).

### Batch 1

| # | Template | Lang | Ordered sections |
|---|---|---|---|
| 1 | `2025-01-11` العرض ينتهي قريباً | AR | LOGO · HERO · CTA · STORY(h20) · GRID(5×490 class) · CTA · FOOTER |
| 2 | `2025-01-26` اليوم العالمي للتعليم | AR | LOGO · HERO · INTRO(h20) · CTA · STORY(h20) · IMG · STORY(h20) · IMG · FOOTER |
| 3 | `2025-02-20` Toufic …Claim discount | EN | LOGO · HERO · INTRO · PROMO(code) · CTA · PROMO(valid 10d) · IMG · STORY(h22) · DIVIDER · LEARN(h18 + 5 bullets + "and so much more!") · CTA · FOOTER |
| 4 | `2025-02-20` صف توفيق …الخصم | AR | LOGO · HERO · INTRO · PROMO · CTA · PROMO · IMG · STORY · DIVIDER · LEARN · CTA · DIVIDER · STORY("شاهد أيضاً") · GRID(3×190 + wide) · FOOTER |
| 5 | `2025-02-21` صف جديد بانتظارك | AR | LOGO · HERO · INTRO · CTA · IMG · STORY · DIVIDER · LEARN · CTA · DIVIDER · STORY("see other classes") · GRID(3×190 + wide) · FOOTER |

**Batch-1 tokens**

| Token | Values seen | Notes |
|---|---|---|
| Heading sizes | 20 (T1–2), 22 / 18 (T3–5) | T1–2 single 20px head; T3–5 use 22 (section) + 18 (sub/list) |
| Body size | 14 (copy/bullets), 13 (footer www), 12 (unsubscribe/code) | consistent |
| Button | fill `#009975`; **radius 40px** (T1–2) vs **radius 4px** (T3–5); 15px (T1–2) / 18px (T3–5); Montserrat 700; pad ~5px×45px | radius + size split |
| Image aspects | hero 600w; class card 490w; logo 118w | T1 uses 490 class cards |
| Max content width | 600 | universal |
| Spacing | 4/5-pt multiples; row pad-top 20–25px; image side-pad 55px (490 imgs) | |
| One-off | T2 partner co-brand (Education Day, أعناب), no LEARN/GRID; alternating heading→image program list | |

### Batch 2

| # | Template | Lang | Ordered sections |
|---|---|---|---|
| 6 | `2025-02-26` Ending soon (EN) | EN | LOGO · HERO(590) · CTA · STORY(h16 urgency) · PROMO(h12 "ends Mar 3") · DIVIDER · "Who is this for?"(h26) · GRID(3×190 + 3×300 mobile) · IMG · STORY(h18) · DIVIDER · LEARN(5 bullets + "and so much more!") · CTA · DIVIDER · FOOTER |
| 7 | `2025-02-26` العرض ينتهي (AR) | AR | LOGO · HERO(590) · STORY(h22 urgency) · STORY(h16) · CTA · "لمن هذا الصف؟"(h33) · GRID(3×190 + 3×300) · IMG · STORY(h22) · DIVIDER · LEARN · CTA · IMG(wide) · FOOTER |
| 8 | `2025-02-28` رمضانكم علم ونور 🌙 | AR | LOGO · HERO · INTRO · IMG · SPACER · FOOTER (no CTA) |
| 9 | `2025-03-08` صف جديد …🌟 | AR | LOGO · HERO · INTRO · CTA · IMG · STORY · DIVIDER · LEARN · CTA · DIVIDER · STORY("see others") · GRID(3×190 + wide) · FOOTER |
| 10 | `2025-03-08` ابن مشروع أحلامك | AR | LOGO · HERO(590) · CTA · "لمن هذا الصف؟"(h33) · GRID(3×190 + 3×300) · IMG · STORY · DIVIDER · LEARN · CTA · DIVIDER · STORY("see others") · GRID(3×190 + wide) · FOOTER |

**Batch-2 tokens**

| Token | Values seen | Notes |
|---|---|---|
| Heading sizes | 33 ("who is this for"), 26, 22, 18, 16, 12 | **6 distinct sizes, no scale** |
| Body size | 14 / 13 / 12 | consistent w/ batch 1 |
| Button | fill `#009975`; **radius 4px**; 18px Montserrat 700 | T6–10 all squared 4px |
| Image aspects | hero 590–600w; persona grid 190w (3-up) + 300w (mobile 2-up dupes); class card 490 absent; wide 600 | grid ships duplicate desktop/mobile copies |
| Max content width | 600 | universal |
| One-off | T8 Ramadan: no CTA/LEARN/GRID, uses `spacer_block`, emoji 🌙; T6/T7 fine-print set as `<h2>` (heading misuse for 12px text) | |

### Batch 3

| # | Template | Lang | Ordered sections |
|---|---|---|---|
| 11 | `2025-03-08` ابن مشروع (-cf49686f) | AR | **Exact duplicate of T10**, LOGO · HERO(590) · CTA · "لمن هذا الصف؟"(h33) · GRID(3×190+300) · IMG · STORY(h22) · DIVIDER · LEARN · CTA · DIVIDER · STORY · GRID(3×190+wide) · FOOTER |
| 12 | `2025-03-13` استثمر هذا الرمضان (RMD20) | AR | LOGO · HERO · INTRO · CTA · STORY(h22 "ابدأ وتعلم") · GRID(**4×140**) · STORY(h19 "وأكثر…") · CTA · SPACER · IMG(wide) · FOOTER |
| 13 | `2025-03-13` رمضان شهر التطور (RMD20) | AR | LOGO · HERO · INTRO · CTA · INTRO(🌟) · INTRO("شاهد أبرز") · GRID(3×190) · CTA · SPACER · IMG(wide) · SPACER · FOOTER |
| 14 | `2025-03-29` عيدية مهارات 🌟 | AR | LOGO · HERO · INTRO · CTA · PROMO(urgency) · STORY(h22) · IMG(wide) · CTA · SPACER · IMG(wide) · FOOTER |
| 15 | `2025-04-17` Bassam's class 🌟 | EN | LOGO · HERO · CTA("Start watching") · INTRO · IMG · CTA("Get the class") · IMG · STORY(h18 "Watch our other classes") · GRID(3×200) · STORY(h16 "and much more…") · CTA("Start now") · FOOTER |

**Batch-3 tokens**

| Token | Values seen | Notes |
|---|---|---|
| Heading sizes | 33 / 22 / 19 / 18 / 16 | new 19px ("وأكثر"); scale sprawl continues |
| Button | fill `#009975` (T11–12,14–15), **but T13 = `#008970`** (off-brand green); radius **4px**; markup shifts `<div>`→`<span class="button">` (T15) | **T13 green conflict** |
| Grid widths | **140 (4-up)** new · 190 (3-up) · 200 (3-up) · 300 (mobile) | grid not yet standardized |
| CTA count | **T15 = 3 CTAs** (Start watching / Get the class / Start now) | violates one-primary rule |
| Body | 14 / 13 / 12 | consistent |
| One-off | T11 is a byte-level dup of T10; T13 uses off-brand green + emoji in body; multi-CTA pattern emerges (T15) | |

### Batch 4

| # | Template | Lang | Ordered sections |
|---|---|---|---|
| 16 | `2025-05-22` بسّام للعرايس 👰💄 | AR | LOGO · HERO · INTRO · CTA("احصل على الصف") · IMG · CTA("شاهد الصف") · STORY(h18 "صفوفنا الأخرى") · GRID(3×200) · STORY(h16 "وأكثر…") · CTA("ابدأ الآن") · FOOTER |
| 17 | `2025-06-03` Bassam's tools (cross-sell) | EN | LOGO · HERO · INTRO · CTA("Get the discount") · IMG · STORY(**h13** "…and so much more!") · CTA("Get the Class") · FOOTER |
| 18 | `2025-07-19` من صفّ واحد لمئات 🌟 | EN/AR | **Image-only**, LOGO · IMG(600) · IMG(600) · IMG(600) · FOOTER (no text/heading/button blocks) |
| 19 | `2025-07-23` سيدريك حداد 💫 | AR | LOGO · HERO(class link) · IMG · STORY(h18 "شاهدي صفوفنا") · GRID(3×200) · FOOTER (no CTA button) |
| 20 | `2025-07-25` سيدريك حداد 🪡 | AR | **Near-dup of T19**, LOGO · HERO · IMG · STORY(h18) · GRID(3×200) · FOOTER (no CTA button) |

**Batch-4 tokens**

| Token | Values seen | Notes |
|---|---|---|
| Heading sizes | 18 / 16 / **13** | T17 sets hype line as 13px `<h2>` (heading misuse again) |
| Button | fill `#009975`; radius **4px**; `<span class="button">` markup; T18–20 have **no button blocks** (CTA via linked images) | |
| Grid widths | 200 (3-up) dominant in batch | |
| CTA count | T16 = **3 CTAs**; T18–20 = **0 button CTAs** (image-driven) | two opposite extremes |
| Body | 14 / 13 / 12 | consistent |
| One-off | T18 fully image-based (no live text, a11y/dark-mode risk); T19≈T20 dup pair; T17 is product cross-sell (Bassam Fattouh cosmetics, partner co-brand, like T2 أعناب) | |

### Batch 5

| # | Template | Lang | Ordered sections |
|---|---|---|---|
| 21 | `2025-08-03` الفصل المجاني (Cedric) | AR | **Image-only**, LOGO · IMG(600,class) · IMG(600,class) · IMG(600) · FOOTER |
| 22 | `2025-08-28` الدفع عبر Meeza (**transactional**) | AR | LOGO · HERO · CTA("اشترك الآن") · IMG · CTA("فعّل اشتراكك") · FOOTER |
| 23 | `2025-10-27` إطلالات مميزة ✨ | AR | **Image-only**, LOGO · IMG(600) · IMG(600) · FOOTER |
| 24 | `2025-10-29` مشكلة في الدفع (**transactional**) | AR | **Image-only**, LOGO · IMG(600) · FOOTER (dunning/payment-failed) |
| 25 | `2025-10-31` لم تبدأ رحلتك 🌟 (re-engage) | AR | **Image-only**, LOGO · IMG(600) · IMG(600) · FOOTER |

**Batch-5 tokens**

| Token | Values seen | Notes |
|---|---|---|
| Dominant pattern | **Image-only** (4/5), no text/heading/button blocks; whole creative is a sliced Canva image | major shift mid-2025 |
| Button (T22 only) | fill **`#008970`** (off-brand) · radius **20px** · **14px** | **3rd button variant** (was 40px/4px) |
| New family | **Transactional** (T22 payment method, T24 payment failed), account/billing, not marketing | add `TXN` to taxonomy |
| Body | 13 / 12 (footer only) | no body copy blocks in image-only sends |
| Risk | image-only = no live text → a11y, dark-mode, deliverability (image-off) all degrade | |

### Batch 6

| # | Template | Lang | Ordered sections |
|---|---|---|---|
| 26 | `2025-10-31` 15 دقيقة ⏱️ | AR | **Image-only**, LOGO · IMG(600) · IMG(600) · FOOTER |
| 27 | `2025-11-20` ساعات قليلة … خصم 40% (gift) | AR | **Image-only**, LOGO · IMG(600) · FOOTER |
| 28 | `2025-11-21` الجمعة البيضاء خصم 40% | AR | **Image-only**, LOGO · IMG(600) · IMG(600) · FOOTER |
| 29 | `2025-11-21` الساعات الأخيرة خصم 40% | AR | **Image-only**, LOGO · IMG(600) · FOOTER |
| 30 | `2025-11-21` هدية خصم 40% | AR | **Image-only**, LOGO · IMG(600) · GRID(3×200) · FOOTER |

**Batch-6 tokens**

| Token | Values seen | Notes |
|---|---|---|
| Dominant pattern | **Image-only, 5/5** · all AR · all White-Friday / gift / 40%-off promo wave (Nov 2025) | |
| Button | none (0 button blocks across batch) | CTA entirely inside artwork |
| Grid | T30 keeps 3×200 linked-class row below the image | only non-image-only element in batch |
| Voice | heavy urgency: "ساعات قليلة", "الساعات الأخيرة", repeated 40% · emoji ⏱️🌟✨ | conflicts w/ strategic-operator voice |
| Footer | unchanged (www · social · unsubscribe) | the one truly stable component |

### Batch 7, image-only era continues (Nov–Dec 2025)

Names from `INDEX.md`. All bg `#141414`, all image-only (LOGO · IMG×n · [GRID 3×200] · FOOTER), zero button blocks.

| # | Template / INDEX name | Lang | Sections |
|---|---|---|---|
| 31 | `2025-11-21` warm acct created, email 1 | AR | LOGO · IMG(600) · IMG(600) · FOOTER |
| 32 | `2025-11-25` BLACK FRIDAY, Email 1 | AR | LOGO · IMG(600) · GRID(3×200) · FOOTER |
| 33 | `2025-11-25` BLACK FRIDAY, Email 2 | AR | LOGO · IMG(600) · IMG(600) · FOOTER |
| 34 | `2025-11-25` BLACK FRIDAY, Email 3 | AR | LOGO · IMG(600) · FOOTER |
| 35 | `2025-12-03` NEW PLAYLISTS, Everyday Recipes | AR | LOGO · IMG(600) · IMG(600) · GRID(3×200) · FOOTER |
| 36 | `2025-12-10` NEW PLAYLISTS, Building Your Brand | AR | LOGO · IMG(600)×3 · GRID(3×200) · FOOTER |
| 37 | `2025-12-20` ACCOUNT CREATED 1A, EOY | AR | LOGO · IMG(600)×3 · GRID(3×200) · FOOTER |
| 38 | `2025-12-20` ACCOUNT CREATED 2A, EOY | AR | LOGO · IMG(600) · IMG(600) · FOOTER |
| 39 | `2025-12-20` ACCOUNT CREATED 1B, EOY | AR | LOGO · IMG(600)×3 · GRID(3×200) · FOOTER |
| 40 | `2025-12-20` ACCOUNT CREATED 2B, EOY | AR | LOGO · IMG(600) · IMG(600) · FOOTER |

**Batch-7 tokens:** image-only is now the house style, the only recurring live-HTML components are LOGO, the optional 3×200 linked-class GRID, and FOOTER. The 3×200 "لمحة / browse our classes" strip is the one reusable module surviving the image-only shift (6 of 10 here).

### Batch 8, NEW design era (Feb 2026 “Elda” guide series)

**System change.** bg → **`#1b1b1b`** (was `#141414`) · standard green → **`#008970`** (was `#009975`) · button radius **4px** / **16px** · logo width now variable (148–214) · hero **590w** · returns to **live body copy** via a new `paragraph_block`. A genuine text-driven template again, first since Era 1.

| # | Template / INDEX name | Lang | Sections |
|---|---|---|---|
| 41 | `2026-02-01` Elda, Guide Email 2 | AR | LOGO(214) · HERO(590) · CTA("حمّل الدليل") · IMG · IMG · CTA("ابدأ الآن") · FOOTER |
| 42 | `2026-02-02` Elda, Guide Email 3 | AR | HERO(590) · CTA("ابدأ الآن") · FOOTER (no logo block) |
| 43 | `2026-02-03` Elda, Guide Email 4 | AR | LOGO · HERO · PARA · IMG · PARA×2 · CTA("اكتشف المزيد") · FOOTER |
| 44 | `2026-02-04` Elda, Guide Email 5 | AR | LOGO · HERO · PARA · IMG · PARA · IMG · CTA("اكتشف المزيد") · FOOTER |
| 45 | `2026-02-14` Love Day | AR | LOGO(148) · HERO · INTRO(14) · CTA("اهدِ اشتراك") · INTRO("لمحة عن صفوف") · GRID(3×180) · FOOTER |
| 46 | `2026-02-16` Elda, Email 1 (Account Creation) | AR | LOGO(177) · HERO · PARA · IMG · PARA · IMG · CTA("ابدأ المشاهدة") · PARA · IMG · FOOTER |

**Batch-8 tokens**

| Token | Era-3 value | vs earlier |
|---|---|---|
| Body background | **`#1b1b1b`** | was `#141414` (6/6 changed) |
| Button fill | **`#008970`** | was `#009975`, the off-brand green is now standard |
| Button | radius **4px** · **16px** · single CTA (except T41) | size drifted 18→16 |
| Body copy | **`paragraph_block`** (real text returns) | replaces image-only + old `text_block` |
| Logo width | 148 / 177 / 214 (variable) | was fixed 118 |
| Hero | 590w | was 600 |
| New module | inline image-between-paragraphs (editorial body) | not seen pre-2026 |

---

## STEP 2.5, Image-Only Email OCR Extraction & Analysis

The 22 image-only emails carry **no live HTML text**, every word is baked into a Canva-exported PNG. To audit them they were rendered (remote images proxied via the `ic.autopilotapp.com` CDN) and the artwork OCR'd. Text below is transcribed from the images; English is a gloss, not a second live language (these emails ship Arabic-in-pixels only).

### Extracted content

| # | Email | Headline (AR · gloss) | Offer / hook | CTA(s) | Recovered live-text sections (baked in) |
|---|---|---|---|---|---|
| T17 | Upgrade Feature Announcement | «كل الصفوف. باشتراك واحد.» · All classes, one subscription | upgrade single class → full library; exclusive discount; categories: business, art, style, cooking, music, acting | اشترك اليوم · فعّل اشتراكك الآن | HERO · BodyCopy · **Benefits list** (anytime/any device · certificates · new content · top Arab experts) · CTA |
| T18 | Cedric, design your style | «أتقني ستايلك» · Master your style | with stylist to Arab stars (Cedric Haddad); Sherine/Najwa looks → Prada/Valentino | شاهدي الصف | HERO+sub · BodyCopy · **LEARN list** (7 body-shape rules · 10 mistakes · 1 shirt 5 looks · smart-shopping · signed certificate · attachments) |
| T19 | Cedric, Accounts Created | (near-dup of T18 creative) | same class, accounts-created audience | شاهدي الصف | HERO · LEARN list |
| T20 | Cedric, LBD free class | «الفستان الأسود… بطريقة جديدة» · The black dress, a new way | **free lesson**; 8 looks from one LBD; everyday→event | شاهدي الفصل · اشتركي في مهارات | HERO+sub · BodyCopy · **Steps list** (create account → class page → watch lesson 8) · closing line |
| T22 | Beauty Persona Announcement | «كل الأسرار لإطلالة مميزة في مكان واحد» · All the secrets in one place | Bassam + Cedric; makeup + wardrobe | ابدئي رحلتك اليوم | HERO · BodyCopy · **class cards** (3) · **"You'll get" list** (9+ makeup looks · 17 wardrobe ideas · colour/fabric secrets · skincare routines) |
| T23 | Failed Payment *(TXN)* | «أهلاً بك على مهارات» · Welcome to Maharat | payment-failed dunning; reassurance | اشترك الآن | HERO · BodyCopy (apology) · **Steps list** (try another method · contact bank · email support@maharat.com) · closing |
| T24 | playlists acct created e2 | «كن أفضل نسخة من نفسك» · Be the best version of you | playlists make starting easy | اشترك الآن | HERO+sub · BodyCopy · **stat row** (15 min daily · 150+ lessons · 20+ playlists) · BodyCopy · playlist names |
| T25 | playlists acct created e3 (15 min) | «استثمر في نفسك» · Invest in yourself | 150+ lessons, <15 min/day | اشترك الآن · ابدأ الآن | HERO (laptop) · BodyCopy · **instructor card row** (7) |
| T26 | BF Subscribers e2 | «اهدِ اشتراك مع خصم 40%» · Gift a subscription, 40% off | gift annual sub; offer ends today | أرسل اشتراك الآن | badge(urgency) · HERO · CTA · BodyCopy |
| T27 | BF New Account e1 | «عرض الجمعة البيضاء, احصل على خصم 40%» | annual sub, unlimited access | اشترك الآن | instructor row · HERO · BodyCopy · **Benefits list** |
| T28/T33 | BF New Accounts e3 / BF Email 3 | «احصل على خصم 40%» · Start next year as your best self | annual content all year | اشترك الآن | badge · instructor row · HERO · BodyCopy |
| T29 | BF Subscribers e1 | «اهدِ اشتراك مهارات بخصم 40%» · A gift that lasts all year | gift annual sub | أرسل هدية الآن · أرسل اشتراك مهارات | HERO+sub · CTA · BodyCopy |
| T30 | warm acct created e1 | «MAHARAT PLAYLISTS LIVE NOW» · قوائم مهارات متاحة الآن | new playlists; 15 min/day; 150+ lessons | اشترك الآن · ابدأ الآن | HERO(eyebrow+title) · BodyCopy · **playlist-card grid** (6, w/ lesson counts) |
| T31 | BF Email 1 | «احصل على خصم 40%» · develop your passion w/ top experts | annual sub, all categories | اشترك الآن | instructor row · HERO · BodyCopy · Benefits list |
| T32 | BF Email 2 | «احصل على خصم 40%, العرض ينتهي غداً» · Learn more for less | offer ends tomorrow | (image CTA) | badge(urgency) · HERO · instructor mosaic · BodyCopy |
| T34 | New Playlists, Everyday Recipes | «اكتشف أشهى الوصفات اليومية مع الشيف سلام دقاق» | Chef Salam playlist; appetizers→desserts | ابدأ المشاهدة · اشترك الآن | HERO+sub · BodyCopy · **dish image strip** · footer line |
| T35 | New Playlists, Building Your Brand | «اكتشف أسرار البراند القوية» · Secrets of strong brands | w/ Rahma Riad + Toufic Kreidieh; brand from zero | شاهد القائمة الآن · اشترك الآن | HERO · BodyCopy · **LEARN list** (define story · voice · visual identity · audience · channels) |
| T36 | Account Created 1A/1B EOY | «كل المهارات التي تحتاجها في اشتراك واحد» · one subscription | 1B variant adds **30% off** annual | استفد من العرض · ابدأ الآن | HERO · BodyCopy *("every lesson designed to be applied, not just watched")* · offer line |
| T37 | Account Created 2A/2B EOY | «ابدأ رحلتك مع مهارات» · Start your journey | **30% off**; learn from people who built their careers | اشترك مع خصم 30% | HERO · BodyCopy *("the difference between consuming content and actual progress")* |

*(T18≈T19, T28≡T33 share creative; instructor-card / playlist-card rows reuse the same headshot assets across many sends.)*

### What the OCR reveals

1. **Image-only ≠ structureless.** Decompiled, these emails use the **same components as Era 1**, HERO, BodyCopy, LEARN/steps/benefits lists, class- & playlist-card grids, CTA, just flattened into pixels. So they *are* componentizable; the artwork simply has to be rebuilt as live MJML. This strengthens the recommended library (no new component types needed; add **BenefitsList**, **StatRow**, **PlaylistCardGrid**, **StepsList** as list variants).
2. **The strongest brand-voice copy is trapped in images.** The EOY account-created lines, «كل درس مصمم ليطبّق، لا ليشاهد فقط» (*every lesson designed to be applied, not just watched*) and «الفرق بين استهلاك المحتوى وبين التقدّم الفعلي» (*the difference between consuming content and actual progress*), are the **best "strategic-operator" voice in the whole archive**, yet they're un-selectable, un-translatable, and invisible to search/preview. Pull this copy into live text at rebuild.
3. **Two voices coexist.** Promo waves (BF, gifting) lean urgency/discount («العرض ينتهي غداً», repeated 40%); lifecycle/onboarding (playlists, account-created, failed-payment) is calmer and more operator-toned. The rebuild should keep the latter and dial back the former.
4. **CTAs are buried in artwork**, «اشترك الآن / ابدأ الآن / شاهدي الصف» live inside the PNG, so they can't be A/B tested, localized, or made tappable-accessible. Every recovered CTA maps cleanly onto the `Button` component.
5. **Accessibility/deliverability cost is total**, zero `alt` text, zero live copy: screen-readers read nothing, image-blocking shows a blank email, dark-mode can't adapt, and link tracking is limited to the whole-image href.

---

## STEP 3, Consolidation (final, n = 45 distinct emails)

*45 distinct emails (46 files; `2025-03-08 …-cf49686f` is a byte dup of T10, excluded from counts). Represents 94 total sends per `INDEX.md`.*

### The headline finding: three design eras

| Era | Window | Count | Signature | bg / green / button |
|---|---|---|---|---|
| **1, Structured blocks** | Jan–Jun 2025 | 16 | Live HTML: hero · intro · CTA · STORY · LEARN list · class GRID. Content-rich. | `#141414` / `#009975` / 4px (40px pill in Jan) |
| **2, Image-only** | Jul–Dec 2025 | 23 | Whole creative = sliced Canva image; only LOGO + (opt) GRID + FOOTER are live HTML. CTA baked into artwork. | `#141414` /, / no buttons |
| **3, New text system** | Feb 2026 | 6 | Returns to live `paragraph_block` body + single CTA; editorial image-between-paras. | **`#1b1b1b`** / **`#008970`** / 4px·16px |

This is the dominant fact of the audit: **the "component system" the brand actually runs on today is barely HTML at all**, roughly half of all 2025 sends are flat images, and the 2026 reboot quietly moved off both brand-target tokens.

### Frequency table, section types (n = 45)

| Section | Count | % | Canonical? |
|---|---|---|---|
| FOOTER | 45 | 100% | ✅ core |
| LOGO (header) | 44 | 98% | ✅ core |
| HERO (top image) | 44 | 98% | ✅ core |
| IMG (additional content image) | ~38 | 84% | ✅ core |
| CTA button | 23 | 51% | ✅ core (absent in all image-only) |
| GRID (class cards 140–200px) | 17 | 38% | ✅ core |
| INTRO / PARA body copy | 16 | 36% | ✅ core |
| STORY / positioning heading | 12 | 27% | ⚠ Era-1/3 |
| SPACER | 8 | 18% | structural |
| LEARN list | 7 | 16% | ⚠ Toufic-only |
| DIVIDER | 7 | 16% | ⚠ Toufic-only |
| PROMO / urgency line | 7 | 16% | ⚠ optional |
| TXN (account/billing) | 2 | 4% | ⚠ separate track |
| Testimonial / Author-bio / Countdown / P.S. | 0 | 0% |, never used |

### Archetype frequency (how emails actually cluster)

| Archetype | Count | Examples |
|---|---|---|
| Image-only promo / announcement | 20 | Black Friday ×6, EOY account-created ×4, New Playlists ×2, Beauty Persona, Upgrade, re-engage |
| Structured class-launch (long-form) | 7 | Toufic EN/AR ×7 (hero+intro+CTA+STORY+LEARN+GRID) |
| Promo blast (light copy + grid) | 6 | Jan EOY, Ramadan ×2, Eid, Bassam welcome/bridal |
| Era-3 guide / editorial | 6 | Elda Guide 2–5, Email 1, Love Day |
| Transactional (account/billing) | 2 | Failed Payment, Meeza/TPAY |
| Partner co-brand | 2 | Aanaab (Education Day), Bassam tools |
| Seasonal greeting (no CTA) | 2 | Ramadan 2025, (Cedric image sends) |

### Recurring components, modal / canonical values (all eras)

| Component | Canonical value | Variants observed |
|---|---|---|
| Content width | **600px** | universal, 0 variation |
| Body background | **`#141414`** (39/45) | `#1b1b1b` (6/45, Era 3), **drift** |
| Button fill | **`#009975`** (Era 1) | `#008970` (Era 3 + 2 strays), **drift** |
| Button radius | **4px** (most) | 40px pill (Jan ×2) · 20px (Meeza) |
| Button text size | 18px (Era 1) | 16px (Era 3) · 14/15px (strays) |
| Button font | Montserrat 700, `<div>`→`<span>` markup over time | |
| Heading sizes | no scale | **13/16/18/19/20/22/26/33**, 8 sizes |
| Body / paragraph | **14px** | `text_block` → `paragraph_block` in Era 3 |
| Footer www line | **13px** white | universal |
| Fine print / unsubscribe | **12px** (→11px span) | universal |
| Hero image | **600w** | 590w (Era 3 + late 2025) |
| Class-card grid | **3×200w** (late) | 5×490 · 4×140 · 3×190 · 3×180, 5 widths |
| Image corner radius | **8px** | 6px once |
| Logo width | **118px** | 148 / 177 / 214 (Era 3) |
| Social row | 6 icons (FB/X/IG/LI/TikTok/YT/Snap) 32px | universal |
| Footer block | www · social · unsubscribe | **the only 100%-stable component across all 3 eras** |

### Conflicts with the brand system (`#141414` / `#009975` / strategic-operator voice)

| # | Where | Conflict | Severity |
|---|---|---|---|
| 1 | **Image-only emails (23/45)** | No live text, fails accessibility, dark-mode, image-blocking clients, and is **un-componentizable in MJML** (nothing to template). Largest single issue. | 🔴 high |
| 2 | Era-3 background | `#1b1b1b` ≠ brand `#141414`. | 🔴 high |
| 3 | Era-3 + strays green | `#008970` ≠ brand `#009975` (8 emails). | 🔴 high |
| 4 | Button geometry | radius 4 / 20 / 40px and size 14/15/16/18px, no canonical. | 🟡 med |
| 5 | Heading scale | 8 distinct sizes (13–33), no ramp; 12–13px text marked up as `<h2>`. | 🟡 med |
| 6 | Typeface | All **Montserrat** incl. Arabic body, DS mandates IBM Plex Sans Arabic for AR (+ Fraunces/Plus Jakarta). | 🟡 med |
| 7 | Voice | Urgency/hype: "الساعات الأخيرة", "Grab your discount", "and so much more!", motivational-coach, not strategic-operator. | 🟡 med |
| 8 | Emoji | 🌙🌟💫⏱️👰💄🪡 in subjects/headings, DS rule is no emoji. | 🟡 med |
| 9 | Grid dupes | persona/class grids ship duplicate desktop(190)+mobile(300) image sets via `mobile_hide`/`desktop_hide`. | 🟢 low |
| 10 | bg/green (Era 1) | ✅ **No conflict**, `#141414` + `#009975` already match the target exactly. The brand target *is* Era 1; the job is to pull Eras 2–3 back to it. |, |

---

## Recommended Component Library

Minimal MJML set that covers the majority of the 45. Tokens are the canonical picks **reconciled to the brand system** (Era-1 values win where they already match; Era-2/3 drift is corrected). Bracketed notes = the correction.

| Component | Canonical tokens |
|---|---|
| **`EmailShell`** | `<mj-body width=600>` · bg **`#141414`** [pull Era-3 `#1b1b1b` back] · RTL default (`dir=rtl`, `lang` swap for EN) · Montserrat now [→ IBM Plex Sans Arabic / Plus Jakarta at full rebrand] |
| **`LogoBar`** | logo **118px** [normalize Era-3 148–214] · centered · pad-top 20px · links maharat.com |
| **`Hero`** | `<mj-image>` 600w · radius 8px · full-bleed · **alt required** (covers image-only top slice too) |
| **`BodyCopy`** | 14px · line-height 150% · white · maps both `text_block` + Era-3 `paragraph_block` [voice: strategic, drop hype] |
| **`Button`** | fill **`#009975`** [pull `#008970` back] · #fff · **16–18px Montserrat 700** · **radius: pick ONE, 28px pill (matches product DS) or 4px** · one primary per email [collapse Era-1 multi-CTA] |
| **`SectionHeading`** | from a fixed scale **H1 28 / H2 22 / Sub 18** · Montserrat 700 · center [replaces the 8-size sprawl] |
| **`LearnList`** *(opt)* | Sub-heading lead + 14px bullet rows · drop "and so much more!" closer |
| **`PromoLine`** *(opt)* | code chip + 14px microcopy [reframe urgency in operator voice; no countdown theatrics] |
| **`Divider`** *(opt)* | hairline rule · full content width |
| **`ClassCardGrid`** | **3-up, 200w** linked cards [standardize from 140/180/190/490] · **one responsive image, not desktop/mobile dupes** · radius 8px · the most reusable surviving module |
| **`FeatureImage`** | single 600w image · radius 8px · optional link |
| **`Footer`** | www 13px + 6 social icons 32px + Unsubscribe 11–12px · white on `#141414` · **already 100% stable, lift verbatim** |

**Type scale to enforce:** H1 28 / H2 22 / Sub 18 / Body 14 / Footer 13 / Fine 12, collapses 8 ad-hoc sizes into 6 steps.

**Two structural decisions block the MJML rebuild:**
1. **Image-only emails (23/45) must be re-authored as real MJML** (hero image + live text + `Button` + `ClassCardGrid`) or they cannot be componentized, themed, or made accessible. This is the bulk of the work, not a detail.
2. **Pick one button** (recommend 28px pill, `#009975`) and **one background** (`#141414`), retire the Era-3 `#1b1b1b`/`#008970` drift.

**Coverage:** the 12 components above reproduce **all 16 Era-1 + all 6 Era-3 emails**, and the **content of every image-only email** once its artwork is decomposed into Hero + BodyCopy + Button + ClassCardGrid.
