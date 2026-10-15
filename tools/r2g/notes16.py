"""Notes for the psa-16.json batch (Oct 15). Three new cards with 25+ PSA 10 sales in 90 days: James Wood 2022 Bowman
Chrome Prospects BCP-108, Jackson Holliday 2022 Bowman Draft Chrome BDC-168, Jac Caglianone 2024 Bowman Draft Chrome
BDC-8. Raw is eBay sold, titles carrying the card number. The same file holds the Oct 15 refresh pulls for the ten
oldest board cards (applied with refresh.py, not from here).
Checked and left off for volume (PSA 10 sales in 90 days): 2023 Prizm Puka Nacua #357 (23), 2023 Bowman Chrome
Prospects Elly De La Cruz BCP-65 (23), 2023 Prizm Jahmyr Gibbs #331 (10), 2023 Prizm Bijan Robinson #305 (9),
2024 Prizm Stephon Castle #234 (9), 2025 Prizm Cam Ward #352 (9), Shedeur Sanders #302 (6), Travis Hunter #301 (1),
2009 Topps Stephen Curry #321 (10, and a 5% gem rate the model does not price). 2017 Prizm Mahomes #269 returned an
empty APR summary twice.
Usage: python3 notes16.py
"""
from r2gnotes import write_notes
LEAD = {
 "wood-2022-bcp108": "1st Bowman Chrome. Raw $2.43 on eBay (28 sales in 30 days, $0.99 to $6.49).",
 "holliday-2022-bdc168": "1st Bowman Chrome, the Draft version. Raw $3 on eBay (11 sales in 30 days, $0.99 to $15).",
 "caglianone-2024-bdc8": "1st Bowman Chrome. Raw $6.75 on eBay (30 sales in 30 days, $1.25 to $85; the image variation sells separately and is excluded).",
}
CLOSE = {
 "wood-2022-bcp108": "Fails at any gem rate: a $45 PSA 10 nets about $31 against a $72 all-in, so a hit loses about $41 and a miss about $61. 66 PSA 10 sales in 90 days ($24 to $105, latest $40). 64% of the pop is a 10, which is why the 10 is cheap.",
 "holliday-2022-bdc168": "Fails at any gem rate: a $30 PSA 10 nets about $21 against a $73 all-in. 48 PSA 10 sales in 90 days ($10 to $55, latest $40). 3,211 tens in circulation; the PSA 9 is $12.",
 "caglianone-2024-bdc8": "Fails at any gem rate: a $75 PSA 10 nets about $52 against a $77 all-in, so even a hit loses about $25. 36 PSA 10 sales in 90 days ($36 to $120, latest $65); the PSA 9 median is $20 on 35 sales. The PSA 10 would need to be about $110 for a hit to cover the cost.",
}
write_notes("psa-16.json", LEAD, CLOSE, "Oct 15")
