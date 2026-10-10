"""Add the 2026 Bowman Chrome Sapphire Baseball deep review to the master page (idempotent)."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Bowman Chrome Sapphire Baseball", "when": "Out now · Oct 10", "score": "7.3",
 "facts": [
  "$599.99 through an EQL draw on Oct 7, sold out. Resale $1,186 to $1,456 on eBay (3 boxes sold Oct 8 to 9)",
  "8 packs of 4. One autograph and three numbered parallels per box; every parallel is Yellow /75 or better",
  "12,638 boxes, up 20.5% on 2025 Chrome Sapphire (SlabSquatch). Base Sapphire runs about 3,475 copies per card",
  "The 34-name prospect autograph list is the 2026 international class. Griffin, Holliday, De Vries, Made and the rookies do not sign it",
  "Image Variations about 1 per 3 boxes; Hidden Gems about 1 per 40 to 50 boxes"
 ],
 "bars": [["Rookie class", 8.0], ["Hit quality", 6.0], ["Print run", 6.5], ["Price vs. value", 7.0]],
 "deep": {
  "lede": "Three days old, so the singles market is thin and most of what has sold is break spots. This review uses three price sources and labels each: confirmed Chrome Sapphire sales (Oct 7 to 10), the June 2026 Bowman Sapphire comps for the same players on the same color ladder, which is the best guide to where these settle, and 2026 Bowman Chrome autograph comps for the 34 signers. The structural story matters more than any single price: the base and prospect checklist is the strongest Sapphire has had in years, and almost none of those names sign.",
  "sections": [
   {"h": "Tier 1 · The cards that carry the product", "items": [
    {"c": "Konnor Griffin · base #1 RC, Image Variation, Hidden Gems HG-19, Sapphire Selections auto", "p": "Chrome Sapphire: Yellow /75 $130 (1). June Sapphire comps: base $11 (37) · Yellow /75 $75 (4) · Gold /50 $83 (2) · Orange /25 $123 to $250 · Red /5 $718 · auto /50 $555",
     "w": "Called up April 3 at 19, signed for nine years and $140 million the same week, and his 2024 Bowman Chrome colors sold for $9,500 to $22,435 during his debut. He is in every chase lane of this product. The Sapphire Selections autograph is his only signature in the set: about 60 unnumbered copies plus Orange /25, Red /5 and a 1/1, at roughly one Selections auto per 14 boxes across 11 names. Expect it to open above $800. The base RC at $10 to $15 and the Yellow /75 around $100 are the sane buys; the Hidden Gem and Image Variation are the trophies."},
    {"c": "Shohei Ohtani · base #100", "p": "Chrome Sapphire: $180 and $200 (3 sales, Oct 9)",
     "w": "The most liquid card on day one and the only veteran that matters here. About 3,475 copies, no autograph in the set. Colors will trade at multiples: the Gold /50 and Orange /25 are the ones to pull. Under $180 for the base is a reasonable entry while boxes are still landing."},
    {"c": "Kevin McGonigle Image Variation Gold /50", "p": "Chrome Sapphire: $1,250 (1, Oct 9). June Sapphire comps: Gold /50 $190 (6) · auto /199 $244 (5)",
     "w": "The Image Variation market opened hot: one McGonigle Gold at $1,250 against a $190 Gold parallel of the same player in June. The 20-card variation set (about one per three boxes, Gold /50, Orange /25, Red /5, 1/1) covers Griffin, McGonigle, Roman Anthony, Murakami, Misiorowski, Wetherholt, Holliday, De Vries, Max Clark, Asigen, Luis Hernandez, Walker Jenkins, Seth Hernandez and Cooper Pratt. These are the best per-pull cards in the box. A Freeland Orange /25 sold at $150, so the premium is for the names, not the set."},
    {"c": "Hidden Gems · Murakami, Cal Raleigh, Colson Montgomery, Griffin, JJ Wetherholt", "p": "No Chrome Sapphire sales yet. June Sapphire comps: Holliday Emerald $309 raw, $162 to $497 graded · Roman Anthony Emerald $305 graded",
     "w": "Five cards, roughly 50 Emerald copies each, plus Onyx /10, Ruby /5 and a 1/1, at about one per 40 to 50 boxes. The Griffin and Murakami Emeralds should open at $400 to $800 on the June comps. If you pull one, sell within the first two weeks; Hidden Gems hold better than most inserts but they still fade once the cases are open."},
    {"c": "Munetaka Murakami · base #76 RC, Hidden Gems HG-16, Image Variation", "p": "No confirmed Chrome Sapphire sales yet",
     "w": "The NPB slugger in his MLB rookie year, with the Japanese collector base that already prices Ohtani, Imai and Okamoto above their stat lines. No autograph here (he signs eight sets in base Bowman Chrome, none in Sapphire), so the base RC and the Hidden Gem are the cards. The base should be a top-five rookie card in the product behind Griffin."}
   ]},
   {"h": "Tier 2 · The autograph list, which is not the headline list", "items": [
    {"c": "Luis Hernandez · Chrome Prospect Sapphire Auto, Sapphire Selections auto, Image Variation", "p": "2026 Bowman Chrome auto comps: base $140 (33) · Refractor /499 $300 (6) · Green /99 $295 (6) · Gold /50 $230 (5, one at $1,903)",
     "w": "The top of the 34-name list by a distance. He signs seven sets in base Bowman Chrome, more than any prospect, and his base Chrome auto trades at $140 with real volume. The Sapphire /199 should settle at $250 to $400 and the Green /99 above that. If your one auto is a Hernandez, the box paid for itself at MSRP."},
    {"c": "Wandy Asigen, Mets · Chrome Prospect Sapphire Auto, Sapphire Selections auto, Image Variation", "p": "2026 Bowman Chrome auto comps: base $50 (64) · Green /99 $190 (4) · Gold /50 $798 (4) · Refractor /299 $137 (7)",
     "w": "The top international signing of the January class, who landed with the Mets after a Yankees deal fell through. Sixty-four base auto sales in ten days is the deepest liquidity of any signer; colors run far above base, which says the market is grading him as a chase. Sapphire /199 at $100 to $150 is fair; the Gold /50 is where the money goes."},
    {"c": "Jurrangelo Cijntje · Chrome Prospect Sapphire Auto", "p": "2026 Bowman Chrome auto comps: base $69 (28) · Green /99 $144 (9) · Gold /50 $281 (7)",
     "w": "The switch-pitcher. A novelty premium with a real arm behind it, and the third name on the list by price. Fine at $100 to $150 for the Sapphire /199."},
    {"c": "Santiago Solarte, Marlins · Chrome Prospect Sapphire Auto", "p": "Chrome Sapphire: Green /99 $175 (1, Oct 8). 2026 Bowman Chrome auto comps: base $18 (53) · Green /99 $79 (5)",
     "w": "The first Chrome Sapphire autograph with a clean sale, and it tells you the Sapphire premium: $175 for a Green /99 that is $79 in base Chrome. Use roughly 2x base Chrome as the opening rule for the rest of the list, then let volume correct it."},
    {"c": "The long tail: Colome, de Brun, Wilton Guerrero Jr., Hyun Seung Lee and 25 others", "p": "2026 Bowman Chrome auto comps: Colome $25 (43) · de Brun $15.50 (48) · Guerrero Jr. $10 (45) · Lee $6 (70)",
     "w": "This is what one autograph per box usually hands you. About half the autos are the base /199 tier and most of the 34 names trade under $30 as base Chrome autos, so a typical Sapphire auto is a $30 to $80 card. SlabSquatch's complaint that the /199 and /99 tiers are too weak for a $600 box is the right one."},
    {"c": "Sapphire Selections Autographs · 11 names", "p": "June Sapphire comps: Roman Anthony $355 (5) · McGonigle $203 (2) · Holliday $200 (2). Chrome Sapphire list: Griffin, Eldridge, Benge, Okamoto, Yesavage, Caissie, Bonemer, Quintero, Renteria, L. Hernandez, Asigen",
     "w": "About 60 unnumbered copies each plus Orange /25, Red /5 and a 1/1, one per 14 boxes or so. Griffin's is the only prospect-grade autograph of a headline name in the whole product; Okamoto and Yesavage are the next two with a market. Everything else in this set is a $150 to $250 card on the June comps."}
   ]},
   {"h": "Tier 3 · Prospects on the Sapphire ladder, no autograph", "items": [
    {"c": "Ethan Holliday BCP-209 (+ Image Variation)", "p": "June Sapphire comps: base $14.50 (40) · Green /99 $71 (4) · Yellow /75 $100 (4). June auto /199 $330, but there is no Holliday auto in Chrome Sapphire",
     "w": "The most-traded prospect base in the Sapphire brand this year. The base is a $15 card with 3,475 copies; the Yellow and Gold are where the premium sits. Buy the Image Variation if you want one Holliday from this product."},
    {"c": "Jesús Made BCP-244", "p": "June Sapphire comps: base $7 (19) · Yellow /75 $62 (4) · Gold /50 $115 (2) · Orange /25 $200",
     "w": "Steady color demand without the volume of Holliday or Griffin. Gold /50 at $115 is the right card at the right price."},
    {"c": "Leo De Vries BCP-170 (+ Image Variation), Eli Willits BCP-245, Max Clark BCP-236 (+ Image Variation), Sebastian Walcott BCP-231", "p": "June Sapphire comps, base: De Vries $5 (9) · Willits $4.48 (17) · Clark $5 (23) · Walcott $1.83 (11). Yellow /75: Willits $30, Clark $25, Walcott $19.50",
     "w": "Big names, cheap Sapphire base. Without an autograph in the set these are parallel plays only: Orange /25 and Red /5 are the ones worth grading, the rest are $5 to $45 cards."}
   ]}
  ],
  "avoid": [
   "Boxes at $1,200 to $1,450 resale. Random-team break spots are clearing at $47 for a one-box break (30 spots, about $1,455 gross) and $115 for two-box, so the resale price is the breaker's revenue, not the box's expected value.",
   "The base /199 autograph tier of the long tail. Half the autos in the product are this tier and most of the 34 names are $10 to $30 cards in base Chrome.",
   "White /30, the new tier between Gold /50 and Orange /25. The market has not priced it yet; wait two weeks before paying an Orange premium for it.",
   "Grading base Sapphire of anyone but Griffin, Ohtani and Murakami. At 3,475 copies and $5 to $15 raw, the fee is the whole card.",
   "Treating the Griffin Sapphire Selections auto as a Chrome Prospect auto. It is unnumbered with about 60 copies, which is scarcer than the /199 tier, but it is a different card and a different market."
  ],
  "notes": [
   "Who does not sign: Griffin (Selections only), Holliday, De Vries, Made, Walcott, Willits, Clark, Murakami, Misiorowski, Roman Anthony, Caglianone, Ohtani. The base Bowman Chrome has Murakami and Caglianone in eight autograph sets each; Sapphire has neither.",
   "Autograph tier split from the published odds: about 51% base /199, 26% Green /99, 13% Gold /50, 7% Orange /25, 3% Black /10, 1% Red /5, and a Padparadscha 1/1 at about 1 per 370 boxes.",
   "Parallel ladder for base and prospects: Yellow /75, Gold /50, White /30, Orange /25, Black /10, Red /5, Padparadscha 1/1. Three per box, so a 10-box case averages about 30 numbered cards, one or two Black /10 and most likely one Red /5.",
   "Print run 12,638 boxes (1,264 cases), up 20.5% from 10,488 in 2025 (SlabSquatch). The larger run shows up in the base and the /199 autos, not in the colors, which are fixed by their serial numbers.",
   "Verdict: at $600 through the draw it was a buy, because break spots alone clear $1,450 a box. At $1,300 resale it is a pass unless you want the Griffin and Murakami Sapphire run specifically. Singles to target: Griffin base and Yellow /75, Ohtani #100 under $180, Luis Hernandez and Asigen Sapphire autos, Image Variations of Griffin, McGonigle, Anthony and Murakami."
  ],
  "src": "Prices: eBay sold listings, Oct 7 to 10 for Chrome Sapphire, Sep 30 to Oct 10 for June Bowman Sapphire and 2026 Bowman Chrome comps, medians with counts. Checklist and odds: Checklist Insider, Degree Grading, Topps. Print run and hit rates: SlabSquatch (Oct 7). Player context: Sports Collectors Digest (Apr 8), CardHitlist, SI."
 }
}

MARK = '/* bowman-chrome-sapphire-2026 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
open(P, 'w').write(s)
print('ok', len(s))
