"""Add the 2026 Panini Donruss Football deep review to the master page (idempotent).
Written Oct 30, two days after the hobby release (Oct 28; blasters and Winter Tins Oct 23), as a structural review
with no sold data. Prices filled in Nov 2 from eBay sold listings (LH_Sold=1&LH_Complete=1) read in the browser pane:
hobby box, Downtowns, Rated Prospects, autographs."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Panini Donruss Football", "when": "Out now · prices Nov 1", "score": "3.9",
 "facts": [
  "Hobby: 12 packs of 10 (120 cards) with one autograph and one memorabilia card, about 12 base parallels, 6 Optic cards and 36 inserts per box, 12 boxes a case. Six fewer packs than last year's 18. $199.95 list per Checklist Insider. eBay sold: $220 median on 32 single boxes Oct 28 to Nov 1 ($190 to $270)",
  "First Donruss Football without the NFL license: no team logos, nicknames or helmet marks (Fanatics holds the exclusive NFL card rights from April 2026). Panini keeps NFLPA rights, so veterans appear by name in airbrushed or college photography",
  "The Rated Rookie line is gone and the 2026 NFL rookies are not in the set: Fernando Mendoza, Jeremiyah Love, Carnell Tate, Jordyn Tyson and Carson Beck appear nowhere on the Checklist Insider or Cardsmiths Breaks checklists. Rated Prospect cards of college players replace them: CJ Carr #3, Dylan Raiola #11, Julian Sayin #13, LaNorris Sellers #119, Dante Moore #132, Darian Mensah #167, Bryce Underwood #191, Jayden Maiava #197",
  "Base set cut from 400 to 199 cards (#1 to #200, no #117), plus a 199-card Optic chromium version. Downtown (34 cards) mixes college quarterbacks (Carr, Sayin, Underwood, Moore, Mensah, Keelon Russell) with retired stars (Favre, Elway, Moss, Emmitt Smith, Warner); Downtown Duos 14. No Downtown odds published",
  "Autographs: 186 base autographs and 189 Optic autographs, plus Campus Kings (28), Jersey Kings (35) and Leather Kings (32) relic autographs /250 or less, Dominators (22) and Gridiron Kings (25) /99 or less. Panini has not published pack odds or a print run"
 ],
 "bars": [["Rookie class", 2.5], ["Hit quality", 4.5], ["Print run", 3.0], ["Price vs. value", 4.5]],
 "deep": {
  "lede": "Written Oct 30, two days after the hobby release (Oct 28); prices refreshed Nov 2 from eBay sold listings through Nov 1. The hobby box sells for $220 (32 sales), the Downtowns for $500 median (35 sales) with Keelon Russell at $900 to $1,012 and the retired-star duals at $550 to $800, and the autographs for $30 median (76 sales). The Rated Prospect base cards are $1 to $2. The Downtown market has held without the logos; the rest of the box has not. This is the first Donruss Football without the NFL license, and Panini has answered it by changing what the product is: the base set is half the size (199 cards), the Rated Rookie line is gone, and the 2026 NFL rookie class is not here at all. Mendoza, Love, Tate and Tyson have their rookie cards in Topps products this year (Heritage, Chrome, Flagship, Bowman). What Donruss sells instead is college quarterbacks as Rated Prospects, retired stars in Downtowns and autographs, and current veterans with the logos airbrushed off. A hobby box is 120 cards for about $200 with one autograph and one relic.",
  "sections": [
   {"h": "Tier 1 · The cards worth opening a hobby box for", "items": [
    {"c": "Downtown · 34 cards: CJ Carr, Julian Sayin, Bryce Underwood, Dante Moore, Darian Mensah, Keelon Russell, Jayden Maiava, John Mateer; Favre, Elway, Moss, Emmitt Smith, Warner, Faulk, Irvin, Kelly, Moon, Donald, Urlacher", "p": "$500 median on 35 eBay sales Oct 26 to Nov 1 ($198 to $1,400, singles and duals together). Keelon Russell $900, $1,000 and $1,012 (3 sales Oct 30 to 31); Ed Reed $432 and $900; Elway $500 (2); Emmitt Smith $450; Strahan $500; Warner $275. Gold /10 and Black 1/1 parallels per Cardlines; no odds published",
     "w": "The case hit, and the part of a Donruss box least tied to the logo: Downtown is bought for the art, and the first week says so. $500 median across 35 sales is in line with a licensed year. The retired-star list does most of the work (Elway, Reed, Smith, Strahan at $430 to $900); the college quarterbacks are a bet on the 2027 draft, and Russell is the one the market has already picked at $900 to $1,012."},
    {"c": "Downtown Duos · 14 cards: Sayin / Bo Jackson, Carr / Nolan James Jr., Emmitt Smith / Aikman, Elway / Peyton Manning, Montana / Steve Young, Fitzgerald / Warner, Calvin Johnson / Barry Sanders, Ham / Joe Greene, Deion Sanders / Moss", "p": "Elway / Manning $800, Aikman / Smith $750, Deion Sanders duo $580, Warner / Fitzgerald $550, Ham / Greene $475 (one sale each, Oct 30 to 31)",
     "w": "Second year of the Duos. The legend pairings are the chase; the two college pairings (Sayin with Bo Jackson, Carr with James) are the unusual ones and the ones breakers will film."},
    {"c": "Rated Prospect base and Optic parallels · Carr #3, Raiola #11, Sayin #13, Sellers #119, Moore #132, Mensah #167, Underwood #191, Lonergan #196, Maiava #197, Inniss #200", "p": "Underwood base $0.99 to $1.75 (3 sales Oct 26 to 29), Holo $1.99 (1), Pink Foil $6.99 and $12.99 (2), Optic base $60 (1 sale Oct 30; another at $0.99). Sellers base $3.99, Stockton $2.50 (1 each). Base ladder: Blue Cubic /499 down to Cloud /25, Gold /10, Black 1/1. Optic: Purple Scope /499 to Gold /10, Black Gold /8, Gold Vinyl and Nebula 1/1",
     "w": "These are the cards in the Rated Rookie slot this year, and they are college cards of players who will have an actual rookie card from Topps in 2027. The numbered Optic colours of Underwood, Sayin and Carr are the ones with a market; the rest is set-filler until a draft position says otherwise."},
    {"c": "Relic autographs · Campus Kings (28, /250 or less), Jersey Kings (35), Leather Kings (32); Dominators (22) and Gridiron Kings (25) autographs /99 or less", "p": "All 2026 Donruss autographs: $30 median on 76 eBay sales Oct 23 to Nov 1 ($1 to $1,000). Leather Kings Sam Leavitt /250 $65, Jersey Kings Merton Hanks /250 $29, Gridiron Kings Howie Long /99 $52, Elway base autograph /15 $100 (one sale each)",
     "w": "One autograph a box, so one of these or a base autograph. Campus Kings is the college signing set (NIL deals) and the one that may carry a rookie-class premium; Dominators and Signature Marks are retired players. Expect sticker autographs on most."}
   ]},
   {"h": "Tier 2 · Mid-range: the inserts and the numbered middle", "items": [
    {"c": "Inserts · Elite (49), Campus Kings (29), Elite Series (25), Gridiron Kings (25), Gridiron Prospects (25), Dominators (25), Throwback (25), Elite Deck (24), On the Horizon (19), Uptown (30), Passing the Torch (28 singles, 14 duals)", "p": "Prices pending",
     "w": "36 inserts a box out of 120 cards, so three in ten cards is an insert. At that density the unnumbered inserts are $1 to $3 cards in any year; Uptown is the usual exception and the Holiday Uptown (2 cards) the odd one."},
    {"c": "Base autographs (186) and Optic autographs (189) · /99 or less, Holo /75, Gold /10, Black 1/1", "p": "Within the $30 median above: Rozier /99 $40, McMahon $30, Kosar /75 $20, Zach Thomas /99 $18.50, Rypien Red /49 $18, Jaworski Red /49 $10, Kewan Lacy Rated Prospect /75 $35, Leavitt $20 (one sale each, Nov 1)",
     "w": "The modal autograph in a box. Checklist runs to 186 names, most of them veterans and college players in the second tier; without the logo the veteran autographs lose the piece buyers paid for."},
    {"c": "Numbered base parallels · Blue Cubic /499, Pink /399, Holo Laser, Purple Cubic and Red Cubic /199, Red Explosion and Stars /149, Hyper /125, Crystals, Explosion, Orange Lava and Purple Crystals /99, Plaid /75, Cosmic /65, Jazz and Purple Explosion /49, Blue Explosion /35, Scope /32, Cloud /25, Gold /10, Black 1/1", "p": "Prices pending",
     "w": "Twelve parallels a box, most of them the unnumbered Holo, Diamond, Fireworks, Cosmos and Yellow. The numbered ones are worth something on a Rated Prospect quarterback and little on a veteran."}
   ]},
   {"h": "Tier 3 · Everything else in the box", "items": [
    {"c": "Base cards · 199 veterans and Rated Prospects, no #117", "p": "Prices pending",
     "w": "About 60 of the 120 cards in a box. Veterans photographed in airbrushed uniforms or college gear; the first Donruss base set where no card shows a team."},
    {"c": "Optic base and Holo parallels · 199 cards", "p": "Prices pending",
     "w": "Six Optic cards a box. The Holo is the Optic version of a Silver and the one Optic card with a resale market in a normal year; this year it is a logo-less Holo."},
    {"c": "Relics · Leather Kings (34), Phenom Jerseys (29), Donruss Threads (29), Jersey Kings (35), Holiday Memorabilia (40)", "p": "Prices pending",
     "w": "The guaranteed second hit. Unlicensed relics are player-worn material without a team mark, which is the piece of the box the licence change hits hardest."}
   ]}
  ],
  "avoid": [
   "Buying a Donruss box for the 2026 NFL rookie class. Mendoza, Love, Tate, Tyson and Beck are not in it. Their rookie cards are in Topps Heritage Football (out Oct 21), Topps Chrome Football (Nov 18), Topps Flagship and Bowman Football.",
   "Paying more than the sold price. The hobby box sells for $220 median on 32 eBay sales (Oct 28 to Nov 1), about half of 2025 Donruss Football, and the box is 120 cards instead of 180. Shops asking $262 are above both the sold price and the $199.95 list for a product with no NFL rookies.",
   "Buying the box for the Rated Prospects. Underwood, the most-hyped of them, is a $1 to $2 base card and a $2 Holo after the first week; only the Optic ($60, one sale) and the numbered colours have a market.",
   "Treating the college Rated Prospects as rookie cards. They are pre-draft cards; the players' rookie cards will come from Topps after the 2027 draft, and that is what the hobby prices as the rookie card.",
   "Assuming every Downtown is a $500 card. The median is $500 across 35 sales, but the range is $198 to $1,400: Russell, Reed, Elway and the legend duals carry it; a mid-list veteran Downtown is a $200 to $300 card."
  ],
  "notes": [
   "Box contents (Checklist Insider, Cardsmiths Breaks, Beckett): hobby 12 packs of 10, one autograph and one memorabilia card, about 12 base parallels, 6 Optic base or parallels and 36 inserts per box, 12 boxes a case. Mega: 6 packs of 12, one relic, six inserts, a numbered parallel in about one of two boxes. Blaster: 6 packs of 10 with six exclusive parallels, six Optic Holos, six inserts, a relic in about one of two. Winter Tin: 3 packs of 5 with Candy Cane Stripe, Candy Cane Optic, Sled or Yellow Lava parallels and holiday memorabilia in one of three.",
   "Dates: hobby Oct 28, blaster and Winter Tin Oct 23 per Checklist Insider; the Beckett preview had the release as TBA and an earlier Checklist Insider date was Sep 30. Mega date not listed.",
   "Prices (eBay sold listings read Nov 2 in the browser pane, lots, cases and break slots excluded by title): hobby box $219.99 median on 32 sales Oct 28 to Nov 1, $190 to $269.95; two presale sales Oct 17 at $219.99 and $395.98 (a 2-box lot). Downtown $499.99 median on 35 sales Oct 26 to Nov 1 (singles and duals, no graded or numbered parallels), $197.50 to $1,400. Autographs $29.99 median on 76 sales Oct 23 to Nov 1, $1 to $1,000 (search '2026 Donruss Football auto' excluding Optic, Elite and break listings). Rated Prospect and base-card sales as stated per line. $199.95 list per Checklist Insider; Cardlines' pre-release estimate was $205 to $225.",
   "Licensing: Panini's NFL licence ended Mar 31, 2026 after the NFL gave Fanatics exclusive card rights in April 2026 (Beckett, The Card Shop Finder). Panini keeps NFLPA rights, so player names and likenesses are used; helmets are airbrushed and college photography is used where possible. The Card Shop Finder reports that Prizm, Select and National Treasures Football end in their current form.",
   "Checklist: base 199 cards (#1 to #200, no #117), down from 400; Optic 199. Rated Prospects (college): Carr #3, Raiola #11, Sayin #13, Sellers #119, Moore #132, Mensah #167, Underwood #191, Lonergan #196, Maiava #197, Inniss #200. None of Mendoza, Love, Tate, Tyson, Beck, Lemon, Reese, Sadiq, Simpson or Nussmeier appears in the base, Optic, Downtown, autograph or relic lists shown by Checklist Insider or Cardsmiths Breaks (the Passing the Torch autograph list is cut off on both pages). Inserts 368 cards: Downtown 34, Downtown Duos 14, Elite 49, Campus Kings 29, Elite Series 25, Gridiron Kings 25, Gridiron Prospects 25, Dominators 25, Throwback 25, Elite Deck 24, On the Horizon 19, Uptown 30, Uptown Holiday 2, Passing the Torch 28 and 14. Relics 167. Autographs 617 per Cardsmiths Breaks' total.",
   "The scores are a first read. Rookie class is scored on who is in the set: no NFL rookies, college prospects in their place. Hit quality is one autograph and one relic, most of them unlicensed stickers. Print run is in the middle because none is published and the product sells at mass retail. Price vs. value uses the $220 sold price and 120 cards. Still pending: Sayin and Carr Rated Prospect singles (no completed sale found by Nov 1), base and Optic base medians, relic medians.",
   "Verdict: pass as an investment, rip for fun if you like the art. At $220 for 120 cards, one autograph ($30 median) and one relic, with no NFL rookies and no logos, the box is a Downtown lottery: the Downtowns have held at $500 median without the logos, but they are case hits with no published odds, and nothing else in the box pays. The rookie money this year is in Topps Chrome Football on Nov 18."
  ],
  "src": "Prices: eBay sold listings (LH_Sold=1&LH_Complete=1) read Nov 2, 2026 in the browser pane; counts and date ranges stated per line; lots, cases and break slots excluded by title. Configuration, dates, list price, checklist, parallels, inserts, autograph and relic sets: Checklist Insider (2026 Donruss Football guide) and Cardsmiths Breaks (full checklist), read Oct 30, 2026. Licensing and the eighteen-to-twelve pack change: Beckett (2026 Donruss Football details), The Card Shop Finder. Price estimate and Downtown parallels: Cardlines via The Ballers Bank. Shop asks: eBay Buy It Now listings quoted by Checklist Insider and Cardsmiths Breaks on Oct 29, and a $262.44 shop listing via The Ballers Bank."
 }
}

MARK = '/* donruss-fb-2026 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', lambda m: entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
open(P, 'w').write(s)
print('ok', len(s))
