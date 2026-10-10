// Newsletter: sign-up band, welcome mail with unsubscribe link, unsubscribe, admin list and test send.
const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
const mails = async p => (await p.request.get(B + '/__mail')).json();
(async () => {
  const b = await chromium.launch(); let bad = 0; const expect = (n, ok) => { console.log((ok ? 'ok  ' : 'BAD ') + n); if (!ok) bad++; };
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, userAgent: UA }); const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(B + '/#reviews'); await p.waitForTimeout(400);
  await p.fill('#news-email', 'reader@example.com'); await p.click('#news-btn'); await p.waitForTimeout(700);
  const note = await p.textContent('#news-note');
  expect('sign-up confirmed on the page: ' + note, /on the list/.test(note));
  const m = (await mails(p)).filter(x => x.to === 'reader@example.com');
  expect('welcome mail sent', m.length === 1 && /Raw-to-Gem Friday/.test(m[0].subject));
  const link = (m[0].text.match(/https?:\S+newsletter\?u=\S+/) || [])[0];
  expect('welcome mail has an unsubscribe link', !!link);
  // second sign-up is idempotent
  const again = await (await p.request.post(B + '/api/newsletter', { data: { action: 'subscribe', email: 'Reader@Example.com', src: 'test' } })).json();
  expect('re-sign-up reports already on list', again.already === true);
  // honeypot
  const hp = await (await p.request.post(B + '/api/newsletter', { data: { action: 'subscribe', email: 'bot@example.com', hp: 'x' } })).json();
  expect('honeypot swallowed quietly', hp.status === 'ok' && (await mails(p)).filter(x => x.to === 'bot@example.com').length === 0);
  // unsubscribe via the link
  const u = await p.request.get(link.replace(/^https?:\/\/[^/]+/, B));
  expect('unsubscribe page served', u.status() === 200 && /unsubscribed/i.test(await u.text()));
  // admin: sign in (API, shares cookies with the page) and list
  await require('./signin.cjs')(p, 'admin@example.com', 'test-password-1', 'Admin');
  await p.goto(B + '/#trade'); await p.waitForSelector('#news-admin:not([hidden])'); await p.waitForTimeout(600);
  expect('admin panel shows 0 active, 1 unsubscribed', /0 active subscribers \(1 unsubscribed\)/.test(await p.textContent('#news-count')));
  // resubscribe then test send
  await p.request.post(B + '/api/newsletter', { data: { action: 'subscribe', email: 'reader@example.com' } });
  const t = await (await p.request.post(B + '/api/newsletter', { data: { action: 'send', subject: 'Test issue', text: 'This is a test issue with enough words to pass the length check for sending.', test: true } })).json();
  expect('test send goes to admin only: ' + JSON.stringify(t), t.status === 'ok' && t.sent === 1 && t.test === true);
  const s = await (await p.request.post(B + '/api/newsletter', { data: { action: 'send', subject: 'Issue 1', text: 'Three cards that clear the grading math this week, with the numbers behind each one.', test: false } })).json();
  const issue = (await mails(p)).filter(x => x.subject === 'Issue 1');
  expect('real send reaches the active subscriber with an unsubscribe footer', s.sent === 1 && issue.length === 1 && /Unsubscribe: http/.test(issue[0].text));
  expect('non-admin list is refused', (await p.request.post(B + '/api/newsletter', { data: { action: 'list' }, headers: { cookie: '' } })).status() === 403);
  expect('no page errors', errs.length === 0); if (errs.length) console.log(errs);
  await b.close(); console.log(bad ? 'NEWS FAILED' : 'NEWS OK'); process.exit(bad ? 1 : 0);
})();
