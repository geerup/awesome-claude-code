# Ragheb Alama: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet holds this instructor's rows and the per-placement picks a designer pulls when a campaign asset needs the real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A generated or AI-edited likeness is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 01 - RAGHEB ALAMA / 05 - PHOTOGRAPHY`. Enumerated live via the Drive MCP, 2026-06-16. 10 catalogued rows, 8 preferred (one per stem group).

Enumeration note: 05 - PHOTOGRAPHY / RETOUCHED (5 jpgs) plus RETOUCHED / ON BLACK (5 png, the 141414 on-brand set). LOWRES sibling not enumerated (lower-res duplicates). read_file_content returned empty this session, so faces_present and orientation are auto, verify.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read returned empty for these files this session, so faces and orientation are unverified. A human or a working vision read confirms them before a row fills an instructor-likeness slot.
- Very large tif and camera-raw originals are catalogued (or excluded where not image/*) but never fetched. Use the jpg or png preferred variant.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | 04032024_RaghebBG_141414.png | 1zcOPrkscCaqYZbRfvu_uZH3RoeWbqL97 | instructor on the brand near-black #141414 (ON BLACK set), hero candidate |
| Portrait general | 4:5 | 05032024_RaghebBG_141414_Expanded.png | 18lRDmNJO_r8tacxlZHH4U762UiBgd0ft | preferred portrait candidate, pull by fileId |
| Portrait alternate | 4:5 | MAHARAT X RAGHEB ALAMA4597 1.jpg | 1QihCL3m4vrTDvl5N79QRh6bUsxGDVqs5 | preferred portrait candidate, pull by fileId |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match the true aspect at build time once the vision read or a human confirms it.

## All rows

Mirrors this instructor's section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| 04032024_RaghebBG_141414.png | 1zcOPrkscCaqYZbRfvu_uZH3RoeWbqL97 | https://drive.google.com/file/d/1zcOPrkscCaqYZbRfvu_uZH3RoeWbqL97/view | RETOUCHED / ON BLACK | yes | yes |  | portrait | auto, verify |
| 05032024_RaghebBG_141414_Expanded.png | 18lRDmNJO_r8tacxlZHH4U762UiBgd0ft | https://drive.google.com/file/d/18lRDmNJO_r8tacxlZHH4U762UiBgd0ft/view | RETOUCHED / ON BLACK | yes | yes |  | portrait | auto, verify |
| MAHARAT X RAGHEB ALAMA4597 1.jpg | 1QihCL3m4vrTDvl5N79QRh6bUsxGDVqs5 | https://drive.google.com/file/d/1QihCL3m4vrTDvl5N79QRh6bUsxGDVqs5/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT X RAGHEB ALAMA4602 1.jpg | 1QsGc4cX32-qbRnt0SfrZ9r50MW0wPteb | https://drive.google.com/file/d/1QsGc4cX32-qbRnt0SfrZ9r50MW0wPteb/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT X RAGHEB ALAMA4608 1.jpg | 1R76UlANzFxyhCK4f48OSfxHgxk-5LNye | https://drive.google.com/file/d/1R76UlANzFxyhCK4f48OSfxHgxk-5LNye/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT X RAGHEB ALAMA4756 1.jpg | 1R2JHMivhNPBliBmgDnVQP_RQYIe7aMlr | https://drive.google.com/file/d/1R2JHMivhNPBliBmgDnVQP_RQYIe7aMlr/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT X RAGHEB ALAMA4773 1.jpg | 1R9_EchA2eGIROS9jtmZwSMizFqu4AGyq | https://drive.google.com/file/d/1R9_EchA2eGIROS9jtmZwSMizFqu4AGyq/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| f42b5166-0704-4d83-b405-f3479b2f3cd2.png | 1Vv82LVNaHOphpnk1ozm_Ab1QVycL2oiz | https://drive.google.com/file/d/1Vv82LVNaHOphpnk1ozm_Ab1QVycL2oiz/view | RETOUCHED / ON BLACK | yes | yes |  | portrait | auto, verify |
| 05032024_RaghebBG_141414_Expanded_Recolored.png | 1qrG9MzGMGfii5TFa1z2peTnBLTPOFtyp | https://drive.google.com/file/d/1qrG9MzGMGfii5TFa1z2peTnBLTPOFtyp/view | RETOUCHED / ON BLACK | yes | no | 18lRDmNJO_r8tacxlZHH4U762UiBgd0ft | portrait | auto, verify |
| 05032024_RaghebBG_141414_Expanded_Recolored_TIM02.png | 1cH1xMK0ciu40GVhrWwtljLn4kvFd5LEa | https://drive.google.com/file/d/1cH1xMK0ciu40GVhrWwtljLn4kvFd5LEa/view | RETOUCHED / ON BLACK | yes | no | 18lRDmNJO_r8tacxlZHH4U762UiBgd0ft | portrait | auto, verify |

## Fetch and refresh

- No proof fetch done for this instructor (Bassam already carries the one cache demo). To fetch a preferred portrait into the gitignored cache, run `python3 .claude/scripts/drive_image_sync.py fetch ragheb-alama --placement 4x5`.
- Refresh the rows: re-enumerate in an MCP session, update `scripts/cache/drive-enum-ragheb-alama.json`, then run `python3 .claude/scripts/drive_image_sync.py catalog ragheb-alama` and `python3 .claude/scripts/image_catalog_check.py ragheb-alama`.
