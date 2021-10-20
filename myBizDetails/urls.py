from django.conf.urls import url
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('mybiz_user_email', views.mybiz_user_email, name='mybiz_user_email'),
    path('myBiz/', views.MyBizListView.as_view() , name='myBizlist' ), 
    #,views.UserDetailView.as_view(), name='userdetails'),
    path("myBiz/<int:pk>/", views.MyBizDetailView.as_view() , name='myBizDetails' ),
    path('myBiz/create/', views.MyBussinessCreateView.as_view() , name='myBiz' ),
    path("myBiz/<int:pk>/update", views.MyBussinessUpdateView.as_view() , name='myBizUpdate' ),
    path('myBiz/<int:pk>/delete/', views.MyBizDeleteView.as_view() , name='myBizDelete' ),
]