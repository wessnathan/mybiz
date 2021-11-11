from django import template
from django.core.checks import messages
from django.db.models import query
from myBizDetails.models import User
from django.contrib.auth.decorators import login_required
from myBizDetails.forms import MyBizUpdateForm
from django.views.generic import ListView,DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.template import RequestContext
from myBiz.settings import EMAIL_HOST_USER
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myBizDetails.models import *
from myBizDetails.forms import MyBizServicesForm



def home(request):
    return render(request, 'myBizDetails/index.html')


def myBizView(request):
    return render(request, 'myBizDetails/mybizview.html')


def mybiz_user_email(request):
    
    if request.method == "POST":
        subject = request.POST['cf-subject']
        sent_by = request.POST['cf-email']
        message = request.POST['cf-message']
        
        email_body = f"{subject} {message} Sent by {sent_by }. "
        
        if subject and sent_by and email_body:
            try:
                send_mail(subject, email_body,sent_by, ['mybizcentre01@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/')
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
    
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        #context['bizservices'] = BizServices.objects.filter(service_id=)
        return context
    
    def owner(request):
        user = request.user
        return render(user)
    
    
    
#CREATE, UPDATE AND DELETE VIEW FOR BUSSINESS INFORMATION
class MyBussinessCreateView(LoginRequiredMixin, CreateView):
    
    template_name = 'myBizDetails/bizdetails_form.html'
    form_class = MyBizUpdateForm
    
    def form_valid(self, form):
        form.instance.bussiness_Owner = self.request.user
        return super().form_valid(form)
    
    
    messages.Info( f'Any other recent posts will be Deleted ')
    
class MyBussinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    queryset = BizDetails.objects.all()
    template_name = 'myBizDetails/bizdetails_form.html'
    form_class = MyBizUpdateForm
    
    messages.Info(f'Fill all theFields in the Form.')
    
    
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

#search bussiness owner function
def search_biz(request):
    if request.is_ajax():
        res = None
        biz = request.POST.get('biz')
        qs = User.objects.filter(username__icontains=biz)
        if len(qs) > 0 and len(biz) > 0:
            data = []
            
            for match in qs:
                rest = {
                    'pk':match.pk,
                    'username':match.username,
                    'email':match.email,
                    
                }
                data.append(rest)
                res = data
        else:
            res = 'No such user account'
        return JsonResponse({'data':res})
    return JsonResponse({})


#create services, update and delete

    
class ServiceListView(ListView):
    models = BizServices
    queryset = BizServices.objects.all()
    template_name = 'myBizDetails/bizservices_list.html'
    context_object_name = 'myservices'
    
    
    def owner(request):
        user = request.user
        return render(user)

class ServiceDetailView(DetailView):
    models = BizServices
    queryset = BizServices.objects.all()
    
    
    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        return context


class ServiceCreateView(LoginRequiredMixin, CreateView):
    
    template_name = 'myBizDetails/bizservice_form.html'
    form_class = MyBizServicesForm
    
    def form_valid(self, form):
        form.instance.service_id = self.request.user
        return super().form_valid(form)
    
class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    queryset = BizServices.objects.all()
    template_name = 'myBizDetails/bizservice_form.html'
    form_class = MyBizServicesForm
    
    
    def get_absolute_url(self):
        return reverse('serviceupdate', kwargs={'pk':self.pk})
    
    def form_valid(self, form):
        form.instance.service_id = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        servicePost = self.get_object()
        
        if self.request.user == servicePost.service_id:
            return True
        return False
    
class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    models = BizServices
    queryset = BizServices.objects.all()
    success_url = '/'
    
    def test_func(self):
        servicePost = self.get_object()
        
        if self.request.user == servicePost.service_id:
            return True
        return False

