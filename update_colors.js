
const updateColor = (property, color) => {
    if (color && property) {
        document.documentElement.style.setProperty(property, color);
    }
};

