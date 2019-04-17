// ==========================================================
// ==================== Work in progress ====================
// ==========================================================

// var lfComponent = document.querySelector('.lf-component');
// var boardsContainer = document.querySelectorAll('.board-container');

// lfComponent.addEventListener('dragstart', dragStart);
// lfComponent.addEventListener('dragend', dragEnd);

// function dragStart(ev) {
//     ev.dataTransfer.setData("text/plain", ev.target.id);
//     // ev.dataTransfer.setDragImage(this, 0, 0);
//     this.className += ' hold';
//     // setTimeout(() => {
//     //     this.className = 'invisible'
//     // }, 0);
// }

// function dragEnd() {

// }




// var active = false;
// var currentX;
// var currentY;
// var initialX;
// var initialY;
// var xOffset = 0;
// var yOffset = 0;

// lfComponent.addEventListener("touchstart", dragStart, false);
// lfComponent.addEventListener("touchend", dragEnd, false);
// lfComponent.addEventListener("touchmove", drag, false);

// lfComponent.addEventListener("mousedown", dragStart, false);
// lfComponent.addEventListener("mouseup", dragEnd, false);
// lfComponent.addEventListener("mousemove", drag, false);

// function dragStart(e) {
//     if (e.type === "touchstart") {
//         initialX = e.touches[0].clientX - xOffset;
//         initialY = e.touches[0].clientY - yOffset;
//     } else {
//         initialX = e.clientX - xOffset;
//         initialY = e.clientY - yOffset;
//     }

//     if (e.target === lfComponent || e.target.parentNode === lfComponent) {
//         active = true;
//     }
// }

// function dragEnd(e) {
//     initialX = 0;
//     initialY = 0;
//     currentX = 0;
//     currentY = 0;
//     xOffset = 0;
//     yOffset = 0;

//     setTranslate(0, 0, lfComponent);


//     active = false;
// }

// function drag(e) {
//     if (active) {

//         e.preventDefault();

//         if (e.type === "touchmove") {
//             currentX = e.touches[0].clientX - initialX;
//             currentY = e.touches[0].clientY - initialY;
//         } else {
//             currentX = e.clientX - initialX;
//             currentY = e.clientY - initialY;
//         }

//         xOffset = currentX;
//         yOffset = currentY;

//         setTranslate(currentX, currentY, lfComponent);
//     }

// }

// function setTranslate(xPos, yPos, el) {
//     el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
// }