from django.urls import path

from management.views import TaskCreateView, TaskListView, \
    TaskUpdateView, TaskDetailView, TaskDeleteView, DashboardView

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path("tasks/create/", TaskCreateView.as_view(), name="tasks-create"),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(),
         name='task-delete'),
]

app_name = "management"
