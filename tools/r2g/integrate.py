"""Append the built entries to netlify/lib/screen-data.mjs (idempotent: replaces entries with the same id)."""
import json, subprocess, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(SITE, "netlify/lib/screen-data.mjs")
AS_OF = "2026-10-22"  # the day of the newest pull; set this when you run a refresh
import datetime
NICE = datetime.date.fromisoformat(AS_OF).strftime("%b ") + str(datetime.date.fromisoformat(AS_OF).day)
src = open(DATA).read()
head, body = src.split("export default ", 1)
cards = json.loads(body.strip().rstrip(";"))
new = json.loads(subprocess.check_output(["python3", os.path.join(HERE, "build.py")], stderr=subprocess.DEVNULL))
byid = {c["id"]: c for c in cards}
maxorder = max(c["order"] for c in cards)
added = replaced = 0
for n in new:
    if not n["note"]:
        print("no note for", n["id"], file=sys.stderr); continue
    if n["id"] in byid:
        old = byid[n["id"]]; n["order"] = old["order"]
        if old["note"].startswith(n["note"]) and len(old["note"]) > len(n["note"]):
            # the board note carries refresh.py sentences that notes.json does not; keep them, and the board's
            # numbers if they are newer than this pull
            n["note"] = old["note"]; n["src"] = old["src"]
            if old.get("asOf", "") > n["asOf"]:
                for k in ("raw", "rawSales30", "psa10", "psa10Sales90", "compType", "psa9", "pop10", "pop9", "popTotal", "asOf", "conf", "src"): n[k] = old[k]
        old.update(n); replaced += 1
    else:
        maxorder += 1; n["order"] = maxorder; cards.append(n); byid[n["id"]] = n; added += 1
# refresh the Trout entry from the PSA pull if present
psa = {}
import glob
for f in sorted(glob.glob(os.path.join(HERE, "psa-*.json"))):
    psa.update(json.load(open(f)))
t = byid.get("trout-2011-topps-update-us175-base"); p = psa.get("trout-2011-tu-us175")
if t and p and "PSA APR (Oct 9)" not in t["note"]:
    t.update({"raw": p["rawMed"], "psa10": round(p["med10"]), "psa10Sales90": p["n10"], "psa9": round(p["med9"]), "pop10": p["pop10"], "pop9": p["pop9"], "popTotal": p["popTotal"], "asOf": p.get("asOf") or "2026-10-09"})
    t["note"] += " PSA APR (Oct 9): PSA 10 130 sales/90d, median $931, average $1,014; PSA 9 80 sales, median $399; raw 15 tracked sales, median $286. PSA POP (Oct 9): 10=7,116, 9=5,788, total 16,942 → 42.0% gem. Still clears comfortably: $356 all-in, a 10 nets about +$292, a 9 nets –$61."
    t["src"] += "; PSA APR + pop (Oct 9)"
head = re.sub(r"checked [A-Z][a-z]+ \d+, 2026", "checked %s, 2026" % NICE, head)
open(DATA, "w").write(head + "export default " + json.dumps(cards, ensure_ascii=False, separators=(",", ":")) + ";\n")
scr = os.path.join(SITE, "netlify/functions/screener.mjs")
s = re.sub(r'asOf: "\d{4}-\d\d-\d\d"', 'asOf: "%s"' % AS_OF, open(scr).read())
open(scr, "w").write(s)
print("added", added, "replaced", replaced, "total", len(cards))
