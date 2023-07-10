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


    class Meta:
        model = Producto
        fields = '__all__'




class CustomUserCreationForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2", ]