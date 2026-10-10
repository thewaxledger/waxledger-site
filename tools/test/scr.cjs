const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const lastCode = async (p, email) => { const m = await (await p.request.get(B + '/__mail')).json(); const x = m.filter(o => o.to === email).pop(); return (x.subject.match(/(\d{6})/) || [])[1]; };
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error' && !/font|net::|402/i.test(m.text())) errs.push(m.text()) });
  await p.goto(B + '/#trade'); await p.waitForTimeout(600);
  await p.click('#hdr-signin'); await p.click('#auth-forgot'); await p.fill('#auth-email', 'pro3@example.com'); await p.click('#auth-email-btn');
  await p.waitForSelector('#auth-code-form:not([hidden])', { timeout: 5000 });
  await p.fill('#auth-code', await lastCode(p, 'pro3@example.com')); await p.click('#auth-code-form button[type=submit]');
  await p.waitForSelector('#auth-pw-form:not([hidden])'); await p.fill('#auth-pw', 'test-password-1'); await p.fill('#auth-pw2', 'test-password-1'); await p.click('#auth-pw-form button[type=submit]');
  await p.waitForSelector('#auth-name-form:not([hidden])'); await p.fill('#auth-name', 'Tester'); await p.click('#auth-name-form button[type=submit]');
  await p.waitForSelector('#bst-board:not([hidden])');
  await p.goto(B + '/#screener'); await p.waitForTimeout(2500);
  const info = await p.evaluate(() => { const v = document.querySelector('[data-view="screener"]'); const rows = v.querySelectorAll('tbody tr'); const txt = v.innerText; return { rows: rows.length, hasOhtani700: /Ohtani[\s\S]{0,80}700/.test(txt), hasAmen: /Amen Thompson/.test(txt), snippet: txt.slice(0, 400) } });
  console.log(JSON.stringify(info)); console.log('errors', JSON.stringify(errs));
  await p.screenshot({ path: 'out/screener.png', fullPage: true });
  await b.close();
})();
