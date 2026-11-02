// Renders the brand assets in assets.html to PNG files in the Brand folder.
// Run: node render.mjs   (uses the Playwright install in the coredile-pos project)
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "/Users/tbsuser/Desktop/coredile-pos/node_modules/playwright/index.mjs";

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.resolve(here, "..");

const shots = [
  ["#avatar", "Profile picture 800x800.png", false],
  ["#banner", "Banner 2560x1440.png", false],
  ["#watermark", "Video watermark 150x150.png", true],
  ["#wordmark", "Logo with name 1600x400.png", true],
];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 2600, height: 1500 }, deviceScaleFactor: 1 });
await page.goto("file://" + path.join(here, "assets.html"));
await page.evaluate(() => document.fonts.ready);
for (const [selector, name, transparent] of shots) {
  await page.locator(selector).screenshot({ path: path.join(out, name), omitBackground: transparent });
  console.log("wrote", name);
}
await browser.close();
