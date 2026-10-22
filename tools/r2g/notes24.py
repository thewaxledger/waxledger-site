"""Notes for the psa-24.json batch (Oct 22). Five new cards with 25+ PSA 10 sales in 90 days. One clears: the 2018
Topps Update Shohei Ohtani US285 (the pitching rookie; the US1 was already on the board). The other four fail on value.
The Oct 22 refresh pulls for the ten oldest board cards (Trae Young, Mitchell, Morant, Edwards, LaMelo, Cunningham,
Banchero and Doncic Silvers, Embiid and Jaylen Brown bases) are in psa-23.json, applied with refresh.py; Banchero
Silver moved from Thin to Marginal (26 sales) and Brown from a volume fail to a value fail (29 sales).
Checked and left off: 2003-04 Topps LeBron James #221 base 295776 (99 PSA 10 sales, $6,600 median, 11.5% gem, but
9,672 nines against 6,869 eights and 8,000 lower: most misses come back 8 or lower, the model's blind spot).
Usage: python3 notes24.py
"""
from r2gnotes import write_notes
LEAD = {
 "ohtani-2018-tu-us285": "Topps Update rookie, the pitching photo (the batting US1 is on the board too). Raw $99 median of 15 PSA-tracked sales ($70 to $126), latest $119.",
 "lillard-2012-prizm-245": "Base Prizm rookie, the first Prizm basketball year. Raw $41 median of 15 PSA-tracked sales ($15 to $91).",
 "towns-2015-prizm-328": "Base Prizm rookie. Raw $8.99 median of 15 PSA-tracked sales ($2.82 to $16.99).",
 "tatis-2019-topps-410": "Topps Series 2 base rookie. Raw $1.50 median of 15 PSA-tracked sales ($0.49 to $3.99).",
 "miller-2023-prizm-152": "Base Prizm rookie. Raw $1.79 median of 15 PSA-tracked sales ($0.50 to $12.99).",
}
CLOSE = {
 "ohtani-2018-tu-us285": "Clears: a $433 PSA 10 nets about $132 over the $169 all-in, a $146 nine loses about $61, and 59% gem against a 32% break-even gives +$52 expected value. 395 PSA 10 sales in 90 days (median $433, latest $401; the average is $557 because the range runs $50 to $1,652) and 14,714 tens in circulation, so the slab is liquid but not scarce. The 10 price has drifted down through October; re-check before buying raw above $110.",
 "lillard-2012-prizm-245": "Fails: a $169 PSA 10 nets about $7 over the $110 all-in, a $55 nine loses about $70, and 49% gem against a 91% break-even gives –$32 expected value. 27 PSA 10 sales in 90 days (median $169, latest $205). Only clears on a raw copy under $25.",
 "towns-2015-prizm-328": "Fails at any gem rate: a $51 PSA 10 nets about $35 against a $79 all-in, so even a hit loses about $44. 38 PSA 10 sales in 90 days (median $51, latest $85). Buy the slab.",
 "tatis-2019-topps-410": "Fails at any gem rate: a $19 PSA 10 nets about $13 against a $71 all-in. 191 PSA 10 sales in 90 days (median $19, latest $20) and 19,881 tens in circulation; the PSA 10 is cheaper than the grading fee. Buy the slab.",
 "miller-2023-prizm-152": "Fails at any gem rate: a $31 PSA 10 nets about $21 against a $72 all-in. 39 PSA 10 sales in 90 days (median $31, latest $33); 60% gem does not help when the 10 is under the fee. Buy the slab.",
}
write_notes("psa-24.json", LEAD, CLOSE, "Oct 22")
