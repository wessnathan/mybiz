from django.contrib import admin
from .models import *
from django.conf import settings


# Register your models here.

admin.site.register(BussinessProducts)
admin.site.register(BusinessTeam)
admin.site.register(BizServices)
#admin.site.register(WorkingDays)


@admin.register(BizDetails)
class BizDetailsAdmin(admin.ModelAdmin):
    list_display = ('bussiness_Name','bussiness_Owner', 'created', 'status')
    list_filter = ('status', 'bussiness_Owner')
    search_fields = ('bussiness_Name', 'bussiness_Owner')
    prepopulated_fields = {'slug': ('bussiness_Name',), }
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')