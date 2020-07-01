// Attribution:

function resize() {
    if (window.innerWidth <= 800) {
        console.log('set to 4');
        document.getElementById('blurFilter').setAttribute('stdDeviation', 4);
    } else {
        console.log('set to 10');
        document.getElementById('blurFilter').setAttribute('stdDeviation', 8);
    }
}

window.addEventListener("resize", resize);
document.addEventListener("DOMContentLoaded", resize);
