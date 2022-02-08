function isMobile() {
    if(window.innerWidth<=450){
        return true
    }
  }




var last_novhold;
var last_novhold_obj;

$('.novelholder').click(function(e){
    
    if (isMobile()==true){
        e.preventDefault();
    }
        
    if (last_novhold==this){
            window.location = this.href
    }

    if (last_novhold){
        last_novhold_obj.removeClass('lifted')
    }
    
    $(this).addClass('lifted')
    
    last_novhold = this
    last_novhold_obj = $(this);
  });



// ajax setup
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue =   decodeURIComponent(cookie.substring(name.length + 1));
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


// usermenu
$('.usermenuitem').click(function(e){
    $('.usermenuitem').removeClass('usermenuitemclick');
    $(this).addClass('usermenuitemclick');
})


$('.dropdown-menu').click(function(e) {
    e.stopPropagation();
    if ($(e.target).is('[data-toggle=modal]')) {
        $($(e.target).data('target')).modal()
    }
});


$(document).ready(function() {
    {
    var input = $(".sbarf");
    var len = input.val().length;
    input[0].focus();
    input[0].setSelectionRange(len, len);
    }
});