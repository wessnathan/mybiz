from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
import time

def registeration(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        #form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!You can now login')
                return redirect('login')
                #return redirect('payaccount')
            
            except IntegrityError:
                username = form.cleaned_data.get('username')
                messages.success(request, f'The username {username}!has already been used. Please try another one')
    else:
        form = UserRegistrationForm()
            
    return render(request, 'registration/registration.html', {'form':form})


def dashboard(request):
    return render( request, 'users/dashboard.html')

def account_expiry_timer(t):
    duration = t * 86400
    while duration:
            mins,secs = divmod(duration,60)
            hours,mins = divmod(mins,60)
            days,hours = divmod(hours,24)
            timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours,mins,secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    print("Done deal..Account expiring")


@login_required

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            
            messages.success(request, f'You have updated your Profile Successfully!!')
            return redirect('currentprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, 'users/profile.html', context )

def currentProfile(request):
    return render(request, 'users/myprofile.html')

@login_required()
#when account expires
def user_deactivate(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    messages.success(request, "User account has been successfully deactivated!")
    return redirect('home')

@login_required()
#after making the payment
def user_activate(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "User account has been successfully activated!")
    return redirect('home')

'''
delete view
@login_required
@require_http_method(['POST'])
def remove_account(request):
    user_pk = request.user.pk
    auth_logout(request)
    User = get_user_model()
    User.objects.filter(pk=user_pk).delete()'''
    