from django.urls import path
from facilitator import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('facilitatorsignup/', views.teacher_signup_view,name='facilitatorsignup'),
]