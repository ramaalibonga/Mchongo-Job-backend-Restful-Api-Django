from xmlrpc.client import ResponseError
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import EmailList,JobDetails,Address,Location
from json import dumps
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from rest_framework.response import  Response
from rest_framework import viewsets
from .serializer import EmailListSerializer,JobDetailsSerializer,AddressSerializer,LocationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class EmailListViews(viewsets.ModelViewSet):
      
      queryset = EmailList.objects.all()
      serializer_class = EmailListSerializer


class JobDetailsViews(viewsets.ModelViewSet):
      authentication_classes = [JWTAuthentication]
      permission_classes = [IsAuthenticated]
      queryset = JobDetails.objects.all()
      serializer_class = JobDetailsSerializer


class AddressViews(viewsets.ModelViewSet):
      authentication_classes = [JWTAuthentication]
      permission_classes = [IsAuthenticated]
      queryset = Address.objects.all()
      serializer_class = AddressSerializer


class LocationViews(viewsets.ModelViewSet):
      authentication_classes = [JWTAuthentication]
      permission_classes = [IsAuthenticated]
      queryset = Location.objects.all()
      serializer_class = LocationSerializer

# adding email address
def create_email(request):
    if request.method =="GET":
        if request.GET.get('email') ==" ":
            return HttpResponse(status=405)
        if request.GET.get('email') is not None:
             email_user = request.GET.get('email')
             if EmailList.objects.filter(email=email_user).exists():
                return HttpResponse("Email alread exist ")
             EmailList.objects.create(email=email_user)
             return HttpResponse("Email created successfully")
        return HttpResponse(status=405)
    return HttpResponse({"valid":False},status=404)
def description(request,id):
      jobdetails = JobDetails.objects.filter(pk=id)
      return render(request,'description.html',{'description':jobdetails})
def details(request):
        jobdetails = JobDetails.objects.filter(country=request.GET.get("id"))
        seliazer_object = serializers.serialize('json',jobdetails) 
        return HttpResponse(seliazer_object)
    
def search(request):
       jobdetails = JobDetails.objects.filter(country__contains =request.GET.get("country"))
       seliazer_object = serializers.serialize('json',jobdetails) 
       return HttpResponse(seliazer_object)
def home(request):
     querySet = JobDetails.objects.all()
     seliazer_object = serializers.serialize('json',querySet)  
    #  json = dumps(seliazer_object)
     return render(request,'index.html',{'items':seliazer_object,'item':querySet})
def login_home(request):
    return render(request,'login.html')

#login function
def signin(request):
        if request.method =="POST":
           if request.POST["username"] ==" " and request.POST["password"] ==" ":
                   return render(request,'login.html')
           username1 = request.POST["username"]
           password1 = request.POST["password"]
           auth_user = authenticate(request,username=username1,password=password1)
           if auth_user is not None:
                  login(request,auth_user)
                  return render(request,'index.html')
           return render(request,'login.html')

def signup(request):
     return render(request,'signup.html')
def signout(request):
           logout(request)
           return render(request,'login.html')


                        