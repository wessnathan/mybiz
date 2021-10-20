from myBizUsers.models import UserProfile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    
    email = forms.EmailField()
    User._meta.get_field('email')._unique = True
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        User._meta.get_field('username')._unique = True
        
        
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio','image','contact']
        

