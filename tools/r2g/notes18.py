"""Notes for the psa-18.json batch (Oct 15). Four new cards with 25+ PSA 10 sales in 90 days: the two Ohtani 2018 cards
the board was missing (Bowman #49 paper, Topps Chrome Update HMT1), the Zion 2019 Prizm base and the Elly De La Cruz
2024 Topps Chrome base. Raw for both Ohtanis is eBay sold, titles carrying the card number, parallels and graded
excluded; Zion and Elly keep PSA's own raw tracking (cheap cards, 15 sales each).
The Oct 15 refresh pulls for the ten oldest board cards are in psa-16.json.
Checked and left off: 2003 Topps LeBron James #221 (102 PSA 10 sales but 12% gem, 39% nine, 28% eight: the model's
PSA 9 miss price overstates it, Aidan's call to keep such cards off), 2009 Topps Stephen Curry #321 (10 sales, 5% gem),
2009 Topps Chrome Curry #101 (4), 2018 Prizm Jalen Brunson #250 base (13), 2023 Prizm Puka Nacua #357 (23),
2017 Prizm Patrick Mahomes #269 base (PSA's spec 6036052 returns no sales summary; the Silver is on the board).
Usage: python3 notes18.py
"""
from r2gnotes import write_notes
LEAD = {
 "ohtani-2018-bowman-49": "His paper Bowman rookie, the most-graded Ohtani card there is (40,105 in the PSA pop). Raw $96 on eBay (114 sales in 13 days, most $80 to $105).",
 "ohtani-2018-tcu-hmt1": "The Topps Chrome Update rookie, the Chrome set that came only in retail mega boxes in 2018. Raw $275 on eBay (74 sales in 30 days, $100 to $1,000; the middle of the range is $215 to $300).",
 "zion-2019-prizm-248": "Base Prizm rookie. Raw $3.50 median of 15 PSA-tracked sales ($1.25 to $33).",
 "elly-2024-tc-44": "Base Topps Chrome rookie. Raw $2.25 median of 15 PSA-tracked sales ($0.99 to $3.99).",
}
CLOSE = {
 "ohtani-2018-bowman-49": "Clears: a $617 PSA 10 nets about $263 over the $166 all-in, a $140 nine loses about $62, and at 38% gem the expected value is +$62 against a 19% break-even. The catch is the pop shape: 51% of all submissions came back 9 and 7.6% came back 8 or lower, so this is a centering-and-corners card; pay the $96 only for a copy with even borders. 278 PSA 10 sales in 90 days (median $617, latest $550; the $21,000 at the top of the range is one outlier).",
 "ohtani-2018-tcu-hmt1": "Clears, third among the five Ohtani rookies on the board by expected value (Topps Chrome #150 +$200, Series 2 #700 +$141): a $910 PSA 10 nets about $288 over the $345 all-in, a $330 nine loses about $101, and 61% gem against a 26% break-even gives +$136 expected value. 218 PSA 10 sales in 90 days (median $910, latest $820). The cost is capital: $275 raw plus $70 in fees per attempt, and a miss is a $100 loss.",
 "zion-2019-prizm-248": "Fails at any gem rate: a $21 PSA 10 nets about $15 against a $73 all-in, so even a hit loses about $59. 147 PSA 10 sales in 90 days ($9.50 to $71, median $21) and 23,148 tens in circulation. The slab is cheaper than the grading fee; buy the 10 if you want one.",
 "elly-2024-tc-44": "Fails at any gem rate: a $61 PSA 10 nets about $43 against a $72 all-in, so a hit loses about $30 and a miss about $60. 26 PSA 10 sales in 90 days ($48 to $468, median $61, latest $65). 30% gem and 54% nine on 3,694 graded: the 2024 Chrome centering problem again.",
}
write_notes("psa-18.json", LEAD, CLOSE, "Oct 15")
