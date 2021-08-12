from django import TaskForm
from django.shortcuts import redirect, render
from.forms import  TaskForm

def listTask(request):
     queryset=TaskForm.objects.order_by('complete','due')
     form=TaskForm()
     if request.methods=='POST':
         form=TaskForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/')
     context={
         'tasks':queryset,
         'form':form,
        }
     return render(request,'list_task.html',context)





# Create your views here.
