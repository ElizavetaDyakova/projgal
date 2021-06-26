let viewport = $("#viewport").width();
let slider = $("div.slider");
let viewSliders = $(".viewSlide");
let viewSlide = 0;
let slideInterval = 6000;

viewSliders[viewSlide].style.backgroundColor = "#6D7688";

function nextSlide() {
    viewSliders[viewSlide].style.backgroundColor = "#98A5BE";
    if (viewSlide < 4) {
        viewSlide++;
    } else {
        viewSlide = 0;
    }
    viewSliders[viewSlide].style.backgroundColor = "#6D7688";
    slider.animate({ 'left': -viewSlide * $('#viewport').width() + "px" }, { 'duration': 1000 })
}
$(".next").click(nextSlide);
$(".prev").click(function() {
    viewSliders[viewSlide].style.backgroundColor = "#98A5BE";
    if (viewSlide > 0) {
        viewSlide--;
    } else {
        viewSlide = 4;
    }
    viewSliders[viewSlide].style.backgroundColor = "#6D7688";
    slider.animate({ 'left': -viewSlide * $('#viewport').width() + "px" }, { 'duration': 1000 })
});
$(document).ready(function() {
    setInterval(nextSlide, slideInterval);
});



// prokr
jQuery(function($) {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 208) {
            $('#nav').addClass('fixed');
        } else if ($(this).scrollTop() < 208) {
            $('#nav').removeClass('fixed');
        }
    });
});