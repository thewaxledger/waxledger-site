// Resolves Playwright from the project if installed, else from the environment's global tools.
module.exports = (() => { try { return require('playwright'); } catch (e) { return require('/opt/npm-tools/node_modules/playwright'); } })();
