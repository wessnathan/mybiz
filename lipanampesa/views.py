from .forms import lipa_account_na_mpesa
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def lipaAccount(request):
    if request.method == "POST":
        accountForm = lipa_account_na_mpesa(request.POST, instance= request.user)
        
        if accountForm.is_valid():
            accountForm.save()
            messages.success(request, f'You have paid for your Account successfully')
            print('payment info saved ')
            return redirect('login')
            
    else:
        accountForm = lipa_account_na_mpesa()
        messages.warning(request, f"There is an error with your payment. ")
        
    context ={
            'accountForm':accountForm
        }
    
    return render(request, 'lipanampesa/lipanampesa.html', context)
    