from django.shortcuts import render
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from tasks.models import Task
from tasks.forms import TaskForm
from django.urls import reverse_lazy
# Create your views here.

#def task_list(request):
#    tasks = Task.objects.all()
#    return render(request,'tasks/task_list.html',{'tasks': tasks})

class TaskListView(ListView):
    model = Task
    tamplete_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        return super().form_valid(form)
    
