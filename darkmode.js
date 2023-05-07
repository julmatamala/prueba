//global darkmode
$(document).ready(function() {
	$('#cambiarFondo').click(function() {
		$('body').toggleClass('modoOscuro');
		$('#aboutush1').toggleClass('modoOscuro');
		$('#registro').toggleClass('modoOscuro');
		$('#bodyCarrito').toggleClass('modoOscuro');
	
	});
});






//index
document.getElementById("petsco").addEventListener("click", function(event) {
	event.preventDefault();
	alert("Ya estás en la pagina principal");
  });

 
 
  //about us
  