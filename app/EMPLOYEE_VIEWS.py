import requests
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app.models import*
from django.contrib import messages
from app.EmployerEmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

def dashboard(request):
    return render(request,'employer/dashboard.html')

def employer_addjobs(request):
    if request.method == "POST":
        job_pic=request.FILES.get('job_pic')
        jobs_name = request.POST.get('jobs_name')
        job_location = request.POST.get('job_location')
        min_sallery = request.POST.get('min_sallery')
        max_sallery = request.POST.get('max_sallery')
        sallery = request.POST.get('sallery')
        Vacancy = request.POST.get('Vacancy')
        # app_date = request.POST.get('app_date')
        desc = request.POST.get('desc')
        Skills = request.POST.get('Skills')
        Experience = request.POST.get('Experience')
        job = Job.objects.create(job_img=job_pic,job_name=jobs_name,job_location=job_location,min_sallery=min_sallery,max_sallery=max_sallery,Vacancy=Vacancy,job_des=desc,job_skill=Skills,job_experience=Experience,salary=sallery)
        job.save()
        messages.success(request,"Successfully Created Jobs")
    else:
        messages.error(request,"Failed to Create Jobs")

    return render(request,'employer/add_jobs.html')

def employer_register(request):
    
    return render(request,'employer/register.html')
def employer_doregister (request):
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    address=request.POST.get("address")

    try:
        user=CustomUser.objects.create_user(first_name=fname,last_name=lname,username=username,password=password,email=email,user_type=2)
        user.employee.address=address
        user.save()
        messages.success(request,"Successfully Created Employee")
        # return HttpResponse("success")
        return HttpResponseRedirect(reverse("employer_login"))
    except:
        messages.error(request,"Failed to Create Employee")
        
        return HttpResponseRedirect(reverse("employer_register"))

   
def employer_login(request):
    return render(request,'employer/login.html')


def employer_dologin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        captcha_token=request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LeWtqUZAAAAANlv3se4uw5WAg-p0X61CJjHPxKT"
        cap_data={"secret":cap_secret,"response":captcha_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)

        if cap_json['success']==False:
            messages.error(request,"Invalid Captcha Try Again")
            return HttpResponseRedirect(reverse("employer_login"))
            # return HttpResponseRedirect("employer_login")

        user=EmailBackEnd.authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="2":
                return HttpResponseRedirect(reverse("dashboard"))
                # return HttpResponseRedirect('/admin_home')
            # elif user.user_type=="2":
            #     return HttpResponseRedirect(reverse("staff_home"))
            # elif user.user_type=="4":
            #    # return HttpResponse("MEMBERS PANEL")
            #     return HttpResponseRedirect(reverse("dashboard"))
            else:
                return HttpResponseRedirect(reverse("employer_login"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("employer_login")


