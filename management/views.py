from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View

from management.forms import TaskCreateForm, TaskUpdateForm
from management.models import Task


# Create your views here.
def index(request):
    return render(request, "management/index.html")


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user

        completed_tasks = Task.objects.filter(assignees=user,
                                              is_completed=True)
        active_tasks = Task.objects.filter(assignees=user,
                                           is_completed=False)

        context = {
            "completed_tasks": completed_tasks,
            "active_tasks": active_tasks,
        }
        return render(request, "management/dashboard.html", context)


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


