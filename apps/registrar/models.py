from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 60, blank=False, null=False)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length= 60, blank=False, null=False)

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length= 50, blank=False, null=False)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    cuil_cuit = models.CharField(max_length= 50, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False,null=False)
    fecha_alta = models.DateField(auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id_usuario']

    def __str__(self):
        return "{}".format(self.user)



class Transportista(models.Model):
    id_transportista = models.AutoField(primary_key=True)
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cedula_azul = models.CharField(max_length= 200, blank=False, null=False)
    cedula_verde = models.CharField(max_length= 200, blank=False, null=False)
    fecha_alta = models.DateField(auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Transportista'
        verbose_name_plural = 'Transportistas'
        ordering = ['id_transportista']

    def __str__(self):
        return "{}, {}".format(self.user.user.last_name,self.user.user.first_name)

class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    transp_id = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    tipo = models.CharField(max_length= 200, blank=False, null=False)
    venc_tecnica = models.DateField(blank=False, null=False)
    patente = models.CharField(max_length= 200, blank=False, null=False)
    marca =models.CharField(max_length= 200, blank=False, null=False)
    modelo = models.CharField(max_length= 200, blank=False, null=False)
    capacidad = models.CharField(max_length= 200, blank=False, null=False)
    fecha_alta = models.DateField(auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        ordering = ['tipo']

    def __str__(self):
        return "{} {} {}".format(self.tipo,self.capacidad,self.venc_tecnica)



    