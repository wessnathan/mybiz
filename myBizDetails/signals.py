from django.contrib.auth.models import User
from django.dispatch import receiver
from django.http import request
from .models import BizDetails
from django.db.models.signals import pre_save, post_save
from django.core.checks import messages
from django.contrib import messages


@receiver(pre_save, sender=BizDetails)
def delete_old_post(sender, instance, created=True, **kwargs):
    if created:
        try:
            first_post = BizDetails.objects.filter(bussiness_Owner=instance.bussiness_Owner).first()
            first_post.delete()
            #messages.warning(f'the old Information about your bussiness hass been Deleted')
            print('Old post deleted. You cannot have two posts')
            print(instance.bussiness_Owner)
        except AttributeError:
            pass
    else:
        messages.success(f'Bussiness Informated Posted Successfully. To make Your Work Easier Always Use update page to add or edit more information about your Bussiness. Posting a new one will make The old one be deleted')
        print('no initial record')
        pass
        

'''
@receiver(post_save, sender=BizDetails)
def delete_saved_post(sender, instance, **kwargs):
    first_post = BizDetails.objects.filter(bussiness_Owner=instance.bussiness_Owner).first()
    first_post.delete()
    print('Old post deleted. You cannot have two posts. Only New post remaining')'''
    
