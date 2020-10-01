from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import crearUsuario,completarDatos, regsitrarseTransportista, miCuenta


urlpatterns = [
    path('login/',LoginView.as_view(template_name='registration/login.html'), name= 'login'),
    path('registrarse/',crearUsuario,name = 'registrarse'),
    path('completarDatos/',completarDatos,name = 'completarDatos'),
    path('serTrnasportista/',regsitrarseTransportista,name = 'registrarseTransportista'),
    path('micuenta/',miCuenta,name = 'micuenta'),
    path('logout/',LogoutView.as_view(),name = 'logout')
]