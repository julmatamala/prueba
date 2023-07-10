from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        return productos    





def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'petscop/home.html', data)

def about_us(request):
    return render(request, 'petscop/aboutus.html')



def carrito(request):
    return render(request, 'petscop/carrito.html')

@permission_required('petscop.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }


    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado")
        else:
            data["form"] = formulario

    return render(request, 'petscop/producto/agregar.html', data)

@permission_required('petscop.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404    


    data = {
            'entity': productos,
            'paginator': paginator
            }
    return render(request, 'petscop/producto/listar.html', data)


@permission_required('petscop.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_producto")
        data['form'] = formulario

    return render(request, 'petscop/producto/modificar.html', data)

@permission_required('petscop.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_producto")


def registro(request):
    data= {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario


    return render(request, 'registration/registro.html', data)