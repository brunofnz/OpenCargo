"""from django.contrib import admin
from django.urls import path
from . import views
from apps.registrarCliente.views import sign_upCLIENTE, sign_upCONDUCTOR, registrar
#from .views import HomeView, PostDetailView, PostCreateView

urlpatterns = [
    path('', sign_upCLIENTE,name='registrar'),
    path('SerConductor/', sign_upCONDUCTOR,name='sign_upCONDUCTOR'),
]"""

from django.urls import path
from .views import UserRegisterView

urlpatterns = [
     path('registro/', UserRegisterView.as_view(), name='registro'),
     #path('login/', UserRegisterView.as_view(), name='login'),
]


