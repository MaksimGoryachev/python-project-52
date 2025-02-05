from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView  # DeleteView, UpdateView

from .forms import LabelForm
from .models import Labels


class LabelListView(ListView):
    model = Labels
    template_name = 'labels/list_labels.html'
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
