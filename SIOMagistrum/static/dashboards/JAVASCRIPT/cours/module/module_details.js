/* ---------------------------------- */
/* MODAL AJOUT EXERCICE (MODULE)      */
/* ---------------------------------- */

document.addEventListener('DOMContentLoaded', () => {
    const modalEx = document.getElementById('modalAjoutExercice');
    const btnAddEx = document.getElementById('addExercice'); 
    const closeExBtn = document.querySelector('.close-ex');

    if (btnAddEx && modalEx) {
        btnAddEx.addEventListener('click', () => {
            modalEx.style.display = 'flex';
            const form = modalEx.querySelector('form');
            if (form) form.reset();
            // Cacher la section code par défaut au reset
            document.getElementById('section-code-test').style.display = 'none';
        });
    }

    if (closeExBtn) {
        closeExBtn.addEventListener('click', () => {
            modalEx.style.display = 'none';
        });
    }

    // Fermeture au clic à l'extérieur
    window.addEventListener('click', (e) => {
        if (e.target === modalEx) {
            modalEx.style.display = 'none';
        }
    });
});

// Affiche ou cache la zone de code selon le type sélectionné
function toggleCodeSection() {
    const typeEx = document.getElementById('type_ex').value;
    const sectionCode = document.getElementById('section-code-test');
    sectionCode.style.display = (typeEx === 'CODE') ? 'block' : 'none';
}

// Fonction AJAX pour tester le code via Django -> Docker
function testerCodeDocker() {
    const btn = document.getElementById('btn-tester-docker');
    const url = btn.getAttribute('data-url'); // RÉCUPÉRATION DE L'URL DEPUIS LE HTML
    
    const code = document.getElementById('code_test').value;
    const consoleBox = document.getElementById('console-resultat');
    const outputText = document.getElementById('output-text');
    const loader = document.getElementById('loader-docker');

    loader.style.display = 'inline-block';
    consoleBox.style.display = 'block';
    outputText.innerText = "Exécution en cours...";
    outputText.className = "";

    fetch(url, { 
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        loader.style.display = 'none';
        outputText.innerText = data.output;
        // Ajout de classes pour la couleur (vert si succès, rouge si erreur)
        outputText.style.color = data.success ? "#2ecc71" : "#e74c3c";
    })
    .catch(error => {
        loader.style.display = 'none';
        outputText.innerText = "Erreur système : Impossible de joindre le serveur Docker.";
        outputText.style.color = "#e74c3c";
    });
}