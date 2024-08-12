# app/urls.py

from django.urls import path
from . import views
from .views import DetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('Sign up/register/', views.register_view, name='register'),
    path('job/<int:pk>/', DetailView.as_view(), name='job-detail'),
    # path('login/', views.login_view, name='login'),
]
