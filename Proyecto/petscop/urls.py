from django.urls import path,include
from petscop.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', about_us, name='about_us'),
    path('agregar-producto/', agregar_producto, name="agregar_producto" ),
    path('listar-producto/', listar_productos, name="listar_producto" ),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),
    path('tienda/', tienda, name="tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),

] 
