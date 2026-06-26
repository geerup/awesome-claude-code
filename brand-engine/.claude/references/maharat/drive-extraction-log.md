# Drive extraction log

Running record of what was mined from the Drive into the scaffold, per
drive-content-mining-plan.md and instructor-mining-plan.md. One table per area.
Prevents double-extraction and makes gaps explicit.

## Instructors / 09 - Mona Ataya (pilot A) - extracted 2026-06-04

| Drive item | Type | Read | Destination(s) | Status |
|---|---|---|---|---|
| [ONE-LINERS FINAL](https://docs.google.com/document/d/1HX5j01JRW1Y2Z3EwNtdQxiJVTIYw97uYGKPVE2X-V2o/edit) | doc, AR | yes, full | voice.md hook patterns, one-liner-library.md, claims table rows 4, 6, 11, 12 | done |
| [FINAL PLAYLIST QUESTIONS](https://docs.google.com/document/d/1zhB6idVFFuJZIU2SW-1sigU916okccFcW6BOQXsE0pw/edit) | doc, bilingual | yes, full | fact file product themes (confirmed playlist set) | done |
| [Mona Playlist Questions (draft)](https://docs.google.com/document/d/1l7TDLeD0mjhMFINHi4FBgNvRy6ZNtQOmiZf-VDd83HU/edit) | doc, bilingual, 2 tabs | yes, full | fact file draft-theme pool, bio facts (claims 15), voice traits | done |
| Organic/ [Shoot Shot List](https://docs.google.com/document/d/1Sr7kGkxAosvUuq2DiZp2Ic8kZPOPcW5L8rrXxH9WfLE/edit) | doc | partial (search preview) | fact file assets; flagged as stream-3 shot-list template candidate for creative-production | partial |
| Research and Strategy | doc or file, unreadable via connector | no | fact file marks it to read manually | blocked |
| Raw footage location | not in Drive docs | no | fact file open item | open |

External verification (research-scout pass, 2026-06-04): Gulf Business, UNCTAD eTrade
for Women, Scoop Empire, Tracxn, Mumzworld blog. Outcomes in the fact-file claims table.
Notable: the 60M figure in the one-liners is not corroborated (sources say over 50M);
the 90 percent first-year failure stat is disputed as stated.

Pack produced:
- context/instructors/_CATALOG.md (registry, 11 rows)
- context/instructors/mona-ataya.md (fact file, 16-row claims table)
- skills/instructor-marketing/SKILL.md (hub)
- skills/instructor-marketing/mona-ataya/{SKILL.md, voice.md, templates/one-liner-library.md, evals/evals.json}

Open items raised by this pilot:
1. Register policy (Levantine instructor voice vs brand MSA). Owner: Arman with Ahmed.
2. Claims confirmation for rows 4, 6, 11; replacement for row 12. Owner: TBD.
3. Catalog public status for all 11 instructors. Owner: Ahmed or team.
4. The unreadable Research and Strategy item (connector scope or file format).
5. Official AR name spellings against campaign assets.
6. Mona Ataya landing page URL, social handles, footage location.

## Pending areas (not yet mined)

Instructors: 01 Ragheb Alama (pilot B, next), then 10, Mo Islam, 08, 07, 06, 05, 04,
03, 02 per the batch order. 00- Maharat folder: phase 2, starting with 07 Email and
WhatsApp Marketing.

## Pilot A review pass - 2026-06-04

Findings fixed: organic shot-list template created (full doc fetched);
EN renders added to the one-liner library; fact file extended with claims rows 17 to 20
(7 funding rounds, 80 plus awards, 2.5M plus mothers as of 2025, Pharmacity
single-source unverified); status-evidence check performed (no public Maharat listing
found, evidence-neutral, status stays unconfirmed); catalog domain provenance marked;
evals.json upgraded to machine_checks (applies_to scoped) + llm_checks;
scripts/eval_runner.py added and self-tested (golden pass exits 0, golden fail exits 1,
governance files pass with --docs).

Process learnings encoded into context/mining-plan-v2.md (the operational plan) and
RUNBOOK.md (Claude Code end-to-end execution). Repo wiring needs recorded in PATCHES.md.

## Batch run, all remaining instructors - 2026-06-04

Method: batched two-pass inventory (OR-parent queries), full fetch of every readable
content doc, web verification (Entrepreneur feature, Arab News, maharat.com homepage,
Play Store listing), packs written, QA per pack_check.

| Instructor | Readable content found | Deeper structure (phase-2 targets) | Verification outcome |
|---|---|---|---|
| elda-choucair | Marketing Script (30 one-liners EN+AR, 3 personas, 3 ad scripts), Curriculum Ideation (13 chapters), PR and LinkedIn launch plan (executed Feb 2026), Brand/Emotions doc | Maharat x Omnicom, OM Logo, Paid, Email, Content, Research, PM | CEO Omnicom Media Group MENA, 20 plus years: verified; 100 plus brands, spend, Cannes: held back |
| ragheb-alama | Music Cheatsheets (3 bilingual lead magnets) | 00 PM, 09 Influencers folders | 40 plus years and public listing: verified via maharat.com |
| salam-dakkak | none at readable level | Website SD folder | Best Female Chef MENA, 20 plus recipes, listing: verified; she is a CHEF (corrects earlier acting guess); award body and year: held back |
| toufic-kredieh | none at readable level | full 00 to 09 campaign tree (Jan 2025) | Founder of Brands For Less, launched: verified via Entrepreneur; spelling Kreidieh in press |
| cedric-haddad | none at readable level | full 01 to 09 campaign tree plus Maharat-side folders | Celebrity stylist, first class launched Aug 2025: verified via Arab News |
| kosai-khauli | none at readable level | full 01 to 08 campaign tree (2024) | Syrian actor, launched: verified via Entrepreneur |
| bassam-fattouh | none at readable level | 03 to 09 tree plus 10 Reactivation and Bridal, 11 Bridal | Listing with step-by-step positioning: verified; two homepage lines may mean two products: confirm |
| rahma-riad | none | full 01 to 08 campaign tree (2024) | No public listing found; class existence to confirm |
| sami-al-jaber | none | Research folder (Jan 2025) | No public listing found; class existence to confirm |
| mo-islam | none | Research folder (Oct 2025) | Identity unconfirmed; stub pack |

Platform: launched 2023, 8 classes by Aug 2025, 200k followers, 1.5M visitors,
100 plus countries, co-founders Arman Khederlarian and Bassem Jamaleddine (Entrepreneur).

Failure isolation notes: depth-2 campaign-folder content was inventoried with links but
not fetched (call-budget bound); recorded as phase-2 targets, not as absent. No pack
required more than 1 repair cycle (the directory-creation defect on the first write,
fixed and re-run).

## Phase 2: 00- Maharat / 07 Email and WhatsApp Marketing - 2026-06-04

| Drive item | Read | Destination | Status |
|---|---|---|---|
| Ortto Integration List of Questions | yes, full | context/findings-email-platform.md (THE incumbent-platform finding) | done |
| Email Marketing - Process Improvement | yes, full | same finding (Ortto module system, brand components) | done |
| User Lists Required | yes, full | skills/07-lifecycle-messaging/segmentation-logic/templates/maharat-user-lists.md | done |
| Newsletter Learnings (MasterClass study) | yes, full | skills/04-copywriting/email-copy/templates/newsletter-patterns.md | done |
| WhatsApp/ subfolder | empty via connector | manual read queued | blocked |
| TPAY Announcement, Database, Cold Emailing, Failed Payments, Inspo subfolders | inventoried | phase-2 depth targets | pending |

Headline: the incumbent email platform open item is CLOSED at the naming level (Ortto,
2024 evidence); currency confirmation queued. The six-list segmentation architecture
and the MasterClass email patterns are now engine templates.

## Phase 2 continued: 07 subfolders, 01 Campaigns, 15 CRM - 2026-06-04

| Drive item | Read | Destination | Status |
|---|---|---|---|
| TPAY Email Announcement | yes, full | email-copy/templates/tpay-egypt-announcement.md (register precedent + payments fact) | done |
| Maharat CRM Requirements (15 CRM) | yes, full | findings-email-platform.md update (Ortto confirmed Feb 2025, HubSpot migration plan, retention trigger, plan discrepancy, viewership triggers) | done |
| Failed Payments Copy | yes, full | 07-lifecycle/templates/failed-payment-recovery.md | done |
| 01 Campaigns folder listing | yes | 09-reporting/learnings-log/templates/campaign-calendar.md (8 campaign precedents indexed) | done (depth pass later) |
| Inspo subfolder | listing only | Skillshare and Masterclass competitor-study folders: phase-2 depth | pending |
| Database, Cold Emailing subfolders | listing only | phase-2 depth | pending |
| 00 Guidelines | second enumeration attempt, still empty via connector | brand-kit open item stays blocked; read manually | blocked |

## Final round: campaign depth, department areas, growth and data - 2026-06-04

| Drive item | Read | Destination | Status |
|---|---|---|---|
| Launch Week Checklist (17 PLAYLISTS) | yes, full | 05-build-launch/templates/launch-week-checklist.md | done |
| Notification Strategy (17 PLAYLISTS) | yes, full | 07-lifecycle/templates/push-notification-principles.md | done |
| Referral Program Strategy Research | yes, full | 02-strategy/templates/referral-program-precedent.md | done |
| App Launch Emails plus App Description | yes, full | 04-copywriting/email-copy/templates/app-launch-emails.md | done |
| Maharat x Aanaab World Education Day docs | listing plus partial | findings-payments-and-partnerships.md | done |
| Boku Research, Boku Alternatives | listing plus partial | same findings file (payments workstream) | done |
| CDF KSA, MHRSD, AFMI, Top 5 Skincare MENA (01 Research) | listing | indexed; B2G cluster parked out of scope per the board | done |
| Ad Campaign Reports, Data Project Briefs (12 Reporting) | listing | phase-3 backlog (paid results goldens) | pending |
| 17 PLAYLISTS: Landing Page, Organic, Influencers subfolders | listing | campaign-archive depth backlog | pending |
| Campaign folders Ramadan 2025 and 2026, BF 2025, EOY 2024 and 2025, Beauty Persona, B1G1 | structure plus partials | campaign-calendar.md indexes all; depth pass is phase-3 | pending |
| EOY Email Content, Playlists Personas, Hero Asset Ideation, Website and App Briefs | TOO LARGE via connector | manual export queued | blocked |
| 12 LEAD GEN, 16 Paid, 14 Social, Growth Hacking, Data, 100M Money Models, Skillshare, Masterclass inspo, Cold Emailing, Database | empty via connector (likely non-Doc files) | manual read queued | blocked |
| 00 Guidelines | second attempt, still unenumerable | brand kit stays blocked on manual read | blocked |

MINING PROGRAM STATUS: phases 1 and 2 of mining-plan-v2 are COMPLETE. Every in-scope
area is now mined, indexed with links, or explicitly blocked with a named manual
action. Phase 3 backlog (depth passes: campaign folders, instructor campaign trees,
Ad Campaign Reports, Inspo studies) is recorded above and in the review queue.

## Class transcripts (Route B manual export) - 2026-06-04

Full class transcripts placed under references/drive-raw/<slug>/ for the instructor
mining pipeline. Raw source only, rewritten to house style on extraction, never copied
through. Slugs match context/instructors/_CATALOG.md.

| Instructor (slug) | File | Destination |
|---|---|---|
| bassam-fattouh | BASSAM_FATTOUH_BRIDAL_Full_Transcript.docx | drive-raw/bassam-fattouh/ |
| bassam-fattouh | Bassam_Fattouh_Makeup_Transcripts.docx | drive-raw/bassam-fattouh/ |
| cedric-haddad | Cedric_Haddad_Master_Transcript_Complete.docx | drive-raw/cedric-haddad/ |
| elda-choucair | Elda_Choucair_Masterclass_Transcript_CH01-11.docx | drive-raw/elda-choucair/ |
| kosai-khauli | Kosai_Khauli_Acting_Transcripts.docx | drive-raw/kosai-khauli/ |
| rahma-riad | Rahma_Riad_Masterclass_COMPLETE.docx | drive-raw/rahma-riad/ |
| salam-dakkak | Salam_Dakkak_Cooking_Transcripts.docx | drive-raw/salam-dakkak/ |
| toufic-kredieh | Toufic Kreidieh - Full Transcript (Arabic).docx | drive-raw/toufic-kredieh/ |
| toufic-kredieh | Toufic Kreidieh - Full Transcript (English).docx | drive-raw/toufic-kredieh/ |

Notes:
- The folder "Toufic Kreidieh" maps to the existing catalog slug toufic-kredieh (the
  catalog records the press spelling Kreidieh). Toufic has both an Arabic and an English
  transcript.
- These are the richest primary source yet for these 7 instructors. They notably upgrade
  the evidence-thin pack for rahma-riad. A re-mine pass per slug can now lift those packs
  from mined-thin or mined to transcript-grounded. Pack and public-status changes still
  follow the catalog rules and the review queue, not this log.

## Instructor photography (approved-image catalog) - 2026-06-16

Enumerated the per-class photography folders under `01 - Classes` to build the approved-instructor
-image catalog (`context/instructors/_IMAGE-CATALOG.md`, mapped by `_IMAGE-FOLDER-MAP.md`). Domain
Viewer access (maharat.com) is in place so the Drive API enumerates the tree. Read-only this
session. The Google Drive MCP server is NOT adopted in settings.json (build-vs-buy plus Ahmed,
flagged in the catalog header). Photography folders are matched by NAME ("contains PHOTOGRAPHY"),
not the NN prefix (the prefix is inconsistent across classes).

| slug | photography folder (id) | enumerated | Destination | Status |
|---|---|---|---|---|
| bassam-fattouh | 05 - PHOTOGRAPHY (1pJvTgwAlhXDlc5Uh_LH7eyjzUuRsor8i) | yes, RETOUCHED tree (12 + ON BLACK 4 = 16) | _IMAGE-CATALOG.md, bassam-fattouh/assets.md, cache drive-enum-bassam-fattouh.json | done (LOWRES, LOWRES SELECTS pending) |
| ragheb-alama | 05 - PHOTOGRAPHY (1-WcULZEIbWY3zO2P5C684STHtw6-i3ax) | folder id only | _IMAGE-CATALOG.md (pending enumeration), ragheb-alama/assets.md | pending |
| salam-dakkak | 05 - PHOTOGRAPHY (1dPqtSRawgWNVEPikCbDoz1OR4Bn_5VfM) | folder id only | _IMAGE-CATALOG.md (pending enumeration), salam-dakkak/assets.md | pending |
| kosai-khauli | 05 - PHOTOGRAPHY (1351XoZC4GvQ678p7lYJleQ4Q7QDwmlg5) | folder id only | _IMAGE-CATALOG.md (pending enumeration), kosai-khauli/assets.md | pending |
| rahma-riad | 05 - PHOTOGRAPHY (1FsptUaWxBpaj3LopkZNHKnRsOzm0ud4r) | folder id only | _IMAGE-CATALOG.md (pending enumeration), rahma-riad/assets.md | pending |
| toufic-kredieh | 09 - PHOTOGRAPHY (1WF1RPZ6paqweydNI3Ojvx3HlUEwQ2XwJ) | folder id only | _IMAGE-CATALOG.md (pending enumeration), toufic-kreidieh/assets.md | pending |
| cedric-haddad | 02 - PHOTOGRAPHY (1nld61pRt37eVDYxPTloYYrNLyQ37ZUGk) | folder id only | _IMAGE-CATALOG.md (pending enumeration), cedric-haddad/assets.md | pending |
| elda-choucair | 02 - PHOTOGRAPHY (1TSZULeSeh9CXAtZOOHEFvgXhEE7SFTnA) | folder id only | _IMAGE-CATALOG.md (pending enumeration), elda-choucair/assets.md | pending |
| mona-ataya | 02 - PHOTOGRAPHY (19rNF6wxbHqpvE9AyJz03sp7vHee7asMD) | folder id only | _IMAGE-CATALOG.md (pending enumeration), mona-ataya/assets.md | pending |
| bassam-fattouh-bridal | none, uses 05 - BANK OF STILLS (1mnueQBjWpGh1NxTeYVxxUhtKR97rmbgN) | folder id only | _IMAGE-CATALOG.md (pending enumeration) | pending |
| sami-al-jaber | none | n/a | recorded as no imagery in Drive | no folder |
| mo-islam | none | n/a | recorded as no imagery in Drive | no folder |

Notes:
- Bassam dedup landmarks held on live data: the `MAHARAT III0579` group (jpg, _COLORCORRECTED.tif
  at 165 MB, _COLORCORRECTED_Blurred.png) collapses to one preferred (the jpg); the
  `15052024_BassamBG_141414` set collapses to one preferred (the base on-brand #141414 portrait).
- Proof fetch: `MAHARAT III0507.jpg` pulled via `download_file_content` into the gitignored cache
  `assets/instructors/bassam-fattouh/` (5,780,385 bytes, valid JPEG), confirming the fetch path and
  that the cache is not committed.
- The Drive `read_file_content` vision read returned empty for these image files, so faces_present
  and orientation are `auto, verify` (unverified). rights_status per image is `confirm with Ahmed`.
