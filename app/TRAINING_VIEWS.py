import requests
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app.models import*
from django.contrib import messages
from app.EmployerEmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def TRAINING_Register(request):
    return render(request,'TRAINING/register.html')

def TRAINING_login(request):
    return render(request,'TRAINING/login.html')

@login_required(login_url='TRAINING_login')
def TRAINING_process(request):
    return render(request,'TRAINING/process.html')
