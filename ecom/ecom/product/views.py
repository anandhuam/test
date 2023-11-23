from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    product=Product.objects.all()
    return render(request,'index.html',{'product':product})

def about(request):
    product=Product.objects.all()
    return render(request,'',{'product':product})

def contact(request):
    product=Product.objects.all()
    return render(request,'',{'product':product})



