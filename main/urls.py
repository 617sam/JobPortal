# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('Sign up/register/', views.register_view, name='register'),
    # path('login/', views.login_view, name='login'),
]
