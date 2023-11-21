from django.contrib import admin
from .models import *



# Register your models here.
class Department_display(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Department,Department_display)

class Batch_display(admin.ModelAdmin):
    list_display=['batch']
    
admin.site.register(Batch,Batch_display)


class Student_display(admin.ModelAdmin):
    list_display=['name','batch']
    
admin.site.register(Students,Student_display)
    



