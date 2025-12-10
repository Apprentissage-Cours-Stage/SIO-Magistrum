document.addEventListener('DOMContentLoaded', () => {
    const modalModule = document.getElementById('modalModule');
    const btnAddModule = document.getElementById('addModule');
    const closeModal = modalModule.querySelector('.close');

    // ouverture
    btnAddModule.addEventListener('click', () => {
        modalModule.style.display = 'flex'; // utiliser flex ici
    });

    // fermeture par croix
    closeModal.addEventListener('click', () => {
        modalModule.style.display = 'none';
    });

    // fermeture par clic hors du modal
    window.addEventListener('click', e => {
        if (e.target === modalModule) {
            modalModule.style.display = 'none';
        }
    });
});
