"""OpenCargo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#landingPage, pagina principal o la del dominio
from OpenCargo.views import landingPage, preguntas

#app de registrar
from apps.registrarCliente.views import sign_upCLIENTE, sign_upCONDUCTOR, registrar

#app de postear
from apps.post.views import HomeView, PostDetailView, PostCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingPage, name='landingPage'),
    path('PreguntasFrecuentes/', preguntas, name='PreguntasFrecuentes'),
    path('signUp-Cliente/', sign_upCLIENTE,name='sign_upCLIENTE'),
    path('signUp-Conductor/', sign_upCONDUCTOR,name='sign_upCONDUCTOR'),
    path('registrar/', registrar,name='Registrar'),


    path('home/', HomeView.as_view(), name="landing"),
    path('blog/', include('apps.post.urls')), ## blog/home/
    path('blog/post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/new', PostCreateView.as_view(), name='post-new')
]
