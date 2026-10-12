"""Notes for the psa-11.json batch (Oct 12): the daily refresh of the ten oldest board entries (refresh.py) plus
one new card, Ivan Demidov's Young Guns. Usage: python3 notes11.py
"""
from r2gnotes import write_notes
LEAD = {
 "demidov-2025-ud-205": "Young Guns rookie (2025-26 Series 1), the most-traded Young Guns PSA 10 of the last 90 days. Raw price is eBay sold ($90 median of 58 sales, Oct 6 to 11); PSA's own raw tracking has $80.",
}
CLOSE = {
 "demidov-2025-ud-205": "Liquid (107 PSA 10 sales in 90 days) and the math is positive but thin: a 28% gem rate against a 22% break-even, about +$16 a try at a $90 raw, with the $136 PSA 9 holding a miss to about –$59. Marginal. It clears at a raw under $75, which the Oct 11 sales ($70 to $90) say is available on a patient bid; above $100 it is a coin flip.",
}
write_notes("psa-11.json", LEAD, CLOSE, "Oct 12")
