from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from management.forms import TaskCreateForm, TaskUpdateForm
from management.models import Task


# Create your views here.
def index(request):
    return render(request, "management/index.html")


@login_required
def dashboard(request):
    return render(request, "management/dashboard.html")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('management:dashboard')


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['deadline']
    paginate_by = 10


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('management:task-list')


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('management:task-list')


