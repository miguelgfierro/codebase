// Attribution: https://www.sitepoint.com/show-modal-popup-after-time-delay/

$(".clear-cookie").on("click", function () {
    Cookies.remove('colorboxShown');
    $(this).replaceWith("<p><em>Cookie cleared. Re-run demo</em></p>");
});

$(".order-cheezburger").on("click", function () {
    $.colorbox.close();
});

function onPopupOpen() {
    $("#modal-content").show();
    $("#yurEmail").focus();
}

function onPopupClose() {
    $("#modal-content").hide();
    Cookies.set('colorboxShown', 'yes', {
        expires: 1
    });
    $(".clear-cookie").fadeIn();
    lastFocus.focus();
}

function displayPopup() {
    $.colorbox({
        inline: true,
        href: "#modal-content",
        className: "cta",
        width: 600,
        height: 350,
        onComplete: onPopupOpen,
        onClosed: onPopupClose
    });
}

var lastFocus;
var popupShown = Cookies.get('colorboxShown');

if (popupShown) {
    console.log("Cookie found. No action necessary");
    $(".clear-cookie").show();
} else {
    console.log("No cookie found. Opening popup in 3 seconds");
    $(".clear-cookie").hide();
    setTimeout(function () {
        lastFocus = document.activeElement;
        displayPopup();
    }, 3000);
}