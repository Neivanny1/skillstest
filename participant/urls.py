from django.urls import path
from participant import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('participanthome/', views.participanthome, name='participanthome'),
    path('participantlogin/', LoginView.as_view(template_name='participant/login.html'), name='participantlogin'),
    path('participantsignup/', views.participant_signup_view, name='participantsignup'),
    path('participantdashboard/', views.participant_dashboard_view, name='participantdashboard'),
    path('viewchallenges/', views.view_challenges_view, name='viewchallenges'),
    path('joinchallenge/<int:pk>', views.join_challenge_view, name='joinchallenge'),
    path('startchallenge/<int:pk>', views.start_challenge_view, name='startchallenge'),
    path('calculatemarks/', views.calculate_marks_view, name='calculatemarks'),
    path('viewresult/', views.view_result_view, name='viewresult'),
    path('checkmarks/<int:pk>', views.check_marks_view, name='checkmarks'),
    path('viewhistory/', views.view_history_view, name='viewhistory'),
]
