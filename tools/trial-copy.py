"""Site copy for the 7-day free trial (Nov 13, 2026, Aidan's call). Run ONLY after both Stripe Payment Links
(monthly and annual) have a 7-day trial switched on, then build, test and push. Idempotent: skips edits already made.
The site already counts Stripe's "trialing" status as an active member (netlify/lib/members.mjs), so no code changes.
Usage: python3 tools/trial-copy.py
"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDITS = {
 "src/index.src.html": [
  ('data-go="membership">Join Pro, $8 a month', 'data-go="membership">Try Pro free for 7 days'),
  ('Go Pro for unlimited comps, the full Raw-to-Gem Calculator, unlimited pre-grading and the members-only Buy/Sell/Trade board.',
   'Go Pro for unlimited comps, the full Raw-to-Gem Calculator, unlimited pre-grading and the members-only Buy/Sell/Trade board. Both Pro plans start with 7 days free: cancel before day 7 and you pay nothing.'),
  ('<li>Members-only Buy/Sell/Trade board, no selling fees</li>', '<li>7 days free, then $8 a month. Cancel any time in the billing portal</li>\n        <li>Members-only Buy/Sell/Trade board, no selling fees</li>'),
  ('data-plan="monthly">Subscribe monthly', 'data-plan="monthly">Start 7-day free trial'),
  ('<li>Works out to $6.25 a month</li>', '<li>7 days free, then $75 for the year</li>\n        <li>Works out to $6.25 a month</li>'),
  ('data-plan="annual">Subscribe annually', 'data-plan="annual">Start free trial, annual'),
 ],
 "tools/pages.py": [
  ('href="/#membership">Go Pro: $8/month or $75/year', 'href="/#membership">Try Pro free for 7 days, then $8/month'),
  ('Pro is $8/month or $75/year.</p>', 'Pro is $8/month or $75/year, and starts with 7 days free.</p>'),
 ],
}
for rel, pairs in EDITS.items():
    p = os.path.join(ROOT, rel); s = open(p).read()
    for old, new in pairs:
        if new in s: continue
        assert s.count(old) == 1, (rel, old[:60])
        s = s.replace(old, new)
    open(p, "w").write(s)
print("trial copy applied")
