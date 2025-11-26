document.addEventListener('DOMContentLoaded', function () {
    const select = document.querySelector('.select-multiple');
    const zone = document.getElementById('zone-affichage');

    if (select) {
        select.addEventListener('change', function () {
            const valeurs = Array.from(select.selectedOptions).map(opt => opt.textContent);
            zone.textContent = valeurs.join(", ");
        });
    }
});