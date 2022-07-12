// Attribution: https://codepen.io/jaeming/pen/XWyaMe
$(function () {
    $('.pop-up').hide();
    $('.pop-up').fadeIn(3000);

    $('.close-button').click(function (e) {

        $('.pop-up').fadeOut(700);
        $('#overlay').removeClass('blur-in');
        $('#overlay').addClass('blur-out');
        e.stopPropagation();
    });
});