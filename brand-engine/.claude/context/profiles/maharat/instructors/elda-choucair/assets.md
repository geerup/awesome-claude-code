# Elda Choucair: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet holds this instructor's rows and the per-placement picks a designer pulls when a campaign asset needs the real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A generated or AI-edited likeness is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 08 - ELDA CHOUCAIR / 02 - PHOTOGRAPHY`. Enumerated live via the Drive MCP, 2026-06-16. 7 catalogued rows, 7 preferred (one per stem group).

Enumeration note: 02 - PHOTOGRAPHY / RETOUCHED (7 C08-maharat jpgs). SELECTS, HIGHRES, LOWRES siblings not enumerated. read_file_content returned empty this session, so faces_present and orientation are auto, verify.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read returned empty for these files this session, so faces and orientation are unverified. A human or a working vision read confirms them before a row fills an instructor-likeness slot.
- Very large tif and camera-raw originals are catalogued (or excluded where not image/*) but never fetched. Use the jpg or png preferred variant.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | C08-maharat-1038.jpg | 1v5uTO-8RRyOgRB1EbfJa5aT6lSpPwdmw | RETOUCHED portrait (no on-black set exists for Elda yet) |
| Portrait general | 4:5 | C08-maharat-1041.jpg | 1_3n0b3zVSefKqG9iVqiFr2MpjQXhu-OG | preferred portrait candidate, pull by fileId |
| Portrait alternate | 4:5 | C08-maharat-1060.jpg | 1hRpRqOGvBL0Qv8lh4feq1DIt45J-Ulo7 | preferred portrait candidate, pull by fileId |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match the true aspect at build time once the vision read or a human confirms it.

## All rows

Mirrors this instructor's section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| C08-maharat-1038.jpg | 1v5uTO-8RRyOgRB1EbfJa5aT6lSpPwdmw | https://drive.google.com/file/d/1v5uTO-8RRyOgRB1EbfJa5aT6lSpPwdmw/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| C08-maharat-1041.jpg | 1_3n0b3zVSefKqG9iVqiFr2MpjQXhu-OG | https://drive.google.com/file/d/1_3n0b3zVSefKqG9iVqiFr2MpjQXhu-OG/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| C08-maharat-1060.jpg | 1hRpRqOGvBL0Qv8lh4feq1DIt45J-Ulo7 | https://drive.google.com/file/d/1hRpRqOGvBL0Qv8lh4feq1DIt45J-Ulo7/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| C08-maharat-1073.jpg | 1BQ4BzKtrfzF2lj17zvtJaAnOr4LWIzht | https://drive.google.com/file/d/1BQ4BzKtrfzF2lj17zvtJaAnOr4LWIzht/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| C08-maharat-1082.jpg | 1p9EoOxX8pmF6Q-1ZVpzqrRoXXJTmiouC | https://drive.google.com/file/d/1p9EoOxX8pmF6Q-1ZVpzqrRoXXJTmiouC/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| C08-maharat-1107.jpg | 1G5-GClHfojAPvk272kl721FXwbp4rcZ2 | https://drive.google.com/file/d/1G5-GClHfojAPvk272kl721FXwbp4rcZ2/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| C08-maharat-1117.jpg | 1Gv5ByRo0bwvXuizaekJybCBHo8VPY2OW | https://drive.google.com/file/d/1Gv5ByRo0bwvXuizaekJybCBHo8VPY2OW/view | RETOUCHED | yes | yes |  | portrait | auto, verify |

## Fetch and refresh

- No proof fetch done for this instructor (Bassam already carries the one cache demo). To fetch a preferred portrait into the gitignored cache, run `python3 .claude/scripts/drive_image_sync.py fetch elda-choucair --placement 4x5`.
- Refresh the rows: re-enumerate in an MCP session, update `scripts/cache/drive-enum-elda-choucair.json`, then run `python3 .claude/scripts/drive_image_sync.py catalog elda-choucair` and `python3 .claude/scripts/image_catalog_check.py elda-choucair`.
