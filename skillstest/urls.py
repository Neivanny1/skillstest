from django.contrib import admin
from django.urls import path, include
from challenge import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('participant/', include('participant.urls')),
    path('facilitator/', include('facilitator.urls')),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),


    # URLS FROM CHALLENGE views file
    path('adminlogin/', LoginView.as_view(template_name='challenge/adminLogin.html'), name='adminlogin'),
    path('admindash/', views.admin_dashboard_view, name='admindash'),
    path('adminhome/', views.admin_home_view, name='adminhome'),
    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    path('contactus/', views.contactus_view, name='contactus'),
    path('aboutus/', views.aboutus_view, name='aboutus'),

    #Handling facilitators
    path('checkpending/', views.check_pending_approval_view, name='checkpending'),
    path('approvepending/<int:pk>', views.approve_pending_view, name='approvepending'),
    path('rejectpending/<int:pk>', views.reject_pending_view, name='rejectpending'),
    path('viewfacilitators/', views.view_facilitators_view, name='viewfacilitators'),
    path('viewfacilitator/', views.view_facilitator_view, name='viewfacilitator'),
    path('totalpayout/', views.total_payout_view, name='totalpayout'),
    path('updatefacilitator/<int:pk>', views.update_facilitator_view, name='updatefacilitator'),
    path('deletefacilitator/<int:pk>', views.delete_facilitator_view, name='deletefacilitator'),

    #Handling participants
    path('viewparticipants/', views.view_participants_view, name='viewparticipants'),
    path('viewparticipant/', views.view_participant_view, name='viewparticipant'),
    path('allparticipantsmarks/', views.view_participants_marks_view, name='allparticipantsmarks'),
    path('updateparticipant/<int:pk>', views.update_participant_view, name='updateparticipant'),
    path('deleteparticipant/<int:pk>', views.delete_participant_view, name='deleteparticipant'),
    path('viewmarks/<int:pk>', views.view_marks_view, name='viewmarks'),
    path('admincheckmarks/<int:pk>', views.admincheck_marks_view, name='admincheckmarks'),
]
