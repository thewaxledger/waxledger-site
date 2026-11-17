"""Nov 17, 2026 re-pricing from eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 17 in the browser pane.
Topps Chrome Football (releases Nov 18): the Nov 16 review had no sold read (browser pane down), so its box line was
asking prices. This replaces it with the presale sales: 40 single hobby boxes Nov 12 to 16, 5 jumbo boxes, 3 cases, one
FDI jumbo. Singles stay pending: an eBay search for 2026 Topps Chrome Football First Day Issue / Molten Mercury singles
(FDI boxes shipped Nov 13) returned one sale (Lenoir Molten Mercury 1/6, $40, Nov 11), and a Mendoza search returned only
Bowman, Flagship, Heritage and Holiday cards. Idempotent: each edit asserts the old text and is skipped when applied."""
import json, os, re
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

def load(slug):
    m = re.search(r'^( /\* ' + re.escape(slug) + r' \*/)(\{.*\})(,?)$', s, re.M)
    assert m, slug
    return m, json.loads(m.group(2))

def save(m, obj):
    global s
    line = m.group(1) + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + m.group(3)
    s = s[:m.start()] + line + s[m.end():]

def rep(obj, path, old, new):
    cur = obj
    for k in path[:-1]: cur = cur[k]
    v = cur[path[-1]]
    if new in v and old not in v: return
    assert old in v, (path, old[:60])
    cur[path[-1]] = v.replace(old, new)

m, r = load('topps-chrome-fb-2026')
if r['when'] != 'Out Nov 18 · boxes Nov 16 (presale sales), singles pending':
    r['when'] = 'Out Nov 18 · boxes Nov 16 (presale sales), singles pending'
    rep(r, ['facts', 0], 'Street before release (asking, not sales): $569.99 to $704.99 across ten retailers in stock on Waxstat Nov 15 ($617 listed median, $662 average), and $565.99 to $580 for the five lowest eBay Buy It Nows on Nov 15 per Cardsmiths Breaks. No sold read yet',
        'eBay sold (presale boxes): $575 median on 40 single hobby boxes Nov 12 to 16 ($559 to $799.99; 36 of the 40 between $559 and $600), $580 on the 15 sold Nov 16. Retailer asking prices Nov 15 were $569.99 to $704.99 (Waxstat, ten in stock). The street has the box at $135 over Topps before a pack is opened')
    rep(r, ['facts', 1], '$789.99 at the same presale. First Day Issue jumbo',
        '$789.99 at the same presale; eBay sold $990 median on 5 presale jumbo boxes Nov 12 to 16 ($950 to $1,299). 12-box hobby cases $7,250 to $7,995.95 (3 sales Nov 13 to 15, $604 to $666 a box). First Day Issue jumbo')
    rep(r, ['facts', 1], 'shipped Nov 13): the same 132 cards',
        'shipped Nov 13; one eBay sale $2,336.99 on Nov 16): the same 132 cards')
    rep(r, ['deep', 'lede'], 'Written Nov 16, two days before release (Nov 18), with no sold prices: the browser pane was down, so the box figures below are retailer and eBay asking prices and every single is pending.',
        'Written Nov 16 and re-priced Nov 17, the day before release (Nov 18): the box figures are now eBay presale sales; every single is still pending (the FDI jumbo boxes shipped Nov 13, but only one FDI single, a Lenoir Molten Mercury 1/6 at $40, has a completed sale).')
    rep(r, ['deep', 'lede'], 'the street is asking $566 to $705 before a single hobby box has been opened, which is where the 2025 box has been trading on StockX all autumn ($588 average on 13 sales, from $349.99 at release).',
        'the street is paying $575 (median of 40 presale boxes sold on eBay Nov 12 to 16, 36 of them between $559 and $600) before a single hobby box has been opened, which is where the 2025 box has been trading on StockX all autumn ($588 average on 13 sales, from $349.99 at release).')
    rep(r, ['deep', 'lede'], 'Until the first cases are broken the numbers to fill in are the box\'s sold median against $440 and $600, and where a plain Mendoza Rookie Variation Autograph opens.',
        'Until the first cases are broken the numbers to fill in are whether the $575 presale box holds through release week, and where a plain Mendoza Rookie Variation Autograph opens.')
    rep(r, ['deep', 'avoid', 0], 'Paying $570 to $700 for a box before the first cases are broken.',
        'Paying $575 or more for a box before the first cases are broken (40 presale boxes sold at that median Nov 12 to 16).')
    r['deep']['notes'].append('Prices Nov 16 (eBay sold listings read Nov 17 in the browser pane; cases, lots, mega boxes, FDI boxes and 2025 boxes excluded by title): single hobby boxes $575 median on 40 sales Nov 12 to 16 ($559 to $799.99, $590.53 average; two outliers at $799.99, the rest $559 to $625), by day Nov 12 six ($559 to $579.99), Nov 13 four ($565 to $799.99), Nov 14 nine ($564 to $625), Nov 15 six ($565.99 to $799.99), Nov 16 fifteen ($574.95 to $599.95, $580 median). Jumbo hobby boxes $989.99 median on 5 sales Nov 12 to 16 ($950, $975, $989.99, $999.95, $1,299). 12-box hobby cases $7,300 (Nov 13), $7,250 and $7,995.95 (Nov 15). FDI jumbo box $2,336.99 (Nov 16, one sale; Dutch auction closed at $2,500). Mega box presale $99.99 (Nov 12, one sale; $79.99 at Topps Dec 2). Singles: a search for 2026 Topps Chrome Football First Day Issue / Molten Mercury singles returned one completed sale (Deommodore Lenoir Molten Mercury 1/6, $40, Nov 11); a Mendoza search returned only his Bowman, Flagship, Heritage and Holiday cards (Bowman Chrome Rookie Autograph /499 $760 and $550, Blue /150 $898, Nov 15 to 16). The asking-price figures in the Nov 16 note are kept for the record.')
    rep(r, ['deep', 'src'], 'No eBay sold read for this review: the browser pane was unavailable on Nov 16, so no 2026 single or box sale is quoted; every 2026 price is marked pending or labelled as an asking price.',
        'Box prices: eBay sold listings (LH_Sold=1&LH_Complete=1), read Nov 17 in the browser pane, sales Nov 12 to 16; singles are pending because no 2026 Topps Chrome Football single beyond one FDI parallel had a completed sale by Nov 17. The Nov 16 draft had no sold read (the browser pane was unavailable that day).')
    save(m, r)

open(P, 'w').write(s)
print('ok')
