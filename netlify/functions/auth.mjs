// Member sign-in. Email + password is the everyday route; a one-time emailed code sets the first password or resets a lost one.
// POST /api/auth  {action:"login", email, password}   -> sets the session cookie; {status:"no_password"} if this email has none yet
// POST /api/auth  {action:"start", email}             -> emails a 6-digit code if the email has an active Pro membership
// POST /api/auth  {action:"verify", email, code}      -> sets the session cookie; returns needsPassword / needsName
// POST /api/auth  {action:"checkout", session_id}     -> right after Stripe Checkout: signs the payer in so they can set a password
// POST /api/auth  {action:"password", password}       -> sets or changes the signed-in member's password
// POST /api/auth  {action:"profile", name, x}         -> sets display name and optional X handle
// POST /api/auth  {action:"comp", email, grant, note}  -> admin: free Pro for an email (creators, shops); grant:false revokes
// POST /api/auth  {action:"comps"}                    -> admin: list complimentary members
// POST /api/auth  {action:"logout"}
// GET  /api/auth                                      -> {member:{...}} or {member:null}
// GET  /api/auth?config=1                             -> which settings are present (never their values)
import { json, bad, sha, rid, normEmail, isEmail, clean, hasActiveMembership, currentMember, bump, sendMail, sessionCookie, cookies, SESSION_DAYS, liveDeps, hashPassword, checkPassword, passwordProblem } from "../lib/members.mjs";

export const config = { path: "/api/auth" };
const CODE_MIN = 15, MAX_TRIES = 5, LOGIN_TRIES_PER_DAY = 25;

async function openSession(deps, email, now) {
  const token = rid(32), exp = now + SESSION_DAYS * 864e5;
  await deps.users.setJSON("session/" + sha(token), { email, created: now, checked: now, exp });
  const pk = "user/" + sha(email), prof = (await deps.users.get(pk, { type: "json" })) || {};
  if (!prof.since) { prof.since = now; await deps.users.setJSON(pk, prof); }
  return { prof, headers: { "set-cookie": sessionCookie(token, SESSION_DAYS * 86400) } };
}

export async function handle(req, deps) {
  const now = deps.now();
  if (req.method === "GET" && new URL(req.url).searchParams.has("config")) {
    return json({ status: "ok", stripe: !!deps.stripeKey, stripeLive: /^rk_live_|^sk_live_/.test(deps.stripeKey || ""), mail: !!deps.mailer, admins: (deps.adminEmails || []).length });
  }
  if (req.method === "GET") {
    const m = await currentMember(req, deps);
    return json({ status: "ok", member: m ? { name: m.name, x: m.x, since: m.since, admin: m.admin, email: m.email } : null });
  }
  if (req.method !== "POST") return bad("Method not allowed", 405);
  let body; try { body = await req.json(); } catch (e) { return bad("Bad request"); }
  const action = body.action;

  if (action === "login") {
    const email = normEmail(body.email);
    if (!isEmail(email)) return bad("Enter a valid email address.");
    if (!(await bump(deps.users, "login/" + sha(email), LOGIN_TRIES_PER_DAY, now))) return bad("Too many sign-in attempts for that email today. Use 'Email me a code' instead.", 429);
    const prof = (await deps.users.get("user/" + sha(email), { type: "json" })) || {};
    if (!prof.pw) {
      // No password on file. Only say so for emails that are actually members, so the form can't be used to look up subscribers.
      let member = false;
      try { member = await hasActiveMembership(email, deps); } catch (e) { return bad("Couldn't check memberships right now. Try again in a minute.", 503); }
      return json({ status: member ? "no_password" : "not_member" });
    }
    if (!checkPassword(body.password, prof.pw)) return bad("That password doesn't match.", 401);
    let ok;
    try { ok = await hasActiveMembership(email, deps); } catch (e) { return bad("Couldn't check memberships right now. Try again in a minute.", 503); }
    if (!ok) return json({ status: "not_member" });
    const s = await openSession(deps, email, now);
    return json({ status: "ok", needsName: !s.prof.name }, 200, s.headers);
  }

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
      await sendMail(deps, { to: email, subject: "Your Wax Ledger code: " + code, text: `Your Wax Ledger code is ${code}\n\nEnter it on the site to set your password. It expires in ${CODE_MIN} minutes. If you didn't ask for it, you can ignore this email.\n\n${deps.site}` });
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
    const s = await openSession(deps, email, now);
    return json({ status: "ok", needsPassword: !s.prof.pw, needsName: !s.prof.name }, 200, s.headers);
  }

  if (action === "checkout") {
    // Stripe sends the payer back with ?session_id={CHECKOUT_SESSION_ID}. The id is unguessable and we accept each one once.
    const sid = clean(body.session_id, 80);
    if (!/^cs_(live|test)_[A-Za-z0-9]+$/.test(sid)) return bad("Bad checkout reference.");
    if (!deps.stripeKey) return bad("Memberships aren't connected yet.", 503);
    const usedKey = "cs/" + sha(sid);
    if (await deps.users.get(usedKey, { type: "json" })) return bad("That checkout link was already used. Sign in with your password, or request a code.");
    let cs;
    try {
      const r = await deps.fetchFn("https://api.stripe.com/v1/checkout/sessions/" + encodeURIComponent(sid), { headers: { authorization: "Bearer " + deps.stripeKey } });
      if (!r.ok) return bad("Couldn't confirm that checkout.", 400);
      cs = await r.json();
    } catch (e) { return bad("Couldn't reach Stripe right now. Try again in a minute.", 503); }
    const email = normEmail(cs.customer_details && cs.customer_details.email || cs.customer_email);
    if (cs.status !== "complete" || !isEmail(email)) return bad("That checkout isn't complete.");
    if (now - (cs.created || 0) * 1000 > 2 * 3600 * 1000) return bad("That checkout link has expired. Sign in with 'Email me a code'.");
    await deps.users.setJSON(usedKey, { at: now });
    const s = await openSession(deps, email, now);
    return json({ status: "ok", email, needsPassword: !s.prof.pw, needsName: !s.prof.name }, 200, s.headers);
  }

  if (action === "password") {
    const m = await currentMember(req, deps);
    if (!m) return bad("Sign in first.", 401);
    const problem = passwordProblem(body.password);
    if (problem) return bad(problem);
    const pk = "user/" + sha(m.email), prof = (await deps.users.get(pk, { type: "json" })) || {};
    prof.pw = hashPassword(body.password);
    await deps.users.setJSON(pk, prof);
    return json({ status: "ok", needsName: !prof.name });
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

  if (action === "comp") {
    // Admin: grant or revoke a complimentary Pro membership. {email, grant:true|false, note}
    const m = await currentMember(req, deps);
    if (!m || !m.admin) return bad("Admins only.", 403);
    const email = normEmail(body.email);
    if (!isEmail(email)) return bad("Enter a valid email address.");
    const key = "comp/" + sha(email);
    if (body.grant === false) { await deps.users.delete(key); return json({ status: "ok", email, comp: false }); }
    await deps.users.setJSON(key, { email, note: clean(body.note, 120), by: m.email, at: now });
    return json({ status: "ok", email, comp: true });
  }
  if (action === "comps") {
    const m = await currentMember(req, deps);
    if (!m || !m.admin) return bad("Admins only.", 403);
    const { blobs } = await deps.users.list({ prefix: "comp/" });
    const rows = (await Promise.all(blobs.map(b => deps.users.get(b.key, { type: "json" })))).filter(Boolean);
    return json({ status: "ok", comps: rows.map(r => ({ email: r.email, note: r.note, at: r.at })) });
  }
  if (action === "logout") {
    const tok = cookies(req).wl_session;
    if (tok) await deps.users.delete("session/" + sha(tok));
    return json({ status: "ok" }, 200, { "set-cookie": sessionCookie("", 0) });
  }
  return bad("Unknown action");
}

export default async req => handle(req, await liveDeps());
