"""Note for the psa-36.json batch (Nov 18): Jacob Misiorowski 2026 Topps Chrome #196 Refractor, added at Aidan's request.
The base #196 (spec 16805212) had 2 PSA 10 sales on the Nov 1 scan; the Refractor (16872428) has 4. Raw is eBay sold
(122 sales Oct 28 to Nov 17, $19.99 median; PSA's own tracking $16.51). Usage: python3 notes36.py"""
from r2gnotes import write_notes
LEAD = {"misiorowski-2026-tc-196-refractor": "The unnumbered Refractor of his 2026 Topps Chrome rookie (#196, released in the first 2026 Chrome set; his flagship #10 base is on the board)."}
CLOSE = {"misiorowski-2026-tc-196-refractor": "Only 4 PSA 10 sales in 90 days (the 10 is $485 median, $430 latest) and 22 cards graded in total, so there is no market to size a gem rate or a resale price from: the 41% gem rate is 9 tens. Fails the 10-sale floor whatever the math says. Re-check in December once more copies have been graded."}
write_notes("psa-36.json", LEAD, CLOSE, "Nov 18")
