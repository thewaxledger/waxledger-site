"""Notes for the psa-38.json batch (Nov 18): five candidates from a short screen of football rookies and one veteran
card (getPriceSummary first, then a full pull for the ones with 25+ PSA 10 sales in 90 days). Raw prices are eBay sold
(LH_Sold=1&LH_Complete=1) read Nov 18 in the browser pane, graded and parallel listings excluded by title.
Screened and left off: Jalen Hurts 2020 Optic #164 base (19 PSA 10 sales), Josh Allen 2018 Prizm #205 Silver (1),
Jude Bellingham 2020-21 Topps Chrome UCL #68 (9), Aaron Judge 2013 Bowman Chrome Draft BDPP19 (19), Elly De La Cruz
2023 BCP-65 (25 sales but a $26 PSA 10), Jaxson Dart 2025 Optic #273 Holo (19), Cam Ward 2025 Optic #293 (18),
Malik Nabers 2024 Prizm #370 base (8), Travis Hunter 2025 Prizm #301 Silver (0), Ashton Jeanty #315 Silver (16),
Shedeur Sanders #302 Silver (15), Jayden Daniels 2024 Donruss The Rookies TR37 (65 sales, a $46 insert; the paper
Rated Rookie did not resolve in the pop search). Dylan Crews 2023 Bowman Draft, Cole Palmer 2023-24 UCC and Jackson
Chourio 2021 BCP did not resolve in the pop search. Usage: python3 notes38.py"""
from r2gnotes import write_notes
LEAD = {
 "dart-2025-prizm-332-silver": "The Silver Prizm of his 2025 Prizm rookie (#332; the base is on the board as a fail). The first 2025 Prizm Silver with enough PSA 10 sales to size: 81 in 90 days against 10 for Cam Ward's.",
 "nacua-2023-prizm-357-silver": "The Silver Prizm of his 2023 Prizm rookie (#357; the base is on the board as a fail).",
 "maye-2024-optic-229": "Donruss Optic Rated Rookie, base (#229). The most-sold 2024 Optic quarterback at PSA: 101 PSA 10 sales in 90 days.",
 "nix-2024-optic-209": "Donruss Optic Rated Rookie, base (#209).",
 "ohtani-2018-bc-1": "His 2018 Bowman Chrome base rookie (#1, batting), the card at the top of the Ohtani rookie market by volume: 190 PSA 10 sales in 90 days at a $4,042 median. His 2018 Bowman paper #49, Topps #700, Topps Chrome #150 and Update cards are on the board.",
}
CLOSE = {
 "dart-2025-prizm-332-silver": "Clears as Grade: raw $64 median on 183 eBay sales (a thick market in both directions), the 10 pays $287 on a $134 all-in and the 9 loses $70, so the 38.6% gem rate sits 19 points above the 19.7% break-even. The pop is 555 tens to 555 nines with 228 eights (16% of the pop), which is the usual Silver Prizm surface-and-corner problem; buy centred copies, not lots. The PSA 10 has been $468 to $850 inside the window with $620 the latest, so the margin moves with his Giants season.",
 "nacua-2023-prizm-357-silver": "Fails on value, narrowly: the 10 pays $50 over a $68 all-in and the 9 loses $38, so the 33.5% gem rate (916 of 2,738) is 10 points under the 43.3% break-even, –$9 a card expected. Raw is $18 on 41 eBay sales; the PSA 10 is $170 on 29 sales. A $200 PSA 10 or a $12 raw would flip it; worth a re-check after the season.",
 "maye-2024-optic-229": "Fails on value: the 10 is $93 on 101 sales, the 9 $19, and raw $3 on 59 eBay sales, so the 10 pays $12 over the $53 all-in and the 9 loses $39; the 36% gem rate is half the 77% break-even. Volume without margin, like the other Optic base Rated Rookies on the board.",
 "nix-2024-optic-209": "Fails on value: a $68 PSA 10 (29 sales) does not cover the $51 all-in after fees and the haircut, so even a 10 loses $4; the 37% gem rate is against a break-even that cannot be reached. A $1.50 raw card to keep raw.",
 "ohtani-2018-bc-1": "Marginal, and the most expensive card on the board to try: $1,820 all-in (raw $1,750 median on 9 eBay base sales Oct 17 to Nov 10, $990 to $1,950; PSA's own tracking mixes in $1.25 to $20 junk), a 10 pays $993 and a 9 loses $785, so the 53.9% gem rate (5,468 of 10,147) is 9.8 points over the 44.1% break-even, +$173 expected on a $1,820 stake. Eights are 5.7% of the pop, so the miss-priced-as-a-9 blind spot is small here. The PSA 10 ranged $190 (a mis-listing) to $8,195 in the window with $4,000 the latest; the median moves by hundreds a week, so re-price before sending one.",
}
write_notes("psa-38.json", LEAD, CLOSE, "Nov 18")
