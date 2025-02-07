from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView

# ,UpdateView
from .forms import LabelForm
from .models import Labels


class LabelListView(SuccessMessageMixin, ListView):
    model = Labels
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    paginate_by = 15
    ordering = ['-create_at']
    extra_context = {'title': _('Labels')}


class LabelCreateView(SuccessMessageMixin, CreateView):
    template_name = 'forms.html'
    model = Labels
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create'),
    }


class LabelDeleteView(SuccessMessageMixin, DeleteView):

    template_name = 'labels/delete.html'
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')
    protected_message = _('It is not possible to delete a label '
                          'because it is in use')
    protected_url = reverse_lazy('labels')
    extra_context = {
        'title': _('Delete label'),
        'name': _(model.name),
    }
