function isMobile() {
    try{ document.createEvent("TouchEvent"); return true; }
    catch(e){ return false; }
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


$('#password')