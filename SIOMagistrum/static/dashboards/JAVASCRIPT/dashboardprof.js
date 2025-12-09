document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modalCours');
    const btn = document.getElementById('openModal');
    const span = document.querySelector('.modal .close');

    // Ouvrir le modal
    if (btn) {
        btn.addEventListener('click', () => {
            modal.style.display = 'block';
        });
    }

    // Fermer le modal en cliquant sur la croix
    if (span) {
        span.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    // Fermer le modal en cliquant en dehors
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
