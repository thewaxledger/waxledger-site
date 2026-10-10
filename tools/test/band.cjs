const { chromium } = require('./pw.cjs');
(async () => { const b = await chromium.launch();
  for (const [n, vp] of [['desk', { width: 1280, height: 900 }], ['phone', { width: 390, height: 844 }]]) {
    const p = await b.newPage({ viewport: vp }); await p.goto('http://localhost:8791/#reviews'); await p.waitForTimeout(400);
    await p.evaluate(() => document.querySelector('.news-band').scrollIntoView()); await p.waitForTimeout(200);
    await p.screenshot({ path: 'out/band-' + n + '.png' }); await p.close();
  } await b.close(); })();
