from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError



class ProductoForm (forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(min_value=1, max_value=1000000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")

        return nombre


    class Meta:
        model = Producto
        fields = '__all__'




class CustomUserCreationForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2", ]