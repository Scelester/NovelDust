// for navbar

var navbar = document.getElementById("navcontainer");
var hiderbutton = document.getElementById("hidenavbutton");



// for content holder
var ctxmain = document.getElementById("ctxmain");

function showsidebar() {
  navbar.classList.add("active_snav");
  hiderbutton.style.display = "initial";
  ctxmain.classList.add("ctxmain");
}
function hidesidebar() {
  event.stopPropagation();
  navbar.classList.remove("active_snav");
  hiderbutton.style.display = "none";
  ctxmain.classList.remove("ctxmain")

}

