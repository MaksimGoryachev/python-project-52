from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django_filters.views import FilterView

from ..base_class import BaseCreateView, BaseDeleteView, BaseUpdateView
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


class TaskCreateView(BaseCreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task was created successfully.')
    title = _('Create task')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(BaseUpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task updated successfully.')
    title = _('Update task')


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
    title = _('Delete task')
