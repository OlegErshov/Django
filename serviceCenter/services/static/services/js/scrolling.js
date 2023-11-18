var imageElements = document.getElementsByTagName('img');
var lastScrollPosition = document.documentElement.scrollTop;
var degrees = 1;

function isScrollingDown() {
    var scroll = document.documentElement.scrollTop;
    var scrollingDown = scroll > lastScrollPosition;
    lastScrollPosition = scroll;
    return scrollingDown;
}

function rotateImagesOnScroll() {
    isDown = isScrollingDown();
    for (let image of imageElements) {
        degrees += isDown ? 1 : -1;
        image.style.transform = 'rotate(' + degrees + 'deg)';
    }
}

window.addEventListener('scroll', rotateImagesOnScroll);
