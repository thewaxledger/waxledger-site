// In-page renderer for the house-style social images (same layout as tools/social/make.py), for sites whose page
// can't load our files (Instagram's headers reset window.name; X's CSP blocks fetches). Paste into the page, then
// wlDraw(spec) -> Promise<Blob> (JPEG). spec: {w,h,eyebrow,head:[[text,color]...],para,rows:[{name,sub,val,pos}]}
window.wlDraw = async (S) => {
  const W = S.w || 1080, H = S.h || 1350, P = 80, c = document.createElement('canvas'); c.width = W; c.height = H;
  const x = c.getContext('2d'), F = '"Segoe UI",Inter,"Helvetica Neue",Arial,sans-serif', M = 'Consolas,"DejaVu Sans Mono",monospace';
  const wrap = (t, font, maxW) => { x.font = font; const out = []; let line = ''; for (const w of t.split(' ')) { const tryL = line ? line + ' ' + w : w; if (x.measureText(tryL).width > maxW && line) { out.push(line); line = w; } else line = tryL; } if (line) out.push(line); return out; };
  x.fillStyle = '#111A2B'; x.fillRect(0, 0, W, H); x.fillStyle = '#E3A92B'; x.fillRect(0, 0, W, 14);
  let y = 112; x.fillStyle = '#AEB7C6'; x.font = `25px ${M}`; x.fillText(S.eyebrow.toUpperCase(), P, y);
  y += 22;
  for (const [t, col] of S.head) for (const ln of wrap(t.toUpperCase(), `900 92px ${F}`, W - 2 * P)) { y += 92; x.fillStyle = col; x.font = `900 92px ${F}`; x.fillText(ln, P - 3, y); }
  y += 30;
  if (S.para) for (const ln of wrap(S.para, `31px ${F}`, W - 2 * P)) { y += 44; x.fillStyle = '#D5DBE5'; x.font = `31px ${F}`; x.fillText(ln, P, y); }
  y += 34;
  for (const r of S.rows) {
    x.font = `bold 42px ${F}`; const vw = x.measureText(r.val).width;
    const nl = wrap(r.name, `800 33px ${F}`, W - 2 * P - 44 - vw - 24), rh = 26 + nl.length * 40 + 34;
    if (y + rh > H - 140) break; // never run into the footer
    x.fillStyle = '#1C283C'; x.fillRect(P, y, W - 2 * P, rh);
    let ty = y + 16; for (const ln of nl) { ty += 36; x.fillStyle = '#fff'; x.font = `800 33px ${F}`; x.fillText(ln, P + 22, ty); }
    x.fillStyle = '#AEB7C6'; x.font = `21px ${M}`; x.fillText(r.sub, P + 22, ty + 34);
    x.fillStyle = r.pos ? '#4CC38A' : '#F08A78'; x.font = `900 42px ${F}`; x.fillText(r.val, W - P - 22 - vw, y + rh / 2 + 15);
    y += rh + 12;
  }
  x.fillStyle = '#E3A92B'; x.font = `900 52px ${F}`; x.fillText('WAX LEDGER', P, H - 78);
  x.fillStyle = '#AEB7C6'; x.font = `26px ${M}`; const u = 'thewaxledger.com'; x.fillText(u, W - P - x.measureText(u).width, H - 82);
  return await new Promise((r) => c.toBlob(r, 'image/jpeg', 0.92));
};
window.WL_SPEC_18 = {
  eyebrow: 'Raw-to-Gem Calculator · PSA APR + pop, Nov 12',
  head: [['580 cards screened.', '#FFFFFF'], ['18 clear the fee.', '#E3A92B']],
  para: 'Raw price from eBay sold, PSA 10 and 9 from 90 days of PSA sales, gem rate from the pop report. Expected value is profit per card graded, after fees.',
  rows: [
    { name: 'Stephen Curry 2025-26 Topps Chrome #201 Refractor', sub: 'raw $78 · PSA 10 $790 on 55 sales · 44% gem', val: '+$138 a try', pos: 1 },
    { name: 'Tim Duncan 1997-98 Topps Chrome #115', sub: 'raw $106 · PSA 10 $1,000 on 81 sales · 28% gem', val: '+$116 a try', pos: 1 },
    { name: 'LeBron James 2025-26 Topps Chrome #127 Refractor', sub: 'raw $68 · PSA 10 $820 on 47 sales · 35% gem', val: '+$108 a try', pos: 1 },
    { name: 'Erling Haaland 2019-20 Topps Chrome UCL #74', sub: 'raw $78 · PSA 10 $417 on 46 sales · 50% gem', val: '+$78 a try', pos: 1 },
  ],
};
