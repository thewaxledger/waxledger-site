"""Nov 15, 2026 re-pricing from eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 14-15 in the browser pane.
Midnight Football (released Nov 13): release-day hobby boxes and the first hobby-box singles. Museum Collection
(released Nov 11): first-week boxes and singles. Seven reviews whose box prices dated Nov 1 (Donruss Football, Chrome F1,
Topps Update, Series 1 Hockey, Allen & Ginter, Bowman Chrome Sapphire, Bowman Football) get a fresh box line.
Idempotent: each edit asserts the old text and is skipped when already applied. Counts, ranges and date windows are stated
per line; break slots, lots, cases, hot packs, complete sets, FDI boxes and 'you pick' listings excluded by title. eBay
returns at most 240 sold listings per search (newest first), so for high-volume products the window is as deep as that
page reached and the oldest date is stated. PSA was not consulted for these (no graded single-card prices)."""
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
    if new in v and old not in v: return  # already applied
    assert old in v, (path, old[:60])
    cur[path[-1]] = v.replace(old, new)

# ---------------------------------------------------------------- Midnight Football: release day (Nov 13-14)
m, r = load('topps-midnight-fb-2026')
if r['when'] != 'Out Nov 13 · prices Nov 14':
    r['when'] = 'Out Nov 13 · prices Nov 14'
    rep(r, ['facts', 0], 'eBay sold (presale boxes): $680 median on 43 single hobby boxes Oct 12 to Nov 11 ($635 to $1,000), $680 on the 14 sold in November ($635 to $775); the first week of presale flips went $720 median (11 sales Oct 12 to 19)',
        'eBay sold since release: $650 median on 11 single hobby boxes Nov 13 to 14 ($580 to $675), down from $680 on 43 presale boxes Oct 12 to Nov 11 and $720 in the first week of presale flips')
    r['facts'][7] = ('First hobby-box singles (eBay sold Nov 12 to 14): autographs $100 median on 40 sales titled as autographs ($0.99 to $699): Allar Rookie Jersey Autograph /12 $699, JSN Dark Matter $550, Barry Sanders Dark Matter /20 $500, Tate REM relic autograph /20 $300, Downs Tenebrous Traces $250 and $202.50, Love Rookie Autograph /125 $225 and Midnight Oil Marks $140, Beck patch autograph $127.50 and Rookie Autograph $75, Reese Tenebrous Traces $130 to $175 (4), Emmett Johnson Midnight Oil Marks /35 $175 and /99 $49, Concepcion Midnight Oil Marks /99 $126, Sadiq Rookie Autograph $85; veterans\' Countdown Calligraphy $20 to $100 (Witten /50 $52 and $66, Likely $99.99 twice, Gates $20). '
                    'Mendoza: no autograph sold yet; Rookie Refractor SP #21 $102.64 (Nov 14), Earthshine E-6 $40 and $45, Equinox autograph /20 $950 (Nov 13, one sale), Molten Mercury /11 $552 (FDI, Nov 12). Base veterans $4 to $5 (Warren, Henry, Barkley, Pickens, Walker, McCaffrey); rookie base Concepcion #82 $10 twice, Harvey #52 $10, Lemon #73 $20, Williams #72 $5.99')
    rep(r, ['deep', 'lede'], 'Written Nov 12, the day before release (Nov 13), from presale box sales and the handful of FDI singles that have sold; every hobby-box single price is pending.',
        'Written Nov 12, re-priced Nov 14 from the first two days of hobby-box sales (release Nov 13).')
    rep(r, ['deep', 'lede'], 'The market has already priced it: 43 presale boxes sold on eBay between Oct 12 and Nov 11 at a $680 median, $140 over Topps, and the first week of flips went $720.',
        'The market priced it at $680 in presale (43 boxes Oct 12 to Nov 11) and $720 in the first week of flips; on release the box slipped to $650 median on 11 sales Nov 13 to 14 ($580 to $675), still $110 over Topps.')
    rep(r, ['deep', 'lede'], 'The FDI singles that have sold say the same: $250 for a Harrison /10 and $300 for a Kittle /35 at the top, $40 and $60 for rookie autographs below the first tier. Whether Mendoza\'s three autograph sets open where his Inception ones did ($800 Red /99, $2,000 Gold /50 in week one) is the number to fill in next week.',
        'The first two days of hobby singles say the same: 40 autographs sold at a $100 median, and the ones above $200 were short-numbered (Allar Rookie Jersey Autograph /12 $699, Sanders Dark Matter /20 $500, Tate REM /20 $300) or Caleb Downs and Jeremiyah Love; Reese, Johnson, Concepcion and Beck autographs run $75 to $175, the veterans\' Countdown Calligraphy $20 to $100. No Mendoza autograph has sold from a hobby box yet; his Equinox autograph /20 went $950 on Nov 13 and his Rookie Refractor SP #21 $103, so whether his base autographs open where his Inception ones did ($800 Red /99, $2,000 Gold /50 in week one) is still the number to fill in.')
    T = r['deep']['sections']
    T[0]['items'][0]['p'] = 'No Mendoza autograph sold from a hobby box through Nov 14. Equinox autograph /20 $950 (Nov 13, one sale), Molten Mercury /11 $552 (FDI, Nov 12), Rookie Refractor SP #21 $102.64 (Nov 14), Earthshine E-6 $40 and $45 (Nov 13 to 14). Comp: his Inception Rookie Autograph Red /99 $800 (Nov 7) and Gold Electricity /50 $2,000 (Nov 8), from this site\'s Inception review'
    T[0]['items'][1]['p'] = 'Love Rookie Autograph /125 $225 and Midnight Oil Marks autograph $140.39 (Nov 13 to 14); Beck patch autograph RIA-CB $127.50 and Rookie Autograph #27 Midnight $75 (Nov 13 to 14). No Simpson sale in the read. Comp: Simpson Inception autographs $150 to $300 (6 sales Nov 6 to 9); Beck $125 and $190'
    T[0]['items'][2]['p'] = 'Sanders / Gibbs $99.99 (Nov 7, FDI); Allen / Kelly Refractor $44.99, Smith-Njigba / Largent $15, Burrow / Chase $9.99 (Nov 13 to 14, one each)'
    rep(r, ['deep', 'sections', 0, 'items', 3, 'p'], 'Kittle Stroke of Midnight /35 $300 (1 sale, Nov 8, FDI); Harrison Jr. autograph /10 $250 (Nov 10).',
        'Kittle Stroke of Midnight /35 $300 (Nov 8, FDI); Harrison Jr. autograph /10 $250 (Nov 10); Barry Sanders Dark Matter /20 $500 and Jaxon Smith-Njigba Dark Matter $550 (Nov 13 to 14); Countdown Calligraphy veterans Witten /50 $52 and $66, Likely $99.99 twice, Monangai /125 $100, John Taylor /50 $75, Andre Johnson /50 $33.79, Gates $20, Gordon $45, Willie Parker $0.99.')
    rep(r, ['deep', 'sections', 1, 'items', 0, 'p'], 'Sadiq Rookie Jersey Autograph $99.99 (1 sale, Nov 8, FDI).',
        'Allar Rookie Jersey Autograph /12 $699 (Nov 13); Price Rookie Jersey Autograph $150 (Nov 14); Sadiq Rookie Jersey Autograph $99.99 (Nov 8, FDI) and Rookie Autograph $85 (Nov 14); Tate REM relic autograph /20 $300 (Nov 14); Allar patch autograph /99 $102.50 (Nov 12).')
    T[1]['items'][1]['p'] = 'Tenebrous Traces: Downs $250 and $202.50, Reese $175, $150, $150 and $129.99, Boston $139.99 (Nov 13 to 14), Antonio Williams $1. Midnight Oil Marks: Johnson /35 $175 and /99 $49, Styles /125 $165, Concepcion /99 $125.99, Love $140.39. Dark Matter: Sanders /20 $500, Smith-Njigba $550. Countdown Calligraphy $20 to $100 (veterans). All autographs titled as such: $100 median on 40 sales Nov 12 to 14'
    T[1]['items'][2]['p'] = 'Early sales (Nov 13 to 14, one each): Tate Earthshine /25 $125, Nussmeier #65 /11 $45, Robinson Nightball Purple /75 $50, Loveland /99 $45, Coleman #40 /99 $18, Bryce Young Morning /125 $7, McCaffrey Summer Solstice /50 $29.99, London Dusk /75 $25, Olave Nightball Midnight /12 $54.99, Harvey Molten Mercury /11 $20.50 (FDI parallel)'
    T[1]['items'][3]['p'] = 'Cam Ward Night Night NN-25 $15 (Nov 13, one sale); no other case hit sold in the read'
    T[2]['items'][0]['p'] = 'Veteran base $3.99 to $5 (Warren #50, Henry #58, Barkley #91, Pickens #29 twice, Walker #18, McCaffrey #69, Chase #1; Nov 13 to 14); rookie base Concepcion #82 $10 twice, Harvey #52 $10, Lemon #73 $20, Williams #72 $5.99; Mendoza Rookie Refractor SP $102.64. Cameron #45 $9.99 (Nov 6, FDI)'
    rep(r, ['deep', 'sections', 2, 'items', 1, 'p'], 'Nussmeier Base Autograph $60 (Nov 8, FDI); Heidenreich Rookie Horizon Signatures $39.99 (Nov 9, FDI).',
        'Rookie Horizon Signatures Nov 13 to 14: Kaelon Black $49.99 and $50 (Refractor /10 $135.83), Emmett Johnson $50 and /125 $50, Taylen Green $49.99, Cyrus Allen $39.99, Ja\'Kobi Lane $39.99, Heidenreich $34.99, Coleman $30, Claiborne $12, Kaliakmanis $10. Nussmeier Base Autograph $60 (Nov 8, FDI).')
    T[2]['items'][2]['p'] = 'Nightball $7 to $10 unnumbered (Collins, Burden, Mayfield, Darnold), Cam Ward $25, Maye and Chase Morning /125 $29.99 each; Insomnia $7 to $20 (Purdy Morning /125 $49.99); Earthshine $11 to $45 (Mendoza $40 and $45, Downs $39.99, Robinson $39.99, Allar $20); Constellations $10 to $45 (Nov 13 to 14)'
    r['deep']['notes'].append('Prices Nov 14 (eBay sold listings read Nov 14 to 15 in the browser pane, sales Nov 12 to 14 unless stated; cases, lots, break slots, FDI boxes and "you pick" listings excluded by title): single hobby boxes $649.99 median on 11 sales Nov 13 to 14 ($580 to $674.97; Nov 13 $633 to $675 on 7, Nov 14 $580 to $649.99 on 4); the last presale week Nov 7 to 12 went $679.99 median on 12 ($635 to $699.99). One 8-box case $4,999 (Nov 13, $625 a box). FDI box $1,499 (Nov 13). Autographs: 40 sales Nov 12 to 14 of listings titled "auto" ($0.99 to $699), $100 median; Rookie Horizon Signatures and other listings titled "Signatures" are not in that count and are listed per line. Mendoza: the eBay search returned eight Midnight listings (the rest were his Topps Flagship #301 base at $1 to $3); no Rookie Autograph, Rookie Horizon Signatures or Rookie Jersey Autograph of his had a completed sale. The Nov 12 notes above keep the presale and FDI detail.')
    rep(r, ['deep', 'src'], 'Prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 12, 2026 in the browser pane, sales through Nov 11; counts, ranges and date windows stated per line; cases, multi-box lots, break slots and FDI boxes excluded from the hobby-box figure by title. Hobby-box singles: none sold yet (release Nov 13); every single listed is an FDI pull.',
        'Prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 14 to 15, 2026 in the browser pane, sales through Nov 14 (presale and FDI figures read Nov 12); counts, ranges and date windows stated per line; cases, multi-box lots, break slots and FDI boxes excluded from the hobby-box figure by title. Hobby-box singles are the first two days of sales (Nov 13 to 14) and will move.')
    save(m, r)

# ---------------------------------------------------------------- Museum Collection: first week (Nov 11-14)
m, r = load('topps-museum-2026')
if r['when'] != 'Out Nov 11 · prices Nov 14':
    r['when'] = 'Out Nov 11 · prices Nov 14'
    rep(r, ['facts', 0], 'eBay presale sold $600 median on 18 single boxes Oct 27 to Nov 9 ($381 to $800), $600 on the 13 sold Nov 3 to 9',
        'eBay sold since release: $584 median on 59 single hobby boxes Nov 11 to 14 ($535 to $800), from $600 on 18 presale boxes Oct 27 to Nov 9')
    singles = ('First-week singles (eBay sold Nov 11 to 14): autographs $56 median on 104 sales ($11.50 to $3,700); the top is Atelier Autograph Books (Misiorowski 1/5 $3,700, Rivera Red /5 $1,400, Jeter /10 $1,099, Chourio /50 $600, Witt /25 $520, Chipper Jones $330) and framed autographs (Trout Gold Frame /10 $2,000, Nomo Bronze /35 $1,000, McGwire Gold $250, Ortiz framed patch $215, Olson Bronze $100). '
               'Archival Autographs $56.50 median on 10 sales (Tolle /99 $200, Kruk Ruby /20 $130, Griffin /199 $150, Lynn /99 $19, Saberhagen $16.99); jumbo patch autographs $178 to $600 (4); Signature Swatches duals $50 to $80 (4); relics $25 median on 35 sales; base cards $5 median on 94 sales (Anthony #18 $9.99, Griffin #30 $18, McGonigle #15 $20, Murakami #14 $14.75, Ohtani #17 $25 to $30)')
    if r['facts'][6].startswith('Comp (2025 Museum'):
        r['facts'].insert(6, singles)
    rep(r, ['deep', 'lede'], 'Written Nov 10, the day before release, with presale box prices and no 2026 singles.',
        'Written Nov 10, re-priced Nov 14 from the first four days of sales (release Nov 11).')
    rep(r, ['deep', 'lede'], '$409.99 at the Topps presale and $600 median on eBay presale (18 single boxes Oct 27 to Nov 9), the same format as last year\'s box, which still sells sealed at $672 (7 sales since September).',
        '$409.99 at the Topps presale, $600 median on eBay presale (18 single boxes Oct 27 to Nov 9) and $584 on 59 boxes in the first four days after release, the same format as last year\'s box, which still sells sealed at $672 (7 sales since September). The first 104 autograph sales came in at a $56 median: the Atelier books and framed autographs carry the top ($3,700 Misiorowski 1/5, $2,000 Trout Gold Frame /10, $1,000 Nomo /35), Archival Autographs are $56.50 median on 10, and base rookies are $10 to $20.')
    T = r['deep']['sections']
    rep(r, ['deep', 'sections', 0, 'items', 0, 'p'], '2026 prices pending.', '2026 (eBay sold Nov 11 to 14, one each): Trout Gold Frame /10 $1,999.99, Nomo Bronze /35 $1,000, Caglianone Bronze Frame /49 silver ink $600 (Nov 10), McGwire Gold Frame $249.99, Ortiz framed patch autograph MFAR-DO $215, Dembele Gold Frame /75 $140 (UCC), Olson Bronze $100; $215 median on 8 framed sales.')
    rep(r, ['deep', 'sections', 0, 'items', 1, 'p'], 'Prices pending.', 'Griffin Archival Autograph /199 $149.99 (Nov 14, one sale); no Anthony, McGonigle or Murakami autograph sold in the read. Base: Griffin #30 $18 and $17.95, McGonigle #15 $20 and $19.99, Anthony #18 $9.99, Murakami #14 $14.75; parallels Anthony Blue /150 $20, Pink /199 $20, McGonigle Gold /275 $20 (Nov 12 to 14).')
    rep(r, ['deep', 'sections', 0, 'items', 2, 'p'], 'Prices pending. No 2025 Canvas original sold in the Oct 27 to Nov 9 read', 'Atelier Autograph Books (eBay sold Nov 11 to 14, one each): Misiorowski 1/5 $3,700, Rivera Red /5 $1,400, Jeter /10 $1,099, Chourio /50 $600, Witt Jr. /25 $520, Chipper Jones $330. No Canvas original sold yet')
    rep(r, ['deep', 'sections', 0, 'items', 3, 'p'], 'Prices pending.', 'Jumbo patch autographs Nov 13 to 14: Crow-Armstrong Gold /50 $599.99, Acuna $305 (redemption), Pedroia / Duran dual book $265, Chourio $177.50.')
    rep(r, ['deep', 'sections', 1, 'items', 0, 'p'], 'Prices pending.', 'Crow-Armstrong Gold /50 $599.99, Acuna $305, Pedroia / Duran dual $265, Chourio $177.50 (Nov 13 to 14, one each); Webb dual relic patch autograph Copper $11.50.')
    rep(r, ['deep', 'sections', 1, 'items', 1, 'p'], 'Prices pending.', 'Signature Swatches duals Nov 11 to 14: Arozarena $79.99, Varitek $55 and $50, Posada $49.99; Painter rookie dual relic autograph /50 $56.')
    rep(r, ['deep', 'sections', 1, 'items', 2, 'p'], 'Prices pending.', 'Anthony Blue /150 $20 and Pink /199 $20, McGonigle Gold /275 $20 (Nov 13); veterans\' numbered parallels mostly $5 to $15.')
    rep(r, ['deep', 'sections', 1, 'items', 3, 'p'], 'Prices pending', 'No Retrospective Signatures or bat-barrel autograph sale in the Nov 11 to 14 read')
    rep(r, ['deep', 'sections', 2, 'items', 0, 'p'], 'Prices pending.', '$5 median on 94 single-card sales Nov 11 to 14 (titles without autograph, relic or serial number): Ohtani #17 $24.99 and $30, Ripken #34 $16.99, Judge #4 $8.99, Bonds #69 $10, Ted Williams #56 $2.49; rookies Misiorowski #53 $19.99, Schlittler $15 and $35, Tolle #70 $24.99.')
    rep(r, ['deep', 'sections', 2, 'items', 1, 'p'], 'Prices pending.', '$56.50 median on 10 sales Nov 12 to 14 ($16.99 to $200): Tolle /99 $200, Griffin /199 $150, Kruk Ruby /20 $129.99, Ford /99 $30, Lynn /99 $19, Saberhagen $16.99.')
    rep(r, ['deep', 'sections', 2, 'items', 2, 'p'], 'Prices pending.', '$25 median on 35 relic sales Nov 11 to 14 ($5.50 to $300): Puckett Meaningful Material /25 $66.66 and $99.99, Skubal Meaningful Material $5.50, Holliday $7, Acuna $8.50, Buxton triple /75 $6, Carroll triple /99 $12.50.')
    r['deep']['notes'].append('Prices Nov 14 (eBay sold listings read Nov 14 to 15 in the browser pane, sales Nov 11 to 14; break slots, lots and cases excluded by title; box median floored at $300): single hobby boxes $584.44 median on 59 sales Nov 11 to 14 ($535 to $799.99); Oct 27 to Nov 14 $588 on 82. Autographs: 104 sales of 2026 Museum listings titled "auto" (UCC soccer excluded), $56 median, $11.50 to $3,700. Framed: 8 sales, $215 median. Archival: 10 sales, $56.50 median. Relics: 35 sales, $25 median. Base: 94 sales of listings without "auto", "relic", "patch", "swatch", "frame" or a serial number, $5 median; one $583.99 multi-quantity hobby listing slipped in and was ignored. eBay serves 240 sold listings per search, newest first, so the base and autograph windows are the depth those pages reached (all reached Nov 11).')
    rep(r, ['deep', 'src'], 'Box prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 10, 2026 in the browser pane, sales through Nov 9;',
        'Box and 2026 single prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 14 to 15, 2026 in the browser pane, sales through Nov 14 (presale boxes read Nov 10);')
    save(m, r)

# ---------------------------------------------------------------- Nov 1 batch: box prices only
def boxline(slug, when_old, when_new, old, new, note):
    global s
    m, r = load(slug)
    if r['when'] == when_new: return
    assert r['when'] == when_old, (slug, r['when'])
    r['when'] = when_new
    rep(r, ['facts', 0], old, new)
    r['deep']['notes'].append(note)
    save(m, r)

boxline('donruss-fb-2026', 'Out now · prices Nov 1', 'Out now · boxes Nov 14, singles Nov 1',
        'eBay sold: $220 median on 32 single boxes Oct 28 to Nov 1 ($190 to $270)',
        'eBay sold: $220 median on 32 single boxes Oct 28 to Nov 1 ($190 to $270); $260 median on 10 boxes Nov 12 to 14 ($229 to $285), two weeks on',
        'Box price Nov 14 (eBay sold listings read Nov 14 in the browser pane; cases, lots, breaks, mega boxes, blasters and tins excluded by title): $259.99 median on 10 single hobby boxes Nov 12 to 14, $229 to $285. The search returned 240 listings reaching back only to Nov 12 because singles share the search, so this is a two-day window. Singles were not re-read.')
boxline('topps-chrome-f1-2026', 'Out now · boxes Nov 1, singles Oct 15', 'Out now · boxes Nov 14, singles Oct 15',
        '$677 two weeks on (26 boxes sold Oct 28 to Nov 1, $630 to $800), down from $948 in presale',
        '$677 two weeks on (26 boxes sold Oct 28 to Nov 1, $630 to $800) and $630 a month on (69 boxes sold Nov 1 to 14, $560 to $900), down from $948 in presale',
        'Box price Nov 14 (eBay sold listings read Nov 14 in the browser pane; cases, lots, breaks, Sapphire, LogoFractor, mega and value boxes excluded by title): $629.95 median on 69 single hobby boxes Nov 1 to 14, $560 to $900. Singles were not re-read.')
boxline('topps-update-2026', 'Out now · boxes Nov 1, singles Oct 15', 'Out now · boxes Nov 14, singles Oct 15',
        '$160 median two weeks on (48 boxes sold Oct 26 to Nov 1, $140 to $200)',
        '$160 median two weeks on (48 boxes sold Oct 26 to Nov 1, $140 to $200); $158 a month on (35 boxes sold Nov 7 to 14, $130 to $179)',
        'Box price Nov 14 (eBay sold listings read Nov 14 in the browser pane; cases, lots, breaks, jumbo, mega, blaster and Japan Edition excluded by title): $158 median on 35 single hobby boxes Nov 7 to 14, $130 to $179 (the 240-listing page reached back to Nov 7). Jumbo and singles were not re-read.')
boxline('ud-series-1-hockey-2026', 'Out now · boxes and top Young Guns Nov 1', 'Out now · boxes Nov 14, Young Guns Nov 1',
        '$138 three weeks on (13 boxes sold Oct 28 to Nov 1, $100 to $181)',
        '$138 three weeks on (13 boxes sold Oct 28 to Nov 1, $100 to $181); $138 five weeks on (19 boxes sold Nov 1 to 13, $109 to $180)',
        'Box price Nov 14 (eBay sold listings read Nov 14 in the browser pane; cases, lots, breaks, tins, blasters and retail excluded by title): $137.99 median on 19 single hobby boxes Nov 1 to 13, $108.61 to $179.95. Young Guns were not re-read.')
boxline('allen-ginter-2026', 'Out now · boxes and top rookies Nov 1', 'Out now · boxes Nov 14, rookies Nov 1',
        '$200 three weeks on (40 boxes sold Oct 26 to Nov 1, $185 to $365)',
        '$200 three weeks on (40 boxes sold Oct 26 to Nov 1, $185 to $365); $198 five weeks on (51 boxes sold Nov 2 to 14, $172 to $395)',
        'Box price Nov 14 (eBay sold listings read Nov 14 in the browser pane; cases, lots, breaks, Chrome, blasters and retail excluded by title): $197.99 median on 51 single hobby boxes Nov 2 to 14, $171.50 to $395. Singles were not re-read.')
boxline('bowman-chrome-sapphire-2026', 'Out now · boxes and top cards Nov 1', 'Out now · boxes Nov 14, cards Nov 1',
        '$1,405 median on 13 boxes sold Oct 12 to 29 ($1,098 to $1,550, one at $2,410)',
        '$1,405 median on 13 boxes sold Oct 12 to 29 ($1,098 to $1,550, one at $2,410); only two boxes sold Nov 1 to 14, $1,014.89 and $1,550 (both Nov 3)',
        'Box price Nov 14 (eBay sold listings read Nov 14 in the browser pane; cases, lots, breaks, Draft, University and single cards excluded by title): two single-box sales Nov 1 to 14, $1,014.89 and $1,550, both Nov 3; too few for a median. Singles were not re-read.')
boxline('bowman-fb-2026', 'Out now · boxes and Manning / Mendoza autos Nov 1', 'Out now · boxes Nov 14, Manning / Mendoza autos Nov 1',
        '$335 a month on (30 sold Oct 26 to Nov 1, $310 to $380)',
        '$335 a month on (30 sold Oct 26 to Nov 1, $310 to $380); $318 six weeks on (14 sold Nov 10 to 14, $295 to $500)',
        'Box prices Nov 14 (eBay sold listings read Nov 14 in the browser pane; cases, lots, breaks, University, Sapphire, mega and blasters excluded by title): hobby $318.25 median on 14 single boxes Nov 10 to 14, $295 to $499.99 (the 240-listing page reached back to Nov 10); jumbo $565 median on 6 boxes Nov 11 to 13, $549.99 to $595. Singles were not re-read.')

open(P, 'w').write(s)
print('ok')
