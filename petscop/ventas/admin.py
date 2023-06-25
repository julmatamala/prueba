from django.contrib import admin
from ventas.models import Cliente, Producto
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','rut','apellido_paterno')
    search_fields = ['nombre']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','cantidad','costo')
    search_fields = ['descripcion']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, ProductoAdmin)