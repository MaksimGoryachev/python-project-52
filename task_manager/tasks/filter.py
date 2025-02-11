from django import forms

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter

from ..labels.models import Labels
from ..statuses.models import Status
from ..users.models import User
from .models import Task


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status'),
        empty_label=_('All')
    )
    executor = ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('Executor'),
        empty_label=_('All')
    )
    label = ModelChoiceFilter(
        queryset=Labels.objects.all(),
        label=_('Label'),
        empty_label=_('All')
    )
    your_tasks = BooleanFilter(
        label=_('Only your own tasks'),
        required=False,
        method='filter_your_tasks',
        widget=forms.CheckboxInput
    )

    def filter_your_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'your_tasks']
