# lifecycle-package: Bassam Fattouh Teaches Makeup, non-converter nurture

Produced by lifecycle-architect from the strategy-artifact and the QA-passed copy-package. Reasoning for the
design, gated for the send. It does not write copy; it references QA-passed variants. The send is blocked and
never runs without approval. Sequence pattern selected by audience and objective: a short nurture-to-conversion
drip for warm non-converters, not a winback (these contacts are fresh from the campaign, not lapsed payers).

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: lifecycle-architect
- stream: 7 lifecycle messaging
- status: gated-pending (design-only; send blocked)
- qa: { skill_eval: pass, arabic_qa: pass, english_qa: pass, compliance: pass (design-only), brand_qa: pass }
- open_items: gate platform (blocks send wiring and suppression sourcing), consent basis for captured emails,
  retention and deletion stance, schedule and send window (ASSUMPTION), price and promotion (ASSUMPTION).

## audience

- The email-captured non-converters from the conversion path, and free-intro viewers who did not subscribe.
  These are warm, freshly opted-in contacts, not the existing 18,000 non-payer owned list (that is the bridal
  campaign's audience). Size resolves from live capture at send time; none invented.

## suppression

- Existing paying subscribers, unsubscribed, hard-bounced. Source to confirm (open item). Applied before sizing.

## flow (ordered, each message references a QA-passed copy variant, one CTA)

```
M1  welcome the intro    trigger: email_submit or free_intro_play, no subscribe.   audience: all captured.
    job: thank them, point back to the free intro, set the promise (do it yourself, step by step).  CTA: watch or continue the intro.
M2  the range            +2 days, no subscribe.   job: show one class spans natural to glam to editorial,
    with inclusive guidance. references V2 and V3 direction.  CTA: see what you will learn.
M3  the value and nudge   +3 days, no subscribe.   job: the masterclass plus all-access subscription, the
    public value line (under $7 a month, billed annually). references V4.  CTA: subscribe now.
M4  light final touch     +4 days, no subscribe, engaged only.   job: one last low-pressure reminder; suppress
    the unengaged to protect deliverability.  CTA: continue the class.
```

- Branch: contacts who subscribe at any point exit the flow immediately. Unengaged after M3 are suppressed from
  M4 (engagement-decay hygiene). No heavy resend to the unengaged.

## send_on_approval

- On approval and after the platform and consent items clear, this sends a 4-message bilingual nurture (Arabic
  primary, English variant by contact language) to the resolved captured audience, toward a paid subscription.
  Nothing sends until then. The email content is in `08-email-sequence.md`.

## Handoff

Assembles the flow for the human gate with the brand-qa and compliance verdicts attached. Coordinates the send
and engagement events with data-tracking-engineer. The send is blocked until the gate platform is named and
Ahmed approves the specific send.
