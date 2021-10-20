from django.conf.urls import url, include
from django.urls import path
from .views import lipaAccount


urlpatterns = [
    path("account-payment/", lipaAccount, name="payaccount"),
]