from django.shortcuts import render
# from.models import *


# # Create your views here.
def index(request):
    students=Student.objects.all()
    return render(request,'index.html',{'students':Student})
def about(request):
    students=Student.objects.all()
    return render(request,'',{'students':Student})
def contact(request):
    students=Student.objects.all()
    return render(request,'',{'students':Student})