"""Notes for the psa-31.json batch (Nov 15): two new football base rookies with real PSA 10 volume, both fail on
expected value. Screened in the pane the same day (pop-report search + getPriceSummary, 24 terms), looking for cards not
yet on the board with 25+ PSA 10 sales in 90 days: Jaxson Dart 2025 Prizm #332 (28 sales, $103 median) and Puka Nacua
2023 Prizm #357 (27, $56) qualified; raw for both is eBay sold read Nov 14 (base only, parallels and graded excluded).
Checked and left off for volume (PSA 10 sales in 90 days, Nov 15): Jaxon Smith-Njigba 2023 Prizm #390 base 10222876 (3;
the Silver on the board has 53), Malik Nabers 2024 Prizm #370 base 12496739 (8), Marvin Harrison Jr. 2024 Prizm #375
base (only the Pandora spec 12499615 returned, 1), Ashton Jeanty 2025 Prizm #315 15118045 (3), Emeka Egbuka 2025 Prizm
#351 15118081 (0), Josh Allen 2018 Prizm #205 Silver 2670023 (1, a $15,000 sale), Allen 2018 Optic #154 Holo 2716037
(11, already on the board), Paul Skenes 2024 Bowman Chrome Prospects BCP125 10962588 (22, $40: a $5 raw card that
loses money graded, so not added as Thin), Jayden Daniels 2024 Donruss The Rookies TR37 12178075 (61 sales but an
insert, $47; the paper Rated Rookie did not resolve through the pop search by card number, nor did Caleb Williams's or
Drake Maye's). No PSA 10 has sold yet of the 2026 Topps Update rookies (Griffin US1 17671019, McGonigle US7 17671025,
Murakami US350 17671352), 2026 Topps Chrome #225 Roman Anthony 16805241, or any 2026-27 Topps Dybantsa card (the pop
search returns only Topps Now Draft and Bowman U Now specs); re-check all of them in December.
PSA's spec 2495436 "2017 Panini Prizm 269 Patrick Mahomes II Prizm" is the Silver Prizm (PSA names the silver parallel
"Prizm"), which is what the board's Mahomes Silver entry already uses; the plain base spec 6036052 still returns an empty
APR summary.
Usage: python3 notes31.py
"""
import os
from r2gnotes import write_notes

LEAD = {
 "dart-2025-prizm-332": "Base rookie from 2025 Prizm, the first Prizm Football under the new NFL deal, released in September; Dart became the Giants' starter in October.",
 "nacua-2023-prizm-357": "Base rookie from 2023 Prizm; his Silver is not on the board (too few PSA 10 sales when checked Oct 15).",
}
CLOSE = {
 "dart-2025-prizm-332": "The 10 trades often enough (28 sales), but a 23% gem rate on a $2 card with a $103 ten and a $22 nine leaves the expected value $23 under the all-in. Fails on expected value. The raw price cannot fall far enough to fix it; the 10 would need to be about $200.",
 "nacua-2023-prizm-357": "A 41% gem rate is good, but a $56 ten nets $39 after the haircut and fees against $52 all-in, so even a 10 loses money. Fails on expected value. A $2 card to keep raw.",
}
write_notes("psa-31.json", LEAD, CLOSE, "Nov 15")
