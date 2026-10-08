# Wax Ledger

Source for [thewaxledger.com](https://thewaxledger.com). Netlify deploys `main` on every push.

- `public/` — the site (single-page `index.html`, icons, brand assets)
- `netlify/functions/comps.mjs` — `/api/comps`: looks a card up in the site's own store (Netlify Blobs) and asks
  SportsCardsPro only for cards it has not seen, or whose values are older than a day. Needs the `SCP_TOKEN`
  environment variable (SportsCardsPro API token) set in Netlify. Without it the site still works; comps show
  "being connected".

Daily upstream calls are capped at 1,500 (see `DAILY_CAP`) to protect the subscription.
