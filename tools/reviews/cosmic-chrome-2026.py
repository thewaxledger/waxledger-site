"""Add the 2026 Topps Cosmic Chrome Baseball deep review to the master page (idempotent).
Written Nov 2, two days before the hobby release (Nov 4; Topps presale Oct 5 at $489.99). Structural review: the
checklist, pack odds and box contents are published; the only sold prices are presale hobby boxes on eBay (read in the
browser pane, LH_Sold=1&LH_Complete=1) and last year's product as a comp. No 2026 single had a completed sale by Nov 2,
so single-card prices are pending. Refresh with eBay sold medians once hobby cases are open."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Topps Cosmic Chrome Baseball", "when": "Out Nov 4 · single prices pending", "score": "5.2",
 "facts": [
  "Hobby: 20 packs of 4 (80 cards), 8 boxes a case. Topps presale $489.99 on Oct 5, up from $329.99 last year. eBay presale sold: $900 median on 76 single boxes Oct 5 to 23 ($700 to $1,000), $950 median on 8 boxes Oct 27 to 31",
  "Fewer than one autograph a box: Cardsmiths Breaks' per-box averages put it at about one in 2.7 hobby boxes; Checklist Insider's pack odds (1:136 for the 58-card main set, 1:653 and longer for the other five) work out closer to one in five. The box sells on the colour parallels, not the hit",
  "200-card base set with 77 rookies: Roman Anthony #122, Konnor Griffin #24, Kevin McGonigle #132, Munetaka Murakami #21, Jac Caglianone #5, Jacob Misiorowski #148, Chase Burns #184, Travis Bazzana #27, Tatsuya Imai #75, Kazuma Okamoto #130, Trey Yesavage #71, Cam Schlittler #66, Andrew Painter #177, Bryce Eldridge #73, Jonah Tong #6, Samuel Basallo #30. Nick Kurtz #136 is in the set without the RC mark",
  "Per hobby box (Cardsmiths Breaks' averages): about 62 base, 2 Refractors, 1 Nucleus, a Magenta Cosmos /299 in four of five boxes, Aqua /199 and White Hole in one of two, Purple /150 in one of 2.5, Blue Moon /99 in one of 3.8, Green /75 in one of five, Gold /50 about one a case, Orange /25 one in 15 boxes, Black /10 one in five cases, Red Flare /5 one in nine cases, SuperFractor one in 47 cases",
  "16 insert sets (532 cards) led by Extraterrestrial Talent (1:6 packs), Forces of the Diamond (1:8), Dual Star Clusters (1:25), Launched Into Orbit (1:40), Stars in the Night (1:80); StarFractor 1:282, Cosmic Dust 1:606, Planetarium 1:961, Mars Attacks MLB 1:1,513, Planetary Pursuit from Sun 1:120 to Pluto 1:28,000. Constellation variations 1:605, Anti-Gravity 1:961 (Checklist Insider)",
  "Comp: a 2025 Cosmic Chrome hobby box sells for $1,150 median on 19 eBay sales Oct 3 to Nov 1 ($870 to $1,400); a 2025 Cosmic Chrome Roki Sasaki base RC about $4 (27 sales Oct 13 to Nov 1, Ultraviolet Beam inserts included)"
 ],
 "bars": [["Rookie class", 7.5], ["Hit quality", 3.5], ["Print run", 5.5], ["Price vs. value", 4.0]],
 "deep": {
  "lede": "Written Nov 2, two days before the hobby release (Nov 4). Topps sold the presale on Oct 5 at $489.99, $160 more than last year's $329.99, and eBay has priced it well above that: 76 single presale boxes sold for a $900 median between Oct 5 and 23, and the eight that sold in the last week of October went for $950. No 2026 single has a completed sale yet, so every single-card price below is pending and will be filled in once cases are open; the structure and last year's product are enough for a first verdict. Cosmic Chrome is a parallel product. A box is 80 cards and a hit is the exception (one autograph in roughly three to five boxes, depending on whose odds you read), so what you are buying for $900 to $950 is about two numbered colour refractors (Cardsmiths Breaks' averages, Magenta /299 through Orange /25) and the chance that one of them is an Anthony, Griffin, McGonigle or Murakami in a short colour. The rookie class is the strongest Topps has had in years and the design is the one that holds its value on the secondary market (2025 boxes sell for $1,150 a year on), which is the case for it. The case against is the price: at $950 a box, a case is $7,600 for about two or three autographs, one Gold /50 and roughly 19 other numbered cards.",
  "sections": [
   {"h": "Tier 1 · The cards worth opening a hobby box for", "items": [
    {"c": "Roman Anthony #122 RC · colour refractors: Orange /25, Black Eclipse /10, Red Flare /5, SuperFractor 1/1", "p": "Prices pending. Comp: his 2026 Topps #189 base RC is $40 in PSA 10 on 158 sales in 90 days (Raw-to-Gem board, Nov 1); 2025 Cosmic Chrome Sasaki base RC about $4 on 27 sales",
     "w": "The rookie of the set and the card every Cosmic Chrome break is sold on. The base and Refractor will be cheap (last year's Sasaki base is $4); the numbered colours under /99 are the ones with a market, and the Black /10 and Red /5 are case-level hits that come out of one box in five to nine cases."},
    {"c": "Konnor Griffin #24, Kevin McGonigle #132, Munetaka Murakami #21 · numbered colours", "p": "Prices pending. Comps: Griffin 2024 Bowman Draft Chrome 1st PSA 10 $134, McGonigle 2025 Bowman Chrome 1st PSA 10 $140, Murakami 2026 Bowman Chrome RC PSA 10 $220 (Raw-to-Gem board, Oct 11 to Nov 1)",
     "w": "The three names after Anthony. Murakami is the one with the most open money behind him (his Bowman paper RC trades 167 times a month raw) and the one whose first Chrome-brand MLB card this is; Griffin and McGonigle are prospect money moving to a rookie card."},
    {"c": "Autographs · Cosmic Chrome Autographs (58 cards, 1:136), Extraterrestrial Talent (20, 1:653), Launched Into Orbit (32, 1:1,051), Stellar Stars (21, 1:1,622), Star Clusters duals (20, 1:15,535); parallels Green /75 to SuperFractor 1/1", "p": "Prices pending",
     "w": "Not in every box, and the odds say most boxes have none: Cardsmiths' averages put an autograph in one of 2.7 boxes, Checklist Insider's pack odds nearer one in five. When one comes it is usually from the 58-card main set, which is rookies and second-year players on sticker; the dual and the Stellar Stars are the ones worth something."},
    {"c": "Cosmic Explorers Cut Signatures · 17 cards, 1:85,901 packs: Einstein, Sagan, Armstrong, Sally Ride, Newton", "p": "Prices pending. No sale possible yet",
     "w": "New this year and the one card in the set that is not a baseball card. At 1:85,901 packs that is one in about 537 cases; it is a lottery ticket, not a reason to buy."}
   ]},
   {"h": "Tier 2 · Mid-range: the numbered middle", "items": [
    {"c": "Numbered base refractors · Magenta Cosmos /299 (4 in 5 boxes), Aqua Equinox /199 (1 in 2), Purple Nebula /150 (1 in 2.5), Blue Moon /99 (1 in 3.8), Green Space Dust /75 (1 in 5), Gold Interstellar /50 (about 1 a case), Orange Galactic /25 (1 in 15 boxes)", "p": "Prices pending",
     "w": "This is the product. A box returns about two numbered cards on average, and which player is on them decides whether the box paid: a Magenta /299 of a veteran is a $5 card, a Gold /50 Anthony is not. The new Magenta /299 adds a numbered card to most boxes without adding value."},
    {"c": "Planetary Pursuit · 100 cards in ten planet tiers, Sun 1:120 packs to Pluto 1:28,000; planet number now on the front", "p": "Prices pending",
     "w": "The insert that gives Cosmic Chrome its case-hit ladder. The rarer planets (Neptune, Pluto) of Anthony or Ohtani will be the biggest non-autograph sales of the release; the Sun and Mercury tiers are $5 to $20 cards in a normal year."},
    {"c": "Variations · Constellation (25 cards, 1:605) and Anti-Gravity (25 cards, 1:961; Black /10, Red /5, SuperFractor 1/1)", "p": "Prices pending",
     "w": "One Constellation variation in about 30 boxes and one Anti-Gravity in 48. Both are new designs; last year's variations sold on the player, not the design."},
    {"c": "StarFractor (100 cards, 1:282), Cosmic Dust (25, 1:606), Planetarium (25, 1:961), Mars Attacks MLB (10, 1:1,513)", "p": "Prices pending",
     "w": "Rare inserts with one or two chase names each. Mars Attacks is the collaboration with Topps' own sci-fi brand and the one that will trade on novelty; StarFractor is the pattern card that holds up."}
   ]},
   {"h": "Tier 3 · Everything else in the box", "items": [
    {"c": "Base cards · about 62 of the 80, plus 2 Refractors (1:10) and a Nucleus Refractor (1:20) per box", "p": "Prices pending. Comp: 2025 Cosmic Chrome Sasaki base RC about $4 on 27 sales",
     "w": "Three quarters of the box. The base card is a chrome design with a dark background and sells for a dollar or two outside the top four rookies; the unnumbered Refractor and Nucleus add a little."},
    {"c": "Common inserts · Extraterrestrial Talent (35 cards, 1:6), Forces of the Diamond (22, 1:8), Dual Star Clusters (8, 1:25), Launched Into Orbit (50, 1:40), Stars in the Night (25, 1:80)", "p": "Prices pending",
     "w": "About five inserts a box, most of them Extraterrestrial Talent and the new Forces of the Diamond. At 1:6 and 1:8 packs these are $2 to $5 cards unless the player is Anthony or Ohtani."},
    {"c": "Lunar box · Topps.com format: the same 80 cards with about 41 base, about 10 Lunar Eclipse /10 parallels and an autograph in three of four boxes (Cardsmiths Breaks)", "p": "No eBay sale yet",
     "w": "The format that puts the hits in every box: ten /10 parallels and most boxes with an autograph. Topps has not published a price and none has sold on eBay; if it lands near the hobby price it is the better box, and the one to compare before buying hobby."}
   ]}
  ],
  "avoid": [
   "Paying $950 for the autograph. Most hobby boxes have none: one in about 2.7 boxes by Cardsmiths Breaks' averages, nearer one in five by Checklist Insider's pack odds. Buy it for the numbered colours or not at all.",
   "Reading the presale price as the release price. 76 presale boxes sold at a $900 median and the last eight at $950, with Topps' own price $489.99; release week usually moves sealed prices one way or the other, and no 2026 single has sold yet to say which.",
   "Buying the base rookies as an investment. Last year's Sasaki base RC is a $4 card a year on; Anthony's 2026 Topps base is $40 in PSA 10 after 158 sales. The base and the unnumbered Refractor are set-filler; the money is in the numbered colours.",
   "Comparing the box to Topps Chrome. Cosmic Chrome is 80 cards and a hit in a minority of boxes; Chrome is 96 cards and an autograph a box for less. The reason to buy Cosmic is the parallel design holding value, not the hit rate.",
   "Treating Nick Kurtz #136 as a rookie card. It carries no RC mark in this set; his 2025 Topps Chrome Update USC178 is the RC the market prices (PSA 10 $103 on the Raw-to-Gem board)."
  ],
  "notes": [
   "Box contents (Checklist Insider, Cardsmiths Breaks): hobby 20 packs of 4, 8 boxes a case; Lunar box 20 packs of 4, 8 a case, Topps.com. Per-box averages from Cardsmiths Breaks are derived from Topps' published pack odds: about 62 base, 2 Refractors, 1 Nucleus, 0.5 White Hole, 0.8 Magenta /299, 0.5 Aqua /199, 0.4 Purple /150, 0.26 Blue /99, 0.2 Green /75, Gold /50 one a case, Orange /25 one in 15 boxes, Black /10 one in five cases, Red /5 one in nine cases, SuperFractor one in 47 cases. Lunar: about 41 base and 10 Lunar Eclipse /10 per box, autograph in three of four boxes.",
   "Autograph odds: Checklist Insider lists Cosmic Chrome Autographs 1:136 hobby packs, Extraterrestrial Talent 1:653, Launched Into Orbit 1:1,051, Stellar Stars 1:1,622, Star Clusters duals 1:15,535, Cosmic Explorers cuts 1:85,901; summed over 20 packs that is about 0.21 autographs a box. Cardsmiths Breaks states about one autograph in 2.7 hobby boxes. The two figures do not agree; both are quoted and the review treats the hit as absent from most boxes either way.",
   "Prices (eBay sold listings read Nov 2 in the browser pane, single boxes only, lots, cases and break slots excluded by title): 2026 hobby presale $900 median on 76 sales Oct 5 to 23, $699.99 to $999.99; $950 median on 8 sales Oct 27 to 31, $900 to $985.50. Topps presale $489.99 (Checklist Insider). 2025 Cosmic Chrome hobby box $1,150 median on 19 sales Oct 3 to Nov 1, $870 to $1,399.99. 2025 Cosmic Chrome Roki Sasaki: $3.99 median on 27 sales Oct 13 to Nov 1 of base and unnumbered insert cards together (graded, numbered and autograph cards excluded). No 2026 Cosmic Chrome Lunar box and no 2026 single had a completed sale.",
   "Checklist (Checklist Insider, Cardsmiths Breaks): base 200 with 77 RC-marked cards; the rookies named above plus Chase DeLauter #7, Otto Kemp #10, Justin Crawford #16, Noah Schultz #28, Owen Caissie #31, Colson Montgomery #33, JJ Wetherholt #40, Brandon Sproat #45, Nolan McLean #74, Bubba Chandler #100, Sal Stewart #180, Kyle Teel #200. Inserts 532 cards in 16 sets: Anti-Gravity 25, Constellation 25, Cosmic Dust 25, Extraterrestrial Talent 35, Launched Into Orbit 50, Mars Attacks MLB 10, Planetarium 25, Planetary Pursuit 100, StarFractor 100, Stars in the Night 25, Stella Nova 25, Stellar Stars 25, Supernova 25, Triple Star Clusters 7, Dual Star Clusters 8, Forces of the Diamond 22. Autographs 158 cards in six sets. New this year: Magenta Cosmos /299, Forces of the Diamond, Mars Attacks MLB, Cosmic Explorers cut signatures, Cosmic Dust (first MLB edition), Constellation variations.",
   "Dates: Nov 4 per Checklist Insider (estimated), Cardsmiths Breaks and DraftKings Network; Topps presale Oct 5 ($489.99), eBay presale listings promise shipping Nov 4 to 7.",
   "The scores are a first read. Rookie class is scored on Anthony, Griffin, McGonigle, Murakami and 73 other RCs, the deepest class in a Topps chrome product this year. Hit quality is scored on an autograph that most boxes do not contain. Print run is in the middle: none is published, Cosmic Chrome is hobby-only with a Topps.com Lunar box, and last year's boxes hold $1,150. Price vs. value uses $950 for 80 cards with about two numbered parallels and no guaranteed hit. Pending after the first week: eBay sold medians with counts for the hobby and Lunar boxes, the Anthony, Griffin, McGonigle and Murakami base and colour refractors, Planetary Pursuit by planet, and the autographs.",
   "Verdict for now: a box to buy for the parallels at the right price, not at $950. The rookie class and the design justify the product; the price does not justify the hit rate. Singles buyers should wait for the first week of sales and buy the numbered Anthony and Murakami colours; box buyers should compare the Lunar box once Topps prices it."
  ],
  "src": "Box prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 2, 2026 in the browser pane; counts and date ranges stated per line; lots, cases and break slots excluded by title. Topps presale price, pack odds, checklist, parallels, inserts, autograph sets, variations and what is new: Checklist Insider (2026 Topps Cosmic Chrome Baseball guide), read Nov 2. Per-box and per-case averages, Lunar box contents, insert and autograph set totals: Cardsmiths Breaks (full checklist), read Nov 2. Release date: Checklist Insider, Cardsmiths Breaks, DraftKings Network. Rookie comps: the Raw-to-Gem board on this site (PSA Auction Prices Realized, Oct 11 to Nov 1). No 2026 single and no Lunar box had a completed sale when this was written."
 }
}

MARK = '/* cosmic-chrome-2026 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', lambda m: entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
open(P, 'w').write(s)
print('ok', len(s))
