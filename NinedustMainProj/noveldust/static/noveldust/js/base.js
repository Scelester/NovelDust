// for navbar

var navbar = document.getElementById("navcontainer");
var hiderbutton = document.getElementById("hidenavbutton");
var scrollnavcont = document.getElementById("navcontcont")


function funcscroll(){
  event.stopPropagation();
}

// for content holder
var ctxmain = document.getElementById("ctxmain");

function showsidebar() {
  hiderbutton.style.display = "initial";
  navbar.classList.add("active_snav");
  ctxmain.classList.add("ctxmain");
}
function hidesidebar() {
  event.stopPropagation();
  hiderbutton.style.display = "none"; 
  navbar.classList.remove("active_snav");
  ctxmain.classList.remove("ctxmain")
}

