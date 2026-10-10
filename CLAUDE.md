# Wax Ledger — project notes for Claude

thewaxledger.com. Aidan Denning's subscription site for sports card investors ($8/month, $75/year via Stripe).
Netlify deploys `main` on every push, so **a push is a deploy**.

## Layout

- `src/index.src.html` — the master page (single-page HTML/CSS/JS). **Edit this, never `public/index.html` directly.**
- `tools/build.py` — builds `public/index.html` from the master (adds `<head>` meta, OG tags, favicons, turns the
  "Preview build · <date>" label into "Beta · <date>"). Run `python3 tools/build.py` after every master edit.
- `netlify/functions/` — `/api/comps` (SportsCardsPro, token in Netlify env), `/api/auth`, `/api/bst`, `/api/screener`.
- `netlify/lib/screen-data.mjs` — the Raw-to-Gem Calculator card data (default export, JSON array). Also mirrored into
  the page by `tools/r2g/integrate.py`.
- `netlify/functions/screener.mjs` — `score()` is the server copy of the page's `scrCompute` model. Keep them identical.
- `tools/r2g/` — Raw-to-Gem research pipeline: `psa-N.json` (PSA Auction Prices Realized + pop pulls, keyed by candidate
  key) + `meta.json` (card identity per key) + `notes.json` (prose note per key, required) → `build.py` → entries →
  `integrate.py` (appends/replaces by id in screen-data.mjs, sets `asOf`). `model.py` prints the verdict per card.
  `candidates.js` is the candidate list used in the browser when pulling PSA data.
- `tools/reviews/` — the scripts that inserted each Product Review (template for new ones). A review is an entry in
  `var REVIEWS=[...]` in the master, marked with a `/* slug */` comment so the script is idempotent. Entries with a
  `deep` object render the expandable "Full breakdown" and show "WAX SCORE / 10"; entries without are sample previews.
- `tools/test/` — `run.sh` starts a stub API server on :8791 serving `public/` (in-memory members, mail, comps) and runs
  `smoke.cjs` (every view, desktop + phone, console errors, horizontal overflow), `rev.cjs` (Product Reviews render),
  `scr.cjs` (member sign-in + Raw-to-Gem board). Screenshots land in `tools/test/out/` (ignored). The stub's
  `/api/comps` returns 402 for non-members; that is expected noise.

## Release checklist

1. Edit `src/index.src.html` (and/or `netlify/**`).
2. `python3 tools/build.py`
3. `bash tools/test/run.sh` — must end with `SMOKE OK` and no page errors.
4. Update the dates: the beta banner text ("checked <date>") and "Preview build · <date>" in the master, `asOf` in
   `screener.mjs` and `screen-data.mjs` entries you refreshed.
5. Commit with a clear message and push `main`.

## Raw-to-Gem model (keep in sync between page and screener.mjs)

fee 59.99, ship 10, sellFee .13, haircut .20, missReal .85, assumedGem .35, minSales 25, minMargin .10, requireReal.
Verdicts: SKIP (estimate comps) → FAIL (fewer than 25 PSA 10 sales in 90 days, or profit ≤ 0) → CANDIDATE (no pop) →
MARGINAL (gem rate minus break-even under 10 pts) → GRADE. There is **no minimum PSA 10 price** (removed Oct 9, 2026
at Aidan's request; it was a search guideline, not a rule).

## Data sources and their quirks

- PSA Auction Prices Realized + pop report: best source for graded sales counts and gem rates. Raw ("UNGRADED") sales
  there are thin and sometimes wrong (a $1.40 "raw" Edwards Silver); cross-check raw prices on eBay sold before trusting.
- eBay sold listings (`LH_Sold=1&LH_Complete=1`): the source for raw prices and for new-product singles. Only reachable
  from a browser pane, not from the container.
- SportsCardsPro: used live by `/api/comps`. Its website serves a Cloudflare challenge to automation — never click
  "Verify you are human" or any CAPTCHA; use PSA/eBay instead.
- Topps Ripped, Cardsmiths Breaks, Checklist Insider, CardHitlist, SlabSquatch: checklist, odds, print runs.

## House rules (from Aidan)

- Never store or type passwords, API keys, tokens, card numbers or bank details anywhere. Secrets live only in Netlify env.
- Never delete posts, listings, members or data. Never post to X/Instagram or send email/DMs without an explicit go
  from Aidan in the conversation; outreach is paused until he says otherwise.
- Do not spend money (ads, tools, test purchases) without asking.
- Comp memberships are admin-only. Do not post the giveaway card as a listing.
- The giveaway link is `/giveaway` (redirect). eBay username for the B/S/T board: amd13cards.
- Tone on the site: plain, specific, numbers with sample sizes. No hype adjectives.
