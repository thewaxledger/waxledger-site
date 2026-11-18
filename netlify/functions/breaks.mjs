// GET /api/breaks -> the Break Guide's product models for Pro members; the product list only for everyone else.
import { json, currentMember, liveDeps } from "../lib/members.mjs";
import BREAKS from "../lib/break-data.mjs";

export const config = { path: "/api/breaks" };

export async function handle(req, deps) {
  const me = await currentMember(req, deps);
  if (me) return json({ status: "ok", member: true, products: BREAKS }, 200, { "cache-control": "private, no-store" });
  return json({ status: "ok", member: false, products: BREAKS.map(p => ({ id: p.id, name: p.name, sport: p.sport, release: p.release, asOf: p.asOf, teams: p.teams.length, formats: p.formats.map(f => f.label) })) });
}

export default async req => handle(req, await liveDeps());
