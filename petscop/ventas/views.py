from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import AddClienteForm
from django.contrib import messages
# Create your views here.
def ventas_view(request):
    context = {
    }
    return render(request, 'ventas.html')

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()

    context = {'clientes': clientes,
               'form_personal':form_personal
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
    return redirect('Clientes')

def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(rut=request.POST.get('rut_personal_eliminar'))
        cliente.delete()
    return redirect('Clientes')