const fs = require('fs');
const puppeteer = require('puppeteer');

(async () => {
    const htmlFile = '/home/coder/index.html'
    if (!fs.existsSync(htmlFile)) {
        console.log("Fichier index.html introuvable.");
        process.exit(1);
    }
    const browser = await puppeteer.launch({headless: true});
    const page = await browser.newPage();

    await page.goto('file://'+htmlFile);
    //Récupère la console JS
    const logs = [];
    page.on('console', msg => logs.push(msg.text()));
    //Attend que la page soit chargée
    await page.waitForTimeout(500);
    //Capture un rendu sous forme de texte
    const content = await page.content();
    await browser.close()

    console.log("=== Rendu HTML ===");
    console.log(content);
    console.log("=== Logs Console ===");
    console.log(logs.join("\n"));
})();