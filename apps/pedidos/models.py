from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Pedido(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    desde = models.CharField(max_length=255,null=True)
    hasta = models.CharField(max_length=255,null=True)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_llegada = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=255,null=True)
    paquetes = models.CharField(max_length=255,null=True)
    peso = models.CharField(max_length=255,null=True)
    descripcion = models.TextField(null=True)
    disponibilidad = models.CharField(max_length=255,null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id) + ' | ' + str(self.author) + ' | ' + self.desde + ' --> ' + self.hasta

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))

class Envio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pedido =  models.ForeignKey(Pedido, on_delete=models.CASCADE)
    entregado = models.CharField(max_length=255,null=True)
    estado = models.CharField(max_length=255,null=True)
    fecha_alta = models.DateField(auto_now=True,auto_now_add=False)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id) + ' | ' + str(self.author) + ' | entregado: ' + self.entregado 

