"""Notes for the psa-8.json batch (Oct 11): the high-gem-rate screen. Fifteen cards with PSA gem rates of 59-87%;
nine are new to the board (this file), six were already on it and were refreshed in place with refresh.py.
Usage: python3 notes8.py
"""
from r2gnotes import write_notes

LEAD = {
 "acuna-2018-tc-193": "Topps Chrome base rookie. The highest gem rate on the board after Soto's Chrome Update: 85% of 15,877 graded came back 10.",
 "soto-2018-tcu-hmt98": "Topps Chrome Update Rookie Debut (#HMT98, the second Soto in the set; the #HMT55 is the one most people call the rookie). 87% gem.",
 "langford-2023-bdc106": "1st Bowman Chrome (Bowman Draft). 76% gem.",
 "clark-2023-bdc76": "1st Bowman Chrome (Bowman Draft). 72% gem.",
 "hughes-2019-ud-201": "Young Guns rookie. 72% gem, which is high even for Young Guns.",
 "carroll-2023-tc-95": "Topps Chrome base rookie. 65% gem.",
 "kaprizov-2020-ud-451": "Young Guns rookie. 64% gem.",
 "jeanty-2025-donruss-305": "Donruss Rated Rookie, the paper base card. 60% gem on a small pop (218).",
 "makar-2019-ud-493": "Young Guns rookie (Series 2). 59% gem.",
}
CLOSE = {
 "acuna-2018-tc-193": "The gem rate is why the 10 is a $44 card: 13,512 PSA 10s exist and 179 sold in 90 days. A $44 PSA 10 nets about $31 after fees against an $83 all-in. Fails on expected value. The lesson of this whole screen: a high gem rate makes the 10 common, and common 10s are cheap.",
 "soto-2018-tcu-hmt98": "5,141 PSA 10s and a $37 price. Fails on expected value by $54. The #HMT55 on the board is the same story at $64.",
 "langford-2023-bdc106": "3,177 PSA 10s, a $25 price, 38 sales in 90 days. Fails on expected value. Skip.",
 "clark-2023-bdc76": "The best of the cheap 1st Bowmans here: 123 PSA 10 sales in 90 days at $70, a $22 PSA 9, 72% gem. Still a $72 all-in against a $49 net on a 10. Fails on expected value by $33; the 10 would need to reach about $115.",
 "hughes-2019-ud-201": "Close: a $215 PSA 10 at 72% gem, a $106 PSA 9, 90 sales in 90 days. The $76 raw (44 eBay sales; PSA tracks $60) puts the all-in at $146 against a $150 net on a 10 and $79 on a 9. Fails on expected value by $17. Clears at a raw under $60, which the PSA-tracked sales suggest is available: buy carefully and it is a grade.",
 "carroll-2023-tc-95": "1,770 PSA 10s at $26. Fails on expected value. Skip.",
 "kaprizov-2020-ud-451": "A $175 PSA 10 at 64% gem, with 79 sales in 90 days, but the PSA 9 is only $65 and the raw $49 (58 eBay sales). The all-in is $119 against a $122 net on a 10. Fails on expected value by $24; it needs the 10 at $210 or the raw at $25.",
 "jeanty-2025-donruss-305": "Eight PSA 10 sales in 90 days and a $45 price. Fails the liquidity floor and on expected value. The Optic version gems 42% and sells more; neither pays at $60 a submission.",
 "makar-2019-ud-493": "The one card in this screen that clears: a $699 PSA 10 (49 sales in 90 days, $569 to $825), a $276 PSA 9 that holds a miss to about –$106, and 59% gem against a 38% break-even. $310 all-in, expected value +$61. Grade it. Raw copies trade at $240 on eBay (38 sales); the edge is gone above $290.",
}
write_notes("psa-8.json", LEAD, CLOSE, "Oct 11")
