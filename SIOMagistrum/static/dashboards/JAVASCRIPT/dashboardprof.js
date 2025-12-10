document.addEventListener('DOMContentLoaded', () => {

    /* ----------------------------- */
    /*  REDIRECTION VERS DETAILS     */
    /* ----------------------------- */
    document.querySelectorAll('.carte-cours').forEach(card => {
        card.addEventListener('click', e => {
            if (!e.target.closest('.btn-modify')) { // ignore si on clique sur le bouton
                const url = card.dataset.href;
                if (url) window.location.href = url;
            }
        });
    });

    /* ----------------------------- */
    /*  MODAL D’AJOUT DE COURS       */
    /* ----------------------------- */

    const modalAjout = document.getElementById('modalAjoutCours');
    const openAjoutBtn = document.getElementById('openModal');
    const closeAjoutBtn = modalAjout.querySelector('.close');

    if (openAjoutBtn) {
        openAjoutBtn.addEventListener('click', () => {
            modalAjout.style.display = 'block';
        });
    }

    closeAjoutBtn.addEventListener('click', () => {
        modalAjout.style.display = 'none';
        modalAjout.querySelector('form').reset();
    });


    /* ----------------------------- */
    /*  MODAL DE MODIFICATION        */
    /* ----------------------------- */

    const modalEdit = document.getElementById('modalEditCours');
    const closeEditBtn = modalEdit.querySelector('.close-edit');

    const editTitre   = modalEdit.querySelector('#edit_titre');
    const editMatiere = modalEdit.querySelector('#edit_matiere');
    const editType    = modalEdit.querySelector('#edit_type_cours');
    const editIconPrev = modalEdit.querySelector('#edit_icon_preview');
    const editBanPrev  = modalEdit.querySelector('#edit_banniere_preview');
    const editCoursId  = modalEdit.querySelector('#edit_cours_id');
    const editForm     = modalEdit.querySelector('form');

    const modifyBtns = document.querySelectorAll('.btn-modify');

    modifyBtns.forEach(btn => {
        btn.addEventListener('click', e => {
            e.preventDefault();
            const courseId = btn.dataset.id;

            editTitre.value = btn.dataset.titre;
            editMatiere.value = btn.dataset.matiere;
            editType.value = btn.dataset.type;

            editIconPrev.src = btn.dataset.icon || "/static/dashboards/ASSETS/ICONPLACEHOLDER.png";
            editBanPrev.src  = btn.dataset.banniere || "/static/dashboards/ASSETS/BANNERPLACEHOLDER.png";

            // Identifiant caché
            editCoursId.value = courseId;

            editForm.action = `/dashboard/professeur/modify/${courseId}/`;

            modalEdit.style.display = 'block';
        });
    });

    closeEditBtn.addEventListener('click', () => {
        modalEdit.style.display = 'none';
        editForm.reset();
    });

    editForm.action = `/dashboard/professeur/modify/${courseId}/`;
    /* ----------------------------- */
    /*  FERMETURE CLICK EXTERIEUR    */
    /* ----------------------------- */

    window.addEventListener('click', e => {
        if (e.target === modalAjout) {
            modalAjout.style.display = 'none';
            modalAjout.querySelector('form').reset();
        }
        if (e.target === modalEdit) {
            modalEdit.style.display = 'none';
            editForm.reset();
        }
    });
});
