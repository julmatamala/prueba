from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.ventas_view, name='Ventas'),
    path('clientes/', views.clientes_view, name='Clientes'),
    path('add_cliente/', views.add_cliente_view, name='AddCliente'),
    path('edit_cliente/', views.edit_cliente_view, name='EditCliente'),
    path('delete_cliente/', views.delete_cliente_view, name='DeleteCliente'),
    
    path('productos/', views.productos_view, name='Productos'),
    path('add_producto/', views.add_producto_view, name='AddProducto'),
    path('edit_producto/', views.edit_producto_view, name='EditProducto'),
    path('delete_producto/', views.delete_producto_view, name='DeleteProducto'),

    
    path('aboutus/', views.about_us, name='about_us'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('carrito/', views.carrito, name='carrito'),
    path('ofertas/', views.ofertas, name='ofertas'),


] 
