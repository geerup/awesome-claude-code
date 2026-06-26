---
name: compliance-privacy-check
description: The compliance and privacy gate. Use to check anything that collects data, sends, or publishes before it reaches the human gate, triggers on "compliance check," "privacy review," "is this PDPL safe," "check the tracking," "check consent and suppression." Verifies no personal or sensitive data in URL parameters or tracking, consent and suppression correctness, Saudi PDPL and data-residency open item surfaced when relevant, data flows disclosed, and no accreditation implication, returning pass or a structured fix list. It flags open items, it does not adopt tools or resolve them.
---

# Compliance and privacy check (the compliance gate)

The compliance and privacy quality gate, used by `compliance-privacy-reviewer`. Runs on
anything that collects data, sends, or publishes: landing pages and signup gates, event and
pixel tracking, email and WhatsApp sends, and any link carrying parameters. A verifier, not
an author and not a tool adopter: it returns pass, or fail with an exact fix list, and it
surfaces open items rather than resolving them. The author or owning agent regenerates
against the list and resubmits to this same gate.

## Purpose

Catch privacy and compliance defects before the human gate sees the package: personal or
sensitive data leaking into URLs or tracking, consent and suppression errors, undisclosed
data flows, the Saudi PDPL and data-residency open item going unflagged, accreditation
implications, and the PDPL and GDPR data-handling gaps: collecting more than the stated
purpose needs, a missing retention or deletion stance, and no path for data-subject access
and deletion requests. A clean pass here means the human gate reviews intent and spend, not
basic compliance hygiene the swarm should have caught.

## When to use

- Conversion path: landing page, signup gate, event and pixel or CAPI tracking (stream 6).
- Lifecycle and build: email and WhatsApp sends and their audiences (streams 5, 7).
- Anything with a tracked link, UTM set, or destination URL.
- Always before the human gate receives the package.

## Inputs

- The asset or spec under review: page, gate, event plan, send definition, link set.
- The audience or suppression logic, where a send is involved.
- `context/04-tools-and-access.md`: the stack and the standing open items, including the PDPL
  and data-residency question.
- The active brief and `context/` for the data the campaign legitimately collects.

## The checks

Run each. Report every failing item, not just the first.

1. no-pii-in-urls: no personal or sensitive data in URL parameters, query strings, UTMs, or
   tracking payloads. No email, phone, name, or identifier in a link or a tracking call.
2. consent-correct: data is collected and used with valid consent for the stated purpose; no
   pre-checked consent, no purpose the consent did not cover.
3. suppression-correct: the send audience excludes the right contacts. Already-paying
   contacts, unsubscribed contacts, and hard-bounced addresses are excluded. Suppression is
   applied, not just described.
4. pdpl-residency-surfaced: when the asset touches Saudi user data, sending, or storage, the
   Saudi PDPL and data-residency open item is surfaced as an open item for the human gate. It
   is flagged, never silently assumed resolved.
5. data-flows-disclosed: where data goes is disclosed to the user and stated in the package,
   for example which platform receives a signup and which pixel or CAPI fires.
6. no-accreditation-implication: nothing in the compliance-facing copy states or implies
   certificates are accredited. They are completion certificates, not accredited.
7. data-minimization: the asset collects only the data the stated purpose needs. Every field,
   parameter, and tracked attribute maps to a stated purpose. Data collected without a purpose
   it serves becomes a fix item, and any unclear case is surfaced as an open item for the human
   gate. The gate flags the gap, it does not resolve the PDPL minimization basis itself.
8. retention-stance: a retention or deletion stance is present, how long the collected data is
   kept and the path by which it is deleted. A missing stance becomes a fix item, and an
   unconfirmed period is surfaced as an open item. The gate flags the gap, it does not set the
   retention period itself.
9. data-subject-rights: the asset states how access and deletion requests from a data subject
   are handled, the route a user takes to reach their data or have it deleted. A missing route
   becomes a fix item, and an unconfirmed process is surfaced as an open item. The gate flags
   the gap, it does not stand up the rights process itself.
10. no-tool-adoption: the check does not adopt a tool, wire a platform, or resolve the
   platform open item. Any tool not on the approved allowlist is flagged for build-vs-buy and
   Ahmed's approval, not used.

## Steps

1. Read the asset, its links and tracking, and its audience or suppression logic.
2. Run each check; capture every failing span or condition, quoted or described exactly.
3. Surface every relevant open item (PDPL, data residency, unconfirmed platform) for the
   human gate.
4. Decide the result: pass only when every check passes, otherwise fail. Open items that are
   correctly surfaced do not by themselves fail the gate; an unsurfaced one does.
5. Return the result in the shape below. Never edit the asset, never adopt a tool.

## Output

- Pass: the asset advances toward the human gate, with any open items attached.
- Fail: a structured fix list, one item per failure:

```
{ check: <the failing check id>, span: "<the offending span or condition, quoted>", fix: "<the required change>" }
```

Example: `{ check: "no-pii-in-urls", span: "?email=user@example.com&utm_source=email", fix: "remove the email parameter, pass no personal data in the URL" }`.

See `templates/compliance-fix-list.md`.

## Hard rules

- Never edit the asset and never adopt or wire a tool. Verify, flag, and route only.
- The platform and PDPL open items are surfaced, never resolved here. Resolution is a
  build-vs-buy pass and Ahmed's approval.
- Binary: pass and advance, or fail and return. No soft warnings that pass through.
- Never put personal or sensitive data in URL parameters or tracking, under any rationale.

## How it connects

- Used by `compliance-privacy-reviewer` on conversion, lifecycle, and build outputs before
  they reach the human gate, per `runtime/verification.md` and `agents/human-gate.md`.
- On pass, the asset advances with open items attached for the human gate. On fail, it
  returns to the owning agent (conversion-engineer, lifecycle-architect, paid-build-engineer)
  with the fix list.
- Open items it surfaces are recorded in the artifact `open_items` per
  `runtime/handoff-contract.md`, so downstream and the human gate are never surprised.
