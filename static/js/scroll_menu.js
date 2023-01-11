$(document).ready(function() {
    jQuery(function($) {
	        $(window).scroll(function(){
	            if($(this).scrollTop()>5){
	                $('.container-menu').addClass('shadow');
	            }
	            else if ($(this).scrollTop()<5){
	                $('.container-menu').removeClass('shadow');
	            }
	        });
	    });
});