// GET /api/screener -> full Screener board for Pro members; the top 3 picks plus counts for everyone else.
// Ranking mirrors the page's default model so free visitors see the same top 3 the Market tab shows.
import { json, currentMember, liveDeps } from "../lib/members.mjs";
import SCREEN from "../lib/screen-data.mjs";

export const config = { path: "/api/screener" };
const A = { fee: 59.99, ship: 10, sellFee: .13, haircut: .20, missReal: .85, assumedGem: .35, minSales: 25, minMargin: .10, requireReal: true };
const num = v => typeof v === "number" && isFinite(v);

export function score(c) {
  if (!(num(c.raw) && num(c.psa10) && num(c.psa9))) return { code: "NODATA" };
  const gemPop = num(c.pop10) && c.popTotal ? c.pop10 / c.popTotal : null, gem = gemPop != null ? gemPop : A.assumedGem;
  const allIn = c.raw + A.fee + A.ship, net10 = c.psa10 * (1 - A.haircut) * (1 - A.sellFee), netMiss = c.psa9 * A.missReal * (1 - A.sellFee);
  const profit = gem * net10 + (1 - gem) * netMiss - allIn, roi = profit / allIn, be = net10 - netMiss ? (allIn - netMiss) / (net10 - netMiss) : null;
  let code = "GRADE";
  if (A.requireReal && c.compType !== "Real") code = "SKIP";
  else if ((num(c.psa10Sales90) ? c.psa10Sales90 : 0) < A.minSales) code = "FAIL";
  else if (profit <= 0) code = "FAIL";
  else if (gemPop == null) code = "CANDIDATE";
  else if (be == null || gem - be < A.minMargin) code = "MARGINAL";
  return { code, roi, profit };
}

export async function handle(req, deps) {
  const me = await currentMember(req, deps);
  const ranked = SCREEN.map(c => ({ c, s: score(c) }));
  const grade = ranked.filter(r => r.s.code === "GRADE").sort((a, b) => b.s.roi - a.s.roi);
  const meta = { total: SCREEN.length, clears: grade.length, asOf: "2026-10-09" };
  if (me) return json({ status: "ok", member: true, ...meta, cards: SCREEN }, 200, { "cache-control": "private, no-store" });
  return json({ status: "ok", member: false, ...meta, cards: grade.slice(0, 3).map(r => r.c) });
}

export default async req => handle(req, await liveDeps());
