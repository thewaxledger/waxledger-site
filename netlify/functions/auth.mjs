// Member sign-in by emailed code.
// POST /api/auth  {action:"start", email}            -> emails a 6-digit code if the email has an active Pro membership
// POST /api/auth  {action:"verify", email, code}     -> sets the session cookie
// POST /api/auth  {action:"profile", name, x}        -> sets display name and optional X handle
// POST /api/auth  {action:"logout"}
// GET  /api/auth                                     -> {member:{...}} or {member:null}
import { json, bad, sha, rid, normEmail, isEmail, clean, hasActiveMembership, currentMember, bump, sendMail, sessionCookie, cookies, SESSION_DAYS, liveDeps } from "../lib/members.mjs";

export const config = { path: "/api/auth" };
const CODE_MIN = 15, MAX_TRIES = 5;

export async function handle(req, deps) {
  const now = deps.now();
  if (req.method === "GET" && new URL(req.url).searchParams.has("config")) {
    // which settings are present (never their values)
    return json({ status: "ok", stripe: !!deps.stripeKey, stripeLive: /^rk_live_|^sk_live_/.test(deps.stripeKey || ""), mail: !!deps.mailer, admins: (deps.adminEmails || []).length });
  }
  if (req.method === "GET") {
    const m = await currentMember(req, deps);
    return json({ status: "ok", member: m ? { name: m.name, x: m.x, since: m.since, admin: m.admin, email: m.email } : null });
  }
  if (req.method !== "POST") return bad("Method not allowed", 405);
  let body; try { body = await req.json(); } catch (e) { return bad("Bad request"); }
  const action = body.action;

  if (action === "start") {
    const email = normEmail(body.email);
    if (!isEmail(email)) return bad("Enter a valid email address.");
    if (!(await bump(deps.users, "start/" + sha(email), 6, now))) return bad("Too many codes requested for that email today. Try again tomorrow.", 429);
    let ok;
    try { ok = await hasActiveMembership(email, deps); } catch (e) { return bad("Couldn't check memberships right now. Try again in a minute.", 503); }
    if (!ok) return json({ status: "not_member" });
    const code = String(crypto.getRandomValues(new Uint32Array(1))[0] % 1000000).padStart(6, "0");
    await deps.users.setJSON("code/" + sha(email), { h: sha(code + email), exp: now + CODE_MIN * 60000, tries: 0 });
    try {
      await sendMail(deps, { to: email, subject: "Your Wax Ledger sign-in code: " + code, text: `Your Wax Ledger sign-in code is ${code}\n\nIt expires in ${CODE_MIN} minutes. If you didn't ask for it, you can ignore this email.\n\n${deps.site}` });
    } catch (e) { return bad("Couldn't send the code email. Try again in a minute.", 503); }
    return json({ status: "sent" });
  }

  if (action === "verify") {
    const email = normEmail(body.email), code = clean(body.code, 10).replace(/\D/g, "");
    const key = "code/" + sha(email), rec = await deps.users.get(key, { type: "json" });
    if (!rec || rec.exp < now) return bad("That code has expired. Request a new one.");
    if (rec.tries >= MAX_TRIES) { await deps.users.delete(key); return bad("Too many wrong tries. Request a new code."); }
    if (rec.h !== sha(code + email)) { rec.tries++; await deps.users.setJSON(key, rec); return bad("That code doesn't match."); }
    await deps.users.delete(key);
    const token = rid(32), exp = now + SESSION_DAYS * 864e5;
    await deps.users.setJSON("session/" + sha(token), { email, created: now, checked: now, exp });
    const pk = "user/" + sha(email), prof = (await deps.users.get(pk, { type: "json" })) || {};
    if (!prof.since) { prof.since = now; await deps.users.setJSON(pk, prof); }
    return json({ status: "ok", needsName: !prof.name }, 200, { "set-cookie": sessionCookie(token, SESSION_DAYS * 86400) });
  }

  if (action === "profile") {
    const m = await currentMember(req, deps);
    if (!m) return bad("Sign in first.", 401);
    const name = clean(body.name, 24).replace(/[^\p{L}\p{N} _.\-']/gu, "");
    const x = clean(body.x, 16).replace(/^@/, "").replace(/[^A-Za-z0-9_]/g, "");
    if (name.length < 2) return bad("Pick a display name of at least 2 characters.");
    const taken = await deps.users.get("name/" + name.toLowerCase(), { type: "json" });
    if (taken && taken.uid !== m.uid) return bad("That name is taken. Try another.");
    const pk = "user/" + sha(m.email), prof = (await deps.users.get(pk, { type: "json" })) || {};
    if (prof.name && prof.name.toLowerCase() !== name.toLowerCase()) await deps.users.delete("name/" + prof.name.toLowerCase());
    prof.name = name; prof.x = x; prof.uid = m.uid;
    await deps.users.setJSON(pk, prof);
    await deps.users.setJSON("name/" + name.toLowerCase(), { uid: m.uid });
    return json({ status: "ok", name, x });
  }

  if (action === "logout") {
    const tok = cookies(req).wl_session;
    if (tok) await deps.users.delete("session/" + sha(tok));
    return json({ status: "ok" }, 200, { "set-cookie": sessionCookie("", 0) });
  }
  return bad("Unknown action");
}

export default async req => handle(req, await liveDeps());
