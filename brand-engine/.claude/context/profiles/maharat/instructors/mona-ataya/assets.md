# Mona Ataya: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet holds this instructor's rows and the per-placement picks a designer pulls when a campaign asset needs the real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A generated or AI-edited likeness is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 09 - MONA ATAYA / 02 - PHOTOGRAPHY`. Enumerated live via the Drive MCP, 2026-06-16. 202 catalogued rows, 195 preferred (one per stem group).

Enumeration note: 09 - PHOTOGRAPHY has NO RETOUCHED folder. HIGHRES holds CR3 camera-raw files (mimeType application/octet-stream, not image/*, and not web-usable), so they are NOT catalogued. The catalogable images are the 195 LOWRES jpgs (retouched=no, the lower-res selects export). LOWRES / AYA SELECTS holds 7 jpgs that duplicate LOWRES stems; the LOWRES copy wins each stem group, the AYA SELECTS copy is the superseded twin. read_file_content returned empty this session, so faces_present and orientation are auto, verify. Mona is the only class with no retouched set: flag for Ahmed that her hero pick comes from LOWRES until a retouched export exists.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read returned empty for these files this session, so faces and orientation are unverified. A human or a working vision read confirms them before a row fills an instructor-likeness slot.
- Very large tif and camera-raw originals are catalogued (or excluded where not image/*) but never fetched. Use the jpg or png preferred variant.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | maharat-1850.JPG | 1FHXhDd2SBalhFgR3gkFCRz4V287X_mHQ | LOWRES select (Mona has NO retouched set: hero comes from LOWRES, flag for Ahmed) |
| Portrait general | 4:5 | maharat-1849.JPG | 1_nBXBQxesxf8Iec0Jkvdgh-LIXD8o0vH | preferred portrait candidate, pull by fileId |
| Portrait alternate | 4:5 | maharat-1851.JPG | 1xlgsCm_Xi2RCs2rb4kpJHPYI4lJ_cfFp | preferred portrait candidate, pull by fileId |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match the true aspect at build time once the vision read or a human confirms it.

## All rows

Mirrors this instructor's section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| maharat-1849.JPG | 1_nBXBQxesxf8Iec0Jkvdgh-LIXD8o0vH | https://drive.google.com/file/d/1_nBXBQxesxf8Iec0Jkvdgh-LIXD8o0vH/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1850.JPG | 1FHXhDd2SBalhFgR3gkFCRz4V287X_mHQ | https://drive.google.com/file/d/1FHXhDd2SBalhFgR3gkFCRz4V287X_mHQ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1851.JPG | 1xlgsCm_Xi2RCs2rb4kpJHPYI4lJ_cfFp | https://drive.google.com/file/d/1xlgsCm_Xi2RCs2rb4kpJHPYI4lJ_cfFp/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1852.JPG | 1WNVQrdFxjTw4l0ZYgxso126CYb0teQfR | https://drive.google.com/file/d/1WNVQrdFxjTw4l0ZYgxso126CYb0teQfR/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1853.JPG | 1yddxvcUoqKVO8SEQmUZvEjypn2h4Bsn7 | https://drive.google.com/file/d/1yddxvcUoqKVO8SEQmUZvEjypn2h4Bsn7/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1854.JPG | 13K2bX7UxBZntukTcUTfkzs--c90bRkTo | https://drive.google.com/file/d/13K2bX7UxBZntukTcUTfkzs--c90bRkTo/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1855.JPG | 17jTqJikZUlV7dpc4isg7R4VjO51IhV5m | https://drive.google.com/file/d/17jTqJikZUlV7dpc4isg7R4VjO51IhV5m/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1856.JPG | 1eA5DjtNU_qLW3lZdNBmwevo0wIozRx4K | https://drive.google.com/file/d/1eA5DjtNU_qLW3lZdNBmwevo0wIozRx4K/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1857.JPG | 1-rNLRO7Dia_HJl-lGuZRHUoC6mAQV-Vh | https://drive.google.com/file/d/1-rNLRO7Dia_HJl-lGuZRHUoC6mAQV-Vh/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1858.JPG | 1xnCMFa1QlIQQr77-M3QwAOPhe6YtTwb4 | https://drive.google.com/file/d/1xnCMFa1QlIQQr77-M3QwAOPhe6YtTwb4/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1859.JPG | 10M6itib1YfT0CqcClaC2P_34DDn0oWRN | https://drive.google.com/file/d/10M6itib1YfT0CqcClaC2P_34DDn0oWRN/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1860.JPG | 1iu0hsKilTEhEWYVjKmxOr2qGDcv4K9ro | https://drive.google.com/file/d/1iu0hsKilTEhEWYVjKmxOr2qGDcv4K9ro/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1861.JPG | 1p5gNxv9Adtdb94OnojrByM8soAsxhc6E | https://drive.google.com/file/d/1p5gNxv9Adtdb94OnojrByM8soAsxhc6E/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1862.JPG | 1zJUN7Qax7ejwge9K2QxqgNQ09j6xCLSh | https://drive.google.com/file/d/1zJUN7Qax7ejwge9K2QxqgNQ09j6xCLSh/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1863.JPG | 1BZdhyD1oH-Y2jYSvXuDI4d9cms7hY75N | https://drive.google.com/file/d/1BZdhyD1oH-Y2jYSvXuDI4d9cms7hY75N/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1864.JPG | 1ucbkBQ0XWCr7Ahvx11ZCBT6T7kX2BCjJ | https://drive.google.com/file/d/1ucbkBQ0XWCr7Ahvx11ZCBT6T7kX2BCjJ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1865.JPG | 10b426yJSk3gtBLPAQ5tN88OQ_oqGv_PR | https://drive.google.com/file/d/10b426yJSk3gtBLPAQ5tN88OQ_oqGv_PR/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1866.JPG | 1C-XexaAEJTwRmoboOxhecpLLtnBOjSLA | https://drive.google.com/file/d/1C-XexaAEJTwRmoboOxhecpLLtnBOjSLA/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1867.JPG | 1oYw5Ki2S_VZ60vTBHlzTQlbviwd-ybBE | https://drive.google.com/file/d/1oYw5Ki2S_VZ60vTBHlzTQlbviwd-ybBE/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1868.JPG | 1mvC_WuIMM6tQi9feHCYNhAlfKiycpGws | https://drive.google.com/file/d/1mvC_WuIMM6tQi9feHCYNhAlfKiycpGws/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1869.JPG | 1CkwlFu3ifcuXSIBdQiu48GvI1Hyb2dpz | https://drive.google.com/file/d/1CkwlFu3ifcuXSIBdQiu48GvI1Hyb2dpz/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1870.JPG | 1QSW10Vljby5jJWmUVmlFKlRLSt6uC2Ii | https://drive.google.com/file/d/1QSW10Vljby5jJWmUVmlFKlRLSt6uC2Ii/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1871.JPG | 1TfsXw5_tSFKfp_lZQtiKOqSeVHrXxhz2 | https://drive.google.com/file/d/1TfsXw5_tSFKfp_lZQtiKOqSeVHrXxhz2/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1872.JPG | 1xjX8diUZ9HfkweqgAAds5JY8hG6qbUpG | https://drive.google.com/file/d/1xjX8diUZ9HfkweqgAAds5JY8hG6qbUpG/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1873.JPG | 1L6ULgBat6YEh38Tt52oxxmy1-BmRGUJ0 | https://drive.google.com/file/d/1L6ULgBat6YEh38Tt52oxxmy1-BmRGUJ0/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1874.JPG | 1024WHqIYb1OEamS_0B8Lyr-x8wRqGnPp | https://drive.google.com/file/d/1024WHqIYb1OEamS_0B8Lyr-x8wRqGnPp/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1875.JPG | 1VgN_iZuH1CVaj73SFFmirjXODYJ_aoWr | https://drive.google.com/file/d/1VgN_iZuH1CVaj73SFFmirjXODYJ_aoWr/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1876.JPG | 1tYermugi92fmXuPQ1gXNd2tC7O-8Pegz | https://drive.google.com/file/d/1tYermugi92fmXuPQ1gXNd2tC7O-8Pegz/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1877.JPG | 1RogmqqufzBdf3XEOWR3p8raO0EobQfu7 | https://drive.google.com/file/d/1RogmqqufzBdf3XEOWR3p8raO0EobQfu7/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1878.JPG | 11onhCVZJJ2h4P4HpxHzlGKQ85DUGnj4_ | https://drive.google.com/file/d/11onhCVZJJ2h4P4HpxHzlGKQ85DUGnj4_/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1879.JPG | 14vkk7BBzSTcCu9qJc_bBCAL7e1tXg8t6 | https://drive.google.com/file/d/14vkk7BBzSTcCu9qJc_bBCAL7e1tXg8t6/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1880.JPG | 1g5JopIGmYtATsuraNkxa1MfnwKNN_om8 | https://drive.google.com/file/d/1g5JopIGmYtATsuraNkxa1MfnwKNN_om8/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1881.JPG | 1JfcVwIQ9Jo2_L1jB8Bt0fDKM8J-S2iTI | https://drive.google.com/file/d/1JfcVwIQ9Jo2_L1jB8Bt0fDKM8J-S2iTI/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1882.JPG | 1l7_opljjIRNYbI1bmWFJo-ZjdJ4YGu1Z | https://drive.google.com/file/d/1l7_opljjIRNYbI1bmWFJo-ZjdJ4YGu1Z/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1883.JPG | 1z1k8uC5FJFJSFhPt6WVXkPc3uQaSOuG5 | https://drive.google.com/file/d/1z1k8uC5FJFJSFhPt6WVXkPc3uQaSOuG5/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1884.JPG | 1J-hKmoiG2YhYj_T-4UPzgTLBxLvjBcFR | https://drive.google.com/file/d/1J-hKmoiG2YhYj_T-4UPzgTLBxLvjBcFR/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1885.JPG | 16n6CYzOAfVc4MWJl0yR7sGgBwAUxwUyu | https://drive.google.com/file/d/16n6CYzOAfVc4MWJl0yR7sGgBwAUxwUyu/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1886.JPG | 1PvOXCksD6sCNP5dEBjRLCSophZbr9_eS | https://drive.google.com/file/d/1PvOXCksD6sCNP5dEBjRLCSophZbr9_eS/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1887.JPG | 1Ht9uOvMiKKl0bR2N3cOlp4UedK8TWyLQ | https://drive.google.com/file/d/1Ht9uOvMiKKl0bR2N3cOlp4UedK8TWyLQ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1888.JPG | 1WRH0B4teI8oPY49zYaZrGVRYbyaK7Jyf | https://drive.google.com/file/d/1WRH0B4teI8oPY49zYaZrGVRYbyaK7Jyf/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1889.JPG | 1YVA7acZRwcaJ8hSExEz7kQB0_ktBuNpR | https://drive.google.com/file/d/1YVA7acZRwcaJ8hSExEz7kQB0_ktBuNpR/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1890.JPG | 1uLnnNcVFr-F2m71eMuklfqSWAflUpW9j | https://drive.google.com/file/d/1uLnnNcVFr-F2m71eMuklfqSWAflUpW9j/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1891.JPG | 1unrMP8kKbd22lbyJOHQI2yAAblWskx63 | https://drive.google.com/file/d/1unrMP8kKbd22lbyJOHQI2yAAblWskx63/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1892.JPG | 1AWQf0gSqzRqpomU-sG3_de_U0LlqhGXo | https://drive.google.com/file/d/1AWQf0gSqzRqpomU-sG3_de_U0LlqhGXo/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1893.JPG | 1mGZv6O9NFq-IbS6FvPT5ks0qsRIo7wQ0 | https://drive.google.com/file/d/1mGZv6O9NFq-IbS6FvPT5ks0qsRIo7wQ0/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1894.JPG | 12ZQLKjbgY2Kj3NFiAJl5Y7cU9AH9NuKC | https://drive.google.com/file/d/12ZQLKjbgY2Kj3NFiAJl5Y7cU9AH9NuKC/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1895.JPG | 1QLOAhttAcVrV8BKPWugxMNIBhzYPK8hT | https://drive.google.com/file/d/1QLOAhttAcVrV8BKPWugxMNIBhzYPK8hT/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1896.JPG | 1nHjjdhL64L75LNOuYglLlYl2vvvCvkH2 | https://drive.google.com/file/d/1nHjjdhL64L75LNOuYglLlYl2vvvCvkH2/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1897.JPG | 1DCOeg2rRsJJBMZ6iIaEWyg7MDR0HAMAB | https://drive.google.com/file/d/1DCOeg2rRsJJBMZ6iIaEWyg7MDR0HAMAB/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1898.JPG | 1o3mgKsEDPa2esFYTnkj5bGD4oEruzcDf | https://drive.google.com/file/d/1o3mgKsEDPa2esFYTnkj5bGD4oEruzcDf/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1899.JPG | 1kMlB1pKMGFoVyoHpCVnmM4s9LXRqxRxt | https://drive.google.com/file/d/1kMlB1pKMGFoVyoHpCVnmM4s9LXRqxRxt/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1900.JPG | 166zyqcJ0CNRpGyxYq_afkS2B5hwOEEPU | https://drive.google.com/file/d/166zyqcJ0CNRpGyxYq_afkS2B5hwOEEPU/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1901.JPG | 1wTr8PXDZl-IfXVAURa1n4du1OcqeEoRT | https://drive.google.com/file/d/1wTr8PXDZl-IfXVAURa1n4du1OcqeEoRT/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1902.JPG | 1YJ2Uci5ZgDYu2KLRoiZ_mI5KqZkemOD9 | https://drive.google.com/file/d/1YJ2Uci5ZgDYu2KLRoiZ_mI5KqZkemOD9/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1903.JPG | 1XeONol3p-E-YH5s5g2ViSXcht6UuWFNw | https://drive.google.com/file/d/1XeONol3p-E-YH5s5g2ViSXcht6UuWFNw/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1904.JPG | 12pcaSqXh8V8P9uMAygTrwHWqZKmxK6RY | https://drive.google.com/file/d/12pcaSqXh8V8P9uMAygTrwHWqZKmxK6RY/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1905.JPG | 1ceyCNqKoZVHOoNhlWcsw3Pg2ULen8Dxm | https://drive.google.com/file/d/1ceyCNqKoZVHOoNhlWcsw3Pg2ULen8Dxm/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1906.JPG | 1fiHLzfXM25f0GL2CmEwzU2ePkZyoAcZK | https://drive.google.com/file/d/1fiHLzfXM25f0GL2CmEwzU2ePkZyoAcZK/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1907.JPG | 1-twjl1hfCWO56APXxvMdpzunAT9A9ZeT | https://drive.google.com/file/d/1-twjl1hfCWO56APXxvMdpzunAT9A9ZeT/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1908.JPG | 1GKP1_5PJ_i9kBV5tQCpGY9Sb1eFDGj8q | https://drive.google.com/file/d/1GKP1_5PJ_i9kBV5tQCpGY9Sb1eFDGj8q/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1909.JPG | 19Pfu1aikqy_8UWruhrTXJImLALuU3fAM | https://drive.google.com/file/d/19Pfu1aikqy_8UWruhrTXJImLALuU3fAM/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1910.JPG | 12kBijmgEJSKZuEVV5VD2zATj-rPSwABY | https://drive.google.com/file/d/12kBijmgEJSKZuEVV5VD2zATj-rPSwABY/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1911.JPG | 1gE7wVQkOXB424VNA3fHcwK8QCCrlRCaN | https://drive.google.com/file/d/1gE7wVQkOXB424VNA3fHcwK8QCCrlRCaN/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1912.JPG | 1f5DwhFYA40FhqjOm5-42_4NUGdJMv3h_ | https://drive.google.com/file/d/1f5DwhFYA40FhqjOm5-42_4NUGdJMv3h_/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1913.JPG | 1aXRe9ZArqcK6Z8TVODqSvDA2voZ3706c | https://drive.google.com/file/d/1aXRe9ZArqcK6Z8TVODqSvDA2voZ3706c/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1914.JPG | 1LTF1iok3yjAQnC1eHHx2iXd8u0-PVtuh | https://drive.google.com/file/d/1LTF1iok3yjAQnC1eHHx2iXd8u0-PVtuh/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1915.JPG | 1jpEeAqGDWeMfbntbC0b1jPgaeGncp4zW | https://drive.google.com/file/d/1jpEeAqGDWeMfbntbC0b1jPgaeGncp4zW/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1916.JPG | 1sQin4gchnAvlwW8HgAV_DOXveseS_iTH | https://drive.google.com/file/d/1sQin4gchnAvlwW8HgAV_DOXveseS_iTH/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1917.JPG | 1bqlZj17q-5CxterBEmVYWK3fsUXKQRAW | https://drive.google.com/file/d/1bqlZj17q-5CxterBEmVYWK3fsUXKQRAW/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1918.JPG | 1HJUL9avoX_GrsRAjov5t2Dhv5Pc-yLav | https://drive.google.com/file/d/1HJUL9avoX_GrsRAjov5t2Dhv5Pc-yLav/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1919.JPG | 1DHv_MuVPGmQLgwbshZ22Y4Rh0Rlmvgbh | https://drive.google.com/file/d/1DHv_MuVPGmQLgwbshZ22Y4Rh0Rlmvgbh/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1920.JPG | 1a6lTKJZokuKh4DN2JLf6D46RSDeUOK4G | https://drive.google.com/file/d/1a6lTKJZokuKh4DN2JLf6D46RSDeUOK4G/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1921.JPG | 1gnhdBCkkThOyHK_ETu-9vFtZ4D7jGcEx | https://drive.google.com/file/d/1gnhdBCkkThOyHK_ETu-9vFtZ4D7jGcEx/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1922.JPG | 1QTlXR9X2cmoIJiw6OOk3f9ZQRHjyfl4X | https://drive.google.com/file/d/1QTlXR9X2cmoIJiw6OOk3f9ZQRHjyfl4X/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1923.JPG | 1_eGnKLyQzQdqabJiCVH4XuG-8HYtVZc6 | https://drive.google.com/file/d/1_eGnKLyQzQdqabJiCVH4XuG-8HYtVZc6/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1924.JPG | 1fUUBUKjs-6v4k3lgXy7ECF5Kokq8rmlw | https://drive.google.com/file/d/1fUUBUKjs-6v4k3lgXy7ECF5Kokq8rmlw/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1925.JPG | 1WmicbJfA6DGC11luktK1iucljkdhpIQ8 | https://drive.google.com/file/d/1WmicbJfA6DGC11luktK1iucljkdhpIQ8/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1926.JPG | 1boqchTh_HMy17LGG80PGhp0hq9kZ97Wg | https://drive.google.com/file/d/1boqchTh_HMy17LGG80PGhp0hq9kZ97Wg/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1927.JPG | 1Ohb4nU22YtDSD83Cxi8gkWW2X0HIEKsU | https://drive.google.com/file/d/1Ohb4nU22YtDSD83Cxi8gkWW2X0HIEKsU/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1928.JPG | 1JXozSzDsNPfhzyBwdT6B59hMvj3iJ8TF | https://drive.google.com/file/d/1JXozSzDsNPfhzyBwdT6B59hMvj3iJ8TF/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1929.JPG | 1wbJwWt7dLxvOdNAVqfTXPuQRlF2xWUvY | https://drive.google.com/file/d/1wbJwWt7dLxvOdNAVqfTXPuQRlF2xWUvY/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1930.JPG | 1f9K_1KmeqjA9xFp2dNZZ_-RhfnGiidDV | https://drive.google.com/file/d/1f9K_1KmeqjA9xFp2dNZZ_-RhfnGiidDV/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1931.JPG | 1oeZIlbzuG2lwl-qrqH6-jRINEQQkfpGD | https://drive.google.com/file/d/1oeZIlbzuG2lwl-qrqH6-jRINEQQkfpGD/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1932.JPG | 1LHhaJfEdKVsFDyYBb7Wy76ZE_5QTjZts | https://drive.google.com/file/d/1LHhaJfEdKVsFDyYBb7Wy76ZE_5QTjZts/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1933.JPG | 1BXX51DypgEoEPJfNJ5pyx774asRkoDn4 | https://drive.google.com/file/d/1BXX51DypgEoEPJfNJ5pyx774asRkoDn4/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1934.JPG | 17GhaDDY4qio6n14rIxPOBVsAqEfi7-IU | https://drive.google.com/file/d/17GhaDDY4qio6n14rIxPOBVsAqEfi7-IU/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1935.JPG | 1G8sLxZwWSMz4tKizG48JxvIRja38jdd_ | https://drive.google.com/file/d/1G8sLxZwWSMz4tKizG48JxvIRja38jdd_/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1936.JPG | 1W1YbRtG73jWhcDBDLfnvQHl4Ya9pXHJY | https://drive.google.com/file/d/1W1YbRtG73jWhcDBDLfnvQHl4Ya9pXHJY/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1937.JPG | 1ngSO8ty5t5dUEs36lgAXCr-aQlpVATo3 | https://drive.google.com/file/d/1ngSO8ty5t5dUEs36lgAXCr-aQlpVATo3/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1938.JPG | 1ns38rqDU1Zuw6NHUM2d6rBw7Ny6cEjk4 | https://drive.google.com/file/d/1ns38rqDU1Zuw6NHUM2d6rBw7Ny6cEjk4/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1939.JPG | 1LQKzLcob7zmo0c3ktV9FCHifZ-mZ9-W4 | https://drive.google.com/file/d/1LQKzLcob7zmo0c3ktV9FCHifZ-mZ9-W4/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1940.JPG | 1CeLNbDeZxh6MXaTsKbQUd1zRCeLHtWXo | https://drive.google.com/file/d/1CeLNbDeZxh6MXaTsKbQUd1zRCeLHtWXo/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1941.JPG | 1F2xfVkImDkkxL1neycBowEMCt1uYRLzy | https://drive.google.com/file/d/1F2xfVkImDkkxL1neycBowEMCt1uYRLzy/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1942.JPG | 1yuv0NXAC5ltHiVHK4FpoiXFL34ghEjV5 | https://drive.google.com/file/d/1yuv0NXAC5ltHiVHK4FpoiXFL34ghEjV5/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1943.JPG | 1Z5iStMQLr9Vix-17Esvj-gzfun1ymuH7 | https://drive.google.com/file/d/1Z5iStMQLr9Vix-17Esvj-gzfun1ymuH7/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1944.JPG | 1-Zt0RQp-uoJeYAelU9izughX9i6gmpLR | https://drive.google.com/file/d/1-Zt0RQp-uoJeYAelU9izughX9i6gmpLR/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1945.JPG | 1MmPk7AhVp7vHZ5ASlzzmt9zEy8V3V5om | https://drive.google.com/file/d/1MmPk7AhVp7vHZ5ASlzzmt9zEy8V3V5om/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1946.JPG | 1uMhCE8h84miU7cDTDUk4zuWsdxHmfpXy | https://drive.google.com/file/d/1uMhCE8h84miU7cDTDUk4zuWsdxHmfpXy/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1947.JPG | 1UTlXN80m2xe-DvDNyv8Sl7XARC70ojQT | https://drive.google.com/file/d/1UTlXN80m2xe-DvDNyv8Sl7XARC70ojQT/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1948.JPG | 1cZ5r-MGky0eopF9m4DraBap1XjhHC8QG | https://drive.google.com/file/d/1cZ5r-MGky0eopF9m4DraBap1XjhHC8QG/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1949.JPG | 1bQj4soPVSpLN34HCi8LO_kU0H1KcNSpW | https://drive.google.com/file/d/1bQj4soPVSpLN34HCi8LO_kU0H1KcNSpW/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1950.JPG | 11Vcl88UZbUHgafn2OX8n8VJI9F-2IWod | https://drive.google.com/file/d/11Vcl88UZbUHgafn2OX8n8VJI9F-2IWod/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1951.JPG | 1w6FHY-uCAxpLhg28HUPXXi-FRUErb-D5 | https://drive.google.com/file/d/1w6FHY-uCAxpLhg28HUPXXi-FRUErb-D5/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1952.JPG | 1n-zkK7vj37qCncn4lxYwdV_GnyyinvZ5 | https://drive.google.com/file/d/1n-zkK7vj37qCncn4lxYwdV_GnyyinvZ5/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1953.JPG | 1GeOYbnh33MJ5eY5IFki48GKcWHW-cW3u | https://drive.google.com/file/d/1GeOYbnh33MJ5eY5IFki48GKcWHW-cW3u/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1954.JPG | 1HRt6TC-hrMcaMG5A3A8_e3lK89BNUohJ | https://drive.google.com/file/d/1HRt6TC-hrMcaMG5A3A8_e3lK89BNUohJ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1955.JPG | 1woX_B7DpgxEudjE3fO_CrVgXl1z_rw0r | https://drive.google.com/file/d/1woX_B7DpgxEudjE3fO_CrVgXl1z_rw0r/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1956.JPG | 1gO1yQw92TpyrGdWZXY657y_Ns3U7wNoj | https://drive.google.com/file/d/1gO1yQw92TpyrGdWZXY657y_Ns3U7wNoj/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1957.JPG | 1GH_sX9dz4esLcCqLnND8gA3xTD72InuF | https://drive.google.com/file/d/1GH_sX9dz4esLcCqLnND8gA3xTD72InuF/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1958.JPG | 1GJNlpusBSQC96cQc2HewFy0wbsIqx-a4 | https://drive.google.com/file/d/1GJNlpusBSQC96cQc2HewFy0wbsIqx-a4/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1959.JPG | 1QGhsNVo_piq-Yv_of-hVGHTIN0T0LIyU | https://drive.google.com/file/d/1QGhsNVo_piq-Yv_of-hVGHTIN0T0LIyU/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1960.JPG | 1RDGasCn-OaT-jCen2u9oLG7UFcjBq0NN | https://drive.google.com/file/d/1RDGasCn-OaT-jCen2u9oLG7UFcjBq0NN/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1961.JPG | 12h3Eh-tIfU7psq4o0gQq9Bv63DZcrsTF | https://drive.google.com/file/d/12h3Eh-tIfU7psq4o0gQq9Bv63DZcrsTF/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1962.JPG | 1F2kmHUJPb2nI_FwP8MC4MsvUlkrIbg7w | https://drive.google.com/file/d/1F2kmHUJPb2nI_FwP8MC4MsvUlkrIbg7w/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1963.JPG | 1wM7fknDAowpr9ggjRGyjxhTL5UaA4neD | https://drive.google.com/file/d/1wM7fknDAowpr9ggjRGyjxhTL5UaA4neD/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1964.JPG | 1kcFy57uU3Y2ZB8xpN2g1t1hgo3fqSwAv | https://drive.google.com/file/d/1kcFy57uU3Y2ZB8xpN2g1t1hgo3fqSwAv/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1965.JPG | 1EZdoxtr6Xv77UMWsrBYPln3xP5hDphr7 | https://drive.google.com/file/d/1EZdoxtr6Xv77UMWsrBYPln3xP5hDphr7/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1966.JPG | 1Bodvm-w35FYZvkodS0PpGDOut3e2DWMU | https://drive.google.com/file/d/1Bodvm-w35FYZvkodS0PpGDOut3e2DWMU/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1967.JPG | 18B4tNeFNzBVzGk2PMhejSw53KQi9C2vC | https://drive.google.com/file/d/18B4tNeFNzBVzGk2PMhejSw53KQi9C2vC/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1968.JPG | 109U9nVls9_c8ZfVijskPY9djEDlycZyY | https://drive.google.com/file/d/109U9nVls9_c8ZfVijskPY9djEDlycZyY/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1969.JPG | 1cziS9hk8IzMHh-sZhBVcCdN3Z28pVHIO | https://drive.google.com/file/d/1cziS9hk8IzMHh-sZhBVcCdN3Z28pVHIO/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1970.JPG | 1jfheIceJGID2US8OVTJUI15z6lRCQTOD | https://drive.google.com/file/d/1jfheIceJGID2US8OVTJUI15z6lRCQTOD/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1971.JPG | 1u6imPXhaxDfe7iz3kHCY1MmQbgbFIQJc | https://drive.google.com/file/d/1u6imPXhaxDfe7iz3kHCY1MmQbgbFIQJc/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1972.JPG | 1UWuOULwBDcmMHoED11K01Ki_3iCGtv01 | https://drive.google.com/file/d/1UWuOULwBDcmMHoED11K01Ki_3iCGtv01/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1973.JPG | 1Xq1-LjN3G3mdT5ppzVGvqP0sEPQolw_m | https://drive.google.com/file/d/1Xq1-LjN3G3mdT5ppzVGvqP0sEPQolw_m/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1974.JPG | 1ZQpqDa3G512gV2wqmeIt180G9R5fbfkn | https://drive.google.com/file/d/1ZQpqDa3G512gV2wqmeIt180G9R5fbfkn/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1975.JPG | 1Uy7vW7FhHbqoVro_6jiD14YtK-uMHbpF | https://drive.google.com/file/d/1Uy7vW7FhHbqoVro_6jiD14YtK-uMHbpF/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1976.JPG | 1TcJD_EsCMTg4ina2w5-U6t5YLTHF8gKA | https://drive.google.com/file/d/1TcJD_EsCMTg4ina2w5-U6t5YLTHF8gKA/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1977.JPG | 1xSpA3S0rOTWGf_5t1DJxDjefR7MfDder | https://drive.google.com/file/d/1xSpA3S0rOTWGf_5t1DJxDjefR7MfDder/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1978.JPG | 1P9ONZaPGKQjmmoYCroNBgwM0Y74zfYIo | https://drive.google.com/file/d/1P9ONZaPGKQjmmoYCroNBgwM0Y74zfYIo/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1979.JPG | 1xCBnAxH-xB2EEnMhO7c8maSDOxRvpFoA | https://drive.google.com/file/d/1xCBnAxH-xB2EEnMhO7c8maSDOxRvpFoA/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1980.JPG | 1yik8algB77WU0i7LAfH4fqLfRkBI2Zna | https://drive.google.com/file/d/1yik8algB77WU0i7LAfH4fqLfRkBI2Zna/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1981.JPG | 1w_H4B38YXnN_9E1CxUKQIuZAILdx0tKt | https://drive.google.com/file/d/1w_H4B38YXnN_9E1CxUKQIuZAILdx0tKt/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1982.JPG | 1Lmp4JP4pjzDg1uumba3FAVj9Pf9R_F9r | https://drive.google.com/file/d/1Lmp4JP4pjzDg1uumba3FAVj9Pf9R_F9r/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1983.JPG | 1rULXXAlWOjSTaayUz-TOxe0xGlmAZ0Iz | https://drive.google.com/file/d/1rULXXAlWOjSTaayUz-TOxe0xGlmAZ0Iz/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1984.JPG | 1b1Ox91cdi-l3YL4zjEZYA-ikw-AVD4hf | https://drive.google.com/file/d/1b1Ox91cdi-l3YL4zjEZYA-ikw-AVD4hf/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1985.JPG | 1O28YmlgWG4t0bXoex36z6J8syMGugntF | https://drive.google.com/file/d/1O28YmlgWG4t0bXoex36z6J8syMGugntF/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1986.JPG | 1LKUWsLKLXUrC8ryFKmVadGiCPoVDbUj2 | https://drive.google.com/file/d/1LKUWsLKLXUrC8ryFKmVadGiCPoVDbUj2/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1987.JPG | 1eX2TMxCnQvzgH_g7BQkH8e0VLQyLtlsv | https://drive.google.com/file/d/1eX2TMxCnQvzgH_g7BQkH8e0VLQyLtlsv/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1988.JPG | 1IMRoFHHkVFd4yBWH_k1thOebIbcDueUg | https://drive.google.com/file/d/1IMRoFHHkVFd4yBWH_k1thOebIbcDueUg/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1989.JPG | 1hkp181vAROMe7p1aKECojuKq3WJk24mM | https://drive.google.com/file/d/1hkp181vAROMe7p1aKECojuKq3WJk24mM/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1990.JPG | 1hRZibpyLeRUvgAorCbA5vFlBNIqWLB0U | https://drive.google.com/file/d/1hRZibpyLeRUvgAorCbA5vFlBNIqWLB0U/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1991.JPG | 1i5-zzGVMv5l_zaxWgeXoQuMKMvfQo-td | https://drive.google.com/file/d/1i5-zzGVMv5l_zaxWgeXoQuMKMvfQo-td/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1992.JPG | 1R_w-aQB7GQu6BNCdxY1bueOsdC5ms8oj | https://drive.google.com/file/d/1R_w-aQB7GQu6BNCdxY1bueOsdC5ms8oj/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1993.JPG | 14FqS2zqk2Sbf5Qz_FnbYsHtjS9LheRFZ | https://drive.google.com/file/d/14FqS2zqk2Sbf5Qz_FnbYsHtjS9LheRFZ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1994.JPG | 1_CCXzEdA7W3u-ndk_JMf60h2WtQHF7d3 | https://drive.google.com/file/d/1_CCXzEdA7W3u-ndk_JMf60h2WtQHF7d3/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1995.JPG | 1FfhYmqxkf0TzZoEEhuya43_AMe2FXPXl | https://drive.google.com/file/d/1FfhYmqxkf0TzZoEEhuya43_AMe2FXPXl/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1996.JPG | 145dfaJxxwotqTAskdlALU64se5awxqkG | https://drive.google.com/file/d/145dfaJxxwotqTAskdlALU64se5awxqkG/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1997.JPG | 1iCTXEpFDet1rezxLn367MEMxvKLvt8Rh | https://drive.google.com/file/d/1iCTXEpFDet1rezxLn367MEMxvKLvt8Rh/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1998.JPG | 1khjSdMrhyOTwpbskkwLn1nisw8HdGpG_ | https://drive.google.com/file/d/1khjSdMrhyOTwpbskkwLn1nisw8HdGpG_/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1999.JPG | 1RunHoYIpUyYgw2IM9iJ3vEEhPr_JzDtd | https://drive.google.com/file/d/1RunHoYIpUyYgw2IM9iJ3vEEhPr_JzDtd/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2000.JPG | 1W4KbLBQya4H58uQAhxLEoVcHGwDgoIea | https://drive.google.com/file/d/1W4KbLBQya4H58uQAhxLEoVcHGwDgoIea/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2001.JPG | 1c1szdCtbBX7w4pI8Zr6m-GH0b3ppogzr | https://drive.google.com/file/d/1c1szdCtbBX7w4pI8Zr6m-GH0b3ppogzr/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2002.JPG | 1DvS57uyF_Cz667XY1mkX7TclCe8mcfkm | https://drive.google.com/file/d/1DvS57uyF_Cz667XY1mkX7TclCe8mcfkm/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2003.JPG | 1o58ME6d2NbVZpqSVGMFm755GTDpHCCLA | https://drive.google.com/file/d/1o58ME6d2NbVZpqSVGMFm755GTDpHCCLA/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2004.JPG | 1tsr46Bno12CSkAabENDpn3LfKPASgt-e | https://drive.google.com/file/d/1tsr46Bno12CSkAabENDpn3LfKPASgt-e/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2005.JPG | 1MgFAsnD--7TgCdKihB8g2kVaOXr3o2oY | https://drive.google.com/file/d/1MgFAsnD--7TgCdKihB8g2kVaOXr3o2oY/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2006.JPG | 1tQiRG0F6PzooCUjs-9ORIlJsvj-8fSnJ | https://drive.google.com/file/d/1tQiRG0F6PzooCUjs-9ORIlJsvj-8fSnJ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2007.JPG | 1XbqHvqVR0rTpzL9_TsD20AWTbe3jRD9r | https://drive.google.com/file/d/1XbqHvqVR0rTpzL9_TsD20AWTbe3jRD9r/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2008.JPG | 1f2ATCKhtg4sHXf5eTSrEndZQOwfOvz6J | https://drive.google.com/file/d/1f2ATCKhtg4sHXf5eTSrEndZQOwfOvz6J/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2009.JPG | 15-aCZAgUPqO6jX0zbpXtWF6KQCichZcT | https://drive.google.com/file/d/15-aCZAgUPqO6jX0zbpXtWF6KQCichZcT/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2010.JPG | 1LLKsEM4waMn4tqUMEMgqx7l6Ve9TgeWL | https://drive.google.com/file/d/1LLKsEM4waMn4tqUMEMgqx7l6Ve9TgeWL/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2011.JPG | 1-_8uOdGO1q6ZZuXRoV597IcZFBh2iJ6P | https://drive.google.com/file/d/1-_8uOdGO1q6ZZuXRoV597IcZFBh2iJ6P/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2012.JPG | 1Ie4ldGWxuiqMaWaXGk4mLB8z4OHG9UaW | https://drive.google.com/file/d/1Ie4ldGWxuiqMaWaXGk4mLB8z4OHG9UaW/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2013.JPG | 1kTPyYAaYrdnCZxO98BfS0Jlf_jLr8rJg | https://drive.google.com/file/d/1kTPyYAaYrdnCZxO98BfS0Jlf_jLr8rJg/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2014.JPG | 1HP2VBkTcOPY0LRCX99AqaJBE6QbzUwdZ | https://drive.google.com/file/d/1HP2VBkTcOPY0LRCX99AqaJBE6QbzUwdZ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2015.JPG | 1fQdY0YUn-_hES26UzhulmrQV3-xx1BDs | https://drive.google.com/file/d/1fQdY0YUn-_hES26UzhulmrQV3-xx1BDs/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2016.JPG | 1qvQpicrbZbvN3CLNrqHhbtXm6czH-YAQ | https://drive.google.com/file/d/1qvQpicrbZbvN3CLNrqHhbtXm6czH-YAQ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2017.JPG | 1nVaOTKaFA-vBdI6h0okq0KoRPVvlJFk5 | https://drive.google.com/file/d/1nVaOTKaFA-vBdI6h0okq0KoRPVvlJFk5/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2018.JPG | 1RXrpeGcgXjwg28oRbBEAtzUyf-aI4t8x | https://drive.google.com/file/d/1RXrpeGcgXjwg28oRbBEAtzUyf-aI4t8x/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2019.JPG | 1uUWAHTnnd3QPrsNXW9_PuKzOMGJ7G1X7 | https://drive.google.com/file/d/1uUWAHTnnd3QPrsNXW9_PuKzOMGJ7G1X7/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2020.JPG | 1VfqwWCVXQ_ddOb8y3_H9sYhK8GeD_o_L | https://drive.google.com/file/d/1VfqwWCVXQ_ddOb8y3_H9sYhK8GeD_o_L/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2021.JPG | 1fwAK9nY7M7fCLKCO0BuF25WvdxVdLknb | https://drive.google.com/file/d/1fwAK9nY7M7fCLKCO0BuF25WvdxVdLknb/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2022.JPG | 1CV1bCwfSbTvH9cyux5ikyosl4QgpGLW6 | https://drive.google.com/file/d/1CV1bCwfSbTvH9cyux5ikyosl4QgpGLW6/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2023.JPG | 1-RKlRv7h_v8RzwRnNPIisG7nAIsCflPx | https://drive.google.com/file/d/1-RKlRv7h_v8RzwRnNPIisG7nAIsCflPx/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2024.JPG | 1IXxc971GdAu8OrgoKqEa_t5YkzemrbOa | https://drive.google.com/file/d/1IXxc971GdAu8OrgoKqEa_t5YkzemrbOa/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2025.JPG | 1bNzOI7-L-u735_IAY5Id0S1-mJOBkkCn | https://drive.google.com/file/d/1bNzOI7-L-u735_IAY5Id0S1-mJOBkkCn/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2026.JPG | 1t8nkkE0T6_gC5KYapc7uMIHROfl2ijMx | https://drive.google.com/file/d/1t8nkkE0T6_gC5KYapc7uMIHROfl2ijMx/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2027.JPG | 1Pez7QKobv9z9G2qJvBxDjYHB5CPuromw | https://drive.google.com/file/d/1Pez7QKobv9z9G2qJvBxDjYHB5CPuromw/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2028.JPG | 1EaHOy4d4tMgqQxd_5RuU90eReEftK6EQ | https://drive.google.com/file/d/1EaHOy4d4tMgqQxd_5RuU90eReEftK6EQ/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2029.JPG | 1KIdReeA5vff6tcIWt3LuQlvj-q_tgRdN | https://drive.google.com/file/d/1KIdReeA5vff6tcIWt3LuQlvj-q_tgRdN/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2030.JPG | 1zzXfubJpXNeAXcWjvKraqiw1gDHpdshh | https://drive.google.com/file/d/1zzXfubJpXNeAXcWjvKraqiw1gDHpdshh/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2031.JPG | 1VbGoKtedg79UfGuvCp503WEeQLdWjLux | https://drive.google.com/file/d/1VbGoKtedg79UfGuvCp503WEeQLdWjLux/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2032.JPG | 1FSqX2ontkSgDA5VD3nwsK-9nnT4Mhezp | https://drive.google.com/file/d/1FSqX2ontkSgDA5VD3nwsK-9nnT4Mhezp/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2033.JPG | 1M4qXMQZQo8gbkWNlWjkiJJ-qRf7vDFQ1 | https://drive.google.com/file/d/1M4qXMQZQo8gbkWNlWjkiJJ-qRf7vDFQ1/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2034.JPG | 1--dHM20nZ-RJd3OqL3BUQqmCkT3cMthL | https://drive.google.com/file/d/1--dHM20nZ-RJd3OqL3BUQqmCkT3cMthL/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2035.JPG | 1m-UJYYCkr6QP9slSPFqQypTxyFGPbc7A | https://drive.google.com/file/d/1m-UJYYCkr6QP9slSPFqQypTxyFGPbc7A/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2036.JPG | 1WZkXtR1a824EIh-C4IsEvqj6vcOWAzqD | https://drive.google.com/file/d/1WZkXtR1a824EIh-C4IsEvqj6vcOWAzqD/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2037.JPG | 1MzcNW_uIlDgDPhzTYkMznZqgu2HmGlLy | https://drive.google.com/file/d/1MzcNW_uIlDgDPhzTYkMznZqgu2HmGlLy/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2038.JPG | 1Madie1MxNATPMdPPRUDs9VkhRSbpl4TG | https://drive.google.com/file/d/1Madie1MxNATPMdPPRUDs9VkhRSbpl4TG/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2039.JPG | 1jt5InvpUkm5zSYh0kWluQgJjNS_u9WpG | https://drive.google.com/file/d/1jt5InvpUkm5zSYh0kWluQgJjNS_u9WpG/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2040.JPG | 1B3c9WyUhyNoaLljIQ4iGwKDuCu3t2BrM | https://drive.google.com/file/d/1B3c9WyUhyNoaLljIQ4iGwKDuCu3t2BrM/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2041.JPG | 1ljGytGndFEnKROyyVffHj1xhTUWvKa_u | https://drive.google.com/file/d/1ljGytGndFEnKROyyVffHj1xhTUWvKa_u/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2042.JPG | 1hx87OETY8LF9NIlptffXFDOcYfOMaXPv | https://drive.google.com/file/d/1hx87OETY8LF9NIlptffXFDOcYfOMaXPv/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-2043.JPG | 1HAXMlYHZoXKIMhaJGcbRRctg0JxsWZ9g | https://drive.google.com/file/d/1HAXMlYHZoXKIMhaJGcbRRctg0JxsWZ9g/view | LOWRES | no | yes |  | portrait | auto, verify |
| maharat-1859.JPG | 1Dxde2gv0nO4miChU5KjKB9CAZE9FLtH6 | https://drive.google.com/file/d/1Dxde2gv0nO4miChU5KjKB9CAZE9FLtH6/view | LOWRES / AYA SELECTS | no | no | 10M6itib1YfT0CqcClaC2P_34DDn0oWRN | portrait | auto, verify |
| maharat-1868.JPG | 1_3MWqbiwl_7lSlIfqGrlkdc4iyb0zVbl | https://drive.google.com/file/d/1_3MWqbiwl_7lSlIfqGrlkdc4iyb0zVbl/view | LOWRES / AYA SELECTS | no | no | 1mvC_WuIMM6tQi9feHCYNhAlfKiycpGws | portrait | auto, verify |
| maharat-1888.JPG | 1P-CQDbvYRoyd-6Gn_XRU7mswCLc5Uuey | https://drive.google.com/file/d/1P-CQDbvYRoyd-6Gn_XRU7mswCLc5Uuey/view | LOWRES / AYA SELECTS | no | no | 1WRH0B4teI8oPY49zYaZrGVRYbyaK7Jyf | portrait | auto, verify |
| maharat-1962.JPG | 1RiM0Paivfbh2UlfHTymhwlBi1Kbta06F | https://drive.google.com/file/d/1RiM0Paivfbh2UlfHTymhwlBi1Kbta06F/view | LOWRES / AYA SELECTS | no | no | 1F2kmHUJPb2nI_FwP8MC4MsvUlkrIbg7w | portrait | auto, verify |
| maharat-1978.JPG | 15lSaAhAfM2wCJTxC893K-JRyBxbwrL5z | https://drive.google.com/file/d/15lSaAhAfM2wCJTxC893K-JRyBxbwrL5z/view | LOWRES / AYA SELECTS | no | no | 1P9ONZaPGKQjmmoYCroNBgwM0Y74zfYIo | portrait | auto, verify |
| maharat-1987.JPG | 1oUSAvJ5kXQjJh65KVOV56j5LDClp0Osq | https://drive.google.com/file/d/1oUSAvJ5kXQjJh65KVOV56j5LDClp0Osq/view | LOWRES / AYA SELECTS | no | no | 1eX2TMxCnQvzgH_g7BQkH8e0VLQyLtlsv | portrait | auto, verify |
| maharat-2001.JPG | 1UbR35hWV89O2xswM_Kcd0DjWkih5Uc9h | https://drive.google.com/file/d/1UbR35hWV89O2xswM_Kcd0DjWkih5Uc9h/view | LOWRES / AYA SELECTS | no | no | 1c1szdCtbBX7w4pI8Zr6m-GH0b3ppogzr | portrait | auto, verify |

## Fetch and refresh

- No proof fetch done for this instructor (Bassam already carries the one cache demo). To fetch a preferred portrait into the gitignored cache, run `python3 .claude/scripts/drive_image_sync.py fetch mona-ataya --placement 4x5`.
- Refresh the rows: re-enumerate in an MCP session, update `scripts/cache/drive-enum-mona-ataya.json`, then run `python3 .claude/scripts/drive_image_sync.py catalog mona-ataya` and `python3 .claude/scripts/image_catalog_check.py mona-ataya`.
