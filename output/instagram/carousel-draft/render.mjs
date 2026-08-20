import { chromium } from "/Users/astronaut/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs";
import { pathToFileURL } from "node:url";
import path from "node:path";

const root = path.resolve(import.meta.dirname);
const browser = await chromium.launch({
  headless: true,
  executablePath: "/Users/astronaut/Library/Caches/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-mac-arm64/chrome-headless-shell",
});
const page = await browser.newPage({ viewport: { width: 1180, height: 1450 }, deviceScaleFactor: 1 });

await page.goto(pathToFileURL(path.join(root, "index.html")).href);
await page.waitForLoadState("networkidle");
await page.evaluate(() => document.fonts.ready);

for (let index = 1; index <= 5; index += 1) {
  const slide = page.locator(`#slide-${index}`);
  await slide.screenshot({ path: path.join(root, `slide-${String(index).padStart(2, "0")}.png`) });
}

await browser.close();
