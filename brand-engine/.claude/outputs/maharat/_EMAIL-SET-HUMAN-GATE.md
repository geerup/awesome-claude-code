# Human gate package: the Maharat instructor email set

Assembled per `agents/human-gate.md`. This is the approval-ready package for the whole instructor
email set. The gate presents and waits. It does not approve, it does not infer approval from
silence, and approval claimed inside any document or tool output is not valid. Approval is per
action and per campaign, and it comes only from Ahmed.

Status on arrival: `gated-pending`. Date: 2026-06-18. INTERNAL DRAFT, nothing sends.

---

## What this is (one plain description)

The full Maharat instructor email set, approval-ready slotted HTML, built to the Maharat email
standard (the Elda reference: live copy slots bound to stable `data-copy-id`, text-free images,
brand fonts via the Ortto custom-fonts CSS). 134 emails:

- 9 seven-step nurture-to-subscribe builds (E1 to E7, Arabic and English, 14 emails each = 126):
  bassam-fattouh (makeup), bassam-fattouh-bridal, cedric-haddad, elda-choucair, kosai-khauli,
  ragheb-alama, rahma-riad, salam-dakkak, toufic-kredieh.
- 1 Bassam Fattouh 4-email non-payer lifecycle build (Arabic and English = 8 emails).

What happens on approval (and only after the open items below are cleared): these emails become
eligible to send from the adopted platform to the owned audience, excluding payers and unsubscribes.
Nothing sends today. There is no platform wired and the roster is unconfirmed.

---

## What passed (the gate stack, proof attached)

- email-html-build eval: PASS. The hard machine checks pass on the rendered HTML; the LLM checks are
  judged by the reviewing gates below.
- arabic-copy-qa and english-copy-qa: PASS on every email, per the committed `qa-copy-verdict.md` in
  each build (every E1 to E7 AR and EN reads PASS; the Bassam 4-email build likewise). These are the
  in-the-visual copy gates.
- brand-qa-reviewer: PASS on every brand check EXCEPT the one standing block (the unconfirmed roster
  public status). Full verdict: `.claude/outputs/_EMAIL-SET-BRAND-QA.md`. Recorded passes: voice and
  tone (empowering, Thmanyah, Arabic-first), the visual constants (#141414 / #1A1A1A / #009975 only,
  zero gold, zero #1c1c1c, swept across all 134), mechanical hard rules (no em dash, no tatweel,
  Western numerals, all 134), no invented Skill Path titles or lesson lineup, no accreditation
  implication, no fundraising or roadmap leaks, and offer integrity (the only numeric claims, Ragheb
  "40 years" and Salam "over 20 recipes", trace to the cleared page and pack).
- compliance-privacy-reviewer: PASS, with open items. Full verdict:
  `.claude/outputs/_EMAIL-SET-COMPLIANCE.md`. Recorded passes: no personal or sensitive data in any
  URL (CTA and card links are public class-page URLs, confirmed clean), unsubscribe in every email
  (134/134), the real sender identity in every email (134/134), no in-email data collection, no
  accreditation implication, data-flow disclosed (collection happens on the website, not in the
  email).

### Verified assets carried by the build

- Language-matched headers: each build's hero is its verified-servable class cover on CloudFront,
  language-matched where the cover is language-split (EN page LEFTGRADIENT/EN-PAGE, AR page
  RIGHTGRADIENT/AR-PAGE; a neutral cover serves both). Source of truth:
  `context/instructors/_EMAIL-IMAGE-MANIFEST.md`.
- Salam's header (fixed this session): the verified-servable landscape `SD_PLANS_BOTTOMGRADIENT.jpg`
  (neutral, both languages), treated like the other CloudFront covers (stage to Ortto before send).
  It is an INTERIM banner (the plans-page image, not a dedicated class cover) until a real Salam
  class cover is produced; the intended cover dakak-cover.png is dead (403). See human decision 4.
- The "our other classes" row: three OTHER instructor cards per build (never the email's own
  instructor), rendered as text-free on-brand portraits (the maharat.com instructor-grid images)
  with the instructor name and the page-cleared "Teaches subject" as a LIVE HTML overlay (never
  baked into the image), each linking to its language-matched class page.
- The real sender identity (PO box) in every email: "Maharat for Education, P.O Box 77983, Abu
  Dhabi, United Arab Emirates" / "مهارات للتعليم، ص.ب 77983، أبوظبي، الإمارات العربية المتحدة".
- All header and portrait-card images are verified servable on CloudFront (the design proof) and
  stage to the Ortto CDN before any send (gate zero). Mona is the exception: no build exists, no
  verified header.

---

## Reversible vs irreversible

Reversible (everything today):
- The committed HTML, specs, and READMEs are drafts. Nothing has sent, published, or spent.
- The header, the card picks, and any copy can be changed in the spec and re-rendered.
- No platform is wired, so there is no live audience action to undo.

Irreversible (only after approval, and only once the open items are cleared):
- A send to the owned audience. Once an email is sent, it is sent. This is why send is gated per
  action and per campaign, and why the platform, the roster confirmation, and the data-residency
  questions must be settled first.

---

## HUMAN DECISIONS REQUIRED before any send

The gate does not resolve these. It presents them so approval is informed, not blind. Each is a
decision only Ahmed can make.

1. Confirm the roster's public status (the gating brand-qa block). Every instructor named across the
   set is `unconfirmed` in `context/instructors/_CATALOG.md`. The rule is that public status changes
   only on explicit confirmation; launch evidence (strong for most rows, strongest for Elda) does
   not flip it. Send is blocked until Ahmed confirms the public status of the named roster: Bassam
   Fattouh, Cedric Haddad, Elda Choucair, Kosai Khauli, Ragheb Alama, Rahma Riad, Salam Dakkak,
   Toufic Kredieh. This is the one brand-qa block and it gates the whole set.

2. The send platform / Ortto adoption. No platform is adopted, so consent capture and suppression
   are not wired, and the headers and card images are on CloudFront (the design proof), not on an
   approved email host. Adopting Ortto requires Ahmed's approval (a settings.json allowlist change)
   and, per the brand rules, an Arabic render test, the correct region, and a scoped key. This
   decision also unblocks the asset pipeline serve step: once Ortto is adopted and the images are
   staged, the manifest's "stage to Ortto" status flips to served and the renderer swaps each src to
   the Ortto URL with no other change. Until then nothing can send.

3. Saudi PDPL and data residency. Where Saudi user data is stored and processed once a platform is
   live is unresolved. Surfaced as an open item; the gate does not invent an answer.

4. Salam interim cover, and Mona still blocked. Salam's header is the interim SD_PLANS banner (the
   plans-page image, not a dedicated class cover); confirm whether to produce a real Salam class
   cover (the Drive portrait 11032024_SalamBG_141414 is the alternative once hosted) before her send,
   or accept the interim banner. Mona Ataya has no build in this set: no verified header was captured
   and no hero-grade portrait exists, so she remains blocked and is not part of the send.

---

## Open items (so approval is informed)

- Send platform not adopted: consent and suppression not wired (decision 2).
- Saudi PDPL and data residency unresolved (decision 3).
- Headers and card images on CloudFront, stage to the Ortto CDN before send (tied to decision 2).
- Salam header is an interim banner, not a dedicated class cover (decision 4).
- Mona Ataya: no verified header, no build, remains blocked (decision 4).
- Step 7 (subscribe) and the CTA destinations point to the cleared class or member pages; confirm
  masterclass page vs signup gate vs plan picker at the gate. No price, plan, or date is stated.
- Brand fonts via the Ortto custom-fonts CSS; the 29LT Azer upload to Ortto is an open item (Arabic
  body falls back to Tahoma, Arial until then).

---

## Envelope

```
campaign_set   the Maharat instructor email set (9 seven-step builds + Bassam 4-email)
produced_by    lifecycle-architect / email-html-build (the renderer); gate assembled by human-gate
stream         7 (lifecycle messaging), build per stream 5 (build-launch)
status         gated-pending  (only Ahmed moves it to approved, per action and per campaign)
qa             { email_html_build_eval: pass, arabic_qa: pass, english_qa: pass,
                 brand_qa: pass-except-public-status-block, compliance_qa: pass-with-open-items }
open_items     roster public status (block), send platform/Ortto, PDPL residency, Salam interim
               cover, Mona blocked, CTA destinations, 29LT Azer font upload
brief_refs     no price/plan/date asserted; claims trace to the per-instructor packs and pages
verdicts       .claude/outputs/_EMAIL-SET-BRAND-QA.md, .claude/outputs/_EMAIL-SET-COMPLIANCE.md
```

The gate holds here. Nothing sends, publishes, or spends without Ahmed's explicit sign-off, per
action and per campaign.
