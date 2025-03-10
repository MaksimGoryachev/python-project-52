from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django_filters.views import FilterView

from ..base_class import BaseDeleteView
from ..mixin import AuthorDeleteMixin, AuthRequiredMixin
from .filter import TaskFilter
from .forms import TaskForm
from .models import Task


class TaskListView(AuthRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show'),
    }


class TaskCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'forms.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task was created successfully.')
    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task updated successfully.')
    template_name = 'forms.html'
    extra_context = {
        'title': _('Update task'),
        'button_text': _('Update'),
    }


class TaskDetailView(AuthRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    extra_context = {
        'title': _('Task details'),
    }
    context_object_name = 'task'


class TaskDeleteView(AuthorDeleteMixin, BaseDeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted successfully.')
    protected_author_url = reverse_lazy('tasks')
    protected_author_message = _('A task can only be deleted by its author.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Delete task'),
        })
        return context
