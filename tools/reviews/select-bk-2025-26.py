"""Add the 2025-26 Panini Select Basketball deep review to the master page (idempotent).
Written Oct 22, the day before the hobby release (Oct 23; First Off The Line boxes shipped from Oct 14). Structural
review: the checklist and box contents are published, pack odds and the print run are not. The only sold prices are
sealed boxes on eBay (read in the browser pane, LH_Sold=1&LH_Complete=1); no single from the NBA set had a completed
sale by Oct 22, so single-card prices are pending. Refresh with eBay sold medians once hobby cases are open."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2025-26 Panini Select Basketball", "when": "Out Oct 23 · single prices pending", "score": "4.6",
 "facts": [
  "Hobby: 12 packs of 5 (60 cards) with three autographs or memorabilia cards, 24 base Prizms parallels and 6 inserts per box, 12 boxes a case. Steel City presale $324.95; one eBay sale at $309.99 (Oct 18); other eBay presale asks $285 to $350",
  "First Off The Line (out Oct 14): same box plus one FOTL autograph /10 or less and three FOTL base Prizms /10 or less. eBay sold $700 median (3 boxes, $675 to $720, Oct 14 to 19)",
  "No NBA license: no team or league logos, and Cooper Flagg, Dylan Harper, Ace Bailey and Kon Knueppel are not in the set. The rookie class on the checklist is led by VJ Edgecombe, Tre Johnson, Derik Queen, Jeremiah Fears, Khaman Maluach, Cedric Coward and Carter Bryant",
  "Base set in the usual tiers: Concourse #1-100, Premier Level #101-200, Courtside #201-300; Checklist Insider lists a fourth Mezzanine Level tier for 400 cards, Cardsmiths Breaks lists 300. 49 Prizms parallels on Concourse, from Silver and Zebra to Tie-Dye /25, Gold /10, Green /5 and Black Finite 1/1",
  "Panini has not published pack odds or a print run; no single card from the set had a completed eBay sale by Oct 22"
 ],
 "bars": [["Rookie class", 4.0], ["Hit quality", 5.5], ["Print run", 5.0], ["Price vs. value", 4.0]],
 "deep": {
  "lede": "Written Oct 22, the day before the hobby release (Oct 23). First Off The Line boxes have been out since Oct 14, so the checklist is confirmed and three FOTL boxes have sold, but no single card from the NBA set had a completed eBay sale when this was written: the single-card prices below are pending and will be filled in once hobby cases are open. The short version: this is Select without the NBA logos and without the top four rookies. Topps holds the NBA license this season, and Flagg, Harper, Bailey and Knueppel are not on this checklist at all. What is left is the Optichrome design, the three-tier base set, the Tie-Dye and Zebra parallels, three hits a box, and a rookie list that starts at VJ Edgecombe. A hobby box at $310 to $325 is 60 cards; the question is whether a Select rookie autograph of Edgecombe or Queen with no team logo on it holds the value the licensed version did, and that is what the first week of sales will answer.",
  "sections": [
   {"h": "Tier 1 · The cards worth opening a hobby box for", "items": [
    {"c": "VJ Edgecombe · Concourse #38, Premier #133, Courtside #240; Rookie Signatures, Rookie Jersey Autographs, Jumbo Rookie Signature Swatches", "p": "Prices pending",
     "w": "The No. 3 pick (76ers) and the first name on this checklist's rookie list. Rookie Signatures are /249 or less with Tie-Dye /25, Gold /10 and Green /5; Rookie Jersey Autographs /99 or less. The Courtside tier is one card in 300 of the base set, so a Courtside Edgecombe parallel is the base chase. With Flagg absent, this is the card a Select box is bought for."},
    {"c": "Derik Queen #17/#114/#233, Tre Johnson #3/#107/#223, Jeremiah Fears #13/#109/#216, Khaman Maluach #43/#121/#231, Cedric Coward #39/#116/#232, Carter Bryant", "p": "Prices pending",
     "w": "Steel City's chase list for autographs is Edgecombe, Queen, Nique Clifford, Asa Newell, Coward and Bryant; Cardsmiths Breaks names Edgecombe, Fears and Coward. None of them is a top-four pick, which is what the rookie-class score reflects."},
    {"c": "Tie-Dye /25, Zebra, Gold /10, Green /5, Black Finite 1/1, Gold Vinyl 1/1 · Concourse, Premier and Courtside", "p": "Prices pending. For scale, the Panini Select EuroLeague Zebras from the same year sell at $5.50 median (36 sales, $1.50 to $25, Jul 27 to Oct 20), and those are not the NBA cards",
     "w": "Zebra is unnumbered and Select's signature chase; Tie-Dye /25 is the numbered one. Each exists on every tier, so a Courtside Zebra of a specific rookie is rare twice over. The EuroLeague numbers are quoted for scale only; the NBA set will price separately."},
    {"c": "Legend autographs · Larry Bird, Shaquille O'Neal, Magic Johnson, Allen Iverson, Dwyane Wade, Hakeem Olajuwon, Kevin Garnett, Julius Erving, Steve Nash; Ja Morant, Cade Cunningham, Giannis", "p": "Prices pending",
     "w": "Steel City's veteran chase list. Signatures and Select Few Signatures (/49 or less) carry them; Immaculate, Flawless and NT-branded autograph subsets (/99, /25, /10) are folded in as hobby hits. With no current-team logos to sell, the legend list is doing more of the work this year."}
   ]},
   {"h": "Tier 2 · Mid-range: inserts and the numbered middle", "items": [
    {"c": "Super short print inserts · Color Wheel (25), Stained Glass (25), Solar Eclipse (15)", "p": "Prices pending",
     "w": "Select's case hits. No odds published; in past years one or two per case. These carry the design, not the logo, so the licensing change should hurt them least."},
    {"c": "Hobby-exclusive inserts · En Fuego (15), Select Future (25), Introductions (20), Notoriety (25, new), Select Buckets (15, new); parallels /149 or less", "p": "Prices pending",
     "w": "Six inserts or insert parallels a box on average. Notoriety and Select Buckets are new this year; the rest are returning sets. Micro Mosaic, Neon Icon, Rookie Revolution, Lodestars and Hot Stars fill out the 301-card insert checklist."},
    {"c": "Numbered base Prizms · Light Blue /299, Red /199, White /149, Purple /125, Blue Camo /99, Neon Green /75, Orange /65, White Wave /49, White Scope /35, Green Wave /25, Red Mojo /20", "p": "Prices pending",
     "w": "24 base Prizms a box, most of them the unnumbered Silver, Blue, Scope, Disco, Tiger and Elephant. The numbered ladder is 49 deep on Concourse and gets shorter on Courtside, where the list starts at Blue Flash /99."},
    {"c": "Relics · Debut Memorabilia, Draft Selections, Jumbo Rookie Swatches (30), Select Swatches, Sparks, Select Threads; base /99, Tie-Dye /25, Gold /10", "p": "Prices pending",
     "w": "Three hits a box with no autograph guarantee stated, so a box can be three relics. Unlicensed relics are swatches of player-worn material without a team mark; that is the piece of a Select box the license change hits hardest."}
   ]},
   {"h": "Tier 3 · Everything else in the box", "items": [
    {"c": "Base cards · Concourse #1-100, Premier #101-200, Courtside #201-300 (plus Mezzanine per Checklist Insider)", "p": "Prices pending",
     "w": "60 cards a box, 24 of them parallels, so about 36 base. Giannis #1/#102/#201, Trae Young #2/#101/#202, Morant #99/#200/#299, Cunningham #100/#199/#300 bookend each tier. Veteran base without logos sells for less than the licensed version did; the rookies will tell."},
    {"c": "Unnumbered Concourse parallels · Blue Cracked Ice, Blue, Cosmic, Disco, Dragon Scale, Elephant, Gold Glitter, Green Mojo, Orange Flash, Red Cracked Ice, Scope, Silver, Tiger, White Sparkle", "p": "Prices pending",
     "w": "The bulk of the 24 Prizms per box. Silver is the one with a market outside the top rookies."},
    {"c": "Veteran and second-tier rookie autographs · Signatures (40), Signature Selections (40), Youth Explosion Signatures (39), Selection Committee (19)", "p": "Prices pending",
     "w": "On a three-hit box, the modal hit is one of these or a relic. The rookie autograph list runs 40 deep across Rookie Signatures, so most rookie autographs will be second-round picks and two-way players."}
   ]}
  ],
  "avoid": [
   "Buying a Select box for Cooper Flagg. He is not in it, and neither are Harper, Bailey or Knueppel. Their rookie cards are in Topps products (Chrome, Flagship, Bowman) this year.",
   "Paying FOTL money ($675 to $720 sold) for one FOTL autograph /10 and three FOTL Prizms /10 on top of a $310 box. The FOTL cards are of the same rookie list; the premium buys serial numbers, not Flagg.",
   "Reading presale asks as prices. One hobby box has sold on eBay ($309.99, Oct 18); the $285 to $350 figures on the checklist sites are listings. Singles have no sold price at all yet.",
   "Assuming last year's Select prices carry over. 2024-25 Select had the NBA license and the logos; this is the first unlicensed Select, and Panini itself says it only has part of the draft class. Wait for a week of sales before paying licensed-era prices for an unlicensed autograph.",
   "Mixing up the 2025-26 Select EuroLeague and Select WNBA cards with this set when searching eBay. All three are titled '2025-26 Panini Select', and the EuroLeague Zebras and Tie-Dyes are the ones that have been selling."
  ],
  "notes": [
   "Box contents (Checklist Insider, Cardsmiths Breaks, Steel City): hobby 12 packs of 5, three autographs or memorabilia cards, 24 base Prizms, 6 inserts or insert parallels per box on average, 12 boxes a case. FOTL (Oct 14): the same plus one FOTL autograph /10 or less and three FOTL base Prizms /10 or less; Spectris Gold FOTL, Spectris Green FOTL and Prizms FOTL are the FOTL-only parallels.",
   "Prices (eBay sold, read Oct 22): FOTL hobby $700 median, 3 sales, $675 to $720, Oct 14 to 19. Hobby $309.99, 1 sale, Oct 18 (presale). Steel City presale $324.95. Checklist Insider's eBay presale listings $284.95 to $349.99 and a 12-box case at $6,659.91 ($555 a box) are asks, not sales. No single card from the NBA set had a completed sale.",
   "Licensing: this is Panini's first Select Basketball without the NBA license (Checklist Insider: it 'loses the official NBA team and league logos'); Topps holds the NBA license for 2025-26 and its Chrome and Flagship sets carry Flagg, Harper, Bailey and Knueppel. Checklist Insider: Panini 'only has access to a portion of the NBA draft class'. Those four do not appear in any section of the Select checklist; Cardlines notes Flagg and Knueppel are not signing for Panini.",
   "Rookies on the checklist: Edgecombe (#38, #133, #240), Tre Johnson (#3, #107, #223), Fears (#13, #109, #216), Queen (#17, #114, #233), Maluach (#43, #121, #231), Coward (#39, #116, #232), Hansen Yang (#19, #143, #206), plus Carter Bryant, Asa Newell, Nique Clifford, Noa Essengue, Walter Clayton Jr., Kobe Sanders, Darius Acuff Jr., Ryan Kalkbrenner and Yaxel Lendeborg. Rookie Signatures 40 cards, Rookie Jersey Autographs 40, Jumbo Rookie Signature Swatches 30.",
   "Base set: Cardsmiths Breaks lists 300 cards (Concourse, Premier Level, Courtside); Checklist Insider lists 400 with a Mezzanine Level tier. Concourse parallels (49): unnumbered Silver, Zebra, Scope, Disco, Tiger, Elephant, Cosmic, Dragon Scale, Gold Glitter and others; numbered Light Blue /299 to Gold /10, Green /5, Silver Vinyl /5, Black Finite 1/1, Gold Vinyl 1/1. Courtside drops the higher-numbered parallels and starts at Blue Flash /99.",
   "Inserts (301 cards): Color Wheel 25, Stained Glass 25, Solar Eclipse 15 (super short prints); En Fuego 15, Select Future 25, Introductions 20, Notoriety 25, Select Buckets 15 (hobby); Crown Jewels 20, Hot Stars 15, Lodestars 15, Micro Mosaic 15, Neon Icon 25, Rookie Revolution 25, Select Certified 20; an Asa Newell All-Star Game Instant Access card. Relics 199 cards across eight sets. Autographs 384 cards across the sets named above plus Immaculate, Flawless and NT-branded subsets.",
   "The scores are a first read. Rookie class is scored on who is in the set, not on the draft class: the top four picks are absent. Hit quality is the three hits with no autograph guarantee. Print run is in the middle because none is published. Price vs. value uses the $310 to $325 box and no single prices. Pending after release: eBay sold medians with counts for the hobby box, the Edgecombe and Queen base, Silver, Zebra and Tie-Dye, the rookie autographs and the super short print inserts.",
   "Verdict for now: wait. At $310 to $325 for 60 cards, three hits and no Flagg, the box needs the Edgecombe autograph market to hold up without a logo on the card, and nothing has sold yet to say it does. If you want Select, buy singles after the first weekend."
  ],
  "src": "Box prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Oct 22, 2026 in the browser pane, break slots and lots excluded by title. Presale price: Steel City Collectibles. Formats, checklist, tiers, parallels, inserts, autograph and relic sets, licensing note and the absent rookies: Checklist Insider (2025-26 Panini Select Basketball guide) and Cardsmiths Breaks (hobby box checklist). EuroLeague Zebra prices for scale: eBay sold, 36 sales Jul 27 to Oct 20."
 }
}

MARK = '/* select-bk-2025-26 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', lambda m: entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
open(P, 'w').write(s)
print('ok', len(s))
