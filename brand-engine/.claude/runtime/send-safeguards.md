# Send safeguards

The standing controls that must all hold for any send, publish, or live site change, per
CLAUDE.md principle 4. You approve an asset or campaign once; after that, its actions run within
these safeguards without a per-action approval. If any safeguard is not in force, the action
stays disabled.

No em dashes. (Western numerals / no tatweel apply when Arabic is in scope.)

1. Test first. A successful test before any real action: a test email to your own address before
   any audience send; a preview/staging render before a site publish. When Arabic is in scope,
   the Arabic render test (RTL correct, Western numerals, no tatweel) is part of this and a fail
   blocks the action.
2. Suppression and consent on every send. Unsubscribes, bounces, and opt-outs are honored without
   exception. Marketing email always carries an unsubscribe path. No one is contacted who has not
   opted in or with whom you have no legitimate basis. No client/employer named without consent.
3. Per-action caps, set in the approved brief, never invented. A send-volume cap and, if you ever
   run paid, a spend cap. A run that would exceed a cap stops and asks.
4. Audit log. Every send or publish is recorded: what you approved, the asset, the audience or
   surface, the recipient count, and the time.
5. Kill switch. A single setting halts all sending and publishing immediately, whatever is in flight.
6. Scope lock. The engine acts only within an approved scope and audience. It never sends to an
   audience, or publishes content, outside what was approved.
7. Data handling resolved. Your data-handling policy (what data is collected, where it lives, how
   consent is recorded) is set before any live send or data collection. No personal or sensitive
   data in URL parameters or tracking.

Owners: `lifecycle-architect` (send package, Gmail drafts), `conversion-engineer` and
`web-designer` (site publish), `compliance-privacy-reviewer` (suppression, consent, data
handling), `data-tracking-engineer` (audit log when analytics are wired). The kill switch is
yours at all times. For a solo brand the default is draft-and-review: most actions stop as a
draft for you to send or publish yourself.
