# Compliance and privacy verdict: the Maharat instructor email set

Gate: compliance-privacy-reviewer (criteria: `agents/compliance-privacy-reviewer.md` +
`skills/compliance-privacy-check`).
Scope: the rendered email set, 134 emails. The 9 seven-step instructor builds (E1 to E7, AR and EN,
14 each = 126) plus the Bassam Fattouh 4-email non-payer build (8). The 10 `index.html` preview
sheets are previews, not emails, and are out of scope. Verify only, nothing edited.
Date: 2026-06-18. Status: INTERNAL DRAFT, nothing sends.

---

## VERDICT (headline)

PASS, with the known open items surfaced for the human gate. No personal or sensitive data in any
URL, unsubscribe and the real sender identity in every email, no in-email data collection, no
accreditation implication. The open items are the send platform (consent and suppression not wired,
because Ortto is not adopted) and the Saudi PDPL and data-residency question. These are surfaced,
not resolved: the gate flags, it does not adopt a tool or invent an answer.

`qa.compliance_qa: pass` (with open items attached).

---

## Checks (recorded exactly)

### 1. No personal or sensitive data in URLs or tracking: PASS, all 134

Inspected every `href` across all 134 rendered emails. Every link is one of: a public class page
(`www.maharat.com/...`, `member.maharat.com/...`), a public Maharat social profile
(Facebook, Instagram, X, LinkedIn, all `maharatarabia`), the Maharat home page, the two Ortto
custom-font CSS links, or one of two Ortto merge tags. There is no name, email, phone, or any
identifier in any query string. The only query strings present are the Ortto font links,
`?family=Acumin+Pro&k=bWFoYXJhdA` and `?family=Lyon+Arabic+Display&k=bWFoYXJhdA`; the `k` value
`bWFoYXJhdA` is base64 for the literal string "maharat", a static public font-kit identifier, not
personal or sensitive data. No UTM parameters anywhere. The only `@` literals in the files are the
retina social-icon filenames (`facebook@2x.png` and the like), not email addresses. The CTA links
and the other-classes card links were checked specifically, per the run instruction: they are
public class-page URLs, confirmed clean.

### 2. Unsubscribe present in every email: PASS, 134/134

Every email carries the `{{ unsubscribe }}` footer link (the platform merge tag, resolved to a
per-recipient unsubscribe URL at send by the platform). None missing.

### 3. Sender identity present (the real PO box): PASS, 134/134

Every email carries the real sender identity in the footer. EN (all 67 EN files): "Maharat for
Education, P.O Box 77983, Abu Dhabi, United Arab Emirates". AR (all 67 AR files): "مهارات للتعليم،
ص.ب 77983، أبوظبي، الإمارات العربية المتحدة". Western numerals throughout. View-in-browser
(`{{ view_in_browser_url }}`) is also present in every email, 134/134.

### 4. Consent and suppression: OPEN ITEM (the send is not wired)

The emails collect no data directly: zero forms, inputs, textareas, selects, `mailto:`, or `tel:`
across all 134. Consent capture and suppression (exclude already-paying, unsubscribed,
hard-bounced) are not implemented because the send platform (Ortto) is not yet adopted. This is an
open item for the human gate, not a defect in the draft. Note recorded: the send is not wired.

### 5. Saudi PDPL and data residency: OPEN ITEM (surfaced, not resolved)

Where Saudi user data is stored and processed once a send platform is live is unresolved. Surfaced
as an open item the human gate must see. The gate does not invent an answer.

### 6. No accreditation implication: PASS, all 134

Zero hits for accredited / certified / certification (EN) and معتمد / اعتماد (AR) in any
customer-facing copy. No certificate claim appears in these nurture emails at all.

### 7. Data-flow disclosure: PASS (no in-email collection point)

No data-collection point exists inside any email. The CTAs link out to public class pages; signup
and consent happen on the website, not in the email, so no in-email disclosure notice is required.
Where the data goes once a platform is live (the website signup, and Ortto as the future send
platform) is stated in the human-gate package so the human approves with the data picture in view.

---

## Open items to attach to the human gate

1. Send platform (Ortto) not adopted. Consent capture and suppression are not wired. Resolution is
   a build-vs-buy pass and Ahmed's approval (a settings.json allowlist change), not this gate. Until
   then nothing can send.
2. Saudi PDPL and data residency unresolved. Where Saudi user data is stored and processed once a
   platform is live. Surfaced, not resolved.
3. Adjacent, asset-side (travels with the same "send not wired" gate, not a privacy defect): the
   header and card images are served from CloudFront as a verified design proof. CloudFront is not
   an approved email host; assets stage to the Ortto CDN before any send.

---

## Defects found

None. No PII in any URL, no undisclosed in-email data collection, no accreditation claim, no Eastern
numerals, no stray email or phone literal.

---

## Disposition

`qa.compliance_qa: pass`, with the open items above attached to the human-gate package. A pass here
is not approval to send: the human gate is separate and decisive, and the send cannot run until the
platform open item is resolved by Ahmed. Nothing sends.
