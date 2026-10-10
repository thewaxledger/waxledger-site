// Free weekly newsletter ("Raw-to-Gem Friday"). Addresses live in the site's own store; nothing else is collected.
// POST /api/newsletter {action:"subscribe", email, src}   -> adds the address (idempotent) and sends a welcome note
// GET  /api/newsletter?u=TOKEN&e=ID                       -> one-click unsubscribe (the link in every email)
// POST /api/newsletter {action:"list"}                    -> admin: count and addresses
// POST /api/newsletter {action:"send", subject, text, test:true|false}
//                                                         -> admin: send an issue to everyone active (test:true sends to the admin only)
import { json, bad, currentMember, sha, rid, isEmail, normEmail, clean, bump, sendMail, liveDeps } from "../lib/members.mjs";

export const config = { path: "/api/newsletter" };
const DAILY_CAP = 500;          // new sign-ups per day, in case a bot finds the form
const PER_IP = 10;              // sign-ups per IP per day
const SEND_GAP_MS = 120;        // between messages, to stay well under the mail host's per-minute limit

const page = (title, body) => new Response(`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title}</title><style>body{margin:0;background:#ECEFF1;font:16px/1.5 system-ui,sans-serif;color:#0F1B2D}main{max-width:520px;margin:12vh auto;background:#fff;border:1px solid #D0D8E0;border-radius:10px;padding:28px}a{color:#765000}</style></head><body><main><h1 style="font-size:22px;margin:0 0 10px">${title}</h1><p>${body}</p><p><a href="/">Back to Wax Ledger</a></p></main></body></html>`, { headers: { "content-type": "text/html; charset=utf-8" } });

function unsubLink(deps, id, rec) { return `${deps.site}/api/newsletter?u=${encodeURIComponent(rec.token)}&e=${encodeURIComponent(id)}`; }

export async function handle(req, deps) {
  const url = new URL(req.url), store = deps.news, now = deps.now();
  if (req.method === "GET") {
    const id = url.searchParams.get("e") || "", tok = url.searchParams.get("u") || "";
    if (!/^[a-f0-9]{16,64}$/.test(id) || !tok) return page("That link isn't valid", "If you want off the list, reply to any issue with 'unsubscribe' and we'll take care of it.");
    const rec = await store.get("sub/" + id, { type: "json" });
    if (!rec || rec.token !== tok) return page("That link isn't valid", "If you want off the list, reply to any issue with 'unsubscribe' and we'll take care of it.");
    if (!rec.unsub) { rec.unsub = now; await store.setJSON("sub/" + id, rec); }
    return page("You're unsubscribed", "No more Raw-to-Gem Friday emails. The site stays free to read whenever you want it.");
  }
  if (req.method !== "POST") return bad("Method not allowed", 405);
  let b = {};
  try { const t = await req.text(); if (t.length > 4000) return bad("Too long."); b = JSON.parse(t || "{}"); } catch (e) { return bad("Bad JSON."); }
  const action = String(b.action || "");

  if (action === "subscribe") {
    if (b.hp) return json({ status: "ok" }); // honeypot filled: a bot; say nothing
    const email = normEmail(b.email);
    if (!isEmail(email)) return bad("That doesn't look like an email address.");
    const ip = req.headers.get("x-nf-client-connection-ip") || (req.headers.get("x-forwarded-for") || "").split(",")[0].trim() || "none";
    if (!(await bump(store, "ip/" + sha(ip).slice(0, 16), PER_IP, now))) return bad("Too many sign-ups from this connection today.", 429);
    if (!(await bump(store, "all", DAILY_CAP, now))) return bad("Sign-ups are paused for today. Try again tomorrow.", 429);
    const id = sha(email).slice(0, 32), key = "sub/" + id;
    const existing = await store.get(key, { type: "json" });
    if (existing && !existing.unsub) return json({ status: "ok", already: true });
    const rec = existing ? { ...existing, unsub: 0, resubscribed: now } : { email, since: now, src: clean(b.src, 40), token: rid(12) };
    await store.setJSON(key, rec);
    try {
      await sendMail(deps, { to: email, subject: "You're on the list: Raw-to-Gem Friday",
        text: `Thanks for signing up.\n\nEvery Friday you'll get three cards that clear the grading math that week: raw price, PSA 10 and PSA 9 comps, the real gem rate, and what one attempt nets. First issue goes out Friday, October 16.\n\nUntil then, the calculator and the product reviews are at ${deps.site}\n\n— Wax Ledger\n\nUnsubscribe any time: ${unsubLink(deps, id, rec)}` });
    } catch (e) { /* the address is saved either way; mail can be retried */ }
    return json({ status: "ok" });
  }

  const me = await currentMember(req, deps);
  if (!me || !me.admin) return bad("Admins only.", 403);
  const { blobs } = await store.list({ prefix: "sub/" });
  const subs = [];
  for (const bl of blobs) { const r = await store.get(bl.key, { type: "json" }); if (r && r.email) subs.push({ id: bl.key.slice(4), ...r }); }
  const active = subs.filter(s => !s.unsub);

  if (action === "list") return json({ status: "ok", active: active.length, total: subs.length, subscribers: active.map(s => ({ email: s.email, since: s.since, src: s.src || "" })) });

  if (action === "send") {
    const subject = clean(b.subject, 150), text = String(b.text || "").slice(0, 20000);
    if (!subject || text.length < 40) return bad("Subject and at least a paragraph of text, please.");
    const targets = b.test ? [{ id: "test", email: me.email, token: "test" }] : active;
    let sent = 0, failed = 0;
    for (const s of targets) {
      const footer = `\n\n—\nYou get this because you signed up at ${deps.site}. Unsubscribe: ${b.test ? "(test send)" : unsubLink(deps, s.id, s)}`;
      try { await sendMail(deps, { to: s.email, subject, text: text + footer }); sent++; } catch (e) { failed++; }
      if (SEND_GAP_MS) await new Promise(r => setTimeout(r, SEND_GAP_MS));
    }
    if (!b.test) await store.setJSON("issue/" + new Date(now).toISOString().slice(0, 10) + "-" + rid(4), { subject, sent, failed, at: now });
    return json({ status: "ok", sent, failed, test: !!b.test });
  }
  return bad("Unknown action.");
}

export default async req => handle(req, await liveDeps());
