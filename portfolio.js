const timeElement = document.querySelector(".time");
const dateElement = document.querySelector(".date");

function formatTime(date) {
    const hours12 = date.getHours() % 12 || 12;
    const minutes = date.getMinutes();
    const isAm = date.getHours() < 12;

    // 9 => 09
    return `${hours12.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')} ${isAm ? 'AM' : 'PM'}`;
}

setInterval(() => {
    const now = new Date();

    timeElement.textContent = formatTime(now);
}, 200);