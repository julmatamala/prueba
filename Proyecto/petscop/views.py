from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Boleta, detalle_boleta
from .forms import ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer
from petscop.compra import Carrito
from django.db.models import F

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

@permission_required('petscop.add_producto')
def agregar_producto_crud(request):

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

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "petscop/producto/tienda.html", {'productos':productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    if producto.cantidad is None or producto.cantidad <= 0:
        # Producto no tiene cantidad disponible
        # Puedes agregar una lógica adicional, como mostrar un mensaje de error
        messages.error(request, "No hay stock disponible para este producto.")
        return redirect("tienda")
    
    carrito.agregar(producto)
    request.session['carrito'][str(producto.id)]['nombre'] = producto.nombre
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

def generarBoleta(request):
    if 'carrito' not in request.session or not request.session['carrito']:
        # El carrito está vacío, mostrar mensaje de error y redirigir a la página anterior
        messages.error(request, 'El carrito está vacío')
        return redirect('tienda')

    precio_total = 0
    for key, value in request.session['carrito'].items():
        precio_total += int(value['acumulado'])
    boleta = Boleta(total=precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
        producto = Producto.objects.get(id=value['producto_id'])
        cant = value['cantidad']
        subtotal = cant * int(value['acumulado'])
        detalle = detalle_boleta(id_boleta=boleta, id_producto=producto, cantidad=cant, subtotal=subtotal)
        detalle.save()
        productos.append(detalle)

        # Restar la cantidad vendida del atributo "cantidad" del producto
        Producto.objects.filter(id=producto.id).update(cantidad=F('cantidad') - cant)

    datos = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'petscop/producto/detallecarrito.html', datos)
