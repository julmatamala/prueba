from django.urls import path
from .views import home, about_us, carrito, agregar_producto, listar_productos, modificar_producto, registro, eliminar_producto

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', about_us, name='about_us'),
    path('carrito/', carrito, name='carrito'),
    path('agregar-producto/', agregar_producto, name="agregar_producto" ),
    path('listar-producto/', listar_productos, name="listar_producto" ),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name='registro')


] 
