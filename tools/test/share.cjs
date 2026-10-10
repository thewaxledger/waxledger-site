// Share images: the Raw-to-Gem drawer and the Pre-Grading result each produce a PNG. Download path is exercised
// (headless Chromium has no Web Share), and the PNGs are written to out/ for a look.
const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
(async () => {
  const b = await chromium.launch(); let bad = 0; const expect = (n, ok) => { console.log((ok ? 'ok  ' : 'BAD ') + n); if (!ok) bad++; };
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, userAgent: UA, acceptDownloads: true }); const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await require('./signin.cjs')(p, 'pro@example.com');
  await p.goto(B + '/#screener?card=ohtani-2018-topps-700-base'); await p.waitForTimeout(1500);
  const [dl] = await Promise.all([p.waitForEvent('download', { timeout: 8000 }), p.click('#drawer-share')]);
  await dl.saveAs('out/share-math.png');
  expect('Raw-to-Gem share image downloads: ' + dl.suggestedFilename(), /wax-ledger-ohtani/.test(dl.suggestedFilename()));
  // pre-grade: synthesize a result and share
  await p.goto(B + '/#pregrade'); await p.waitForTimeout(500);
  await p.evaluate(() => { window.__wl.pgShareTest = true; });
  const got = await p.evaluate(() => { try { PG = PG; } catch (e) { return 'no PG'; } return 'ok'; }).catch(() => 'scoped');
  // PG lives inside the IIFE, so drive the button through a synthetic share object exposed for tests
  const [dl2] = await Promise.all([p.waitForEvent('download', { timeout: 8000 }), p.evaluate(() => window.__wl.shareGradeCard({ grade: 9, subs: { center: 9, corners: 10, edges: 10, surface: 10 }, p: 0.41, verdict: 'Worth a look', conf: 'High', front: '61/39', back: '72/28', corners: 94, edges: 96, flags: [] }))]);
  await dl2.saveAs('out/share-grade.png');
  expect('Pre-Grading share image downloads: ' + dl2.suggestedFilename(), /pregrade/.test(dl2.suggestedFilename()));
  expect('no page errors', errs.length === 0); if (errs.length) console.log(errs);
  await b.close(); console.log(bad ? 'SHARE FAILED' : 'SHARE OK'); process.exit(bad ? 1 : 0);
})();
