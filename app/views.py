import json
from django.shortcuts import redirect, render
import requests
import razorpay
from .models import*
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    job = Job.objects.all().order_by('id')[0:5]

    return render(request,'homepage/home.html',{'job':job})

def joblisting(request):
    job = Job.objects.all()
    return render(request,'homepage/job_listing.html',{'job':job})


def jobdetails(request,pk):
    
    job=Job.objects.all().filter(id=pk)

    return render(request,'homepage/job_details.html',{'job':job})

def course(request):
     course = Course.objects.all()
     return render(request,'homepage/course.html',{'course':course})

def about(request):
     return render(request,'homepage/about.html')

def contact(request):
     return render(request,'homepage/contact.html')
     
@login_required(login_url='member_login')
def apply(request):
     return render(request,'homepage/apply.html')



