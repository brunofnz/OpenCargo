from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Transportista

# Create your views here.

def registrar(request):
    print("hola")
    if request.method == 'POST':
        print("entre al post")
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        contrasena = request.POST["contrasena1"]
        cuil_cuit = request.POST["documento"]
        direccion = request.POST["direccion"]
        email = request.POST["email"]
        tipo = request.POST["tipo"]
        telefono = request.POST["telefono"]
        cliente = Cliente(nombre=nombre,apellido=apellido,contrasena=contrasena,cuil_cuit=cuil_cuit, direccion=direccion,email=email,tipo=tipo,telefono=telefono)
        cliente.save()
    return sign_upCLIENTE(request)
        

def sign_upCLIENTE(request):
    return render(request, "sign_upCLIENTE.html")

def sign_upCONDUCTOR(request):
    return render(request, "sign_upCONDUCTOR.html")