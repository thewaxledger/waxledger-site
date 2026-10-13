"""Notes for the psa-14.json batch (Oct 13). Five new cards with 25+ PSA 10 sales in 90 days: three Young Guns
(Carlsson, Fantilli, Pettersson) and two base Prizm football rookies (Kyler Murray, Justin Jefferson). Raw is eBay
sold, titles carrying the card number. The same file holds the Oct 13 refresh pulls for the ten oldest board cards
(applied with refresh.py, not from here). Checked and left off for volume: 2025 Prizm Jaxson Dart #332 (24 PSA 10
sales), Cam Ward #352 (9), Jeanty #315 (3), Travis Hunter #301 (1); 2018 Prizm Saquon Barkley #202 (19); 2023 Prizm
Puka Nacua #357 (20), Bijan Robinson #305 (9); 2024 Prizm Stephon Castle #234 (9); 2025 Topps Chrome James Wood
#132 (9), Dylan Crews #146 (2). Usage: python3 notes14.py
"""
from r2gnotes import write_notes
LEAD = {
 "carlsson-2023-ud-468": "Young Guns rookie (2023-24 Series 2). Raw $29 on eBay (57 sales in 30 days, $20 to $50).",
 "fantilli-2023-ud-711": "Young Guns rookie from 2023-24 Upper Deck Extended Series, card #711. Raw $20 on eBay (11 sales in 30 days, $17 to $31).",
 "pettersson-2018-ud-248": "Young Guns rookie (2018-19 Series 1). Raw $22 on eBay (11 sales in 30 days, $16 to $42).",
 "murray-2019-prizm-301": "Base Prizm rookie. Raw $5 on eBay, but only nine clean base sales in 30 days ($1 to $16).",
 "jefferson-2020-prizm-398": "Base Prizm rookie. Raw $5 on eBay (45 sales in 30 days, $1 to $26).",
}
CLOSE = {
 "carlsson-2023-ud-468": "Fails on expected value. Volume is there (83 PSA 10 sales in 90 days at $125 to $300) and a hit pays about $49, but 44% gem is 12 points short of the 56% break-even because the $51 PSA 9 does not cover a $99 all-in. A raw copy at about $16 would bring it to break-even, and none sold that low.",
 "fantilli-2023-ud-711": "Fails: a 10 nets less than the all-in, so even a 50% gem rate loses about $39 a try. 33 PSA 10 sales in 90 days at $97 to $150. The PSA 10 would need to be about $130 for a hit to cover the cost, before counting the misses.",
 "pettersson-2018-ud-248": "Fails. The gem rate is the highest of this batch (75%, 2,870 tens of 3,850), which is why the PSA 10 is only $75: a hit loses about $40 after the grading fee. 36 PSA 10 sales in 90 days; the PSA 9 price is seven sales.",
 "murray-2019-prizm-301": "Fails at any gem rate: a $53 PSA 10 nets about $37 against a $75 all-in. Liquid (88 PSA 10 sales in 90 days, $25 to $95, latest $37) but the price is too low to carry the fee.",
 "jefferson-2020-prizm-398": "Fails: a $95 PSA 10 nets about $66 against a $75 all-in, so a hit loses about $9 and a miss about $56, and 27% gem means most are misses. 31 PSA 10 sales in 90 days. The Silver Prizm is the version on the board with a wider gap.",
}
write_notes("psa-14.json", LEAD, CLOSE, "Oct 13")
