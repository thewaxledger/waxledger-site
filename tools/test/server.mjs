import http from "node:http"; import fs from "node:fs"; import path from "node:path";
import { handle as auth } from "../../netlify/functions/auth.mjs";
import { handle as bst } from "../../netlify/functions/bst.mjs";
import { handle as screener } from "../../netlify/functions/screener.mjs";
import { handle as comps } from "../../netlify/functions/comps.mjs";
import { handle as hit } from "../../netlify/functions/hit.mjs";
import { handle as newsletter } from "../../netlify/functions/newsletter.mjs";
import { currentMember } from "../../netlify/lib/members.mjs";
const compsStore = (() => { const m = new Map(); return { get: async (k) => m.has(k) ? JSON.parse(m.get(k)) : null, setJSON: async (k, v) => m.set(k, JSON.stringify(v)), delete: async k => m.delete(k) }; })();
const scpFetch = async url => { const u = new URL(url); if (u.pathname.endsWith("/products")) return { ok: true, status: 200, json: async () => ({ status: "success", products: [] }) };
  const q = u.searchParams.get("q") || "x"; return { ok: true, status: 200, json: async () => ({ status: "success", id: Math.abs([...q].reduce((a, c) => a * 31 + c.charCodeAt(0) | 0, 7)), "product-name": q, "console-name": "Basketball Cards 2025 Topps Chrome", "loose-price": 1950 }) }; };
const ROOT = new URL("../../public/", import.meta.url).pathname;
function store() {
  const m = new Map();
  return {
    get: async (k, o) => { if (!m.has(k)) return null; const v = m.get(k); if (o && o.type === "json") return JSON.parse(v); if (o && o.type === "arrayBuffer") return v; return v; },
    set: async (k, v) => { m.set(k, v); }, setJSON: async (k, v) => { m.set(k, JSON.stringify(v)); },
    delete: async k => { m.delete(k); }, list: async ({ prefix }) => ({ blobs: [...m.keys()].filter(k => k.startsWith(prefix || "")).map(key => ({ key })) }), _m: m
  };
}
const MEMBERS = new Set(["pro@example.com", "pro2@example.com", "pro3@example.com"]);
const mail = [];
const deps = {
  users: store(), board: store(), photos: store(), traffic: store(), salt: "local", news: store(), now: () => Date.now(), site: "http://localhost:8791",
  stripeKey: "rk_test", adminEmails: ["admin@example.com"],
  mailer: async o => { mail.push(o); },
  fetchFn: async url => {
    const u = new URL(url);
    if (u.pathname === "/v1/customers") { const e = u.searchParams.get("email"); return { ok: true, json: async () => ({ data: MEMBERS.has(e) ? [{ id: "cus_" + e }] : [] }) }; }
    if (u.pathname === "/v1/subscriptions") return { ok: true, json: async () => ({ data: [{ status: "active" }] }) };
    if (u.pathname.startsWith("/v1/checkout/sessions/")) { const id = u.pathname.split("/").pop(); if (id === "cs_test_good") { MEMBERS.add("newpro@example.com"); return { ok: true, json: async () => ({ id, status: "complete", created: Math.floor(Date.now() / 1000) - 60, customer_details: { email: "newpro@example.com" } }) }; } return { ok: false, status: 404, json: async () => ({}) }; }
    return { ok: false, status: 404, json: async () => ({}) };
  }
};
http.createServer(async (req, res) => {
  const u = new URL(req.url, "http://x");
  if (u.pathname === "/__mail") { res.end(JSON.stringify(mail)); return; }
  if (u.pathname === "/api/auth" || u.pathname === "/api/bst" || u.pathname === "/api/screener" || u.pathname === "/api/comps" || u.pathname === "/api/hit" || u.pathname === "/api/newsletter") {
    const chunks = []; for await (const c of req) chunks.push(c);
    const body = chunks.length ? Buffer.concat(chunks) : undefined;
    const r = new Request("http://localhost:8791" + req.url, { method: req.method, headers: req.headers, body: req.method === "GET" ? undefined : body });
    let out;
    if (u.pathname === "/api/screener") out = await screener(r, deps);
    else if (u.pathname === "/api/hit") out = await hit(r, deps);
    else if (u.pathname === "/api/newsletter") out = await newsletter(r, deps);
    else if (u.pathname === "/api/comps") out = await comps(r, { store: compsStore, fetchFn: scpFetch, token: "t", member: await currentMember(r, deps), visitor: "local-visitor" });
    else out = await (u.pathname === "/api/auth" ? auth : bst)(r, deps);
    const h = {}; out.headers.forEach((v, k) => { h[k] = v; }); res.writeHead(out.status, h);
    res.end(Buffer.from(await out.arrayBuffer())); return;
  }
  let f = path.join(ROOT, u.pathname === "/" ? "index.html" : u.pathname);
  if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, "index.html");
  if (!fs.existsSync(f)) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { "content-type": f.endsWith(".html") ? "text/html" : f.endsWith(".css") ? "text/css" : f.endsWith(".xml") ? "application/xml" : f.endsWith(".png") ? "image/png" : f.endsWith(".svg") ? "image/svg+xml" : "application/octet-stream" }); res.end(fs.readFileSync(f));
}).listen(8791, () => console.log("up"));
