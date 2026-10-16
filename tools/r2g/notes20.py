"""Notes for the psa-20.json batch (Oct 16). Three new cards with 25+ PSA 10 sales in 90 days, all fails on value:
the Acuna 2018 Topps Chrome Update HMT25 the board was missing and the base
Prizm rookies of Trae Young (2018 #78) and Donovan Mitchell (2017 #117), whose Silvers were already on the board.
Raw prices are PSA's own ungraded tracking (15 sales each; cheap cards, so a cross-check would not move the verdict).
The Oct 16 refresh pulls for the ten oldest board cards (Caminero, De Vries, Holmgren x2, Amen Thompson, Scoot, SGA
Silver, Mahomes Donruss, Jefferson Silver, Purdy base) are in psa-19.json, applied with refresh.py; the Acuna 2018 Topps
Update US250 pull in this file refreshed the existing board card the same way (the board spells him Acuña there).
Checked and left off for volume (PSA 10 sales in 90 days): 2024 Prizm Marvin Harrison Jr. #375 base 12496744 (15),
2024 Prizm Malik Nabers #370 base 12496739 (10), 2020 Prizm Tyrese Maxey #256 base 4735763 (17). 2022 Topps Chrome
Julio Rodriguez #222: PSA lists the rookie only as an SP (spec 7885073), which may be the same card as the board's
"SP photo variation" entry, so it was not pulled.
Usage: python3 notes20.py
"""
from r2gnotes import write_notes
LEAD = {
 "acuna-2018-tcu-hmt25": "The Topps Chrome Update rookie from the 2018 retail mega boxes. Raw $10 median of 15 PSA-tracked sales ($4.75 to $19.99).",
 "trae-2018-prizm-78": "Base Prizm rookie (the Silver is on the board). Raw $1.70 median of 15 PSA-tracked sales ($0.99 to $7).",
 "mitchell-2017-prizm-117": "Base Prizm rookie (the Silver is on the board). Raw $2.99 median of 15 PSA-tracked sales ($1.31 to $7.99).",
}
CLOSE = {
 "acuna-2018-tcu-hmt25": "Fails at any gem rate even though 92% of submissions come back 10: a $43 PSA 10 nets about $30 against an $80 all-in, so a hit loses about $50. 112 PSA 10 sales in 90 days (median $43, latest $46). The gem rate makes it a safe grade and a bad trade; 10,435 tens in the pop keep the slab at $40.",
 "trae-2018-prizm-78": "Fails at any gem rate: a $21 PSA 10 nets about $14 against a $72 all-in, so a hit loses about $57. 112 PSA 10 sales in 90 days (median $21, latest $17) and 27,288 graded, 51% of them a 9. Same answer as the Silver, which fails on value too.",
 "mitchell-2017-prizm-117": "Fails at any gem rate: a $30 PSA 10 nets about $21 against a $73 all-in, so a hit loses about $52. 47 PSA 10 sales in 90 days (median $30, latest $35) and 5,334 tens in circulation. The slab costs less than half the grading fee.",
}
write_notes("psa-20.json", LEAD, CLOSE, "Oct 16")
