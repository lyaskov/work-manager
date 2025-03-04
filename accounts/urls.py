from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts.views import WorkerRegisterView, profile_view, UserEditView

urlpatterns = [
    path('login/',
         LoginView.as_view(
             redirect_authenticated_user=True, next_page='/dashboard/'
         ),
         name='login'),
    path('register/', WorkerRegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', UserEditView.as_view(), name='profile-edit'),
    path('', include('django.contrib.auth.urls')),
]