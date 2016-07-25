$(document).ready(function() {
    //scroll functionality on edit section page
    $("select").change(function(){
        var selectedSection = $("#first-choice").val();
        $('body').scrollTo('div .post_section_' + selectedSection, 800,{offset:-100});
        $("div .post_section_" + selectedSection).effect("highlight", {color: '#29b0b6'}, 2000);
    })

    //add url when click on edit function
    $("div.section-edit").click(function(){
        window.location=$(this).find("a").attr("href"); return this;
    });


    $('.bannerTitle').addClass('animated rubberBand');


    $("i.fa-facebook, i.fa-github,i.fa-linkedin").hover(function(){
      $(this).addClass('animated rubberBand');
    },function(){
      $(this).removeClass('animated rubberBand');

    });




    var native_width = 0;
	var native_height = 0;
    $(".large").css("background","url('" + $(".small").attr("src") + "') no-repeat");

	//Now the mousemove function
	$(".magnify").mousemove(function(e){
		//When the user hovers on the image, the script will first calculate
		//the native dimensions if they don't exist. Only after the native dimensions
		//are available, the script will show the zoomed version.
		if(!native_width && !native_height)
		{
			//This will create a new image object with the same image as that in .small
			//We cannot directly get the dimensions from .small because of the
			//width specified to 200px in the html. To get the actual dimensions we have
			//created this image object.
			var image_object = new Image();
			image_object.src = $(".small").attr("src");

			//This code is wrapped in the .load function which is important.
			//width and height of the object would return 0 if accessed before
			//the image gets loaded.
			native_width = image_object.width;
			native_height = image_object.height;
		}
		else
		{
			//x/y coordinates of the mouse
			//This is the position of .magnify with respect to the document.
			var magnify_offset = $(this).offset();
			//We will deduct the positions of .magnify from the mouse positions with
			//respect to the document to get the mouse positions with respect to the
			//container(.magnify)
			var mx = e.pageX - magnify_offset.left;
			var my = e.pageY - magnify_offset.top;

			//Finally the code to fade out the glass if the mouse is outside the container
			if(mx < $(this).width() && my < $(this).height() && mx > 0 && my > 0)
			{
				$(".large").fadeIn(100);
			}
			else
			{
				$(".large").fadeOut(100);
			}
			if($(".large").is(":visible"))
			{
				//The background position of .large will be changed according to the position
				//of the mouse over the .small image. So we will get the ratio of the pixel
				//under the mouse pointer with respect to the image and use that to position the
				//large image inside the magnifying glass
				var rx = Math.round(mx/$(".small").width()*native_width - $(".large").width()/2)*-1;
				var ry = Math.round(my/$(".small").height()*native_height - $(".large").height()/2)*-1;
				var bgp = rx + "px " + ry + "px";

				//Time to move the magnifying glass with the mouse
				var px = mx - $(".large").width()/2;
				var py = my - $(".large").height()/2;
				//Now the glass moves with the mouse
				//The logic is to deduct half of the glass's width and height from the
				//mouse coordinates to place it with its center at the mouse coordinates

				//If you hover on the image now, you should see the magnifying glass in action
				$(".large").css({left: px, top: py, backgroundPosition: bgp});
			}
		}
	})

});


//jQuery for navigation bar "Active"
$(function(){
   $(".navbar-nav li a").each(function(){
       $(this).parent().removeClass("active");
          if(this.href == window.location){
                 $(this).parent().addClass("active");
            }
   });
});


$(function(){
   var lang = "";
   $(".banner").css("background-image","-webkit-linear-gradient(left,#156269,#0c0000)");
   $('.banner').attr('data-attr-second', 'Post section for Python, Django, GitHub');
   $('.banner').attr('data-attr', 'Posts');
   $(".navbar-nav li a").each(function(){
          if(this.href == window.location){
             lang = $(this).text();
             switch(lang){
                case "Django":
                    $(".banner").css("background-image","-webkit-linear-gradient(left,#006633,#215E36)");
                    $('.banner').attr('data-attr', 'Django');
                    $('.banner').attr('data-attr-second', 'The web framework for perfectionists with deadlines');
                    break;
                case "Python":
                    $(".banner").css("background-image","-webkit-linear-gradient(left,#2b5b84,#2b6b84)");
                    $('.banner').attr('data-attr', 'Python');
                    $('.banner').attr('data-attr-second', 'The efficient programming language for quick development');
                    break;
                case "GitHub":
                    $(".banner").css("background-image","-webkit-linear-gradient(left,#6e3a6b,#622d73)");
                    $('.banner').attr('data-attr', 'GitHub');
                    $('.banner').attr('data-attr-second', 'The powerful version control system for better software lifecycle');
                    break;
                case "Posts":
                    $(".banner").css("background-image","-webkit-linear-gradient(left,#156269,#0c0000)");
                    $('.banner').attr('data-attr', 'Posts');
                    $('.banner').attr('data-attr-second', 'Post section for Python, Django, GitHub');
                    break;
                case "Contact":
                    $(".banner").css("background-image","-webkit-linear-gradient(left,#781b3b,#921b33)");
                    $('.banner').attr('data-attr', 'Contact');
                    $('.banner').attr('data-attr-second', 'Here is place for keeping connection');
                    break;
                case "Log in":
                    $(".banner").css("background-image","-webkit-linear-gradient(left,#494047,#0c0000)");
                    $('.banner').attr('data-attr', 'LogIn');
                    $('.banner').attr('data-attr-second', ' Explore more you would like to know');
                    break;
             }
          }



   });
});


//jQuery for toggle title in banner when screen size change to small
$(function(){
    $( ".bgh" ).click(function() {
        $( ".bannerTitle" ).toggle("slow");
    });
});


$(function(){
    $(".btn-know-more").click(function(){
        $('html, body').animate({
        scrollTop: $(".main_title").offset().top - $("div.navbar-header").height() - 30
    }, 1000);
    return false;
});

});


//jQuery for menu toggle and parallax background, title when scroll down and up
var state = "down";
$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    if(top.location.pathname === "/"){
     var main_title_off_set = $(".bannerTitle").offset().top;
     var sub_title_off_set = $(".sub_title").offset().top;
     var python_off_set = $(".python_section").offset().top;
     var django_off_set = $(".django_section").offset().top;
     var jQuery_off_set = $(".jQuery_section").offset().top;
    }else{
     var banner = $(".banner").height()/2;
    }


    if((scroll > main_title_off_set || scroll > banner)  &&  state === "down"){
        $("nav").stop(true).animate({ "backgroundColor": "black"}, {duration: 1000,queue:false});
        $('.profile').addClass('animated fadeInUp');
        state = "up";
    }
    if(scroll > sub_title_off_set){
        $(".python_pic").addClass('animated fadeIn');
    }
    if (scroll > python_off_set){
         $(".django_pic").addClass('animated slideInRight');
         $(".laptop").addClass('animated slideInLeft ');
         $(".iphone").addClass('animated fadeIn ');
    }
    if (scroll > django_off_set){
        $('.jQuery_pic').addClass('animated fadeInUp');
        $('.siteTraffic').addClass('animated fadeInUp');
    }


    if(scroll > jQuery_off_set){
        $('.index_pic_info').addClass('animated flipInY');
        $('.index_pic_tech').addClass('animated flipInY');
        $('.index_pic_rese').addClass('animated flipInY');
        $('.index_pic_conn').addClass('animated flipInY');
    }
    else if ((scroll < main_title_off_set || scroll < banner) && state === "up"){
        $("nav").stop(true).animate({ "backgroundColor": "transparent"}, {duration: 1000,queue:false});
        state = "down";
    }

   $(".jumbotron").css("background-position", "0  " + -scroll/3 + "px");
   $(".bannerTitle").css("top", 36 - scroll/100 + "%");
});



$(function(){
if(top.location.pathname === "/"){
    var newDate = new Date();
    new Morris.Line({
      // ID of the element in which to draw the chart.
      element: 'myfirstchart',
      // Chart data records -- each entry in this array corresponds to a point on
      // the chart.
      data: [
          { date: newDate.getFullYear().toString()+ "-" + (newDate.getMonth()+1).toString()+"-"+newDate.getDate().toString(), value: 20 },
          { date: newDate.getFullYear().toString()+ "-" + (newDate.getMonth()+1).toString()+"-"+(newDate.getDate()-1).toString(), value: 20 },
          { date: newDate.getFullYear().toString()+ "-" + (newDate.getMonth()+1).toString()+"-"+(newDate.getDate()-2).toString(), value: 22 },
          { date: newDate.getFullYear().toString()+ "-" + (newDate.getMonth()+1).toString()+"-"+(newDate.getDate()-3).toString(), value: 33 },
          { date: newDate.getFullYear().toString()+ "-" + (newDate.getMonth()+1).toString()+"-"+(newDate.getDate()-4).toString(), value: 44 },
          { date: newDate.getFullYear().toString()+ "-" + (newDate.getMonth()+1).toString()+"-"+(newDate.getDate()-5).toString(), value: 55 },
          { date: newDate.getFullYear().toString()+ "-" + (newDate.getMonth()+1).toString()+"-"+(newDate.getDate()-6).toString(), value: 11 },
      ],
      // The name of the data record attribute that contains x-values.
      xkey: 'date',
      // A list of names of data record attributes that contain y-values.
      ykeys: ['value'],
      // Labels for the ykeys -- will be displayed when you hover over the
      // chart.
      labels: ['Value'],
    //  dateFormat:function (date) {
    //    d = new Date(date);
    //    return d.getDate().toString() + "-" + (d.getMonth()+1).toString() + "-" + d.getFullYear().toString(); }
    });
}

});

