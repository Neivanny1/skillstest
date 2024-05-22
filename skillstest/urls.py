from django.contrib import admin
from django.urls import path, include
from challenge import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('participant/', include('participant.urls')),
    path('facilitator/', include('facilitator.urls')),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),


    # URLS FROM CHALLENGE views file
    path('adminlogin/', LoginView.as_view(template_name='challenge/adminLogin.html'), name='adminlogin'),
    path('admindash/', views.admin_dashboard_view, name='admindash'),
    path('adminhome/', views.admin_home_view, name='adminhome'),
    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    path('contactus/', views.contactus_view, name='contactus'),
    path('aboutus/', views.aboutus_view, name='aboutus'),

    #Handling admin tasks
    path('checkpending/', views.check_pending_approval_view, name='checkpending'),
    path('approvepending/<int:pk>', views.approve_pending_view, name='approvepending'),
]
