from django.contrib import admin
from .models import Marca, Producto
from .forms import ProductoForm

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "descripcion", "marca", "tipo_producto", "imagen"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["tipo_producto", "marca"]
    list_per_page= 5
    form = ProductoForm
    




admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)