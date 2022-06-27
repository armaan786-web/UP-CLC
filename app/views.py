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




# Create your views here.
def home(request):
    

    return render(request,'homepage/home.html')

def joblisting(request):
     return render(request,'homepage/job_listing.html')

def about(request):
     return render(request,'homepage/about.html')

def contact(request):
     return render(request,'homepage/contact.html')

def regi(request):
    role = Role.objects.all()
    return render(request,'homepage/register.html',{'role':role})


def douserregister(request):
   if request.method == "POST":

      role_id = request.POST.get("role")
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      username = request.POST.get("username")
      father_name = request.POST.get("father_name")
      gender = request.POST.get("gender")
      mobile_no = request.POST.get("mobile_no")
      dob = request.POST.get("dob")
      adhaar = request.POST.get("adhaar")
      pan_no = request.POST.get("pan_no")
      caste = request.POST.get("caste")
      city = request.POST.get("city")
      state = request.POST.get("state")
      pin = request.POST.get("pin")
      address = request.POST.get("address")
      email = request.POST.get("email")
      
      password = ("123456")
      

      role=Role.objects.get(id=role_id)

      amount = int(request.POST.get("amount"))*100 
      client=razorpay.Client(auth =("rzp_test_czVP739sBN5blU" , "MBpgYsg92tAkraZtv5BMyLeq"))
      
      payment=client.order.create({'amount':amount, 'currency':'INR' , 'payment_capture' : '1'})
      user=CustomUser.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,adhaar=adhaar,password=password,user_type=4)
      user.member.father_name=father_name
      user.member.gender=gender
      user.member.mobile_no=mobile_no
      user.member.dob=dob
      # user.member.adhaar=adhaar
      user.member.pan_no=pan_no
      user.member.caste=caste
      user.member.city=city
      user.member.state=state
      user.member.pin=pin
      # user.member.email=email
      user.member.address=address

      user.member.role_id=role

      user.member.amount=amount
      user.member.payment_id=payment['id']
      user.save()
      context = {
         'fname':fname,
         'lname':lname,
         'username':username,
         'email':email,
         'payment':payment

      }

      
      # coffee=Coffee(name = name , amount = amount , payment_id = payment['id'])
      # coffee.save()
      return render(request , 'homepage/doregister.html',context)
   return render(request,'homepage/doregister.html')
        
        # name = request.POST.get("firstname")
     #    firstname = request.POST.get("fname")
     #    lastname = request.POST.get("lname")
      #   username = request.POST.get("username")
      #   mobile_no = request.POST.get("mobile_no")
      #   father_name = request.POST.get("father_name")
      #   gender = request.POST.get("gender")
      #   password = request.POST.get("password")
      #   address = request.POST.get("address")

      #   amount = int(request.POST.get("amount"))*100 
      #   client=razorpay.Client(auth =("rzp_test_Ry0NdyRbZevRle" , "9kPb02DDhfBNr1LmjFVkJONX"))
        
      #   payment=client.order.create({'amount':amount, 'currency':'INR' , 'payment_capture' : '1'})
     #    user=CustomUser.objects.create_user(username=username,password=password,user_type=4)
     #    user.member.address=mobile_no
     #    user.member.address=father_name
     #    user.member.address=gender
     #    user.member.address=address
     #    user.member.amount=amount
     #    user.member.payment_id=payment['id']
     #    user.save()

        
        # coffee=Coffee(name = name , amount = amount , payment_id = payment['id'])
        # coffee.save()
      #   return render(request , 'homepage/home.html', {'payment':payment})
   #  return render(request,'homepage/home.html')
@csrf_exempt
def Success(request):
 if request.method=="POST":
     a=request.POST
     print(a)
     order_id=""
     for key,val in a.items():
      if key=="razorpay_order_id":
        order_id = val
        break
     user=Member.objects.filter(payment_id=order_id).first() 
     user.paid=True
     user.save()
 return render(request , 'homepage/success.html')   

def doLogin(request):
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
            return HttpResponseRedirect("/")

        user=EmailBackEnd.authenticate(request,username=request.POST.get("adhaarNo"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="4":
                return HttpResponseRedirect(reverse("member_dashboard"))
                # return HttpResponseRedirect('/admin_home')
            # elif user.user_type=="2":
            #     return HttpResponseRedirect(reverse("staff_home"))
            # elif user.user_type=="4":
            #    # return HttpResponse("MEMBERS PANEL")
            #     return HttpResponseRedirect(reverse("dashboard"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")



