# app/urls.py

from django.urls import path
from . import views
from .views import DetailView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register_view, name='register'),
    path('login/', views.user_login, name='login'),
    path('jobs/', views.job_create_view, name='jobs'),
    path('job/update/<int:job_id>/', views.job_update_view, name='job_update'),
    path('job/delete/<int:job_id>/', views.job_confirm_delete_view, name='job_confirm_delete'),
    path('job/<int:pk>/', DetailView.as_view(), name='job-detail'),
]
