from django.contrib import admin
from .models import *

# Register your models here.
class product_display(admin.ModelAdmin):
    list_display=['name','price','brand','image']
admin.site.register(Product,product_display)
