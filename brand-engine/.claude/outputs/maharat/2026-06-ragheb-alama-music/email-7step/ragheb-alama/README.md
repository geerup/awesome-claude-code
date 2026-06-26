# Email 7-step: Ragheb Alama, Teaches Music and Performance (nurture-to-subscribe, slotted build)

Status: draft, not approved, nothing sends. Blocked on catalog status. Approval-ready HTML that
stops at the human gate, the same status as the existing Bassam makeup build.

Fourteen self-contained, slotted, live-component emails (E1 to E7, Arabic and English) built to
the Maharat email standard (the Elda reference): `context/email-design-system.md` (tokens, the
12+1 component library, brand fonts, themes) and `runtime/email-module-map.md` (the slot, role,
lang, copy-id contract and gate routing). Bound to claims-disciplined copy authored by
copywriter-ar (AR and EN) from the instructor's pack
(`skills/instructor-marketing/ragheb-alama/` SKILL.md, voice.md, masterclass-pages.md) plus
`context/brand-voice.md`. Nothing invented: no price, plan, date, lesson count, award, or fact
outside the pack.

## The 7-step arc

1. Welcome / intro to the class (watch).
2. Why this skill and why this instructor (watch).
3. What you will learn (carries the ListBlock, emerald-bullet "what you will learn").
4. The free first lesson (watch the first lesson free).
5. The instructor's credibility (watch).
6. Momentum and what you will be able to do (keep going).
7. The offer: subscribe.

Steps 1 to 6 are watch-focused; step 7 is the subscription offer. One primary CTA per email.

## Header image (gate-zero) and send-readiness

- Header source: CloudFront (verified servable at source, NOT an approved email host).
- `src`: `https://dt92b02v6m7lx.cloudfront.net/RA_CLASSCOVER_DESKTOP_01_NOGRADIENT.webp`
- Send-readiness (per `context/instructors/_EMAIL-IMAGE-MANIFEST.md`): BLOCKED: stage header to Ortto CDN. Header verified servable on CloudFront only.
- Deliverability note: Header is the verified CloudFront CLASSCOVER. CloudFront is NOT an approved email host: stage the bytes to the Ortto CDN (or prove with an inbox send-test) and swap the src before any send. Draft is fine.

The header is the gate-zero precondition (`skills/email-asset-qa` check 0). A raw
`dt92b02v6m7lx.cloudfront.net` cover is verified at source but is NOT an approved email host: it
must be staged to the Ortto CDN (`m.autopilotapp.com`, `ic.autopilotapp.com`) or proven with an
inbox send-test before the build is send-ready. Drafts are fine.

## What "slotted live-component" means here

- Every line of copy is a LIVE HTML text slot (`data-slot="copy"`) bound to a stable
  `data-copy-id` (`email-ragheb-alama-<id>-<role>-<lang>`; eyebrow and footer sender are
  campaign-stable). Copy is never baked into an image and never rewritten in the build.
- Every image is text-free (`data-slot="element"`) with descriptive alt: the LogoBar (autopilot
  CDN logo), the Hero (the manifest header), and the Footer social icons (the getbee set), all on
  approved hosts.
- The 7-step body modules are driven by the spec per email: SectionHeading (eyebrow + headline),
  BodyCopy, and on step 3 a ListBlock. FeatureImage and PromoLine are available in the renderer
  but omitted here (no rights-cleared feature image staged, no real promo code; the renderer never
  invents a code or a deadline).
- Brand fonts via the Ortto-hosted custom-fonts CSS: Lyon Arabic Display and 29LT Azer for Arabic,
  Acumin Pro for English. No binary embedded or committed.
- Dark theme. `dir="rtl"` for Arabic, `dir="ltr"` for English.
- One primary CTA per email: an MSO VML roundrect for Outlook plus a non-mso pill, near-black
  `#141414` label on emerald `#009975` (about 5:1, clears WCAG AA). Never white on emerald.
- Sender identity and an unsubscribe link in every email. The `{{ unsubscribe }}` and
  `{{ view_in_browser_url }}` are platform merge tags wired at send.

## Files

- `spec.json` the render-ready spec, the single source of truth for the HTML: subjects,
  preheaders, the per-slot copy with stable `data-copy-id` mapping, the manifest header as
  `hero_image`, the held-back claims, and the open items.
- `e1.ar.html` ... `e7.en.html` one self-contained slotted email each (14 total).
- `index.html` a dark preview sheet: open it to see all 14 with subjects, alternates, preheaders,
  and an inline preview of each.

## Regenerate

The renderer is campaign-agnostic, stdlib-only, and emits the slotted component HTML.

```
python3 .claude/scripts/email_render.py .claude/outputs/2026-06-ragheb-alama-music/email-7step/ragheb-alama/spec.json
python3 .claude/scripts/email_render.py <spec.json> --check   # house-style sweep only
python3 .claude/scripts/house_style_sweep.py <file> ...       # the FORBIDDEN sweep, any file
```

The committed slotted HTML is the source of truth; the MJML library under
`skills/05-build-launch/email-html-build/mjml/` compiles to match it. The ClassCardGrid is the 'our other classes' bottom row of three OTHER PORTRAIT instructor cards: a text-free on-brand `#141414` portrait (the same image the maharat.com instructor grid uses), an emerald accent rule, the instructor name, and the page-cleared Teaches subject as a LIVE HTML overlay (never baked into the image), each linking to its language-matched class page. To change the three OTHER instructors, edit the spec's `class_cards`; to enable the PromoLine, add a real `promo.code` to an email; the renderer never invents one.

## Claims discipline: held back

These claims are deliberately kept OUT of the copy (page-cleared facts plus voice.md
verified-safe beliefs only):

- Specific discography, songs, or albums (not page-cleared)
- Awards, sales figures, or chart positions (not page-cleared)
- TV-show names and any associated figures (held back per skill)
- Lesson count, chapter count, or class duration (page does not enumerate)
- Price, plan, or subscription figures (campaign input, not in pack)
- Launch dates or release dates (none in pack)
- Testimonials or named students (none in pack)
- Catalog status as confirmed (pending confirmation despite public listing)
- Any guarantee of fame, hits, or a music career (forbidden framing)
- Accreditation of the completion certificate (never)

## ClassCardGrid (portrait cards) and PromoLine

- ClassCardGrid: three OTHER PORTRAIT instructor cards (not this email's instructor), language-matched, are wired. Each is a text-free on-brand portrait (the maharat.com grid image, verified servable on CloudFront 2026-06-18) with the instructor name and the Teaches subject as a live HTML overlay. Like the hero, the portrait card images stage to the Ortto CDN before any send; the renderer previews on the CloudFront proof until then. Still an INTERNAL DRAFT blocked on catalog status (the roster is unconfirmed in `context/instructors/_CATALOG.md`).
- PromoLine OMITTED. No real promo code or deadline exists for this campaign, and the renderer
  never invents one.

## Body images

The on-brand `#141414` Drive portraits in `context/instructors/_IMAGE-CATALOG.md` are
`needs-hosting`: Drive links are not hot-linkable in email. This build uses only the header plus
the logo and social icons (all on approved hosts). Stage a body portrait to the Ortto CDN or
compose via Canva before adding a FeatureImage.

## Build choices

- Brand constants only: paper `#141414`, panel `#1A1A1A`, emerald `#009975`. The pending gold
  `#C4963C` and panel `#1c1c1c` are kept out (pending Ahmed). Verified: zero forbidden colors.
- Table-based layout, inline CSS, 600 wide card, mobile media query.
- House style enforced by the same forbidden-character sweep as `scripts/pack_check.py`: no em
  dash, no en dash, no tatweel, Western numerals only. The sweep is CLEAN on all 14 plus the spec
  and the index.

## Before any send (open items)

These slotted files are not yet through the gate agents or the human gate. Before a send:

1. Header source: CloudFront (verified servable at source, NOT an approved email host). Header is the verified CloudFront CLASSCOVER. CloudFront is NOT an approved email host: stage the bytes to the Ortto CDN (or prove with an inbox send-test) and swap the src before any send. Draft is fine.
2. Send-readiness (manifest): BLOCKED: stage header to Ortto CDN. Header verified servable on CloudFront only.
3. Catalog status: ragheb-alama is unconfirmed in context/instructors/_CATALOG.md. Every instructor email is an INTERNAL DRAFT blocked on catalog status, the same status as the existing Bassam build. Nothing sends.
ClassCardGrid wired as PORTRAIT instructor cards: three OTHER classes, language-matched, each a text-free on-brand portrait (the maharat.com grid image) with the instructor name and the Teaches subject as a live HTML overlay. The portrait card images, like the hero, stage to the Ortto CDN before any send (verified servable on CloudFront; pending Ortto). Still blocked on catalog status.
5. PromoLine OMITTED: no real promo code or deadline exists for this campaign, and the renderer never invents one. Add a real code to the spec to enable it.
6. Body images (the on-brand #141414 Drive portraits in _IMAGE-CATALOG.md) are needs-hosting: Drive links are not hot-linkable in email. Stage to the Ortto CDN or compose via Canva before use; this build uses only the header plus the logo and social icons (all approved hosts).
7. No price, plan, date, or promotion is stated, per the claims discipline. The plan picker on the page carries any confirmed numbers. Step 7 (subscribe) points to the class page as the subscribe entry; confirm the subscribe or plan-picker destination at the human gate.
8. CTA destinations are the page-cleared class or member URLs. Confirm masterclass page vs signup gate vs plan picker at the human gate.
9. Brand fonts (Lyon Arabic Display, 29LT Azer for AR; Acumin Pro for EN) via the Ortto-hosted custom-fonts CSS. 29LT Azer upload to Ortto is an open item; until then Arabic body falls back to Tahoma, Arial. No font binary embedded or committed.
10. Send platform OPEN (Ortto not yet adopted). The {{ unsubscribe }} and {{ view_in_browser_url }} are platform merge tags wired at send.
11. Gate stack before any send: email-html-build eval, arabic-copy-qa or english-copy-qa per copy slot by data-lang, email-asset-qa (gate-zero header check) on every image module, accessibility-qa, compliance-privacy-check, brand-qa-reviewer, then the human gate. Copy is claims-disciplined draft; these renders are not yet through the gate agents.

The human gate approves per action and per campaign. Nothing here sends on its own.
