"""Static, indexable pages generated from the site's data at build time.

  public/grade/<card-id>/index.html   one page per Raw-to-Gem card (numbers, verdict, one line of why; the rest is Pro)
  public/grade/index.html             every card, grouped by sport
  public/reviews/<slug>/index.html    one page per deep Product Review (the full review)
  public/reviews/index.html           all reviews
  public/static.css, sitemap.xml, robots.txt

Called by tools/build.py. Data: netlify/lib/screen-data.mjs and the REVIEWS block in src/index.src.html.
"""
import json, os, re, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "public")
SITE = "https://thewaxledger.com"
A = dict(fee=59.99, ship=10, sellFee=.13, haircut=.20, missReal=.85, assumedGem=.35, minSales=25, minMargin=.10)

esc = lambda s: html.escape(str(s if s is not None else ""), quote=True)

def usd(x, sign=False):
    if x is None: return "n/a"
    s = ("+" if sign and x > 0 else "–" if x < 0 else "") + "$" + format(abs(round(x)), ",")
    return s

def pct(x): return "n/a" if x is None else str(round(x * 100)) + "%"

def slug_of_review(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

# ---------- data ----------
def load_cards():
    src = open(os.path.join(ROOT, "netlify/lib/screen-data.mjs")).read()
    body = src.split("export default ", 1)[1].strip().rstrip(";")
    return json.loads(body)

def load_reviews():
    src = open(os.path.join(ROOT, "src/index.src.html")).read()
    block = src[src.index("var REVIEWS=["):]
    block = block[:block.index("\n];")]
    out = []
    for m in re.finditer(r"/\* ([a-z0-9-]+) \*/(\{.*\}),?$", block, re.M):
        try: out.append((m.group(1), json.loads(m.group(2))))
        except json.JSONDecodeError: pass
    return out

# ---------- model (mirror of scrCompute / screener.mjs score) ----------
def compute(c):
    r = {}
    if not all(isinstance(c.get(k), (int, float)) for k in ("raw", "psa10", "psa9")):
        r["code"] = "NODATA"; return r
    gem_pop = (c["pop10"] / c["popTotal"]) if c.get("pop10") and c.get("popTotal") else None
    gem = gem_pop if gem_pop is not None else A["assumedGem"]
    all_in = c["raw"] + A["fee"] + A["ship"]
    net10 = c["psa10"] * (1 - A["haircut"]) * (1 - A["sellFee"])
    net_miss = c["psa9"] * A["missReal"] * (1 - A["sellFee"])
    ev = gem * net10 + (1 - gem) * net_miss
    profit = ev - all_in
    be = (all_in - net_miss) / (net10 - net_miss) if net10 != net_miss else None
    r.update(gem=gem, gemPop=gem_pop, allIn=all_in, net10=net10, netMiss=net_miss, ev=ev, profit=profit, roi=profit / all_in, be=be,
             up10=net10 - all_in, down9=net_miss - all_in, margin=(gem - be) if be is not None else None)
    sales = c.get("psa10Sales90") or 0
    if c.get("compType") != "Real": r["code"], r["label"], r["why"] = "SKIP", "Skip", "The PSA 10 price is an estimate, not real sales."
    elif sales < A["minSales"]: r["code"], r["label"], r["why"] = "FAIL", "Fail", f"Only {sales} PSA 10 sales in 90 days, under the 25-sale minimum."
    elif profit <= 0: r["code"], r["label"], r["why"] = "FAIL", "Fail", "Negative expected value after the fee, shipping and selling costs."
    elif gem_pop is None: r["code"], r["label"], r["why"] = "CANDIDATE", "Verify pop", "Profitable on a placeholder gem rate; the real population is not in yet."
    elif be is None or gem - be < A["minMargin"]: r["code"], r["label"], r["why"] = "MARGINAL", "Marginal", f"Gem rate {pct(gem)} is within 10 points of the {pct(be)} break-even."
    else: r["code"], r["label"], r["why"] = "GRADE", "Grade", f"Gem rate {pct(gem)} against a {pct(be)} break-even, with {sales} PSA 10 sales in 90 days."
    return r

# ---------- shell ----------
CSS = """:root{--bg:#ECEFF1;--surface:#fff;--surface-2:#F4F6F8;--ink:#0F1B2D;--ink-2:#44536A;--ink-3:#657388;--line:#D0D8E0;--gold:#E3A92B;--gold-ink:#765000;--on-gold:#1A1300;--up:#0D7446;--up-bg:#DFF2E8;--down:#B2372A;--down-bg:#FAE4E0;--display:"Barlow Condensed","Arial Narrow",Arial,sans-serif;--body:"Instrument Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0A101A;--surface:#121A28;--surface-2:#192335;--ink:#E8EDF4;--ink-2:#AAB6C8;--ink-3:#8492A7;--line:#2A374D;--gold:#EDB840;--gold-ink:#F2C75C;--up:#4FC78E;--up-bg:#11301F;--down:#F2877A;--down-bg:#3A1915;color-scheme:dark}}
:root[data-theme=dark]{--bg:#0A101A;--surface:#121A28;--surface-2:#192335;--ink:#E8EDF4;--ink-2:#AAB6C8;--ink-3:#8492A7;--line:#2A374D;--gold:#EDB840;--gold-ink:#F2C75C;--up:#4FC78E;--up-bg:#11301F;--down:#F2877A;--down-bg:#3A1915;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 var(--body)}a{color:var(--gold-ink)}
.wrap{max-width:980px;margin:0 auto;padding:0 16px}
header{background:var(--surface);border-bottom:1px solid var(--line)}.hdr{display:flex;align-items:center;gap:16px 24px;flex-wrap:wrap;padding:14px 0}
.brand{font-family:var(--display);font-weight:800;font-size:1.5rem;letter-spacing:.01em;color:var(--ink);text-decoration:none;text-transform:uppercase}
.nav{display:flex;gap:4px 14px;flex-wrap:wrap;font-size:14px}.nav a{color:var(--ink-2);text-decoration:none}.nav a:hover{color:var(--ink)}
.btn{display:inline-block;padding:9px 14px;border-radius:8px;border:1px solid var(--line);text-decoration:none;color:var(--ink);font-weight:600;font-size:14px}.btn-gold{background:var(--gold);border-color:var(--gold);color:var(--on-gold)}
main{padding:28px 0 40px}.eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);margin:0 0 6px}
h1{font-family:var(--display);font-weight:800;font-size:clamp(1.9rem,4.5vw,2.8rem);line-height:1.02;margin:0 0 10px;text-transform:uppercase}
h2{font-family:var(--display);font-weight:700;font-size:1.35rem;margin:26px 0 10px;text-transform:uppercase;letter-spacing:.01em}
.lede{color:var(--ink-2);font-size:1.05rem;max-width:70ch;margin:0 0 18px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:14px 0}
.verdict{display:inline-block;font-family:var(--mono);font-weight:700;font-size:12px;letter-spacing:.06em;padding:5px 10px;border-radius:6px;text-transform:uppercase}
.v-GRADE{background:var(--up-bg);color:var(--up)}.v-MARGINAL{background:#FFF3D6;color:#765000}.v-FAIL,.v-SKIP,.v-NODATA{background:var(--down-bg);color:var(--down)}.v-CANDIDATE{background:var(--surface-2);color:var(--ink-2)}
.tbl{overflow-x:auto;-webkit-overflow-scrolling:touch}table{width:100%;border-collapse:collapse;font-size:14.5px}th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}@media (max-width:600px){table{font-size:13px}th,td{padding:7px 6px}}th{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);font-weight:500}td.num,th.num{text-align:right;font-family:var(--mono);white-space:nowrap}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}.grid a{display:block;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:12px 14px;text-decoration:none;color:var(--ink)}.grid a small{display:block;color:var(--ink-3);font-size:12.5px;margin-top:3px}
.pro{border:1px solid var(--gold);background:var(--surface);border-radius:10px;padding:18px 20px;margin:22px 0}.pro h2{margin-top:0}.pro ul{margin:8px 0 14px;padding-left:18px;color:var(--ink-2)}
.facts{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:6px;color:var(--ink-2)}.facts li{padding-left:14px;position:relative}.facts li::before{content:"";position:absolute;left:0;top:.65em;width:6px;height:2px;background:var(--gold-ink)}
.bars{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:7px 10px;align-items:center;font-size:13px;color:var(--ink-2);margin-top:14px}.bar{height:6px;background:var(--surface-2);border-radius:3px;overflow:hidden}.bar i{display:block;height:100%;background:var(--ink)}
.score{font-family:var(--display);font-weight:800;font-size:3rem;line-height:.9}.score small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.06em;color:var(--ink-3);font-weight:400;margin-top:4px}
.top{display:flex;justify-content:space-between;gap:16px;align-items:flex-start}
.chase{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px}.chase li{padding-left:14px;position:relative;line-height:1.5}.chase li::before{content:"";position:absolute;left:0;top:.68em;width:6px;height:2px;background:var(--gold-ink)}.chase b{display:block}.chase .p{display:block;font-family:var(--mono);font-size:12px;color:var(--gold-ink);margin-top:2px}.chase p{margin:4px 0 0;color:var(--ink-2)}
.news{border-top:1px solid var(--line);background:var(--surface);padding:26px 0}.news form{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px}.news input[type=email]{flex:1 1 240px;padding:11px 12px;border:1px solid var(--line);border-radius:8px;background:var(--surface-2);color:var(--ink);font:inherit}.hp{position:absolute;left:-9999px}
footer{border-top:1px solid var(--line);padding:24px 0 40px;color:var(--ink-3);font-size:12.5px}.mono{font-family:var(--mono)}.muted{color:var(--ink-3)}.small{font-size:13px}
"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0F1B2D">
<meta property="og:type" content="article"><meta property="og:site_name" content="Wax Ledger"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="https://thewaxledger.com/og-image.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@thewaxledger">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap">
<link rel="stylesheet" href="/static.css">
{extra}
</head>
<body>
<header><div class="wrap hdr"><a class="brand" href="/">Wax Ledger</a><nav class="nav"><a href="/#market">Market</a><a href="/#screener">Raw-to-Gem Calculator</a><a href="/#pregrade">Pre-Grading Tool</a><a href="/grade/">Grading guides</a><a href="/reviews/">Product reviews</a><a href="/#releases">Releases</a></nav><a class="btn btn-gold" href="/#membership" style="margin-left:auto">Go Pro</a></div></header>
<main><div class="wrap">
"""

TAIL = """</div></main>
<section class="news"><div class="wrap"><p class="eyebrow">Raw-to-Gem Friday</p><b>Three cards that clear the grading math. Every Friday, free.</b>
<form id="news-form"><input type="text" name="hp" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="email" id="news-email" placeholder="you@example.com" aria-label="Email address" required><button class="btn btn-gold" type="submit">Sign up</button><span class="small muted" id="news-note" style="flex-basis:100%">One email a week. Unsubscribe with one click.</span></form></div></section>
<footer><div class="wrap"><p>Wax Ledger is an independent publication. It is not affiliated with eBay, PSA, Topps, Fanatics, Panini, Upper Deck or Leaf. Nothing here is financial advice.<br><a href="mailto:info@thewaxledger.com">info@thewaxledger.com</a> · <a href="/terms.html">Terms</a> · <a href="/privacy.html">Privacy</a> · <a href="/refunds.html">Refunds &amp; cancellation</a></p><p class="mono">{stamp}</p></div></footer>
<script>
(function(){var f=document.getElementById("news-form");f.addEventListener("submit",function(e){e.preventDefault();var em=document.getElementById("news-email"),n=document.getElementById("news-note");
if(!/^[^\\s@]+@[^\\s@]+\\.[a-z]{2,}$/i.test(em.value.trim())){n.textContent="That doesn't look like an email address.";return}n.textContent="Signing you up…";
fetch("/api/newsletter",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({action:"subscribe",email:em.value.trim(),src:"{src}",hp:f.elements.hp.value})}).then(function(r){return r.json()}).then(function(j){n.textContent=j.status==="ok"?(j.already?"You're already on the list.":"You're on the list. Check your inbox for a welcome note."):(j.error||"Something went wrong. Try again in a minute.")}).catch(function(){n.textContent="Something went wrong. Try again in a minute."})});
try{if(localStorage.getItem("wl-admin")!=="1"){var p=JSON.stringify({v:"{view}",r:document.referrer||"",w:window.innerWidth<760?"m":"d",s:1,q:""});if(!(navigator.sendBeacon&&navigator.sendBeacon("/api/hit",new Blob([p],{type:"application/json"}))))fetch("/api/hit",{method:"POST",headers:{"content-type":"application/json"},body:p,keepalive:true})}}catch(e){}
})();
</script>
</body>
</html>
"""

def shell(title, desc, url, body, view, src, stamp, extra=""):
    return HEAD.format(title=esc(title), desc=esc(desc), url=esc(url), extra=extra) + body + TAIL.replace("{stamp}", esc(stamp)).replace("{src}", src).replace("{view}", view)

def card_name(c):
    return f"{c['player']} {c['year']} {c['set']} #{c['cardNo']} {c['parallel']}"

# ---------- grade pages ----------
def grade_page(c, m, related, stamp):
    name = card_name(c)
    url = f"{SITE}/grade/{c['id']}/"
    verdict = m.get("label", "No data")
    first = re.split(r"(?<=[.!?])\s", (c.get("note") or "").strip())[0] if c.get("note") else ""
    if len(first) > 220: first = first[:217].rsplit(" ", 1)[0] + "…"
    title = f"Is the {name} worth grading? {verdict}: the PSA math"
    desc = f"{name}: raw {usd(c['raw'])}, PSA 10 {usd(c['psa10'])} ({c.get('psa10Sales90') or 0} sales in 90 days), PSA 9 {usd(c['psa9'])}, gem rate {pct(m.get('gemPop'))}. Verdict: {verdict}. Data as of {c['asOf']}."
    rows = [
        ("Raw price (recent eBay sales)", usd(c["raw"]), f"{c.get('rawSales30') or 0} tracked sales"),
        ("PSA 10", usd(c["psa10"]), f"{c.get('psa10Sales90') or 0} sales in 90 days" + ("" if c.get("compType") == "Real" else " · estimate")),
        ("PSA 9", usd(c["psa9"]), "the miss outcome"),
        ("PSA population", f"{(c.get('pop10') or 0):,} tens of {(c.get('popTotal') or 0):,} graded", f"gem rate {pct(m.get('gemPop'))}" if m.get("gemPop") is not None else "no pop data yet"),
    ]
    tbl = "".join(f"<tr><td>{esc(a)}</td><td class='num'>{esc(b)}</td><td class='muted'>{esc(d)}</td></tr>" for a, b, d in rows)
    math = ""
    if m.get("code") != "NODATA":
        math = f"""<h2>The math on one attempt</h2>
<div class="tbl"><table><tr><td>All-in cost (raw + {usd(A['fee'])} grading + {usd(A['ship'])} shipping)</td><td class="num">{usd(m['allIn'])}</td></tr>
<tr><td>If it gems: PSA 10 after a {int(A['haircut']*100)}% haircut and {int(A['sellFee']*100)}% selling fee</td><td class="num">{usd(m['up10'], True)}</td></tr>
<tr><td>If it comes back a 9</td><td class="num">{usd(m['down9'], True)}</td></tr>
<tr><td>Expected profit at a {pct(m['gem'])} gem rate</td><td class="num"><b>{usd(m['profit'], True)}</b></td></tr>
<tr><td>Break-even gem rate</td><td class="num">{pct(m['be']) if m.get('be') is not None and 0 <= m['be'] <= 2 else 'n/a'}</td></tr></table></div>"""
    rel = "".join(f"<a href='/grade/{esc(r['id'])}/'>{esc(card_name(r))}<small>{esc(compute(r).get('label','No data'))}</small></a>" for r in related)
    body = f"""<p class="eyebrow">Grading guide · {esc(c['sport'])}</p>
<h1>{esc(name)}</h1>
<p class="lede">Is it worth grading? <span class="verdict v-{m.get('code','NODATA')}">{esc(verdict)}</span> &nbsp;{esc(m.get('why',''))}</p>
<div class="card"><div class="tbl"><table><tr><th>Input</th><th class="num">Value</th><th>Basis</th></tr>{tbl}</table></div></div>
{math}
{('<h2>About this card</h2><p>' + esc(first) + '</p>') if first else ''}
<div class="pro"><h2>The full breakdown is for Pro members</h2><ul><li>The complete note on this card: what moves the price, what sends it back a 9, when to buy</li><li>The math at your own grading fee, shipping and sell price, with the break-even chart</li><li>All {{N}} cards on the board, ranked by expected return, refreshed from PSA sales and pop data</li><li>The Buy/Sell/Trade board and unlimited Pre-Grading Tool runs</li></ul><a class="btn btn-gold" href="/#membership">Go Pro: $8/month or $75/year</a> &nbsp; <a class="btn" href="/#screener?card={esc(c['id'])}">Open in the calculator</a></div>
<p class="small muted">Sources: {esc(c.get('src',''))}. Data as of {esc(c['asOf'])}. Model: {usd(A['fee'])} grading fee, {usd(A['ship'])} shipping, {int(A['sellFee']*100)}% selling fee, {int(A['haircut']*100)}% haircut on the PSA 10 comp, PSA 9 realized at {int(A['missReal']*100)}%. Not financial advice.</p>
<h2>Related cards</h2><div class="grid">{rel}</div>
<p class="small"><a href="/grade/">All grading guides</a></p>
"""
    return title, desc, url, body

def grade_index(cards, stamp):
    url = f"{SITE}/grade/"
    by = {}
    for c in cards: by.setdefault(c["sport"], []).append(c)
    secs = ""
    for sport in sorted(by):
        items = sorted(by[sport], key=lambda c: (compute(c).get("code") != "GRADE", -(compute(c).get("profit") or -1e9)))
        secs += f"<h2>{esc(sport)}</h2><div class='grid'>" + "".join(f"<a href='/grade/{esc(c['id'])}/'>{esc(card_name(c))}<small>{esc(compute(c).get('label','No data'))} · PSA 10 {esc(usd(c['psa10']))}</small></a>" for c in items) + "</div>"
    body = f"""<p class="eyebrow">Grading guides</p><h1>Is it worth grading? {len(cards)} cards, one answer each</h1>
<p class="lede">Every card is priced on both outcomes, a PSA 10 and a miss, weighted by its real PSA gem rate and set against what one attempt costs. The verdict and the numbers are free; the full notes and the ranked board are for Pro members.</p>{secs}"""
    return "Is it worth grading? Raw-to-Gem guides for " + str(len(cards)) + " cards", "Raw price, PSA 10 and PSA 9 comps, real gem rates and the grading math for " + str(len(cards)) + " sports cards, with a verdict on each.", url, body

# ---------- review pages ----------
def review_page(slug, r, stamp):
    url = f"{SITE}/reviews/{slug}/"
    d = r.get("deep") or {}
    title = f"{r['n']} review: what to chase, what to skip, and whether the box is worth it"
    desc = (d.get("lede") or " ".join(r.get("facts", [])[:2]))[:300]
    bars = "".join(f"<span>{esc(b[0])}</span><span class='bar'><i style='width:{float(b[1])*10}%'></i></span><span class='mono'>{float(b[1]):.1f}</span>" for b in r.get("bars", []))
    facts = "".join(f"<li>{esc(f)}</li>" for f in r.get("facts", []))
    secs = ""
    for sec in d.get("sections", []):
        secs += f"<h2>{esc(sec['h'])}</h2><ul class='chase'>" + "".join(f"<li><b>{esc(it['c'])}</b><span class='p'>{esc(it['p'])}</span><p>{esc(it['w'])}</p></li>" for it in sec["items"]) + "</ul>"
    if d.get("avoid"): secs += "<h2>What to skip</h2><ul class='chase'>" + "".join(f"<li><p>{esc(t)}</p></li>" for t in d["avoid"]) + "</ul>"
    if d.get("notes"): secs += "<h2>Notes</h2><ul class='chase'>" + "".join(f"<li><p>{esc(t)}</p></li>" for t in d["notes"]) + "</ul>"
    body = f"""<p class="eyebrow">Product review · {esc(r.get('when',''))}</p>
<div class="top"><div><h1>{esc(r['n'])}</h1></div><div class="score">{esc(r['score'])}<small>WAX SCORE / 10</small></div></div>
<div class="card"><ul class="facts">{facts}</ul><div class="bars">{bars}</div></div>
<p class="lede">{esc(d.get('lede',''))}</p>
{secs}
<p class="small muted">{esc(d.get('src',''))}</p>
<div class="pro"><h2>Want the grading math on the cards in this review?</h2><p class="small">The Raw-to-Gem Calculator prices every card on both outcomes and tells you which ones clear the fee. Pro is $8/month or $75/year.</p><a class="btn btn-gold" href="/#membership">Go Pro</a> &nbsp; <a class="btn" href="/reviews/">All reviews</a></div>
"""
    return title, desc, url, body

def reviews_index(reviews, stamp):
    url = f"{SITE}/reviews/"
    items = "".join(f"<a href='/reviews/{esc(s)}/'>{esc(r['n'])}<small>Score {esc(r['score'])} · {esc(r.get('when',''))}</small></a>" for s, r in reviews)
    body = f"""<p class="eyebrow">Product reviews</p><h1>Is the box worth ripping?</h1><p class="lede">Every product is scored on the same four things: the rookie class, the quality of the hits, how much of it was printed, and box price against expected value. Prices are real sold data with sample sizes.</p><div class="grid">{items}</div>"""
    return "Sports card product reviews: is the box worth ripping?", "Wax Ledger product reviews with real sold prices, pull odds and a chase list for each release.", url, body

# ---------- driver ----------
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(content)

def build(stamp):
    cards = load_cards(); reviews = load_reviews()
    write(os.path.join(PUB, "static.css"), CSS)
    urls = [f"{SITE}/", f"{SITE}/grade/", f"{SITE}/reviews/"]
    n = len(cards)
    for c in cards:
        m = compute(c)
        same_player = [r for r in cards if r["player"] == c["player"] and r["id"] != c["id"]]
        same_sport = [r for r in cards if r["sport"] == c["sport"] and r["player"] != c["player"]]
        related = (same_player + same_sport)[:4]
        title, desc, url, body = grade_page(c, m, related, stamp)
        body = body.replace("{N}", str(n))
        write(os.path.join(PUB, "grade", c["id"], "index.html"), shell(title, desc, url, body, "screener", "guide", stamp))
        urls.append(url)
    title, desc, url, body = grade_index(cards, stamp)
    write(os.path.join(PUB, "grade", "index.html"), shell(title, desc, url, body, "screener", "guide-index", stamp))
    for slug, r in reviews:
        title, desc, url, body = review_page(slug, r, stamp)
        write(os.path.join(PUB, "reviews", slug, "index.html"), shell(title, desc, url, body, "reviews", "review", stamp))
        urls.append(url)
    title, desc, url, body = reviews_index(reviews, stamp)
    write(os.path.join(PUB, "reviews", "index.html"), shell(title, desc, url, body, "reviews", "review-index", stamp))
    today = datetime.date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{esc(u)}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write(os.path.join(PUB, "sitemap.xml"), sm)
    write(os.path.join(PUB, "robots.txt"), f"User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: {SITE}/sitemap.xml\n")
    return len(cards), len(reviews), len(urls)

if __name__ == "__main__":
    print(build("Beta · " + datetime.date.today().strftime("%b %-d, %Y")))
