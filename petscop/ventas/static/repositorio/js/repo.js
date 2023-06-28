$(document).ready(function () {

  $("#basic-form").validate({
    rules: {
      rut: {
        required: true,
        minlength: 8,
        maxlength: 10
      },
      edad: {
        required: true,
        number: true,
        min: 18,
        max: 99
      },
      nombre: {
        required: true,
        minlength: 3,
        maxlength: 40,
      },
      apellido_paterno: {
        required: true,
        minlength: 3,
        maxlength: 20,
      },
      contrasena: {
        required: true,
        minlength: 8,
        maxlength: 20
      },
      telefono: {
        required: true,
        minlength: 8,
        maxlength: 9,
        number: true
      },
      email: {
        required: true,
        email: true
      },
      Direccion: {
        required: true,
        maxlength: 50,

      }
    },
    messages: {
      rut: {
        required: "Ingrese El Rut",
        minlength: "El rut tiene que ser de 8 a 10 dígitos y solo puede contener numeros, letras y guion bajo.",
        maxlength: "El nombre tiene que ser de 8 a 10 dígitos y solo puede contener numeros, letras y guion bajo."
      },
      edad: {
        required: "Ingrese la edad",
        number: "debe ser solo numeros",
        min: "la edad minima es de 18 años",
        max: "la edad maxima es de 99 años"
      },
      email: {
        required: "Ingrese El email",
        email: "El correo debe estar en el formato: abc@mail.com"
      },
      nombre: {
        required: "Por favor ingrese su nombre",
        minlength: "El nombre debe tener al menos 3 caracteres",
        maxlength: "El nombre no debe tener más de 50 caracteres",
      },
      apellido_paterno: {
        required: "Por favor ingrese su su apellido_paterno",
        minlength: "El nombre debe tener al menos 3 caracteres",
        maxlength: "El nombre no debe tener más de 50 caracteres",
      },
      telefono: {
        required: "Ingrese el numero de celular",
        minlength: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros",
        maxlength: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros",
        number: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros"
      },

      Direccion: {
        required: "Debe ingresar su direccion",
        max: "la direccion solo acepta 50 caracteres"
      },
      contrasena: {
        required: "Debe ingresar una contraseña"
      },
    },
    errorElement: 'span',
    submitHandler: function (form) {
      // Enviar el mensaje personalizado
      alert("¡Gracias por completar el formulario!");
      form.submit();
    }
  });

});

