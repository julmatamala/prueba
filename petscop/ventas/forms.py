from django import forms  
from ventas.models import Cliente,Producto


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

class EditarClienteForm(forms.ModelForm):
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
        widgets ={
                'rut': forms.TextInput(attrs={'type': 'text', 'id':'rut_editar'}),
                'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
                'apellido_paterno': forms.TextInput(attrs={'id': 'apellido_editar'}),
                'telefono': forms.NumberInput(attrs={'id': 'telefono_editar'}),
                'email': forms.TextInput(attrs={'id': 'email_editar'}),
                'direccion': forms.TextInput(attrs={'id': 'direccion_editar'}),
                'edad': forms.NumberInput(attrs={'id': 'edad_editar'}),
                'contraseña': forms.TextInput(attrs={'id': 'contraseña_editar'}),
        }


class AddProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ( 'codigo', 'descripcion', 'costo', 'cantidad', 'imagen' )
        labels ={
                'codigo': 'Codigo: ', 
                'descripcion': 'Descripcion: ',
                'costo': 'Valor: ', 
                'cantidad': 'Cantidad: ',
                'imagen': 'Imagen: ' , 
        }  


class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ( 'codigo', 'descripcion', 'costo', 'cantidad', 'imagen' )
        labels ={
                'codigo': 'Codigo: ', 
                'descripcion': 'Descripcion: ',
                'costo': 'Valor $: ', 
                'cantidad': 'Cantidad: ',
                'imagen': 'Imagen: ' , 
        }  

        widgets ={
                'codigo': forms.TextInput(attrs={'type': 'text', 'id':'codigo_editar'}),
                'descripcion': forms.TextInput(attrs={'id': 'descripcion_editar'}),
                'costo': forms.NumberInput(attrs={'id': 'costo_editar'}),
                'cantidad': forms.NumberInput(attrs={'id': 'cantidad_editar'}),
                'imagen': forms.TextInput(attrs={'id': 'imagen_editar'}),
        }



class LoginForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('email',  'contraseña' )
        labels ={
                'email': 'E-mail: ', 
                'contraseña': 'Contraseña: '
        }
