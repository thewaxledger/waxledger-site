// PSA pull helper for the Raw-to-Gem pipeline. Paste into the browser pane's console (or run with the pane's
// JavaScript tool) on any https://www.psacard.com/ page, then:
//   await srch('2019 topps chrome fernando tatis 203')   -> [[item name, specId], ...]  (50 results max; be specific)
//   await specName('2806015')                            -> set and card name for a specId, to confirm the match
//   await pull('2806015')                                -> one psa-N.json entry, with asOf set to today
// Worked out Oct 11, 2026 against the site's own tRPC endpoints (the ones the /spec/psa/<id> page calls):
//   getPriceSummary    timeRange is in MONTHS (3 = last 90 days; 0 = all time). Checked by counting paged sales.
//   getSalesBySpecId   pageSize max 5, cursor is the page number, grade is a string; its timeRange is ignored,
//                      so sales are cut at 90 days here by date.
//   getPopulationSummary  grade10/grade9/grade8 totalCount, total.totalCount, gemRate.
// Medians use the newest 50 PSA 10 sales, 25 PSA 9 sales and 15 ungraded sales inside the 90 days.
const TODAY = new Date().toISOString().slice(0, 10);
window.trpc = async (proc, json) => {
  const u = '/api/psa/trpc/' + proc + '?batch=1&input=' + encodeURIComponent(JSON.stringify({ 0: btoa(JSON.stringify({ json })) }));
  const r = await fetch(u); const t = await r.text();
  try { return JSON.parse(t)[0]; } catch (e) { return { err: r.status, t: t.slice(0, 300) }; }
};
window.srch = async (q) => {
  const h = await fetch('/auctionprices/search?q=' + encodeURIComponent(q)).then((r) => r.text());
  const d = new DOMParser().parseFromString(h, 'text/html');
  return [...d.querySelectorAll('a[href^="/spec/psa/"]')].map((a) => [a.textContent.trim(), a.getAttribute('href').split('/').pop()]);
};
window.specName = async (id) => {
  const h = await fetch('/spec/psa/' + id).then((r) => r.text());
  const m = new DOMParser().parseFromString(h, 'text/html').querySelector('main');
  const t = (m ? m.textContent : '').replace(/\s+/g, ' '); const i = t.indexOf('Search a player');
  return t.slice(0, i > 0 ? i : 160);
};
window.pull = async (specId) => {
  const med = (a) => { const s = a.slice().sort((x, y) => x - y); const m = s.length >> 1; return s.length ? (s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2) : null; };
  const r2 = (x) => (x == null ? null : Math.round(x * 100) / 100);
  const cut = new Date(new Date(TODAY + 'T23:59:59Z') - 90 * 864e5);
  const sum = await trpc('researchJourney.getPriceSummary', { specId, department: 'psa', salesSummaryType: 'GRADES', gradingType: 'ALL', qualifiers: 'NON_QUALIFIERS', timeRange: 3 });
  const ss = sum.result.data.json.salesSummary; const g = (n) => (ss.find((s) => s.grade === n) || { metrics: {} }).metrics;
  const page = async (input, maxN) => {
    const out = [];
    for (let c = 1; out.length < maxN && c <= Math.ceil(maxN / 5) + 1; c++) {
      const s = await trpc('researchJourney.getSalesBySpecId', { specId, gradingType: 'ALL', pageSize: 5, timeRange: 0, cursor: c, ...input });
      if (!s.result) break;
      const j = s.result.data.json; let stop = false;
      for (const x of j.sales) { if (new Date(x.saleDate) < cut) { stop = true; break; } out.push(x); }
      if (stop || !j.hasNextPage) break;
    }
    return out.slice(0, maxN);
  };
  const s10 = await page({ grade: '10', qualifiers: 'NON_QUALIFIERS', direction: 'forward' }, 50);
  const s9 = await page({ grade: '9', qualifiers: 'NON_QUALIFIERS', direction: 'forward' }, 25);
  const raw = await page({ gradingCompany: ['UNGRADED'], qualifiers: 'ALL' }, 15);
  const pop = (await trpc('researchJourney.getPopulationSummary', { specId, department: 'psa', filter: 'all' })).result.data.json;
  const cnt = (k) => (pop[k] ? pop[k].totalCount : 0); const pr = (a) => a.map((x) => x.salePrice);
  return {
    specId, n10: g(10).quantity || 0, avg10: r2(g(10).averagePrice), med10: r2(med(pr(s10))), min10: g(10).minimumPrice ?? null, max10: g(10).maximumPrice ?? null,
    latest10: s10[0] ? s10[0].salePrice : null, medN10: s10.length, old10: s10.length ? s10.at(-1).saleDate.slice(0, 10) : null, new10: s10.length ? s10[0].saleDate.slice(0, 10) : null,
    n9: g(9).quantity || 0, avg9: r2(g(9).averagePrice), med9: r2(med(pr(s9))), medN9: s9.length,
    rawN: raw.length, rawMed: r2(med(pr(raw))), rawLast: raw[0] ? raw[0].salePrice : null, rawOldest: raw.length ? raw.at(-1).saleDate.slice(0, 10) : null,
    rawMin: raw.length ? Math.min(...pr(raw)) : null, rawMax: raw.length ? Math.max(...pr(raw)) : null,
    pop10: cnt('grade10'), pop9: cnt('grade9'), pop8: cnt('grade8'), popTotal: pop.total.totalCount, gemRate: pop.gemRate, asOf: TODAY,
  };
};
// Pop-report search (the APR search misses most base cards). JSONP, so it needs no jQuery; works on any psacard.com
// page. Returns [{specid, description}]. One term at a time with a pause; some terms error (see CLAUDE.md).
window.popSearch = (term) => new Promise((res, rej) => {
  const cb = 'psacb' + Date.now() + Math.floor(Math.random() * 1e6); const s = document.createElement('script');
  window[cb] = (d) => { delete window[cb]; s.remove(); res(Array.isArray(d) ? d : (d && d.d) || []); };
  s.onerror = () => { delete window[cb]; s.remove(); rej(new Error('popSearch failed: ' + term)); };
  s.src = 'https://www.collectorsuniverse.com/specsearch/search/psaformatted?callback=' + cb + '&term=' + encodeURIComponent(term) + '&includePopOnly=true&mandatoryAdditionalTerms=';
  document.head.appendChild(s);
});
// Run a candidate list (candidates.js CANDS_NOV1 shape: key, term, must[], not[]): search, keep the first spec whose
// description carries every `must` token and no `not` token, pull it. Returns {key: entry|{err}} and logs as it goes.
// Call with a slice of 3 to 5 at a time and copy the result out: the pane can drop mid-run.
window.runCands = async (list, pause = 1500) => {
  const out = {};
  for (const c of list) {
    try {
      const hits = await popSearch(c.term);
      const ok = hits.filter((h) => { const d = (h.description || '').toLowerCase(); return (c.must || []).every((m) => d.includes(m)) && !(c.not || []).some((n) => d.includes(n)); });
      if (!ok.length) { out[c.key] = { err: 'no spec', seen: hits.slice(0, 8).map((h) => h.specid + ' ' + h.description) }; console.log(c.key, 'no spec'); continue; }
      const e = await pull(String(ok[0].specid)); e.desc = ok[0].description; out[c.key] = e;
      console.log(c.key, ok[0].specid, ok[0].description, 'n10', e.n10, 'med10', e.med10, 'gem', e.gemRate);
    } catch (err) { out[c.key] = { err: String(err) }; console.log(c.key, 'ERR', String(err)); }
    await new Promise((r) => setTimeout(r, pause));
  }
  return out;
};
