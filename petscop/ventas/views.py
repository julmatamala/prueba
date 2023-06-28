from django.shortcuts import render, redirect
from .models import Cliente, Producto, Egreso, ProductosEgreso
from .forms import AddClienteForm,EditarClienteForm,AddProductoForm, EditarProductoForm
from django.contrib import messages
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.conf import settings
import os
# Create your views here.
def ventas_view(request):
    context = {
    }
    return render(request, 'index.html')

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()

    context = {'clientes': clientes,
               'form_personal':form_personal,
               'form_editar':form_editar
               }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    #print("Guardar CLiente")
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el cliente")    
                return redirect('Clientes')
    return redirect('Clientes')

def edit_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(
            request.POST, request.FILES, instance= cliente)
        if form.is_valid:
            form.save()
    return redirect('Clientes')


def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('Clientes')


def productos_view(request):
    """""
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()
"""
    productos= Producto.objects.all()
    form_add = AddProductoForm()
    form_editar = EditarProductoForm()

    context = {
        'productos': productos,
        'form_add': form_add,
        'form_editar': form_editar
    }
    return render(request, 'productos.html', context)


def add_producto_view(request):
    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el producto")    
                return redirect('Productos')
    return redirect('Productos')


def edit_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_editar'))
        form = EditarProductoForm(
            request.POST, request.FILES, instance= producto)
        if form.is_valid:
            form.save()
    return redirect('Productos')

def delete_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_eliminar'))
        producto.delete()

    return redirect('Productos')



def ofertas(request):
    return render(request, 'ofertas.html')

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'aboutus.html')

def register(request):
    if request.method == 'POST':
        form = AddClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    else:
        form = AddClienteForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    return render(request, 'login.html')

def carrito(request):
    return render(request, 'carrito.html')
    

