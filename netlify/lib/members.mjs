// Shared helpers for member features: JSON responses, cookies, sessions, Stripe membership check, email.
// Everything that touches the outside world comes in through `deps` so handlers can be tested locally.
import crypto from "node:crypto";

export const SESSION_DAYS = 30;
export const RECHECK_MS = 24 * 3600 * 1000; // re-confirm the Stripe subscription at most once a day per session

export function json(body, status = 200, headers = {}) {
  return new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...headers } });
}
export function bad(msg, status = 400) { return json({ status: "error", error: msg }, status); }

export function cookies(req) {
  const out = {};
  (req.headers.get("cookie") || "").split(/;\s*/).forEach(p => { const i = p.indexOf("="); if (i > 0) out[p.slice(0, i)] = decodeURIComponent(p.slice(i + 1)); });
  return out;
}
export function sessionCookie(token, maxAgeSec) {
  return `wl_session=${encodeURIComponent(token)}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${maxAgeSec}`;
}
export const sha = s => crypto.createHash("sha256").update(String(s)).digest("hex");
export const rid = (n = 16) => crypto.randomBytes(n).toString("base64url");
export const normEmail = e => String(e || "").trim().toLowerCase();
export const isEmail = e => /^[^\s@]{1,64}@[^\s@]{1,190}\.[a-z]{2,}$/i.test(e);
export const clean = (s, max) => String(s == null ? "" : s).replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, "").trim().slice(0, max);

export function isAdmin(email, deps) {
  return (deps.adminEmails || []).map(normEmail).includes(normEmail(email));
}

// Active Pro membership = any subscription for a customer with this email in an active-like state.
export async function hasActiveMembership(email, deps) {
  if (isAdmin(email, deps)) return true;
  if (!deps.stripeKey) throw new Error("stripe-not-configured");
  const auth = { headers: { authorization: "Bearer " + deps.stripeKey } };
  const cr = await deps.fetchFn("https://api.stripe.com/v1/customers?limit=20&email=" + encodeURIComponent(email), auth);
  if (!cr.ok) throw new Error("stripe " + cr.status);
  const customers = (await cr.json()).data || [];
  for (const c of customers) {
    const sr = await deps.fetchFn("https://api.stripe.com/v1/subscriptions?status=all&limit=20&customer=" + encodeURIComponent(c.id), auth);
    if (!sr.ok) throw new Error("stripe " + sr.status);
    const subs = (await sr.json()).data || [];
    if (subs.some(s => ["active", "trialing", "past_due"].includes(s.status))) return true;
  }
  return false;
}

// Returns {email, name, admin} for a valid session, re-checking the membership once a day; null otherwise.
export async function currentMember(req, deps) {
  const tok = cookies(req).wl_session;
  if (!tok) return null;
  const key = "session/" + sha(tok);
  const s = await deps.users.get(key, { type: "json" });
  const now = deps.now();
  if (!s || s.exp < now) return null;
  if (now - (s.checked || 0) > RECHECK_MS) {
    let ok = true;
    try { ok = await hasActiveMembership(s.email, deps); } catch (e) { ok = true; } // don't lock members out when Stripe is unreachable
    if (!ok) { await deps.users.delete(key); return null; }
    s.checked = now; await deps.users.setJSON(key, s);
  }
  const profile = (await deps.users.get("user/" + sha(s.email), { type: "json" })) || {};
  return { email: s.email, uid: sha(s.email).slice(0, 16), name: profile.name || "", x: profile.x || "", since: profile.since || s.created, admin: isAdmin(s.email, deps) };
}

// Daily counters for rate limits: returns false once `limit` is reached.
export async function bump(store, key, limit, now) {
  const day = new Date(now).toISOString().slice(0, 10), k = "rate/" + day + "/" + key;
  const r = (await store.get(k, { type: "json" })) || { n: 0 };
  if (r.n >= limit) return false;
  r.n++; await store.setJSON(k, r); return true;
}

export async function sendMail(deps, { to, subject, text, replyTo }) {
  if (!deps.mailer) throw new Error("mail-not-configured");
  await deps.mailer({ from: '"Wax Ledger" <info@thewaxledger.com>', to, subject, text, replyTo });
}

// Real dependencies on Netlify. Imported lazily so local tests don't need the packages.
export async function liveDeps() {
  const { getStore } = await import("@netlify/blobs");
  const env = k => (globalThis.Netlify && Netlify.env && Netlify.env.get(k)) || process.env[k] || "";
  let mailer = null;
  if (env("SMTP_PASS")) {
    const nodemailer = (await import("nodemailer")).default;
    const t = nodemailer.createTransport({ host: env("SMTP_HOST") || "mail.privateemail.com", port: 465, secure: true, auth: { user: env("SMTP_USER") || "info@thewaxledger.com", pass: env("SMTP_PASS") } });
    mailer = opts => t.sendMail(opts);
  }
  return {
    users: getStore({ name: "members", consistency: "strong" }),
    board: getStore({ name: "bst", consistency: "strong" }),
    photos: getStore({ name: "bst-photos", consistency: "strong" }),
    fetchFn: fetch, now: () => Date.now(), mailer,
    stripeKey: env("STRIPE_KEY"),
    adminEmails: env("ADMIN_EMAILS").split(",").map(s => s.trim()).filter(Boolean),
    site: "https://thewaxledger.com"
  };
}
