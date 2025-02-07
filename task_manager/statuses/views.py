from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView

from .forms import StatusForm
from .models import Status


class StatusListView(SuccessMessageMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    paginate_by = 15
    ordering = ['-create_at']
    extra_context = {'title': _('Statuses')}


class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status created successfully.')
    form_class = StatusForm
    template_name = 'forms.html'
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create'),
    }
