document.addEventListener('DOMContentLoaded', () => {

    /* ----------------------------- */
    /*  MODAL AJOUT MODULE           */
    /* ----------------------------- */

    const modalAjoutModule = document.getElementById('modalAjoutModule');
    const btnAddModule = document.getElementById('addModule');
    const closeAddBtn = modalAjoutModule.querySelector('.close-add');

    btnAddModule.addEventListener('click', () => {
        modalAjoutModule.style.display = 'flex';
        modalAjoutModule.querySelector('form').reset();
        modalAjoutModule.querySelector('form').action =
            `/dashboard/professeur/module/add/${modalAjoutModule.dataset.cours}/`;
    });

    closeAddBtn.addEventListener('click', () => {
        modalAjoutModule.style.display = 'none';
        modalAjoutModule.querySelector('form').reset();
    });


    /* ----------------------------- */
    /*  MODAL EDIT MODULE            */
    /* ----------------------------- */

    const modalEditModule = document.getElementById('modalEditModule');
    const closeEditModuleBtn = modalEditModule.querySelector('.close-edit');

    const editTitre = document.getElementById('edit_titre_module');
    const editDesc = document.getElementById('edit_description_module');
    const editOrdre = document.getElementById('edit_ordre_module');
    const editForm = modalEditModule.querySelector('form');

    const modifyBtnsModule = document.querySelectorAll('.btn-modify');

    modifyBtnsModule.forEach(btn => {
        btn.addEventListener('click', e => {
            e.preventDefault();
            e.stopPropagation();

            editTitre.value = btn.dataset.titre;
            editDesc.value = btn.dataset.description;
            editOrdre.value = btn.dataset.ordre;

            const moduleId = btn.dataset.id;
            editForm.action = `/dashboard/professeur/module/modify/${moduleId}/`;

            modalEditModule.style.display = 'flex';
        });
    });

    closeEditModuleBtn.addEventListener('click', () => {
        modalEditModule.style.display = 'none';
        editForm.reset();
    });

    /* ----------------------------- */
    /*  FERMETURE CLIQUE EXTERIEUR   */
    /* ----------------------------- */

    window.addEventListener('click', e => {
        if (e.target === modalAjoutModule) {
            modalAjoutModule.style.display = 'none';
        }

        if (e.target === modalEditModule) {
            modalEditModule.style.display = 'none';
        }
    });
});
