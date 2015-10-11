		
var rotation = function (){
	$('#header_logo').animate(
		{
			borderSpacing: -360
			
		}, 
		{
			step: function(now,fx) {
				$(this).css('-webkit-transform','rotate('+now+'deg)'); 
				$(this).css('-moz-transform','rotate('+now+'deg)');
				$(this).css('transform','rotate('+now+'deg)');
			},
			duration: 1000,
			complete: function(){
				$(this).fadeOut("slow", function(){
					//animation to make dragon ....
				
					$("#header_logo_dragon").animate({
						opacity: 0.6,
						width:291,
						height: 339
					},800);	
				});
					
			}
		},
		'linear'
	);
};
		
$(document).ready(function() {
	
$("#js-rotating").Morphext({
    animation:"zoomInLeft", // Overrides default "bounceIn"
    separator: ",", // Overrides default ","
    speed: 3000, // Overrides default 2000
    complete: function () {
        // Overrides default empty function
    }
});


});
		
window.onload = function() {
	var menu = $('.navbar');
	menu.wrap('<div class ="nav-placeholder"></div>');
	$(".nav-placeholder").height(menu.outerHeight());
	var origOffsetY = menu.offset().top;
	function scroll() {
		var scrollpos = $(window).scrollTop();
		$(".status").html(scrollpos);
		if ($(window).scrollTop() >= origOffsetY) {
			menu.addClass('fixed');
		} else {
				menu.removeClass('fixed');
			}

		}
	document.onscroll = scroll;	
};

$(function(){ 
	$("#nav_About").click(function(){ 
        $.scrollTo('#About',500,
		{offset:-52}
		);
	return false
    }); 

	$("#nav_Education").click(function(){ 
        $.scrollTo('#Education',500,{offset:-62}); 
	return false
    }); 

    $("#nav_Experience").click(function(){ 
        $.scrollTo('#Experience',800,{offset:-72});
	return false
    }); 
    $("#nav_Portfolio").click(function(){ 
        $.scrollTo('#Portfolio',1000); 
	return false
    }); 
    $("#nav_Skills").click(function(){ 
        $.scrollTo('#Skills',1200);
	return false
    }); 
    $("#nav_Contact").click(function(){ 
        $.scrollTo('#Contact',1500); 
	return false
    }); 
}); 

/*$(function(){
	$(".nav a").click(function(){ 
	$(".nav").find(".active").removeClass("active");
    $(this).parent().addClass("active");
	}); 
});*/



$(window).scroll(function(){
	  var sections = $('section');
	  var cur_pos = $(this).scrollTop();
	  var nav = $('nav');
	  var nav_height = nav.outerHeight();
	 
  sections.each(function() {
	  
    var top = $(this).offset().top - nav_height,
        bottom = top + $(this).outerHeight();

    if (cur_pos >= top && cur_pos <= bottom) {
      nav.find('.active').removeClass('active');
     sections.removeClass('active');
      
    $(this).addClass('active');
      nav.find('a[href="#'+$(this).attr('id')+'"]').parent().addClass('active');
    }
  });
});

