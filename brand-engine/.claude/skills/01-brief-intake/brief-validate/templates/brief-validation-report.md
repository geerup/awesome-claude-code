# Brief Validation Report: [campaign_id]

Internal artifact, stream 1. Validates the active brief against
`briefs/_TEMPLATE-campaign-brief.md`. No customer-facing copy. No em dashes, Western
numerals only.

- campaign_id: [from the brief filename]
- validated_by: strategy-lead
- date: [YYYY-MM-DD]

---

## 1. Per-field status

Status values: PRESENT (confirmed value), ASSUMPTION (placeholder, do not act on), OPEN ITEM
(unresolved, downstream must account for it), MISSING (template expects it, brief silent).

| Section | Field | Status | Note |
|---|---|---|---|
| Identity | campaign_id | [PRESENT/ASSUMPTION/OPEN ITEM/MISSING] | [note] |
| Identity | name | [status] | [note] |
| Entry point | entry_point | [status] | [note] |
| Entry point | objective | [status] | [note] |
| Entry point | success_metric | [status] | [note] |
| Audience | audience | [status] | [note] |
| Audience | segments | [status] | [note] |
| Audience | suppression | [status] | [note] |
| Audience | audience_size | [status] | [planning estimate vs resolved at send time] |
| Offer | product | [status] | [note] |
| Offer | plan | [status] | [note] |
| Offer | price | [status] | [never invented] |
| Offer | promotion | [status] | [never invented] |
| Channels | channels | [status] | [note] |
| Channels | signup_gate | [status] | [note] |
| Channels | gate_platform | [status] | [note] |
| Budget | budget | [status] | [note] |
| Budget | target_cpa_or_roas | [status] | [note] |
| Budget | start_date | [status] | [note] |
| Budget | end_date | [status] | [note] |
| Budget | send_window | [status] | [note] |
| Creative | creative_direction | [status] | [note] |
| Creative | assets_available | [status] | [note] |
| Constraints | constraints | [status] | [note] |
| Approvals | approval_status | [status] | [note] |

## 2. ASSUMPTION list (placeholders, do not act on)

- [field]: [what the brief says, what a real value would unblock]

## 3. OPEN ITEM list (unresolved, downstream must account for)

- [item]: [why it is open, which stream it affects]

## 4. Stop-and-ask list (MISSING fields the campaign needs)

- [field]: [why it is needed] [what is blocked until supplied]

If this list is non-empty, the brief is blocked on those fields. No value is invented to
fill them.

## 5. Planning-estimate fields (resolve from live data later)

- [field]: [estimate carried forward, resolves at send time]

## 6. Readiness

[ready to scope] | [ready to scope with flagged assumptions] | [blocked on the stop-and-ask list]
