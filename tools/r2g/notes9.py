"""Notes for the psa-9.json batch (Oct 11): the NBA / NHL / MLB scan. Seventeen cards already on the board were
refreshed in place with refresh.py; these are the new ones. Griffey 1989 Upper Deck #1 was pulled and left off the
board: 3% gem with most misses at PSA 8 or lower, which the miss-equals-a-9 model does not price (see the commit).
Usage: python3 notes9.py
"""
from r2gnotes import write_notes

LEAD = {
 "luka-2018-optic-177": "Donruss Optic Rated Rookie, base.",
 "luka-2018-optic-177-holo": "Donruss Optic Rated Rookie Holo, the Optic silver.",
 "hali-2020-prizm-262": "Base Prizm rookie (the Silver is on the board separately).",
 "giannis-2013-hoops-275": "NBA Hoops base rookie, the cheapest Giannis rookie.",
 "tatum-2017-prizm-16-silver": "Silver Prizm rookie.",
 "booker-2015-prizm-308": "Base Prizm rookie.",
 "booker-2015-prizm-308-silver": "Silver Prizm rookie.",
 "mackinnon-2013-ud-238": "Young Guns rookie (Series 1).",
 "crosby-2005-ud-201": "Young Guns rookie, the modern hockey card. Beware reprints: eBay 'raw' listings under $100 are copies, and were excluded from the raw price here.",
 "ovechkin-2005-ud-443": "Young Guns rookie (Series 2).",
 "draisaitl-2014-ud-223": "Young Guns rookie (Series 1).",
 "qhughes-2019-ud-249": "Young Guns rookie (Series 1). 59% gem.",
 "trout-2011-bcd-101": "Bowman Chrome Draft rookie (#101), the chrome counterpart of the Topps Update rookie on the board. Raw price is PSA's tracking of 15 sales; no clean eBay raw sample came back, so treat it as a guide.",
 "bazzana-2024-bdc1": "1st Bowman Chrome (Bowman Draft), the No. 1 pick card of the 2024 draft.",
 "mhj-2024-prizm-silver": "Silver Prizm rookie.",
 "nabers-2024-prizm-silver": "Silver Prizm rookie.",
}
CLOSE = {
 "luka-2018-optic-177": "Liquid (98 PSA 10 sales in 90 days) but a $130 PSA 10 at a 40% gem rate against a $45 PSA 9 cannot cover the $100 all-in. Fails on expected value. Skip; the Prizm base on the board is the same story with better numbers.",
 "luka-2018-optic-177-holo": "The math clears (a $909 PSA 10, a $260 PSA 9, 33% gem against a 22% break-even, about +$48 a try), but PSA tracked five PSA 10 sales in 90 days from a pop of 383. Fails the liquidity floor. If you own one raw, grade it; do not buy to grade.",
 "hali-2020-prizm-262": "A $55 PSA 10 cannot cover the fee. Fails. Skip.",
 "giannis-2013-hoops-275": "A $173 PSA 10 at 48% gem against a $70 PSA 9 and a $34 raw: expected value –$19. Fails on expected value. Clears at a raw under $18, which is below where it trades.",
 "tatum-2017-prizm-16-silver": "Clears on paper: 55% gem against a 35% break-even, a $283 PSA 9 that holds a miss to about –$111, expected value +$64. Eighteen PSA 10 sales in 90 days is under the floor, and the raw sample is thin (3 clean eBay sales around $250 to $280). Fails the liquidity floor; a candidate if the 10 trades weekly.",
 "booker-2015-prizm-308": "A $99 PSA 10 at 44% gem cannot cover the $95 all-in. Fails. Skip.",
 "booker-2015-prizm-308-silver": "Seven PSA 10 sales in 90 days from a pop of 245 and a thin raw market (4 PSA-tracked sales). The math is a coin flip (+$20). Fails the liquidity floor. Skip.",
 "mackinnon-2013-ud-238": "A $1,050 PSA 10 (30 sales in 90 days), a $349 PSA 9 that holds a miss to about –$135, and 49% gem against a 24% break-even. $370 all-in, expected value +$122. Grade it. Raw trades at $300 on eBay (30 sales); the edge is gone above $410.",
 "crosby-2005-ud-201": "The 9 alone covers the all-in ($2,012 PSA 9 against $1,570 in), so the break-even gem rate is 4% and the real rate is 46%: expected value about +$900 a try. It fails only the liquidity count, 17 PSA 10 sales in 90 days, which for a $5,200 card is a real market. The risk is the ticket: a raw Crosby is $1,500 to $1,800 and you need to know it is not one of the many reprints. Grade it if you own one; buy raw only from a seller you trust.",
 "ovechkin-2005-ud-443": "The best new card on the board: a $3,800 PSA 10 (26 sales in 90 days), a $1,302 PSA 9 that covers the $920 all-in on its own, so the break-even gem rate is below zero and the real rate is 30%. Expected value about +$540 a try. Grade it. Raw trades at $850 on eBay (20 sales, $630 to $890 this month); above $1,250 the 9 no longer covers.",
 "draisaitl-2014-ud-223": "Clears on paper (53% gem against a 21% break-even, +$78) but ten PSA 10 sales in 90 days from a pop of 1,158. Fails the liquidity floor. Grade it if you own one.",
 "qhughes-2019-ud-249": "A 59% gem rate and 49 PSA 10 sales in 90 days, but the 10 is $251, the 9 $96, the raw $72: expected value –$10. Fails on expected value, just. Clears at a raw under $60.",
 "trout-2011-bcd-101": "Thirteen PSA 10 sales in 90 days and a $570 median that ranges $95 to $725. The math says +$67 on PSA's $85 raw, which looks low for this card. Fails the liquidity floor. The Topps Update rookie on the board is the liquid version.",
 "bazzana-2024-bdc1": "Ten PSA 10 sales in 90 days at $80 and a 25% gem rate. Fails. Skip.",
 "mhj-2024-prizm-silver": "A $100 PSA 10 at 35% gem against a $20 PSA 9. Fails on expected value. Skip.",
 "nabers-2024-prizm-silver": "A 14% gem rate and a $27 PSA 9 against a $223 PSA 10 that sold 17 times. Fails. Skip.",
}
write_notes("psa-9.json", LEAD, CLOSE, "Oct 11")
