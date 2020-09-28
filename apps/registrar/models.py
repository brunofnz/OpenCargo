from django.db import models

# Create your models here.

class Transportista(models.Model):
    ide = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 200, blank=False, null=False)
    apellido = models.CharField(max_length= 200, blank=False, null=False)
    nacionalidad = models.CharField(max_length= 200, blank=False, null=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellido']

    def __str__(self):
        return "{}, {}".format(self.apellido,self.nombre)


    