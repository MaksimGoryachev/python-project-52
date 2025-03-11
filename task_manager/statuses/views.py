from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from ..base_class import BaseCreateView, BaseDeleteView, BaseUpdateView
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


class StatusCreateView(BaseCreateView):
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status created successfully.')
    form_class = StatusForm
    title = _('Create status')


class StatusUpdateView(BaseUpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated successfully.')
    title = _('Update status')


class StatusDeleteView(ProtectDeletionMixin, BaseDeleteView):
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status deleted successfully.')
    protect_deletion_url = reverse_lazy('statuses')
    protect_deletion_message = _('It is not possible to delete '
                                 'a status because it is being used')
    related_name = 'status'
    title = _('Delete status')
