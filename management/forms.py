from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from management.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'deadline',
            'priority',
            'task_type',
            'assignees'
        ]
        widgets = {
            'deadline': forms.DateInput(
                attrs={'type': 'date', 'min': date.today().isoformat()}
            ),
            'assignees': forms.CheckboxSelectMultiple
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')

        if deadline and deadline < date.today():
            raise ValidationError("The deadline cannot be in the past.")

        return deadline


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'deadline',
            'priority',
            'task_type',
            'assignees',
            'is_completed'
        ]
        widgets = {
            'deadline': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'assignees': forms.CheckboxSelectMultiple
        }
