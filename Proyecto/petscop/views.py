from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'petscop/home.html', data)

def login(request):
    return render(request, 'petscop/login.html')
    return render(request, 'petscop/carusel.html')

def about_us(request):
    return render(request, 'petscop/aboutus.html')

def register(request):
    return render(request, 'petscop/register.html')

def carrito(request):
    return render(request, 'petscop/carrito.html')


def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }


    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'petscop/producto/agregar.html', data)


def listar_productos(request):
    productos = Producto.objects.all()
    data = {
            'productos': productos
            }

    return render(request, 'petscop/producto/listar.html', data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data['form'] = formulario

    return render(request, 'petscop/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_producto")
