from myBizDetails.models import User
from django.contrib.auth.decorators import login_required
from myBizDetails.forms import MyBizUpdateForm
from django.views.generic import ListView,DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myBizDetails.models import *



def home(request):
    return render(request, 'myBizDetails/index.html')


def myBizView(request):
    return render(request, 'myBizDetails/mybizview.html')

#send email to the owner of the bussiness


def mybiz_user_email(request, userEmail):
    
    if request.method == "POST":
        name = request.POST['cf-name']
        email = request.POST['cf-email']
        message = request.POST['cf-message']
        
        if name and email and message:
            try:
                send_mail(name, message, email, [userEmail])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            
            return HttpResponse('Make sure all fields are entered and valid.')
        
    else:
        return

#detail views and create

class MyBizListView(ListView):
    models = BizDetails
    queryset = BizDetails.objects.all()
    template_name = 'myBizDetails/bizdetails_list.html'
    context_object_name = 'singleBiz'
    
    def owner(request):
        user = request.user
        return render(user)
    
class UserListView(ListView):
    models = BizDetails
    template_name = 'myBizDetails/userdetailview_detail.html'
    context_object_name = 'myuser'
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BizDetails.objects.filter(bussiness_Owner=user)
    
    

class MyBizDetailView(DetailView):
    models = BizDetails
    queryset = BizDetails.objects.all()
    


class MyBussinessCreateView(LoginRequiredMixin, CreateView):
    
    template_name = 'myBizDetails/bizdetails_form.html'
    form_class = MyBizUpdateForm
    
    def form_valid(self, form):
        form.instance.bussiness_Owner = self.request.user
        return super().form_valid(form)
    
class MyBussinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    queryset = BizDetails.objects.all()
    template_name = 'myBizDetails/bizdetails_form.html'
    form_class = MyBizUpdateForm
    
    
    def get_absolute_url(self):
        return reverse('myBizUpdate', kwargs={'pk':self.pk})
    
    def form_valid(self, form):
        form.instance.bussiness_Owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        myBizPost = self.get_object()
        
        if self.request.user == myBizPost.bussiness_Owner:
            return True
        return False
    
class MyBizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    models = BizDetails
    queryset = BizDetails.objects.all()
    success_url = '/'
    
    def test_func(self):
        myBizPost = self.get_object()
        
        if self.request.user == myBizPost.bussiness_Owner:
            return True
        return False
    
    

