from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, PostDetailView, PostCreateView

urlpatterns = [
    path('pedidos/', HomeView.as_view(), name='pedidos'),
    path('pedidos/<int:pk>', PostDetailView.as_view(), name='post-detail1'),
    path('pedidos/new', PostCreateView.as_view(), name='post-new1')
]