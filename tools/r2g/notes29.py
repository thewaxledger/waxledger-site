"""Notes for the psa-29.json batch (Nov 12): 20 new cards from a wide candidate search Aidan asked for (about 580
search terms across basketball, football, baseball, hockey and soccer; PSA price summary first, pop for anything with
20+ PSA 10 sales at $70+, then eBay sold for the raw price and a full PSA pull for the ones with headroom).
18 clear as Grade and 2 as Thin market (Yamal 2024 Topps Chrome Euro #17, 23 PSA 10 sales; Iverson 1996-97 Topps
Chrome #171, 24). Every raw price is an eBay sold median of the last 45 days read Nov 12 (rawSrc), not PSA's tracking;
PSA 10 prices for the soccer cards, Wade, Giannis and the three 2025-26 Topps Chrome Refractors were cross-checked on
eBay sold PSA 10 listings the same day and matched.
Older cards (1996 to 2003, and the 2012 and 2014 Prizm) have 9% to 24% of their PSA pop at 8 or lower; the model prices
every miss as a 9, so each of those notes carries a stress line (sub-9 grades valued at 40% of a 9). None of them is in
the blind-spot group CLAUDE.md describes (most misses 8 or lower): in every case the 9 is the most common miss.
Checked and left off, eBay raw above the price the model needs (Nov 12): Kawhi Leonard 2012 Prizm #209 1946623 (raw
$42 vs $34), Kyrie Irving 2012 Prizm #201 1911317, Anthony Edwards 2020 Optic Holo 5782978 ($54 vs $47), Caitlin Clark
2024 Select WNBA #72 Silver 12139956 ($56 vs $55), McCaffrey 2017 Prizm Silver 2491096 ($44 vs $30), Purdy 2022 Optic
Holo 8878734 ($65 vs $39), Maye 2024 Optic Holo 13214396 ($35 vs $30), Caleb Williams 2024 Optic Holo 13214368 ($50 vs
$34), Kelce 2013 Topps Chrome #118 2131138 ($25 vs $23), Acuna 2018 Topps Chrome Refractor 2618711, Judge 2013 Bowman
Chrome Draft BDPP19 2048541 (24 sales, raw $230 vs $240: marginal). Blind-spot cards seen and left off: Kobe 1996 Topps
#138, Hoops #281, Upper Deck #58, SP #134, Collector's Choice #267, Skybox Premium #55; Jordan 1988 to 1990 Fleer and
1989 Hoops; Shaq 1992; Jeter 1993 Topps; Curry 2009 Upper Deck #234 (36% of the pop at 8 or lower against 38% nines).
Ohtani 2018 Bowman Chrome #1 2641967 returned a $5,504 PSA 10 average that does not look like the base card; not used.
Hockey Young Guns did not resolve through the pop search (it returns Young Guns Renewed inserts); search by card number.
Usage: python3 notes29.py
"""
import json, os
from r2gnotes import write_notes, A, money, signed, pct
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "psa-29.json")))

LEAD = {
 "curry-2012-prizm-72": "His base card in the first Prizm set (2012-13), not a rookie; the most traded Curry Prizm in PSA 10.",
 "lebron-2012-prizm-1": "Card #1 of the first Prizm set (2012-13, Heat), not a rookie.",
 "kobe-2012-prizm-24": "His base card in the first Prizm set (2012-13), not a rookie.",
 "wemby-2025-tc-221-refractor": "Third-year card, the unnumbered Refractor from the first Topps Chrome set under the NBA licence Topps took over from Panini.",
 "curry-2025-tc-201-refractor": "Veteran card, the unnumbered Refractor from the first Topps Chrome set under the NBA licence Topps took over from Panini.",
 "lebron-2025-tc-127-refractor": "Veteran card, the unnumbered Refractor from the first Topps Chrome set under the NBA licence Topps took over from Panini.",
 "duncan-1997-tc-115": "His Topps Chrome rookie (1997-98), base, not the Refractor.",
 "wade-2003-tc-115": "His Topps Chrome rookie (2003-04), base, not the Refractor; the same set as the LeBron #111 on the board.",
 "jsn-2023-prizm-390-silver": "Silver Prizm rookie (Seahawks).",
 "allen-2018-donruss-304": "Rated Rookie from the paper Donruss set, the cheapest of his three main rookies and by far the most traded: 332 PSA 10 sales in 90 days.",
 "haaland-2019-tc-ucl-74": "His first Topps Chrome card (2019-20 UEFA Champions League), the card the market treats as his rookie.",
 "messi-2022-prizm-wc-7": "Base Prizm from the 2022 World Cup set (Argentina), the tournament he won; not a rookie.",
 "ronaldo-2014-prizm-wc-161": "His first Prizm card (2014 World Cup, Portugal), not a rookie; the companion to the Messi #12 on the board.",
 "manning-1998-tc-165": "His Topps Chrome rookie (1998), base, not the Refractor.",
 "kobe-1996-finest-74": "His Finest rookie (1996-97, #74), base, not the Refractor.",
 "kobe-1996-bowmans-best-r23": "His Bowman's Best rookie (1996-97, #R23), base, not the Refractor or Atomic Refractor.",
 "giannis-2013-select-178": "His Select rookie (2013-14), base, not a Prizm parallel.",
 "judge-2017-tcu-hmt50": "Rookie Debut card from 2017 Topps Chrome Update, the retail-only set; his base rookie in that set family is on the board as #169 (Chrome) and US99 (Update).",
 "yamal-2024-tc-euro-17": "His Spain card from 2024 Topps Chrome UEFA Euro; the 2023-24 Topps Chrome UCC #64 on the board is the one the market treats as his rookie.",
 "iverson-1996-tc-171": "His Topps Chrome rookie (1996-97), base, not the Refractor; the same set as the Kobe #138 on the board.",
}
TAIL = {
 "curry-2012-prizm-72": "The dearest raw card of this batch at $330, and only 7 raw sales in the window, so check the copy closely before paying it.",
 "lebron-2012-prizm-1": "A 9 covers the cost here, so the risk is a grade of 8 or lower, not a miss at 9.",
 "kobe-2012-prizm-24": "A 9 covers the cost here, so the risk is a grade of 8 or lower, not a miss at 9.",
 "wemby-2025-tc-221-refractor": "The gap between a $45 raw card and a $568 ten is unusually wide and the card is new; raw copies on eBay have often been passed over for grading, so buy only copies you have looked at for centring and surface.",
 "curry-2025-tc-201-refractor": "The gap between a $78 raw card and a $790 ten is unusually wide and the card is new; raw copies on eBay have often been passed over for grading, so buy only copies you have looked at for centring and surface.",
 "lebron-2025-tc-127-refractor": "The gap between a $68 raw card and an $820 ten is unusually wide and the card is new; raw copies on eBay have often been passed over for grading, so buy only copies you have looked at for centring and surface.",
 "duncan-1997-tc-115": "Raw copies ran $57 to $250 in the window; condition drives that spread, and early Chrome often shows greening and surface wear that cap the grade.",
 "wade-2003-tc-115": "Raw copies ran $20 to $120; the cheap ones are usually off-centre.",
 "jsn-2023-prizm-390-silver": "The 10 has climbed with his season (latest $420 against a $308 median) and raw has followed, from about $40 over the summer to $45 to $55 now; the verdict holds up to a raw price of about $52.",
 "allen-2018-donruss-304": "The thinnest pass of the batch: the verdict holds up to a raw price of about $170, and raw copies sold from $60 to $415.",
 "haaland-2019-tc-ucl-74": "17 raw sales in the window, $68 to $124.",
 "messi-2022-prizm-wc-7": "A $15 raw card, so the grading fee is most of the cost; World Cup demand in 2026 is part of the 10's price.",
 "ronaldo-2014-prizm-wc-161": "Gem rate is 26%, so three of four come back short; the 9 nearly covers the cost.",
 "manning-1998-tc-165": "19% gem: four of five come back short, and the pass rests on a 9 nearly covering the $335 all-in. Raw copies ran $87 to $700.",
 "kobe-1996-finest-74": "Only 5 raw sales in the window ($175 to $207), so the raw price is a small sample.",
 "kobe-1996-bowmans-best-r23": "14% gem, the lowest of the batch: six of seven come back short and the pass rests on a $275 nine covering the $202 all-in.",
 "giannis-2013-select-178": "Only 5 raw sales in the window ($53 to $125), so the raw price is a small sample; 27 PSA 10 sales is just over the floor.",
 "judge-2017-tcu-hmt50": "81% gem is the highest of the batch; the verdict holds up to a raw price of about $125.",
 "yamal-2024-tc-euro-17": "23 PSA 10 sales in 90 days, two short of the floor, so it shows as a Thin market.",
 "iverson-1996-tc-171": "24 PSA 10 sales in 90 days, one short of the floor, so it shows as a Thin market. 16% gem.",
}
CLOSE = {}
for key, d in D.items():
    p10, p9, raw = d["med10"], d["med9"], d["rawMed"]
    gem = d["pop10"] / d["popTotal"]; fee = A["feeHigh"] if p10 > A["feeCap"] else A["fee"]
    allIn = raw + fee + A["ship"]; net10 = p10 * (1 - A["haircut"]) * (1 - A["sellFee"]); netMiss = p9 * A["missReal"] * (1 - A["sellFee"])
    ev = gem * net10 + (1 - gem) * netMiss - allIn; be = (allIn - netMiss) / (net10 - netMiss)
    nine = f"a {money(p9)} nine " + (f"clears it by about {money(netMiss - allIn)}" if netMiss >= allIn else f"loses about {money(allIn - netMiss)}")
    bet = "a break-even near 0%" if be <= 0.005 else f"a {pct(be)} break-even"
    head = "Thin market, passes on value" if d["n10"] < A["minSales"] else "Grades"
    txt = f"{head}: a {money(p10)} PSA 10 nets about {money(net10 - allIn)} over the {money(allIn)} all-in, {nine}, and {pct(gem)} gem against {bet} gives {signed(ev)} expected value."
    low = (d["popTotal"] - d["pop10"] - d["pop9"]) / d["popTotal"]
    if low >= 0.09:
        stress = gem * net10 + (d["pop9"] / d["popTotal"]) * netMiss + low * 0.4 * netMiss - allIn
        txt += f" {pct(low)} of the PSA pop is an 8 or lower and the model prices every miss as a 9; with those valued at 40% of a 9 the expected value is {signed(stress)}."
    CLOSE[key] = txt + " " + TAIL[key]
if __name__ == "__main__":
    write_notes("psa-29.json", LEAD, CLOSE, "Nov 12")
