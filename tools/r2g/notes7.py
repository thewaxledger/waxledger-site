"""Notes for the psa-7.json batch (Oct 11): Wembanyama, Cooper Flagg and Dylan Harper flagship cards.
Usage: python3 notes7.py   (idempotent: rewrites the keys listed in LEAD)
"""
from r2gnotes import write_notes

LEAD = {
 "wemby-2023-optic-225": "Donruss Optic Rated Rookie, base.",
 "wemby-2023-optic-225-holo": "Donruss Optic Rated Rookie Holo, the Optic equivalent of a silver.",
 "wemby-2023-donruss-220": "Donruss Rated Rookie, the paper base card.",
 "wemby-2023-hoops-277": "NBA Hoops base rookie, the cheapest licensed Wembanyama rookie.",
 "wemby-2023-pdp-002": "Prizm Draft Picks base, the pre-NBA card released before Prizm.",
 "wemby-2023-pdp-002-silver": "Prizm Draft Picks Silver Prizm, the first silver Wembanyama card of the season.",
 "wemby-2023-select-087": "Select Concourse base rookie (#87, the Concourse tier).",
 "wemby-2023-select-087-silver": "Select Concourse Silver Prizm rookie.",
 "wemby-2023-tc-001": "Topps Chrome #1 base rookie, from the 2023-24 Topps Chrome set Topps released after regaining the licence.",
 "wemby-2023-tc-001-refractor": "Topps Chrome #1 Refractor (unnumbered).",
 "wemby-2023-mosaic-238": "Mosaic base rookie.",
 "wemby-2023-mosaic-238-silver": "Mosaic Silver rookie.",
 "flagg-2025-topps-201": "Topps flagship paper base rookie, the most-graded Flagg card.",
 "flagg-2024-bcu-016": "Bowman Chrome University base, the Duke-uniform card from the season before the draft.",
 "flagg-2024-bcu-016-refractor": "Bowman Chrome University Refractor (unnumbered), Duke uniform.",
 "flagg-2025-topps-now-draft-0d1": "Topps Now Draft card, printed to order after the draft (the print run is the pop).",
 "harper-2025-topps-202": "Topps flagship paper base rookie.",
 "harper-2024-bcu-022": "Bowman Chrome University base, Rutgers uniform.",
 "pca-2020-bd-72-chrome-refractor": "1st Bowman Chrome Refractor (unnumbered), the chase version of the BD-72. The PSA 10 is sliding: the 40-sale median is $750, the last 15 sales (Sep 27 to Oct 8) median $615 and the latest printed $465, so the math here uses $615.",
 "pca-2020-bd-72-chrome": "1st Bowman Chrome base. Same slide as the Refractor: 40-sale median $369, last 15 sales median $315, latest $255; the math uses $315.",
 "pca-2020-bd-72-paper": "1st Bowman paper base.",
}
CLOSE = {
 "wemby-2023-optic-225": "Gem rate 48% against a 51% break-even: a wash, with real liquidity (98 PSA 10 sales in 90 days). Fails on expected value by $2. Buy raw under $12 and it is marginal.",
 "wemby-2023-optic-225-holo": "Gem rate 45% against a 26% break-even, 54 PSA 10 sales in 90 days, and a $286 PSA 9 that holds a miss to about –$175 on a $386 all-in. Grade it. Raw copies at $316 on eBay (56 sales); above $400 the cushion is gone.",
 "wemby-2023-donruss-220": "A 23% gem rate on a $170 PSA 10 cannot cover the $80 all-in; 61% of the pop is a 9. Fails on expected value. Skip.",
 "wemby-2023-hoops-277": "The 76% gem rate is real and 154 PSA 10 sales in 90 days is real liquidity, but a $90 PSA 10 nets about $63 after fees against a $76 all-in. Fails on expected value. The 10 would need to reach $120.",
 "wemby-2023-pdp-002": "Gems 59% of the time, but a $113 PSA 10 cannot cover the $80 all-in. Fails on expected value. Skip.",
 "wemby-2023-pdp-002-silver": "Gem rate 68% against a 21% break-even, and a $110 PSA 9 (only 5 tracked sales) that holds a miss to about –$23. Grade it. 27 PSA 10 sales in 90 days is just over the liquidity floor, so sell patiently. Raw at $35 on eBay (66 sales).",
 "wemby-2023-select-087": "A 77% gem rate on a $116 PSA 10 still cannot cover the $87 all-in. Fails on expected value. Skip.",
 "wemby-2023-select-087-silver": "Gem rate 67% against a 48% break-even, 40 PSA 10 sales in 90 days. Grade it at a raw under $100; the edge disappears above $130. Raw trades at $100 on eBay (47 sales), where PSA's own raw tracking had $80.",
 "wemby-2023-tc-001": "Only 27% gem, but the $552 PSA 10 against a $35 raw makes the break-even 9%, and the $105 PSA 9 holds a miss to about –$27. Grade it. 44 PSA 10 sales in 90 days. Buy raw under $50.",
 "wemby-2023-tc-001-refractor": "The math is the best in this batch (a $2,562 PSA 10 against a $300 raw), but PSA tracked 8 PSA 10 sales in 90 days and the last one printed $984. Fails the liquidity floor. If you own one raw, grade it; do not buy to grade until the 10 trades weekly.",
 "wemby-2023-mosaic-238": "20 PSA 10 sales in 90 days, under the floor, and a $147 PSA 10 at a 46% gem rate is a wash. Fails. Skip.",
 "wemby-2023-mosaic-238-silver": "Five PSA 10 sales in 90 days and a pop of 385. The math clears on paper (a $995 PSA 10 against a $50 raw) but there is no market to sell into. Fails the liquidity floor. If you own one raw, grade it.",
 "flagg-2025-topps-201": "PSA caps its count at 1,000 PSA 10 sales in 90 days, so it is the most liquid Flagg card, but a $105 PSA 10 at a 33% gem rate against a $25 PSA 9 cannot cover the $74 all-in. Fails on expected value. Skip.",
 "flagg-2024-bcu-016": "Gems 53% of the time, but an $82 PSA 10 cannot cover the $74 all-in. Fails on expected value. Skip.",
 "flagg-2024-bcu-016-refractor": "Gem rate 47% against a 43% break-even: expected value about +$5, and only 10 PSA 10 sales in 90 days. Fails the liquidity floor. Skip as a buy-to-grade.",
 "flagg-2025-topps-now-draft-0d1": "An 81% gem rate (print-to-order cards arrive clean) and 308 PSA 10 sales in 90 days, but a $64 PSA 10 nets about $45 after fees against a $76 all-in. Fails on expected value. Skip.",
 "harper-2025-topps-202": "A $118 PSA 10 at a 42% gem rate against a $34 PSA 9 cannot cover the $72 all-in. Fails on expected value. Skip.",
 "harper-2024-bcu-022": "Five PSA 10 sales in 90 days and a pop of 231; nobody is grading the Rutgers card. Fails the liquidity floor and on expected value. Skip.",
 "pca-2020-bd-72-chrome-refractor": "A 70% gem rate against a 27% break-even, 155 PSA 10 sales in 90 days, and a $200 PSA 9 that holds a miss to about –$76. Grade it, but price the 10 at $500 to $600, not the $750 from a month ago: at the $465 latest sale the expected value is still about +$50. Raw at $154 on eBay (71 sales); above $200 the edge thins fast.",
 "pca-2020-bd-72-chrome": "Gem rate 63% against a 6% break-even: the $125 PSA 9 nearly covers the $100 all-in by itself. Grade it. Liquid (121 PSA 10 sales in 90 days) and cheap to try; buy raw under $35.",
 "pca-2020-bd-72-paper": "A $120 PSA 10 at a 65% gem rate against a $42 PSA 9 cannot quite cover the $77 all-in. Fails on expected value by $12. The Chrome versions are where the grade pays.",
}
write_notes("psa-7.json", LEAD, CLOSE, "Oct 11")
