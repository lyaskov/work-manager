from django import forms
from django.contrib.auth.forms import UserCreationForm

from management.models import Worker, Position


class WorkerRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        self.fields['password1'].widget.attrs.pop('aria-describedby', None)
        self.fields['password2'].widget.attrs.pop('aria-describedby', None)

    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    position = forms.ModelChoiceField(queryset=Position.objects.all(), required=True)

    class Meta:
        model = Worker
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'position',
            'password1',
            'password2'
        ]
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }


