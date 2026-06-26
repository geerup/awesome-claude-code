# Bassam Fattouh: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet
holds Bassam's rows and the per-placement picks a designer pulls when a campaign asset needs the
real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A
generated likeness of Bassam is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 04 - BASSAM FATTOUH / 05 - PHOTOGRAPHY`
(folderId `1pJvTgwAlhXDlc5Uh_LH7eyjzUuRsor8i`). Enumerated live via the Drive MCP, 2026-06-16.
RETOUCHED (`1K9wciRUzRqUtCT3FXaW8OWXiPagdUhHT`) holds 12 images plus an `ON BLACK` subfolder of 4.
The `LOWRES` and `LOWRES SELECTS` siblings are not yet enumerated (phase-2 depth).

RETOUCHED is preferred. The `15052024_BassamBG_141414` set is the hero candidate: the instructor
already composited on the brand near-black #141414.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a
  human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read
  returned empty for these files this session, so faces and orientation are unverified. A human or
  a working vision read confirms them before a row fills an instructor-likeness slot. Filenames and
  the shoot context strongly imply studio portraits, but that is not yet machine-confirmed.
- The `.tif` (`MAHARAT III0579 copy_COLORCORRECTED.tif`) is 165 MB. Do not fetch it. Use the jpg
  preferred twin.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | 15052024_BassamBG_141414.png | 1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR | instructor on the brand #141414, hero candidate, RETOUCHED |
| Portrait, general | 4:5 | MAHARAT III0507.jpg | 1mfvxt10ah9GHXFP6qTbkKJ3k_4zvx-mS | RETOUCHED portrait, jpg, fetched to cache as the proof image |
| Portrait, alternate | 4:5 | MAHARAT III0579 copy.jpg | 1CNIEdaBc7vzDbFr8Ga266Q67_FJViJ9v | RETOUCHED portrait, preferred over its .tif and _Blurred twins |
| Detail crop (not a likeness slot) | varies | MAHARAT III0655 copy_RetouchedShoe.jpg | 17vI3dsFQaXLYGlXbDLnbl6PcpX7R1e3v | product or detail, faces_present no, do not use as the instructor |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match
the true aspect at build time once the vision read or a human confirms it.

## All Bassam rows

Mirrors the bassam-fattouh section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its
stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| 15052024_BassamBG_141414.png | 1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR | https://drive.google.com/file/d/1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR/view | RETOUCHED / ON BLACK | yes | yes |  | portrait | auto, verify |
| MAHARAT III0507.jpg | 1mfvxt10ah9GHXFP6qTbkKJ3k_4zvx-mS | https://drive.google.com/file/d/1mfvxt10ah9GHXFP6qTbkKJ3k_4zvx-mS/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0516.jpg | 1boT9rSgP926Mb8Sx1S6waImoygmO981H | https://drive.google.com/file/d/1boT9rSgP926Mb8Sx1S6waImoygmO981H/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0537.jpg | 18aZYXE1kpekJmd6Qpa_RsqlqU-o3RIHD | https://drive.google.com/file/d/18aZYXE1kpekJmd6Qpa_RsqlqU-o3RIHD/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0542.jpg | 10ThF2Eq4DwP0mtZgdgzeh-sRcgpIDOtw | https://drive.google.com/file/d/10ThF2Eq4DwP0mtZgdgzeh-sRcgpIDOtw/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0579 copy.jpg | 1CNIEdaBc7vzDbFr8Ga266Q67_FJViJ9v | https://drive.google.com/file/d/1CNIEdaBc7vzDbFr8Ga266Q67_FJViJ9v/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0598 copy.jpg | 1ggGJXnIUpCNkIpP8MWfyfiNatU_poHMA | https://drive.google.com/file/d/1ggGJXnIUpCNkIpP8MWfyfiNatU_poHMA/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0627 copy.jpg | 1OfPKX2FP_zjYgjbHCr4RKNog38n6-iZ5 | https://drive.google.com/file/d/1OfPKX2FP_zjYgjbHCr4RKNog38n6-iZ5/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT III0655 copy.jpg | 1HOt1qbPDB98E4uAjecKHiU-ADMEEmE65 | https://drive.google.com/file/d/1HOt1qbPDB98E4uAjecKHiU-ADMEEmE65/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| 15052024_BassamBG_141414_Blurred.png | 1EJnTdbYF8j60dzJIbAVK2G6JAfhpokXl | https://drive.google.com/file/d/1EJnTdbYF8j60dzJIbAVK2G6JAfhpokXl/view | RETOUCHED | yes | no | 1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR | portrait | auto, verify |
| 15052024_BassamBG_141414_Blurred.png | 1KYRdZIVHYX4dpXvskmeEW5-ZQ68bHOJg | https://drive.google.com/file/d/1KYRdZIVHYX4dpXvskmeEW5-ZQ68bHOJg/view | RETOUCHED / ON BLACK | yes | no | 1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR | portrait | auto, verify |
| 15052024_BassamBG_141414_Blurred_Recolored_TIM02.png | 1KH1FvrOUDpyzkDhQ_09daQxrhgFPnwfD | https://drive.google.com/file/d/1KH1FvrOUDpyzkDhQ_09daQxrhgFPnwfD/view | RETOUCHED / ON BLACK | yes | no | 1KZ8gLRTyInxnuvvgZM8lbE-C-px10lqR | portrait | auto, verify |
| MAHARAT III0516.jpg | 1KRPpRriE0T4dkTifUsoGB8uws24uWkLz | https://drive.google.com/file/d/1KRPpRriE0T4dkTifUsoGB8uws24uWkLz/view | RETOUCHED / ON BLACK | yes | no | 1boT9rSgP926Mb8Sx1S6waImoygmO981H | portrait | auto, verify |
| MAHARAT III0579 copy_COLORCORRECTED.tif | 1UUwmJHvWzWmHQdsdBdlBkJWmkiOfVz1V | https://drive.google.com/file/d/1UUwmJHvWzWmHQdsdBdlBkJWmkiOfVz1V/view | RETOUCHED | yes | no | 1CNIEdaBc7vzDbFr8Ga266Q67_FJViJ9v | portrait | auto, verify |
| MAHARAT III0579 copy_COLORCORRECTED_Blurred.png | 1G-S8tNpbdx-LJngekpCMUXnzqgFvMH1N | https://drive.google.com/file/d/1G-S8tNpbdx-LJngekpCMUXnzqgFvMH1N/view | RETOUCHED | yes | no | 1CNIEdaBc7vzDbFr8Ga266Q67_FJViJ9v | portrait | auto, verify |
| MAHARAT III0655 copy_RetouchedShoe.jpg | 17vI3dsFQaXLYGlXbDLnbl6PcpX7R1e3v | https://drive.google.com/file/d/17vI3dsFQaXLYGlXbDLnbl6PcpX7R1e3v/view | RETOUCHED | yes | no | 1HOt1qbPDB98E4uAjecKHiU-ADMEEmE65 | product-detail | no |

## Fetch and refresh

- Proof fetch done: `MAHARAT III0507.jpg` was pulled via the Drive MCP `download_file_content` into
  `assets/instructors/bassam-fattouh/MAHARAT_III0507.jpg` (5,780,385 bytes, valid JPEG). That path
  is gitignored, so `git status` shows nothing under `assets/`.
- Refresh the rows: re-enumerate in an MCP session, update
  `scripts/cache/drive-enum-bassam-fattouh.json`, then run
  `python3 .claude/scripts/drive_image_sync.py catalog bassam-fattouh` and
  `python3 .claude/scripts/image_catalog_check.py bassam-fattouh`.
