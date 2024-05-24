from django.urls import path
from facilitator import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('facilitatorhome/', views.facilitatorhome, name='facilitatorhome'),
    path('facilitatorsignup/', views.facilitator_signup_view, name='facilitatorsignup'),
    path('facilitatorlogin/', LoginView.as_view(template_name='facilitator/login.html'), name='facilitatorlogin'),
    path('facilitatordashboard/', views.facilitator_dashboard_view, name='facilitatordashboard'),
    path('addchallenge/', views.add_challenge_view, name='addchallenge'),
    path('addorviewchallenge/', views.add_or_view_challenge_view, name='addorviewchallenge'),
    path('viewchallenge/', views.viewchallengeview, name='viewchallenge'),
    path('deletechallenge/<int:pk>', views.challenge_del_view, name='deletechallenge'),
    path('addorviewquestion/', views.add_or_view_question_view, name='addorviewquestion'),
    path('viewquestions/', views.viewquestionsview, name='viewquestions'),
    path('viewquestion/<int:pk>', views.view_question_view, name='viewquestion'),
    path('addquestion/', views.add_question_view, name='addquestion'),
    path('removequestion/<int:pk>', views.remove_question_view, name='removequestion'),
]
