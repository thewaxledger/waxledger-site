"""Shared note writer for the Raw-to-Gem pipeline: the numeric body of each note is generated from a psa-N.json
entry with the site model; LEAD and CLOSE (per key) are written by hand. Used by notes5.py, notes7.py, ...
    from r2gnotes import write_notes; write_notes("psa-7.json", LEAD, CLOSE, "Oct 11")
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
A = dict(fee=59.99, ship=10, sellFee=.13, haircut=.20, missReal=.85, assumedGem=.35, minSales=25, minMargin=.10)

def money(x, dec=0):
    if x is None: return "n/a"
    s = f"{abs(x):,.{dec}f}"
    return ("–$" if x < 0 else "$") + s
def signed(x):
    return ("+$" if x >= 0 else "–$") + f"{abs(x):,.0f}"
def pct(x): return f"{x*100:.0f}%"


def write_notes(datafile, LEAD, CLOSE, day):
    D = json.load(open(os.path.join(HERE, datafile)))
    N = json.load(open(os.path.join(HERE, "notes.json")))
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
        body = (f"PSA APR ({day}): {d['n10']} PSA 10 sales in 90 days, median {money(psa10)}{rng}{latest}; PSA 9 {d['n9']} sales, median {money(psa9)}; {rawtxt}. "
                f"PSA POP: 10={d['pop10']:,}, 9={d['pop9']:,}, 8={d['pop8']:,}, total {d['popTotal']:,} → {pct(gem)} gem, {betxt}. "
                f"{money(allIn)} all-in: a 10 nets about {signed(net10 - allIn)}, a 9 nets {signed(netMiss - allIn)}, expected value {signed(profit)}.")
        N[key] = f"{lead} {body} {CLOSE[key]}"

    json.dump(N, open(os.path.join(HERE, "notes.json"), "w"), indent=1, ensure_ascii=False)
    print("notes written:", len(LEAD))
