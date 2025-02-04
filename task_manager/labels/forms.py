from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Labels


class LabelForm(forms.ModelForm):

    name = forms.CharField(max_length=150, required=True, label=_('Name'))

    class Meta:
        model = Labels
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Name'),
                'autofocus': 'true'
            }),
        }
        error_messages = {
            'name': {
                'unique': _('A label with this name already exists.'),
            },
        }
