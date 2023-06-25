from django import forms  
from ventas.models import Cliente


class AddClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ( 'rut', 'nombre', 'apellido_paterno', 'telefono', 'email', 'direccion',
                   'edad', 'contraseña' )
        labels ={
                'rut': 'Rut: ', 
                'nombre': 'Nombres: ',
                'apellido_paterno': 'Apellido Paterno: ' , 
                'telefono': 'Telefono: ', 
                'email': 'E-mail: ', 
                'direccion': 'direccion: ',
                'edad': 'Edad: ', 
                'contraseña': 'Contraseña: '
        }