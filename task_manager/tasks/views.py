from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django_filters.views import FilterView

from .forms import TaskForm
from .filter import TaskFilter
from .models import Task


class TaskListView(FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    paginate_by = 15
    ordering = ['-created_at']
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show'),
    }


class TaskCreateView(SuccessMessageMixin, CreateView):
    template_name = 'forms.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task created successfully.')
    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task updated successfully.')
    template_name = 'forms.html'
    extra_context = {
        'title': _('Update task'),
        'button_text': _('Update'),
    }


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted successfully.')
    template_name = 'delete.html'
    protected_massage = _('An issue can only be deleted by its author.')
    protected_url = reverse_lazy('tasks')
    extra_context = {
        'title': _('Delete task'),
        'button_text': _('Yes, delete'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.object.name
        return context
