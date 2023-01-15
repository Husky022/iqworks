
$(document).ready(function() {
	$('#start, .callback-first-content, #calc-consultation').click(function(event){
		event.preventDefault();
		$('#overlay').fadeIn(250,
		 	function(){
				$('#popUp')
					.css('display', 'block')
					.animate({opacity: 1, top: '30%'}, 490);
		});
	});

    $('#video').click(function(event){
		event.preventDefault();
		$('#overlay').fadeIn(250,
		 	function(){
				$('#player')
					.css('display', 'block')
					.animate({opacity: 1, top: '25%'}, 490);
		});
	});

	$('#close, #overlay').click(function(event){
		event.preventDefault();
		$('#popUp')
			.animate({opacity: 0, top: '0%'}, 490,
				function(){
					$(this).css('display', 'none');
					$('#overlay').fadeOut(220);
				}
			);
	});

	$('#overlay, #video-close').click(function(event){
		$('#player')
			.animate({opacity: 0, top: '0%'}, 490,
				function(){
					$(this).css('display', 'none');
					$('#overlay').fadeOut(220);
				}
			);
		event.preventDefault();
		player.pauseVideo();
	});

});