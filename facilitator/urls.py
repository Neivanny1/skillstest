from django.urls import path
from facilitator import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('facilitatorhome/', views.facilitatorhome, name='facilitatorhome'),
    path('facilitatorsignup/', views.facilitator_signup_view, name='facilitatorsignup'),
    path('facilitatorlogin/', LoginView.as_view(template_name='facilitator/login.html'), name='facilitatorlogin'),
    path('facilitatordashboard/', views.facilitator_dashboard_view, name='facilitatordashboard'),
    path('addchallenge/', views.add_challenge_view, name='addchallenge'),
    path('addorviewchallenge', views.add_or_view_challenge_view, name='addorviewchallenge'),
    path('viewchallenge', views.viewchallengeview, name='viewchallenge')
]
