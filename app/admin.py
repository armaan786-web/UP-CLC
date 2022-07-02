from django.contrib import admin
from .models import*

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Instructor)
admin.site.register(Member)
admin.site.register(Role)
admin.site.register(Job)
admin.site.register(Course)
admin.site.register(Center)
admin.site.register(Location)
