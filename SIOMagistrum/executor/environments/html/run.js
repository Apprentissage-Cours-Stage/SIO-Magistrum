const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path')

(async () => {
    const browser = await puppeteer.launch({
        executablePath: '/usr/bin/chromium-browser',
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu'
        ]
    });

    try {
        const page = await browser.newPage();

        page.on('console', msg => {
            const type = msg.type();
            const text = msg.text();
            console.log(`[${type}] ${text}`);
        });

        page.on('pageerror', error => {
            console.error(`[ERROR] ${error.message}`);
        });

        const htmlPath = 'file://code/index.html';
        await page.goto(htmlPath,  {
            waitUntil: 'networkidle0',
            timeout: 5000,
        });

        await page.waitForTimeout(1000);

        const finalHtml = await page.content();

        console.log('\n--- Page chargée avec succès ---');

    } catch (error) {
        console.error('Erreur:', error.message);
        process.exit(1);
    } finally {
        await browser.close();
    }
})