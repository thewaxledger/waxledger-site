"""Add the 2026 Topps Update Series Baseball deep review to the master page (idempotent).
Written Oct 12, two days before release: the structure and odds are final, box prices are presale sales,
single-card prices were a handful of early retail sales. Refreshed Oct 15 from eBay sold listings dated Oct 14 and 15:
box and base-rookie medians with counts, numbered parallels, Golden Mirror, 1952 variations, case-hit inserts, autographs, relics."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Topps Update Series Baseball", "when": "Out now · boxes Nov 1, singles Oct 15", "score": "5.4",
 "facts": [
  "Hobby: 20 packs of 12 with one autograph or relic. $109.99 at Topps' Sep 14 presale (sold out); $178 median on eBay in the first two days after release (34 boxes sold Oct 14 to 15); $160 median two weeks on (48 boxes sold Oct 26 to Nov 1, $140 to $200)",
  "Jumbo: 10 packs of 40 with one autograph and one relic, $325 median at release (50 sold Oct 14 to 15), $315 on Oct 26 to Nov 1 (52 sold, $280 to $600). Hobby cases $2,025 median (13 sold), about $169 a box",
  "350 cards, US1 to US350: 85 rookie cards, 40 Rookie Debut cards, 195 veterans, 16 Veteran Combos, 14 Season Highlights",
  "Base rookies on day one: Konnor Griffin US1 $2.29 median (45 sales), Kevin McGonigle US7 $3.49 (51), Munetaka Murakami US350 Rookie Debut $2.22 (12). Rookie Debuts of Griffin (US255) and McGonigle (US140) $3 to $4",
  "About two numbered parallels per hobby box. 1952 Rookie Variations fall 1 in 5,952 hobby packs, about one every 25 cases; two have sold so far ($80 and $1,000), neither a Griffin or McGonigle"
 ],
 "bars": [["Rookie class", 8.5], ["Hit quality", 5.0], ["Print run", 3.5], ["Price vs. value", 4.5]],
 "deep": {
  "lede": "Refreshed Oct 15, the day after release, from eBay sold listings dated Oct 14 and 15 (the Oct 12 presale version of this review is superseded). Every price below is a median with the sale count in parentheses, or a list of individual sales where there are fewer than five. Day-one prices are the high-water mark for base and inserts and the low-water mark for the rarest cards, because the people opening hobby cases on release day list everything at once; expect the base rookies to drift lower and the case hits to settle as more surface. The short version has not changed: the rookie class is the best in years, the base cards are already $2 to $3.50, and the hobby box still sells for about $70 over what Topps charged.",
  "sections": [
   {"h": "Tier 1 · The cards worth opening a hobby box for", "items": [
    {"c": "1952 Rookie Variations · 25 cards, short print", "p": "Two sales: Sam Antonacci US301 $80 (Oct 15), Carson Benge US3 $1,000 (Oct 14). 1 in 5,952 hobby packs",
     "w": "The new chase this year: 25 rookies on the 1952 Topps design, with a separate 24-card autograph version. At 20 packs a box that is one every 298 boxes, or about one in 25 cases. No Griffin or McGonigle has sold yet; the $1,000 Benge is a day-one ask that was met once, not a market. Nobody should buy a box expecting one."},
    {"c": "Golden Mirror variations · all 350 cards", "p": "About 45 sold Oct 14 to 15. Veterans and lesser rookies $15 to $100, median about $45 (25). McGonigle US7 $400 (1) · Nolan McLean US10 $300 (1) · Juan Soto US99 $200 (1) · JJ Wetherholt $199 (1). Legends: Ichiro $400 and $500, Mattingly $300, Garciaparra $300, Sabathia $500. Golden Mirror autographs $200 to $900 (6). 1 in 606 hobby packs",
     "w": "About one every 30 hobby boxes, or about two in every five cases, and the pull is a random one of 350 subjects: the typical result is a $45 veteran. The three cards that pay for a case are McGonigle, Griffin (no sale yet) and the legends. Golden Mirror Legend variations (50 cards) are 1 in 11,904 packs."},
    {"c": "Numbered Rainbow Foil parallels of the top rookies · hobby and jumbo only", "p": "Griffin US1: Purple /250 $80 (1) · Black /75 $85 (1) · Orange /25 $325 (1) · Black Cat Foil /10 $85 (1) · Gold /2026 $38, $39, $40, $45, $50, $75. McGonigle US7: Gold /2026 $50, $50, $50, $60 (one at $100 on Oct 11). Murakami Black Sandglitter /10 Rookie Debut $499 (1). Odds: Purple /250 1 in 44 packs · Blue /150 1 in 74 · Green /99 1 in 112 · Gold /50 1 in 217 · Orange /25 1 in 433 · Black /10 1 in 1,082 · Red /5 1 in 2,168",
     "w": "Added together those odds give about one numbered Rainbow Foil per hobby box, and a Gold /2026 (1 in 21 packs) is the second numbered card. With 350 subjects the chance that either is one of the four best rookies is about 1 in 44 per box. The Griffin ladder is pricing where Allen & Ginter's did: $80 to $85 for anything /250 to /75, a jump at /25."},
    {"c": "Case-hit inserts: Home Field (HA), All Kings (AK), Heavy Lumber SSP", "p": "Griffin Home Field HA-59 $380 and $499 · Griffin All Kings AK-31 $1,200 and $1,400 · McGonigle Heavy Lumber HL-48 $300 (1) · McGonigle True Photo Variation SSP $550 (1)",
     "w": "Day-one prices from two sales each. These are the cards breakers are chasing, and on Oct 14 and 15 they sold for more than any numbered parallel of the same player. Topps has not published odds for them; treat them as the one-in-many-cases tier until a print run or ratio appears."},
    {"c": "Autographs: 1991 Topps, Real One, Flagship Autograph Patch, All-Star Stitches, 1952 Rookie Variation", "p": "About 200 autographs sold Oct 13 to 15, median about $40 (half between $20 and $100). 1991 Topps autos $25 (70) · Real One autos $75 (8) · patch autographs (Flagship Auto Patch, All-Star Stitches, Heavy Lumber) mostly $60 to $200 · Hao-Yu Lee autos $500 to $700 (3) · Bazzana Flagship Auto Green /99 $300 (1). No Griffin, McGonigle or Wetherholt autograph has sold",
     "w": "One autograph or relic per hobby box, and most boxes get the relic. The typical autograph is a $25 on-card 1991 Topps of a veteran or a mid-tier rookie; the chase signers (Griffin, McGonigle, Wetherholt among rookies, Trout, Acuña and Crow-Armstrong among veterans) have not reached the market yet, which usually means redemptions. Jumbo boxes guarantee one of each."}
   ]},
   {"h": "Tier 2 · Rookies: which card is the rookie card", "items": [
    {"c": "Konnor Griffin · US1 RC and US255 Rookie Debut", "p": "US1 base $2.29 (45, $0.99 to $9.99) · US255 Rookie Debut $2.92 (21) · Team Color Variation $150 (1) · Rainbow Foil $15 (1) · Black Gold insert BG-5 $9 (15) · 1991 Topps insert U91-24 $4 to $5 · Rising Rookies Relic $50 (2) · 1991 Topps relic $20 to $30 (3) · Flagship Autograph $190 (1)",
     "w": "US1 is the card with the RC logo; US255 is the Rookie Debut, a second card that has historically sold for less, though on day one buyers are paying a dollar more for it. His Allen & Ginter base is $2.99 on 50 sales, and this will be printed in larger numbers. Buy the numbered parallels or nothing."},
    {"c": "Kevin McGonigle · US7 RC and US140 Rookie Debut", "p": "US7 base $3.49 (51, $1.25 to $20, most under $4) · US140 Rookie Debut $4 (23) · Gold /2026 $50 to $60 (4) · Black Gold Pink parallel $35 to $50 (3) · Aqua foil $40 (1) · All-Star Stitches relic $37 (1) · Golden Mirror $400 (1) · True Photo Variation SSP $550 (1) · Heavy Lumber SSP $300 (1)",
     "w": "Baseball America's Rookie of the Year (.278 with 18 home runs in 156 games). His base card is selling for a dollar more than Griffin's and his chase cards for more than anyone's in the set; he is the best-priced rookie in the product on day one. Expect $2 to $3 for the base once more hobby cases are open."},
    {"c": "Munetaka Murakami · US350 Rookie Debut", "p": "US350 $2.22 (12, $0.99 to $9.99) · Team Color Border Variation US319 $70 (1) · Major League Material relic $43 to $45 (3) · 1991 Topps relic $29 to $39 (4) · All-Star Stitches relic $67 (1) · Rising Rookies Relic $25 and $50 · 1991 Topps autograph $100 (1)",
     "w": "Update has his Rookie Debut and two subset cards (US103, US246), not his base rookie card; that is #503 in the flagship set (PSA's catalog). The White Sox season ended in ALDS Game 5 on Oct 10. His 2026 Bowman Red RC Variation is the card with a graded market: PSA 10 $500 median on 19 sales in 90 days."},
    {"c": "JJ Wetherholt US50, Travis Bazzana US75, Justin Crawford US2, Carson Benge US3, Andrew Painter US63, Noah Schultz US105", "p": "Wetherholt Golden Mirror $199 (1) · Bazzana Flagship Auto Green /99 $300 (1) · Benge 1952 Rookie Variation $1,000 (1). Base cards $1 to $3",
     "w": "The second line of the class. Each also has a Rookie Debut card later in the set (Wetherholt US245, Bazzana US278). Base cards are $1 to $3; the parallels numbered /250 and lower are the versions with a price."},
    {"c": "Rookie Debut only: Roman Anthony US194, Jacob Misiorowski US136, Jac Caglianone US21, Nolan McLean US10, Trey Yesavage US58, Bryce Eldridge US334", "p": "McLean Golden Mirror US10 $300 (1) and Real One Golden Mirror autograph redemption $800 (1). Base Rookie Debuts $1 to $4",
     "w": "These players had their rookie cards in Series 1, Series 2 or last year's Update. A Rookie Debut is a real card with the RC logo, but collectors price it under the base rookie."}
   ]},
   {"h": "Tier 3 · Everything else in the box", "items": [
    {"c": "Inserts: 1991 Topps Baseball, 2026 All-Star Game, All Aces, Heavy Lumber, Home Field, Stat Stars, Black Gold", "p": "Griffin 1991 Topps U91-24 $4 to $5 · Griffin Black Gold BG-5 $9 (15) · Griffin Stars of MLB $3 to $5 · Griffin Autumn Ascensions $3 to $15 · Murakami Gold Autumn Ascensions /50 $200 (1)",
     "w": "About 17 inserts per hobby box, and at these prices they are set-filler apart from the SSP case hits above. The 1991 design is in its third series this year; a 100-card Chrome version comes only in the Silver Pack that ships with each hobby box (Silver Pack Mojo Griffin $9, McGonigle Purple /250 $70)."},
    {"c": "Unnumbered parallels: Rainbow Foil, Gold /2026", "p": "Griffin Rainbow Foil $15 (1) · Griffin Gold /2026 $38 to $75 (6) · McGonigle Gold /2026 $50 to $60 (4). Rainbow Foil 1 in 10 hobby packs, Gold /2026 1 in 21",
     "w": "Two Rainbow Foils and one Gold per box on average. The Gold is numbered to 2,026, which is not scarce; it carries a price only on the top rookies, where $50 on day one is more than the odds justify (one Griffin or McGonigle Gold every 175 boxes, roughly)."},
    {"c": "Relics: Major League Material, All-Star Stitches, Rising Rookie Relics, 1991 Topps relics, City Connect swatches", "p": "Murakami Major League Material $43 to $45 (3) · Griffin and Murakami Rising Rookies Relic $25 to $50 · 1991 Topps rookie relics $20 to $39 · McGonigle All-Star Stitches $37 (1), Murakami $67 (1)",
     "w": "The usual result of the one guaranteed hit. The rookie relics are holding $25 to $50 on day one; veterans' single-color swatches will be $10 cards. Budget the hit as a relic unless it turns out to be an autograph."}
   ]}
  ],
  "avoid": [
   "Paying $178 for a hobby box that Topps sold for $109.99. The release-day median (34 boxes, Oct 14 to 15) is the same as the presale median, so the market has not yet priced in the fact that the box's one hit is usually a $10 to $50 relic. The jumbo at $325 is the better buy per card if you are opening anything: 400 cards, two hits, two Silver Packs.",
   "Buying a box for the rookies. A hobby box holds 240 cards with about two numbered parallels, and the odds that either is Griffin, McGonigle, Wetherholt or Bazzana are about 1 in 44. The base rookies cost $2 to $3.50 each on day one and will cost less next week.",
   "Grading base rookies from this set at $59.99 a card. The 2018 Update base rookies of Ronald Acuña Jr. and Juan Soto, with 63% and 65% gem rates, sell for $35 and $39 in PSA 10 (197 and 221 sales in 90 days, PSA APR Oct 12); the Raw-to-Gem model puts the expected loss at $54 and $56 a card. The 2018 Ohtani US1 clears because a PSA 10 is $495. A flagship base rookie only pays for grading when the player becomes that.",
   "Reading the single-sale prices above as settled. The $1,000 Benge 1952 variation, the $1,400 Griffin All Kings and the $550 McGonigle photo variation are one or two sales each on the first two days; they will move, probably down, as cases are opened.",
   "Confusing Rookie Debut cards with rookie cards when buying lots. Griffin, McGonigle, Wetherholt and Bazzana have both in this set; check the card number."
  ],
  "notes": [
   "Refreshed Nov 2 (eBay sold listings read in the browser pane, lots, cases and breaks excluded): hobby box $160 median on 48 sales Oct 26 to Nov 1 ($139.50 to $349.99), down from $178 at release; jumbo $315 median on 52 sales ($280 to $600), unchanged. Griffin US1 base about $2 (28 sales Oct 30 to Nov 1, $0.50 to $9.99 for the base and unnumbered foils) and McGonigle US7 base $1.99 (33 sales, $0.55 to $19.99), both down from $2.29 and $3.49 on day one. The other single-card lines below keep their Oct 13 to 15 reads.",
   "Hobby odds used above (Checklist Insider): Rainbow Foil 1:10, Gold /2026 1:21, Purple Rainbow /250 1:44, Blue /150 1:74, Green /99 1:112, Gold Rainbow /50 1:217, Orange /25 1:433, Independence Day /76 1:560, Black /75 and 75 Years of Topps /75 1:567, Golden Mirror 1:606, Canvas /50 1:851, Black Rainbow /10 1:1,082, Wood /25 and Memorial Day Camo /25 1:1,701, Clear 1:2,058, Red Rainbow /5 1:2,168, 1952 Rookie Variation 1:5,952, Golden Mirror Legend 1:11,904, Player Number variation 1:29,671.",
   "Formats: hobby (20 packs of 12 plus a five-card Silver Pack), jumbo (10 packs of 40, two Silver Packs), value box (6 packs of 12, $24.99 at Topps), hanger (59 cards), fat pack (36 cards), super box. Sandglitter parallels are jumbo-only, Diamante hanger-only, Holiday variations retail-only, Clear variations hobby-only.",
   "Checklist counts are from baseball.cards and Cardsmiths Breaks and agree with each other on the card numbers quoted here. Topps marks the checklist as subject to change.",
   "Topps does not publish a print run. Update is the third series of the flagship set and is sold in every format at mass retail; treat every unnumbered base card as unlimited.",
   "Still pending: a Griffin or McGonigle 1952 Rookie Variation sale, any Griffin, McGonigle or Wetherholt autograph, and odds for the Home Field, All Kings and Heavy Lumber SSP inserts. Next refresh after the first full week of sales.",
   "Verdict: a strong rookie checklist in the most heavily printed product of the year. At $109.99 a hobby box was a fair rip for set builders; at $178 it is a pass, and the $325 jumbo is the format to open if you must. Buy the singles: numbered parallels of Griffin and McGonigle at $80 to $85 for the /250 to /75 colors, and wait on the SSP case hits until there are more than two sales of each."
  ],
  "src": "Box prices: eBay sold listings, Oct 14 to 15 (post-release) and Sep 14 to Oct 12 (presale), medians with counts, single boxes only. Single-card prices: eBay sold listings, Oct 14 to 15, medians with counts where five or more sold, otherwise individual sales. Topps price and configuration: Topps.com and Checklist Insider. Checklist and odds: Checklist Insider, Cardsmiths Breaks, baseball.cards. 2018 Update comparison: PSA Auction Prices Realized and pop report, Oct 12. Player context: Baseball America, CBS Sports."
 }
}

MARK = '/* topps-update-2026 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', lambda m: entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
# The short sample preview for the same product is replaced by this entry.
s = re.sub(r' \{kind:"Preview",n:"2026 Topps Update Series Baseball",.*?\]\},\n', '', s, count=1, flags=re.S)
open(P, 'w').write(s)
print('ok', len(s))
