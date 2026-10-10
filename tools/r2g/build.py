"""Merge PSA Auction Prices Realized pulls (psa-*.json) with hand-written meta (meta.json) into screen-data entries.
Usage: python3 build.py > new-entries.json
"""
import json, glob, os, datetime, math
HERE = os.path.dirname(os.path.abspath(__file__))
AS_OF = "2026-10-09"
raw = {}
for f in sorted(glob.glob(os.path.join(HERE, "psa-*.json"))):
    raw.update(json.load(open(f)))
meta = json.load(open(os.path.join(HERE, "meta.json")))
notes = json.load(open(os.path.join(HERE, "notes.json"))) if os.path.exists(os.path.join(HERE, "notes.json")) else {}

def r2(x):
    return None if x is None else round(float(x) * 100) / 100

def raw_sales_30(d):
    """PSA lists ungraded sales too; we pulled up to 15. Scale the span of those 15 to a 30-day rate."""
    n = d.get("rawN") or 0
    if not n:
        return 0
    oldest = d.get("rawOldest")
    if not oldest or n < 15:
        return n if n < 15 else n  # fewer than 15 in the whole 90-day window: use the count as-is (per 90d, conservative)
    days = (datetime.date.fromisoformat(AS_OF) - datetime.date.fromisoformat(oldest)).days or 1
    return max(n, round(n * 30 / days))

out = []
order = 100
for key, m in meta.items():
    d = raw.get(key)
    if not d:
        print("missing data for", key, file=__import__("sys").stderr); continue
    psa10 = d.get("med10") if d.get("med10") is not None else d.get("avg10")
    psa9 = d.get("med9") if d.get("med9") is not None else d.get("avg9")
    rawp = d.get("rawMed")
    n10 = d.get("n10") or 0
    conf = "H" if n10 >= 25 and (d.get("rawN") or 0) >= 10 else "M" if n10 >= 8 else "L"
    comp = "Real" if n10 >= 3 else "Estimate"
    entry = {
        "id": m["id"], "player": m["player"], "year": m["year"], "set": m["set"], "cardNo": m["cardNo"], "parallel": m["parallel"], "sport": m["sport"],
        "raw": r2(rawp), "rawSales30": raw_sales_30(d), "psa10": r2(psa10), "psa10Sales90": n10, "compType": comp, "psa9": r2(psa9),
        "pop10": d.get("pop10"), "pop9": d.get("pop9"), "popTotal": d.get("popTotal"), "asOf": AS_OF, "conf": conf, "order": order,
        "note": notes.get(key, ""), "src": "PSA Auction Prices Realized, last 90 days (Oct 9, 2026); PSA pop report (Oct 9); raw = PSA-tracked ungraded eBay sales"
    }
    order += 1
    out.append(entry)
print(json.dumps(out, ensure_ascii=False, indent=0))
