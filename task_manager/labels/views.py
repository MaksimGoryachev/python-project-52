from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from ..base_class import BaseCreateView, BaseDeleteView, BaseUpdateView
from ..mixin import AuthRequiredMixin, ProtectDeletionMixin
from .forms import LabelForm
from .models import Labels


class LabelListView(AuthRequiredMixin, ListView):
    model = Labels
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    paginate_by = 15
    ordering = ['-create_at']
    extra_context = {'title': _('Labels')}


class LabelCreateView(BaseCreateView):
    model = Labels
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')
    title = _('Create label')


class LabelUpdateView(BaseUpdateView):
    model = Labels
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully updated')
    title = _('Update label')


class LabelDeleteView(ProtectDeletionMixin, BaseDeleteView):
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')
    protect_deletion_url = reverse_lazy('labels')
    protect_deletion_message = _('It is not possible to delete '
                                 'a label because it is being used')
    related_name = 'labels'
    title = _('Delete label')
