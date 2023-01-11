$(document).ready(function() {
    $('.how-we-work-item, .object-preview').mouseenter(function() {
        var a = $(this).find('.for-change').attr('src')
        b = a.replace('.png','-red.png');
        $(this).children('img').attr('src', b)
    });
    $('.how-we-work-item, .object-preview').mouseleave(function() {
        var a = $(this).find('.for-change').attr('src')
        b = a.replace('-red.png','.png');
        $(this).children('img').attr('src', b)
    });
});