/*registro*/
$(document).ready(function () {
    $("#basic-form").validate({
        rules: {
            inputrut: {
                required: true,
                minlength: 9,
                maxlength: 10
            },
            inputEdad: {
                required: true,
                number: true,
                min: 18,
                max: 125
            },
            nameInput: {
                required: true,
                minlength: 3,
                minlength: 20
            },
            lnameInput: {
                required: true,
                minlength: 3,
                maxlength: 20

            },
            inputrePas: {
                required: true,
                minlength: 8,
                maxlength: 40

            },
            inputPas: {
                required: true,
                minlength: 8,
                maxlength: 40

            },
            inputcontact: {
                required: true,
                minlength: 9,
                maxlength: 12,
                number: true
            },

            emailInput: {
                required: true,
                email: true
            },
            inputAdress: {
                required: true

            },
            inputRegión: {
                required: true

            },
            inputComuna: {
                required: true

            },
 


        },
        messages: {
            inputrut: {
                required: "Ingrese El Rut",
                minlength: "El rut tiene que ser de 9 a 10 dígitos y solo puede contener numeros, letras y guion bajo.",
                maxlength: "El nombre tiene que ser de 9 a 10 dígitos y solo puede contener numeros, letras y guion bajo."
            },
            inputEdad: {
                required: "Ingrese la edad",
                number: "debe ser solo numeros",
                min: "la edad minima es de 18 años",
                max: "la edad maxima es de 125 años"
            },
            emailInput: {
                required: "Ingrese El email",
                email: "El correo debe estar en el formato: abc@mail.com"
            },
            nameInput: {
                required: "Ingrese El nombre",
                minlength: "El nombre tiene que ser de 3 a 20 dígitos y solo puede contener letras.",
                maxlength: "El nombre tiene que ser de 3 a 20 dígitos y solo puede contener letras."
            },
            lnameInput: {
                required: "Ingrese el Apellido paterno",
                minlength: "El nombre tiene que ser de 3 a 20 dígitos y solo puede contener letras.",
                maxlength: "El nombre tiene que ser de 3 a 20 dígitos y solo puede contener letras."
            },
            inputrePas: {
                required: "Ingrese el Apellido materno",
                minlength: "El Apellido paterno tiene que ser de 3 a 20 dígitos y solo puede contener letras.",
                maxlength: "El Apellido materno tiene que ser de 3 a 20 dígitos y solo puede contener letras."
            },
            inputcontact: {
                required: "Ingrese el numero de celular",
                minlength: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros",
                maxlength: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros",
                number: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros"
            },
            inputAdress: {
                required: "Debe ingresar su direccion"
            },

            inputRegión: {
               
                required: "Debe ingresar su región"
            },

            inputComuna: {
                required: "Debe ingresar su comuna"
            }
        }
    });
});
/*login*/
$(document).ready(function() {
    $("#login-form").validate({
      rules: {
        usuario : {
          required: true,
        },
        contraseña: {
          required: true,
        },

      },
      messages : {

        usuario: {
          required: "Please enter your username",
        },
        contraseña: {
            required: "Please enter your password",
          },

      }
    });
  });