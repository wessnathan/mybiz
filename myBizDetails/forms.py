from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import *

class MyBizUpdateForm(forms.ModelForm):
    class Meta:
        model = BizDetails
        exclude = ['bussiness_Owner','slug','publish','status','created','updated',]
        
#class MyBizForm(forms.ModelForm):
    #class Meta:
        #