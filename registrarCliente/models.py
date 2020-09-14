from django.db import models

# Create your models here.

def registrar_Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    contrasena=models.CharField(max_length=50)
    cuil_cuit=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    email=models.EmailField()
    tipo=models.CharField(max_length=10)
    telefono=models.CharField(max_length=20)
