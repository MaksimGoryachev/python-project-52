from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView

from ..base_class import BaseDeleteView
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


class LabelCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'forms.html'
    model = Labels
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create'),
    }


class LabelUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'forms.html'
    model = Labels
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully updated')
    extra_context = {
        'title': _('Update label'),
        'button_text': _('Update'),
    }


class LabelDeleteView(ProtectDeletionMixin, BaseDeleteView):
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')
    protect_deletion_url = reverse_lazy('labels')
    protect_deletion_message = _('It is not possible to delete '
                                 'a label because it is being used')
    related_name = 'labels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Delete label'),
        })
        return context
