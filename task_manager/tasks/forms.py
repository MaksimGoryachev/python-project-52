from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'labels')
        widgets = {
            'name': forms.TextInput(attrs={
                'autofocus': 'true',
                'placeholder': _('Name')
            }),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': _('Description')
            }),
            'status': forms.Select(),
            'executor': forms.Select(),
            'labels': forms.SelectMultiple(),
        }
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }
        error_messages = {
            'name': {
                'unique': _('A task with this name already exists.'),
            },
            'status': {
                'required': _('Please select an item from this list.'),
            },
        }
