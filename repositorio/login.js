$(document).ready(function () {
   
    $("#basic-form").validate({     
      rules: {
        contrasena: {
            required:true,
            minlength:8,
            maxlength:20
            },
  
        email: {
          required: true,
          email: true
        },
  
      },

      messages: {
        email: {
          required: "Ingrese El email",
          email: "El correo debe estar en el formato: abc@mail.com"
        },

        contrasena: {
            required: "Debe ingresar una contraseña"
          },
    },

    errorElement : 'span'

  });

});