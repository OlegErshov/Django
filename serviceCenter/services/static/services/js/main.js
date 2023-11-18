const banners = document.querySelectorAll('.circular-image');

let curBanner = 0;
let rotationInterval;

function displayCurBanner(curIndex) {
    console.log('Current banner: ' + curIndex);
    banners.forEach((banner, i) => {
        if (i === curIndex) {
            banner.style.display = 'flex';
        } else {
            banner.style.display = 'none';
        }
    });
}

function rotate() {
    const interval = milliseconds;
    rotationInterval = setInterval(() => {
        if (document.hasFocus()) {
            curBanner = (curBanner + 1) % banners.length;
            displayCurBanner(curBanner);
        }
    }, interval);
}


displayCurBanner(curBanner);
rotate();
