from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import serializers
from myBizDetails.models import BizDetails, BizServices, BussinessProducts, BusinessTeam
from myBizDetails.models import User
from django.http import JsonResponse
from .serializers import BizDetailsSerializer, BussinessProductsSerializer, BizServicesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response




#serializers
@api_view(['GET'])
def bizdetailsList(request):
    bizdetails = BizDetails.objects.all()
    serializer = BizDetailsSerializer(bizdetails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bizservicelist(request):
    bizservices = BizServices.objects.all()
    serializer = BizServicesSerializer(bizservices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bussinessProductList(request):
    bussinessProducts = BussinessProducts.objects.all()
    serializer = BussinessProductsSerializer(bussinessProducts, many=True)
    return Response(serializer.data)
    
    
@api_view(['GET'])
def bizDetail(request, pk):
    try:
        bizdetails = BizDetails.objects.get(id=pk)
        serializer = BizDetailsSerializer(bizdetails, many=False)
        return Response(serializer.data)

    except:
        return HttpResponse
        

@api_view(['GET'])
def bizservicesDetail(request, pk):
    try:
        bizservice =BizServices.objects.get(id=pk)
        serializer = BizServicesSerializer(bizservice, many=False)
        return Response(serializer.data)
    
    except:
        return HttpResponse

@api_view(['POST'])
def myBizCreate(request):
    serializer = BizDetailsSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
    return Response(new_data)


@api_view(['POST'])
def myBizUpdate(request, pk):
    bizdetails = BizDetails.objects.get(id=pk)
    serializer = BizDetailsSerializer(instance=bizdetails, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def myBizDelete(request, pk):
    bizdetails = BizDetails.objects.get(id=pk)
    bizdetails.delete()
    
    return Response('Data deleted Successfully')




    





