from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Transportista, Vehiculo


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            
        ]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'user',
            'cuil_cuit',
            'fecha_nacimiento',
            'direccion',
            'localidad'
        ]

class TransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        fields = [
            'user',
            'cedula_azul',
            'cedula_verde',
        ]

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'transp_id',
            'tipo',
            'venc_tecnica',
            'patente',
            'marca',
            'modelo',
            'capacidad'
        ]

