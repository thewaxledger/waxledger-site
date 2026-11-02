"""Notes for the psa-25.json batch (Nov 1): the rookie / 1st Bowman scan Aidan asked for. 35 candidates pulled (see
candidates.js CANDS_NOV1); five have 10+ PSA 10 sales in 90 days and go on the board, all as FAIL. None clears:
the PSA 10s are too cheap against the $70 all-in, or (Hernandez, McGonigle) the gem rate is too far under break-even.
Checked and left off for volume (PSA 10 sales in 90 days): every 2026 Topps Chrome base rookie (PSA has 1 to 28 of
each in its pop so far: Murakami #274 5 sales, Misiorowski #196 2, Anthony #225 0, Griffin #74 1, McGonigle #16 0,
Okamoto #78 0, Schlittler #262 0, Wetherholt #119 0), Murakami 2026 Topps #503 (8, $150 median, 63% gem; worth a
re-check in December), Willits 2025 BDC-1 (3), Anderson BDC-3 (7), Parker BDC-8 (4), Doyle BDC-12 (0), Josuar
Gonzalez 2025 BCP153 (1), Elian Pena BCP155 (3), Rainiel Rodriguez BCP200 (4), Crews 2025 TC #146 (2), James Wood
2025 TC #132 (6), Kristian Campbell 2025 TC #171 (1), Walker Jenkins 2024 BDC166 (1). Ethan Holliday has no 2025
Bowman Draft card at PSA. The Oct 10-11 refresh pulls are in psa-26.json (refresh.py).
Usage: python3 notes25.py
"""
from r2gnotes import write_notes
LEAD = {
 "anthony-2026-topps": "Topps Series 1 base rookie, the most-graded Roman Anthony card (2,157 in the PSA pop). Raw $1.50 median of 15 PSA-tracked sales ($0.99 to $15).",
 "hernandez-2025-bdc-25": "1st Bowman Chrome of the 2025 draft's top pitcher (No. 6 pick). Raw $3.99 median of 15 PSA-tracked sales ($0.99 to $5.34).",
 "mcgonigle-2025-bcp-79": "Second-year Bowman chrome prospect card, not his 1st (that is 2023 Bowman Draft, which PSA's search did not surface). Raw $4.25 median of 15 PSA-tracked sales ($0.99 to $5).",
 "kurtz-2024-bdc-56": "1st Bowman Chrome, the year before his 2025 rookie cards (his Topps Chrome Update USC178 RC is on the board too). Raw $4 median of 15 PSA-tracked sales ($2.36 to $8).",
 "eldridge-2023-bdc-107": "1st Bowman Chrome of the Giants' 6-foot-7 first baseman. Raw $1.54 median of 15 PSA-tracked sales ($0.99 to $5.50).",
}
CLOSE = {
 "anthony-2026-topps": "Fails at any gem rate: a $40 PSA 10 nets about $28 against a $71 all-in, so even a hit loses about $44. 158 PSA 10 sales in 90 days (median $40, latest $40, range $26 to $499) and 1,454 tens in circulation at 67% gem; the market is deep and the slab is cheap. Buy the slab, not the raw. His 2026 Topps Chrome #225 has 1 card in the PSA pop so far (Nov 1).",
 "hernandez-2025-bdc-25": "Fails on expected value in a thin market: a $114 PSA 10 nets about $5 over the $74 all-in, a $25 nine loses about $55, and 46% gem against a 91% break-even gives –$27 expected value. 15 PSA 10 sales in 90 days (median $114, latest $90, range $87 to $199). The 10 has slipped through October; only a raw copy under $2 with a strong gem read changes the answer.",
 "mcgonigle-2025-bcp-79": "Fails on expected value: a $140 PSA 10 nets about $23 over the $74 all-in, a $23 nine loses about $57, and 38% gem against a 71% break-even gives –$27 expected value. 67 PSA 10 sales in 90 days (median $140, latest $128, range $104 to $458) and a 600/683/205 pop split (10/9/8), so most submissions come back a 9. Liquid slab; buy the 10 at $130 to $140 rather than grading.",
 "kurtz-2024-bdc-56": "Fails at any gem rate: a $70 PSA 10 nets about $49 against a $74 all-in, so even a hit loses about $25. 45 PSA 10 sales in 90 days (median $70, latest $56, range $45 to $125) and 765 tens in circulation at 39% gem. The 10 has fallen from $125 in August to $56 at the end of October. Buy the slab.",
 "eldridge-2023-bdc-107": "Fails at any gem rate: a $70 PSA 10 nets about $49 against a $72 all-in, so even a hit loses about $23. 17 PSA 10 sales in 90 days (median $70, latest $70, range $51 to $81), 337 tens in circulation at 69% gem. A high gem rate does not help when the 10 is under the fee. Buy the slab.",
}
write_notes("psa-25.json", LEAD, CLOSE, "Nov 1")
