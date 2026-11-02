# Wax Ledger — project notes for Claude

thewaxledger.com. Aidan Denning's subscription site for sports card investors ($8/month, $75/year via Stripe).
Netlify deploys `main` on every push, so **a push is a deploy**.

## Layout

- `src/index.src.html` — the master page (single-page HTML/CSS/JS). **Edit this, never `public/index.html` directly.**
- `tools/build.py` — builds `public/index.html` from the master (adds `<head>` meta, OG tags, favicons, turns the
  "Preview build · <date>" label into "Beta · <date>"). Run `python3 tools/build.py` after every master edit.
- `netlify/functions/` — `/api/comps` (SportsCardsPro, token in Netlify env), `/api/auth`, `/api/bst`, `/api/screener`.
- `netlify/functions/hit.mjs` — `/api/hit`, first-party traffic counting (no cookies, no third party). The page sends a
  beacon on load and on each tab switch (`track()` in the master); admins signed in on the device are not counted
  (`wl-admin` flag in localStorage). `GET /api/hit?days=14` is admin-only and feeds the "Admin: site traffic" panel on
  the Buy/Sell/Trade tab. Data lives in the `traffic` blob store, one JSON per day. `TRAFFIC_SALT` (optional Netlify env)
  salts the daily visitor hash. Headless/bot user agents are skipped, so tests set a normal UA.
- `netlify/functions/newsletter.mjs` — `/api/newsletter`, the free weekly "Raw-to-Gem Friday" list. Sign-up band above the
  footer on every view and on the static pages; addresses in the `newsletter` blob store; one-click unsubscribe link in
  every email; admin panel on the B/S/T tab lists subscribers and sends an issue (test-to-me first). Issues are plain text.
- `tools/pages.py` — static, indexable pages built by `tools/build.py` from the same data: `/grade/<id>/` for every
  Raw-to-Gem card (numbers, verdict, one line of why; the full note and ranked board stay Pro), `/grade/`, `/reviews/<slug>/`
  for each deep review, `/reviews/`, `static.css`, `sitemap.xml`, `robots.txt`. They are committed output; never hand-edit.
  The app opens a card from `/#screener?card=<id>` (members).
- Pre-Grading detection (`pgDetect` → `pgRefineQuad` → `pgEdgeSearch` → `pgAspectFix` → `pgRectify` → `pgMeasure` in the
  master): the quad is fitted on a background model; `pgEdgeSearch` then collects well-supported straight lines near each
  side (offset and angle), forms the 2.5 × 3.5 combinations, flattens the nearest ones at low resolution (`pgWarp` +
  `pgInnerFrame`) and keeps the one that shows a printed border (narrowest wins; a holder's margin is wider); `pgAspectFix`
  handles parallel offsets if the shape is still off. Checks: "Card outline" (re-fitted / off / edge not found / picture
  edge uncertain) and "Card is in a holder" (strong parallel edges 1–8 mm outside two or more sides). Known limit: a card
  inside a toploader or card saver whose lit rim is stronger than the card's own edge, with no printed border to probe
  (Topps Chrome Basketball), stays flagged rather than fixed; the advice is to shoot the raw card. Gold = card edge
  (Photo tab), blue dashed = picture edge (Card tab).
- Share images: "Share image" on a Pre-Grading result and "Share the math" in the Raw-to-Gem drawer render a watermarked
  PNG (canvas) and use the Web Share sheet on phones, download elsewhere.
- `tools/outreach-drafts-<date>.md` — post and message drafts. Nothing in there is posted or sent without Aidan's go.
- `netlify/lib/screen-data.mjs` — the Raw-to-Gem Calculator card data (default export, JSON array). Also mirrored into
  the page by `tools/r2g/integrate.py`.
- `netlify/functions/screener.mjs` — `score()` is the server copy of the page's `scrCompute` model. Keep them identical.
- `tools/r2g/` — Raw-to-Gem research pipeline: `psa-N.json` (PSA Auction Prices Realized + pop pulls, keyed by candidate
  key) + `meta.json` (card identity per key) + `notes.json` (prose note per key, required) → `build.py` → entries →
  `integrate.py` (appends/replaces by id in screen-data.mjs, sets `asOf`). `model.py` prints the verdict per card.
  `candidates.js` is the candidate list used in the browser when pulling PSA data.
  `pull.js` is the browser-side pull: load it on a psacard.com page in the browser pane, then `srch(query)` finds the specId
  and `pull(specId)` returns one `psa-N.json` entry. Its header lists the PSA endpoints and their quirks. Pull a few cards
  per call and copy the results out as you go: the pane can drop mid-run and the page state goes with it.
  When the APR search (`/auctionprices/search?q=`) does not list a card, the pop-report search does: on any psacard.com
  page with jQuery, `$.ajax({url:'https://www.collectorsuniverse.com/specsearch/search/psaformatted',dataType:'jsonp',
  data:{term:'2025 bowman brr-1 cooper flagg',includePopOnly:true,mandatoryAdditionalTerms:''}})` returns
  `[{specid, description}]`; the same specId then works with `getPopulationSummary` and `getSalesBySpecId`.
  `refresh.py psa-N.json key=boardId ...` updates a card already on the board in place (numbers + one dated sentence)
  without replacing its note; use it instead of giving an existing card a second id. Check `screen-data.mjs` for the
  player before adding, the daily review adds cards too.
  2025-26 Topps Chrome Basketball has two releases with the same rookies: Topps Chrome (#251 Flagg, #252 Harper,
  #253 Edgecombe, #254 Knueppel, #255 Bailey; white jerseys) and Topps Chrome Update (#151-#155, different photos,
  Knueppel in the yellow jersey). PSA specs are separate (Update was catalogued in Oct 2026, pops still tiny), but
  sellers title both the same way, so raw prices must come from eBay listings whose titles carry the card number
  (`rawStrict` in the pane: require #254, exclude "update" and #154, and the Basketball Refractor / Skylight parallels).
  PSA's own raw tracking mixes the two (it had the #154 Refractor's $13 on the #254 spec).
  Model blind spot: the miss is priced as a PSA 9 at 85%. For cards where most misses come back 8 or lower (vintage:
  Griffey 1989 UD #1 is 3% gem, 25% nine, 35% eight) that overstates the miss value, so such cards are left off the
  board until the model prices the full grade distribution (Aidan's call).
  Spec IDs found Oct 11 and not yet pulled in full: Skenes USC88 12100378, Kurtz 15000056, Henderson 9161725, SGA Prizm
  2676839, Bailey Chrome 14982055, Acuna US250 2652951, Guerrero 2800015, Tatis 2806015, Soto US300 2652939, Wembanyama
  Prizm 10279296. The Makar / Jack Hughes / Kaprizov / MacKinnon / Demidov hockey cards found Oct 11 are on the board.
  Checked Oct 14 and left off for volume (PSA 10 sales in 90 days): Arozarena 2020 Topps Chrome #49 3451435 (47, but a
  $10 PSA 10), Caminero 2024 Topps Chrome #213 11374827 (18), Volpe 2023 Topps Chrome #4 9161727 (17), Derrick Henry
  2016 Prizm #298 2366808 (16), Garrett Wilson 2022 Prizm #309 8411814 (3), Odunze 2024 Prizm #385 12496754 (2).
  PSA has no spec yet for the Flagg Chrome Update #151 cards.
  Checked Oct 15 and left off for volume: Nacua 2023 Prizm #357 10222841 (23), De La Cruz 2023 BCP-65 8589333 (23),
  Gibbs 2023 Prizm #331 10222815 (10), Bijan 2023 Prizm #305 10222790 (9), Castle 2024 Prizm #234 12967097 (9),
  2025 Prizm base rookies (Ward #352 15118082: 9, Sanders #302 15118032: 6, Hunter #301 15118031: 1, Jeanty #315
  15118045; spec = 15117730 + card number), Curry 2009 Topps #321 1699202 (10, 5% gem). Mahomes 2017 Prizm #269
  6036052 returns an empty APR summary. Also left off Oct 15: Brunson 2018 Prizm #250 base 2692960 (13), Curry 2009
  Topps Chrome #101 889317 (4). On the board since Oct 15: Ohtani 2018 Bowman #49 2558288, Ohtani 2018 Topps Chrome
  Update HMT1 2659442, Zion 2019 Prizm #248 base 2879876, De La Cruz 2024 Topps Chrome #44 11374656 (psa-18.json).
  Three daily-review sessions ran on Oct 15 in parallel and pushed on top of each other; a run that finds main moved
  under it should reset to origin/main and re-apply only what is new (new psa-N batch, review text, news), never
  force-push. The PSA APR search misses most base cards; the pop-report search works on
  https://www.psacard.com/pop (that page has jQuery), one term at a time with a pause, and errors on some terms.
  build.py keeps the newest pull per key across psa-*.json (by asOf), so a refresh pull in a new file wins over an
  old one in psa-2.json.
  Pop-report spec descriptions carry no `#`: "2026 Topps Chrome 225 Roman Anthony", "2025 Bowman Chrome Prospects
  BCP153 Josuar Gonzalez", "2025 Bowman Draft Bdc-25 Seth Hernandez Chrome"; the base card is the shortest matching
  description. `popSearch(term)` (JSONP, no jQuery) and `runCands(list)` in pull.js do the search-filter-pull loop; the
  search is fuzzy and capped at 25, so put the card number in the term. PSA rate-limits (HTTP 429) after a few hundred
  tRPC calls in a row; pause a second or two between pulls and wait a few minutes if it starts.
  Nov 1 scan (psa-25.json): PSA has only 1 to 28 of each 2026 Topps Chrome base rookie in its pop (Murakami #274 the
  most), so none has volume yet; Murakami 2026 Topps #503 had 8 PSA 10 sales ($150, 63% gem), re-check in December.
  `pull.js` returns `latest10`; refresh.py and r2gnotes.py read that key. integrate.py replaces every meta.json card from
  build.py, so a note edited on the board by hand (refresh.py sentences included) must be copied back into notes.json
  first or the next integrate run reverts it.
- `tools/reviews/` — the scripts that inserted each Product Review (template for new ones). A review is an entry in
  `var REVIEWS=[...]` in the master, marked with a `/* slug */` comment so the script is idempotent. Entries with a
  `deep` object render the expandable "Full breakdown" and show "WAX SCORE / 10"; entries without are sample previews.
- `tools/test/` — `run.sh` starts a stub API server on :8791 serving `public/` (in-memory members, mail, comps) and runs
  `smoke.cjs` (every view, desktop + phone, console errors, horizontal overflow), `rev.cjs` (Product Reviews render),
  `scr.cjs` (member sign-in + Raw-to-Gem board), `traffic.cjs` (visit counting and the admin panel), `panel.cjs`
  (screenshot of the traffic panel), `news.cjs` (newsletter), `pages.cjs` (static pages + deep link), `filt.cjs` (Raw-to-Gem column sort and filter dropdowns, desktop + phone), `share.cjs`
  (share images), `pg.cjs` (Pre-Grading detection on synthetic photos: plain, toploader rim, dark-on-dark, off-centre,
  keystone, chrome pinstripe in a toploader, lit holder corner). `signin.cjs` signs a test member in through the site's own forms. Screenshots land in `tools/test/out/` (ignored). The stub's `/api/comps` returns
  402 for non-members; that is expected noise.

## Release checklist

1. Edit `src/index.src.html` (and/or `netlify/**`).
2. `python3 tools/build.py`
3. `bash tools/test/run.sh` — every block must end OK (SMOKE, TRAFFIC, NEWS, PAGES, FILT, SHARE, PG) with no page errors.
4. Update the dates: the beta banner text ("checked <date>") and "Preview build · <date>" in the master, `asOf` in
   `screener.mjs` and `screen-data.mjs` entries you refreshed.
5. Commit with a clear message and push `main`.

## Raw-to-Gem model (keep in sync between page and screener.mjs)

fee 39.99 (PSA Value, when the PSA 10 is at or under feeCap 500) / feeHigh 59.99 (PSA Standard, above it; `scrFee()` in the master,
the same test in screener.mjs, pages.py, model.py, r2gnotes.py and refresh.py; changed Nov 1, 2026 at Aidan's request when PSA
reopened Value at $39.99 with a $500 declared-value cap), ship 10, sellFee .13, haircut .20, missReal .85, assumedGem .35,
minSales 25, minThin 10, minMargin .10, requireReal. Notes written before Nov 1 quote the $59.99 all-in in their prose; the
board's numbers are computed live, and the glossary on the tab says so.
Verdicts: SKIP (estimate comps) → THIN ("Thin market": 10–24 PSA 10 sales in 90 days, profit > 0, gem rate from the pop;
added Oct 12 at Aidan's request) → FAIL (fewer than 10 PSA 10 sales, 10–24 without a profit, or profit ≤ 0) → CANDIDATE (no pop) →
MARGINAL (gem rate minus break-even under 10 pts) → GRADE. A card with `waiveSales: true` in screen-data.mjs skips the
sales floor entirely (Aidan's call, per card; the note must say so). There is **no minimum PSA 10 price** (removed Oct 9, 2026
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
