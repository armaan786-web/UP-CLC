from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        ('1', 'members'),
        ('2', 'Employer'),
        # ('3 ', 'Customer'),

    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to = 'media/profile_pic')
    

   
class abc(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(max_length=20)
    dob = models.DateField(("Date"), default=datetime.date.today)
    adhar_no = models.CharField(max_length=50)
    pan_no = models.CharField(max_length=50)
    caste=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return str(self.admin)

    # class Meta:
    #     db_table = "abc"
    



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            abc.objects.create(admin=instance,address="")
        # if instance.user_type==2:
        #     members.objects.create(admin=instance,address="")
        
        

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.ABC.save()
    # if instance.user_type==2:
    #     instance.members.save()
    
