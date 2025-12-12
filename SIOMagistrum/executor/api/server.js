const express = require('express');
const { exec } = require('child_process');
const fs = require('fs').promises;
const path = require('path');
const {v4: uuidv4} = require('uuid');
const { error } = require('console');
const { stdout, stderr, exitCode } = require('process');

const app = express();
app.use(express.json({limit: '10mb'}));

const TIMEOUT = 10000
const TEMP_DIR = path.join(__dirname, 'temp');

const ENV_CONFIG = {
    html: {
        image: 'runner-html',
        buildPath: './environments/html'
    },
    javascript: {
        image: 'runner-js',
        buildPath: './environments/javascript'
    },
    php: {
        image: 'runner-php',
        buildPath: './environments/php'
    },
    java: {
        image: 'runner-java',
        buildPath: './environments/java'
    },
    python: {
        image: 'runner-puthon',
        buildPath: './environments/python'
    }
};

fs.mkdir(TEMP_DIR, {recursive: true});

app.post('/execute', async (req, res) => {
    const { language, code, files} = req.body;

    if (!language || !ENV_CONFIG[language]) {
        return res.status(400).json({error: 'Langage non supporté'});
    }

    const sessionId = uuidv4();
    const sessionDir = path.join(TEMP_DIR, sessionId);

    try {
        await fs.mkdir(sessionDir, {recursive: true});

        if (language == 'html') {
            await fs.writeFile(path.join(sessionDir, 'index.html'), code);
            if (files?.css) {
                await fs.writeFile(path.join(sessionDir, 'style.css'), files.css);
            }
            if (files?.js) {
                await fs.writeFile(path.join(sessionDir, "index.js"), files.js);
            }
        } else if (language == 'javascript') {
            await fs.writeFile(path.join(sessionDir, 'main.js'), code);
        } else if (language == 'php') {
            await fs.writeFile(path.join(sessionDir, 'main.php'), code);
        } else if (language == 'java') {
            await fs.writeFile(path.join(sessionDir, 'Main.java'), code);
        } else if (language == 'python') {
            await fs.writeFile(path.join(sessionDir, 'main.py'), code);
        }

        const res = await executeInDocker(language, sessionDir, sessionId);

        res.json(result);
    } catch (error) {
        res.status(500).json({
            error: error.message,
            stdout: '',
            stderr: error.message
        });
    } finally {
        setTimeout(async () => {
            try {
                await fs.rm(sessionDir, {recursive: true, force: true});
            } catch (e) {
                console.error('Erreur nettoyage:', e);
            }
        }, 5000);
    }
});

async function executeInDocker(language, sessionDir, sessionId) {
    const config = ENV_CONFIG[language];

    return new Promise((resolve, reject) => {
        const cmd = `docker run --rm \
            --name exec-${sessionId} \
            --memory="128m" \
            --cpus="0.5" \
            --network="none" \
            --read-only \
            --tmpfs /tmp \
            -v "${sessionDir}:/code:ro" \
            ${config.image}`;
        
        const timeout = setTimeout(() => {
            exec(`docker kill exec-${sessionId}`, () => {});
            reject(new Error('Timeout: exécution trop longue'));
        }, TIMEOUT);

        exec(cmd, {timeout: TIMEOUT}, (error, stdout, stderr) => {
            clearTimeout(timeout);

            resolve({
                stdout: stdout || '',
                stderr: stderr || '',
                exitCode: error ? error.code : 0,
                success: !error || error.code === 0
            });
        });
    });
}

app.post('/build-images', async (req, res) => {
    try {
        const results = {};
        for (const [lang, config] of Object.entries(ENV_CONFIG)) {
            const cmd = `docker build -t ${config.image} ${config.buildPath}`;

            await new Promise((resolve, reject) => {
                exec(cmd, (error, stdout, stderr) => {
                    if (error) {
                        results[lang] = {success: false, error: stderr};
                        reject(error);
                    } else {
                        results[lang] = {success: true};
                        resolve();
                    }
                });
            });
        }

        res.json({message: 'Images construites', results});
    } catch (error) {
        res.status(500).json({error: error.message});
    }
});

app.get('/health', (req, res) => {
    res.json({status: 'ok'});
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`API d'exécution de code sur le port ${PORT}`);
});