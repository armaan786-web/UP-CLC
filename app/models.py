from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.



class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Employee"),(3,"Instructor"),(4,"members"),(5,"Training"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
    adhaar = models.CharField(max_length=50,null=True,blank=True)
    profile_pic = models.ImageField(upload_to = 'media/profile_pic')
    pan_no = models.CharField(max_length=100,null=True,blank=True)


class gallary(models.Model):
    galary_pic = models.ImageField(upload_to = 'Galary', null= True, blank=True)

class AdminHOD(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()   


class City(models.Model):
    city = models.CharField(max_length=100)    
    active = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=False, auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.city
    

class Role(models.Model):

    role_name = models.CharField(max_length=100)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    min_sal = models.PositiveIntegerField()
    max_sal = models.PositiveIntegerField()
    gov_approved = models.PositiveIntegerField()
    margin = models.PositiveIntegerField()
    is_employer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    # active = models.BooleanField(default=False)
    # inactive = models.BooleanField(default=False)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=False, auto_now=True,null=True,blank=True)
    objects=models.Manager()


    def __str__(self):
        return self.role_name

    class Meta:
        db_table = "role"
        
    

class Employer(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    

    
    mob_no = models.IntegerField(null=True,blank=True)
    emp_city = models.CharField(max_length=100)
    emp_state = models.CharField(max_length=100)
    emp_pin_code = models.IntegerField(null=True,blank=True)
    address=models.TextField()
    pan_Card = models.ImageField(upload_to = 'pancard/', null= True, blank=True)
    section = models.CharField(max_length=50,null=True,blank=True)
    # services = models.ForeignKey(Role,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=70,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    objects=models.Manager()

    def __str__(self):
        return self.admin.username


class Booking(models.Model):
    # id=models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    services = models.ForeignKey(Role,on_delete=models.CASCADE)
    no_of_worker = models.CharField(max_length=100)
    gender_preference = models.CharField(max_length=100)
    
    work_start_Date = models.DateField(auto_now_add=False,null=True,blank=True)
    landmark = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    pin_code = models.IntegerField(null=True,blank=True)
    specific_requirements = models.CharField(max_length=100,null=True,blank=True)
    sallery_offerd = models.IntegerField(null=True,blank=True)
    goverment = models.CharField(max_length=100)
    department = models.CharField(max_length=50,null=True,blank=True)
    total_monthly = models.IntegerField(blank=True,null=True)
    paid=models.BooleanField(default=False)
    payment_id=models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.employer_id.admin.username
    



class outer(models.Model):
    
    name= models.CharField(max_length=100)
    mob = models.CharField(max_length=50)
    services = models.CharField(max_length=50)
    no_of_worker = models.CharField(max_length=100)
    gender_preference = models.CharField(max_length=100)
    
    work_start_Date = models.CharField(max_length=100,null=True,blank=True)
    landmark = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    pin_code = models.IntegerField(null=True,blank=True)
    specific_requirements = models.CharField(max_length=100,null=True,blank=True)
    sallery_offerd = models.IntegerField(null=True,blank=True)
    goverment = models.CharField(max_length=100)
    department = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
    


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
    


class Course(models.Model):
    course_img = models.ImageField(upload_to = 'course_pic')
    course_name = models.CharField(max_length=100)
    course_amt = models.IntegerField()
    company_name = models.CharField(max_length=100)
    course_location = models.CharField(max_length=100)
    course_des = RichTextField()
    course_skill = RichTextField()
    course_experience = RichTextField()

    def __str__(self):
        return self.course_name
    

class Center(models.Model):
    center_name = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=False, auto_now=True,null=True,blank=True)
    objects=models.Manager()

    def __str__(self):
        return self.center_name

    class Meta:
        db_table = "center"
        
class Location(models.Model):
    center_name = models.ForeignKey(Center,on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.center_name)
    
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
    payment_id=models.CharField(max_length=70)
    paid=models.BooleanField(default=False)
    amount=models.CharField(max_length=70)
    role_id=models.ForeignKey(Role,on_delete=models.DO_NOTHING,null=True,blank=True)
    
    
    marital_status=models.CharField(max_length=50,null=True,blank=True)
    job_seeker=models.CharField(max_length=50,null=True,blank=True)
    adhar_front = models.ImageField(upload_to = 'worker/', null= True, blank=True)
    adhar_back = models.ImageField(upload_to = 'worker/', null= True, blank=True)
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

class Training(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    dob = models.DateField(auto_now_add=False,null=True,blank=True)
    # adhaar = models.CharField(max_length=50,null=True,blank=True)
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
    


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Employer.objects.create(admin=instance,address="")
        if instance.user_type==3:
            Instructor.objects.create(admin=instance,address="")
        if instance.user_type==4:
            Member.objects.create(admin=instance,address="")
        if instance.user_type==5:
            Training.objects.create(admin=instance,address="")
        # if instance.user_type==3:
        #     Students.objects.create(admin=instance,course_id=Courses.objects.get(id=1),session_year_id=SessionYearModel.object.get(id=1),address="",profile_pic="",gender="")



@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.employer.save()
    if instance.user_type==3:
        instance.instructor.save()
    if instance.user_type==4:
        instance.member.save()
    if instance.user_type==5:
        instance.training.save()
