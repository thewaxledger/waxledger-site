"""Nov 18, 2026 re-pricing from eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 18 (about 22:00 UTC) in the
browser pane. Topps Chrome Football released today: the first singles sold, so the "pending" lines get release-day
numbers. Searches: "2026 topps chrome football" + mendoza refractor 351 / mendoza auto / mendoza /50 / mendoza /25 /
mendoza image variation / ty simpson / jeremiyah love / carson beck / sonny styles / jordyn tyson / makai lemon /
prem1ere patch auto / tecmo auto / hobby box / jumbo box / first day issue, newest first, 240 per search; titles with
Bowman, Heritage, Flagship (91TRC), Holiday, Inception, Midnight, 2025, lots and breaks excluded by title.
Idempotent: each edit asserts the old text and is skipped when applied."""
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
if r['when'] != 'Out Nov 18 · boxes and singles Nov 18 (release day)':
    r['when'] = 'Out Nov 18 · boxes and singles Nov 18 (release day)'
    rep(r, ['facts', 0], 'eBay sold (presale boxes): $575 median on 40 single hobby boxes Nov 12 to 16 ($559 to $799.99; 36 of the 40 between $559 and $600), $580 on the 15 sold Nov 16.',
        'eBay sold: $589.99 median on 31 single hobby boxes Nov 17 to 18 ($549.99 to $650; 13 of them on release day at the same median), $579 on 79 boxes Nov 12 to 18. The presale week was $575 on 40 boxes Nov 12 to 16.')
    rep(r, ['facts', 0], 'The street has the box at $135 over Topps before a pack is opened',
        'The street has the box at $150 over Topps on release day')
    rep(r, ['facts', 1], 'eBay sold $990 median on 5 presale jumbo boxes Nov 12 to 16 ($950 to $1,299).',
        'eBay sold $991 median on 21 single jumbo boxes Nov 12 to 18 ($945 to $1,359.99; $999.99 on the 11 sold Nov 17 to 18).')
    rep(r, ['facts', 1], 'shipped Nov 13; one eBay sale $2,336.99 on Nov 16)',
        'shipped Nov 13; eBay sales $2,500 Nov 10, $2,336.99 Nov 16 and $2,325 Nov 17)')
    rep(r, ['deep', 'lede'], 'Written Nov 16 and re-priced Nov 17, the day before release (Nov 18): the box figures are now eBay presale sales; every single is still pending (the FDI jumbo boxes shipped Nov 13, but only one FDI single, a Lenoir Molten Mercury 1/6 at $40, has a completed sale).',
        'Written Nov 16 and re-priced on release day, Nov 18, from the first day of eBay sales: the Mendoza Refractor opened at $65 (32 sales), his base card at $10 (17 sales), and the hobby box held at $589.99 (31 sales Nov 17 to 18). No plain Mendoza, Simpson, Love or Beck Rookie Variation Autograph had sold by the evening of release day; the one Mendoza autograph sale is an FDI Molten Mercury 2/6 at $7,400 (Nov 17).')
    rep(r, ['deep', 'lede'], 'the street is paying $575 (median of 40 presale boxes sold on eBay Nov 12 to 16, 36 of them between $559 and $600) before a single hobby box has been opened,',
        'the street paid $575 for it in presale (40 boxes Nov 12 to 16) and $589.99 on release day (31 boxes Nov 17 to 18, $549.99 to $650),')
    rep(r, ['deep', 'lede'], 'Until the first cases are broken the numbers to fill in are whether the $575 presale box holds through release week, and where a plain Mendoza Rookie Variation Autograph opens.',
        'Day one puts the Mendoza Refractor at $65 and his base at $10, Simpson and Love Refractors under $10, and the other rookies\' base and inserts at $1 to $8: a $589.99 hobby box is paying for the autograph slot and for a Mendoza colour (Yellow /275 $120 up to Purple /75 $350 so far), and the number still to fill in is where a plain Mendoza Rookie Variation Autograph opens, since the only sale so far is the FDI 2/6 at $7,400.')
    t1 = r['deep']['sections'][0]['items']
    rep(t1[0], ['p'], 'Prices pending (release Nov 18; FDI singles shipped Nov 13 but were not read). Comp:',
        'Release day, Nov 18 (eBay sold): Refractor $65 median on 32 sales ($20 to $250; 26 of the 32 between $50 and $100); base #351 $10 median on 17 sales ($4.50 to $49.99); Yellow /275 $119.99 (1); Blue /150 $159.99 and $500 (2); Aqua Lava /199 $274 and $300 (2); Purple /75 $350 (1); Prism $150, Wave $179.99, RayWave $99.99, Pulsar $75 and $88, Football Leather $75 to $100 (3), Red White & Blue $29.99 to $49.99 (3); Image Variation $75 and $180 (2). Rookie Variation Autograph: no plain sale yet; FDI Molten Mercury autograph 2/6 $7,400 (Nov 17). No Gold /50, Orange /25, Black /10 or Red /5 sold yet. Comp:')
    rep(t1[1], ['p'], 'Prices pending. Comp:',
        'Release day, Nov 18 (eBay sold): Simpson Blue Lava /150 $40 and Pink /250 $29.95, Refractor $2 to $6 (4), base $2.50 to $3 (3); Love Blue /150 $49.99, base $1.25 to $5 (3); Beck Blue RayWave /150 $30, Football Leather $8.95, Refractor $6 and $14.99, base $1.99. No autograph of the three sold yet. Comp:')
    rep(t1[2], ['p'], 'Prices pending', 'No sale yet (eBay sold searched Nov 18 for Prem1ere Patch and Debut Patch: none completed)')
    rep(t1[3], ['p'], 'Prices pending', 'Nov 18 (eBay sold, titled as Tecmo inserts, numbering not stated in the titles): Joe Burrow TECMO-11 $3,500, Jerry Rice TECMO-5 $1,200 (one each). No Chromograph or Gold Shield sale yet')
    t2 = r['deep']['sections'][1]['items']
    rep(t2[0], ['p'], 'Prices pending', 'Nov 18 (eBay sold): Mendoza Yellow /275 $119.99, Blue /150 $159.99 and $500, Aqua Lava /199 $274 and $300, Purple /75 $350; Simpson Blue Lava /150 $40 and Pink /250 $29.95; Love Blue /150 $49.99; Beck Blue RayWave /150 $30; Tyson White /30 $119.99 (Nov 17); Styles Gold Pulsar /50 $50. One or two sales each')
    rep(t2[1], ['p'], 'Prices pending', 'No 2026 Chrome Football veteran numbered Refractor or Chrome Etch sale found by Nov 18 (a Mahomes search returned only his Holiday Blue /150 at $24.99)')
    rep(t2[2], ['p'], 'Prices pending', 'Nov 17 to 18 (eBay sold, one each): Styles Rookie Autograph Aqua Lava /199 $399.99; Emmett Johnson Refractor autograph /499 $100; Jalon Daniels Blue Lava /150 $50; Tez Johnson Aqua /199, Taurean York Blue /150 and Jalon Kilgore base $19.99 each; Jermod McCoy Magenta /399 $10. No Mendoza, Simpson, Love or Beck plain autograph yet')
    rep(t2[3], ['p'], 'Prices pending', 'Mendoza, Nov 18 (eBay sold): Destiny D-15 $19 to $30 (6), Instinct INS-20 $10 to $30 (11), Serenity SY-16 $15 to $40 (5), Ball of Duty BD-14 $7.50 to $18 (5), Activators A-16 $2 to $20 (6), Touchdown Theory TT-14 $20 (2), Day 1 $20, Grid Lock $19.99. Simpson, Love, Beck and Tyson inserts $3 to $8')
    t3 = r['deep']['sections'][2]['items']
    rep(t3[0], ['p'], 'Prices pending', 'Nov 18 (eBay sold): Mendoza base $10 median on 17 sales ($4.50 to $49.99) and Refractor $65 median on 32; Simpson base $2.50 to $3, Love $1.25 to $5, Beck $1.99, Styles $3 to $5.26, Tyson $4, Lemon $3.25; Tyson Refractor $2 to $10 (5), Simpson Refractor $2 to $6 (4)')
    rep(t3[1], ['p'], 'Prices pending', 'Nov 18 (eBay sold): Mendoza Ball of Duty $7.50 to $18 (5), his Grid Lock $19.99; other players\' veteran inserts not yet searched')
    rep(t3[2], ['p'], 'Prices pending', 'Mega ships Dec 2; hanger and blaster exclusives seen as singles Nov 18: Mendoza Pulsar $75 and $88, RayWave $99.99, Football Leather $75 to $100 (3). No retail box sale read')
    rep(r, ['deep', 'avoid', 0], 'Paying $575 or more for a box before the first cases are broken (40 presale boxes sold at that median Nov 12 to 16).',
        'Paying $590 or more for a box on the release-day pattern (31 boxes sold at a $589.99 median Nov 17 to 18, after $575 in presale).')
    rep(r, ['deep', 'avoid', 1], 'the single will cost less than the box in week one, as his Inception and Midnight autographs did.',
        'the single will cost less than the box in week one, as his Inception and Midnight autographs did (no plain one had sold by the evening of release day).')
    r['deep']['notes'].append('Prices Nov 18, release day (eBay sold listings read about 22:00 UTC Nov 18 in the browser pane; Bowman, Heritage, Flagship, Holiday, Inception, Midnight, 2025, lots and breaks excluded by title): single hobby boxes $589.99 median on 31 sales Nov 17 to 18 ($549.99 to $650) and $579 on 79 sales Nov 12 to 18; jumbo $991 median on 21 single boxes Nov 12 to 18 ($945 to $1,359.99); FDI jumbo $2,325 (Nov 17). Mendoza: Refractor $65 median on 32 sales Nov 18 (sorted: $20, $20, $25, $25, $35, $50, $50, $55, five at $59.99, $64.99, three at $65, $74.99, $75, $84, $85, $99.97, two at $99.99, six at $100, $125, $250); base #351 $10 median on 17 ($4.50 to $49.99); colours one or two sales each as listed in Tier 1. Every count and range in the tiers is from the same read; a line that says "no sale yet" means the search returned no completed 2026 Chrome Football listing of that card by then.')
    rep(r, ['deep', 'src'], 'Box prices: eBay sold listings (LH_Sold=1&LH_Complete=1), read Nov 17 in the browser pane, sales Nov 12 to 16; singles are pending because no 2026 Topps Chrome Football single beyond one FDI parallel had a completed sale by Nov 17.',
        'Box and single prices: eBay sold listings (LH_Sold=1&LH_Complete=1), read Nov 18 (release day, about 22:00 UTC) in the browser pane, sales Nov 12 to 18 for boxes and Nov 17 to 18 for singles; counts, ranges and dates stated per line. The Nov 17 read (presale boxes only, singles pending) is superseded.')
    save(m, r)

open(P, 'w').write(s)
print('ok')
