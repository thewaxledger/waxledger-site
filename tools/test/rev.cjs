const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
(async () => {
  const b = await chromium.launch();
  for (const [name, vp] of [['desk', { width: 1280, height: 900 }], ['phone', { width: 390, height: 844 }]]) {
    const ctx = await b.newContext({ viewport: vp }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error' && !/font|net::|402/i.test(m.text())) errs.push(m.text()) });
    await p.goto(B + '/#reviews'); await p.waitForTimeout(800);
    const info = await p.evaluate(() => { const g = document.querySelector('#review-grid'); const d = g.querySelector('details.review-deep'); return { cards: g.querySelectorAll('article.review').length, hasDeep: !!d, items: g.querySelectorAll('.chase li').length, h3: g.querySelector('article.review h3').innerText } });
    await p.screenshot({ path: 'out/rev-' + name + '-closed.png', fullPage: false });
    await p.click('details.review-deep summary'); await p.waitForTimeout(400);
    await p.screenshot({ path: 'out/rev-' + name + '-open.png', fullPage: true });
    console.log(name, JSON.stringify(info), 'errors', JSON.stringify(errs));
    await ctx.close();
  }
  await b.close();
})();
