"""Nov 10, 2026 re-pricing of three deep reviews from eBay sold listings (LH_Sold=1&LH_Complete=1) read in the
browser pane on Nov 10 (sales through Nov 9): Inception Football (first prices), Select Basketball and Heritage
Football (both older than 14 days). Idempotent: each edit asserts the old text and is skipped when already applied.
Counts, ranges and date windows are stated per line; break slots, lots, cases and 'you pick' listings excluded by
title; box medians floor at a sanity price to drop mis-tagged singles."""
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

# ---------------------------------------------------------------- Inception Football
m, r = load('topps-inception-fb-2026')
if r['when'] != 'Out Nov 6 · prices Nov 9':
    r['when'] = 'Out Nov 6 · prices Nov 9'
    rep(r, ['facts', 0], 'No sold prices yet: the 2026 box and every 2026 single are pending (see notes)',
        'eBay sold: $475 median on 39 single hobby boxes Nov 4 to 9 ($343 to $600); $435 median on the 13 sold Nov 8 to 9 ($380 to $555)')
    rep(r, ['deep', 'lede'], 'Written Nov 8, two days after release (Nov 6), without sold prices: the browser pane that reads eBay and PSA was not available, so every 2026 price here is pending and the numbers are the structure and last year\'s box.',
        'Written Nov 8, re-priced Nov 10 from eBay sold listings through Nov 9. The box trades above Topps: $475 median on 39 single hobby boxes Nov 4 to 9 and $435 on the 13 sold over the weekend, against $379.99 on release day.')
    rep(r, ['deep', 'lede'], 'the eBay street price, and whether Mendoza\'s autograph opens where Maye\'s did, are the two numbers to fill in next week.',
        'the first weekend answered one question: Mendoza\'s numbered Rookie Autographs opened at $800 (Red /99, Nov 7) and $2,000 (Gold Electricity /50, Nov 8), above where Maye\'s plain autograph sat a year on, while the other rookie autographs settled at $75 median on 23 sales. One name carries the box.')
    T = r['deep']['sections']
    T[0]['items'][0]['p'] = 'Rookie Autograph Red /99 $800 (Nov 7) and Gold Electricity /50 $2,000 (Nov 8), the only two Rookie Autograph sales read; FDI hard-signed Rookie Autograph $785 (Nov 6). Base #151 $51 median (3 sales, $45 to $57, Nov 7 to 9); Rookie Short Print $255 (1, Nov 7). No unnumbered Rookie Autograph or Provenance patch of his sold in the read. Comp: Drake Maye 2024 Inception Rookie Autograph about $365 raw on 113 sales (Hobby Card Index, Oct 3)'
    T[0]['items'][1]['p'] = 'Simpson autographs $150 to $300 (6 sales Nov 6 to 9): Rookie Autograph Red /99 $300, Silver Signings /100 $180 and $285, Rookie Autograph Variation /75 $154 and unnumbered $150. Love: Provenance Patch Autograph Aqua /75 $142.50 and /25 $300, FDI Jumbo Patch Autograph /22 $161 to $218 (3 sales Nov 6 to 7); no plain Love Rookie Autograph sold yet. Beck Rookie Autograph $125 and $190 (Nov 7, Nov 9). Comp: Daniels and Nix 2024 Rookie Autographs about $200 each'
    T[0]['items'][2]['p'] = 'Allar/Bernard Dual Rookie Autograph /25 $286 (Nov 9); Singleton/Tate Dual Rookie Relic Autograph Book /49 $400 (Nov 8). Two sales so far. Comp: 2024 Dual Rookie Relic Autographs $430 median on 38 sales across 5 cards'
    T[0]['items'][3]['p'] = 'Bettis /5 $300 and McNabb 1/1 $499 (both Nov 9); no Brady, Manning or Sanders sold yet. Comp: 2024 Dawn of Greatness $161 median on 67 sales across 15 cards'
    T[1]['items'][0]['p'] = '$148 median (10 sales Nov 6 to 9, $31 to $300), most of them FDI /22 copies: Beck $204, Cooper Jr. $172 to $200, Concepcion $154, Bell $122 to $140; Love Aqua /75 $142.50 and /25 $300; Sarratt /50 $31. Comp: 2024 Provenance $21.49 median on 312 sales; Maye about $540'
    T[1]['items'][3]['p'] = 'Silver Signings: Simpson /100 $180 and $285 (Nov 7, Nov 9). No Genesis book sold in the read'
    T[2]['items'][0]['p'] = 'Mendoza #151 $51 median (3 sales, $45 to $57, Nov 7 to 9); other base not read. Comp: 2024 base rookies about $1.60 raw, PSA 10 rookies about $36'
    T[2]['items'][1]['p'] = '$75 median on 23 sales Nov 6 to 9 ($18.50 to $200) for Rookie Autographs, Green parallels and Variations outside Mendoza, Simpson and Love: Beck $125 to $190, Tate $135, Allar $115, Concepcion $95, Sarratt $30, McCoy $18.50. Comp: 2024 Rookie Autographs $6.31 median on 1,857 sales a year on'
    T[2]['items'][2]['p'] = 'Mendoza Rookie Short Print $255 (1, Nov 7); no Launch sold in the read. Comp: 2024 Launch about $9'
    r['deep']['avoid'][0] = 'Paying $475 for a box as a way to get a Mendoza autograph. Rookie Autographs fall 1:4 packs across 46 names, so a Mendoza is roughly one box in 180; his numbered ones opened at $800 and $2,000, so the single is not cheap either, but at least it is the card.'
    r['deep']['notes'][1] = 'Prices (eBay sold listings, LH_Sold=1&LH_Complete=1, read Nov 10 in the browser pane, sales through Nov 9; break slots, lots, cases and FDI boxes excluded by title, box median floored at $300 to drop mis-tagged singles): hobby box $475 median, 39 sales Nov 4 to 9, $343 to $600; $435 median on 13 sales Nov 8 to 9, $380 to $555. Mendoza: Rookie Autograph Red /99 $800 (Nov 7), Gold Electricity /50 $2,000 (Nov 8), FDI Rookie Autograph $785 (Nov 6), base #151 $45, $51, $57.29 (Nov 7 to 9), Rookie Short Print $255 (Nov 7). Simpson: Red /99 $300, Silver Signings /100 $179.99 and $285, Variation /75 $154, Variation $150 (Nov 6 to 9). Love: Provenance Aqua /75 $142.50 (Nov 8), /25 $299.99 (Nov 9), FDI Jumbo Patch Autograph /22 $161.38, $172.50, $217.50 (Nov 6 to 7). Beck Rookie Autograph $125 (Nov 7), $189.99 (Nov 9). Rookie Autographs, Green parallels and Variations outside those three: $75 median, 23 sales Nov 6 to 9, $18.50 to $199.99. Provenance: $148 median, 10 sales Nov 6 to 9, $31 to $299.99. Duals: Allar/Bernard /25 $286 (Nov 9), Singleton/Tate book /49 $399.99 (Nov 8). Dawn of Greatness: Bettis /5 $299.99, McNabb 1/1 $499 (Nov 9). Topps prices: $369.99 presale Oct 5, $379.99 release day Nov 6 by EQL raffle (Checklist Insider, Hammy Puller). FDI: $2,000 opening Dutch auction Oct 1, sold out at $900 (Checklist Insider). Comps are the 2024 Inception Football set as catalogued by Hobby Card Index (read Nov 8; its catalog prices were pulled Oct 3, 2026 from sold data): Rookie Autographs $6.31 (48 cards, 1,857 sales), Rookie Autograph Variations $16.43 (19, 718), Provenance Patch Autographs $21.49 (35, 312), Dawn of Greatness $161.28 (15, 67), Dual Rookie Relic Autographs $430 (5, 38); Maye Rookie Autograph about $365 raw (113 sales), $650 PSA 10; Williams $290 (82); Daniels and Nix about $200; base rookies $1.60, PSA 10 rookies about $36; Launch about $9.'
    rep(r, ['deep', 'notes', 5], 'The scores are a first read without prices.', 'The scores are a first read, held on Nov 10 with four days of sales.')
    rep(r, ['deep', 'notes', 5], 'Pending after the first week: eBay sold medians with counts for the box, the Mendoza, Simpson, Love and Beck Rookie Autographs and Variations, the Provenance patches, the duals and a Dawn of Greatness; then the box\'s street price against $379.99.',
        'Still pending: a plain, unnumbered Mendoza Rookie Autograph, a Love Rookie Autograph, Charged Particles and Immersion, and the box\'s second-week median against the $475 first-week read.')
    r['deep']['notes'][6] = 'Verdict for now: a singles product, with one exception. The box sells at $475 on eBay against $379.99 at Topps, so the raffle allotment was underpriced and the secondary market is paying a $95 premium for a seven-card pack with one sticker autograph from a 46-name set whose non-Mendoza median is $75. Mendoza is the exception: $800 for a Red /99 and $2,000 for a Gold /50 in the first weekend are the Maye prices of a year on, paid in week one. Buy Simpson and Beck Rookie Autographs now while breakers list ($125 to $300); wait on Mendoza unless the Raiders start keeps going; buy the box only if a seven-card rip at $475 is the point. Investors: the second-week box median against $475 is the number to watch; the 2024 box sits near $510 sealed on a $249.99 start with three hits.'
    r['deep']['src'] = 'Prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 10, 2026 in the browser pane, sales through Nov 9; counts, ranges and date windows stated per line; break slots, multi-box lots, cases and FDI boxes excluded by title. Box configuration, presale and release-day prices, FDI auction, checklist, card numbers and teams, parallels, autograph and insert sets, pack odds: Checklist Insider (2026 Topps Inception Football guide), read Nov 8. Topps launch-page details (noon ET Nov 6 opening, $379.99, one autograph per box, preview parallels): Hammy Puller guide, read Nov 8. 2024 Inception Football comps: Hobby Card Index hub, read Nov 8, whose catalog prices were pulled Oct 3, 2026 from sold data (medians, card counts and sale counts as stated per line; it could not verify its $510 sealed-box figure against sold data). Release dates: Checklist Insider, Cardsmiths Breaks, DraftKings Network.'
    save(m, r)

# ---------------------------------------------------------------- Select Basketball
m, r = load('select-bk-2025-26')
if r['when'] != 'Out Oct 23 · prices Nov 9':
    r['when'] = 'Out Oct 23 · prices Nov 9'
    rep(r, ['facts', 0], 'Steel City presale $324.95; one eBay sale at $309.99 (Oct 18); other eBay presale asks $285 to $350',
        'eBay sold: $220 median on 10 single hobby boxes Nov 4 to 9 ($199 to $302), $223 on the 18 sold since Oct 28; the presale was $310 to $325')
    rep(r, ['facts', 1], 'eBay sold $700 median (3 boxes, $675 to $720, Oct 14 to 19)', 'eBay sold $675 median (3 boxes, $625 to $696, Oct 28 to Nov 6), from $700 at release')
    rep(r, ['facts', 4], 'no single card from the set had a completed eBay sale by Oct 22', 'singles priced below from eBay sold through Nov 9')
    T = r['deep']['sections']
    T[0]['items'][0]['p'] = 'Autographs $238 median (18 sales Oct 23 to Nov 9, $119 to $625): Rookie Signatures /249 $150, Orange /149 $128, Rookie Patch Autograph /99 $228, Jersey Patch Autograph /75 $203, FOTL Gold Spectris Colorgraphs /10 $275, Edgecombe/Fears Pairings autograph /49 $250, Tie-Dye dual autograph /25 $305; Rookie Patch Autograph Black Finite 1/1 $4,050 (Nov 8). Zebra Courtside $255 (1, Nov 9); Color Wheel $136 (1, Nov 3); base Courtside #240 $4 to $7.50 (3, Nov 3)'
    T[0]['items'][1]['p'] = 'Rookie autographs outside Edgecombe: $20 median across 127 sales Nov 2 to 9 ($0.99 to $1,025). Rookie Signatures /249 of the second-tier names $1 to $10 (Clifford, Sanders, Newell, Lanier), Colorgraphs /99 $4 to $16 (Sorber, Coward, Maluach $12), Queen patch autograph /99 $8.50, Gonzalez Jumbo Rookie Patch Autograph /75 $31, Beringer FOTL Gold Spectris patch autograph /10 $71'
    T[0]['items'][2]['p'] = 'Tie-Dye /25 $25 median (88 sales Oct 25 to Nov 9, $0.99 to $420): Acuff Jr. Concourse 25/25 $138, Olajuwon Premier $35, Fudd $30, rookie patch cards $7 to $18. Zebra $20.50 median (15 sales Oct 30 to Nov 9, $3 to $400): Edgecombe Courtside $255, Carter Bryant Courtside $150, Iverson $60, Lin $45, Coward $20.50. Gold /10, Green /5 and the 1/1s: no base-card sale read; the Edgecombe Black Finite 1/1 above is a patch autograph'
    T[1]['items'][0]['p'] = 'Color Wheel $85 median (7 sales Nov 3 to 9, $30 to $290): Acuff Jr. $290, Arenas $145, Edgecombe $136, Magic Johnson $85, Morant $40, Flemings $30. Stained Glass and Solar Eclipse: Edgecombe Solar Eclipse $20.50 (1, Nov 8)'
    T[2]['items'][0]['p'] = 'Edgecombe Courtside #240 $4 to $7.50 (3 sales, Nov 3); Edgecombe Buckets insert $3 (Nov 6). Base cards otherwise list at $1 to $3'
    T[2]['items'][2]['p'] = '$20 median across 127 rookie and veteran autograph sales Nov 2 to 9 ($0.99 to $1,025); Rookie Signatures /249 $1 to $10 for most names, Meleek Thomas /49 $44 to $60'
    r['deep']['notes'][1] = 'Prices (eBay sold listings, LH_Sold=1&LH_Complete=1, read Nov 10 in the browser pane, sales through Nov 9; break slots, lots and cases excluded by title; box median floored at $150): hobby $220 median, 10 sales Nov 4 to 9, $199 to $301.90; $223 median on 18 sales Oct 28 to Nov 9. FOTL $675 median, 3 sales Oct 28 to Nov 6 ($625, $675, $696.05). Edgecombe autographs $238 median, 18 sales Oct 23 to Nov 9, $119.40 to $625, individual cards as stated in Tier 1; Rookie Patch Autograph Black Finite 1/1 $4,050 (Nov 8). Rookie and veteran autographs across the set $19.99 median, 127 sales Nov 2 to 9. Tie-Dye /25 $25.05 median, 88 sales Oct 25 to Nov 9. Zebra $20.50 median, 15 sales Oct 30 to Nov 9. Color Wheel $85 median, 7 sales Nov 3 to 9. Earlier reads (Oct 22): FOTL $700 median on 3 sales Oct 14 to 19; one hobby presale at $309.99 (Oct 18); Steel City presale $324.95.'
    r['deep']['src'] = 'Prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 10, 2026 in the browser pane, sales through Nov 9; counts, ranges and date windows stated per line; break slots, lots and cases excluded by title. Earlier box reads Oct 22 as noted. Presale price: Steel City Collectibles. Formats, checklist, tiers, parallels, inserts, autograph and relic sets, licensing note and the absent rookies: Checklist Insider (2025-26 Panini Select Basketball guide) and Cardsmiths Breaks (hobby box checklist).'
    save(m, r)

# ---------------------------------------------------------------- Heritage Football
m, r = load('topps-heritage-fb-2026')
if r['when'] != 'Out now · prices Nov 9':
    r['when'] = 'Out now · prices Nov 9'
    rep(r, ['facts', 0], 'eBay sold since release: $186 median (46 boxes, $160 to $255, Oct 20 to 22); presale boxes went $190 median (117 since Sep 29)',
        'eBay sold: $150 median (49 boxes, $120 to $415, Nov 3 to 9), down from $186 in release week (46 boxes, Oct 20 to 22) and $190 in presale')
    rep(r, ['facts', 1], 'ships Nov 4; presale sales $75 median (21, $60 to $96, Sep 29 to Oct 22)', 'out Nov 4; $56 median (30 boxes, $27 to $90, Nov 3 to 9), from $75 in presale')
    T = r['deep']['sections']
    T[0]['items'][0]['p'] = 'Paper #272 $2.49 median (106 sales, $0.99 to $30, Nov 5 to 9), from $3.99 in release week. Chrome #272 $25 median (59 sales, $6.50 to $55, Nov 5 to 9): plain Chrome $10 to $13, Refractor $30 to $40, Silver Sparkle $28. Autographs, now sold: Heritage Rookie Autograph /76 $432 and $449, Founding Era Ink /76 $304 and $340, Real One on-card $570, Chrome Gold autograph /50 $1,501, autograph relic /100 $499; $449 median on those 9 sales Nov 5 to 9. Image variation $60 to $79 (2, Nov 9)'
    T[0]['items'][1]['p'] = 'Love paper #133 $1.49 median (9 sales, $1 to $2.24, Nov 7 to 9). Earlier reads: Love image variation $69 (1, Oct 22); Love Rookie Lineage relic $29.99 (1, Oct 22). No Love autograph read'
    T[1]['items'][0]['p'] = '$15 median (234 sales, $0.99 to $200, Nov 7 to 9), down from $60 on 17 sales in release week: Mendoza $60 to $79, Josh Allen no-helmet $45, Drake Maye $40, Sean Taylor $25, JSN $22, Bo Nix $20, Lemon $8.50 to $12, Hurts $0.99'
    T[1]['items'][1]['p'] = 'Chrome Refractors and sparkles $2.50 median (154 sales, $0.25 to $13, Nov 8 to 9), from $5.99 in release week. Mendoza Chrome $25 median (59)'
    T[2]['items'][0]['p'] = 'Love #133 $1.49 (9); Mendoza #272 $2.49 (106); other base lists at $0.99 a card'
    r['deep']['notes'][1] = 'Box prices (eBay sold, read Nov 10, sales through Nov 9): hobby $150 median, 49 sales Nov 3 to 9, $119.99 to $415; release week (read Oct 22) $186 median, 46 sales Oct 20 to 22; presale $190 median, 117 sales Sep 29 to Oct 22. Mega $56 median, 30 sales Nov 3 to 9, $27.27 to $89.99; presale $75 median, 21 sales Sep 29 to Oct 22. Singles (Nov 10 read): Mendoza paper #272 $2.49 median, 106 sales Nov 5 to 9; Mendoza Chrome $25 median, 59 sales Nov 5 to 9; Mendoza autographs $449 median, 9 sales Nov 5 to 9 ($304 to $1,501; hot-pack and base listings excluded); image variations $15.24 median, 234 sales Nov 7 to 9; Chrome Refractors $2.50 median, 154 sales Nov 8 to 9; Love paper #133 $1.49 median, 9 sales Nov 7 to 9. Lines that still say Oct 21 or 22 keep the release-week read. Break slots, lots and you-pick listings excluded by title.'
    r['deep']['src'] = 'Prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 10, 2026 in the browser pane (sales through Nov 9) for boxes, Mendoza, Love, image variations and Chrome Refractors; lines dated Oct 20 to 22 keep the Oct 22 read; counts and date ranges stated per line; break slots, multi-box lots and \'you pick\' listings excluded by title. Topps price: Checklist Insider. Formats, checklist, parallels and insert sets: Checklist Insider (updated Oct 16), Cardsmiths Breaks, Steel City product sheet, Sports Illustrated (Sep 19). Mendoza Bowman Chrome auto comparison: this site\'s 2026 Bowman Football review, eBay sold Sep 30 to Oct 9.'
    save(m, r)

open(P, 'w').write(s)
print('ok')
