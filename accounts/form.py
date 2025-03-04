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

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password Confirmation'

    first_name = forms.CharField(
        max_length=150,
        required=True,
        label="First name",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First name'}
        ),
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label="Last name",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last name'}
        ),
    )
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-select'}
        ),
        empty_label="Select Position"
    )

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
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}
            ),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'position']
