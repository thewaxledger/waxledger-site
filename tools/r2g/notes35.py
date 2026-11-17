"""Notes for the psa-35.json batch (Nov 17, second run): four cards from a pane screen of 24 pop-report terms
(getPriceSummary first, full pulls for the ones with 20+ PSA 10 sales in 90 days). Raw is eBay sold read Nov 17 in
the pane (last 45 days, plain parallel only; graded, numbered, lots and breaks excluded by title); PSA's own raw
tracking is kept in the pull as rawPsa.
One clears as Grade: Cooper Flagg 2025-26 Topps Chrome #251 X-Fractor (141 PSA 10 sales, $710 median, 43% gem, raw
$155.50 on 31 eBay sales, +$71). Fernando Mendoza 2025 Bowman University Chrome #109 base is marginal (108 sales,
$125, 45% gem against a 45% break-even, raw $5.50 on 99), Neymar 2014 Prizm World Cup #112 fails on value (35 sales,
$89, 19% gem, raw $8) and Paul Skenes 2024 Topps Chrome Update USC88 Refractor is a thin market (20 sales, $188,
44% gem, raw $19, +$3).
Screened and left off (PSA 10 sales in 90 days): the Silver Prizms of Jokic 2015 #335 2392418 (5), Giannis 2013 #290
2110454 (4), Lillard 2012 #245 1919845 (1), Jaylen Brown 2016 #44 2394100 (14, $470), Josh Allen 2018 #205 2670023
(1), Saquon 2018 #202 2656063 (0), CeeDee Lamb 2020 #334 4064155 (1); Kyler Murray 2019 Prizm #301 Silver 2872228
(17 sales at a $504 median but the two latest 10s sold for $91 and $102, and three raw sales in 45 days: pulled, left
off); Embiid 2014 Prizm #253 Prizm 2421882 (8); Harden 2012 Prizm #95 2770681 (5); Scottie Barnes 2021 Prizm #320
7119094 (15, $41); Nabers 2024 Prizm #370 base 12496739 (8); Eli Willits 2025 Bowman Draft BDC-1 15205927 (3);
Josuar Gonzalez 2025 BCP153 base 14520189 (not screened: the search returned parallels first); Yordan Alvarez has no
2019 Topps Chrome Update spec (his Chrome Update card is 2020 U53 4292469); Dylan Crews does not resolve through the
pop search. Flagg's 2025 Panini Instant Rated Rookie Retro RRR-16 14676506 had 50 PSA 10 sales at $76 (not pulled;
an Instant print-to-order card). Usage: python3 notes35.py
"""
from r2gnotes import write_notes

LEAD = {
 "flagg-2025-tc-251-xfractor": "The X-Fractor of his Topps Chrome rookie, the unnumbered hobby parallel that sellers title as a Refractor variant; the base, Refractor, Prism, Pulsar and Basketball Refractor #251 are all on the board. The deepest PSA 10 market of the five Flagg #251 parallels: 141 sales in 90 days.",
 "mendoza-2025-bu-chrome-109": "His 1st Bowman, the base Bowman University Chrome card (college, Indiana); the Sapphire #109 is on the board as a thin market. Named the Raiders' starter on Nov 12 and made his first start Nov 16 at Seattle.",
 "neymar-2014-prizm-wc-112": "Base Prizm from the 2014 World Cup set (Brazil), the first Prizm soccer set; the Messi #12 and Ronaldo #161 from the same set are on the board.",
 "skenes-2024-tcu-usc88-refractor": "The unnumbered Refractor of his Topps Chrome Update rookie (the base USC88 is on the board and fails on value).",
}
CLOSE = {
 "flagg-2025-tc-251-xfractor": "A $710 ten on 141 sales against a $225 all-in: a 10 nets about +$268, a 9 loses $76, expected value +$71 with a 43% gem rate clearing the 22% break-even by 21 points. Two cautions: the 10 is sliding (latest $630, the 90-day average $732) and so is the raw (the newest eBay sales $73 to $130 against the $155.50 45-day median; PSA's own tracking has $121.50 on its last 15). The Standard fee applies because the 10 is over $500. Grade, and buy raw at the newer prices, not the median.",
 "mendoza-2025-bu-chrome-109": "A $5.50 card with a $125 ten on 108 sales: a 10 nets +$32, a 9 loses $26, and a 45% gem rate lands on the 45% break-even, so the expected value is $0. Marginal by the model, and the cheapest Mendoza card to send if a copy is pack-fresh and centred; 1,798 graded with 813 tens says plenty of people are trying.",
 "neymar-2014-prizm-wc-112": "An $89 ten on 35 sales and an $8 raw, but only 19% of 4,805 graded copies are a 10 (62% are a 9, 13% an 8 or lower): the expected value is –$28 on a $58 all-in and the break-even gem rate is 90%. Fails on expected value. Skip; the Messi #12 from the same set clears because its 10 is $499 on 104 sales.",
 "skenes-2024-tcu-usc88-refractor": "A $19 raw and a $188 ten on 20 sales: a 10 nets +$62, a 9 loses $43, and a 44% gem rate clears the 41% break-even by three points, expected value +$3. Twenty PSA 10 sales in 90 days is a thin market, the latest 10 sold for $134 (Nov 9), and the margin is three points of gem rate. Thin market: not worth sending in bulk; the base USC88 fails outright.",
}
write_notes("psa-35.json", LEAD, CLOSE, "Nov 17")
