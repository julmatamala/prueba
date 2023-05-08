//global darkmode
$(document).ready(function() {
	$('#cambiarFondo').click(function() {
		$('body').toggleClass('modoOscuro');
		$('#aboutush1').toggleClass('modoOscuro');
		$('#registro').toggleClass('modoOscuro');
		$('#bodyCarrito').toggleClass('modoOscuro');
	
	});

	$('#petsco').click(function(event){
		event.preventDefault();
		alert("Ya estás en la pagina principal");
	})

	// Obtener el campo de entrada y los elementos de contador
	var input = $('#inputrut');
	console.log(input);
	var count = $('#char-count');
	
	// Configurar el límite de caracteres
	var maxChars = 10; // Por ejemplo, 280 caracteres como en Twitter
	count.text("0/" + maxChars); // Mostrar el contador inicializado
	
	// Escuchar el evento "input" en el campo de entrada
	input.on('input', function() {
	  // Obtener la longitud actual del texto en el campo de entrada
	  var len = input.val().length;
	  
	  // Actualizar los contadores
	  count.text(len + "/" + maxChars);
	  
	  // Cambiar el color del contador a rojo si se ha alcanzado o superado el límite de caracteres
	  if (len >= maxChars) {
		count.css('color', 'red');
	  } else {
		count.css('color', '');
	  }
	});
  });
  
  
  
  
  