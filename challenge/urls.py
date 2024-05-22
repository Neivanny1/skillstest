# challenge/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admindash/', views.admin_dashboard_view, name='admindash'),
    path('adminhome/', views.admin_home_view, name='adminhome'),
]
