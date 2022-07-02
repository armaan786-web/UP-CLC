from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app.models import*
from django.contrib import messages

def HOD(request):
    member_count=Member.objects.all().count()
    role_count=Role.objects.all().count()
    instructor_count=Instructor.objects.all().count()
    return render(request,'HOD/dashboard.html',{'member_count':member_count,'role_count':role_count,'instructor_count':instructor_count})



def ADD_ROLE(request):
    if request.method == 'POST':
        role = request.POST.get('role')

        try:
            
            if Role.objects.filter(role_name = role).exists():
                messages.warning(request,role + " is already Taken ")
                return redirect('add_role')
            rolee = Role.objects.create(role_name=role)
            rolee.save()
            messages.success(request,"Successfully Created Role")
            return HttpResponseRedirect(reverse("add_role"))
        except:
            messages.error(request,"Failed to Create Role")
            return HttpResponseRedirect(reverse("add_role"))

    return render(request,'HOD/add_role.html')

def MANAGE_ROLE(request):
    role = Role.objects.all()

    return render(request,'HOD/manage_roll.html',{'role':role})


def edit_role(request,role_id):
    role=Role.objects.get(id=role_id)
    return render(request,"HOD/edit_role.html",{"role":role,"id":role_id})



def edit_role_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        role_id=request.POST.get("role_id")
        first_name=request.POST.get("fname")
        # last_name=request.POST.get("lname")
        # email=request.POST.get("email")
        # username=request.POST.get("username")
        # address=request.POST.get("address")

        try:
            user=Role.objects.get(id=role_id)
            user.role_name=first_name
            # user.last_name=last_name
            # user.email=email
            # user.username=username
            user.save()

            # employee_model=Employee.objects.get(admin=employee_id)
            # employee_model.address=address
            # employee_model.save()
            messages.success(request,"Successfully Edited Employee")
            return HttpResponseRedirect(reverse("manage_role"))
        except:
            messages.error(request,"Failed to Edit Employee")
            return HttpResponseRedirect(reverse("manage_role"))



def DELETE_ROLE(request,role_id):
    
    # agent = SuperAgent.objects.get(admin=id)
    employee = Role.objects.get(id=role_id)
    employee.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('manage_role')




def ADD_EMPLOYEE(request):

    return render(request,'HOD/add_employee.html')



def do_employee_signup(request):
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
        return HttpResponseRedirect(reverse("add_employee"))
    except:
        messages.error(request,"Failed to Create Employee")
        return HttpResponseRedirect(reverse("add_employee"))


def manage_employee(request):
    employee=Employee.objects.all()
    return render(request,"HOD/manage_employee.html",{"employee":employee})

def edit_employee(request,employee_id):
    employee=Employee.objects.get(admin=employee_id)
    return render(request,"HOD/edit_employee.html",{"employee":employee,"id":employee_id})


def edit_employee_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        employee_id=request.POST.get("employee_id")
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=employee_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            employee_model=Employee.objects.get(admin=employee_id)
            employee_model.address=address
            employee_model.save()
            messages.success(request,"Successfully Edited Employee")
            return HttpResponseRedirect(reverse("edit_employee",kwargs={"employee_id":employee_id}))
        except:
            messages.error(request,"Failed to Edit Employee")
            return HttpResponseRedirect(reverse("edit_employee",kwargs={"employee_id":employee_id}))



def DELETE_EMPLOYEE(request,employee_id):
    
    # agent = SuperAgent.objects.get(admin=id)
    employee = CustomUser.objects.get(id=employee_id)
    employee.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('manage_employee')





######################## Instructor ##############################

def ADD_INSTRUCTOR(request):
    return render(request,'HOD/add_instructor.html')



def do_instructor_signup(request):
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    address=request.POST.get("address")

    try:
        user=CustomUser.objects.create_user(first_name=fname,last_name=lname,username=username,password=password,email=email,user_type=3)
        user.instructor.address=address
        user.save()
        messages.success(request,"Successfully Created Instructor")
        return HttpResponseRedirect(reverse("add_instructor"))
    except:
        messages.error(request,"Failed to Create Employee")
        return HttpResponseRedirect(reverse("add_instructor"))





def manage_instructor(request):
    instructor=Instructor.objects.all()
    return render(request,"HOD/manage_instructor.html",{"instructor":instructor})



def edit_instructor(request,instructor_id):
    instructor=Instructor.objects.get(admin=instructor_id)
    return render(request,"HOD/edit_instructor.html",{"instructor":instructor,"id":instructor_id})






def edit_instructor_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        instructor_id=request.POST.get("instructor_id")
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=instructor_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            employee_model=Instructor.objects.get(admin=instructor_id)
            employee_model.address=address
            employee_model.save()
            messages.success(request,"Successfully Edited Instructor")
            return HttpResponseRedirect(reverse("edit_instructor",kwargs={"instructor_id":instructor_id}))
        except:
            messages.error(request,"Failed to Edit Instructor")
            return HttpResponseRedirect(reverse("edit_instructor",kwargs={"instructor_id":instructor_id}))



def manage_members(request):
    member = Member.objects.all()

    return render(request,'HOD/manage_members.html',{'member':member})



def TRAINING_CENTER(request):
    if request.method == 'POST':
        center_name = request.POST.get('training')

        try:
            
            if Center.objects.filter(center_name = center_name).exists():
                messages.warning(request,center_name + " is already Taken ")
                return redirect('training_center')
            center = Center.objects.create(center_name=center_name)
            center.save()
            messages.success(request,"Successfully Created Center")
            return HttpResponseRedirect(reverse("training_center"))
        except:
            messages.error(request,"Failed to Create Role")
            return HttpResponseRedirect(reverse("training_center"))

    return render(request,'HOD/training.html')


def MANAGE_CENTER(request):
    center = Center.objects.all()
    return render(request,'HOD/manage_center.html',{'center':center})



def edit_center(request,center_id):
    center=Center.objects.get(id=center_id)
    return render(request,"HOD/edit_role.html",{"center":center,"id":center_id})



def edit_center_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        center_id=request.POST.get("center_id")
        center_name=request.POST.get("center_name")
        # last_name=request.POST.get("lname")
        # email=request.POST.get("email")
        # username=request.POST.get("username")
        # address=request.POST.get("address")

        try:
            center=Center.objects.get(id=center_id)
            center.center_name=center_name
            # user.last_name=last_name
            # user.email=email
            # user.username=username
            center.save()

            # employee_model=Employee.objects.get(admin=employee_id)
            # employee_model.address=address
            # employee_model.save()
            messages.success(request,"Successfully Updated Center")
            return HttpResponseRedirect(reverse("manage_center"))
        except:
            messages.error(request,"Failed to Updated Center")
            return HttpResponseRedirect(reverse("manage_center"))




def DELETE_CENTER(request,center_id):
    
    # agent = SuperAgent.objects.get(admin=id)
    center = Center.objects.get(id=center_id)
    center.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('manage_center')


def LOCATION(request):

    center = Center.objects.all()
    return render(request,'HOD/location.html',{'center':center})

def doLocation(request):
    if request.method == "POST":
        center_id = request.POST.get('center_id')
        location = request.POST.get('location')
        center=Center.objects.get(id=center_id)

        loc = Location.objects.create(center_name=center,location=location)
        loc.save()

        

    return render(request,'HOD/location.html')
