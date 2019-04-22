
const filters = ["filter1", "filter2", "filter3", "filter4"];
var active = document.getElementsByClassName("show-all")[0];

function setActive(btn) {
    btn.style.color = "var(--medium-dark-color)";
    btn.style.backgroundColor = "var(--light-medium-color)";
}

function unsetActive(btn) {
    btn.style.color = "var(--light-color)";
    btn.style.backgroundColor = "var(--medium-dark-color)";
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