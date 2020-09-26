"""from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Transportista
from OpenCargo.views import landingPage

# Create your views here.

def registrar(request):
    print("hola")
    if request.method == 'REGISTRAR':
        print("entre al post")
        nombre = request.REGISTRAR["nombre"]
        apellido = request.POST["apellido"]
        contrasena = request.POST["contrasena1"]
        cuil_cuit = request.POST["documento"]
        direccion = request.POST["direccion"]
        email = request.POST["email"]
        tipo = request.POST["tipo"]
        telefono = request.POST["telefono"]
#recibo todos los datos

        cliente = Cliente(nombre=nombre,apellido=apellido,contrasena=contrasena,cuil_cuit=cuil_cuit, direccion=direccion,email=email,tipo=tipo,telefono=telefono)
        cliente.save()

    return home(request)
        
def sign_upCLIENTE(request):
    return render(request, "registro.html")

def sign_upCONDUCTOR(request):
    return render(request, "sign_upCONDUCTOR.html")"""


from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')
