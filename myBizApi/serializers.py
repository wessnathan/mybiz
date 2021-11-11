from django.db import models
from rest_framework import fields, serializers
from myBizDetails.models import BizDetails, BussinessProducts,BusinessTeam, BizServices

class BizDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BizDetails
        exclude = ('publish','created','updated',)
        #fields = '__all__'
        
class BizServicesSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = BizServices
        fields = '__all__'
    
class BussinessProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BussinessProducts
        fields = '__all__'
        

class BussinessTeamserializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessTeam
        fields = '__all__'
        
        
