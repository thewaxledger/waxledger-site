"""Notes for the psa-33.json batch (Nov 17): four candidates from a pane screen of 16 pop-report terms (13 specs
checked with getPriceSummary), full pulls for the four with 10+ PSA 10 sales in 90 days. Raw is eBay sold read Nov 17 in
the pane (last 45 days, plain parallel only: colour refractors, Ice / Cracked Ice, graded, damaged and lots excluded by
title); PSA's own raw tracking is kept in the pull as rawPsa and agrees within 10% on all four.
Two clear as Grade: Shohei Ohtani 2018 Topps Chrome #150 Refractor (84 PSA 10 sales, $4,202 median of the newest 50,
67% gem, raw $2,025 on 15 sales) and Lamine Yamal 2023-24 Topps Chrome UEFA Club Competitions #64 Refractor (27 sales,
$1,800, 43% gem, raw $304 on 9 sales). Two are thin markets: Caitlin Clark 2024 Prizm WNBA #22 Silver (19 sales, $2,880,
7% gem, raw $260 on 47) and Cam Ward 2025 Prizm #352 Silver (10 sales, $473, 21% gem, raw $19 on 97).
Left off for volume (PSA 10 sales in 90 days): Mayfield 2018 Prizm #201 Silver (1), Bellingham 2020 Topps Chrome
Bundesliga #31 base (16) and Refractor (8), Mobley 2021 Prizm #325 (2), Jalen Williams 2022 Prizm #246 (2), McCain 2024
Prizm #222 (1), Sasaki 2025 Topps Chrome #217 Refractor (2), McConkey 2024 Prizm #365 (8), Travis Hunter 2025 Prizm
#301 (0). The Dart and Jeanty Silvers did not surface in the first 25 pop-search hits; try "silver" in the term next time.
Usage: python3 notes33.py
"""
from r2gnotes import write_notes

LEAD = {
 "ohtani-2018-tc-150-refractor": "The unnumbered Refractor of his 2018 Topps Chrome rookie (the base #150 is also on the board). The most expensive raw card on the board: a $2,000 card going in, so the Standard fee applies and a miss costs real money.",
 "yamal-2023-tc-ucc-64-refractor": "The unnumbered Refractor of his first Topps Chrome card (the base #64 is on the board too; his 2024 Euro #17 is a thin market).",
 "clark-2024-prizm-wnba-22-silver": "The Silver Prizm of her 2024 Prizm WNBA rookie (the base #22 is on the board). Her second WNBA season ended in September; the card trades year-round.",
 "ward-2025-prizm-352-silver": "The Silver Prizm of the 2025 first overall pick's Prizm rookie (his base #352 had nine PSA 10 sales when checked Oct 15 and is not on the board). Titans starter since Week 1.",
}
CLOSE = {
 "ohtani-2018-tc-150-refractor": "A 67% gem rate on 3,098 graded and 84 PSA 10 sales in 90 days make this the deepest market on the board, and a 10 nets about $830 over the $2,095 all-in. The caution is the price itself: the 10 is sliding (the newest 50 sales median $4,202 against a 90-day average of $5,249, latest $3,600), raw copies sold between $1,224 and $3,300 in 45 days, and a 9 loses about $190. Grade, with the margin shrinking week to week; the raw price paid decides it.",
 "yamal-2023-tc-ucc-64-refractor": "27 PSA 10 sales at $1,800 against a $304 raw card and a 43% gem rate: a 10 nets about $880 and a 9 loses $115, expected value +$315. Clears the floor by two sales, so check the 90-day count before sending a stack; the raw read is nine eBay sales in 45 days (PSA's tracking agrees at $290).",
 "clark-2024-prizm-wnba-22-silver": "The 10 is $2,880 but only 7% of 3,471 graded copies are a 10 (53% are a 9, 34% an 8 or lower), so the expected value is +$24 on a $330 all-in; a 9 loses $104. 19 PSA 10 sales in 90 days makes it a thin market, not a grade. A card to send only if the copy is pack-fresh and centred; the board prices the miss as a 9, and a third of misses here are worse.",
 "ward-2025-prizm-352-silver": "A $19 card with a $473 ten and a 21% gem rate: expected value +$52 on $69 all-in, and a 9 at $89 nearly covers the cost. Ten PSA 10 sales in 90 days is exactly the thin-market floor; a $300 latest sale says the 10 is softening after a 2-8 start for the Titans. Thin market: grade clean copies, do not stock up.",
}
write_notes("psa-33.json", LEAD, CLOSE, "Nov 17")
