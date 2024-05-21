from django.urls import path
from participant import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('participanthome/', views.participanthome, name='participanthome'),
    path('participantlogin/', LoginView.as_view(template_name='participant/login.html'), name='participantlogin'),
    path('participantsignup/', views.participant_signup_view, name='participantsignup'),
    path('participantdashboard/', views.participant_dashboard_view, name='participantdashboard'),
]
