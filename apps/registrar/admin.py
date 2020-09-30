from django.contrib import admin
from .models import Provincia,Localidad,Usuario,Transportista,Vehiculo
# Register your models here.

admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Usuario)
admin.site.register(Transportista)
admin.site.register(Vehiculo)