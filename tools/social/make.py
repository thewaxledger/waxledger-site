"""Social images for X (1200x675) and Instagram (1080x1350) in the house style of public/social/*.jpg.
Numbers come from netlify/lib/screen-data.mjs with the site's Raw-to-Gem model, so every image matches the board.
Usage: python3 tools/social/make.py OUTDIR      (writes <name>-x.jpg and <name>-ig.jpg per post)
"""
import json, os, sys, html
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARDS = {c["id"]: c for c in json.loads(open(os.path.join(ROOT, "netlify/lib/screen-data.mjs")).read().split("export default ", 1)[1].strip().rstrip(";"))}

def model(c):
    gem = c["pop10"] / c["popTotal"]; fee = 59.99 if c["psa10"] > 500 else 39.99
    allin = c["raw"] + fee + 10; n10 = c["psa10"] * .8 * .87; nm = c["psa9"] * .85 * .87
    return dict(gem=gem, fee=fee, allin=allin, n10=n10, nm=nm, ev=gem * n10 + (1 - gem) * nm - allin, be=(allin - nm) / (n10 - nm))

def usd(x, sign=False):
    s = f"${abs(x):,.0f}"
    return (("+" if x >= 0 else "–") + s) if sign else s

def short(c):
    yr = c["year"]; st = c["set"].replace("Panini ", "").replace("Upper Deck", "UD").replace("UEFA Champions League", "UCL")
    par = "" if c["parallel"].startswith(("Base", "Rated Rookie base")) else " " + c["parallel"].split(" (")[0].replace(" RC", "")
    return f"{c['player']} {yr} {st} #{c['cardNo']}{par}"

CSS = """
*{margin:0;box-sizing:border-box}body{background:#111A2B;color:#fff;font-family:Inter,'DejaVu Sans',sans-serif}
.f{position:relative;width:W;height:H;padding:PADpx;overflow:hidden;border-top:14px solid #E3A92B;display:flex;flex-direction:column}
.eb{font-family:'DejaVu Sans Mono',monospace;color:#AEB7C6;letter-spacing:.06em;font-size:EBpx;text-transform:uppercase}
.h{font-weight:900;text-transform:uppercase;line-height:.98;letter-spacing:-.01em;font-size:HPpx;margin-top:10px}
.h .r{color:#F08A78}.h .g{color:#E3A92B}.h .gr{color:#4CC38A}
.p{color:#D5DBE5;font-size:Ppx;line-height:1.42;margin-top:26px}
.rows{margin-top:24px;display:flex;flex-direction:column;gap:10px}
.row{background:#1C283C;padding:14px 22px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.row b{display:block;font-size:RBpx;font-weight:800}.row small{display:block;font-family:'DejaVu Sans Mono',monospace;color:#AEB7C6;font-size:RSpx;margin-top:6px}
.row .v{font-weight:900;font-size:RVpx;white-space:nowrap}.pos{color:#4CC38A}.neg{color:#F08A78}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:26px}
.cell{background:#1C283C;padding:18px 22px}.cell .k{font-family:'DejaVu Sans Mono',monospace;color:#AEB7C6;font-size:RSpx;text-transform:uppercase}
.cell .n{font-weight:900;font-size:CNpx;margin-top:6px}.cell .s{color:#AEB7C6;font-size:RSpx;margin-top:4px;font-family:'DejaVu Sans Mono',monospace}
.ft{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;padding-top:20px}
.ft .b{color:#E3A92B;font-weight:900;font-size:FBpx;letter-spacing:-.01em}.ft .u{font-family:'DejaVu Sans Mono',monospace;color:#AEB7C6;font-size:FUpx}
"""
SIZES = {"x": dict(W="1200px", H="675px", PAD=54, EB=19, HP=58, P=22, RB=24, RS=16, RV=30, CN=40, FB=34, FU=20),
         "ig": dict(W="1080px", H="1350px", PAD=80, EB=25, HP=96, P=31, RB=33, RS=22, RV=42, CN=60, FB=52, FU=26)}

def page(kind, body):
    css = CSS
    z = SIZES[kind]
    css = css.replace("width:W", "width:" + z["W"]).replace("height:H", "height:" + z["H"])
    for k, v in sorted(z.items(), key=lambda kv: -len(kv[0])):
        if k not in ("W", "H"): css = css.replace(k + "px", str(v) + "px")
    return f"<html><head><style>{css}</style></head><body><div class='f'>{body}<div class='ft'><span class='b'>WAX LEDGER</span><span class='u'>thewaxledger.com</span></div></div></body></html>"

def math_card(cid, eyebrow, head, line, kind):
    c = CARDS[cid]; m = model(c)
    cells = [
        ("Raw, eBay sold", usd(c["raw"]), f"all-in {usd(m['allin'])} with the ${m['fee']:.2f} PSA fee + $10 ship"),
        ("PSA 10", usd(c["psa10"]), f"{c['psa10Sales90']} sales in 90 days · nets {usd(m['n10'] - m['allin'], True)}"),
        ("PSA 9", usd(c["psa9"]), f"nets {usd(m['nm'] - m['allin'], True)} if it misses"),
        ("Gem rate (PSA pop)", f"{m['gem']*100:.0f}%", f"break-even {max(m['be'],0)*100:.0f}% · EV {usd(m['ev'], True)} a try"),
    ]
    if kind == "x": cells = cells  # same four cells, smaller type
    grid = "".join(f"<div class='cell'><div class='k'>{html.escape(k)}</div><div class='n'>{html.escape(n)}</div><div class='s'>{html.escape(s)}</div></div>" for k, n, s in cells)
    p = f"<p class='p'>{html.escape(line)}</p>" if kind == "ig" else ""
    return f"<p class='eb'>{html.escape(eyebrow)}</p><h1 class='h'>{head}</h1>{p}<div class='grid'>{grid}</div>"

def list_card(ids, eyebrow, head, line, kind, n=5):
    rows = ""
    for cid in ids[:4 if kind == "ig" else 3]:
        c = CARDS[cid]; m = model(c)
        rows += (f"<div class='row'><div><b>{html.escape(short(c))}</b><small>raw {usd(c['raw'])} · PSA 10 {usd(c['psa10'])} on {c['psa10Sales90']} sales · {m['gem']*100:.0f}% gem</small></div>"
                 f"<span class='v {'pos' if m['ev'] > 0 else 'neg'}'>{usd(m['ev'], True)} a try</span></div>")
    p = f"<p class='p'>{html.escape(line)}</p>" if line else ""
    return f"<p class='eb'>{html.escape(eyebrow)}</p><h1 class='h'>{head}</h1>{p}<div class='rows'>{rows}</div>"

POSTS = [
 ("nov13-18buys", "list", dict(ids=["curry-2025-topps-chrome-201-refractor", "duncan-1997-topps-chrome-115-base", "james-2025-topps-chrome-127-refractor", "haaland-2019-topps-chrome-ucl-74-base", "wade-2003-topps-chrome-115-base"],
   eyebrow="Raw-to-Gem Calculator · PSA APR + pop, Nov 12", head="580 cards screened.<br><span class='g'>18 clear the fee.</span>",
   line="Raw price from eBay sold, PSA 10 and 9 from 90 days of PSA sales, gem rate from the pop report. Expected value is profit per card graded, after fees.")),
 ("nov14-curry-ref", "math", dict(cid="curry-2025-topps-chrome-201-refractor", eyebrow="The math · 2025-26 Topps Chrome #201 Refractor", head="Stephen Curry<br><span class='gr'>Refractor</span>",
   line="A $78 raw card with a $790 ten. 44% of them come back 10 at PSA.")),
 ("nov15-allen", "math", dict(cid="allen-2018-panini-donruss-304-rated", eyebrow="The math · 2018 Donruss Rated Rookie #304", head="Josh Allen<br><span class='gr'>Donruss #304</span>",
   line="332 PSA 10 sales in 90 days, the most liquid card on the board. The margin is thin: it holds up to about $170 raw.")),
 ("nov16-zion", "list", dict(ids=["zion-2019-panini-prizm-248-base", "tatis-2019-topps-chrome-203-base", "stroud-2023-panini-prizm-339-base", "morant-2019-panini-prizm-249-base"],
   eyebrow="Raw-to-Gem Calculator · the other side", head="44% to 70% gem.<br><span class='r'>All of them lose money.</span>",
   line="A high gem rate on a card whose PSA 10 sells for $20 to $30 can't cover a $40 grading fee.")),
 ("nov17-haaland", "math", dict(cid="haaland-2019-topps-chrome-ucl-74-base", eyebrow="The math · 2019-20 Topps Chrome UCL #74", head="Erling Haaland<br><span class='gr'>Chrome rookie</span>",
   line="Half the PSA pop is a 10, and a 9 at $168 almost covers the all-in by itself.")),
 ("nov18-wade", "math", dict(cid="wade-2003-topps-chrome-115-base", eyebrow="The math · 2003-04 Topps Chrome #115", head="Dwyane Wade<br><span class='gr'>Chrome rookie</span>",
   line="One in four comes back a 10, and a $618 ten carries the other three.")),
 ("nov19-jsn", "math", dict(cid="smith-njigba-2023-panini-prizm-390-silver", eyebrow="The math · 2023 Prizm #390 Silver", head="Jaxon Smith-Njigba<br><span class='gr'>Silver Prizm</span>",
   line="The ten has followed his season up. Raw has followed too, so the margin is about $7 wide.")),
 ("nov20-kobe", "math", dict(cid="bryant-2012-panini-prizm-24-base", eyebrow="The math · 2012-13 Prizm #24", head="Kobe Bryant<br><span class='gr'>first-year Prizm</span>",
   line="The PSA 9 covers the $274 all-in, so the risk is an 8, not a miss.")),
]

def main(out):
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, kind, spec in POSTS:
            for fmt, (w, h) in (("x", (1200, 675)), ("ig", (1080, 1350))):
                body = math_card(kind=fmt, **spec) if kind == "math" else list_card(kind=fmt, **spec)
                pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
                pg.set_content(page(fmt, body)); pg.wait_for_timeout(150)
                pg.screenshot(path=os.path.join(out, f"{name}-{fmt}.jpg"), type="jpeg", quality=90); pg.close()
        b.close()
    print("wrote", len(POSTS) * 2, "images to", out)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "public/social/nov13"))
