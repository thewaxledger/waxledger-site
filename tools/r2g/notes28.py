"""Notes for the psa-28.json batch (Nov 3): the ten oldest board cards refreshed in place (refresh.py) plus four new
cards with real PSA 10 volume: Yamal 2023-24 Topps Chrome UCC #64, Messi 2014 Prizm World Cup #12, Mbappé 2018 Prizm
World Cup #80 (the board's first soccer cards) and Bueckers 2025 Prizm WNBA #5. Yamal's raw is an eBay sold median
(108 sales, cross-checked against PSA's $42); Messi's and Mbappé's raw prices are PSA's own tracking because the browser
pane dropped before the eBay check, and the notes say so.
Pulled and left off: LeBron 2003 Topps #221 (295776; 100 PSA 10 sales at $6,301, 11% gem, but 28% of the pop is a PSA 8
and the model prices every miss as a 9, the blind spot noted in CLAUDE.md; Aidan's call), Dybantsa 2025 Bowman
University Best #9 (16151661; released Oct 30, no graded sale yet, pop 9), Bueckers 2025 Prizm WNBA #147 (15174027;
15 PSA 10 sales at $120, 20% gem; the second Bueckers card in the base set), Angel Reese 2024 Prizm WNBA #10
(12860608; one PSA 10 sale).
Usage: python3 notes28.py
"""
from r2gnotes import write_notes
LEAD = {
 "yamal-2023-tc-ucc-64": "His first Topps Chrome card (2023-24 UEFA Club Competitions, Barcelona), the card the market treats as his rookie. The board's first soccer card. Raw $43.95 median of 108 eBay sales since Aug 10, base #64 only (graded copies and parallels excluded); PSA's own raw tracking shows $42 on 15 sales.",
 "messi-2014-prizm-wc-12": "His first Prizm card (2014 World Cup, Argentina), not a rookie card; the most traded Messi card in PSA 10. Raw $50 median of 15 PSA-tracked sales ($14 to $92), not yet cross-checked on eBay.",
 "mbappe-2018-prizm-wc-80": "His Prizm rookie (2018 World Cup, France). Raw $46.67 median of 15 PSA-tracked sales ($28 to $74), not yet cross-checked on eBay; at a $70 raw price the verdict would be marginal.",
 "bueckers-2025-prizm-wnba-5": "Base Prizm rookie (Dallas Wings), the 2025 No. 1 pick; the set also carries her at #147, which has fewer sales (15 PSA 10s at $120). Raw $1.59 median of 15 PSA-tracked sales ($0.99 to $100).",
}
CLOSE = {
 "yamal-2023-tc-ucc-64": "Grades: a $460 PSA 10 nets about $226 over the $94 all-in, a $101 nine loses about $19, and 39% gem against an 8% break-even gives +$76 expected value, one of the widest margins on the board. 135 PSA 10 sales in 90 days (median $460, range $140 to $746, latest $426), 120 PSA 9 sales. The 9 holding $101 is what makes it safe: the miss costs less than the fee.",
 "messi-2014-prizm-wc-12": "Grades: a $499 PSA 10 nets about $247 over the $100 all-in, a $112 nine loses about $17, and 35% gem against a 6% break-even gives +$75 expected value. 104 PSA 10 sales in 90 days (median $499, range $299 to $650, latest $600), 91 PSA 9 sales. Only 7% of the pop is a PSA 8, so the model's 9-priced miss is close to right here; a 2014 card still needs a centering check before the fee.",
 "mbappe-2018-prizm-wc-80": "Grades on PSA's raw price: a $269 PSA 10 nets about $91 over the $97 all-in, a $79 nine loses about $38, and 46% gem against a 30% break-even gives +$21 expected value. 65 PSA 10 sales in 90 days (median $269, range $194 to $399, latest $240), 87 PSA 9 sales. The margin is 16 points, so the verdict survives a raw price up to about $65; above that it is marginal, and eBay has not been checked yet.",
 "bueckers-2025-prizm-wnba-5": "Fails on value: an $80 PSA 10 nets about $4 over the $52 all-in, a $19 nine loses about $38, and 32% gem against a 90% break-even gives –$24 expected value. 35 PSA 10 sales in 90 days (median $80, range $52 to $120, latest $59) and the 10 has slipped through October. Buy the slab, or hold the raw card for a dollar.",
}
write_notes("psa-28.json", LEAD, CLOSE, "Nov 3")
