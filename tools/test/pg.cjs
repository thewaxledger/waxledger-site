// Pre-Grading Tool: card detection on synthetic photos drawn in-page. Four scenes: a white-border card on a dark mat,
// the same card in a toploader whose rim shows on the right (the outline must be pulled back to the card's edge),
// a black-border card on a black mat (the tool must say the card edge was not found), and an off-centre card.
const { chromium } = require('./pw.cjs');
const B = 'http://localhost:8791';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
const SCENE = (opts) => new Promise((res) => {
  const W = 1600, H = 1200, cv = document.createElement('canvas'); cv.width = W; cv.height = H; const x = cv.getContext('2d');
  x.fillStyle = opts.mat; x.fillRect(0, 0, W, H);
  // a faint texture on the mat so it is not a flat colour
  for (let i = 0; i < 4000; i++) { x.fillStyle = 'rgba(255,255,255,' + (Math.random() * 0.04) + ')'; x.fillRect(Math.random() * W, Math.random() * H, 2, 2); }
  const cw = 700, ch = 980, ppm = cw / 63.5;
  // the card itself, drawn on its own canvas (with a toploader rim if asked), then placed with tilt or keystone
  const pad = 40, cc = document.createElement('canvas'); cc.width = cw + 2 * pad + (opts.rimRight || 0); cc.height = ch + 2 * pad; const c = cc.getContext('2d');
  c.fillStyle = opts.mat; c.fillRect(0, 0, cc.width, cc.height); c.translate(pad, pad);
  if (opts.rim) { c.fillStyle = opts.rim; c.fillRect(-10, -10, cw + 20 + opts.rimRight, ch + 20); }
  c.fillStyle = opts.border; c.fillRect(0, 0, cw, ch);
  const bl = opts.bl * ppm, br = opts.br * ppm, bt = opts.bt * ppm, bb = opts.bb * ppm;
  const g = c.createLinearGradient(bl, bt, cw - br, ch - bb); g.addColorStop(0, '#5a7fb8'); g.addColorStop(1, '#2b3a5c');
  c.fillStyle = g; c.fillRect(bl, bt, cw - bl - br, ch - bt - bb);
  c.fillStyle = '#e8d5a8'; c.beginPath(); c.arc(cw / 2, ch * .42, cw * .18, 0, Math.PI * 2); c.fill();
  c.fillStyle = '#c0392b'; c.fillRect(cw * .3, ch * .55, cw * .4, ch * .3);
  c.fillStyle = '#ffffff'; c.font = 'bold 48px sans-serif'; c.fillText('PLAYER', cw * .3, ch * .9);
  x.save(); x.translate(W / 2, H / 2); x.rotate((opts.rot || 0) * Math.PI / 180);
  if (opts.key) { // keystone: each row of the card canvas drawn narrower towards the top
    for (let r = 0; r < cc.height; r++) { const sc = 1 - opts.key * (1 - r / cc.height); x.drawImage(cc, 0, r, cc.width, 1, -cc.width * sc / 2, r - cc.height / 2, cc.width * sc, 1.02); }
  } else x.drawImage(cc, -cc.width / 2, -cc.height / 2);
  x.restore();
  cv.toBlob((b) => { const f = new File([b], 'scene.jpg', { type: 'image/jpeg' }); window.__wl.pgLoad('back', f);
    setTimeout(() => { const s = window.__wl.pgState('back'); res({ lr: s.lr, tb: s.tb, bm: s.borderMm, fix: s.aspectFix, aspect: s.aspect, found: s.found, innerFound: s.innerFound,
      checks: s.checks.map((c) => c.label + ':' + c.state), quality: s.quality }); }, 400); }, 'image/jpeg', 0.92);
});
(async () => {
  const b = await chromium.launch(); let bad = 0; const expect = (n, ok) => { console.log((ok ? 'ok  ' : 'BAD ') + n); if (!ok) bad++; };
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, userAgent: UA }); const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(B + '/#pregrade'); await p.waitForTimeout(600);
  const near = (a, b, t) => Math.abs(a - b) <= t;
  // 1. white border, dark mat, 2 mm all round, 3 degrees of tilt
  let r = await p.evaluate(SCENE, { mat: '#262626', border: '#f2f2f2', bl: 2, br: 2, bt: 2, bb: 2, rot: 3 });
  console.log('   plain:', JSON.stringify({ lr: r.lr.toFixed(1), tb: r.tb.toFixed(1), bm: r.bm, fix: r.fix && r.fix.sides, aspect: r.aspect.toFixed(3) }));
  expect('plain: card found, 2 mm borders, 50/50', r.found && near(r.lr, 50, 3) && near(r.tb, 50, 3) && near(r.bm.l, 2, .35) && near(r.bm.r, 2, .35) && !r.fix);
  expect('plain: outline check ok', r.checks.some((c) => c === 'Card outline:ok'));
  // 2. toploader rim: 60 px of grey rim on the right of the card
  r = await p.evaluate(SCENE, { mat: '#262626', border: '#f2f2f2', bl: 2, br: 2, bt: 2, bb: 2, rot: 2, rim: '#8a8a8a', rimRight: 60 });
  console.log('   rim:  ', JSON.stringify({ lr: r.lr.toFixed(1), tb: r.tb.toFixed(1), bm: r.bm, fix: r.fix && r.fix.sides, aspect: r.aspect.toFixed(3) }));
  expect('rim: outline re-fitted on the right', !!r.fix && /right in/.test(r.fix.sides.join(',')));
  expect('rim: borders back to 2 mm, 50/50', near(r.bm.r, 2, .4) && near(r.lr, 50, 4));
  expect('rim: outline check warns', r.checks.some((c) => c === 'Card outline re-fitted:warn'));
  // 3. black border on a black mat: the outer edge is invisible, the tool must say so
  r = await p.evaluate(SCENE, { mat: '#141414', border: '#121212', bl: 2, br: 2, bt: 2, bb: 2, rot: 0 });
  console.log('   dark: ', JSON.stringify({ lr: r.lr.toFixed(1), bm: r.bm, fix: r.fix && r.fix.sides, aspect: r.aspect.toFixed(3), checks: r.checks }));
  expect('dark: flagged (card edge not found or outline off)', r.checks.some((c) => /Card edge not found:bad|Card outline off:bad|Card edge unverified:warn|Picture edge uncertain:warn|Picture edge not found:warn/.test(c)));
  // 4. off-centre: 1 mm left, 3 mm right, 1.5 top, 2.5 bottom
  r = await p.evaluate(SCENE, { mat: '#303030', border: '#ffffff', bl: 1, br: 3, bt: 1.5, bb: 2.5, rot: -2 });
  console.log('   off:  ', JSON.stringify({ lr: r.lr.toFixed(1), tb: r.tb.toFixed(1), bm: r.bm, fix: r.fix && r.fix.sides, aspect: r.aspect.toFixed(3) }));
  expect('off-centre: 25/75 and 37/63 within 4 points, no re-fit', near(r.lr, 25, 4) && near(r.tb, 37.5, 4) && !r.fix);
  // 5. shot at an angle: 10% keystone, the fix must leave a correct outline alone
  r = await p.evaluate(SCENE, { mat: '#262626', border: '#f2f2f2', bl: 2, br: 2, bt: 2, bb: 2, rot: 1, key: .10 });
  console.log('   key:  ', JSON.stringify({ lr: r.lr.toFixed(1), tb: r.tb.toFixed(1), bm: r.bm, fix: r.fix && r.fix.sides, aspect: r.aspect.toFixed(3), checks: r.checks.filter((c) => /outline|Straight|Corrected/.test(c)) }));
  expect('keystone: no re-fit, borders within 0.5 mm, no outline flag', !r.fix && near(r.bm.l, 2, .5) && near(r.bm.r, 2, .5) && near(r.lr, 50, 4) && near(r.tb, 50, 6) && r.checks.some((c) => c === 'Card outline:ok'));
  // 6. a chrome card: 1 mm silver pinstripe border, dark mat, toploader rim showing 70 px on the right, slight tilt
  r = await p.evaluate(SCENE, { mat: '#1e1e1e', border: '#c4c4c4', bl: 1, br: 1, bt: 1, bb: 1, rot: 1.5, rim: '#9a9a9a', rimRight: 70 });
  console.log('   chrome:', JSON.stringify({ lr: r.lr.toFixed(1), tb: r.tb.toFixed(1), bm: r.bm, fix: r.fix && r.fix.sides, aspect: r.aspect.toFixed(3) }));
  expect('chrome in toploader: re-fitted, 1 mm borders within 0.35, 50/50 within 5', !!r.fix && near(r.bm.l, 1, .35) && near(r.bm.r, 1, .35) && near(r.lr, 50, 5) && near(r.tb, 50, 5));
  expect('no page errors', errs.length === 0); if (errs.length) console.log(errs);
  await b.close(); console.log(bad ? 'PG FAILED' : 'PG OK'); process.exit(bad ? 1 : 0);
})();
