const filters = ['internal', 'external'];
var active = document.getElementsByClassName("show-all")[0];

function setActive(btn) {
    btn.style.background = "linear-gradient(to right, var(--color1-first) 0%, var(--color1-second) 100%)";
    btn.style.outline = "none";
    btn.style.outline = "none";
}

function unsetActive(btn) {
    btn.style.background = "var(--background-second)";
    btn.style.outline = "none";
}


filters.forEach(element => {
    const btn = document.getElementsByClassName(element)[0];
    btn.addEventListener("click", () => {
        unsetActive(active);
        active = btn;
        setActive(active);

        listItems = document.getElementsByClassName('resources-item');

        for (i = 0; i < listItems.length; i++) {
            itemFilterType = listItems[i].getAttribute('data-type');

            if (itemFilterType === element) {
                listItems[i].style.display = "";
            } else {
                listItems[i].style.display = "none";
            }
        }
    });
});

const btnShowAll = document.getElementsByClassName("show-all")[0];
setActive(btnShowAll);
btnShowAll.addEventListener("click", () => {
    unsetActive(active);
    active = btnShowAll;
    setActive(active);
    listItems = document.getElementsByClassName('resources-item');
    for (i = 0; i < listItems.length; i++) {
        listItems[i].style.display = "";
    }
});