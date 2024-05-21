from django.contrib import admin
from django.urls import path, include
from challenge import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('participant/', include('participant.urls')),
    path('challenge/', include('challenge.urls')),
    path('facilitator/', include('facilitator.urls')),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    path('contactus/', views.contactus_view, name='contactus'),
    path('aboutus/', views.aboutus_view, name='aboutus'),
]
