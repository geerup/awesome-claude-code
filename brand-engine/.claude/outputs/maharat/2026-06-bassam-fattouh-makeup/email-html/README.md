# Email HTML: Bassam Fattouh Teaches Makeup (non-payer lifecycle, slotted build)

Status: draft, not approved, nothing sends. Approval-ready HTML that stops at the human gate.

Eight self-contained, slotted, live-component emails (E1 to E4, Arabic and English) built to the
Maharat email standard, the same standard as the Elda reference builds. Rebuilt from the earlier
simplistic flat renders. Bound to the QA-passed copy in `../01-emails.ar-en.md`, nothing invented,
no price or plan stated (per the brief).

The standard: `context/email-design-system.md` (tokens, the 12+1 component library, brand fonts,
themes) and `runtime/email-module-map.md` (the slot, role, lang, copy-id contract and the gate
routing).

## What "slotted live-component" means here

- Every line of copy is a LIVE HTML text slot (`data-slot="copy"`) bound to a stable
  `data-copy-id` from the spec and tagged `data-lang`. Copy is never baked into an image and never
  rewritten in the build (verified verbatim against the approved copy).
- Every image is text-free (`data-slot="element"`) with descriptive alt: the LogoBar (autopilot
  CDN logo), the Hero (Bassam class cover), and the Footer social icons (the getbee set).
- Brand fonts via the Ortto-hosted custom-fonts CSS in the head: Lyon Arabic Display and 29LT Azer
  for Arabic, Acumin Pro for English. No binary embedded or committed.
- Dark theme. `dir="rtl"` for Arabic, `dir="ltr"` for English.
- One primary CTA per email: an MSO VML roundrect for Outlook plus a non-mso pill, near-black
  `#141414` label on emerald `#009975` (about 5:1, clears WCAG AA). Never white on emerald.
- Sender identity and an unsubscribe link in every email.

Each module-bearing cell carries `data-ortto-module`, `data-slot`, and where applicable
`data-role`, `data-lang`, `data-copy-id`, and `data-link-slot`, so a built email is at once a
brand-correct render, an Ortto-editable asset, and a gate-traceable artifact.

## Files

- `emails.spec.json` the render-ready spec, the single source of truth for the HTML: subjects,
  preheaders, the per-slot copy with stable `data-copy-id` mapping, the campaign `hero_image`, and
  the open items.
- `e1.ar.html` ... `e4.en.html` one self-contained slotted email each (8 total).
- `index.html` a dark preview sheet: open it in a browser to see all 8 with subjects, alternates,
  preheaders, and an inline preview of each.

## Copy-id binding

Each slot binds to a stable id: `email-bassam-<id>-<role>-<lang>` (for example
`email-bassam-e1-headline-ar`, `email-bassam-e3-cta-en`). The eyebrow and the footer sender line
are campaign-stable: `email-bassam-eyebrow-ar`, `email-bassam-footer-sender-en`. The copy text is
bound from `../01-emails.ar-en.md`, never altered.

## Regenerate or edit

The renderer is campaign-agnostic, stdlib-only, and emits the slotted component HTML.

```
python3 .claude/scripts/email_render.py .claude/outputs/2026-06-bassam-fattouh-makeup/email-html/emails.spec.json
python3 .claude/scripts/email_render.py <spec.json> --check   # house-style sweep only, writes nothing
python3 .claude/scripts/house_style_sweep.py <file> ...        # the FORBIDDEN sweep, any file
```

Edit the copy or the hero in `emails.spec.json` and re-render. To change the three OTHER instructors
in the ClassCardGrid, edit `class_cards`. This slotted renderer supersedes the earlier flat renderer:
the committed slotted HTML is the source of truth, and the MJML library under
`skills/05-build-launch/email-html-build/mjml/` compiles to match it (`npx mjml`).

## ClassCardGrid: portrait instructor cards

The "watch also" grid is the "our other classes" bottom row of three OTHER PORTRAIT instructor cards
(not this email's instructor): a text-free on-brand `#141414` portrait (the same image the
maharat.com instructor grid uses), an emerald accent rule, the instructor name, and the page-cleared
Teaches subject as a LIVE HTML overlay (never baked into the image), each linking to its
language-matched class page. Here the three are Cedric Haddad, Elda Choucair, and Ragheb Alama. The
portrait card images, like the hero, are verified servable on CloudFront and stage to the Ortto CDN
before any send; the renderer previews on the CloudFront proof until then. This is still an INTERNAL
DRAFT blocked on catalog status: `bassam-fattouh` and every other instructor are `unconfirmed` in
`context/instructors/_CATALOG.md`, so nothing sends.

## Hero image and assets

- Hero: the Bassam class cover `BF_CLASS_PAGE_RIGHTGRADIENT.JPG`, the published class page
  `og:image`, a 16:9 rights-cleared banner. It is the same approach the Elda build uses (the
  rights-cleared class cover as the lifecycle email hero, copy overlaid as live slots, never a
  generated portrait).
- LogoBar, social icons: the autopilot CDN logo and the getbee social icon set, both from the
  references, both on approved hosts.
- The `#141414` Drive portrait (`15052024_BassamBG_141414`) in `context/instructors/_IMAGE-CATALOG.md`
  is the preferred hero once hosted on the Ortto CDN; Drive links are not hot-linkable in email.

## Build choices

- Brand constants only: paper `#141414`, panel `#1A1A1A`, emerald `#009975`. The pending gold
  `#C4963C` and panel `#1c1c1c` are kept out (pending Ahmed). Verified: zero forbidden colors.
- Table-based layout, inline CSS, 600 wide card, mobile media query.
- House style enforced by the same forbidden-character sweep as `scripts/pack_check.py`: no em
  dash, no en dash, no tatweel, Western numerals only. The sweep is CLEAN on all 8 plus the spec
  and the index.

## Before any send (open items)

These slotted files are not yet through the gate agents or the human gate. Before a send:

1. **Confirm hero deliverability.** A direct server-side fetch of the CloudFront class cover
   returns 403 (the WAF likely blocks datacenter IPs). It is the page's own `og:image`, so it
   loads in a normal browser, but email clients fetch through their own proxies. `email-asset-qa`
   (approved-cdn-hosting) blocks final pass until the rights-cleared bytes are staged to the Ortto
   CDN and the `src` is swapped, or it renders in a real inbox send-test. Neither raw CloudFront
   objects nor Drive links are guaranteed hot-linkable in email.
2. Run the email gate stack on the renders, in order: `email-html-build` eval, then `arabic-copy-qa`
   or `english-copy-qa` per copy slot by `data-lang`, then `email-asset-qa` on every image module,
   then `accessibility-qa` (email render), then `compliance-privacy-check`, then `brand-qa-reviewer`,
   then the human gate.
3. Confirm the CTA destination (masterclass page vs signup gate vs the plan picker). Current href
   is the published class page.
4. Confirm the send platform. Ortto is not yet adopted (data region, scoped API key, Arabic render
   test). The `{{ unsubscribe }}` and `{{ view_in_browser_url }}` merge tags and the plain-text
   multipart alternative are wired by the platform at send.
5. Copy note for the author: the Arabic address is mixed across emails (E1, E3, E4 read masculine,
   E2 feminine). Rendered faithfully from the approved copy. Decide if a single register is intended.
6. 29LT Azer is not yet uploaded to Ortto; the Arabic body falls back to Tahoma until it is.
7. The human gate approves per action and per campaign. Nothing here sends on its own.
