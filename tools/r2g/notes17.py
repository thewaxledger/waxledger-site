"""Notes for the psa-17.json batch (Oct 15). Three base Topps Chrome rookies with 25+ PSA 10 sales in 90 days whose
misses mostly come back PSA 9 (the model prices a miss as a 9): 2007-08 Kevin Durant #131, 2003-04 LeBron James #111,
1996-97 Kobe Bryant #138. Raw is eBay sold, titles carrying the card number, graded and refractors excluded.
Checked and left off because most misses grade 8 or lower (the model would overstate the miss value, per the Oct 14
rule): 2003-04 Topps LeBron James #221 (102 PSA 10 sales, but 56% of the non-10 pop is PSA 8 or lower) and 1996-97
Topps Kobe Bryant #138 (220 sales, 50% of misses are 8 or lower). Also checked, under 25 PSA 10 sales: 2018 Prizm
Saquon Barkley #202 (19), 2023 Prizm Puka Nacua #357 (23), 2024-25 Prizm Stephon Castle #234 (9), 2025 Donruss Cam
Ward #350 (9) and Travis Hunter #301 (2), 2025 Topps Chrome Dylan Crews #146 (2), 2022-23 Prizm Jalen Williams #246
(4), 2024 Prizm WNBA Angel Reese #147 (2), 2009-10 Topps Stephen Curry #321 (10). 2001 Upper Deck Golf Tiger Woods #1
has 228 PSA 10 sales but would add a fifth sport to the board (Aidan's call).
Usage: python3 notes17.py
"""
from r2gnotes import write_notes
LEAD = {
 "durant-2007-tc-131": "Base Topps Chrome rookie, the Chrome version of his flagship RC. Raw $143 on eBay (20 sales in 30 days, $74 to $349; most $100 to $220).",
 "lebron-2003-tc-111": "Base Topps Chrome rookie. Raw $3,038 on eBay (10 sales in 30 days, $2,275 to $4,600); condition drives that range and a raw copy at the low end is usually one a grader would not send.",
 "kobe-1996-tc-138": "Base Topps Chrome rookie. Raw $1,975 on eBay (11 sales in 30 days, $1,200 to $4,350); the spread is condition, so the median assumes a copy with clean edges and no chrome scratches.",
}
CLOSE = {
 "durant-2007-tc-131": "Clears because the PSA 9 alone covers the cost: a $391 nine nets about $289 against a $213 all-in, and the $1,415 ten nets about $985. 45 PSA 10 sales in 90 days ($825 to $1,700, latest $1,700). 25% of the pop is a 10 and 54% is a 9, so three attempts in four come back a profitable 9; the risk is an 8 (15% of the pop), which sells for less than the raw price.",
 "lebron-2003-tc-111": "Clears on the PSA 9: a $4,550 nine nets about $3,365 against a $3,108 all-in, and the $14,850 ten nets about $10,336. 63 PSA 10 sales in 90 days ($12,600 to $20,000, latest $12,600). 22% of the pop is a 10, 45% a 9 and 23% an 8; an 8 is the loss case, so this is a card to grade only from a copy that has been checked under magnification. Big ticket: $3,100 per attempt.",
 "kobe-1996-tc-138": "Clears on the PSA 9 by a wide margin: a $4,500 nine nets about $3,328 against a $2,045 all-in, and the $15,873 ten nets about $11,047. 29 PSA 10 sales in 90 days ($12,000 to $27,500, latest $15,600), the thinnest volume of the three. Only 12% of the pop is a 10 and 60% is a 9, so this is a bet on the 9, not the 10. Big ticket: $2,000 per attempt.",
}
write_notes("psa-17.json", LEAD, CLOSE, "Oct 15")
