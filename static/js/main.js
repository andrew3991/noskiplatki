$(document).ready(function(){
	$(".widget h2").click(
		function(){
			$(this).parent().toggleClass('active');
		});

    /*Catalog item Add/like*/
/*    $(".product").hover(function(){
    	$(this).find('.product_buttons').stop();
        $(this).find('#likes').css('visibility','visible').animate();
        $(this).find('.product_buttons').show(200);
        
    },
    function(){
    	$(this).find('.product_buttons').stop();
        $(this).find('.product_buttons').hide(150);
        $(this).find('#likes').css('visibility','hidden').animate();
        $(this).find('.product_info').css('margin-bottom','0px').animate();
        
    }); */

    $(".product").hover(function(){
        $(this).find('.product_buttons').stop();
        $(this).find('.product_buttons').slideToggle(250)
        
    },
    function(){
        $(this).find('.product_buttons').stop();
        $(this).find('.product_buttons').slideToggle(250);
        
    }); 
    /*CAROUSEL*/
    $('.owl-carousel').owlCarousel({
    loop:false,
    margin:10,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true,
            loop:false
        },
        600:{
            items:3,
            nav:true,
            loop:false
        },
        1000:{
            items:5,
            nav:true,
            loop:false
        }
    }
    });
    $( ".owl-prev").html('<i class="fa fa-angle-left"></i>');
    $( ".owl-next").html('<i class="fa fa-angle-right"></i>');
    
    /*CODE AJAX*/
   $('.product_buttons  #likes').click(function(){
    var $obj = $(this);
    var catid;
    var catslug;
    catid = $obj.attr("data-catid");
    catslug = $obj.attr("data-catslug");
    $.post('/'+catid+'/'+catslug + '/new/',{'csrfmiddlewaretoken': csrftoken}, function(response){
            if (response.status == 'added') {
                $obj.removeClass('stars').addClass('stars-add');
            }else {
                $obj.removeClass('stars-add').addClass('stars');}
            console.log("success");
            
    });
               
    });
/*$('#likes').click(function() {
    var $obj = $(this);
    $obj.prop('disabled', true);

    var catid;
    var catslug;
    catid = $(this).attr("data-catid");
    catslug = $(this).attr("data-catslug");

    $.ajax({
    url: '/'+catid+'/'+catslug + '/new/',
    type: 'POST',
    data: {'csrfmiddlewaretoken': csrftoken},
    success: function(response) {
        if (response.status == 'added') {
        $obj.removeClass('stars').addClass('stars-add');}
        else {
        $obj.removeClass('stars-add').addClass('stars');}
        $obj.parent('.favorite').children('.fav-count').text(response.fav_count);
        $obj.prop('disabled', false);
    }
    });
*/

    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")
        send_date();

      })
    function send_date() {
        console.log("create post is working!") // sanity check
        $.ajax({
            url : "contact/", // the endpoint
            type : "POST", // http method
            data : { name: $('#name').val(),
                    email: $('#email').val(),
                    number_phone: $('#number_phone').val(),
                    client_message: $('#client_message').val(),
                    'csrfmiddlewaretoken': csrftoken }, // data sent with the post request
            // handle a successful response
            /*beforeSend: startLoadingAnimation(),*/

            success : function(json) {
                /*stopLoadingAnimation()*/
                $('#name').val(''); // remove the value from the input
                $('#email').val('');
                $('#number_phone').val('');
                $('#client_message').val('');
                console.log(json); // log the returned json to the console
                console.log("success");
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }

        });
    };

    




   function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });



});