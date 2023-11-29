from django.shortcuts import render
from .forms import Todo_forms
from . models import *

# Create your views here.
def index(request):
    context={}

    todo_form=Todo_forms()
    todo=Todo.objects.all()


    if request.method=='POST':
        if 'save' in request.POST:
            todo_form=Todo_forms(request.POST)
            todo_form.save()
       

    context['todo_form']=todo_form
    context['todo']=todo

    return render(request,'index.html',context)

