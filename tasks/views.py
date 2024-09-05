from django.shortcuts import render
from .models import Task
from django.views.generic import ListView
# Create your views here.

#def task_list(request):
#    tasks = Task.objects.all()
#    return render(request,'tasks/task_list.html',{'tasks': tasks})

class TaskListView(ListView):
    model = Task
    tamplete_name = 'tasks/task_list.html'
    context_object_name = 'tasks'