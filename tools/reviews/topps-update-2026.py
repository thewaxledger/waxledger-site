"""Add the 2026 Topps Update Series Baseball deep review to the master page (idempotent).
Written Oct 12, two days before release: the structure and odds are final, box prices are presale sales,
single-card prices are a handful of early retail sales and are marked as such. Refresh after Oct 14."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Topps Update Series Baseball", "when": "Out Oct 14 · presale prices", "score": "5.4",
 "facts": [
  "Hobby: 20 packs of 12 with one autograph or relic. $109.99 at Topps' Sep 14 presale (sold out); $180 median on eBay presale (29 boxes sold Oct 1 to 12, $165 to $250)",
  "Jumbo: 10 packs of 40 with one autograph and one relic, $319 median (41 sold Sep 14 to Oct 11). Hobby cases $2,025 median (13 sold), about $169 a box",
  "350 cards, US1 to US350: 85 rookie cards, 40 Rookie Debut cards, 195 veterans, 16 Veteran Combos, 14 Season Highlights",
  "Rookie cards: Konnor Griffin US1, Kevin McGonigle US7, JJ Wetherholt US50, Travis Bazzana US75. Rookie Debut: Munetaka Murakami US350, Roman Anthony US194",
  "About two numbered parallels per hobby box. 1952 Rookie Variations fall 1 in 5,952 hobby packs, about one every 25 cases"
 ],
 "bars": [["Rookie class", 8.5], ["Hit quality", 5.0], ["Print run", 3.5], ["Price vs. value", 4.5]],
 "deep": {
  "lede": "Written Oct 12, two days before release. The checklist and odds are published, so the shape of the product is known. Box prices below are real presale sales from eBay sold listings. Single-card prices are not a market yet: some retail product reached buyers early and a few dozen singles sold between Oct 8 and Oct 12, one to four sales per card. Those are listed as individual sales, not medians, and the full price tables will be added once hobby boxes open. The short version: the rookie class is the same one that carries Allen & Ginter and Bowman Chrome this year, the base cards will be printed in very large numbers, and the hobby box is selling for about $70 over what Topps charged.",
  "sections": [
   {"h": "Tier 1 · The cards worth opening a hobby box for", "items": [
    {"c": "1952 Rookie Variations · 25 cards, short print", "p": "Prices pending. 1 in 5,952 hobby packs",
     "w": "The new chase this year: 25 rookies on the 1952 Topps design, with a separate 24-card autograph version. At 20 packs a box that is one every 298 boxes, or about one in 25 cases. Nobody should buy a box expecting one; they matter because they will set the top of the singles market for Griffin and McGonigle."},
    {"c": "Golden Mirror variations · all 350 cards", "p": "One early sale: Connelly Early US285 $170 (Oct 10). 1 in 606 hobby packs",
     "w": "About one every 30 hobby boxes, or about two in every five cases. The single sale above is a mid-tier rookie; a Griffin or McGonigle will sell for a multiple of it. Golden Mirror Legend variations (50 cards) are 1 in 11,904 packs."},
    {"c": "Numbered Rainbow Foil parallels of the top rookies · hobby and jumbo only", "p": "Prices pending. Purple /250 1 in 44 packs · Blue /150 1 in 74 · Green /99 1 in 112 · Gold /50 1 in 217 · Orange /25 1 in 433 · Black /10 1 in 1,082 · Red /5 1 in 2,168",
     "w": "Added together those odds give about one numbered Rainbow Foil per hobby box, and a Gold /2026 (1 in 21 packs) is the second numbered card. With 350 subjects the chance that either is one of the four best rookies is about 1 in 44 per box. One early Gold /2026 has sold: McGonigle US7 at $100 on Oct 11, a single sale."},
    {"c": "Autographs: 75 Years of Topps, Real One, 1952 Rookie Variation, Flagship Autograph Patch", "p": "Prices pending",
     "w": "One autograph or relic per hobby box, and most boxes get the relic. Chase signers named on the checklist include Griffin, McGonigle and Wetherholt among rookies and Mike Trout, Ronald Acuña Jr. and Pete Crow-Armstrong among veterans. Jumbo boxes guarantee one of each."}
   ]},
   {"h": "Tier 2 · Rookies: which card is the rookie card", "items": [
    {"c": "Konnor Griffin · US1 RC and US255 Rookie Debut", "p": "Early sales, Oct 8 to 12: US1 base $2.50 and $3.25 · US255 Rookie Debut $5 · retail Orange/Black Foil $6 and $10 · Jack O'Lantern $6.99",
     "w": "US1 is the card with the RC logo; US255 is the Rookie Debut, a second card that has historically sold for less. His Allen & Ginter base is $2.99 on 50 sales and this will be printed in larger numbers. Buy the numbered parallels or nothing."},
    {"c": "Kevin McGonigle · US7 RC and US140 Rookie Debut", "p": "Early sales, Oct 8 to 12: US7 base $2.50, $12.50, $12.50 · US140 Rookie Debut $4 and $5 · Gold /2026 $100 (1) · All-Star Game insert $7",
     "w": "Baseball America's Rookie of the Year (.278 with 18 home runs in 156 games). Three base sales between $2.50 and $12.50 show there is no settled price yet. Expect $2 to $4 once hobby cases are open."},
    {"c": "Munetaka Murakami · US350 Rookie Debut", "p": "Early sales, Oct 8 to 12: US350 $3.95 and $4.50 · retail Holiday parallel $9.99 · Black Gold insert $15",
     "w": "Update has his Rookie Debut and two subset cards (US103, US246), not his base rookie card; that is #503 in the flagship set (PSA's catalog). The White Sox season ended in ALDS Game 5 on Oct 10. His 2026 Bowman Red RC Variation is the card with a graded market: PSA 10 $500 median on 19 sales in 90 days."},
    {"c": "JJ Wetherholt US50, Travis Bazzana US75, Justin Crawford US2, Carson Benge US3, Andrew Painter US63, Noah Schultz US105", "p": "Early sales: Wetherholt US50 $3 and $4.50. The rest pending",
     "w": "The second line of the class. Each also has a Rookie Debut card later in the set (Wetherholt US245, Bazzana US278). Base cards will be $1 to $3; the parallels numbered /250 and lower are the versions with a price."},
    {"c": "Rookie Debut only: Roman Anthony US194, Jacob Misiorowski US136, Jac Caglianone US21, Nolan McLean US10, Trey Yesavage US58, Bryce Eldridge US334", "p": "One early sale: Misiorowski US136 $19.99 (Oct 9), which is high for a Rookie Debut and should not be read as the price",
     "w": "These players had their rookie cards in Series 1, Series 2 or last year's Update. A Rookie Debut is a real card with the RC logo, but collectors price it under the base rookie."}
   ]},
   {"h": "Tier 3 · Everything else in the box", "items": [
    {"c": "Inserts: 1991 Topps Baseball, 2026 All-Star Game, All Aces, Heavy Lumber, Home Field, Stat Stars", "p": "Early sales: McGonigle 1991 Topps $15 (1) · Ohtani \"Doing It All\" US240 $8.99, $8.99, $15",
     "w": "About 17 inserts per hobby box. The 1991 design is in its third series this year; a 100-card Chrome version comes only in the Silver Pack that ships with each hobby box."},
    {"c": "Unnumbered parallels: Rainbow Foil, Gold /2026", "p": "Prices pending. Rainbow Foil 1 in 10 hobby packs, Gold /2026 1 in 21",
     "w": "Two Rainbow Foils and one Gold per box on average. The Gold is numbered to 2,026, which is not scarce; it carries a price only on the top rookies."},
    {"c": "Relics: Major League Material, All-Star Stitches, Rising Rookie Relics, City Connect swatches", "p": "Prices pending",
     "w": "The usual result of the one guaranteed hit. Most of these are plain single-color swatches of veterans. Budget the hit as a relic unless it turns out to be an autograph."}
   ]}
  ],
  "avoid": [
   "Paying $180 for a hobby box that Topps sold for $109.99. The 87 presale boxes sold on eBay since Sep 14 have a $175 median and the last 29 are at $180; there is no post-release price yet, and a presale premium of $70 over the Topps price is a lot to pay for one autograph or relic.",
   "Buying a box for the rookies. A hobby box holds 240 cards with about two numbered parallels, and the odds that either is Griffin, McGonigle, Wetherholt or Bazzana are about 1 in 44. The base rookies will cost less than a pack.",
   "Grading base rookies from this set at $59.99 a card. The 2018 Update base rookies of Ronald Acuña Jr. and Juan Soto, with 63% and 65% gem rates, sell for $35 and $39 in PSA 10 (197 and 221 sales in 90 days, PSA APR Oct 12); the Raw-to-Gem model puts the expected loss at $54 and $56 a card. The 2018 Ohtani US1 clears because a PSA 10 is $495. A flagship base rookie only pays for grading when the player becomes that.",
   "Reading the early single sales above as prices. They come from a few retail boxes opened before release, one to four sales per card.",
   "Confusing Rookie Debut cards with rookie cards when buying lots. Griffin, McGonigle, Wetherholt and Bazzana have both in this set; check the card number."
  ],
  "notes": [
   "Hobby odds used above (Checklist Insider): Rainbow Foil 1:10, Gold /2026 1:21, Purple Rainbow /250 1:44, Blue /150 1:74, Green /99 1:112, Gold Rainbow /50 1:217, Orange /25 1:433, Independence Day /76 1:560, Black /75 and 75 Years of Topps /75 1:567, Golden Mirror 1:606, Canvas /50 1:851, Black Rainbow /10 1:1,082, Wood /25 and Memorial Day Camo /25 1:1,701, Clear 1:2,058, Red Rainbow /5 1:2,168, 1952 Rookie Variation 1:5,952, Golden Mirror Legend 1:11,904, Player Number variation 1:29,671.",
   "Formats: hobby (20 packs of 12 plus a five-card Silver Pack), jumbo (10 packs of 40, two Silver Packs), value box (6 packs of 12, $24.99 at Topps), hanger (59 cards), fat pack (36 cards), super box. Sandglitter parallels are jumbo-only, Diamante hanger-only, Holiday variations retail-only, Clear variations hobby-only.",
   "Checklist counts are from baseball.cards and Cardsmiths Breaks and agree with each other on the card numbers quoted here. Topps marks the checklist as subject to change.",
   "Topps does not publish a print run. Update is the third series of the flagship set and is sold in every format at mass retail; treat every unnumbered base card as unlimited.",
   "Pending after release: medians with counts for the base rookies, the numbered parallels, 1952 Rookie Variations, autographs by signer and relics.",
   "Verdict for now: a strong rookie checklist in the most heavily printed product of the year. At $109.99 a hobby box was a fair rip for set builders; at $180 it is a pass. Wait a week and buy the singles: numbered parallels of Griffin and McGonigle, and any 1952 Rookie Variation that lists before the market has a price for it."
  ],
  "src": "Box prices: eBay sold listings, Sep 14 to Oct 12 (presale), medians with counts. Single-card prices: eBay sold listings, Oct 8 to 12, individual early sales only. Topps price and configuration: Topps.com and Checklist Insider. Checklist and odds: Checklist Insider, Cardsmiths Breaks, baseball.cards. 2018 Update comparison: PSA Auction Prices Realized and pop report, Oct 12. Player context: Baseball America, CBS Sports."
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
