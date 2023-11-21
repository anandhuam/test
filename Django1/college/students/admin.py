from django.contrib import admin
from.models import *


# Register your models here.
class Department_display(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Department,Department_display)
