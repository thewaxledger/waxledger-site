"""Add the 2026 Topps Allen & Ginter Baseball deep review to the master page (idempotent)."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Topps Allen & Ginter Baseball", "when": "Out now · Oct 10", "score": "5.6",
 "facts": [
  "Hobby: 24 packs of 8 with two hits. $139.99 at release, $201 median on eBay (24 boxes sold Oct 7 to 10, most at $199.99)",
  "300-card base set, the smallest A&G base set so far, with no short prints for the first time since 2015 (Baseballcardpedia)",
  "About 149,200 copies of each base card by Baseballcardpedia's estimate",
  "Rip Cards: 200 subjects numbered /199, 1 in 81 hobby packs, so about one every 3.4 boxes. Unripped median $175 (23 sold Oct 9 to 10)",
  "Framed mini autographs fall 1 in 67 packs (baseball) and 1 in 150 (non-baseball). Most boxes have at least one plain relic among the two hits"
 ],
 "bars": [["Rookie class", 8.5], ["Hit quality", 5.5], ["Print run", 3.5], ["Price vs. value", 5.0]],
 "deep": {
  "lede": "Four days of eBay sold listings, Oct 7 to 10, pulled for the box, the Rip Cards and the two rookies with the most volume (Konnor Griffin and Munetaka Murakami). eBay cut off our pull before we reached the framed mini autographs, so autograph prices beyond two single sales are pending and will be added on the next refresh. What the data already shows: the rookie class is the best A&G has had in years and the base cards are $3 anyway, because roughly 149,000 of each were printed. The money in this product is in the Rip Cards and the numbered parallels.",
  "sections": [
   {"h": "Tier 1 · Rip Cards, the one hit that pays for a box", "items": [
    {"c": "Rip Cards /199 · 200 subjects, unripped", "p": "Median $175 (23 sold Oct 9 to 10, $90 to $365). Ohtani $365 · Griffey Jr. $350 (2) · Sal Stewart $295 · Kurtz $200 · Caglianone $200 · Willie Mays $140 · Jeremy Peña $90. Konnor Griffin $500 (1, Oct 8)",
     "w": "One in 81 hobby packs, about one every 3.4 boxes, and the only common hit that clears the price of the box on its own. Each holds a mini exclusive or a red-ink mini autograph. The market is paying more for the sealed card than for what is usually inside: ripped Rip Cards sold for a $20 median (13 sales) and most of the exclusive minis we saw were $12 to $40 (Skenes $30, Elly De La Cruz $35, Roman Anthony $20 to $40). Unless you want the gamble, sell it unripped."},
    {"c": "Double Rip Cards /50 · 100 pairings, hobby only", "p": "Median $350 (11 sold Oct 7 to 10, $199 to $500). Griffey Jr. $500 · Harper/Schwarber $400 · Yamamoto/Sasaki $321 · Murakami/Montgomery $225",
     "w": "One in 1,212 packs, about one every 50 boxes. Two minis inside. Same rule as the singles: the unripped card is the asset."}
   ]},
   {"h": "Tier 2 · Rookie parallels with real prices", "items": [
    {"c": "Munetaka Murakami #5 RC", "p": "Base $2.99 (52 sold) · Black Border mini $15 (14) · Chrome $20 (15) · Blue Foil Filigree /150 $75 and $80 · Green /99 $70 · Mini Brooklyn Back /25 $150 · Purple Chrome Refractor /75 $200 · Gold Foil Filigree /50 $250 (1 sale each unless counted)",
     "w": "Thirty home runs as a rookie (Yahoo Sports, Sep 24) and the strongest parallel prices in the set: his numbered cards are selling at two to three times Griffin's. A framed mini autograph redemption sold for $250 on Oct 8. The Black Border mini at $15 with 14 sales is the liquid card under $20."},
    {"c": "Konnor Griffin #103 RC", "p": "Base $2.99 (50 sold) · Mini Chrome $12 (15) · Black Border mini $18 (7) · Chrome Refractor $20 (6) · Chrome Blue Refractor /150 $50 (1) · Chrome Purple Refractor /75 $70 (1) · Framed mini autograph Blue /50 $999 (1, Oct 8)",
     "w": "The most traded rookie in the product by listing count, and the base card is still $3. His N43 ($4, 24 sold), N34 mini ($7, 15) and Rookie Design Variation mini ($6, 17) are all cheaper than a coffee. The one sale that matters is the framed mini autograph at $999; treat it as a single data point until more sell."},
    {"c": "Kevin McGonigle #206 RC, Roman Anthony #200 RC", "p": "Base: McGonigle $2.49 (57 sold, Oct 5 to 10) · Anthony $2.30 (4, Oct 9 to 10)",
     "w": "McGonigle was the presumptive AL Rookie of the Year favorite in late September, with Parker Messick closing (Yahoo Sports, Sep 24). Anthony re-injured his right hand in the Wild Card Series and the Red Sox expect rest, not surgery (MLB.com). Neither has parallel volume yet."}
   ]},
   {"h": "Tier 3 · Everything else in the box", "items": [
    {"c": "The other rookies: Misiorowski #163, Wetherholt #183, Bazzana #159, Eldridge #73, Basallo #146, Chandler #170, McLean #123, Tong #165", "p": "Prices pending. Expect base cards at or under the $2 to $3 that Griffin and Murakami bring",
     "w": "A deep class on paper. At this print run the base rookies are binder cards; the parallels numbered /150 and lower are the only versions with a price."},
    {"c": "Relics", "p": "Prices pending",
     "w": "Design A relics are 1 in 37 packs (about 1,300 copies each by Baseballcardpedia's estimate), Design B 1 in 70, framed mini relics 1 in 70. Together that is about 1.3 of the 2.2 hits an average box produces from the published odds."},
    {"c": "Inserts: Wicked Power, N43, N34, 50 Ways to Say Hello", "p": "Griffin N43 $4 (24) · Griffin N34 mini $7 (15) · Murakami N43 $3 (30) · Murakami N34 $10 (26)",
     "w": "Wicked Power and N43 are estimated at more than 90,000 copies per card. Collect them if you like the set; they are not value."}
   ]}
  ],
  "avoid": [
   "Paying $200 for a hobby box that was $139.99 at release. From the published odds a box averages about 0.3 Rip Cards, 0.5 framed mini autographs and 1.3 plain relics. About three boxes in four have no Rip Card.",
   "Ripping a Rip Card for value. Unripped $175 median, ripped $20, and most exclusive minis sold for $12 to $40.",
   "Grading base rookies. About 149,000 copies of each and a $3 raw price; no PSA 10 premium survives that supply.",
   "Paying up for Chrome and Mini Chrome as if they were scarce. Baseballcardpedia estimates 2,500 Chrome and 3,800 Mini Chrome copies per card; Griffin's sell for $7 to $12.",
   "Reading the two autograph sales above as a market. One Griffin /50 at $999 and one Murakami redemption at $250 are all we have."
  ],
  "notes": [
   "Hits per average hobby box from the published hobby odds (24 packs): framed mini autograph 0.36 baseball plus 0.16 non-baseball, Design A relic 0.65, Design B relic 0.34, framed mini relic 0.34, Rip Card 0.30, autographed relic 0.03. That adds to about 2.2, in line with the two hits Topps states.",
   "Parallel ladder (hobby odds): Silver Portrait 1 in 5, Foil Filigree 1 in 24, Blue /150, Green /99, Gold /50, Orange /25, Black /10, Red /5, Purple 1/1. Minis: A&G back 1 in 5, Black Border 1 in 10, No Number /50, Brooklyn Back /25, Stained Glass 25 copies, Metal /3, Wood 1/1.",
   "Chrome is back as a parallel: Chrome 1 in 13 packs, Refractor 1 in 24, X-Fractor 1 in 288, then numbered Blue through Red and a SuperFractor.",
   "Print estimates here are Baseballcardpedia's, worked back from pack odds. Topps does not publish a print run.",
   "Pending on the next refresh: framed mini autograph prices by signer, relic prices, and base prices for the rest of the rookie class.",
   "Verdict: a strong checklist in a heavily printed product. At $140 it was a fair rip for set builders; at $200 it is a pass unless you are chasing Rip Cards. Singles to target: Murakami Black Border mini near $15, Murakami and Griffin parallels numbered /150 and lower, unripped Rip Cards of rookies under the $175 median."
  ],
  "src": "Prices: eBay sold listings, Oct 7 to 10 (McGonigle from Oct 5), medians with counts; single sales are marked. eBay stopped serving our pull on Oct 10 before autographs and relics were read, so those are pending. Checklist, odds and print estimates: Baseballcardpedia. Player context: Yahoo Sports (Sep 24), MLB.com."
 }
}

MARK = '/* allen-ginter-2026 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', lambda m: entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
open(P, 'w').write(s)
print('ok', len(s))
