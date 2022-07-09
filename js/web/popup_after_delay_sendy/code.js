// Attribution: 

function onPopupOpen() {
    $("#modal-content").show();
    $("#FirstName").focus();
}

function onPopupClose() {
    $("#modal-content").hide();
    lastFocus.focus();
}

var lastFocus;
var delay = 3000;

setTimeout(function () {
    lastFocus = document.activeElement;
    onPopupOpen();
}, delay);

$(".close-button").on("click", function () {
    onPopupClose();
});