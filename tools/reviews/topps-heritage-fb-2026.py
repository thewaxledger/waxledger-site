"""Add the 2026 Topps Heritage Football deep review to the master page (idempotent).
Written Oct 20, the day before the hobby release (Oct 21). Structural review: the checklist and box contents are
published, pack odds are not, and no box or single has a sold price we could verify (the browser pane was down, so
eBay sold listings were not reachable; SportsCardsPro has no entry yet). Every price below is either Topps' own price
or a dealer/eBay asking price and is labelled as such. Refresh with eBay sold medians after Oct 21."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Topps Heritage Football", "when": "Out Oct 21 · prices pending", "score": "5.3",
 "facts": [
  "Hobby: 20 packs of 8 (160 cards) with one autograph or relic per box, 12 boxes a case. $129.99 at Topps; dealer presale asks $184.99 to $249.95 (Cardsmiths Breaks' lowest eBay ask, Steel City). No sold price yet",
  "Mega box: 17 packs of 8, $49.99, follows Nov 4. Value blaster: 8 packs of 8, $24.99. Fat packs have their own border parallel",
  "400-card base set on the 1976 Topps design, the first Heritage Football since the 2015 set. 100 rookies marked RC: Mendoza #272, Jeremiyah Love #133, Ty Simpson #288, Carnell Tate #305, Makai Lemon #18, Drew Allar #27, Caleb Downs #187",
  "A 400-card Chrome parallel set runs alongside the paper set, Refractor through SuperFractor 1/1. 150 image variations (alternate jersey, black and white, flipped helmet, legend, no-name)",
  "Topps has not published pack odds, short-print numbers or a print run; the checklist is marked subject to change"
 ],
 "bars": [["Rookie class", 7.5], ["Hit quality", 4.0], ["Print run", 5.0], ["Price vs. value", 4.5]],
 "deep": {
  "lede": "Written Oct 20, the day before the hobby release (Oct 21). The checklist and box contents are published; pack odds, short prints and the print run are not, so nothing below is stated as a ratio. There are no sold prices yet: boxes have not shipped, and the asking prices quoted here are Topps' own price and dealer presale asks, not sales. Single-card prices are pending and will be filled in from eBay sold listings once hobby cases are open. The short version: a hobby box is 160 cards on the 1976 design with one hit that may be a relic rather than an autograph, in a set with 100 rookies and a Chrome set riding alongside the paper one. At $129.99 it is a set-builder's box; at the $185 to $250 dealers are asking it is a bet on the Mendoza rookie market.",
  "sections": [
   {"h": "Tier 1 · The cards worth opening a hobby box for", "items": [
    {"c": "Fernando Mendoza · #272 RC, Chrome #272, Heritage Rookie Autograph, Real One Rookie Autograph", "p": "Prices pending. For scale, his 2026 Bowman Chrome Rookie Auto sells at $560 (23 sales, $500 to $810, Sep 30 to Oct 9)",
     "w": "The No. 1 pick, backing up Kirk Cousins in Las Vegas; he has thrown eight NFL passes (6 of 8 for 48 yards in a 45-17 loss to New England on Oct 11). One autograph or relic per hobby box across a signer list that mixes 100 rookies with veterans and retired players, so a Mendoza autograph in a given box is a long shot; Topps has not said how long. The paper #272 and the Chrome #272 are the cards most boxes will actually produce."},
    {"c": "Jeremiyah Love · #133 RC, Ty Simpson #288, Carnell Tate #305, Garrett Nussmeier, Jordyn Tyson · rookie autographs", "p": "Prices pending",
     "w": "Cardsmiths Breaks lists Love and Nussmeier with Mendoza as the chase rookie autographs, and Bo Nix and Caleb Williams as the chase veterans. Heritage Rookie Autographs carry at least a Gold /50 parallel (Topps' own teaser)."},
    {"c": "Low-numbered Chrome parallels · Gold Refractor /50, Orange /25, Red /5, SuperFractor 1/1; paper Color of the Year /76 and Bicentennial /200", "p": "Prices pending",
     "w": "The Chrome set is a full 400 cards, so a numbered Chrome of one particular rookie is one card in 400 at each level. The Bicentennial /200 and Color of the Year /76 are the paper set's numbered parallels, the 76 a nod to the design year."},
    {"c": "Walter Payton cut autographs; Founding Era Ink; Classic Renditions Autographs", "p": "Prices pending",
     "w": "Steel City's product sheet lists Payton cut signatures. The 1976 Topps #148 Payton rookie is the design's best-known card, and the packaging references it. Expect these at case-hit rarity or rarer; Topps has not published a count."}
   ]},
   {"h": "Tier 2 · Mid-range: variations, Chrome and inserts", "items": [
    {"c": "Image variations · 150 cards: Alternate Jersey (20), Black & White (30), Flipped Helmet (20), Image (50), Legend and No Name (30 between them)", "p": "Prices pending",
     "w": "Heritage's traditional short-printed chase. Topps has not published the football odds, so how many land in a hobby box is unknown. The Black & White list includes a Tom Brady #7 that does not match the base #7 (Trey McBride), one of several checklist inconsistencies Checklist Insider flags."},
    {"c": "Chrome Refractors and the format sparkles · Light Blue Sparkle (hobby), Silver Sparkle (mega), Pink Sparkle (blaster), Aqua Sparkle (fat pack); Blue /150, Green /99, Black /76", "p": "Prices pending",
     "w": "Each format has its own Chrome sparkle parallel, which splits the chase four ways and keeps the hobby version from being the only one. Blue /150 to Black /76 is the higher-numbered half of the ladder."},
    {"c": "Inserts · The Expansion (one star per 1976 franchise, 28 cards), New Age Performers (chromium), All-Pro Series (1976 Wonder Bread design), Sweetness (3 greats, 5 current backs), Through the Years", "p": "Prices pending",
     "w": "No odds published. The Expansion marks the Seahawks' and Buccaneers' 1976 arrival; Justin Herbert is the preview card. Through the Years is a Brady set that includes his one-game 2008 season."},
    {"c": "Relics · Gridiron Collection, Locker Room, Real One, Rookie Lineage; autograph relics in the same four families plus Flashbacks and Bicentennial", "p": "Prices pending",
     "w": "The hobby guarantee is one autograph or relic, and Topps has not said in what proportion. A hobby box whose hit is a veteran relic is unlikely to return the box price; that is the usual pattern for Heritage relics, and the football numbers will be filled in after release. Mega and blaster boxes have no hit guarantee listed."}
   ]},
   {"h": "Tier 3 · Everything else in the box", "items": [
    {"c": "Base cards · 400, with 2025 Record Breakers #1 to 8, League Leaders #201 to 208, team cards #351 to 382, AFC/NFC Championship and Super Bowl LX #331 to 333", "p": "Prices pending",
     "w": "160 cards a hobby box against a 400-card set: three boxes do not complete the set once the duplicates are counted, and any base short prints (Topps has not said whether the 400 includes them) push that further. 100 of the 400 are rookies, a quarter of the set."},
    {"c": "Border parallels by format · Dark Gray (hobby), Red (mega), Dark Green (blaster), Dark Yellow (fat pack); Flip Stock and Black Border (hobby)", "p": "Prices pending",
     "w": "Unnumbered. Heritage's border parallels sell for a few dollars outside the top rookies; the Black Border is the one that has carried a premium in the baseball set."},
    {"c": "Veteran autographs and relics outside the chase names", "p": "Prices pending",
     "w": "Base Chrome Autographs and Real One Autographs cover veterans and retired players as well as rookies. On a one-hit box, the modal hit is one of these."}
   ]}
  ],
  "avoid": [
   "Paying $185 to $250 for a box Topps sells for $129.99. That is $1.16 to $1.56 a card for 160 cards and one hit that may be a relic. Try Topps.com on release day first.",
   "Buying a hobby box for a Mendoza autograph. One hit per box, split between autographs and relics, across 100 rookies plus veterans and legends. Buy the single after release.",
   "Reading dealer asks as prices. Nothing in this product has a sold price yet; Checklist Insider's $174.50 to $249.99 are listings, and so is the $3,839.99 eBay case.",
   "Confusing the Chrome set with the paper set when buying singles. Both are numbered 1 to 400 with the same photos; the Chrome Refractor and the paper base of the same card will be listed with the same title.",
   "Assuming the mega box is the same as the hobby box with fewer packs. Mega is 17 packs of 8 with its own Red Border and Silver Sparkle parallels and no hit guarantee, and it follows two weeks later (Nov 4)."
  ],
  "notes": [
   "Box contents (Checklist Insider, Cardsmiths Breaks, Steel City): hobby 20 packs of 8, one autograph or relic per box on average, 12 boxes a case; mega 17 packs of 8 (136 cards), $49.99, Nov 4; value blaster 8 packs of 8 (64 cards), $24.99; fat packs with a Dark Yellow Border and Aqua Sparkle parallel, no configuration published.",
   "Prices (asks, not sales, Oct 20): Topps $129.99 hobby. Steel City presale $249.95. Cardsmiths Breaks' lowest eBay Buy It Now $184.99, other listings $195 to $199.99. Checklist Insider's resale listings $174.50 to $249.99 and a 12-box hobby case at $3,839.99 ($320 a box). No box has sold on a completed listing we could verify; the browser pane that reaches eBay sold listings was unavailable when this was written.",
   "Design: 1976 Topps Football, the set's 50th anniversary; Heritage Football last ran for the 2015 season. 400 paper cards and a 400-card Chrome set with Refractor, Blue /150, Green /99, Black /76, Gold /50, Orange /25, Red /5 and SuperFractor 1/1. Paper parallels: Dark Gray Border (hobby), Red (mega), Dark Green (blaster), Dark Yellow (fat pack), Flip Stock and Black Border (hobby), Bicentennial /200, Color of the Year /76.",
   "Rookies: 100 base cards marked RC. Mendoza #272 (Raiders), Jeremiyah Love #133 (Cardinals), Ty Simpson #288 (Rams), Carnell Tate #305 (Titans), Makai Lemon #18 (Eagles), Drew Allar #27 (Steelers), Caleb Downs #187 (Cowboys), Arvell Reese #166 (Giants), Kenyon Sadiq #317 (Jets), Jadarian Price #393 (Seahawks), Kevin Coleman Jr. #13 (Dolphins). Checklist Insider notes the checklist is marked subject to change and has duplicate and misspelled entries (#142 twice in Chrome, Otton/Otten).",
   "Autograph sets: Base Chrome Autograph, Heritage Rookie Autographs (Gold /50 confirmed), Classic Renditions, Founding Era Ink, Real One and Real One Rookie Autographs, Bicentennial Relic Autographs. Relic sets: Gridiron Collection, Locker Room, Real One, Rookie Lineage; autograph relics in those families plus Flashbacks. Walter Payton cut autographs per Steel City. No odds for any of them.",
   "The scores are a first read. Rookie class is scored on the draft class, not on Heritage prices, which do not exist yet. Hit quality is scored low because the one hit per box can be a relic. Print run is scored in the middle because Topps has not published one. Pending after release: eBay sold medians with counts for hobby and mega boxes, the Mendoza and Love paper, Chrome and autograph cards, the image variations and the numbered Chrome parallels.",
   "Verdict for now: at $129.99 from Topps, a reasonable box for someone who wants the 1976 design and a shot at a rookie autograph. At $185 or more, pass and buy the Mendoza and Love singles once cases are open and prices settle."
  ],
  "src": "No sold prices yet (Oct 20). Topps price: Checklist Insider. Dealer asks: Steel City Collectibles, Cardsmiths Breaks (eBay Buy It Now), Checklist Insider resale listings. Formats, checklist, parallels and insert sets: Checklist Insider (updated Oct 16), Cardsmiths Breaks, Steel City product sheet, Sports Illustrated (Sep 19). Mendoza Bowman Chrome auto comparison: this site's 2026 Bowman Football review, eBay sold Sep 30 to Oct 9."
 }
}

MARK = '/* topps-heritage-fb-2026 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', lambda m: entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
open(P, 'w').write(s)
print('ok', len(s))
