from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True)
    image = models.ImageField(default='myBizProfilePic/default.jpg' , upload_to='myBizProfilePic/')
    gender_select = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_select, max_length=6)
    contact = models.CharField(max_length=12, default='2547')
    account_validity = models.CharField(max_length=3, default=366)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    '''def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        
        super().save(force_insert, force_update, using, update_fields)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width >300:
            img_output_size = (300,300)
            
            img.thumbnail(img_output_size)
            img.save(self.image.path)'''
            
    
