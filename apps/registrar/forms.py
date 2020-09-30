from django import forms
from django.contrib.auth.models import User
from .models import Usuario


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        ]


