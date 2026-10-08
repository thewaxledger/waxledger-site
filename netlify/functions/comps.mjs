// Wax Ledger comps: look a card up in the site's own store first, ask SportsCardsPro only for cards we have not seen
// (or whose values are older than a day), save what comes back so the Ledger grows with every search.
//
// GET /api/comps?q=michael+jordan+rookie   -> best match with values, plus up to 20 other matches
// GET /api/comps?id=72584                  -> one product by SportsCardsPro id
// GET /api/comps?recent=1                  -> the most recently added cards and the running count
// GET /api/comps?ping=1                    -> {configured:true|false}
//
// The SportsCardsPro token lives in the SCP_TOKEN environment variable and never reaches the browser.
export const config = { path: "/api/comps" };

const UPSTREAM = "https://www.sportscardspro.com/api";
const FRESH_MS = 24 * 3600 * 1000;      // serve from the store without asking upstream
const STALE_MS = 7 * 24 * 3600 * 1000;  // older than this and we refresh before answering
const DAILY_CAP = 1500;                 // upstream calls per UTC day, to keep one subscription healthy
const INDEX_MAX = 2000;

export function normalizeQuery(q) {
  return String(q || "").toLowerCase().replace(/[^\p{L}\p{N}#'\-\/\s.]/gu, " ").replace(/\s+/g, " ").trim().slice(0, 80);
}

function cents(v) { return typeof v === "number" && v > 0 ? Math.round(v) / 100 : null; }

export function shapeProduct(p) {
  return {
    id: String(p.id),
    name: p["product-name"] || "",
    set: p["console-name"] || "",
    sport: p.genre || "",
    released: p["release-date"] || "",
    prices: {
      raw: cents(p["loose-price"]),
      g7: cents(p["cib-price"]),
      g8: cents(p["new-price"]),
      g9: cents(p["graded-price"]),
      bgs95: cents(p["box-only-price"]),
      psa10: cents(p["manual-only-price"])
    },
    volume: typeof p["sales-volume"] === "number" ? p["sales-volume"] : (parseInt(p["sales-volume"], 10) || null),
    fetchedAt: Date.now()
  };
}

function json(body, status = 200, extra = {}) {
  return new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...extra } });
}

// Everything below takes its dependencies as arguments so it can run locally without Netlify.
export async function handle(req, deps) {
  const { store, fetchFn, token, now = () => Date.now() } = deps;
  const url = new URL(req.url);
  const q = normalizeQuery(url.searchParams.get("q"));
  const id = (url.searchParams.get("id") || "").replace(/\D/g, "");
  if (url.searchParams.has("ping")) return json({ configured: !!token });
  if (url.searchParams.get("fields") && token) { // diagnostic: field names and values upstream returns for one product (no token echoed)
    const r = await fetchFn(UPSTREAM + "/product?id=" + encodeURIComponent(url.searchParams.get("fields").replace(/\D/g, "")) + "&t=" + encodeURIComponent(token));
    const b = await r.json(); delete b.t; return json(b);
  }
  if (url.searchParams.has("recent")) {
    const index = (await store.get("index", { type: "json" })) || { items: [], n: 0 };
    return json({ status: "ok", n: index.n || index.items.length, items: index.items.slice(0, 24) });
  }
  if (!q && !id) return json({ status: "error", error: "Give me a card to look up." }, 400);
  if (!token) return json({ status: "not_configured", error: "Live comps are not connected yet." }, 503);

  const t = now();
  async function quotaOk() {
    const day = new Date(t).toISOString().slice(0, 10);
    const rec = (await store.get("quota:" + day, { type: "json" })) || { n: 0 };
    if (rec.n >= DAILY_CAP) return false;
    rec.n++;
    await store.setJSON("quota:" + day, rec);
    return true;
  }
  async function upstream(path) {
    if (!(await quotaOk())) throw new Error("quota");
    const ctl = new AbortController();
    const timer = setTimeout(() => ctl.abort(), 9000);
    try {
      const r = await fetchFn(UPSTREAM + path + "&t=" + encodeURIComponent(token), { signal: ctl.signal, headers: { "user-agent": "WaxLedger/1.0 (+https://thewaxledger.com)" } });
      const body = await r.json();
      if (!r.ok || body.status !== "success") throw new Error(body["error-message"] || ("upstream " + r.status));
      return body;
    } finally { clearTimeout(timer); }
  }
  async function saveProduct(prod) {
    await store.setJSON("product:" + prod.id, prod);
    const index = (await store.get("index", { type: "json" })) || { items: [], n: 0 };
    if (!index.items.some(i => i.id === prod.id)) {
      index.items.unshift({ id: prod.id, name: prod.name, set: prod.set, psa10: prod.prices.psa10, raw: prod.prices.raw, at: prod.fetchedAt });
      index.n = (index.n || 0) + 1;
      if (index.items.length > INDEX_MAX) index.items.length = INDEX_MAX;
      await store.setJSON("index", index);
    }
  }
  async function productById(pid, cached) {
    const age = cached ? t - cached.fetchedAt : Infinity;
    if (cached && age < STALE_MS) return { product: cached, cached: true };
    try {
      const body = await upstream("/product?id=" + encodeURIComponent(pid));
      const prod = shapeProduct(body);
      await saveProduct(prod);
      return { product: prod, cached: false };
    } catch (e) {
      if (cached) return { product: cached, cached: true, stale: true };
      throw e;
    }
  }

  try {
    if (id) {
      const cached = await store.get("product:" + id, { type: "json" });
      const r = await productById(id, cached);
      const back = url.searchParams.get("q") ? (await store.get("query:" + q, { type: "json" })) : null;
      return json({ status: "ok", q, product: r.product, matches: back ? back.matches : [], cached: r.cached, stale: !!r.stale });
    }
    const qrec = await store.get("query:" + q, { type: "json" });
    if (qrec && t - qrec.at < FRESH_MS) {
      const cached = await store.get("product:" + qrec.best, { type: "json" });
      if (cached) return json({ status: "ok", q, product: cached, matches: qrec.matches, cached: true });
    }
    // ask upstream: best match with values, and the list of other matches
    let best, list = [];
    try {
      const body = await upstream("/product?q=" + encodeURIComponent(q));
      best = shapeProduct(body);
    } catch (e) {
      if (qrec) { // fall back to what we had
        const cached = await store.get("product:" + qrec.best, { type: "json" });
        if (cached) return json({ status: "ok", q, product: cached, matches: qrec.matches, cached: true, stale: true });
      }
      if (/quota/.test(e.message)) return json({ status: "busy", error: "The Ledger hit its daily lookup limit. Try again tomorrow." }, 429);
      if (/No products|not found|no results/i.test(e.message)) return json({ status: "none", q, error: "No card matched that search." }, 404);
      throw e;
    }
    try {
      const body = await upstream("/products?q=" + encodeURIComponent(q));
      list = (body.products || []).map(p => ({ id: String(p.id), name: p["product-name"] || "", set: p["console-name"] || "" }));
    } catch (e) { list = []; }
    const matches = list.filter(m => m.id !== best.id).slice(0, 19);
    await saveProduct(best);
    await store.setJSON("query:" + q, { best: best.id, matches, at: t });
    return json({ status: "ok", q, product: best, matches, cached: false });
  } catch (e) {
    return json({ status: "error", error: "Couldn't reach the price source right now." , detail: String(e.message || e).slice(0, 120) }, 502);
  }
}

export default async (req) => {
  const { getStore } = await import("@netlify/blobs"); // imported here so the handler above can run in local tests without Netlify
  const token = (globalThis.Netlify && Netlify.env && Netlify.env.get("SCP_TOKEN")) || process.env.SCP_TOKEN || "";
  return handle(req, { store: getStore("comps"), fetchFn: fetch, token });
};
