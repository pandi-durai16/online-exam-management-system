// Total exam time (passed from exam.html)
let totalTime = EXAM_TIME; // seconds

function startTimer() {
    const timeText = document.getElementById("time");
    const timerBox = document.getElementById("timer");

    const interval = setInterval(() => {
        let minutes = Math.floor(totalTime / 60);
        let seconds = totalTime % 60;

        timeText.innerText =
            minutes.toString().padStart(2, "0") + ":" +
            seconds.toString().padStart(2, "0");

        // Warning when last 1 minute
        if (totalTime <= 60) {
            timerBox.style.backgroundColor = "#fdecea";
            timerBox.style.color = "#c62828";
        }

        // Time up → auto submit
        if (totalTime <= 0) {
            clearInterval(interval);
            alert("Time is up! Exam will be submitted automatically.");
            document.forms[0].submit();
        }

        totalTime--;
    }, 1000);
}

window.onload = startTimer;
