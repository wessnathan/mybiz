from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from .models import *

class lipa_account_na_mpesa(forms.ModelForm):
    class Meta:
        model = Account_Payment_Mpesa
        fields = ['account_phone_number','amount_paid', 'account_valid_days']