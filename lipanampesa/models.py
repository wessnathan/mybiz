from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta 

# Create your models here.

class Account_Payment_Mpesa(models.Model):
    duration = (
        ('365', '365'),
        ('730', '730'),
        ('1095', '1095'),
    )
    plans = (
        ('250', '250'),
        ('500', '500'),
        ('1000', '1000'),
    )
    expiry_days = timedelta(365)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_phone_number = models.CharField(default='2547xxxxxx05', max_length=12)
    amount_paid = models.CharField(choices=plans, default=500, max_length=4)
    account_valid_days = models.CharField(choices=duration,  max_length=4, blank=False, default='Days')
    user_account_duration = models.PositiveIntegerField(blank=False, default='1')
    #user_account_plan = models.CharField(choices=plans, max_length=10, blank=False, default=' ')
    
    def __str__(self):
        return f"{self.user} Account Expiring in  -{self.user_account_duration} {self.account_valid_days} time -  Amount Paid {self.amount_paid}"
    
    class Meta:
        verbose_name_plural = 'User Payment Plans'