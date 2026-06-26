# Cedric Haddad: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet holds this instructor's rows and the per-placement picks a designer pulls when a campaign asset needs the real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A generated or AI-edited likeness is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 07 - CEDRIC HADDAD / 02 - PHOTOGRAPHY`. Enumerated live via the Drive MCP, 2026-06-16. 5 catalogued rows, 1 preferred (one per stem group).

Enumeration note: 02 - PHOTOGRAPHY / RETOUCHED holds two subfolders only: ROMARIO (5 clean retoucher jpgs, frames 015,021,173,265,303) and FACEAPP (5 AI FaceApp-processed jpeg twins of the same 5 frames). The FaceApp variants are AI face-edited likenesses, so they are deliberately NOT catalogued: the approved-image registry is real rights-cleared photography only, and a generated or AI-edited likeness never gets a row. Only the 5 clean ROMARIO frames are catalogued. NOTE on dedup: the shared stem_key strips trailing 1-3 digit suffixes, so the five distinct ROMARIO frame numbers (015,021,173,265,303) collapse into one stem group; the gate therefore flags exactly one as preferred=yes and the other four as preferred=no superseded_by it. Those four are NOT true duplicates, they are distinct usable frames: pull any by fileId. SELECTS, HIGH RES, LOWRES siblings not enumerated; a retouching-brief deck was skipped (not an image). read_file_content returned empty this session, so faces_present and orientation are auto, verify.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read returned empty for these files this session, so faces and orientation are unverified. A human or a working vision read confirms them before a row fills an instructor-likeness slot.
- Very large tif and camera-raw originals are catalogued (or excluded where not image/*) but never fetched. Use the jpg or png preferred variant.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | Maharat-Cedric-173.jpg | 16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX | clean ROMARIO retouch portrait (the preferred winner of the collapsed stem group) |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match the true aspect at build time once the vision read or a human confirms it.

## All rows

Mirrors this instructor's section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| Maharat-Cedric-173.jpg | 16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX | https://drive.google.com/file/d/16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX/view | RETOUCHED / ROMARIO | yes | yes |  | portrait | auto, verify |
| Maharat-Cedric-015.jpg | 1iwIkl8b4hLnA8AObpAdP-aUJJUAJLkRz | https://drive.google.com/file/d/1iwIkl8b4hLnA8AObpAdP-aUJJUAJLkRz/view | RETOUCHED / ROMARIO | yes | no | 16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX | portrait | auto, verify |
| Maharat-Cedric-021.jpg | 1rUaNiLhAZ2HFjGBLCnUUymwZXuRDzM_1 | https://drive.google.com/file/d/1rUaNiLhAZ2HFjGBLCnUUymwZXuRDzM_1/view | RETOUCHED / ROMARIO | yes | no | 16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX | portrait | auto, verify |
| Maharat-Cedric-265.jpg | 1dNX7mTQtT1lQUYwKAJQlJQHEUVnSErx4 | https://drive.google.com/file/d/1dNX7mTQtT1lQUYwKAJQlJQHEUVnSErx4/view | RETOUCHED / ROMARIO | yes | no | 16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX | portrait | auto, verify |
| Maharat-Cedric-303.jpg | 13_xoJjs9_pyzza43B3AXTTFB2-wG8wCT | https://drive.google.com/file/d/13_xoJjs9_pyzza43B3AXTTFB2-wG8wCT/view | RETOUCHED / ROMARIO | yes | no | 16OxNh4JwXklNUu8DIaGb-ygOBcPUB2WX | portrait | auto, verify |

## Fetch and refresh

- No proof fetch done for this instructor (Bassam already carries the one cache demo). To fetch a preferred portrait into the gitignored cache, run `python3 .claude/scripts/drive_image_sync.py fetch cedric-haddad --placement 4x5`.
- Refresh the rows: re-enumerate in an MCP session, update `scripts/cache/drive-enum-cedric-haddad.json`, then run `python3 .claude/scripts/drive_image_sync.py catalog cedric-haddad` and `python3 .claude/scripts/image_catalog_check.py cedric-haddad`.
