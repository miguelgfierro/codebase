var elements = document.querySelectorAll('[data-chaffle]');
var elm = document.querySelectorAll('[data-chaffle-onLoad]');

Array.prototype.forEach.call(elements, function (el) {
    var chaffle = new Chaffle(el)
    el.addEventListener('mouseover', function () {
        chaffle.init();
    });
});

Array.prototype.forEach.call(elm, function (el) {
    var chaffle = new Chaffle(el, {
        delay: 200
    })
    setInterval(function () {
        chaffle.init();
    }, 8000)
});
