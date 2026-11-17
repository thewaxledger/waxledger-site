"""Nov 17, 2026 singles re-pricing for the two reviews whose single-card reads were a month old: Topps Update
(singles last read Nov 2) and Topps Chrome F1 (singles last read Nov 2 for Lindblad, Oct 10 to 15 for the rest).
Source: eBay sold listings (LH_Sold=1&LH_Complete=1, newest first, 240 per search) read Nov 17 in the browser pane,
lots, cases, breaks and graded cards excluded by title. Idempotent: each review is skipped when its `when` already
carries the Nov 17 singles date."""
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

# ---------------- Topps Update ----------------
m, r = load('topps-update-2026')
if r['when'] != 'Out now · boxes Nov 16, singles Nov 17':
    r['when'] = 'Out now · boxes Nov 16, singles Nov 17'
    rep(r, ['facts', 0], '$158 a month on (35 boxes sold Nov 7 to 14, $130 to $179)',
        '$158 a month on (35 boxes sold Nov 7 to 14, $130 to $179) and $160 on Nov 15 to 16 (14 boxes, $149 to $275)')
    rep(r, ['facts', 1], '$315 on Oct 26 to Nov 1 (52 sold, $280 to $600).',
        '$315 on Oct 26 to Nov 1 (52 sold, $280 to $600), $320 on Nov 11 to 16 (5 sold, $276 to $330).')
    rep(r, ['facts', 3], 'Rookie Debuts of Griffin (US255) and McGonigle (US140) $3 to $4',
        'Rookie Debuts of Griffin (US255) and McGonigle (US140) $3 to $4. A month on (Nov 15 to 17): Griffin US1 $1.50 (39 sales), McGonigle US7 $1.89 (33), Murakami US350 $1.48 (32), the Rookie Debuts $1.75 and $2.17')
    rep(r, ['facts', 4], 'two have sold so far ($80 and $1,000), neither a Griffin or McGonigle',
        'the Griffin US1 has now sold four times, $475 to $600 Nov 6 to 10 ($512 median), the McGonigle US7 once at $390 (Nov 10), and the Benge that opened at $1,000 resold for $400 (Nov 10)')
    rep(r, ['deep', 'sections', 0, 'items', 0, 'p'], 'Two sales: Sam Antonacci US301 $80 (Oct 15), Carson Benge US3 $1,000 (Oct 14). 1 in 5,952 hobby packs',
        'Griffin US1 $512 median (4 sales Nov 6 to 10: $550, $475, $600, $340) · McGonigle US7 $390 (Nov 10) · Benge US3 $1,000 (Oct 14) then $400 (Nov 10) · Hao-Yu Lee US111 $160 to $295 (4) · Antonacci US301 $80 to $130 (3) · Painter US63 $50 to $85 (4) · the rest $7 to $55. Autograph version: Bazzana /10 $2,000 (Nov 6), Crawford /10 $123.50, Susac Red Ink /5 $180. 1 in 5,952 hobby packs')
    rep(r, ['deep', 'sections', 0, 'items', 0, 'w'], 'No Griffin or McGonigle has sold yet; the $1,000 Benge is a day-one ask that was met once, not a market.',
        'The Griffin has settled at about $500 and the Benge fell from $1,000 to $400 once a second copy surfaced, which is the pattern for every SSP in this set.')
    rep(r, ['deep', 'sections', 0, 'items', 1, 'p'], 'Golden Mirror autographs $200 to $900 (6). 1 in 606 hobby packs',
        'Golden Mirror autographs $200 to $900 (6). A month on (Nov 10 to 17): $42 median on 178 sales; Nolan Ryan Legend $1,400 and $1,500, Griffey $1,051, Rivera $305, Mathews $600, Randy Johnson $649; Golden Mirror autographs Witt Real One redemption $2,700 and $989, Yamamoto $2,000, Freeman $1,650, Acuña Gold Ink $900, Harris $800, Albies $750. 1 in 606 hobby packs')
    rep(r, ['deep', 'sections', 0, 'items', 2, 'p'], 'Murakami Black Sandglitter /10 Rookie Debut $499 (1). Odds:',
        'Murakami Black Sandglitter /10 Rookie Debut $499 (1). Nov 15 to 17: Griffin Gold /2026 $8.50 to $50 (4) · Griffin Orange Sandglitter /25 (US99) $135 · Griffin Purple /250 Rookie Debut $26 · Griffin Black /75 (US99) $79 · McGonigle Blue /150 $34 · McGonigle Purple /250 $29 and $30 · McGonigle Gold /2026 $21 and $37 · McGonigle Gold Holo /50 $129. Odds:')
    rep(r, ['deep', 'sections', 0, 'items', 4, 'p'], 'No Griffin, McGonigle or Wetherholt autograph has sold',
        'A month on: $38 median on 173 autographs sold Nov 15 to 17; McGonigle 1991 Topps auto Blue /150 $240 (Nov 17), Murakami ASG auto /26 $500 (Nov 16). No Griffin or Wetherholt autograph has sold')
    rep(r, ['deep', 'sections', 1, 'items', 0, 'p'], 'US1 base $2.29 (45, $0.99 to $9.99) · US255 Rookie Debut $2.92 (21)',
        'US1 base $2.29 (45, $0.99 to $9.99) on day one, $1.50 (39, $0.60 to $5) Nov 15 to 17 · US255 Rookie Debut $2.92 (21) on day one, $1.75 (7) Nov 16')
    rep(r, ['deep', 'sections', 1, 'items', 0, 'w'], 'Buy the numbered parallels or nothing.',
        'A month on the base is $1.50 and the Gold /2026 has slipped from $40 to $50 to $8.50 to $50. Buy the numbered parallels or nothing.')
    rep(r, ['deep', 'sections', 1, 'items', 1, 'p'], 'US7 base $3.49 (51, $1.25 to $20, most under $4) · US140 Rookie Debut $4 (23)',
        'US7 base $3.49 (51, $1.25 to $20, most under $4) on day one, $1.89 (33) Nov 15 to 17 · US140 Rookie Debut $4 (23) on day one, $2.17 (8) Nov 16')
    rep(r, ['deep', 'sections', 1, 'items', 1, 'w'], 'Expect $2 to $3 for the base once more hobby cases are open.',
        'A month on the base is $1.89, a dollar under where it opened; his 1952 variation sold once at $390.')
    rep(r, ['deep', 'sections', 1, 'items', 2, 'p'], 'US350 $2.22 (12, $0.99 to $9.99)',
        'US350 $2.22 (12, $0.99 to $9.99) on day one, $1.48 (32) Nov 15 to 17')
    rep(r, ['deep', 'sections', 1, 'items', 3, 'p'], 'Benge 1952 Rookie Variation $1,000 (1). Base cards $1 to $3',
        'Benge 1952 Rookie Variation $1,000 (Oct 14), then $400 (Nov 10) · Bazzana 1952 Rookie Variation Auto /10 $2,000 (Nov 6). Base cards $1 to $3')
    rep(r, ['deep', 'sections', 2, 'items', 1, 'p'], 'Griffin Gold /2026 $38 to $75 (6) · McGonigle Gold /2026 $50 to $60 (4).',
        'Griffin Gold /2026 $38 to $75 (6) on day one, $8.50 to $50 (4) Nov 15 to 16 · McGonigle Gold /2026 $50 to $60 (4) on day one, $21 and $37 a month on.')
    rep(r, ['deep', 'avoid', 1], 'The base rookies cost $2 to $3.50 each on day one and will cost less next week.',
        'The base rookies cost $2 to $3.50 each on day one and $1.50 to $1.90 a month later.')
    rep(r, ['deep', 'notes', 5], 'Still pending: a Griffin or McGonigle 1952 Rookie Variation sale, any Griffin, McGonigle or Wetherholt autograph, and odds for the Home Field, All Kings and Heavy Lumber SSP inserts. Next refresh after the first full week of sales.',
        'Still pending: any Griffin or Wetherholt autograph, and odds for the Home Field, All Kings and Heavy Lumber SSP inserts. The Griffin and McGonigle 1952 Rookie Variations have now sold (Nov 6 to 10, above).')
    rep(r, ['deep', 'notes', 6], 'numbered parallels of Griffin and McGonigle at $80 to $85 for the /250 to /75 colors,',
        'numbered parallels of Griffin and McGonigle, which a month on are $26 to $34 for the /250 and /150 colors and $79 for the /75,')
    r['deep']['notes'].insert(1, 'Singles re-priced Nov 17 (eBay sold listings read Nov 17 in the browser pane, lots, cases, breaks and graded cards excluded): Griffin US1 base $1.50 median on 39 sales Nov 15 to 17 ($0.60 to $5; one $100 outlier excluded), US255 Rookie Debut $1.75 (7); McGonigle US7 base $1.89 (33), US140 Rookie Debut $2.17 (8); Murakami US350 $1.48 (32). Golden Mirror variations $42 median on 178 sales Nov 10 to 17. Autographs $38 median on 173 sales Nov 15 to 17. 1952 Rookie Variations: Griffin US1 $549.99 and $474.99 (Nov 6), $600 (Nov 7), $340 (Nov 10); McGonigle US7 $390 (Nov 10); Benge US3 $400 (Nov 10); Hao-Yu Lee US111 $200, $160, $175, $295 (Nov 5 to 16); Antonacci $86, $130, $80; Painter $76, $70, $50, $85. Hobby box $160 median on 14 single boxes Nov 15 to 16 ($149 to $275); jumbo $320 median on 5 Nov 11 to 16 ($276 to $330). The day-one reads are kept beside the new ones so the drift is visible.')
    rep(r, ['deep', 'src'], 'Single-card prices: eBay sold listings, Oct 14 to 15, medians with counts where five or more sold, otherwise individual sales.',
        'Single-card prices: eBay sold listings, Oct 14 to 15 (day one) and Nov 15 to 17 (a month on, read Nov 17 in the browser pane), medians with counts where five or more sold, otherwise individual sales.')
    rep(r, ['deep', 'lede'], 'The short version has not changed: the rookie class is the best in years, the base cards are already $2 to $3.50, and the hobby box still sells for about $70 over what Topps charged.',
        'Singles re-priced Nov 17, a month on: the base rookies have halved ($1.50 Griffin, $1.89 McGonigle), the Griffin 1952 variation has found a $500 level on four sales, and the hobby box is $160. The short version has not changed: the rookie class is the best in years, the base cards are $1.50 to $2, and the hobby box still sells for about $50 over what Topps charged.')
    save(m, r)

# ---------------- Topps Chrome F1 ----------------
m, r = load('topps-chrome-f1-2026')
if r['when'] != 'Out now · boxes Nov 16, singles Nov 17':
    r['when'] = 'Out now · boxes Nov 16, singles Nov 17'
    rep(r, ['facts', 0], '$630 a month on (69 boxes sold Nov 1 to 14, $560 to $900), down from $948 in presale',
        '$630 a month on (69 boxes sold Nov 1 to 14, $560 to $900; $630 on the 12 sold Nov 10 to 16, $600 to $695), down from $948 in presale')
    rep(r, ['facts', 3], 'His F1 Debut Patch Autograph is a 1/1',
        'His F1 Debut Patch Autograph is a 1/1. A month on, the #12 base is $2.60 (8 sales Nov 10 to 15) and the Refractor $5.50 to $19 (13 sales Nov 8 to 16)')
    rep(r, ['facts', 4], '18 single cards have sold on eBay since',
        '18 single cards had sold on eBay by Oct 13; by Nov 17 every tier below has a read (base autographs $24 median on 42 sales Nov 15 to 17)')
    rep(r, ['deep', 'sections', 0, 'items', 0, 'p'], 'Prices pending. One early sale each:',
        'Base Chrome Autographs (unnumbered) $24 median on 42 sales Nov 15 to 17: legends and F2, F3 and F1 Academy drivers $6 to $50, Hadjar $87 and his Vuelta 1 $116.50, Colapinto Vuelta 1 $51, Hülkenberg $47 and $51, Albon $39. All autographs including parallels $27 median (230 sales Nov 14 to 17). Top of the market: Podium Triple Red /5 Verstappen, Russell and Sainz $9,000 (Nov 16), Norris, Piastri and Leclerc Podium /5 $8,600 (Nov 14), Hamilton Purple /75 $3,250 (Nov 15), Norris Vuelta 1 Orange /25 $2,200 (Nov 16), Norris Gold /50 $560, Pérez Orange /25 $1,225. First Day Issue sales from October:')
    rep(r, ['deep', 'sections', 0, 'items', 0, 'w'], 'The two sales above are First Day Issue parallels numbered to 15, so they are a ceiling, not a guide to a base autograph.',
        'A base autograph is a $24 card unless the signer is on the 2026 grid; the four- and five-figure sales are numbered parallels of the title contenders and the Podium Triples.')
    rep(r, ['deep', 'sections', 0, 'items', 1, 'p'], 'No sales yet',
        '#12 base $2.60 median (8 sales Nov 10 to 15, $1 to $9) · #12 Refractor $5.50 to $19 (13 sales Nov 8 to 16, $9.50 median) · Prism Refractor $1 to $10 (3) · Purple RayWave /75 $61 · Green RayWave /99 $48 · Futuro FUT-1 $49 (Nov 16) · Helix SSP $500 (Nov 17) · Helmet Collection HC-12 $11 to $17.50 (5). Autographs (Nov 2 read): Aqua $256, Checker /10 $1,000, Red Checker /5 $2,300')
    rep(r, ['deep', 'sections', 0, 'items', 2, 'p'], 'Prices pending',
        'Nov 13 to 17: Norris Black /10 $455 · Verstappen Gold /50 (Grand Prix Winner #132) $145 · Verstappen Gold Checker /50 $100 · Verstappen Helmet Collection /199 $380 · Hamilton Helmet Collection Green /99 $365 · Hamilton Austin to Mexico City Orange /25 $300 · Verstappen and Hadjar duo Orange /25 $42 · Norris Gold Prism /50 $13.50 and $35 · Verstappen Blue /150 $12.88, Green RayWave /99 $20, Aqua /199 $6.74 · Hamilton Aqua /199 $7 · Norris Green /99 $4.25')
    rep(r, ['deep', 'sections', 0, 'items', 3, 'p'], 'Prices pending',
        'Verstappen Genesis $102.50 (Nov 16) · Lindblad Helix $500 (Nov 17); no Chrome Anime or Grail sale in the Nov 14 to 17 pages')
    rep(r, ['deep', 'sections', 1, 'items', 0, 'p'], 'Early sales, Oct 12 to 13: Verstappen $40 · Russell, Gasly and Perez $15 each',
        'Early sales, Oct 12 to 13: Verstappen $40 · Russell, Gasly and Perez $15 each. A month on (Nov 15 to 17): Verstappen HC-5 $35 median (14 sales, $20.50 to $40) · Hamilton HC-8 $16 and $16.50 · Lindblad HC-12 $11 to $17.50 (5)')
    rep(r, ['deep', 'sections', 1, 'items', 1, 'p'], 'Early sales: Antonelli Speed Wheels $25 (Oct 11) · Verstappen Austin to Mexico City $14.99 (Oct 10)',
        'Early sales: Antonelli Speed Wheels $25 (Oct 11) · Verstappen Austin to Mexico City $14.99 (Oct 10). A month on: Verstappen Austin to Mexico City $3.49, Dancing in the Rain $3 to $5.60 · Hamilton Dancing in the Rain $3.25, Speed Wheels $0.99 · Antonelli Dancing in the Rain $4 · Norris Dancing in the Rain $2 · Lindblad Austin to Mexico City and Dancing in the Rain $1')
    rep(r, ['deep', 'sections', 1, 'items', 2, 'p'], 'One early sale: Nikola Tsolov #26 Prism Refractor $4 (Oct 11)',
        'One early sale: Nikola Tsolov #26 Prism Refractor $4 (Oct 11). A month on: Verstappen Prisms $1.50 to $3.25 (5 sales Nov 15, assorted subset numbers) · Antonelli #4 Prism $16.15 · Lindblad #12 Prism $1 to $10 (3)')
    rep(r, ['deep', 'sections', 2, 'items', 0, 'p'], 'One early sale: George Russell #120 Grand Prix Winner $4 (Oct 13). The rest pending',
        'One early sale: George Russell #120 Grand Prix Winner $4 (Oct 13). A month on: Verstappen #5 $2.43 to $3.50 (3 sales Nov 14 to 16) · Antonelli #4 $1 · Norris #1 $0.60 · Lindblad #12 $2.60 (8) · Verstappen subset cards (Grand Prix Winner, Driver of the Day) $1 to $3.25')
    rep(r, ['deep', 'sections', 2, 'items', 1, 'p'], 'One early sale: Ayrton Senna numbered refractor $14.99 (Oct 12; the listing calls it Green /199, and the checklist has Green /99 and Aqua /199)',
        'One early sale: Ayrton Senna numbered refractor $14.99 (Oct 12; the listing calls it Green /199, and the checklist has Green /99 and Aqua /199). A month on: Verstappen Blue /150 $12.88, Green RayWave /99 $20, Aqua /199 $6.74 · Hamilton Aqua /199 $7 · Norris Green /99 $4.25 · Antonelli Driver of the Day Pink /250 $26 · Lindblad #100 Aqua /199 $1.25 and $3.26')
    rep(r, ['deep', 'avoid', 0], 'Paying $850 for a hobby box that Topps sold for $469.99 and $479.99 on release day. The 31 single boxes sold on eBay in presale had a $935 median; the 10 sold Oct 13 to 15 are at $850.',
        'Paying $630 or more for a hobby box that Topps sold for $469.99 and $479.99 on release day. The 31 single boxes sold on eBay in presale had a $935 median; the 10 sold Oct 13 to 15 were $850; a month on it is $630 (12 sold Nov 10 to 16), still $150 over Topps.')
    rep(r, ['deep', 'notes', 8], 'At $850 it is a pass. Wait for hobby cases to open and buy singles.',
        'At $850 it was a pass and at $630 a month on it still is: the one autograph is a $24 card unless the signer is a current F1 driver, and the base and inserts of the top drivers are $1 to $5. Buy singles.')
    r['deep']['notes'].insert(1, 'Singles re-priced Nov 17 (eBay sold listings read Nov 17 in the browser pane, lots, cases, breaks, Sapphire, LogoFractor, Red Envelope and graded cards excluded): base Chrome Autographs $24.25 median on 42 unnumbered sales Nov 15 to 17 ($5.77 to $116.50); all autographs $27 median on 230 sales Nov 14 to 17. Lindblad #12 base $2.60 median on 8 sales Nov 10 to 15, Refractor $9.50 median on 13 sales Nov 8 to 16 ($1.25 to $19). Verstappen Helmet Collection HC-5 $35 median on 14 sales Nov 15 to 17. Verstappen #5 base $2.43, $2.99 and $3.50 (Nov 14 to 16). Hobby box $630 median on 12 single boxes Nov 10 to 16 ($599.99 to $694.95), the same level as the Nov 14 read.')
    rep(r, ['deep', 'src'], 'Single-card prices: eBay sold listings, Oct 10 to 13, individual early sales from First Day Issue boxes.',
        'Single-card prices: eBay sold listings, Oct 10 to 13 (individual early sales from First Day Issue boxes) and Nov 8 to 17 (a month on, read Nov 17 in the browser pane), medians with counts where five or more sold.')
    rep(r, ['deep', 'lede'], 'Single-card prices are not a market yet: only First Day Issue boxes have been opened, and 18 cards sold between Oct 10 and Oct 13. Those are listed as individual sales, not medians.',
        'Singles re-priced Nov 17, a month after release: a base autograph is $24 (42 sales), Lindblad\'s rookie card is $2.60 and his Refractor $9.50, Verstappen\'s base is $3 and his Helmet Collection insert $35, and the hobby box is $630. The October single-card reads (18 early sales from First Day Issue boxes) are kept beside the new ones.')
    save(m, r)

open(P, 'w').write(s)
print('ok')
