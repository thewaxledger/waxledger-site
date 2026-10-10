// Screenshot of the admin traffic panel after the traffic test has populated a day.
const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
const lastCode = async (p, email) => { const m = await (await p.request.get(B + '/__mail')).json(); const x = m.filter(o => o.to === email).pop(); return (x.subject.match(/(\d{6})/) || [])[1]; };
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, userAgent: UA }); const p = await ctx.newPage();
  await p.goto(B + '/#trade'); await p.waitForTimeout(400);
  await p.click('#hdr-signin'); await p.fill('#auth-login-email', 'admin@example.com'); await p.fill('#auth-login-pw', 'test-password-1'); await p.click('#auth-login-form button[type=submit]');
  await p.waitForSelector('#traffic-admin:not([hidden])', { timeout: 8000 }); await p.waitForTimeout(800);
  await p.evaluate(() => { document.querySelector('#traffic-admin').open = true; document.querySelector('#traffic-admin').scrollIntoView(); });
  await p.waitForTimeout(300); await p.screenshot({ path: 'out/traffic-panel.png' });
  await b.close();
})();
