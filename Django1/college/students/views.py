from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> this is home page</h1>')
def About_us(request):
    return HttpResponse('<h1> this is About page</h1>')
def Contact(request):
    return HttpResponse('<h1> this is contact page</h1>')

