"""Notes for the psa-22.json batch (Oct 20). Three new cards with 25+ PSA 10 sales in 90 days, all fails on value:
the Silver Prizm rookies of Brock Bowers (2024 #315) and Ja'Marr Chase (2021 #337), whose base Prizms were already on
the board, and the 2019-20 Donruss Optic Ja Morant Rated Rookie #168 base. Raw prices are PSA's own ungraded tracking.
The Oct 20 refresh pulls for the ten oldest board cards (Purdy Silver, Stroud base and Silver, Giannis, Jokic, Zion
Silver, Haliburton Silver, Maxey Silver, Brunson Silver, Wembanyama Silver) are in psa-21.json, applied with refresh.py.
Checked and left off for volume: 2019-20 Donruss Optic Morant #168 Holo 2970540 (18 PSA 10 sales in 90 days).
Usage: python3 notes22.py
"""
from r2gnotes import write_notes
LEAD = {
 "bowers-2024-prizm-315-silver": "Silver Prizm rookie (the base is on the board). Raw $11 median of 15 PSA-tracked sales ($6.05 to $14.99).",
 "chase-2021-prizm-337-silver": "Silver Prizm rookie (the base is on the board). Raw $26 median of 15 PSA-tracked sales ($10 to $34.99).",
 "morant-2019-optic-168": "Optic Rated Rookie base. Raw $2.25 median of 15 PSA-tracked sales ($0.99 to $13).",
}
CLOSE = {
 "bowers-2024-prizm-315-silver": "Fails: a $197 PSA 10 nets about $56 over the $81 all-in, but a $35 nine loses about $55, and at 27% gem against a 50% break-even the expected value is –$25. 60% of submissions come back 9. 44 PSA 10 sales in 90 days (median $197, latest $192).",
 "chase-2021-prizm-337-silver": "Fails, narrowly: a $250 PSA 10 nets about $78 over the $96 all-in, a $50 nine loses about $59, and 38% gem against a 43% break-even gives –$7 expected value. Exactly 25 PSA 10 sales in 90 days (median $250, latest $300), so it sits on the volume floor too. A raw copy under $20 with sharp corners would flip it.",
 "morant-2019-optic-168": "Fails at any gem rate: a $22 PSA 10 nets about $15 against a $72 all-in, so a hit loses about $57. 67 PSA 10 sales in 90 days (median $22, latest $32) and 9,608 tens in circulation. Buy the slab.",
}
write_notes("psa-22.json", LEAD, CLOSE, "Oct 20")
