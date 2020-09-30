from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import crearUsuario


urlpatterns = [
    path('login/',LoginView.as_view(template_name='registration/login.html'), name= 'login'),
    path('registrarse/',crearUsuario,name = 'registrarse'),
    path('logout/',LogoutView.as_view(),name = 'logout')
]