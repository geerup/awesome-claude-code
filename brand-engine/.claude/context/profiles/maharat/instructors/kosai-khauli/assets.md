# Kosai Khauli: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet holds this instructor's rows and the per-placement picks a designer pulls when a campaign asset needs the real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A generated or AI-edited likeness is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 03 - KOSAI KHAULI / 05 - PHOTOGRAPHY`. Enumerated live via the Drive MCP, 2026-06-16. 18 catalogued rows, 16 preferred (one per stem group).

Enumeration note: 05 - PHOTOGRAPHY / RETOUCHED (13 jpgs incl. one _LowRes twin) plus RETOUCHED / BLACK BACKGROUND (two 141414 on-brand sets plus a 300x400 compressed headshot). LOWRES sibling not enumerated. read_file_content returned empty this session, so faces_present and orientation are auto, verify.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read returned empty for these files this session, so faces and orientation are unverified. A human or a working vision read confirms them before a row fills an instructor-likeness slot.
- Very large tif and camera-raw originals are catalogued (or excluded where not image/*) but never fetched. Use the jpg or png preferred variant.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | 04032024_KosaiBG_141414.png | 1d8J0UPHnw7Z9ZZHYNSheo26ri_FtCCN9 | instructor on the brand near-black #141414 (BLACK BACKGROUND set), hero candidate |
| Portrait general | 4:5 | 26012024_Kosai-Khauli-Bg-Change-141414.jpg | 1d8tLHSEwi_wCFt-Y3WuRKzI7W0rfND6N | preferred portrait candidate, pull by fileId |
| Portrait alternate | 4:5 | Kosai_Khauli_300x400_compressed.jpg | 1lDYhQGKHmtmzbYW9ZsPa1TTcHDIL90cv | preferred portrait candidate, pull by fileId |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match the true aspect at build time once the vision read or a human confirms it.

## All rows

Mirrors this instructor's section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| 04032024_KosaiBG_141414.png | 1d8J0UPHnw7Z9ZZHYNSheo26ri_FtCCN9 | https://drive.google.com/file/d/1d8J0UPHnw7Z9ZZHYNSheo26ri_FtCCN9/view | RETOUCHED / BLACK BACKGROUND | yes | yes |  | portrait | auto, verify |
| 26012024_Kosai-Khauli-Bg-Change-141414.jpg | 1d8tLHSEwi_wCFt-Y3WuRKzI7W0rfND6N | https://drive.google.com/file/d/1d8tLHSEwi_wCFt-Y3WuRKzI7W0rfND6N/view | RETOUCHED / BLACK BACKGROUND | yes | yes |  | portrait | auto, verify |
| Kosai_Khauli_300x400_compressed.jpg | 1lDYhQGKHmtmzbYW9ZsPa1TTcHDIL90cv | https://drive.google.com/file/d/1lDYhQGKHmtmzbYW9ZsPa1TTcHDIL90cv/view | RETOUCHED / BLACK BACKGROUND | yes | yes |  | headshot | auto, verify |
| Untitled Capture3074 1.jpg | 1U9rzcJ5SlrzU5rSjAL26Rh7k-omtqd_J | https://drive.google.com/file/d/1U9rzcJ5SlrzU5rSjAL26Rh7k-omtqd_J/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3076 1.jpg | 1Y6ChJQ-HV560oU9rV7MHRGTWiwkHk0jI | https://drive.google.com/file/d/1Y6ChJQ-HV560oU9rV7MHRGTWiwkHk0jI/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3088 1.jpg | 11Zwv9okqUEoMoqR4wOOj2R0ZJBWO394A | https://drive.google.com/file/d/11Zwv9okqUEoMoqR4wOOj2R0ZJBWO394A/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3101 1.jpg | 1dmJ8wN64ZWu0KeLj9bIPFnE_mQhpdocP | https://drive.google.com/file/d/1dmJ8wN64ZWu0KeLj9bIPFnE_mQhpdocP/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3120 1.jpg | 1iWgyFMxwrmfuyLzMmbFxq4lbwvRMKipt | https://drive.google.com/file/d/1iWgyFMxwrmfuyLzMmbFxq4lbwvRMKipt/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3138 1.jpg | 1LKU1J8YaMGEPwDMHXxiYKsAp8eY3jGZ3 | https://drive.google.com/file/d/1LKU1J8YaMGEPwDMHXxiYKsAp8eY3jGZ3/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3166 1.jpg | 1-25WwD-f8MdZDE0JX1nXholFuEEFWCwX | https://drive.google.com/file/d/1-25WwD-f8MdZDE0JX1nXholFuEEFWCwX/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3196 1.jpg | 1AgBHymLZnjn5qDENDi5LppPJUw7Drwfz | https://drive.google.com/file/d/1AgBHymLZnjn5qDENDi5LppPJUw7Drwfz/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3220 1.jpg | 1E-AvFnRm7RHwDEjpxBv_80QGU4rECtET | https://drive.google.com/file/d/1E-AvFnRm7RHwDEjpxBv_80QGU4rECtET/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3227 1.jpg | 1DwNlDSJl6tW2jyX8U8TZEDDY6Joj0SOD | https://drive.google.com/file/d/1DwNlDSJl6tW2jyX8U8TZEDDY6Joj0SOD/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3237 1.jpg | 1gHsDk6BRKcswhXthMQh-Xh6V0YJTxByt | https://drive.google.com/file/d/1gHsDk6BRKcswhXthMQh-Xh6V0YJTxByt/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3248 1.jpg | 14dnRdxvUePr5K2WlOt9AhCvRATqXs1wa | https://drive.google.com/file/d/14dnRdxvUePr5K2WlOt9AhCvRATqXs1wa/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Untitled Capture3248 1_LowRes.jpg | 1jhOyWZSoK_HoeRY4Vb9xdubi75QsbG-T | https://drive.google.com/file/d/1jhOyWZSoK_HoeRY4Vb9xdubi75QsbG-T/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| 04032024_KosaiBG_141414_Recolored_TIM02.png | 1dJc_6vTg_btnvzwEd8xCSeGI3rNl_7oV | https://drive.google.com/file/d/1dJc_6vTg_btnvzwEd8xCSeGI3rNl_7oV/view | RETOUCHED / BLACK BACKGROUND | yes | no | 1d8J0UPHnw7Z9ZZHYNSheo26ri_FtCCN9 | portrait | auto, verify |
| 26012024_Kosai-Khauli-Bg-Change-141414_Recolored_TIM02.png | 1dL4XSzZCj8Nz2dX6WCt83UKSrfPP0fFt | https://drive.google.com/file/d/1dL4XSzZCj8Nz2dX6WCt83UKSrfPP0fFt/view | RETOUCHED / BLACK BACKGROUND | yes | no | 1d8tLHSEwi_wCFt-Y3WuRKzI7W0rfND6N | portrait | auto, verify |

## Fetch and refresh

- No proof fetch done for this instructor (Bassam already carries the one cache demo). To fetch a preferred portrait into the gitignored cache, run `python3 .claude/scripts/drive_image_sync.py fetch kosai-khauli --placement 4x5`.
- Refresh the rows: re-enumerate in an MCP session, update `scripts/cache/drive-enum-kosai-khauli.json`, then run `python3 .claude/scripts/drive_image_sync.py catalog kosai-khauli` and `python3 .claude/scripts/image_catalog_check.py kosai-khauli`.
