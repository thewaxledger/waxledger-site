"""Write notes.json entries for the psa-6.json batch (flagship QB rookies: Silver Prizms, Optic Holos, Rated Rookies).
The numbers are generated from psa-6.json with the site model; the lead and closing sentences are written per card.
Usage: python3 notes5.py   (idempotent: rewrites the keys listed in LEAD)
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
A = dict(fee=59.99, ship=10, sellFee=.13, haircut=.20, missReal=.85, assumedGem=.35, minSales=25, minMargin=.10)
D = json.load(open(os.path.join(HERE, "psa-6.json")))
N = json.load(open(os.path.join(HERE, "notes.json")))

def money(x, dec=0):
    if x is None: return "n/a"
    s = f"{abs(x):,.{dec}f}"
    return ("–$" if x < 0 else "$") + s
def signed(x):
    return ("+$" if x >= 0 else "–$") + f"{abs(x):,.0f}"
def pct(x): return f"{x*100:.0f}%"

LEAD = {
 "mahomes-2017-prizm-269-silver": "Silver Prizm rookie, the chase version of the flagship Mahomes card. PSA lists it as '#269 Prizm'.",
 "burrow-2020-prizm-307-silver": "Silver Prizm rookie.",
 "herbert-2020-prizm-325-silver": "Silver Prizm rookie.",
 "hurts-2020-prizm-343-silver": "Silver Prizm rookie.",
 "lamar-2018-prizm-212-silver": "Silver Prizm rookie. PSA tracked only 2 PSA 10 sales in 90 days, so the 10 comp is an estimate from those two.",
 "tua-2020-prizm-339-silver": "Silver Prizm rookie (PSA catalogues the card as #339).",
 "tua-2020-prizm-339": "Base Prizm rookie (PSA catalogues the card as #339).",
 "tlaw-2021-prizm-331-silver": "Silver Prizm rookie.",
 "tlaw-2021-prizm-331": "Base Prizm rookie.",
 "caleb-2024-prizm-301-silver": "Silver Prizm rookie, the most-traded football silver on the board.",
 "daniels-2024-prizm-347-silver": "Silver Prizm rookie.",
 "maye-2024-prizm-329-silver": "Silver Prizm rookie.",
 "nix-2024-prizm-309-silver": "Silver Prizm rookie.",
 "jj-2024-prizm-400-silver": "Silver Prizm rookie.",
 "jj-2024-prizm-400": "Base Prizm rookie.",
 "penix-2024-prizm-378-silver": "Silver Prizm rookie.",
 "penix-2024-prizm-378": "Base Prizm rookie.",
 "byoung-2023-prizm-311-silver": "Silver Prizm rookie.",
 "byoung-2023-prizm-311": "Base Prizm rookie.",
 "richardson-2023-prizm-343-silver": "Silver Prizm rookie (the #343 card; #304 is the variation).",
 "richardson-2023-prizm-343": "Base Prizm rookie (the #343 card; #304 is the variation).",
 "love-2020-prizm-363-silver": "Silver Prizm rookie.",
 "love-2020-prizm-363": "Base Prizm rookie.",
 "dak-2016-prizm-231-silver": "Silver Prizm rookie. PSA lists it as '#231 Prizm', the 2016 naming.",
 "mahomes-2017-optic-177": "Donruss Optic Rated Rookie, base. The most liquid Mahomes rookie at this price.",
 "mahomes-2017-optic-177-holo": "Donruss Optic Rated Rookie Holo, the Optic equivalent of a silver.",
 "burrow-2020-optic-151": "Donruss Optic Rated Rookie, base.",
 "burrow-2020-optic-151-holo": "Donruss Optic Rated Rookie Holo.",
 "herbert-2020-optic-153": "Donruss Optic Rated Rookie, base.",
 "herbert-2020-optic-153-holo": "Donruss Optic Rated Rookie Holo.",
 "burrow-2020-donruss-301": "Donruss Rated Rookie, the paper base card.",
 "herbert-2020-donruss-303": "Donruss Rated Rookie, the paper base card.",
 "allen-2018-optic-154-holo": "Donruss Optic Rated Rookie Holo.",
 "lamar-2018-optic-167-holo": "Donruss Optic Rated Rookie Holo.",
 "caleb-2024-optic-201": "Donruss Optic Rated Rookie, base.",
 "caleb-2024-optic-201-holo": "Donruss Optic Rated Rookie Holo.",
 "daniels-2024-optic-248": "Donruss Optic Rated Rookie, base.",
 "daniels-2024-optic-248-holo": "Donruss Optic Rated Rookie Holo.",
 "stroud-2023-optic-244": "Donruss Optic Rated Rookie, base.",
 "stroud-2023-optic-244-holo": "Donruss Optic Rated Rookie Holo.",
}
CLOSE = {
 "mahomes-2017-prizm-269-silver": "The 9 covers the all-in by itself, so the gem rate barely matters. The only risk is the $845 ticket and the time to sell a $7,500 card. Grade it.",
 "burrow-2020-prizm-307-silver": "The math clears, but PSA tracked only 16 PSA 10 sales in 90 days, short of the 25 floor: a $1,850 card that trades once a week. Fails the liquidity floor. If you already own one, grading it is still the right call.",
 "herbert-2020-prizm-325-silver": "Eight PSA 10 sales in 90 days and the 10 price moved from $1,599 to $838 inside the window. Fails the liquidity floor and the expected value is a coin flip. Skip.",
 "hurts-2020-prizm-343-silver": "Exactly at the liquidity floor, but the gem rate is 5 points short of break-even. Fails on expected value. A raw under $80 would flip it.",
 "lamar-2018-prizm-212-silver": "Raw copies trade at $800–935 on eBay (3 sales), roughly the PSA 9 price, and a 10 is a $5,700 card that sold twice in 90 days. Not enough sales for a verdict. Skip until the 10 trades more often.",
 "tua-2020-prizm-339-silver": "Fourteen PSA 10 sales in 90 days and the 10 is only $136. Fails the liquidity floor and on expected value. Skip.",
 "tua-2020-prizm-339": "A $15 PSA 10 cannot cover a $60 fee. Fails on expected value. Skip.",
 "tlaw-2021-prizm-331-silver": "A 7% gem rate is the lowest on the board; the $1,125 PSA 10 is what keeps the expected value at zero. Eleven sales in 90 days fails the liquidity floor. Skip.",
 "tlaw-2021-prizm-331": "Six PSA 10 sales in 90 days and a 9% gem rate. Fails the liquidity floor and on expected value. Skip.",
 "caleb-2024-prizm-301-silver": "The break-even gem rate is 8% against a real 19%, and 113 PSA 10 sales in 90 days is the best football liquidity on the board. Grade it. Buy raw under $200; above $280 the edge is gone.",
 "daniels-2024-prizm-347-silver": "The gem rate (12%) sits a point under break-even (13%), so one attempt is a wash. Fails on expected value by $6. A raw at $60 or a 10 back above $850 would flip it to marginal.",
 "maye-2024-prizm-329-silver": "Gem rate 21% against a 17% break-even: a 4-point cushion, under the 10 we want. Marginal. Clears at a raw under $120.",
 "nix-2024-prizm-309-silver": "Gem rate 22% against a 16% break-even, a 6-point cushion. Marginal. The 10 price fell from $1,350 to $551 inside the window, so the cushion is shrinking.",
 "jj-2024-prizm-400-silver": "Liquid, but a $199 PSA 10 and a $30 PSA 9 cannot cover the $85 all-in at a 26% gem rate. Fails on expected value. Skip.",
 "jj-2024-prizm-400": "A $27 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "penix-2024-prizm-378-silver": "Liquid, but the 22% gem rate is half the 41% break-even. Fails on expected value. Skip.",
 "penix-2024-prizm-378": "A $25 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "byoung-2023-prizm-311-silver": "185 PSA 10 sales in 90 days, the most liquid card in this batch, and a 46% gem rate that lands exactly on the 47% break-even. Expected value is zero. Fails on expected value. Buy raw under $35 and it is a grade.",
 "byoung-2023-prizm-311": "A $40 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "richardson-2023-prizm-343-silver": "A $65 PSA 10 cannot cover the fee, and 21 sales in 90 days is under the floor. Fails. Skip.",
 "richardson-2023-prizm-343": "A $12 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "love-2020-prizm-363-silver": "Eighteen PSA 10 sales in 90 days, under the floor, and the eBay raw ($115) is above the PSA 9 price ($104): the market already prices the card as a 9. Fails. Skip.",
 "love-2020-prizm-363": "A $53 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "dak-2016-prizm-231-silver": "A 66% gem rate, the highest on the board, against a 62% break-even: too thin a cushion. Marginal. The spread between the 9 ($90) and the 10 ($278) is what makes it work at all; clears at a raw under $60.",
 "mahomes-2017-optic-177": "Gem rate 45% against a 12% break-even, with 92 PSA 10 sales in 90 days. The 9 price ($603) means a miss loses only about $40. Grade it.",
 "mahomes-2017-optic-177-holo": "The math is strong (a 9 nearly covers the $1,542 all-in), but 23 PSA 10 sales in 90 days is just under the 25 floor. Fails the liquidity floor by two sales. If you own one raw, grade it.",
 "burrow-2020-optic-151": "A $97 PSA 10 and a 42% gem rate cannot cover the $85 all-in. Fails on expected value. Skip.",
 "burrow-2020-optic-151-holo": "Gem rate 42% against a 43% break-even: a wash. Fails on expected value by $3. Buy raw under $65 and it is marginal.",
 "herbert-2020-optic-153": "A $44 PSA 10 cannot cover the fee, even at a 62% gem rate. Fails on expected value. Skip.",
 "herbert-2020-optic-153-holo": "Liquid and gems 53% of the time, but the 10 ($208) is too cheap against a $121 all-in. Fails on expected value. Skip.",
 "burrow-2020-donruss-301": "A $63 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "herbert-2020-donruss-303": "A $37 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "allen-2018-optic-154-holo": "The math clears comfortably (12% break-even against a 42% gem rate), but only 12 PSA 10 sales in 90 days. Fails the liquidity floor. If you own one raw, grade it.",
 "lamar-2018-optic-167-holo": "Eight PSA 10 sales in 90 days. The math clears, the market is thin. Fails the liquidity floor. Skip as a buy-to-grade.",
 "caleb-2024-optic-201": "A $157 PSA 10 at a 30% gem rate, against a $33 PSA 9, cannot cover the $72 all-in. Fails on expected value. Skip.",
 "caleb-2024-optic-201-holo": "Gem rate 20% against a 19% break-even: expected value about +$5. Marginal, and 33 sales in 90 days is just over the floor. Buy raw under $35 and it is a grade.",
 "daniels-2024-optic-248": "A $42 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "daniels-2024-optic-248-holo": "Liquid, but the 28% gem rate is half the 60% break-even. Fails on expected value. Skip.",
 "stroud-2023-optic-244": "A $30 PSA 10 cannot cover the fee. Fails on expected value. Skip.",
 "stroud-2023-optic-244-holo": "153 PSA 10 sales in 90 days and a 57% gem rate, but the 10 is $91. Fails on expected value. Skip.",
}

for key, lead in LEAD.items():
    d = D[key]
    psa10 = d["med10"] if d["med10"] is not None else d["avg10"]
    psa9 = d["med9"] if d["med9"] is not None else d["avg9"]
    raw = d["rawMed"]
    gem = d["pop10"] / d["popTotal"] if d.get("pop10") and d.get("popTotal") else A["assumedGem"]
    allIn = raw + A["fee"] + A["ship"]; net10 = psa10 * (1 - A["haircut"]) * (1 - A["sellFee"]); netMiss = psa9 * A["missReal"] * (1 - A["sellFee"])
    ev = gem * net10 + (1 - gem) * netMiss; profit = ev - allIn
    be = (allIn - netMiss) / (net10 - netMiss) if net10 != netMiss else None
    rng = f", range {money(d['min10'])}–{money(d['max10'])}" if d.get("min10") is not None else ""
    latest = f", latest {money(d['latest10'])}" if d.get("latest10") is not None else ""
    if d.get("rawSrc"):
        rawtxt = f"raw {money(raw)} median on eBay sold ({d['rawSrc'].split('(')[1].rstrip(')')}; PSA's own raw tracking showed {money(d['rawPsa'])} on {d.get('rawNPsa', 15)} sales)"
    else:
        rawtxt = f"raw {d['rawN']} tracked sales, median {money(raw, 2 if raw < 20 else 0)}" + (f", latest {money(d['rawLast'], 2 if d['rawLast'] < 20 else 0)}" if d.get("rawLast") is not None else "")
    betxt = ("a 9 alone covers the all-in, so the break-even gem rate is 0%" if be is not None and be <= 0 else f"against a break-even gem rate of {pct(be)}" + (", which can't be reached" if be > 1 else "") if be is not None else "")
    body = (f"PSA APR (Oct 11): {d['n10']} PSA 10 sales in 90 days, median {money(psa10)}{rng}{latest}; PSA 9 {d['n9']} sales, median {money(psa9)}; {rawtxt}. "
            f"PSA POP: 10={d['pop10']:,}, 9={d['pop9']:,}, 8={d['pop8']:,}, total {d['popTotal']:,} → {pct(gem)} gem, {betxt}. "
            f"{money(allIn)} all-in: a 10 nets about {signed(net10 - allIn)}, a 9 nets {signed(netMiss - allIn)}, expected value {signed(profit)}.")
    N[key] = f"{lead} {body} {CLOSE[key]}"

json.dump(N, open(os.path.join(HERE, "notes.json"), "w"), indent=1, ensure_ascii=False)
print("notes written:", len(LEAD))
