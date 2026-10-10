// Traffic counting: anonymous visits are counted, admin visits are not, and the admin panel renders the table.
const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
const lastCode = async (p, email) => { const m = await (await p.request.get(B + '/__mail')).json(); const x = m.filter(o => o.to === email).pop(); return (x.subject.match(/(\d{6})/) || [])[1]; };
(async () => {
  const b = await chromium.launch(); let bad = 0;
  // two anonymous visitors: one desktop from a referrer, one phone direct; each looks at two tabs
  for (const [vp, ref] of [[{ width: 1280, height: 900 }, 'https://x.com/thewaxledger'], [{ width: 390, height: 844 }, '']]) {
    const ctx = await b.newContext({ viewport: vp, userAgent: UA, extraHTTPHeaders: { 'x-forwarded-for': vp.width > 700 ? '203.0.113.5' : '198.51.100.9' } });
    const p = await ctx.newPage();
    await p.goto(B + '/#market', { referer: ref || undefined }); await p.waitForTimeout(400);
    await p.click('[data-go="screener"]'); await p.waitForTimeout(400);
    await ctx.close();
  }
  // admin arrives (counts as a visitor until signed in: one load of #trade), signs in, then clicks around: those must not count
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, userAgent: UA, extraHTTPHeaders: { 'x-forwarded-for': '192.0.2.77' } });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(B + '/#trade'); await p.waitForTimeout(500);
  await p.click('#hdr-signin'); await p.click('#auth-forgot'); await p.fill('#auth-email', 'admin@example.com'); await p.click('#auth-email-btn');
  await p.waitForSelector('#auth-code-form:not([hidden])', { timeout: 5000 });
  await p.fill('#auth-code', await lastCode(p, 'admin@example.com')); await p.click('#auth-code-form button[type=submit]');
  await p.waitForSelector('#auth-pw-form:not([hidden])'); await p.fill('#auth-pw', 'test-password-1'); await p.fill('#auth-pw2', 'test-password-1'); await p.click('#auth-pw-form button[type=submit]');
  await p.waitForSelector('#auth-name-form:not([hidden])'); await p.fill('#auth-name', 'Admin'); await p.click('#auth-name-form button[type=submit]');
  await p.waitForSelector('#bst-board:not([hidden])'); await p.waitForTimeout(600);
  // admin reloads and clicks around: should not add views
  await p.goto(B + '/#reviews'); await p.waitForTimeout(400); await p.click('[data-go="market"]'); await p.waitForTimeout(400);
  const j = await (await p.request.get(B + '/api/hit?days=2')).json();
  const today = j.days[j.days.length - 1];
  const panel = await p.evaluate(() => { location.hash = 'trade'; return new Promise(r => setTimeout(() => r({ hidden: document.querySelector('#traffic-admin').hidden, rows: document.querySelectorAll('#traffic-table tbody tr').length, total: document.querySelector('#traffic-total').textContent }), 900)) });
  const expect = (name, ok) => { console.log((ok ? 'ok  ' : 'BAD ') + name); if (!ok) bad++; };
  expect('three visitors counted (two anonymous + admin before sign-in): ' + today.visitors, today.visitors === 3);
  expect('five tab views counted, none after admin sign-in: ' + today.views, today.views === 5);
  expect('three page loads: ' + today.loads, today.loads === 3);
  expect('referrer x.com recorded: ' + JSON.stringify(today.sources), today.sources['x.com'] === 1 && today.sources.direct === 2);
  expect('one phone, two desktop: ' + JSON.stringify(today.devices), today.devices.m === 1 && today.devices.d === 2);
  expect('tabs market 2, screener 2, trade 1: ' + JSON.stringify(today.tabs), today.tabs.market === 2 && today.tabs.screener === 2 && today.tabs.trade === 1);
  expect('admin panel visible with 14 rows and totals', !panel.hidden && panel.rows === 14 && /Last 14 days: 3 visitor-days/.test(panel.total));
  expect('non-admin GET is refused', (await p.request.get(B + '/api/hit', { headers: { cookie: '' } })).status() === 403);
  expect('no page errors', errs.length === 0); if (errs.length) console.log(errs);
  await b.close(); console.log(bad ? 'TRAFFIC FAILED' : 'TRAFFIC OK'); process.exit(bad ? 1 : 0);
})();
