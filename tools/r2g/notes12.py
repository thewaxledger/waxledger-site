"""Notes for the psa-12.json batch (Oct 12): young baseball players (Misiorowski, Schlittler, Rice, Caminero,
De Paula, Roman Anthony), rookie cards and 1st Bowman Chrome. 2026 Topps Chrome Misiorowski #196 and Schlittler
#262 were pulled and left off: PSA has graded one copy between them. Caminero 2024 Topps Chrome Update #USC193
(pop 51), Kristian Campbell 2025 Topps Chrome #171 and Dylan Crews 2025 Topps Chrome #146 (2 PSA 10 sales each)
were left off for the same reason. Usage: python3 notes12.py
"""
from r2gnotes import write_notes
LEAD = {
 "misi-2026-t-10": "2026 Topps Series 1 base rookie, the paper flagship card. Misiorowski debuted for Milwaukee in June 2025, so his rookie cards are 2026 issues.",
 "schl-2026-t-111": "2026 Topps Series 1 base rookie, the paper flagship card. Schlittler debuted for the Yankees in July 2025.",
 "schl-2025-bcp166": "1st Bowman Chrome (2025 Bowman Chrome Prospects). Most sold listings title it 1st Bowman.",
 "depaula-2023-bcp111": "1st Bowman Chrome (2023 Bowman Chrome Prospects), Dodgers.",
 "cam-2023-bcp61": "1st Bowman Chrome (2023 Bowman Chrome Prospects), the most-traded Caminero PSA 10 by far.",
 "anthony-2023-bcp71": "1st Bowman Chrome (2023 Bowman Chrome Prospects), Red Sox. Raw price is PSA's tracking of 15 sales; the eBay sample (13 clean sales, $6 median) agrees roughly.",
 "rice-2025-t-337": "2025 Topps Series 1 base rookie, the paper flagship card.",
 "rice-2024-bcp186": "1st Bowman Chrome (2024 Bowman Chrome Prospects), Yankees.",
 "rice-2025-tc-139": "2025 Topps Chrome base rookie.",
 "misi-2022-bdc132": "1st Bowman Chrome (2022 Bowman Draft Chrome #BDC-132).",
}
CLOSE = {
 "misi-2026-t-10": "The best young baseball card in this scan: a $2 raw, a $271 PSA 10 (53 sales in 90 days, $90 to $450, latest $290) and a 61% gem rate against a 21% break-even. About +$59 a try. The grading fee is the whole cost, so this is a volume play: the $57 PSA 9 still loses about $30 on a miss. The 10 is priced on hype for a pitcher with half a season in; sell 10s as they come back rather than holding a stack.",
 "schl-2026-t-111": "Clears, thinner than Misiorowski: a $1.50 raw, a $165 PSA 10 (58 sales, $126 to $240) and a 61% gem rate against a 44% break-even. About +$13 a try. The edge disappears if the PSA 10 drops under about $140.",
 "schl-2025-bcp166": "Clears: a $9 raw, a $209 PSA 10 (44 sales, latest $225) and a 54% gem rate against a 37% break-even. About +$17 a try. The 1st Bowman holds a higher PSA 10 than the paper rookie at a similar gem rate.",
 "depaula-2023-bcp111": "Liquid (75 PSA 10 sales) and a 70% gem rate, but a $120 PSA 10 nets about $84 after fees against a $74 all-in, and the $29 PSA 9 makes every miss a $53 loss. Fails on expected value by about $9. It clears if the PSA 10 holds above about $135.",
 "cam-2023-bcp61": "The most liquid card in the scan (195 PSA 10 sales) and a 71% gem rate, but 3,110 PSA 10s exist and the 10 is an $82 card. Fails on expected value. The same lesson as the high-gem screen: a common 10 does not cover a $60 fee.",
 "anthony-2023-bcp71": "77 PSA 10 sales at $116 and a 46% gem rate. A 10 barely covers the all-in and a miss loses $56. Fails on expected value.",
 "rice-2025-t-337": "20 PSA 10 sales, under the floor, and a 29% gem rate. Fails on liquidity and on expected value.",
 "rice-2024-bcp186": "Four PSA 10 sales in 90 days (one at $1,000). Fails the liquidity floor; the math is a coin flip at a $236 median anyway.",
 "rice-2025-tc-139": "Three PSA 10 sales from a pop of 132. Fails the liquidity floor.",
 "misi-2022-bdc132": "On paper the strongest card here: a $25 raw against a $672 PSA 10 ($525 to $800), and the $106 PSA 9 covers most of the $95 all-in, so the break-even gem rate is 4% against a real 28%. About +$91 a try. It fails only the liquidity floor, 10 PSA 10 sales in 90 days. If you own one raw, grade it.",
}
write_notes("psa-12.json", LEAD, CLOSE, "Oct 12")
