"""Notes for the psa-27.json batch (Nov 2): Bowman Sapphire (baseball and Bowman University football) plus more rookies,
at Aidan's request. 56 cards pulled; 11 have 10+ PSA 10 sales in 90 days and go on the board. Raw prices for the five
priciest Sapphire cards are eBay sold medians (raw base Sapphire titled with the card number, graded and colour copies
excluded); PSA's own raw tracking is kept as rawPsa.
Sapphire, checked and left off for volume (PSA 10 sales in 90 days / gem rate): 2025 Bowman Sapphire Griffin BCP86
13742259 (0 / 9%), Made BCP50 13742223 (2 / 16%), De Vries BCP59 (0), 2024 Chrome Sapphire De Vries 179 12387676
(3 / 22%), 2025 Chrome Sapphire Josuar Gonzalez 153 14694016 (0) and Elian Pena 155 14694018 (6 / 82%), 2023 Chrome
Sapphire Salas 171 SP 10016661 (4), 2025 Bowman Draft Sapphire Willits 15409162 (2 / 22%) and Hernandez 15409186
(2 / 34%), 2024 Draft Sapphire Bazzana 12638054 (1 / 23%), Kurtz 12638109 (3 / 20%), Jenkins 12638219 (2), 2023 Draft
Sapphire Skenes 10279529 (2 / 22%, $486 ten), 2020 Draft Sapphire Witt BD152 6252588 (3, $230). Bowman University
Chrome Sapphire: Underwood 196 (6), Dante Moore 137 (6), Jeanty 17 (8, 84% gem), Love 2024 #100 12600544 (7, $135),
Hunter 2023 #36 (5), Caleb Williams 2023 #1 (3). 2026 Bowman Sapphire and Chrome Sapphire Griffin/Made specs exist
but have no recorded sales yet.
Rookies left off: Witt 2020 BD152 Chrome 4120534 (2), Rutschman 2023 TCU USC1 9970661 (0), Dominguez 2024 TC #89 (8,
$13 ten), Evan Carter 2024 TC #136 (0), Jacob Wilson 2025 TCU USC150 15000028 (1), Cam Smith 2025 TCU #19 (1),
Castle 2024-25 Topps Chrome #122 (1), Risacher #169 and Sarr #136 (0), McConkey 2024 Prizm #365 (9, $27), Achane
2023 Prizm #365 (5). Young Guns searches for Cooley, Luke Hughes, Johnston and Caufield only surfaced inserts; their
base Young Guns specs still need finding.
Usage: python3 notes27.py
"""
from r2gnotes import write_notes
LEAD = {
 "sap-mcgonigle-2025": "Sapphire Edition of his 2025 Bowman Chrome prospect card (June 2025 Bowman Sapphire); his 1st Bowman is 2023 Bowman Draft. Raw $64.50 median of 21 eBay sales since Sep 3 ($34 to $90).",
 "sap-caminero-2023": "Sapphire Edition of his 1st Bowman Chrome (2023 Bowman Sapphire). Raw $82 median of 10 eBay sales since Aug 20 ($20 to $175).",
 "sap-anthony-2023": "Sapphire Edition of his 1st Bowman Chrome (2023 Bowman Sapphire). Raw $80 median of 13 eBay sales since Aug 4 ($31 to $400); not the 2023 Chrome Sapphire BCP-220, which sells for $5 to $12.",
 "sap-wood-2022": "Sapphire Edition of his 1st Bowman Chrome (2022 Bowman Sapphire). Raw $23.50 median of 15 PSA-tracked sales ($16.50 to $40).",
 "sap-griffin-2024d": "Sapphire Edition of his 1st Bowman Chrome (2024 Bowman Draft Sapphire), the Pirates' 2024 first-rounder, called up April 2026. Raw $100 median of 13 eBay sales since Sep 2 ($82 to $380).",
 "sap-clark-2023d": "Sapphire Edition of his 1st Bowman Chrome (2023 Bowman Draft Sapphire). Raw $45 median of 15 PSA-tracked sales ($22.50 to $101).",
 "sapu-mendoza-2025": "Bowman University Chrome Sapphire (college, Indiana), the 2026 No. 1 pick's pre-NFL Sapphire. Raw $45 median of 9 eBay sales since Sep 3 ($22 to $90).",
 "rk-gunnar-2019bdc": "1st Bowman Chrome base (2019 Bowman Draft). Raw $2.36 median of 15 PSA-tracked sales ($0.99 to $19.99).",
 "rk-carroll-2019bdc": "1st Bowman Chrome base (2019 Bowman Draft). Raw $2.25 median of 15 PSA-tracked sales ($1.25 to $7.70).",
 "rk-julio-2022tcu": "Topps Chrome Update base rookie, his main Chrome RC (the #222 on the board is the short-print photo variation). Raw $1.25 median of 15 PSA-tracked sales ($0.70 to $2.49).",
 "rk-saquon-2018prizm": "Base Prizm rookie. Raw $8 median of 15 PSA-tracked sales ($4.50 to $17.50).",
}
CLOSE = {
 "sap-mcgonigle-2025": "Thin market but profitable: a $322 PSA 10 nets about $110 over the $114 all-in, a $99 nine loses about $41, and 40% gem against a 27% break-even gives +$19 expected value. 12 PSA 10 sales in 90 days (median $322, range $290 to $400). The 9 holds $99 because Sapphire is short-printed, which is what makes the miss survivable. Buy raw under $70; McGonigle was Baseball America's Rookie of the Year.",
 "sap-caminero-2023": "Fails on expected value: a $200 PSA 10 nets about $7 over the $132 all-in, a $64 nine loses about $85, and 73% gem against a 93% break-even gives -$18. 46 PSA 10 sales in 90 days (median $200, latest $132). Clears only on a raw copy under $65.",
 "sap-anthony-2023": "Fails: profitable at PSA's tracked raw price, but at the $80 eBay median it loses $16 expected (31% gem against a 45% break-even), and only 10 PSA 10 sales in 90 days (median $282, latest $189). Clears on a raw copy under $65.",
 "sap-wood-2022": "Fails at any gem rate: a $96 PSA 10 nets about $67 against a $73 all-in, so even a hit loses about $6. 29 PSA 10 sales in 90 days (median $96.50, latest $113.50) and 983 tens in circulation at 67% gem. Buy the slab.",
 "sap-griffin-2024d": "Thin market but profitable: a $328 PSA 10 nets about $78 over the $150 all-in, a $115 nine loses about $65, and 53% gem against a 46% break-even gives +$10 expected value. 22 PSA 10 sales in 90 days (median $328, latest $370). The margin is seven points, so a centering pre-screen decides it. Buy raw at $100 or less.",
 "sap-clark-2023d": "Fails at any gem rate: a $121 PSA 10 nets about $84 against a $95 all-in, so even a hit loses about $11. 31 PSA 10 sales in 90 days (median $121, range $72 to $200), 75% gem. Buy the slab.",
 "sapu-mendoza-2025": "Thin market but profitable: a $260 PSA 10 nets about $86 over the $95 all-in, a $70 nine loses about $43, and 53% gem against a 33% break-even gives +$25 expected value. 12 PSA 10 sales in 90 days (median $260, latest $300). A college card of the 2026 No. 1 pick, who is still the Raiders' backup: the price moves with whether he starts.",
 "rk-gunnar-2019bdc": "Fails at any gem rate: a $35 PSA 10 nets about $24 against a $52 all-in. 38 PSA 10 sales in 90 days and 2,377 tens in circulation at 77% gem. Buy the slab.",
 "rk-carroll-2019bdc": "Fails at any gem rate: a $38 PSA 10 nets about $26 against a $52 all-in. 28 PSA 10 sales in 90 days and 2,017 tens in circulation at 68% gem. Buy the slab.",
 "rk-julio-2022tcu": "Fails on volume and value: 17 PSA 10 sales in 90 days at a $39 median, and the 10 nets about $27 against a $51 all-in. Buy the slab.",
 "rk-saquon-2018prizm": "Fails on volume and value: 19 PSA 10 sales in 90 days at an $80 median, and 39% gem against a 107% break-even. A hit loses about $3 at the $40 fee. Buy the slab.",
}
write_notes("psa-27.json", LEAD, CLOSE, "Nov 2")
