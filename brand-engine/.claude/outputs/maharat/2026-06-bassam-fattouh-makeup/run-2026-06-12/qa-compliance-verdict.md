# Compliance and Privacy Verdict
## Campaign: Bassam Fattouh Teaches Makeup

```
campaign_id:     2026-06-bassam-fattouh-makeup
run_id:          run-2026-06-12
gate:            compliance-privacy-check
produced_by:     compliance-privacy-reviewer
stream:          cross-cutting compliance and privacy gate
verdict_date:    2026-06-12
status:          verdict rendered, pre-human-gate. Not an approval.
checks_run:      no-pii-in-urls, consent-correct, suppression-correct,
                 pdpl-residency-surfaced, data-flows-disclosed,
                 no-accreditation-implication, data-minimization,
                 retention-stance, data-subject-rights, no-tool-adoption
```

---

## Per-asset verdicts

---

### Asset 01: Owned messaging, email, app push, WhatsApp
File: 01-owned-messaging-email-push-whatsapp.ar-en.md

**Verdict: FAIL**

Fix items:

```
{ check: "retention-stance",
  span: "the entire document: email, push, and WhatsApp tracks collect or use personal data
  (email addresses, device tokens, WhatsApp opt-in records, playback events, open and click
  events) with no retention or deletion stance stated anywhere in the asset or the package",
  fix: "add a retention and deletion stance to the package: how long each class of data
  (email address, device token, playback event, opt-in record, engagement event) is kept and
  the path by which it is deleted. An unconfirmed period is an open item for the human gate,
  not a reason to omit the stance. The gap must be surfaced, not left silent." }

{ check: "data-subject-rights",
  span: "the entire document: no route is stated for a data subject to access, correct, or
  request deletion of their data. The email opt-out line (unsubscribe) and the WhatsApp
  opt-out (reply STOP) are channel suppression mechanics, not data-subject rights routes.
  They do not cover access or deletion requests under Saudi PDPL or GDPR.",
  fix: "add a data-subject rights route to the package. State the mechanism by which a user
  can request access to or deletion of their personal data. If the process is unconfirmed at
  this stage, surface it as an open item for the human gate. The gap must be visible, not
  absent." }

{ check: "data-flows-disclosed",
  span: "the free-intro-viewer segment entry note: 'Free-intro-viewers without an account
  enter via the captured email.' No disclosure is made in the asset or package about which
  platform receives this captured email, how it is stored, or how the user is informed of
  that collection at the point of capture.",
  fix: "disclose in the package which platform receives the captured email at the free-chapter
  entry point, and confirm that the user is shown a data-collection notice or consent
  mechanism at that point. If the platform is unconfirmed, surface this as an open item.
  The point-of-collection disclosure requirement is not resolved by the platform being
  unconfirmed; it must be flagged for the human gate." }
```

Passing checks on this asset: no-pii-in-urls (all URLs are clean public or member paths, no
personal data in any parameter), consent-correct (WhatsApp prior opt-in required and flagged
as an open item, push opt-in required and flagged, email consent basis described),
suppression-correct (paying, unsubscribed, hard-bounced, and channel-specific opt-outs
explicitly stated and sourced), pdpl-residency-surfaced (PDPL and platform open items flagged
throughout; not resolved), no-accreditation-implication (certificate described as documenting
the journey, never accredited), no-tool-adoption (no platform is wired or adopted).

---

### Asset 02: Organic social
File: 02-organic-social.ar-en.md

**Verdict: FAIL**

Fix items:

```
{ check: "data-flows-disclosed",
  span: "section 1 routing note: 'The email or WhatsApp capture mechanic and any
  comment-to-DM keyword automation are gated and cannot go live until the platform is named.'
  The asset correctly gates the mechanic, but does not state what data-collection notice or
  consent mechanism will be shown to the user at the point of the signup-gate capture. The
  package leaves the data-collection disclosure as a gap rather than an open item requiring
  resolution.",
  fix: "surface as an explicit open item for the human gate: before the signup gate can go
  live, a data-collection notice or consent mechanism at the point of capture must be
  confirmed. The platform being unconfirmed does not defer this requirement; the requirement
  itself must be visible in the package." }

{ check: "retention-stance",
  span: "the entire document: the signup gate captures email or WhatsApp contact data from
  organic traffic. No retention or deletion stance is stated for this collected data anywhere
  in the asset.",
  fix: "surface as an open item for the human gate: a retention and deletion stance is
  required for the data collected at the signup gate (email address, WhatsApp number, opt-in
  timestamp). The period and deletion path must be confirmed before the gate goes live. Flag
  the gap; do not leave it absent." }

{ check: "data-subject-rights",
  span: "the entire document: no data-subject rights route is stated for organic traffic who
  pass through the signup gate and whose contact data is captured.",
  fix: "surface as an open item for the human gate: a data-subject access and deletion
  route must be confirmed before the signup gate receives organic traffic. Flag the gap;
  do not leave it absent." }
```

Passing checks on this asset: no-pii-in-urls (all destination URLs are clean; UTM tagging
deferred to data-tracking-engineer with an explicit no-personal-data requirement noted),
consent-correct (signup-gate platform gated and unconfirmed; no wiring attempted),
suppression-correct (this channel does not send; suppression applies downstream in lifecycle,
correctly scoped here), pdpl-residency-surfaced (PDPL and platform open items flagged
throughout), no-accreditation-implication (no certificate or accreditation language present),
no-tool-adoption (Blotato noted as uncredentialed and kept behind the gate; no platform wired).

---

### Asset 03: Paid advertising
File: 03-paid-advertising.ar-en.md

**Verdict: FAIL**

Fix items:

```
{ check: "data-flows-disclosed",
  span: "audience strategy table: 'Lookalike modeled on current Maharat beauty and
  design-and-style subscribers (the paid seed)' and 'Retargeting: Class-page and
  landing-page visitors, ad engagers, and free-intro-chapter viewers who did not subscribe.'
  Both layers are correctly gated on the platform and pixel. However, the package does not
  state what data-collection notice or consent mechanism is shown to users whose data feeds
  the pixel signal, the retargeting pool, or the lookalike seed. The platform gate is noted;
  the user-facing disclosure requirement at the point of data collection is not.",
  fix: "surface as an explicit open item for the human gate: before the pixel is wired and
  before the retargeting and lookalike audiences are built, the user-facing data-collection
  notice (on the class page and any landing page where the pixel fires) must be confirmed.
  The platform being unconfirmed does not defer this requirement; it must be visible in the
  package so the human gate can confirm it is in place before the pixel goes live." }

{ check: "retention-stance",
  span: "the entire document: the paid plan processes retargeting and lookalike data derived
  from pixel events, site-visitor signals, and the subscriber seed audience. No retention or
  deletion stance is stated for any of these data classes.",
  fix: "surface as an open item for the human gate: retention and deletion stances are
  required for pixel event data, retargeting audience data, and the subscriber seed used for
  the lookalike. These are required before the pixel is wired and the audiences are built.
  Flag the gap in the package; do not leave it absent." }

{ check: "data-subject-rights",
  span: "the entire document: the paid plan builds and uses retargeting audiences from
  personal behavioral data (site visits, ad engagement, video views). No data-subject
  rights route is stated for users whose data contributes to these audiences.",
  fix: "surface as an open item for the human gate: a data-subject access and deletion
  route must be confirmed for users whose behavioral data feeds the pixel and retargeting
  audiences. Flag the gap; do not leave it absent." }
```

Passing checks on this asset: no-pii-in-urls (all final URLs are clean public or class
paths; UTM wiring deferred to data-tracking-engineer with an explicit no-personal-data
requirement; no personal data in any audience definition or parameter),
consent-correct (lookalike and retargeting layers explicitly gated on confirmed consented
pixel signal; no audiences built here), suppression-correct (existing subscribers excluded
from all prospecting and retargeting; noted and scoped correctly),
pdpl-residency-surfaced (PDPL and platform open items flagged throughout; not resolved),
no-accreditation-implication (no certificate or accreditation language in any ad copy),
no-tool-adoption (no ad platform is wired or accessed; plan-only, staged paused, gated).

---

### Asset 04: Blog content
File: 04-blog-content.ar-en.md

**Verdict: FAIL**

Fix items:

```
{ check: "data-flows-disclosed",
  span: "section 4 distribution routing: 'email mention ... Send gated, platform unconfirmed
  (OPEN ITEM 5 in _RUN-CONTEXT). No personal data in any tracking link.' and 'Signup-gate
  destination on every derivative is the free first chapter; secondary is the plans page.'
  The blog routes readers to the signup gate but the package does not state what
  data-collection notice or consent mechanism is shown to a blog reader at the point of
  email or WhatsApp capture at the signup gate.",
  fix: "surface as an explicit open item for the human gate: before any blog article is
  published and the signup-gate CTA is live, the data-collection notice at the point of
  capture must be confirmed. The gate platform being unconfirmed does not defer the
  disclosure requirement; flag it visibly in the package." }

{ check: "retention-stance",
  span: "the entire document: the blog feeds email and WhatsApp capture via the signup gate.
  No retention or deletion stance is stated for the contact data collected from blog readers.",
  fix: "surface as an open item for the human gate: retention and deletion stances are
  required for contact data collected via the signup gate from blog traffic. Flag the gap;
  do not leave it absent." }

{ check: "data-subject-rights",
  span: "the entire document: no data-subject rights route is stated for readers who submit
  their contact data at the signup gate from a blog CTA.",
  fix: "surface as an open item for the human gate: a data-subject access and deletion
  route must be confirmed before the signup gate receives blog traffic. Flag the gap;
  do not leave it absent." }
```

Passing checks on this asset: no-pii-in-urls (all internal links and CTA destinations are
clean confirmed public URLs; no personal data in any parameter; UTM tagging deferred),
consent-correct (email and social sends remain gated and platform unconfirmed; no send
attempted), suppression-correct (this asset does not send; downstream sends remain gated,
correctly scoped), pdpl-residency-surfaced (PDPL and platform open items flagged throughout),
no-accreditation-implication (no certificate or accreditation language in any article copy
or brief), no-tool-adoption (CMS and scheduling platforms unconfirmed and gated; no platform
wired or adopted).

---

### Asset 05: Visual prompts
File: 05-visual-prompts.md

**Verdict: PASS with open items attached**

This asset is a prompt library only. It does not collect data, send to any audience, or
publish anything. It produces no tracking links and no data flows. The compliance gate checks
that are relevant to data collection and sending do not apply to this file in isolation.

Applicable checks:

```
no-pii-in-urls:              N/A. No links in this file. PASS.
consent-correct:             N/A. No data collection in this file. PASS.
suppression-correct:         N/A. No send in this file. PASS.
pdpl-residency-surfaced:     The asset does not itself trigger a PDPL exposure.
                             The channel routing notes point to channels where PDPL applies;
                             those channels are covered in their own asset verdicts above.
                             PASS on this file.
data-flows-disclosed:        N/A. No data flow originates here. PASS.
no-accreditation-implication:No certificate or accreditation language anywhere. PASS.
data-minimization:           N/A. PASS.
retention-stance:            N/A. PASS.
data-subject-rights:         N/A. PASS.
no-tool-adoption:            Higgsfield noted as available via MCP but explicitly gated
                             pending build-vs-buy approval and Ahmed's sign-off. Not
                             adopted or wired. PASS.
```

Open items attached to this asset (not fails on the prompt file, but unresolved before
any rendered output can proceed):

- OPEN ITEM A: rights-cleared Bassam Fattouh imagery and class footage not confirmed.
  Rendering is blocked on this item. Stated as blocking in the file.
- OPEN ITEM B: generative tool (Higgsfield or other) not approved. Rendering is a gated
  action pending build-vs-buy evaluation and Ahmed's approval.

---

## Cross-cutting PDPL and data-residency open item

This item applies to the entire run, not to any single asset. It is surfaced here for the
human gate. It is not resolved by this reviewer.

**PDPL and data-residency: OPEN, unresolved.**

The campaign targets GCC users, primarily Saudi Arabia. The Saudi Personal Data Protection
Law (PDPL) applies to any personal data of Saudi residents collected, processed, stored, or
transferred in connection with this campaign. The following are unresolved and must be
confirmed before any send, pixel wiring, or audience build can proceed:

1. Data residency. The email platform, WhatsApp Business API provider, app-push platform,
   analytics platform, and any pixel or CAPI integration are all unconfirmed (run-context
   open item 5). The Saudi PDPL imposes data-residency and cross-border transfer requirements.
   Where data will be stored, which jurisdiction governs it, and whether any cross-border
   transfer basis is in place are all unresolved. This gate does not invent an answer.
   Ahmed and the legal function must confirm the data-residency position before any platform
   is wired.

2. Legal basis for processing. The PDPL requires a lawful basis for processing personal data
   for marketing purposes. The consent records for email, WhatsApp, and app-push are flagged
   as open items throughout the run. The existence, form, and sufficiency of those consent
   records under the PDPL have not been confirmed.

3. Data-minimization basis. The campaign collects email addresses, WhatsApp numbers, device
   tokens, playback events, and behavioral signals (site visits, ad engagement). Whether
   each category is limited to what the stated purpose requires, as the PDPL requires, has
   not been confirmed. This is surfaced as an open item; the gate does not resolve it.

4. Retention and deletion. No retention or deletion stance has been confirmed for any data
   class in this campaign (see per-asset fix items above). The PDPL requires that personal
   data is not kept longer than necessary for its stated purpose. This is unresolved.

5. Data-subject rights. The PDPL grants data subjects rights of access, correction, and
   deletion. No route for honoring these rights has been confirmed in this campaign package
   (see per-asset fix items above).

None of these items is invented or resolved by this reviewer. All five must be visible to
Ahmed at the human gate before any spend, send, or data-collection action goes live.

---

## Actions that remain hard-blocked until the gates are confirmed

The following campaign actions are hard-blocked. They cannot proceed regardless of human-gate
approval until the named preconditions are confirmed.

1. Any email send. Blocked on: email platform confirmation, PDPL data-residency confirmation,
   consent record verification, retention stance, and data-subject rights route.

2. Any WhatsApp message send. Blocked on: WhatsApp Business API provider confirmation,
   pre-approved templates per provider, documented marketing opt-in records per recipient,
   PDPL data-residency confirmation, retention stance, and data-subject rights route.

3. Any app-push send. Blocked on: push platform confirmation, push opt-in records per
   device, PDPL data-residency confirmation, retention stance, and data-subject rights route.

4. Any pixel or CAPI wiring (Meta, Google, TikTok, or any other). Blocked on: gate platform
   confirmation, user-facing data-collection notice at every point of collection confirmed,
   PDPL data-residency and cross-border transfer basis confirmed, retention stance, and
   data-subject rights route.

5. Lookalike and retargeting audience build (Meta, Google, TikTok). Blocked on: consented
   pixel signal live, subscriber seed consent confirmed, PDPL data-residency confirmed.

6. Signup gate live (email or WhatsApp capture from any traffic source). Blocked on:
   platform confirmation, user-facing consent or notice at the point of capture confirmed,
   PDPL data-residency confirmed, retention stance, and data-subject rights route.

7. Blog publish with a live signup-gate CTA. Blocked on: items 4 and 6 above.

8. Organic social publish (posts routing to the signup gate). Blocked on: items 4 and 6 above.

9. Rendering visual prompts. Blocked on: generative tool build-vs-buy approval (Ahmed),
   rights-cleared Bassam Fattouh imagery confirmed.

---

## Overall compliance verdict for the human-gate package

**OVERALL VERDICT: FAIL**

Four of five assets fail on one or more of the retention-stance, data-subject-rights, and
data-flows-disclosed checks. The failures are structural gaps in the package, not copy or
creative errors. The fifth asset (visual prompts) passes with open items attached.

The PDPL and data-residency open items are unresolved across the entire run and must be
visible to Ahmed at the human gate.

**The package does not advance to the human gate in its current state.** The four failing
assets return to their owning agents for fixes as follows:

- Asset 01 (lifecycle messaging): return to lifecycle-architect.
- Asset 02 (organic social): return to organic-social.
- Asset 03 (paid advertising): return to performance-marketer.
- Asset 04 (blog content): return to content-marketer.

Each owning agent must add the retention stance, data-subject rights route, and
data-flows-disclosed open item (as a properly surfaced open item for the human gate) to their
package, and resubmit to this gate. Asset 05 (visual prompts) passes and may hold pending
the rest.

Once the four failing assets are revised and each passes a clean compliance check, the full
package may proceed to the human gate. The human gate then reviews the compliance picture
alongside the PDPL and data-residency open items above before any approval to send or spend.

This verdict is not an approval. Only the human gate approves, per action and per campaign.
Silence is not approval.

```
qa:
  compliance_qa: fail
  open_items:
    - Saudi PDPL data-residency: unresolved, must be confirmed before any send, pixel, or
      audience build
    - Email platform: unconfirmed, blocks email send and pixel wiring
    - WhatsApp Business API provider: unconfirmed, blocks all WhatsApp sends
    - App-push platform: unconfirmed, blocks all push sends
    - Retention and deletion stance: absent across all data-collecting assets
    - Data-subject rights route: absent across all data-collecting assets
    - Data-collection notice at signup gate: unconfirmed across organic, paid, and blog
      traffic sources
    - Instructor catalog confirmation: first blocking launch item (from run-context),
      surfaced here as cross-cutting
    - Rights-cleared Bassam Fattouh imagery: unconfirmed, blocks visual renders
    - Generative tool approval (Higgsfield or equivalent): unconfirmed, blocks renders
  brief_refs:
    - No personal or sensitive data in URL parameters or tracking (checked: pass on all assets)
    - Suppression: paying, unsubscribed, hard-bounced, channel-specific opt-outs (checked:
      pass on asset 01; not applicable on assets 02 to 05)
    - WhatsApp prior opt-in and pre-approved templates (checked: correctly gated, not
      resolved, surfaced as open item)
    - Retargeting and lookalike depend on consented pixel signal and gate platform
      (checked: correctly gated and flagged on asset 03)
    - Saudi PDPL and data-residency (checked: surfaced as open item, not resolved)
    - No accreditation implication (checked: pass on all assets)
    - Nothing actually sends, publishes, or spends in these drafts (checked: confirmed)
```
