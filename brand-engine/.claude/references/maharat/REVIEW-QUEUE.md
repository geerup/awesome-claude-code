# REVIEW QUEUE (the asynchronous human gate)

Decisions awaiting a human. Batch runs append here instead of stopping. Resolve an
item, apply the resolution (catalog or fact file), then delete the entry. Owners:
Ahmed (statuses, claims, campaign questions), Arman (brand, register, paywall).

Until an instructor's status item is resolved, that instructor's pack is internal-only
and produces no public-facing assets.

## Open items

### Policy (blocks no mining, blocks public rendering choices)
- [ ] Register policy: instructor-voice Levantine colloquial vs brand Gulf-familiar
      MSA. Packs currently render MSA per the interim policy. Owner: Arman with Ahmed.
- [ ] Claims-confirmation owner: who verifies internal figures the public record
      cannot (first queue below). Owner: Ahmed to assign.

### mona-ataya (pack mined 2026-06-04, pending)
- [ ] Public status: launched or in production? Public-site check found no listing
      (evidence-neutral). Owner: Ahmed.
- [ ] Claim row 4: confirm the 60 million figure or keep "over 50 million" (sourced).
- [ ] Claim row 6: confirm "3 kids under age 10" detail or keep "3 children".
- [ ] Claim row 11: confirm the 2 percent internet-penetration stat.
- [ ] Claim row 12 replacement: a sourced startup-failure stat, if one is wanted.
- [ ] Claim row 20: confirm Pharmacity (single source) before any use.
- [ ] Unreadable Drive item: Research and Strategy doc; read manually and fold in.
- [ ] Landing page URL, social handles, footage location.
- [ ] Official AR name spelling against campaign assets.

### Phase 2 findings (2026-06-04)
- [ ] PLATFORM (updated): Ortto confirmed as incumbent in the Feb 2025 CRM doc, AND a full Ortto-to-HubSpot migration is the team's stated long-term plan (interim HubSpot MVP, advisor Vahakn, owner-brief George). TENSION: the workshop research said skip HubSpot (weak Arabic RTL). Resolve: where is the migration in mid 2026, and has an Arabic test run on HubSpot? Owner: Ahmed with George and Vahakn.
- [ ] PLAN STRUCTURE: the CRM doc says class vs 6-month vs 12-month; the company brief says 1, 3, 12 months. Confirm the real lineup before any pricing copy. Owner: Ahmed.
- [ ] REGISTER PRECEDENT (input to the register-policy question): production emails use Egyptian colloquial for Egypt-targeted promo (TPAY) and MSA for transactional (failed payments). The policy is likely a purpose-by-geo matrix; decide it as such. Owner: Arman with Ahmed.
- [ ] WhatsApp subfolder unreadable via connector: read manually; the BSP question stays open.
- [ ] TPAY Announcement folder: confirm what it is (carrier billing?) in the payments context.
- [ ] User-lists automation: the historical pull and ongoing automation from the lists doc has no named owner (joins the ManyChat item).

### Final mining round (2026-06-04)
- [ ] PRODUCT NAMING: Playlists launched Oct 2025 as the bite-size product; the brief says Skill Paths is built but not launched. Same product, sibling, or successor? Blocks any copy that names either. Owner: Arman with Ahmed.
- [ ] Referral program (give 20, get 20 research, Oct 2025): did it ship? If yes it joins the lifecycle arc; if no it is a ready stream-2 proposal. Owner: Ahmed.
- [ ] Manual exports needed (too large for the connector): EOY Email Content, Maharat Playlists Personas, Playlists Hero Asset Ideation, Website and App Briefs.
- [ ] Ad Campaign Reports folder (12 Reporting): the paid results archive; schedule as the phase-3 source for analytics-reporter goldens and the learnings log.
- [ ] Aanaab partnership: still active? The World Education Day pattern is reusable each January if so. Owner: Ahmed.

### (batch runs append per-instructor sections below)

### Batch run 2026-06-04 (10 packs)

#### Status confirmations (Ahmed): flip catalog public status where appropriate
- [ ] elda-choucair: internal launch plan executed Feb 2026 (strongest evidence). Confirm launched plus official class title and URL.
- [ ] ragheb-alama, salam-dakkak, bassam-fattouh, cedric-haddad, kosai-khauli, toufic-kredieh: publicly listed or press-confirmed as launched. Confirm each, plus official titles and URLs.
- [ ] rahma-riad, sami-al-jaber: NO public evidence found. Does a class exist or is it in production? Packs are hard-blocked from public assets until answered.
- [ ] mo-islam: identity unconfirmed. Who is this and what is the class? One line unblocks the pack.
- [ ] mona-ataya: status still pending from pilot A.

#### Held-back claims to confirm (owner: per the claims-confirmation assignment)
- [ ] elda: "100 plus brands", spend figures, the Cannes Grand Prix case (name the campaign).
- [ ] salam: awarding body and year behind Best Female Chef MENA.
- [ ] toufic: surname spelling (Kredieh vs press Kreidieh); any figures before use; homepage success-strategies line attribution.
- [ ] cedric: celebrity client names are permanently blocked unless explicitly cleared.
- [ ] kosai: series and award names before any are used.
- [ ] bassam: do the two homepage lines mean one class or two products?
- [ ] sami: every career stat (caps, goals, records) per-claim before use.

#### Process items
- [ ] Depth-2 campaign folders (toufic, cedric, kosai, bassam, rahma, elda subfolders): schedule the phase-2 deep mine; they likely hold proven past copy.
- [ ] Official AR name spellings for all, against campaign assets.

### arabskills.info external skills (research 2026-06-10, pending)
Source: arabskills.info (github.com/ArabAgentSkills/Skills, MIT, nascent: 7 stars, 1 maintainer, draft maturity). Full readout: references/2026-06-arabskills-info-skills-research.md. Nothing installed. Decision is Ahmed's, per principle 3.
- [x] ADOPTED 2026-06-10 (recorded as the explicit Ahmed-gate approval). Farasa removed (research-only). `AS-arabic-nlp` is live at .claude/skills/AS-arabic-nlp/ and the branch was merged to main. Scope: CAMeL Tools (MIT, default) plus the GPL family (flagged). Security review clean (bundled script dropped). See .claude/skills/AS-arabic-nlp/VETTING.md.
- [ ] Remaining open item, does NOT block the skill as guidance: legal sign-off on the GPL-family licenses (PyArabic GPL-3.0 confirmed; Tashaphyne, Qalsadi, arabic-stopwords to confirm individually) before those libraries are bundled or distributed in the product. Decide separate-process vs linked integration at that time. Owner: legal.
- [ ] `AS-arab-market-context`: hold by default. Decide whether an external, AI-drafted country-context skill is wanted alongside curated context/ (which wins on conflict). Owner: Ahmed.
- [ ] `AS-arabic-copywriting-dialects`: recommended do-not-adopt (competes with copywriter-ar plus arabic-copy-qa, carries off-brand dialect and Arabizi, does not encode the no-em-dash, Western-numerals, no-tatweel rules). Confirm reject, or scope a review of only its reference notes. Owner: Arman with Ahmed.
- [ ] Confirm rejection of the bulk `npx skills add ArabAgentSkills/Skills` route (runs an npm installer, pulls all 22 skills including payments, identity, and PII-scoped ones out of scope here). Owner: Ahmed.
