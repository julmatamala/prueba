from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.petscop_view, name='Petscop'),
    path('aboutus/', views.about_us, name='about_us'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('carrusel/', views.carusel, name='carrusel'),
    path('carrito/', views.carrito, name='carrito'),




] 
