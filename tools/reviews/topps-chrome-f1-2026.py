"""Add the 2026 Topps Chrome Formula 1 deep review to the master page (idempotent).
Written Oct 13, two days before the hobby release: the checklist and box contents are published, pack odds are not.
Box prices are presale sales from eBay sold listings. Only First Day Issue boxes (shipped Oct 9) have been opened,
so single-card prices are 18 individual sales and are listed as such. Refresh after Oct 15."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Topps Chrome Formula 1", "when": "Out now · boxes Nov 1, singles Oct 15", "score": "4.8",
 "facts": [
  "Hobby: 20 packs of 4 (80 cards) with one autograph, four Prism Refractors and three or more numbered parallels. $469.99 at Topps' Sep 15 presale, $479.99 on release day; $850 median on eBay around release (10 boxes sold Oct 13 to 15), $677 two weeks on (26 boxes sold Oct 28 to Nov 1, $630 to $800), down from $948 in presale",
  "Mega box: 6 packs of 7, $209 median on eBay presale (21 sold Oct 3 to 12). Value box: 28 cards, $71 median (47 sold Oct 1 to 13)",
  "200-card base set: 22 F1 drivers, 22 F2, 27 F3, 17 F1 Academy, then cars, Grand Prix winners, legends, duos, team logos and team principals",
  "One rookie card on the checklist: Arvid Lindblad #12 (and his car card, #100). His F1 Debut Patch Autograph is a 1/1",
  "Topps has not published pack odds or a print run. First Day Issue boxes shipped Oct 9; 18 single cards have sold on eBay since"
 ],
 "bars": [["Rookie class", 4.0], ["Hit quality", 6.5], ["Print run", 5.5], ["Price vs. value", 3.0]],
 "deep": {
  "lede": "Written Oct 13, two days before the hobby release (Oct 15, 11am ET at Topps); hobby box price updated Oct 15 ($850 median on 10 eBay sales Oct 13 to 15). The checklist and the box contents are published; pack odds are not, so nothing below is stated as a ratio unless Topps gave a per-box or per-case count. Box prices are real presale sales from eBay sold listings. Single-card prices are not a market yet: only First Day Issue boxes have been opened, and 18 cards sold between Oct 10 and Oct 13. Those are listed as individual sales, not medians. The short version: a hobby box costs about twice what Topps charged for it, it holds 80 cards and one autograph from a list of about 100 signers that runs from Verstappen to F3 and F1 Academy drivers, and the checklist has one rookie card.",
  "sections": [
   {"h": "Tier 1 · The cards worth opening a hobby box for", "items": [
    {"c": "Autographs of the title contenders · Chrome Autographs, Vuelta 1, Podium Triple Autographs", "p": "Prices pending. One early sale each: George Russell Molten Mercury auto /15 $2,299.99 (Oct 10) · Sergio Perez Molten Mercury auto /15 $1,100 (Oct 12)",
     "w": "One autograph per hobby box. Chrome Autographs has about 100 subjects: Verstappen, Norris, Hamilton, Leclerc, Piastri, Russell and Antonelli are on it, and so are F2, F3 and F1 Academy drivers, team principals and retired drivers. Vuelta 1 is a 22-card set of the current grid. The two sales above are First Day Issue parallels numbered to 15, so they are a ceiling, not a guide to a base autograph."},
    {"c": "Arvid Lindblad · #12 RC, Futuro autograph FUT-1, F1 Debut Patch Autograph 1/1", "p": "No sales yet",
     "w": "The only card on the checklist marked RC. Futuro Chrome Autographs is a four-card set (Lindblad, Rafael Câmara, Ugo Ugochukwu, Kaylee Countryman) with parallels from Orange /25 down. For scale, last year's equivalent card, Kimi Antonelli's 2025 Topps Chrome F1 #8, sells for a $754 median in PSA 10 (20 sales in 90 days, $550 to $1,875) and $99 in PSA 9 (39 sales); PSA has graded 264 and 68 are tens (PSA APR and pop report, Oct 13). That is one driver's card a year on, not a forecast for Lindblad."},
    {"c": "Low-numbered parallels of Verstappen, Norris, Hamilton, Antonelli · Gold /50, Orange /25, Full Grid /22, Black /10, Red /5, SuperFractor 1/1", "p": "Prices pending",
     "w": "Hobby boxes carry the Prism ladder (Blue /150 down to Red /5) and the Full Grid Refractor /22. Three or more numbered cards per box across a 200-card base set and every insert set means a numbered card of one particular driver is a long shot in a single box; Topps has not published the odds."},
    {"c": "Case hits: Chrome Anime (9 cards), Genesis (10), Futuro (4), The Grail (3 in hobby)", "p": "Prices pending",
     "w": "Checklist Insider lists each of these as a case hit: about one per 12-box case, which at presale prices is one per $11,000 of boxes. The Grail has Norris, Verstappen and Piastri and leads to a 1/1 gold autograph prize card."}
   ]},
   {"h": "Tier 2 · Mid-range: inserts and unnumbered refractors", "items": [
    {"c": "Helmet Collection (22 cards) and Image Variations (10)", "p": "Early sales, Oct 12 to 13: Verstappen $40 · Russell, Gasly and Perez $15 each",
     "w": "Four sales, all from First Day Issue boxes. Prices set by a handful of early boxes usually come down once hobby cases are open."},
    {"c": "Speed Wheels, Austin to Mexico City, Dancing in the Rain, Helix, Abu Dhabi At Night (22 cards each)", "p": "Early sales: Antonelli Speed Wheels $25 (Oct 11) · Verstappen Austin to Mexico City $14.99 (Oct 10)",
     "w": "One sale each. Austin to Mexico City, Dancing in the Rain and Helmet Collection have the full numbered parallel run; Helix and Abu Dhabi At Night have only a SuperFractor."},
    {"c": "Prism Refractors · hobby only, four per box", "p": "One early sale: Nikola Tsolov #26 Prism Refractor $4 (Oct 11)",
     "w": "The unnumbered hobby parallel. Tsolov is an F2 driver; a top F1 driver's Prism has not sold yet."},
    {"c": "Molten Mercury /15 · First Day Issue only", "p": "Early sales: Rafael Câmara $400 (Oct 11) · George Russell #120 $299.99 (Oct 10) · Ella Lloyd $150 (Oct 12). Câmara autograph /15 $1,500 (Oct 10)",
     "w": "Not in hobby boxes. Listed here because these are most of the money that has changed hands so far, and because sellers will price hobby parallels against them. A /15 from a format that sold out at $1,600 a box is not a comparison for a /150."}
   ]},
   {"h": "Tier 3 · Everything else in the box", "items": [
    {"c": "Base cards · 200 subjects", "p": "One early sale: George Russell #120 Grand Prix Winner $4 (Oct 13). The rest pending",
     "w": "Of the 200, 22 are current F1 drivers (#1 to #22) and 66 are F2, F3 and F1 Academy drivers. The others are cars, Grand Prix winner and Driver of the Day cards, 15 legends, duos, team logos and team principals."},
    {"c": "Base Refractor and numbered Pink /250, Aqua /199, Blue /150, Green /99, Purple /75", "p": "One early sale: Ayrton Senna numbered refractor $14.99 (Oct 12; the listing calls it Green /199, and the checklist has Green /99 and Aqua /199)",
     "w": "The higher-numbered half of the ladder. With 66 feeder-series drivers in the base set, most of these will not be F1 drivers."},
    {"c": "Retail-only inserts: Suit Up, Home Straight, The Grid, Art du Grand Prix", "p": "Not in hobby boxes",
     "w": "Mega and value boxes have their own parallels (Checker Flag in mega, black-and-white RayWave in value) and these insert sets. Art du Grand Prix is one per 40-box value case."}
   ]}
  ],
  "avoid": [
   "Paying $850 for a hobby box that Topps sold for $469.99 and $479.99 on release day. The 31 single boxes sold on eBay in presale had a $935 median; the 10 sold Oct 13 to 15 are at $850. That is about $11.85 a card for 80 cards and one autograph. Try the Topps sale first.",
   "Reading the Molten Mercury sales as hobby prices. Every four-figure sale so far is a First Day Issue card numbered to 15.",
   "Buying a hobby box for Lindblad. One rookie card in a 200-card set, with three or more numbered parallels a box spread across the base set and the inserts. Buy the single after release.",
   "Assuming the autograph is a current F1 driver. The Chrome Autographs list has about 100 subjects; 22 drivers are on the grid, and the rest are F2, F3 and F1 Academy drivers, team principals and retired drivers.",
   "Confusing the formats when buying sealed. Hobby (Oct 15), mega and value boxes, First Day Issue (shipped Oct 9), Hongbao, Logofractor (Oct 29) and Sapphire (Nov 12) are seven different products with different parallels."
  ],
  "notes": [
   "Refreshed Nov 2 (eBay sold listings read in the browser pane, lots, cases and breaks excluded): hobby box $677.50 median on 26 sales Oct 28 to Nov 1 ($630 to $799.99), down 20% from the $850 release-week median and 29% from the $948 presale. Lindblad base and unnumbered inserts (Helmet Collection, Dancing in the Rain, Prism Refractor) $3.49 median on 47 sales Oct 28 to Nov 1; Lindblad autographs: Aqua refractor $256, Checker /10 $1,000, Red Checker /5 $2,299.99 (one sale each, Oct 14 to 30). The other single-card lines below keep their Oct 10 to 15 reads.",
   "Box contents (Topps Ripped): hobby is 20 packs of 4 with one autograph, four Prism Refractors and three or more numbered parallels, 12 boxes a case. Mega is 6 packs of 7 with eight Checker Flag parallels, two refractors and two retail inserts. Value is 28 cards (7 packs of 4 per Topps Ripped, 4 packs of 7 per Checklist Insider) with four black-and-white RayWave Refractors, two refractors and two retail inserts. First Day Issue is 20 packs of 4 with one Molten Mercury autograph /15, two Molten Mercury parallels /15 and three more numbered cards.",
   "Presale box prices, eBay sold, single boxes only: hobby $900 median on 19 sales Sep 15 to 30 ($714 to $1,320) and $948 on 12 sales Oct 1 to 12. One sealed 12-box case sold for $11,694 on Sep 30, about $975 a box. Release week: hobby $850 median on 10 sales Oct 13 to 15 ($775 to $1,049). Mega $181 median on 68 sales since Sep 15, $209 on the 21 since Oct 3 ($143 to $280). Value $71 on 47 sales Oct 1 to 13 ($60 to $120).",
   "First Day Issue sold through a Topps Dutch auction on Sep 10 that opened at $2,000 and sold out at $1,600 (Checklist Insider). No sealed First Day Issue box showed up in eBay sold listings.",
   "Base set layout (Checklist Insider): F1 drivers #1 to #22, F2 #23 to #44, F3 #45 to #71, F1 Academy #72 to #88, F1 cars #89 to #110, Grand Prix winners #111 to #134, Driver of the Day #135 to #149, award winners #150 to #152, legends #153 to #167, duos #168 to #178, team logos #179 to #189, team principals #190 to #200. Norris #1, Piastri #2, Russell #3, Antonelli #4, Verstappen #5, Hadjar #6, Leclerc #7, Hamilton #8. Topps marks the checklist as subject to change.",
   "Parallels: Refractor, Pink /250, Aqua /199, Blue /150, Green /99, Purple /75, Gold /50, Orange /25, Full Grid /22, Black /10, Red /5, SuperFractor 1/1, printing plates. Hobby adds the Prism ladder, mega the Checker Flag ladder, value the RayWave ladder.",
   "Release dates for the other editions differ by source: Topps Ripped puts Hongbao on Oct 15 with hobby, Steel City lists Hongbao and Logofractor for Oct 29. Sapphire is Nov 12.",
   "The scores are a first read. Print run is scored in the middle because Topps has not published one and no pack odds are out to estimate it from. Pending after release: medians with counts for the top drivers' base, Prism and numbered parallels, the Lindblad rookie, autographs by signer and the case hits.",
   "Verdict for now: at the Topps price a hobby box is a reasonable gamble on one autograph. At $850 it is a pass. Wait for hobby cases to open and buy singles."
  ],
  "src": "Box prices: eBay sold listings, Sep 15 to Oct 12 (presale) and Oct 13 to 15 (release), medians with counts, single boxes only. Single-card prices: eBay sold listings, Oct 10 to 13, individual early sales from First Day Issue boxes. Topps prices, formats and checklist: Checklist Insider, Topps Ripped, Topps.com, Cardsmiths Breaks. Antonelli comparison: PSA Auction Prices Realized and pop report, Oct 13."
 }
}

MARK = '/* topps-chrome-f1-2026 */'
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', lambda m: entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)
open(P, 'w').write(s)
print('ok', len(s))
