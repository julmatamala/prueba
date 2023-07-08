$(document).ready(function() {
  $('#login-button').on('click', function(event) {
      event.preventDefault();
      
      let username = $('#username-input').val();
      let password = $('#password-input').val();
      
      let emailRegex = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
      if (!emailRegex.test(username)) {
          alert('Ingresa un correo electrónico válido');
          return;
      }
      
      if (password === '') {
          alert('Ingresa tu contraseña');
          return;
      }
      
      window.location.href = "{% url 'Petscop' %}";
  });
});