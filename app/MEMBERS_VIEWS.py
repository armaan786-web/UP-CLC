from django.shortcuts import redirect, render
from .models import*


def dashboard(request):
    return render(request,'MEMBERS/dashboard.html')

def payment_information(request):
    member = Member.objects.all()

    return render(request,'MEMBERS/payment_info.html',{'member':member})