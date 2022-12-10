from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogPost, name='blog-api'),
    path('post/<int:id>/', views.blogPost, name='blog-api'),
]
