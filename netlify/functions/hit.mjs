// Site traffic, kept in the site's own store. No cookies, no third party, nothing personal stored.
// POST /api/hit  {v, r, w, s, q}  -> counts one page view: v = tab shown, r = referrer, w = "m"|"d" (phone/desktop),
//                                     s = 1 on the first view of a page load, q = utm_source if the URL carried one.
//                                     Visitors are counted once a day by a salted hash of IP + user agent; the hash is
//                                     all that is kept, and it cannot be turned back into either.
// GET  /api/hit?days=14            -> admin only: one row per day with visitors, views, tabs, sources and devices.
import { json, bad, currentMember, sha, liveDeps } from "../lib/members.mjs";

export const config = { path: "/api/hit" };
const VIEWS = ["market", "comps", "screener", "pregrade", "trade", "releases", "trending", "reviews", "membership"];
const BOT = /bot|crawl|spider|slurp|preview|headless|lighthouse|pingdom|monitor|facebookexternalhit|embedly|curl|wget|python-requests/i;
const MAX_UNIQ = 20000; // per day; past this, visitors are still counted as views but not as new uniques
const dayOf = ms => new Date(ms).toISOString().slice(0, 10);

function host(ref) {
  try { const h = new URL(ref).hostname.replace(/^www\./, ""); return h || "direct"; } catch (e) { return "direct"; }
}
const inc = (o, k) => { o[k] = (o[k] || 0) + 1; };

export async function handle(req, deps) {
  const url = new URL(req.url);
  const store = deps.traffic;
  if (req.method === "GET") {
    const me = await currentMember(req, deps);
    if (!me || !me.admin) return bad("Admins only.", 403);
    const days = Math.min(90, Math.max(1, parseInt(url.searchParams.get("days") || "14", 10) || 14));
    const out = []; const now = deps.now();
    for (let i = days - 1; i >= 0; i--) {
      const day = dayOf(now - i * 864e5);
      const d = (await store.get("day/" + day, { type: "json" })) || null;
      out.push(d ? { day, visitors: Object.keys(d.uniq || {}).length, views: d.hits || 0, loads: d.loads || 0, tabs: d.views || {}, sources: d.refs || {}, utm: d.src || {}, devices: d.dev || {} }
                 : { day, visitors: 0, views: 0, loads: 0, tabs: {}, sources: {}, utm: {}, devices: {} });
    }
    const totals = out.reduce((t, r) => { t.visitors += r.visitors; t.views += r.views; t.loads += r.loads; return t; }, { visitors: 0, views: 0, loads: 0 });
    return json({ status: "ok", days: out, totals });
  }
  if (req.method !== "POST") return bad("Method not allowed", 405);
  const ua = req.headers.get("user-agent") || "";
  if (!ua || BOT.test(ua)) return json({ status: "ok", skipped: "bot" });
  let b = {};
  try { const t = await req.text(); if (t.length > 1000) return bad("Too long."); b = JSON.parse(t || "{}"); } catch (e) { return bad("Bad JSON."); }
  const v = VIEWS.includes(b.v) ? b.v : "market";
  const ref = host(String(b.r || ""));
  const same = ref === "direct" || /(^|\.)thewaxledger\.com$/.test(ref) || ref === "localhost";
  const w = b.w === "m" ? "m" : "d";
  const utm = String(b.q || "").replace(/[^\w.-]/g, "").slice(0, 40);
  const now = deps.now(), day = dayOf(now);
  const ip = req.headers.get("x-nf-client-connection-ip") || (req.headers.get("x-forwarded-for") || "").split(",")[0].trim() || "";
  const visitor = sha(day + "|" + ip + "|" + ua + "|" + (deps.salt || "")).slice(0, 20);
  const key = "day/" + day;
  const d = (await store.get(key, { type: "json" })) || { hits: 0, loads: 0, views: {}, refs: {}, dev: {}, src: {}, uniq: {} };
  d.hits++;
  inc(d.views, v);
  if (b.s) { d.loads++; inc(d.refs, same ? "direct" : ref); inc(d.dev, w); if (utm) inc(d.src, utm); }
  if (!d.uniq[visitor] && Object.keys(d.uniq).length < MAX_UNIQ) d.uniq[visitor] = 1;
  await store.setJSON(key, d); // last writer wins; at this traffic level a lost increment now and then is acceptable
  return json({ status: "ok" });
}

export default async req => handle(req, await liveDeps());
