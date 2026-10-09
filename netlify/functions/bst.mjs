// Members-only Buy/Sell/Trade board.
// GET  /api/bst                       -> recent open listings (members); {preview:{count}} for everyone else
// GET  /api/bst?id=ID                 -> one listing with replies
// GET  /api/bst?photo=PID             -> photo bytes (members)
// POST /api/bst {action:"create", type, title, details, price, wants, grade, shipping, photos:[dataURL]}
// POST /api/bst {action:"reply", id, text}
// POST /api/bst {action:"message", id, text}          -> emails the lister; reply-to is the sender's email
// POST /api/bst {action:"buy", id}                    -> "I'll take it at the asking price": recorded on the listing and emailed to the lister
// POST /api/bst {action:"offer", id, amount, note}    -> a dollar offer: recorded on the listing and emailed to the lister
// Money never moves through the site; buyer and seller settle directly (PayPal G&S or similar).
// POST /api/bst {action:"status", id, status}         -> owner/admin: open | sold | closed
// POST /api/bst {action:"delete", id}                 -> owner/admin
// POST /api/bst {action:"report", id, reason}
import { json, bad, rid, clean, currentMember, bump, sendMail, liveDeps } from "../lib/members.mjs";

export const config = { path: "/api/bst" };
const TYPES = ["sell", "buy", "trade"], MAX_PHOTOS = 4, MAX_PHOTO_BYTES = 900 * 1024, LIST_MAX = 300;
const LIMITS = { create: 8, reply: 60, message: 20, report: 20, buy: 10, offer: 20 };

function pub(l, me) {
  return {
    id: l.id, type: l.type, title: l.title, details: l.details, price: l.price, wants: l.wants, grade: l.grade, shipping: l.shipping,
    photos: l.photos, status: l.status, created: l.created, updated: l.updated, replies: (l.replies || []).length,
    seller: { name: l.name, x: l.x, since: l.since }, mine: me && l.uid === me.uid, reported: me && me.admin ? (l.reports || []).length : undefined,
    offers: me && l.uid === me.uid ? (l.offers || []).map(o => ({ id: o.id, name: o.name, email: o.email, kind: o.kind, amount: o.amount, note: o.note, at: o.at })) : undefined,
    myOffer: me ? ((l.offers || []).filter(o => o.uid === me.uid).map(o => ({ kind: o.kind, amount: o.amount, at: o.at })).pop() || null) : undefined
  };
}

export async function handle(req, deps) {
  const url = new URL(req.url), me = await currentMember(req, deps), now = deps.now();

  if (req.method === "GET") {
    const photo = url.searchParams.get("photo");
    if (photo) {
      if (!me) return bad("Members only.", 401);
      const buf = await deps.photos.get("p/" + photo.replace(/[^\w-]/g, ""), { type: "arrayBuffer" });
      if (!buf) return bad("Not found", 404);
      return new Response(buf, { headers: { "content-type": "image/jpeg", "cache-control": "private, max-age=86400" } });
    }
    const id = url.searchParams.get("id");
    if (id) {
      if (!me) return bad("Members only.", 401);
      const l = await deps.board.get("l/" + id.replace(/[^\w-]/g, ""), { type: "json" });
      if (!l || l.status === "deleted") return bad("That listing is gone.", 404);
      return json({ status: "ok", listing: { ...pub(l, me), replies: (l.replies || []).map(r => ({ id: r.id, name: r.name, text: r.text, at: r.at, mine: r.uid === me.uid, seller: r.uid === l.uid })) } });
    }
    const { blobs } = await deps.board.list({ prefix: "l/" });
    const keys = blobs.map(b => b.key).sort().reverse().slice(0, LIST_MAX);
    if (!me) return json({ status: "ok", member: false, preview: { count: keys.length } });
    const all = (await Promise.all(keys.map(k => deps.board.get(k, { type: "json" })))).filter(l => l && l.status !== "deleted");
    return json({ status: "ok", member: true, me: { name: me.name, admin: me.admin }, listings: all.map(l => pub(l, me)) });
  }

  if (req.method !== "POST") return bad("Method not allowed", 405);
  if (!me) return bad("Members only. Sign in with your Pro email.", 401);
  if (!me.name) return bad("Pick a display name first.", 400);
  let b; try { b = await req.json(); } catch (e) { return bad("Bad request"); }
  const a = b.action;
  if (LIMITS[a] && !(await bump(deps.board, a + "/" + me.uid, LIMITS[a], now))) return bad("You've hit today's limit for that. Try again tomorrow.", 429);

  if (a === "create") {
    const type = TYPES.includes(b.type) ? b.type : null;
    const title = clean(b.title, 90), details = clean(b.details, 1500), price = clean(b.price, 20).replace(/[^\d.,]/g, ""), wants = clean(b.wants, 200), grade = clean(b.grade, 40), shipping = clean(b.shipping, 80);
    if (!type) return bad("Choose Selling, Buying or Trading.");
    if (title.length < 4) return bad("Give the listing a title (player, year, set, card number).");
    if (type === "trade" && !wants) return bad("Say what you'd trade for.");
    const photos = Array.isArray(b.photos) ? b.photos.slice(0, MAX_PHOTOS) : [];
    if (type === "sell" && !photos.length) return bad("Add at least one photo of the card you're selling.");
    const ids = [];
    for (const d of photos) {
      const m = /^data:image\/jpeg;base64,([A-Za-z0-9+/=]+)$/.exec(String(d));
      if (!m) return bad("Photos must be images.");
      const buf = Buffer.from(m[1], "base64");
      if (buf.length > MAX_PHOTO_BYTES) return bad("A photo is too large.");
      const pid = rid(12); await deps.photos.set("p/" + pid, buf); ids.push(pid);
    }
    const id = new Date(now).toISOString().replace(/[-:.TZ]/g, "") + "-" + rid(5);
    const l = { id, type, title, details, price, wants, grade, shipping, photos: ids, status: "open", created: now, updated: now, uid: me.uid, email: me.email, name: me.name, x: me.x, since: me.since, replies: [], reports: [] };
    await deps.board.setJSON("l/" + id, l);
    return json({ status: "ok", listing: pub(l, me) });
  }

  const id = clean(b.id, 40).replace(/[^\w-]/g, ""), key = "l/" + id;
  const l = await deps.board.get(key, { type: "json" });
  if (!l || l.status === "deleted") return bad("That listing is gone.", 404);
  const owner = l.uid === me.uid;

  if (a === "reply") {
    const text = clean(b.text, 600);
    if (!text) return bad("Write a reply first.");
    if (l.status !== "open") return bad("This listing is closed to replies.");
    l.replies = l.replies || []; l.replies.push({ id: rid(6), uid: me.uid, name: me.name, text, at: now }); l.updated = now;
    await deps.board.setJSON(key, l);
    if (!owner) { try { await sendMail(deps, { to: l.email, subject: `New reply on "${l.title}"`, text: `${me.name} replied to your Wax Ledger listing "${l.title}":\n\n${text}\n\nSee it: ${deps.site}/#trade` }); } catch (e) {} }
    return json({ status: "ok" });
  }
  if (a === "message") {
    const text = clean(b.text, 1500);
    if (!text) return bad("Write a message first.");
    if (owner) return bad("That's your listing.");
    try {
      await sendMail(deps, { to: l.email, replyTo: me.email, subject: `Wax Ledger: ${me.name} about "${l.title}"`, text: `${me.name}${me.x ? " (@" + me.x + " on X)" : ""} sent you a private message about your listing "${l.title}":\n\n${text}\n\nReply to this email to answer them directly. Their email address is ${me.email}.\n\nTrade safely: use PayPal Goods & Services or another method with buyer protection, ship with tracking, and report anything suspicious from the listing.\n${deps.site}/#trade` });
    } catch (e) { return bad("Couldn't send the message right now. Try again shortly.", 503); }
    return json({ status: "ok" });
  }
  if (a === "buy" || a === "offer") {
    if (owner) return bad("That's your listing.");
    if (l.status !== "open") return bad("This listing is no longer open.");
    if (l.type !== "sell") return bad("Offers are for cards listed for sale. Reply or message the lister instead.");
    let amount;
    if (a === "buy") {
      amount = Number(String(l.price || "").replace(/,/g, ""));
      if (!(amount > 0)) return bad("This listing has no asking price. Make an offer instead.");
    } else {
      amount = Number(String(b.amount == null ? "" : b.amount).replace(/[^\d.]/g, ""));
      if (!(amount > 0) || amount > 1e6) return bad("Enter an offer amount in dollars.");
      amount = Math.round(amount * 100) / 100;
    }
    const note = a === "offer" ? clean(b.note, 500) : "";
    l.offers = (l.offers || []).filter(o => o.uid !== me.uid); // one standing offer per member; a new one replaces it
    l.offers.push({ id: rid(6), uid: me.uid, name: me.name, email: me.email, kind: a, amount, note, at: now }); l.updated = now;
    await deps.board.setJSON(key, l);
    const money = "$" + amount.toLocaleString("en-US", { minimumFractionDigits: amount % 1 ? 2 : 0, maximumFractionDigits: 2 });
    const subject = a === "buy" ? `Wax Ledger: ${me.name} wants to buy "${l.title}" at ${money}` : `Wax Ledger: ${money} offer from ${me.name} on "${l.title}"`;
    const body = (a === "buy"
      ? `${me.name}${me.x ? " (@" + me.x + " on X)" : ""} clicked Buy on your listing "${l.title}" and will take it at your asking price of ${money}.`
      : `${me.name}${me.x ? " (@" + me.x + " on X)" : ""} offered ${money} for your listing "${l.title}".` + (note ? `\n\nTheir note: ${note}` : ""))
      + `\n\nReply to this email to accept or counter; it goes straight to them at ${me.email}. Agree on payment (PayPal Goods & Services is the safe default), ship with tracking, then mark the listing sold on the board.\n\nOffers on this listing: ${deps.site}/#trade`;
    try { await sendMail(deps, { to: l.email, replyTo: me.email, subject, text: body }); }
    catch (e) { return bad("Saved your " + (a === "buy" ? "purchase request" : "offer") + ", but the email to the seller failed. They'll still see it on the listing.", 503); }
    return json({ status: "ok", amount });
  }
  if (a === "status") {
    if (!owner && !me.admin) return bad("Only the lister can change that.", 403);
    if (!["open", "sold", "closed"].includes(b.status)) return bad("Unknown status");
    l.status = b.status; l.updated = now; await deps.board.setJSON(key, l);
    return json({ status: "ok" });
  }
  if (a === "delete") {
    if (!owner && !me.admin) return bad("Only the lister can delete it.", 403);
    for (const p of l.photos || []) await deps.photos.delete("p/" + p);
    await deps.board.delete(key);
    return json({ status: "ok" });
  }
  if (a === "report") {
    const reason = clean(b.reason, 300) || "No reason given";
    l.reports = l.reports || [];
    if (!l.reports.some(r => r.uid === me.uid)) l.reports.push({ uid: me.uid, name: me.name, reason, at: now });
    await deps.board.setJSON(key, l);
    for (const admin of deps.adminEmails || []) { try { await sendMail(deps, { to: admin, subject: `Report on BST listing "${l.title}"`, text: `${me.name} (${me.email}) reported the listing "${l.title}" by ${l.name} (${l.email}).\n\nReason: ${reason}\n\nListing id ${l.id}. Remove it from ${deps.site}/#trade while signed in as an admin.` }); } catch (e) {} }
    return json({ status: "ok" });
  }
  return bad("Unknown action");
}

export default async req => handle(req, await liveDeps());
