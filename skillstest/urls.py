# skillstest/urls.py
from django.contrib import admin
from django.urls import path, include
from challenge import views as challenge_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', challenge_views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('participant/', include('participant.urls')),
    path('challenge/', include('challenge.urls')),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('afterlogin/', challenge_views.afterlogin_view, name='afterlogin'),
    path('contactus/', challenge_views.contactus_view, name='contactus'),
    path('aboutus/', challenge_views.aboutus_view, name='aboutus'),
]
