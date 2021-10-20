from django.conf.urls import url, include
from . import views
from myBizUsers.views import registeration, dashboard, currentProfile, profile
from django.urls import path


urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path('currentprofile/', views.currentProfile, name='currentprofile'),
    path('profile/', profile, name='profile'),
    path('register/', views.registeration , name='register'),
    
    
]