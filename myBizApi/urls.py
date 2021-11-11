from django.urls import path
from . import views


urlpatterns = [
    #serializers views
    path('myBizList/', views.bizdetailsList, name='myBizList' ),
    path('myBizDetails/<str:pk>/', views.bizDetail, name='myBizDetails' ),
    path('myBizCreate/<int:pk>', views.myBizCreate, name='myBizCreate' ),
    path('myBizUpdate/<str:pk>/', views.myBizUpdate, name='myBizUpdate' ),
    path('myBizDelete/<str:pk>/', views.myBizDelete, name='myBizDelete' ),
    #services
    path('serviceapi/', views.bizservicelist, name='servicesapi' ),
    path('serviceapi/<str:pk>/', views.bizservicesDetail, name='detailservicesapi' ),
]
