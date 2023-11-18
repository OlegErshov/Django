   var lastDisplayedTime;
    function displayCountdown(lastDisplayedTime) {
        const countdownElement = document.getElementById('countdown');
        function updateCountdown() {
            const currentTime = new Date().getTime();
            const timeLeft = lastDisplayedTime - currentTime;

            if (timeLeft <= 0) {
                countdownElement.textContent = 'Finished';
            } else {
                const minutes = Math.floor((timeLeft % 3600000) / 60000);
                const seconds = Math.floor((timeLeft % 60000) / 1000);
                countdownElement.textContent = `${minutes}:${seconds}`;
            }
        }

        updateCountdown();
        const intervalId = setInterval(updateCountdown, 1000);

        localStorage.setItem('lastDisplayedTime', lastDisplayedTime);

        window.onbeforeunload = () => {
            clearInterval(intervalId);
        };
    }

    lastDisplayedTime = localStorage.getItem('lastDisplayedTime');

    if (lastDisplayedTime) {
        displayCountdown(Number(lastDisplayedTime));
    } else {
        lastDisplayedTime = new Date().getTime() + 3600000;
        displayCountdown(lastDisplayedTime);
    }