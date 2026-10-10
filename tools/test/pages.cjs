// Static pages: a grade page, the grade index, a review page and the reviews index render, link back correctly,
// and the app opens the right card from #screener?card=<id> for a member.
const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
(async () => {
  const b = await chromium.launch(); let bad = 0; const expect = (n, ok) => { console.log((ok ? 'ok  ' : 'BAD ') + n); if (!ok) bad++; };
  for (const [name, vp] of [['desk', { width: 1280, height: 900 }], ['phone', { width: 390, height: 844 }]]) {
    const ctx = await b.newContext({ viewport: vp, userAgent: UA }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    for (const path of ['/grade/ohtani-2018-topps-700-base/', '/grade/', '/reviews/bowman-fb-2026/', '/reviews/']) {
      const r = await p.goto(B + path); await p.waitForTimeout(250);
      const info = await p.evaluate(() => ({ h1: (document.querySelector('h1') || {}).innerText || '', len: document.body.innerText.length, overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1, canon: (document.querySelector('link[rel=canonical]') || {}).href || '' }));
      expect(name + ' ' + path + ' renders: ' + info.h1.slice(0, 50), r.status() === 200 && info.len > 400 && !info.overflow && /thewaxledger\.com/.test(info.canon));
      if (path === '/grade/ohtani-2018-topps-700-base/' && name === 'desk') await p.screenshot({ path: 'out/page-grade.png', fullPage: true });
      if (path === '/reviews/bowman-fb-2026/' && name === 'phone') await p.screenshot({ path: 'out/page-review-phone.png', fullPage: false });
    }
    expect(name + ' no page errors', errs.length === 0); if (errs.length) console.log(errs);
    await ctx.close();
  }
  // deep link for a member
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, userAgent: UA }); const p = await ctx.newPage();
  try { await require('./signin.cjs')(p, 'pro2@example.com'); } catch (e) {
    console.log('sign-in failed: ' + e.message.slice(0, 60)); console.log(await p.evaluate(() => [...document.querySelectorAll('[id^=auth-][id$=-form]')].map(f => f.id + ':' + (f.hidden ? 'hidden' : 'shown')).join(' ') + ' | note: ' + ((document.querySelector('#auth-note') || {}).innerText || '') + ' | board hidden: ' + document.querySelector('#bst-board').hidden));
  }
  await p.goto(B + '/#screener?card=ohtani-2018-topps-700-base'); await p.waitForTimeout(1500);
  const d = await p.evaluate(() => { const dr = document.querySelector('#drawer'); return { open: !dr.hidden, text: dr.innerText.slice(0, 80) } });
  expect('deep link opens the Ohtani card for a member: ' + d.text.replace(/\n/g, ' '), d.open && /Ohtani/i.test(d.text));
  const sm = await (await p.request.get(B + '/sitemap.xml')).text();
  expect('sitemap lists grade and review pages', /\/grade\/ohtani-2018-topps-700-base\//.test(sm) && /\/reviews\/bowman-fb-2026\//.test(sm));
  await b.close(); console.log(bad ? 'PAGES FAILED' : 'PAGES OK'); process.exit(bad ? 1 : 0);
})();
