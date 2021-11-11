from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from .models import *

class MyBizUpdateForm(forms.ModelForm):
    class Meta:
        model = BizDetails
        exclude = ['bussiness_Owner','slug','publish','status','created','updated',]
        
        
class MyBizServicesForm(forms.ModelForm):
    class Meta:
        model = BizServices
        exclude = ['service_id']
        #fields = '__all__'
        
#class MyBizForm(forms.ModelForm):
    #class Meta:
        #