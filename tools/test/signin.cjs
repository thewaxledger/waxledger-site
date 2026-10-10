// Signs the page in through the site's own forms. Tries the password form first; if the address has no password yet
// (fresh stub store), falls back to the emailed-code flow and sets one.
const B = 'http://localhost:8791';
const lastCode = async (p, email) => { const m = await (await p.request.get(B + '/__mail')).json(); const x = m.filter(o => o.to === email).pop(); return (x.subject.match(/(\d{6})/) || [])[1]; };
module.exports = async function signIn(p, email, password = 'test-password-1', name = 'Tester') {
  if (!/#trade$/.test(p.url())) { await p.goto(B + '/#trade'); await p.waitForTimeout(400); }
  await p.click('#hdr-signin');
  await p.fill('#auth-login-email', email); await p.fill('#auth-login-pw', password); await p.click('#auth-login-form button[type=submit]');
  const ok = await p.waitForSelector('#bst-board:not([hidden])', { timeout: 4000 }).then(() => true).catch(() => false);
  if (ok) return;
  if (await p.$('#auth-forgot')) await p.click('#auth-forgot');
  await p.fill('#auth-email', email); await p.click('#auth-email-btn');
  await p.waitForSelector('#auth-code-form:not([hidden])', { timeout: 5000 });
  await p.fill('#auth-code', await lastCode(p, email)); await p.click('#auth-code-form button[type=submit]');
  const pw = await p.waitForSelector('#auth-pw-form:not([hidden])', { timeout: 4000 }).then(() => true).catch(() => false);
  if (pw) { await p.fill('#auth-pw', password); await p.fill('#auth-pw2', password); await p.click('#auth-pw-form button[type=submit]'); }
  const nm = await p.waitForSelector('#auth-name-form:not([hidden])', { timeout: 4000 }).then(() => true).catch(() => false);
  if (nm) { await p.fill('#auth-name', name); await p.click('#auth-name-form button[type=submit]'); }
  await p.waitForSelector('#bst-board:not([hidden])', { timeout: 8000 });
};
