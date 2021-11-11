from django.conf.urls import url
from django.urls import path, re_path
from . import views


urlpatterns = [
    #landing page view
    path('', views.home, name='home'),
    
    #general business view 
    path('myBiz/', views.MyBizListView.as_view() , name='myBizlist' ), 
    path('myBiz/search/', views.search_biz, name='search'),
    path('mybiz_user_email', views.mybiz_user_email, name='mybiz_user_email'),
    
    #view to create and update users bussines information
    path('myBiz/create/', views.MyBussinessCreateView.as_view() , name='myBiz' ),
    path("myBiz/<int:pk>/update", views.MyBussinessUpdateView.as_view() , name='myBizUpdate' ),
    path('myBiz/<int:pk>/delete/', views.MyBizDeleteView.as_view() , name='myBizDelete' ),
    
    #service form view
    path('services/',views.ServiceListView.as_view(), name='service_list' ),
    path('services/<int:pk>',views.ServiceDetailView.as_view(), name='service_detail' ),
    path('services/create',views.ServiceCreateView.as_view(), name='service_create' ),
    path('services/<int:pk>/update',views.ServiceUpdateView.as_view(), name='serviceupdate' ),
    path('services/<int:pk>/delete',views.ServiceDeleteView.as_view(), name='servicedelete' ),
    
    
]