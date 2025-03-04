from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from accounts.form import WorkerRegistrationForm, UserEditForm
from management.models import Worker


class WorkerRegisterView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('management:dashboard')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = WorkerRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('management:dashboard')
        return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


class UserEditView(LoginRequiredMixin, UpdateView):
    model = Worker
    form_class = UserEditForm
    template_name = 'accounts/user_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
