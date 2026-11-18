"""Build netlify/lib/break-data.mjs (the Break Guide's member-only data) from tools/breaks/<product>/.
Each product folder holds product.json (identity, box prices with their source, caveats, method) and the model output:
formats.json, summary.json, spots.json (one row per team and format), chases.json, rookies.json, checklist.json.
model.py in the folder is the script that produced those rows; rerun it when odds or weights change, then run this.
Usage: python3 tools/breaks/build.py
"""
import json, os, glob
from collections import defaultdict, OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(SITE, "netlify/lib/break-data.mjs")

def load(d, n): return json.load(open(os.path.join(d, n + ".json")))

def product(d):
    p = load(d, "product"); formats = load(d, "formats"); summary = {s["format"]: s for s in load(d, "summary")}
    spots = load(d, "spots"); chases = load(d, "chases"); rookies = load(d, "rookies"); checklist = load(d, "checklist")
    fm = []
    for f in formats:
        pr = p["prices"].get(f["format"], {}); s = summary.get(f["format"], {})
        fm.append({"id": f["format"], "label": f["label"], "boxesCase": f["boxes_case"], "autosBox": f["autos_box"],
                   "box": pr.get("box", f["box_market"]), "boxSrc": pr.get("src", ""), "boxTopps": f.get("box_presale"),
                   "rookieAutoPct": f.get("rookie_auto_share_pct"), "star": s.get(p["star"]["field"])})
    teams = OrderedDict()
    for r in spots:
        t = teams.setdefault(r["abbr"], {"abbr": r["abbr"], "team": r["team"], "signers": r["top_signers"], "rookieSigners": r["rookie_signers"],
                                         "otherAutos": r["other_autos"], "ssp": r["ssp_inserts"], "patch": r["patch_autos"], "headline": r["headline"], "f": {}})
        t["f"][r["format"]] = {"rank": r["rank"], "tier": r["tier"], "share": r["share"], "p": r["p_slot"], "pr": r["p_rookie_slot"]}
    held = defaultdict(lambda: defaultdict(OrderedDict))  # abbr -> kind -> player -> [set/note]
    for c in sorted(checklist, key=lambda c: -c.get("weight", 0)):
        k = c["kind"]; lab = c["note"] if k == "Base rookie" else c["set"].replace(" Autographs", "") + (" (" + c["note"] + ")" if c.get("note") else "")
        held[c["abbr"]][k].setdefault(c["player"], []).append(lab or "")
    for a, t in teams.items():
        h = held.get(a, {})
        t["hold"] = {"rookies": [[pl, ", ".join(x for x in v if x)] for pl, v in h.get("Base rookie", {}).items()],
                     "autos": [[pl, ", ".join(v)] for pl, v in h.get("Auto", {}).items()],
                     "ssp": [[pl, ", ".join(v)] for pl, v in h.get("Short-print insert", {}).items()],
                     "patch": list(h.get("Patch auto 1/1", {}).keys()), "retail": list(h.get("Retail auto", {}).keys())}
    ch = OrderedDict()
    for c in sorted(chases, key=lambda c: c["sort"]):
        e = ch.setdefault(c["chase"], {"chase": c["chase"], "kind": c["kind"], "team": c["team"], "basis": c["basis"], "perBox": {}})
        e["perBox"][c["format"]] = c["per_box"]
    return {"id": p["id"], "name": p["name"], "sport": p["sport"], "release": p["release"], "asOf": p["asOf"], "review": p.get("review"), "unit": p.get("unit", "team"),
            "starLabel": p["star"]["label"], "caveat": p["caveat"], "noOdds": p.get("noOdds", ""), "rookieNote": p.get("rookieNote", ""), "method": p["method"],
            "formats": fm, "teams": list(teams.values()), "chases": list(ch.values()),
            "rookies": [{"player": r["player"], "team": r["team"], "pos": r["pos"], "auto": r["rookie_auto"], "other": r["other_autos"], "ssp": r["ssp_inserts"], "weight": r["weight"], "status": r["status"]} for r in rookies]}

prods = [product(os.path.dirname(f)) for f in glob.glob(os.path.join(HERE, "*", "product.json"))]
prods.sort(key=lambda p: p["release"], reverse=True)
open(OUT, "w").write("// Built by tools/breaks/build.py from tools/breaks/<product>/. Do not edit by hand.\nexport default " + json.dumps(prods, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("break-data.mjs:", len(prods), "products,", os.path.getsize(OUT), "bytes;", ", ".join(p["id"] for p in prods))
