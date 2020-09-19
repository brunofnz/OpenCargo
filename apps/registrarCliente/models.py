from django.db import models

# Create your models here.

class Cliente(models.Model):
    email=models.EmailField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    contrasena=models.CharField(max_length=50)
    cuil_cuit=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    tipo=models.CharField(max_length=10)
    telefono=models.CharField(max_length=20)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        txt="{0}\t{1},{2}\t{3}\t"
        return txt.format(self.cuil_cuit,self.apellido,self.nombre,self.tipo)


class Transportista(models.Model):
    email=models.EmailField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    contrasena=models.CharField(max_length=50)
    cuil_cuit=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    vehiculo=models.CharField(max_length=100)
    registro_conducir=models.CharField(max_length=100)
    seguro=models.CharField(max_length=100)
    telefono=models.CharField(max_length=20)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        txt="{0}\t{1},{2}\t{3}\t"
        return txt.format(self.cuil_cuit,self.apellido,self.nombre,self.vehiculo)