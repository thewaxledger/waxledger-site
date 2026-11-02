"""Add the 2026-27 Upper Deck Series 1 Hockey deep review to the master page (idempotent)."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026-27 Upper Deck Series 1 Hockey", "when": "Out now · boxes and top Young Guns Nov 1", "score": "5.9",
 "facts": [
  "Hobby: 12 packs of 12, about six Young Guns per box. $150 median on eBay at release (12 boxes sold Oct 7 to 10); $138 three weeks on (13 boxes sold Oct 28 to Nov 1, $100 to $181)",
  "250 cards: 200 veterans and 50 Young Guns (#201 to #250, the last one a Frondell/Martone checklist)",
  "No guaranteed autograph or memorabilia card. The only autographs are Snow Spray variations at about 1 in 5,570 packs",
  "Young Guns parallels: Outburst Silver 1 in 60 hobby packs, Clear Cut 1 in 144, Deluxe /250, Exclusives /100, Outburst Red /25, High Gloss /10",
  "Martone base $50 median (82 sales Oct 27 to Nov 1) and Hagens $56 (77 sales Oct 29 to Nov 1), down from $95 and $70 in release week"
 ],
 "bars": [["Rookie class", 6.5], ["Hit quality", 5.0], ["Print run", 5.0], ["Price vs. value", 6.0]],
 "deep": {
  "lede": "Three days of sales, all from eBay sold listings between Oct 7 and Oct 10 unless a line says otherwise. Base Young Guns already have real volume (23 to 89 sales each for the names below), so those medians are usable. Parallels are thin, one to eight sales each, and are shown as individual prices. The shape of the product is simple: three top-seven picks from the 2025 draft carry it, a second group of four or five names is worth sleeving, and the other 36 Young Guns are $3 cards. Release-week prices on Young Guns almost always fall as retail arrives, and blasters and tins land Oct 21.",
  "sections": [
   {"h": "Tier 1 · The three Young Guns that carry the box", "items": [
    {"c": "Porter Martone · Young Guns #209, Flyers", "p": "Base $95 (89 sold) · Canvas Young Guns $109 (25, Oct 9 to 10) · Outburst Silver $378 to $500 (4) · Deluxe /250 $386 (1)",
     "w": "The most expensive base Young Gun in the set and the most traded. Sixth pick in 2025. The Canvas at $109 is only $14 over the base while falling at 1 in 24 packs across every Canvas rookie, which makes it the better card at the price. The base at $95 on day three is the number most likely to come down once retail opens: sell extras now, buy the one you want in November."},
    {"c": "James Hagens · Young Guns #206, Bruins", "p": "Base $70 (83 sold, $35 to $126) · Canvas Young Guns $57 (18) · Outburst Silver $207 to $300 (5, Oct 9) · Exclusives /100 $496 (1, Oct 8)",
     "w": "Seventh pick in 2025 and a Boston market behind him. The spread on the base is wide, $35 to $126 in the same four days, which says buyers have not agreed on him yet. The Canvas trading under the base is unusual and is the buy of the two."},
    {"c": "Anton Frondell · Young Guns #201, Blackhawks", "p": "Base $63 (78 sold) · Outburst Silver $265 (8, $225 to $300) · Clear Cut $386 (1, Oct 9) · Exclusives /100 $701 (1, Oct 8)",
     "w": "Third overall in 2025 and card #201, the first Young Gun in the set, which hockey collectors pay for. His Outburst Silver has the cleanest parallel market in the product: eight sales in a $75 range. We found no sold Canvas Young Guns of his this week. Cheapest of the three as a base card and the highest draft pick, so it is the one with room if he sticks in Chicago."}
   ]},
   {"h": "Tier 2 · Worth sleeving", "items": [
    {"c": "Cole Hutson · Young Guns #223, Capitals", "p": "Base $41 (55 sold, $30 to $80) · Canvas Young Guns $50 (11) · Outburst Silver $140 to $249 (4) · Deluxe /250 $250 (1)",
     "w": "Lane Hutson's brother, with 10 points in 14 NHL games late last season (Cardlines). The only name outside the top three with a base card over $30, and the tightest floor of the group: nothing sold under $30."},
    {"c": "Konsta Helenius · Young Guns #210, Sabres", "p": "Base $28 (48 sold)",
     "w": "63 points in 63 AHL games before his NHL look (Cardlines). Priced as the fifth name in the set, which is about right."},
    {"c": "Victor Eklund #220, Ilya Protas #218, David Reinbacher #222, Carter Yakemchuk #249", "p": "Base: Eklund $20 (52) · Protas $18 (38) · Reinbacher $15 (41) · Yakemchuk $14 (31). Clear Cut: Reinbacher $150, Protas $119, Yakemchuk $50 (1 sale each)",
     "w": "The $14 to $20 group. Protas was the AHL rookie of the year with 66 points in 69 games (Cardlines) and is the cheapest production in the set. Reinbacher, a fifth overall pick in 2023, has the widest gap between base and Clear Cut, a sign that Montreal collectors are buying the scarce version and ignoring the base."}
   ]},
   {"h": "Tier 3 · The other 40 Young Guns", "items": [
    {"c": "Brayden Yager #242, Sacha Boisvert #243, Alex Bump #207, Oliver Bonk #240", "p": "Base: Yager $10 (23) · Boisvert $9 (27) · Bump $7 (30) · Bonk $6 (30). Deluxe /250: Boisvert $100, Bonk $80, Yager $40, Bump $15 (1 sale each)",
     "w": "First-round picks trading as $6 to $10 base cards. Fine to hold a few raw; none of them covers a grading fee."},
    {"c": "The long tail: 36 names", "p": "$2.75 to $4 medians on the five we sampled (Lindstein, Hameenaho, Sykora, Hinds, Uchacz; 84 sales). Checklist #250 $6 (29)",
     "w": "This is four or five of the six Young Guns in a typical box. Their Clear Cut and Deluxe parallels are $10 to $40 cards, with a few team-collector exceptions (Lindstein Clear Cut $105)."}
   ]}
  ],
  "avoid": [
   "Buying hobby boxes at $150 for value. Adding the 13 Young Guns we priced, the checklist and 36 commons at $3.25 gives about $10.40 per Young Gun, so six a box is about $62 before fees. The box is a ripping product, not a sealed-value one, unless you hit an Outburst Silver or Clear Cut of the top three.",
   "Paying release-week prices for base Young Guns of the top three. Retail formats arrive Oct 21 and add supply of exactly these cards.",
   "Grading base Young Guns of anyone outside the top three. Our Raw-to-Gem data on the 2024-25 Young Guns shows PSA 10 rates of 23% (Lane Hutson, 7,632 graded) and 29% (Michkov, 5,087 graded); at those rates a $40 raw card needs a PSA 10 of roughly $400 or more to break even.",
   "Insert sets as value. Fan Faves, Repping, Vibe Check, Debut Dates, Here We Go!, Sizzle Reel and UD Portraits fall every four to eight packs. Frondell's sold for $3 to $15 this week.",
   "Treating the two published odds sheets as settled. Checklist Insider lists base Outburst Silver at 1 in 30 hobby packs and Hockey Checklists at 1 in 15; the Young Guns odds (1 in 60 and 1 in 144) agree on both."
  ],
  "notes": [
   "Refreshed Nov 2 (eBay sold listings read in the browser pane, lots, cases and breaks excluded): hobby box $137.99 median on 13 sales Oct 28 to Nov 1 ($99.99 to $180.78), down from $150 at release. Porter Martone Young Guns base $49.96 median on 82 sales Oct 27 to Nov 1 ($0.99 to $67.89), down from $95; James Hagens base $55.99 median on 77 sales Oct 29 to Nov 1 ($4.25 to $99.99), down from $70. Hagens now sells above Martone. The other single-card lines below keep their Oct 7 to 10 reads.",
   "What a case looks like, from the published odds: 144 packs, about 72 Young Guns, six Canvas Young Guns, two or three Young Guns Outburst Silver and one Young Guns Clear Cut. With 50 subjects, a case does not guarantee one of each base Young Gun.",
   "Not in this set: anyone from the 2026 draft. Gavin McKenna appears only on an NHL Draft insert (SP-1). The 2026 class waits for later products (Cardlines).",
   "Short prints: Holotypes 1 in 1,008 packs; Electric Soul, Youthful Spirits and Bootleg 1 in 2,880; Fanimation 1 in 4,850. None had enough sales this week to price.",
   "Stencils fall 1 in 3 packs with Red /999, Yellow /299, Green /199, Blue /99 and Purple /25. The 100-card set continues in Series 2.",
   "Upper Deck does not publish a print run and we have not found a reliable estimate, so the Print run score reflects a flagship product sold in five formats, not a measured number.",
   "Verdict: a normal Series 1. Rip a box for $150 if you like opening Young Guns; do not buy it expecting the cards to cover it. Singles to target: Frondell base under $60, Martone and Hagens Canvas over their base cards, Cole Hutson base near $35, Protas base under $20. Recheck all of it after Oct 21."
  ],
  "src": "Prices: eBay sold listings, Oct 7 to 10 (Yager, Boisvert, Bonk, Lindstein and Hameenaho include sales from Oct 1 to 6), medians with counts; single sales are marked. Checklist and odds: Checklist Insider, Hockey Checklists. Player context: Cardlines. Gem rates: PSA pop report, Oct 10."
 }
}

MARK = '/* ud-series-1-hockey-2026 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', lambda m: entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
open(P, 'w').write(s)
print('ok', len(s))
