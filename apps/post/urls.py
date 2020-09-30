from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, PostDetailView, PostCreateView

urlpatterns = [
    path('viajes/', HomeView.as_view(), name='viajes'),
    path('viajes/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('viajes/new', PostCreateView.as_view(), name='post-new')
]