from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.http import request
from .models import UserProfile
from lipanampesa.models import Account_Payment_Mpesa
from django.db.models.signals import pre_save, post_save


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Account_Payment_Mpesa.objects.create(user=instance)
        


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    #instance.Account_Payment_Mpesa.save()
    
    
def create_trial_version(sender, instance, **kwargs):
    print('trial version started')
    
post_save.connect(create_trial_version, sender=User)