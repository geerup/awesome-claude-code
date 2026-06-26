# Rahma Riad: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet holds this instructor's rows and the per-placement picks a designer pulls when a campaign asset needs the real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A generated or AI-edited likeness is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 05 - RAHMA RIAD / 05 - PHOTOGRAPHY`. Enumerated live via the Drive MCP, 2026-06-16. 20 catalogued rows, 20 preferred (one per stem group).

Enumeration note: 05 - PHOTOGRAPHY / RETOUCHED (20 files: 11 jpgs plus two 141414 on-brand png sets, IMG1-6). No ON BLACK subfolder; the 141414 pngs sit directly in RETOUCHED. LOWRES sibling not enumerated. read_file_content returned empty this session, so faces_present and orientation are auto, verify.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read returned empty for these files this session, so faces and orientation are unverified. A human or a working vision read confirms them before a row fills an instructor-likeness slot.
- Very large tif and camera-raw originals are catalogued (or excluded where not image/*) but never fetched. Use the jpg or png preferred variant.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | 18092024_RahmaBG_141414_IMG1.png | 1-NgbV23l0tkPKL7zrNoiCvZjx7g5N6YH | instructor on the brand near-black #141414 set, hero candidate |
| Portrait general | 4:5 | 18092024_RahmaBG_141414_IMG2.png | 1jp5Sq44kHZtbL6q8zSmEGa5qnL2Iasin | preferred portrait candidate, pull by fileId |
| Portrait alternate | 4:5 | 18092024_RahmaBG_141414_IMG3.png | 1gBD2tRFVaDAA540-8KXuMDsvehtqVWhy | preferred portrait candidate, pull by fileId |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match the true aspect at build time once the vision read or a human confirms it.

## All rows

Mirrors this instructor's section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| 18092024_RahmaBG_141414_IMG1.png | 1-NgbV23l0tkPKL7zrNoiCvZjx7g5N6YH | https://drive.google.com/file/d/1-NgbV23l0tkPKL7zrNoiCvZjx7g5N6YH/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| 18092024_RahmaBG_141414_IMG2.png | 1jp5Sq44kHZtbL6q8zSmEGa5qnL2Iasin | https://drive.google.com/file/d/1jp5Sq44kHZtbL6q8zSmEGa5qnL2Iasin/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| 18092024_RahmaBG_141414_IMG3.png | 1gBD2tRFVaDAA540-8KXuMDsvehtqVWhy | https://drive.google.com/file/d/1gBD2tRFVaDAA540-8KXuMDsvehtqVWhy/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| 20102024_RahmaBG_141414_IMG4.png | 1HcrWkql79MGQBuEPIK4iZ88BRwtI2G_I | https://drive.google.com/file/d/1HcrWkql79MGQBuEPIK4iZ88BRwtI2G_I/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| 20102024_RahmaBG_141414_IMG5.png | 1bLnrDQ0RKiDFnq51GHDLDOMg6vpoGokq | https://drive.google.com/file/d/1bLnrDQ0RKiDFnq51GHDLDOMg6vpoGokq/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| 20102024_RahmaBG_141414_IMG6.png | 1shsYu2Nc-IHIx8n5QKAec6F1k0Dw3LS8 | https://drive.google.com/file/d/1shsYu2Nc-IHIx8n5QKAec6F1k0Dw3LS8/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0005.jpg | 1AYlDeD6muuftzAZG48KHQdVQ6OGjLQkE | https://drive.google.com/file/d/1AYlDeD6muuftzAZG48KHQdVQ6OGjLQkE/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0009.jpg | 1TzzSnc-tLcVC8oSxZj5yZHOuu_utg3uq | https://drive.google.com/file/d/1TzzSnc-tLcVC8oSxZj5yZHOuu_utg3uq/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0025.jpg | 1HIRf2ZFSx4KQyJptFuRP7qsVLaQMrJVN | https://drive.google.com/file/d/1HIRf2ZFSx4KQyJptFuRP7qsVLaQMrJVN/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0032.jpg | 1bGyx7d5bAW7ARlaYyH-eR9xe0SPOe-vO | https://drive.google.com/file/d/1bGyx7d5bAW7ARlaYyH-eR9xe0SPOe-vO/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0033.jpg | 1GjZVqz96_FcFuFpnsOapUoW4cMNpmXim | https://drive.google.com/file/d/1GjZVqz96_FcFuFpnsOapUoW4cMNpmXim/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0036.jpg | 1VDomOdgfYhv7sdxnx7xPd7HBHzNiqpRj | https://drive.google.com/file/d/1VDomOdgfYhv7sdxnx7xPd7HBHzNiqpRj/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0037.jpg | 12BwdSr-20NXy-6Z0zOaRKhq9YPHA4GzR | https://drive.google.com/file/d/12BwdSr-20NXy-6Z0zOaRKhq9YPHA4GzR/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0051.jpg | 1izre4Cz5dLJaYPxGTan9r8MY3Rk6-hJR | https://drive.google.com/file/d/1izre4Cz5dLJaYPxGTan9r8MY3Rk6-hJR/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0278.jpg | 1UUJT0zFxhuUB1jo047wgkDSWl7vDUV6u | https://drive.google.com/file/d/1UUJT0zFxhuUB1jo047wgkDSWl7vDUV6u/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0282.jpg | 1O0kz__psEHZVs4XPDKPXSIDfntaX1ID3 | https://drive.google.com/file/d/1O0kz__psEHZVs4XPDKPXSIDfntaX1ID3/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0286.jpg | 1-wrY4xhocrmELBap54ZZzKbFOzVaVeIz | https://drive.google.com/file/d/1-wrY4xhocrmELBap54ZZzKbFOzVaVeIz/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0309.jpg | 1NW7hApmxbaTFxzIdubWs507RdoxbJLfD | https://drive.google.com/file/d/1NW7hApmxbaTFxzIdubWs507RdoxbJLfD/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0310.jpg | 1KRuH6FmlQySmsl1NwcqxGmVMvB-3ck28 | https://drive.google.com/file/d/1KRuH6FmlQySmsl1NwcqxGmVMvB-3ck28/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0312.jpg | 1pq3QZh1F5eoS5VDQSrtYwCRgm1oLDkfB | https://drive.google.com/file/d/1pq3QZh1F5eoS5VDQSrtYwCRgm1oLDkfB/view | RETOUCHED | yes | yes |  | portrait | auto, verify |

## Fetch and refresh

- No proof fetch done for this instructor (Bassam already carries the one cache demo). To fetch a preferred portrait into the gitignored cache, run `python3 .claude/scripts/drive_image_sync.py fetch rahma-riad --placement 4x5`.
- Refresh the rows: re-enumerate in an MCP session, update `scripts/cache/drive-enum-rahma-riad.json`, then run `python3 .claude/scripts/drive_image_sync.py catalog rahma-riad` and `python3 .claude/scripts/image_catalog_check.py rahma-riad`.
