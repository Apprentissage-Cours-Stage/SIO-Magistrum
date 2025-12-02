document.addEventListener("DOMContentLoaded", function () {
    const select = document.getElementById("matières");
    const container = document.getElementById("tags-container");

    if (!select) {
        console.log("Le select #matieres est introuvable");
        return;
    }

    select.addEventListener("change", () => {
        const selected = select.options[select.selectedIndex];
        const value = selected.value;
        const label = selected.text;

        if ([...container.children].some(tag => tag.dataset.value === value)) {
            select.value = "";
            return;
        }

        const tag = document.createElement("div");
        tag.className = "tag";
        tag.dataset.value = value;
        tag.innerHTML = `
            <span>${label}</span>
            <button type="button">&times;</button>
        `;

        tag.querySelector("button").addEventListener("click", () => tag.remove());

        container.appendChild(tag);
        select.value = "";
    });
});
