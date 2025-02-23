from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from accounts.form import WorkerRegistrationForm


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
            return redirect('dashboard')
        return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})