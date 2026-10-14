"""Notes for the psa-15.json batch (Oct 14). Five new cards with 25+ PSA 10 sales in 90 days: four base Prizm football
rookies (CeeDee Lamb, Brock Bowers, Ja'Marr Chase, Jonathan Taylor) and the 2020 Topps Chrome Luis Robert. Raw is
eBay sold, titles carrying the card number (Robert keeps PSA's own raw tracking: only 5 clean eBay sales in 30 days).
The same file holds the Oct 14 refresh pulls for the ten oldest board cards (applied with refresh.py, not from here).
Checked and left off for volume: 2022 Prizm Garrett Wilson #309 (3 PSA 10 sales), 2024 Prizm Rome Odunze #385 (2),
2023 Topps Chrome Anthony Volpe #4 (17), 2024 Topps Chrome Junior Caminero #213 (18), 2016 Prizm Derrick Henry #298
(16), 2020 Topps Chrome Randy Arozarena #49 (47 sales but a $10 PSA 10). Already on the board: Anthony Edwards #258
(118), Jayson Tatum #16 (79), the Makar / Jack Hughes / Kaprizov / MacKinnon / Demidov hockey cards.
Usage: python3 notes15.py
"""
from r2gnotes import write_notes
LEAD = {
 "lamb-2020-prizm-334": "Base Prizm rookie. Raw $3 on eBay (26 sales in 30 days, $1 to $65; most under $5).",
 "bowers-2024-prizm-315": "Base Prizm rookie. Raw $2 on eBay (14 sales in 30 days, $1 to $14).",
 "robert-2020-tc-60": "Base Topps Chrome rookie. Raw $2.60 median of 15 PSA-tracked sales; only five clean eBay sales in 30 days ($0.70 to $5).",
 "chase-2021-prizm-337": "Base Prizm rookie (PSA catalogues it as #337). Raw $3 on eBay (18 sales in 30 days, $1 to $40).",
 "taylor-2020-prizm-332": "Base Prizm rookie. Raw $1.50 on eBay (22 sales in 30 days, $0.50 to $40).",
}
CLOSE = {
 "lamb-2020-prizm-334": "Fails at any gem rate: a $65 PSA 10 nets about $45 against a $73 all-in, so even a hit loses about $28. 26 PSA 10 sales in 90 days ($38 to $100, latest $99). The PSA 10 would need to be about $105 for a hit to cover the cost, and 30% gem means most attempts come back a $22 nine.",
 "bowers-2024-prizm-315": "Fails at any gem rate: a $51 PSA 10 nets about $35 against a $72 all-in. 26 PSA 10 sales in 90 days, $26 to $150 with the median at the low end. The PSA 9 is $15, so a miss loses about $61.",
 "robert-2020-tc-60": "Fails by the widest margin on the board: the PSA 10 is $7 (59 sales in 90 days, $3 to $31), below the $25 PSA 9 median, because 17,745 tens are in circulation at an 82% gem rate. Nothing about this card covers a $60 grading fee.",
 "chase-2021-prizm-337": "Fails at any gem rate: a $60 PSA 10 nets about $42 against a $73 all-in, so a hit loses about $32 and a miss about $61. 27 PSA 10 sales in 90 days ($44 to $126, latest $64); the PSA 9 median is $17 on 24 sales. Half the pop is a 10, which keeps the 10 cheap.",
 "taylor-2020-prizm-332": "Fails at any gem rate: a $38 PSA 10 nets about $26 against a $71 all-in. 29 PSA 10 sales in 90 days ($17 to $146, median $38). The PSA 9 is $15. Not a grading card at these prices.",
}
write_notes("psa-15.json", LEAD, CLOSE, "Oct 14")
