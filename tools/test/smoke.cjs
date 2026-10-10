// Loads every view at desktop and phone widths against the stub server and reports page errors.
// Known noise: /api/comps returns 402 for non-members in the stub (comps are member-gated), so that one is ignored.
const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const VIEWS = ['market', 'screener', 'pregrade', 'trade', 'comps', 'releases', 'reviews', 'trending', 'membership'];
(async () => {
  const b = await chromium.launch(); let bad = 0;
  for (const [name, vp] of [['desk', { width: 1280, height: 900 }], ['phone', { width: 390, height: 844 }]]) {
    const ctx = await b.newContext({ viewport: vp }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    p.on('console', m => { if (m.type() === 'error' && !/font|net::|402/i.test(m.text())) errs.push(m.text()) });
    for (const v of VIEWS) {
      await p.goto(B + '/#' + v); await p.waitForTimeout(500);
      const info = await p.evaluate(v => { const el = document.querySelector('[data-view="' + v + '"]'); return { shown: !!el && !el.hidden, text: el ? el.innerText.length : 0, overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1 } }, v);
      const ok = info.shown && info.text > 50 && !info.overflow;
      if (!ok) bad++;
      console.log((ok ? 'ok  ' : 'BAD ') + name + ' #' + v + ' text=' + info.text + (info.overflow ? ' HORIZONTAL-OVERFLOW' : ''));
    }
    if (errs.length) { bad++; console.log('ERRORS ' + name + ': ' + JSON.stringify(errs.slice(0, 5))); }
    await ctx.close();
  }
  await b.close();
  console.log(bad ? 'SMOKE FAILED (' + bad + ')' : 'SMOKE OK');
  process.exit(bad ? 1 : 0);
})();
