from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, PostDetailView, PostCreateView

urlpatterns = [
    path('', HomeView.as_view(), name="landing"),
    path('posts/', views.posts , name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-new')
]