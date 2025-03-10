from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView

from ..base_class import BaseDeleteView
from ..mixin import AuthRequiredMixin, ProtectDeletionMixin
from .forms import StatusForm
from .models import Status


class StatusListView(AuthRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    paginate_by = 15
    ordering = ['-create_at']
    extra_context = {'title': _('Statuses')}


class StatusCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status created successfully.')
    form_class = StatusForm
    template_name = 'forms.html'
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create'),
    }


class StatusUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated successfully.')
    template_name = 'forms.html'
    extra_context = {
        'title': _('Update status'),
        'button_text': _('Update'),
    }


class StatusDeleteView(ProtectDeletionMixin, BaseDeleteView):
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status deleted successfully.')
    protect_deletion_url = reverse_lazy('statuses')
    protect_deletion_message = _('It is not possible to delete '
                                 'a status because it is being used')
    related_name = 'status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Delete status'),
        })
        return context
