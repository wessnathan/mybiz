from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from .choices import weekdays, times

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')
    
    
class BizDetails(models.Model):
    id =models.AutoField(primary_key=True)
    bussinessStatus = (
        ('Draft', 'Draft'),('Created', 'Created'),('Active', 'Active'),('Deactive', 'Deactive'),
    )
    bussiness_Owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bussiness_Type = models.CharField(max_length=100, default=' ')
    bussiness_Logo = models.CharField(max_length=13, default='any word')
    bussiness_Name = models.CharField(max_length=100, unique=True, default=' ')
    bussiness_Info = models.CharField(max_length=100, unique=True, default=' ')
    bussiness_Description = models.TextField(default='')
    about_Services_Offered = models.TextField(default=' ')
    bussiness_Goals = models.TextField(default=' ')
    week_day = models.CharField(max_length=25, choices=weekdays, default='Monday - Friday')
    time = models.CharField(max_length=18, choices=times, default='9.00 AM - 5.00 PM')
    weekend = models.CharField(max_length=25, choices=weekdays, default='Saturday')
    weekend_opens = models.CharField(max_length=18, choices=times, default='10.00 AM - 2.00 PM')
    bussiness_Facebook = models.CharField(max_length=100, default=' ')
    bussiness_Instagram = models.CharField(max_length=100, default=' ')
    bussiness_Whatsapp = models.CharField(max_length=12, default='+2547 ')
    bussiness_Linkedin = models.CharField(max_length=100, default=' ')
    bussiness_Email = models.EmailField( default=' ')
    bussiness_Address = models.CharField(max_length=50, default=' ')
    bussiness_Location = models.CharField(max_length=50, default='Nairobi,Kenya ')
    bussiness_Background_Image = models.ImageField(default='homepage/bs4.jpg', upload_to='homepage/')
    image_of_bussiness = models.ImageField(default='bussiness/default.jpg', upload_to='bussiness/')
    image_of_manager = models.ImageField(default='manager/default.jpg', upload_to='manager/')
    slug = models.SlugField(max_length=250, unique_for_date='created')
    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=bussinessStatus, default='active')
    
    objects = models.Manager() # The default manager.
    published = ActiveManager()
    
    class Meta:
        verbose_name_plural = "Bussiness Information"
        ordering = ('-publish',)
    def __str__(self):
        return self.bussiness_Name
    
    def get_absolute_url(self):
        return reverse('userdetails', args=[str(self.bussiness_Owner)])  #args=[int(self.id)]
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.bussiness_Owner)
        super(BizDetails, self).save(*args, **kwargs)
        
        '''if BizDetails.objects.filter(bussiness_Owner=self.bussiness_Owner).count() == 1:
        else:
            first_post = BizDetails.objects.filter(bussiness_Owner=self.bussiness_Owner).first()
            first_post.delete()
            print('Old post deleted. You cannot have two posts')
            
        pre_save.connect(save,sender=BizDetails)'''
        
class BizServices(models.Model):
    service_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    service_title = models.CharField(max_length=40, default=' ')
    service = models.CharField(max_length=200, default=' ')
    service_photo = models.ImageField(upload_to='services')
    
    def __str__(self):
        return self.service_title
    
    def get_absolute_url(self):
        return reverse('service_detail', args=[int(self.id)])
    
    class Meta:
        verbose_name_plural = 'Service Offered By User'
    
    
class BussinessProducts(models.Model):
    id =models.AutoField(primary_key=True)
    bussinessOwnerId = models.ForeignKey(BizDetails, on_delete=CASCADE)
    productName = models.CharField(max_length=50, default=' ')
    productDescription = models.CharField(max_length=300, default=' ')
    productImage = models.ImageField()
    
    def get_absolute_url(self):
        return reverse('myProducts', args=[self.id])
    
    def __str__(self):
        return self.productName
    class Meta:
        verbose_name_plural = "Bussiness Products"
    
class BusinessTeam(models.Model):
    id =models.AutoField(primary_key=True)
    bussinessOwnerId = models.ForeignKey(BizDetails, on_delete=CASCADE)
    fullNameOfMember = models.CharField(max_length=50, default=' ')
    roleOfMember = models.CharField(max_length=50, default=' ')
    photoOfMember = models.ImageField()
    
    def __str__(self):
        return self.fullNameOfMember
    class Meta:
        verbose_name_plural = "Bussiness Team Members"

