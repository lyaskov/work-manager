from django.urls import path

from management.views import index, dashboard

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
]
app_name = "management"
