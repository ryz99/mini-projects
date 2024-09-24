from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.
# Looks for _list
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

# Looks for _detail
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

#
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')
