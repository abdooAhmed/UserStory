(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
	  (($('#sidebar').hasClass("active"))? $('.testimonial-group').css('max-width','160rem') :$('.testimonial-group').css('max-width','79rem'));
  });

})(jQuery);
