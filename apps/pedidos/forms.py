from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'author',
            'desde',
            'hasta',
            'fecha_inicio',
            'fecha_llegada',
            'descripcion',
            'disponibilidad'
        ]
