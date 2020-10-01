from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, PostDetailView, PostCreateView, misPedidosView, misPedidosDetailView, misEnvios

urlpatterns = [
    path('pedidos/', HomeView.as_view(), name='pedidos'),
    path('pedidos/<int:pk>', PostDetailView.as_view(), name='post-detail1'),
    path('misEnvios/', misEnvios, name='misEnvios'),
    path('misPedidos/', misPedidosView.as_view(), name='misPedidos'),
    path('misPedidos/<int:pk>', misPedidosDetailView.as_view(), name='detalleMiPedido'),
    path('pedidos/new', PostCreateView.as_view(), name='post-new1')
]