// Raw-to-Gem board: column sorting and filter dropdowns, desktop table and phone list.
const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const lastCode = async (p, email) => { const m = await (await p.request.get(B + '/__mail')).json(); const x = m.filter(o => o.to === email).pop(); return (x.subject.match(/(\d{6})/) || [])[1]; };
(async () => {
  const b = await chromium.launch(); let bad = 0; const expect = (n, ok) => { console.log((ok ? 'ok  ' : 'BAD ') + n); if (!ok) bad++; };
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error' && !/font|net::|402/i.test(m.text())) errs.push(m.text()) });
  await p.goto(B + '/#trade'); await p.waitForTimeout(600);
  await p.click('#hdr-signin'); await p.click('#auth-forgot'); await p.fill('#auth-email', 'pro4@example.com'); await p.click('#auth-email-btn');
  await p.waitForSelector('#auth-code-form:not([hidden])', { timeout: 5000 });
  await p.fill('#auth-code', await lastCode(p, 'pro4@example.com')); await p.click('#auth-code-form button[type=submit]');
  await p.waitForSelector('#auth-pw-form:not([hidden])'); await p.fill('#auth-pw', 'test-password-1'); await p.fill('#auth-pw2', 'test-password-1'); await p.click('#auth-pw-form button[type=submit]');
  await p.waitForSelector('#auth-name-form:not([hidden])'); await p.fill('#auth-name', 'Tester'); await p.click('#auth-name-form button[type=submit]');
  await p.waitForFunction(() => /sign out/i.test(document.body.innerText), null, { timeout: 15000 });
  await p.goto(B + '/#screener'); await p.waitForFunction(() => document.querySelectorAll('#scr-body tr').length > 3, null, { timeout: 15000 });
  await p.evaluate(() => { const d = document.getElementById('auth-dlg'); if (d && d.open) d.close(); });
  errs.length = 0; // count only errors from the board itself, not the sign-up flow
  const rows = () => p.evaluate(() => [...document.querySelectorAll('#scr-body tr')].map(tr => { const td = tr.querySelectorAll('td'); const num = s => { const m = s.replace(/[−]/g, '-').replace(/[,$+%]/g, '').match(/-?[\d.]+/); return m ? +m[0] : null }; return { roi: num(td[10].innerText), n10: num(td[5].innerText), why: td[11].innerText } }));
  const base = (await rows()).length;
  await p.click('[data-ssort="roi"]'); await p.waitForTimeout(200);
  let r = await rows();
  expect('ROI sort shows every card, highest first', r.length > base && r.every((x, i) => i === 0 || x.roi == null || r[i - 1].roi == null || r[i - 1].roi >= x.roi));
  await p.selectOption('#scr-head select[data-sf="verdict"]', 'LIQ'); await p.waitForTimeout(200);
  r = await rows();
  expect('verdict filter: only volume fails, still ROI-sorted (' + r.length + ')', r.length > 0 && r.every(x => /few PSA 10 sales/i.test(x.why) && x.n10 < 25) && r.every((x, i) => i === 0 || r[i - 1].roi >= x.roi));
  await p.selectOption('#scr-head select[data-sf="roi"]', '.5-'); await p.waitForTimeout(200);
  r = await rows();
  expect('ROI 50%+ on top (' + r.length + ')', r.every(x => x.roi >= 50));
  await p.click('[data-ssort="roi"]'); await p.waitForTimeout(200);
  r = await rows();
  expect('second click sorts ascending', r.every((x, i) => i === 0 || r[i - 1].roi <= x.roi));
  await p.click('#scr-head [data-sreset]'); await p.waitForTimeout(200);
  await p.selectOption('#scr-head select[data-sf="profit"]', 'sort:-1'); await p.waitForTimeout(200);
  r = await p.evaluate(() => [...document.querySelectorAll('#scr-body tr')].map(tr => +tr.querySelectorAll('td')[9].innerText.replace(/[−]/g, '-').replace(/[$,+]/g, '')));
  expect('dropdown "Highest to lowest" sorts profit (' + r.length + ')', r.length > 41 && r.every((x, i) => i === 0 || isNaN(x) || isNaN(r[i - 1]) || r[i - 1] >= x));
  await p.click('#scr-head [data-sreset]'); await p.waitForTimeout(200);
  expect('reset clears filters and sort', (await rows()).length >= base && await p.evaluate(() => ![...document.querySelectorAll('#scr-head select')].some(s => s.value)));
  await p.screenshot({ path: 'out/filters-desk.png' });
  // phone
  await p.setViewportSize({ width: 390, height: 844 }); await p.waitForTimeout(300);
  await p.selectOption('#scr-msort', 'roi:-1'); await p.selectOption('#scr-mfilters select[data-sf="n10"]', '0-10'); await p.waitForTimeout(200);
  const ph = await p.evaluate(() => ({ n: document.querySelectorAll('#scr-list .row-scr').length, over: document.documentElement.scrollWidth > innerWidth + 1, vis: getComputedStyle(document.querySelector('#scr-mfilters')).display }));
  expect('phone: sort + volume filter list (' + ph.n + '), no overflow', ph.n > 0 && !ph.over && ph.vis === 'flex');
  await p.screenshot({ path: 'out/filters-phone.png', fullPage: false });
  expect('no page errors', errs.length === 0); if (errs.length) console.log(errs);
  await b.close(); console.log(bad ? 'FILT FAILED' : 'FILT OK'); process.exit(bad ? 1 : 0);
})();
