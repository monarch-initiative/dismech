/**
 * Take screenshots of pathograph visualizations from rendered disorder pages.
 * Injects local copies of D3/dagre since CDN may be unreachable from headless browser.
 * Usage: node scripts/screenshot_pathograph.js
 */
let chromium;
try {
    chromium = require('/opt/node22/lib/node_modules/playwright').chromium;
} catch (e) {
    chromium = require('playwright').chromium;
}
const fss = require('fs');
const path = require('path');

const PAGES = [
    { file: 'Asthma.html', name: 'asthma' },
    { file: 'Sickle_Cell_Disease.html', name: 'sickle_cell' },
    { file: 'Ehlers-Danlos_Syndrome.html', name: 'ehlers_danlos' },
];

const OUTPUT_DIR = path.join(__dirname, '..', 'docs', 'images');
const PAGES_DIR = path.join(__dirname, '..', 'pages', 'disorders');
const D3_PATH = '/tmp/d3.v7.min.js';
const DAGRE_PATH = '/tmp/dagre.min.js';

async function main() {
    fss.mkdirSync(OUTPUT_DIR, { recursive: true });

    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
        viewport: { width: 1400, height: 900 },
        deviceScaleFactor: 2,
    });

    // Block CDN requests and serve local copies instead
    await context.route('**/d3.v7.min.js', async (route) => {
        const body = fss.readFileSync(D3_PATH);
        await route.fulfill({ contentType: 'application/javascript', body });
    });
    await context.route('**/dagre.min.js', async (route) => {
        const body = fss.readFileSync(DAGRE_PATH);
        await route.fulfill({ contentType: 'application/javascript', body });
    });

    for (const { file, name } of PAGES) {
        const filePath = path.join(PAGES_DIR, file);
        if (!fss.existsSync(filePath)) {
            console.log(`Skipping ${file} - not found`);
            continue;
        }

        const page = await context.newPage();
        await page.goto(`file://${filePath}`, { waitUntil: 'networkidle' });
        await page.waitForTimeout(2000);

        const d3ok = await page.evaluate(() => typeof d3 !== 'undefined');
        const nodeCount = await page.evaluate(() =>
            document.querySelectorAll('#pathograph-svg .pg-nodes > g').length);
        console.log(`  ${name}: D3=${d3ok} nodes=${nodeCount}`);

        // Scroll to pathograph
        await page.evaluate(() => {
            const el = document.getElementById('pathograph');
            if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
        });
        await page.waitForTimeout(500);

        // Screenshot the pathograph card
        const card = await page.evaluateHandle(() => {
            const el = document.getElementById('pathograph');
            return el ? el.closest('.card') : null;
        });
        if (card && card.asElement()) {
            await card.asElement().screenshot({
                path: path.join(OUTPUT_DIR, `pathograph_${name}.png`),
            });
            console.log(`  Captured: pathograph_${name}.png`);
        } else {
            console.log(`  No pathograph card in ${file}`);
        }

        // Tooltip screenshot
        if (nodeCount > 0) {
            const targetIdx = Math.min(1, nodeCount - 1);
            const nodeLocator = page.locator('#pathograph-svg .pg-nodes > g').nth(targetIdx);
            await nodeLocator.hover({ force: true });
            await page.waitForTimeout(600);

            const tooltipVisible = await page.evaluate(() => {
                const tt = document.getElementById('pathograph-tooltip');
                return tt && tt.style.opacity === '1';
            });
            if (tooltipVisible) {
                const cardEl = await page.evaluateHandle(() => {
                    const el = document.getElementById('pathograph');
                    return el ? el.closest('.card') : null;
                });
                if (cardEl && cardEl.asElement()) {
                    await cardEl.asElement().screenshot({
                        path: path.join(OUTPUT_DIR, `pathograph_${name}_tooltip.png`),
                    });
                    console.log(`  Captured: pathograph_${name}_tooltip.png`);
                }
            } else {
                console.log(`  Tooltip not visible after hover`);
            }
            await page.mouse.move(0, 0);
            await page.waitForTimeout(300);
        }

        // Click-highlight screenshot (asthma only)
        if (name === 'asthma' && nodeCount > 0) {
            const nodeLocator = page.locator('#pathograph-svg .pg-nodes > g').first();
            await nodeLocator.click({ force: true });
            await page.waitForTimeout(600);

            const cardEl = await page.evaluateHandle(() => {
                const el = document.getElementById('pathograph');
                return el ? el.closest('.card') : null;
            });
            if (cardEl && cardEl.asElement()) {
                await cardEl.asElement().screenshot({
                    path: path.join(OUTPUT_DIR, `pathograph_${name}_highlight.png`),
                });
                console.log(`  Captured: pathograph_${name}_highlight.png`);
            }
        }

        // Full page overview (asthma only)
        if (name === 'asthma') {
            await page.mouse.click(10, 10);
            await page.waitForTimeout(300);
            await page.evaluate(() => window.scrollTo(0, 0));
            await page.waitForTimeout(300);
            await page.screenshot({
                path: path.join(OUTPUT_DIR, 'pathograph_fullpage.png'),
                fullPage: false,
            });
            console.log(`  Captured: pathograph_fullpage.png`);
        }

        await page.close();
    }

    await browser.close();
    console.log(`\nScreenshots saved to ${OUTPUT_DIR}`);
}

main().catch(err => {
    console.error(err);
    process.exit(1);
});
