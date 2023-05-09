

$(document).ready(function () {
   
    $("#basic-form").validate({     
      rules: {
        rut: {
          required: true,
          minlength: 9,
          maxlength: 10
        },
  
        edad: {
          required: true,
          number: true,
          min: 18,
          max: 35
        },
        

        nombre: {
            required: true,
            minlength: 3,
            maxlength: 50,
           
        },

        contrasena: {
            required:true,
            minlength:8,
            maxlength:20
            },

        contrasenaconfirmar: {
        equalTo:"#contrasena",
         },
        
  
        telefono: {
          required: true,
          minlength: 9,
          maxlength: 12,
          number: true
        },
  
        email: {
          required: true,
          email: true
        },
  
        Genenero: {
          required: true
        },
        Direccion: {
          required: true,
      }
  
      },

      messages: {
        rut: {
          required: "Ingrese El Rut",
          minlength: "El rut tiene que ser de 9 a 10 dígitos y solo puede contener numeros, letras y guion bajo.",
          maxlength: "El nombre tiene que ser de 9 a 10 dígitos y solo puede contener numeros, letras y guion bajo."
        },
        edad: {
          required: "Ingrese la edad",
          number: "debe ser solo numeros",
          min: "la edad minima es de 18 años",
          max: "la edad maxima es de 35 años"
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
        
        telefono: {
          required: "Ingrese el numero de celular",
          minlength: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros",
          maxlength: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros",
          number: "El numero de celular tiene que ser de 9 a 12 dígitos y solo puede contener numeros"
        },
        Genenero: {
          required: "Debe seleccionar un genero de la lista"
        },
        Direccion: {
          required: "Debe ingresar su direccion"
        },
        contrasena: {
            required: "Debe ingresar una contraseña"
          },
        contrasenaconfirmar: {
            equalTo: "Las contraseña no coiciden"
          },
    },

    errorElement : 'span'

  });

});


