from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.


class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Employee"),(3,"Instructor"),(4,"members"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
    adhaar = models.CharField(max_length=50,null=True,blank=True)
    profile_pic = models.ImageField(upload_to = 'media/profile_pic')
    

class AdminHOD(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()   



class Employee(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.admin.username

class Job(models.Model):
    # employee = models.ForeignKey(to=Employee,on_delete=models.CASCADE) 
    job_img = models.ImageField(upload_to='Jobs_Img')
    job_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    min_sallery = models.IntegerField()
    max_sallery = models.IntegerField()
    Vacancy = models.IntegerField()
    date =models.DateField(auto_now_add=True)
    # date =models.DateField(auto_now_add=False)
    job_des = RichTextField()
    job_skill = RichTextField()
    job_experience = RichTextField()
    salary = models.IntegerField()

    def __str__(self):
        return self.job_name
    




class Role(models.Model):
    role_name = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=False, auto_now=True,null=True,blank=True)
    objects=models.Manager()

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = "role"
        

class Member(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    dob = models.DateField(auto_now_add=False,null=True,blank=True)
    adhaar = models.CharField(max_length=50,null=True,blank=True)
    pan_no = models.CharField(max_length=50,null=True,blank=True)
    caste = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    pin = models.CharField(max_length=50,null=True,blank=True)
    address=models.TextField(null="True",blank=True)
    paid=models.BooleanField(default=False)
    payment_id=models.CharField(max_length=70)
    amount=models.CharField(max_length=70)
    role_id=models.ForeignKey(Role,on_delete=models.DO_NOTHING,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.admin.username
    


class Instructor(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.admin.username
  

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Employee.objects.create(admin=instance,address="")
        if instance.user_type==3:
            Instructor.objects.create(admin=instance,address="")
        if instance.user_type==4:
            Member.objects.create(admin=instance,address="")
        # if instance.user_type==3:
        #     Students.objects.create(admin=instance,course_id=Courses.objects.get(id=1),session_year_id=SessionYearModel.object.get(id=1),address="",profile_pic="",gender="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.employee.save()
    if instance.user_type==3:
        instance.instructor.save()
    if instance.user_type==4:
        instance.member.save()
