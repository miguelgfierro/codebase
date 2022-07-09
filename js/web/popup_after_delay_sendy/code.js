// Attribution: https://www.sitepoint.com/show-modal-popup-after-time-delay/

function onPopupOpen() {
    $("#modal-content").show();
    $("#email").focus();
}

function onPopupClose() {
    $("#modal-content").hide();
    lastFocus.focus();
}

// No hace falta?
function displayPopup() {
    $.colorbox({
        inline: true,
        href: "#modal-content",
        className: "cta",
        width: 450,
        height: 600,
        onComplete: onPopupOpen,
        onClosed: onPopupClose
    });
}

var lastFocus;
var delay = 3000;

setTimeout(function () {
    lastFocus = document.activeElement;
    displayPopup();
    //onPopupOpen();
}, delay);
