"""Refresh cards that are already on the board from a fresh PSA pull without replacing their hand-written notes.
Updates raw/psa10/psa9/sales/pop/asOf in netlify/lib/screen-data.mjs and appends one dated sentence to the note.
Usage: python3 refresh.py psa-7.json wemby-2023-prizm-136=wembanyama-2023-panini-prizm-136-base [key=boardId ...]
"""
import json, os, sys, datetime, re
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(SITE, "netlify/lib/screen-data.mjs")
A = dict(fee=59.99, ship=10, sellFee=.13, haircut=.20, missReal=.85)

def money(x, dec=0):
    s = f"{abs(x):,.{dec}f}"; return ("–$" if x < 0 else "$") + s
def signed(x): return ("+$" if x >= 0 else "–$") + f"{abs(x):,.0f}"

pulls = json.load(open(os.path.join(HERE, sys.argv[1])))
src = open(DATA).read(); head, body = src.split("export default ", 1)
cards = json.loads(body.strip().rstrip(";")); byid = {c["id"]: c for c in cards}
for arg in sys.argv[2:]:
    key, bid = arg.split("="); d = pulls[key]; c = byid[bid]
    day = d.get("asOf"); nice = datetime.date.fromisoformat(day).strftime("%b ") + str(datetime.date.fromisoformat(day).day)
    if f"PSA APR ({nice})" in c["note"]:
        print("already refreshed", bid); continue
    psa10 = d["med10"] if d.get("med10") is not None else d["avg10"]; psa9 = d["med9"] if d.get("med9") is not None else d["avg9"]; raw = d["rawMed"]
    gem = d["pop10"] / d["popTotal"]
    allIn = raw + A["fee"] + A["ship"]; net10 = psa10 * (1 - A["haircut"]) * (1 - A["sellFee"]); netMiss = psa9 * A["missReal"] * (1 - A["sellFee"])
    ev = gem * net10 + (1 - gem) * netMiss
    rawtxt = (f"raw {money(raw)} on eBay sold ({d['rawSrc'].split('(')[1].rstrip(')')})" if d.get("rawSrc")
              else f"raw {money(raw, 2 if raw < 20 else 0)} median of {d['rawN']} PSA-tracked sales")
    n10txt = f"{d['n10']:,}" + ("+" if d["n10"] >= 1000 else "")
    sent = (f" PSA APR ({nice}): PSA 10 {n10txt} sales/90d, median {money(psa10)}, latest {money(d['latest10'])}; PSA 9 {d['n9']:,} sales, median {money(psa9)}; {rawtxt}. "
            f"PSA POP ({nice}): 10={d['pop10']:,}, 9={d['pop9']:,}, total {d['popTotal']:,} → {gem*100:.1f}% gem. "
            f"{money(allIn)} all-in: a 10 nets about {signed(net10 - allIn)}, a 9 nets {signed(netMiss - allIn)}, expected value {signed(ev - allIn)}.")
    c.update({"raw": round(raw * 100) / 100, "psa10": round(psa10 * 100) / 100, "psa9": round(psa9 * 100) / 100, "psa10Sales90": d["n10"], "compType": "Real",
              "pop10": d["pop10"], "pop9": d["pop9"], "popTotal": d["popTotal"], "asOf": day, "conf": "H" if d["n10"] >= 25 else "M"})
    c["note"] += sent
    if f"({nice}, " not in c["src"]: c["src"] += f"; PSA APR + pop ({nice})" + (f"; raw = {d['rawSrc']}" if d.get("rawSrc") else "")
    print("refreshed", bid, "10", money(psa10), "n10", d["n10"], "raw", money(raw), "EV", signed(ev - allIn))
open(DATA, "w").write(head + "export default " + json.dumps(cards, ensure_ascii=False, separators=(",", ":")) + ";\n")
