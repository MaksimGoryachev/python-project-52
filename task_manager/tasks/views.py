from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView

from .forms import TaskForm
from .models import Task


class TaskListView(SuccessMessageMixin, ListView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'tasks'
    paginate_by = 15
    ordering = ['-created_at']
    extra_context = {'title': _('Tasks')}


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task created successfully.')
    form_class = TaskForm
    template_name = 'forms.html'
    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
