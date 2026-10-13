"""Notes for the psa-13.json batch (Oct 12): rookie autographs and numbered or parallel versions of the board's top
names (Harper, Flagg, Knueppel, Edgecombe, Misiorowski, Crow-Armstrong, Wembanyama). PSA APR + pop, raw from eBay sold
where the sample was clean. Also checked and left off: Wembanyama Prizm Red /299 (13 PSA 10 sales at $14,400 but no PSA 9
sales to price the miss), Mahomes 2017 Prizm Orange /249 (7 PSA 10 sales, one raw sale), Flagg and Harper numbered Topps
Chrome colors (Aqua /199, Teal /299, Magenta /399, Green /99: 0 to 5 PSA 10 sales each), the Topps Chrome auto color
parallels (0 to 2 sales), Flagg Bowman Chrome University autos (no PSA 10 sales). Usage: python3 notes13.py
"""
from r2gnotes import write_notes
LEAD = {
 "harper-auto": "Chrome Rookie Autographs #TCAR-DH, the base (unnumbered) on-card auto from 2025-26 Topps Chrome. Raw is eBay sold ($586 median of 45 sales, $365 to $1,300 for most of them); PSA's own tracking has $531.",
 "flagg-auto": "Chrome Rookie Autographs #TCAR-CF, the base (unnumbered) on-card auto. Raw is eBay sold ($1,775 median of 40 sales, $1,500 to $2,200 in October).",
 "knueppel-auto": "Chrome Rookie Autographs #TCAR-KK, base (unnumbered). Raw $300 on eBay (12 sales, $238 to $550).",
 "harper-252-xfractor": "X-Fractor parallel of the #252 rookie, unnumbered. Raw $70 on eBay (53 sales).",
 "harper-252-pulsar": "Pulsar Refractor parallel of the #252 rookie, unnumbered. Raw $80 on eBay (62 sales). The PSA 9 price is two sales.",
 "harper-252-bball": "Basketball Refractor parallel of the #252 rookie, unnumbered. Raw is PSA's tracking of 15 sales ($75); eBay had two clean sales at $80 and $91. The PSA 9 price is a single sale.",
 "flagg-251-prism": "Prism Refractor parallel of the #251 rookie, unnumbered. Raw $180 on eBay (53 sales).",
 "flagg-251-pulsar": "Pulsar Refractor parallel of the #251 rookie, unnumbered. Raw $175 on eBay (47 sales).",
 "flagg-251-bball": "Basketball Refractor parallel of the #251 rookie, unnumbered. Raw is PSA's tracking ($245, 15 sales); no clean eBay sample came back.",
 "edge-253-bball": "Basketball Refractor parallel of the #253 rookie, unnumbered. Raw is PSA's tracking ($36, 15 sales); one eBay sale at $45.",
 "edge-253-prism": "Prism Refractor parallel of the #253 rookie, unnumbered. Raw $12.50 on eBay (28 sales).",
 "misi-auto": "Chrome Draft Pick Autographs #CDA-JMI, the base (unnumbered) 1st Bowman auto. Raw $975 on eBay (18 sales, $750 to $1,150 since late August); PSA's tracking has $722.",
 "misi-auto-ref": "#CDA-JMI Refractor /499. Raw is two eBay sales, $1,700 (Sep 22) and $1,400 (Oct 7); PSA's own raw tracking shows $405, which is the base refractor with an in-person autograph, not this card.",
 "misi-auto-blue": "#CDA-JMI Blue Refractor /150. Raw is PSA's tracking of five sales ($1,855); eBay had two, $3,104 (Aug 13) and $7,000 (Sep 27), so the raw price is a guess.",
 "pca-cda": "Chrome Draft Picks Autographs #CDA-PC, the base (unnumbered) 1st Bowman auto. Raw $1,200 on eBay (10 sales, $810 to $1,475 since late September); PSA's tracking ($360) is wrong for this card.",
 "pca-cda-ref": "#CDA-PC Refractor /499. Raw $1,200 on eBay (6 sales, $792 to $1,499).",
 "pca-cda-purple": "#CDA-PC Purple Refractor /250. Raw is PSA's tracking of 11 sales ($1,250); one eBay sale at $1,200.",
 "pca-ra": "Topps Chrome Rookie Autographs #RA-PC, the base (unnumbered) rookie auto. Raw $750 on eBay (58 sales, $435 to $700 in October).",
 "pca-ra-ref": "#RA-PC Refractor /499. Raw $911 on eBay (8 sales, $560 to $1,200).",
 "wemby-prizm-green": "Green Prizm parallel of the #136 rookie, the unnumbered retail green. Raw $355 on eBay (45 sales).",
}
CLOSE = {
 "harper-auto": "The 10 is a different card from the 9: $3,000 against $637, with 42 PSA 9 sales to 13 PSA 10s. A 24% gem rate still clears an 11% break-even, so each try is about +$200 on a $656 all-in, with a miss costing about $185. Thin market: 13 PSA 10 sales in 90 days. The pop (103 tens of 435) says this auto gems about one in four; buy the raw clean and centered or the math is the 9's.",
 "flagg-auto": "A 13% gem rate (128 tens of 965 graded) against a 4% break-even: the $2,300 PSA 9 nets more than the $1,845 all-in needs, so a miss costs about $145 and a hit pays about $3,200. About +$300 a try. Thin market: 15 PSA 10 sales in 90 days, $5,500 to $12,000. The raw ticket is the risk, not the grade; most copies come back 9.",
 "knueppel-auto": "The cheapest way into this set of autos: $300 raw, $1,476 PSA 10, and the $458 PSA 9 covers most of the all-in. About +$140 a try at a 25% gem rate. Thin market: 14 PSA 10 sales in 90 days.",
 "harper-252-xfractor": "Clears: a $70 raw, a $635 PSA 10 with 36 sales in 90 days, and a 42% gem rate against an 18% break-even. About +$88 a try; a miss (the $102 PSA 9) costs about $65. The best-volume Harper parallel.",
 "harper-252-pulsar": "A 56% gem rate against a 19% break-even and a $573 PSA 10: about +$113 a try on a $150 all-in. Thin market: 16 PSA 10 sales in 90 days, and the PSA 9 price rests on two sales.",
 "harper-252-bball": "A 47% gem rate and a $510 PSA 10 on a $75 raw: about +$73 a try. Thin market: 11 PSA 10 sales in 90 days, and the PSA 9 price is a single sale.",
 "flagg-251-prism": "Clears: a $180 raw, a $1,262 PSA 10 with 36 sales in 90 days, and a 25% gem rate against a 14% break-even. About +$84 a try, with the $200 PSA 9 limiting a miss to about –$100. Three in four come back 9, so this is a numbers game, not a pick-one.",
 "flagg-251-pulsar": "Clears: a $175 raw, a $760 PSA 10 with 32 sales, 43% gem against a 28% break-even. About +$56 a try; a miss costs about $112. The latest sale printed $560, the low of the range.",
 "flagg-251-bball": "An 19% gem rate (163 tens of 869) is the problem: the break-even is also 19%, so expected value is –$3 on a $315 all-in. Fails. The $1,170 PSA 10 is real, the odds of getting one are not.",
 "edge-253-bball": "A 61% gem rate and a $291 PSA 10 on a $36 raw: about +$31 a try, with the $45 PSA 9 making every miss a $72 loss. Thin market: 22 PSA 10 sales in 90 days, three short of the floor.",
 "edge-253-prism": "A $382 PSA 10 on a $12.50 raw clears on paper (+$10), but a 25% gem rate and nine PSA 10 sales in 90 days. Fails the liquidity floor.",
 "misi-auto": "A $2,904 PSA 10 against a $975 raw, 36% gem, about +$124 a try, but eight PSA 10 sales in 90 days. Fails the liquidity floor, two sales short of the thin-market tier. The $920 PSA 9 holds a miss to about –$364.",
 "misi-auto-ref": "A $4,218 PSA 10 (ten sales, $2,880 to $5,002) against a $1,550 raw and a 44% gem rate: about +$215 a try. Thin market, and the raw price is two sales; treat the number as a range from $1,400 to $1,700.",
 "misi-auto-blue": "The biggest number in this batch: a $6,950 PSA 10 (eight sales, $5,701 to $7,600) at a 59% gem rate, with the one PSA 9 sale ($2,500) covering the all-in. Fails the liquidity floor at eight sales, and the raw price is not known well enough to act on. If you own one, grade it.",
 "pca-cda": "Five PSA 10 sales in 90 days and a $1,200 raw against a $2,310 PSA 10: the math is a wash (–$14). Fails. The Refractor /499 is the version with a market.",
 "pca-cda-ref": "The PSA 9 ($1,912, 31 sales) nets more than the $1,270 all-in, so the break-even gem rate is below zero: a miss pays about +$144 and a hit about +$1,034. Expected value about +$322 at a 20% gem rate. Thin market: 22 PSA 10 sales in 90 days, three short of the floor. The safest grade in this batch if the raw is really $1,200.",
 "pca-cda-purple": "A $3,676 PSA 10 (16 sales, $1,300 to $6,500) at a 39% gem rate against an 11% break-even: about +$382 a try, with the $1,568 PSA 9 holding a miss to about –$160. Thin market: 16 sales, and the PSA 10 range is wide.",
 "pca-ra": "Clears, and liquid: 41 PSA 10 sales in 90 days at $2,000 ($601 to $3,025), a 49% gem rate against a 23% break-even, a $750 raw. About +$191 a try; the $874 PSA 9 holds a miss to about –$173. The best auto on the board by volume.",
 "pca-ra-ref": "A $2,405 PSA 10 on a $911 raw, but a 31% gem rate and a $790 PSA 9 (below the base auto's 9) make the expected value –$64, and there were eight PSA 10 sales. Fails. The base auto is the better buy at this price gap.",
 "wemby-prizm-green": "Clears: a $355 raw, a $1,080 PSA 10 with 75 sales in 90 days, a 52% gem rate against a 35% break-even. About +$86 a try; a miss (the $336 PSA 9) costs about $176. Not numbered, but it is the most liquid Wembanyama parallel after the Silver.",
}
write_notes("psa-13.json", LEAD, CLOSE, "Oct 12")
