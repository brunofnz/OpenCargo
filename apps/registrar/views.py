from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import UserForm, UsuarioForm, TransportistaForm, VehiculoForm
from .models import Localidad, Transportista, Vehiculo


# Create your views here.


def crearUsuario(request):
    if request.method == 'POST':
        usuario_form = UserForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('landingPage')
    else:
        usuario_form = UserForm()
        print(usuario_form)
    return render(request,'registration/registro.html',{'usuario_form':usuario_form})

def completarDatos(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('pedidos')
    else:
        usuario_form = UsuarioForm()
        print(usuario_form)
    localidad = Localidad.objects.all()
    return render(request,'registration/completarDatos.html',{'usuario_form':usuario_form,'object_list': localidad})

def regsitrarseTransportista(request):
    if request.method == 'POST':
        transportista_form = TransportistaForm(request.POST)
        vehiculo_form = VehiculoForm(request.POST)
        if transportista_form.is_valid() and vehiculo_form.is_valid():
            transportista_form.save()
            vehiculo_form.save()
            return redirect('pedidos')
    else:
        transportista_form = TransportistaForm()
        vehiculo_form = VehiculoForm()
    localidad = Localidad.objects.all()
    return render(request,'registration/registrarseTransportista.html',{'transportista_form':transportista_form,'vehiculo_form':vehiculo_form,'object_list': localidad})

