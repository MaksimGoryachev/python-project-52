from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView  # CreateView, DeleteView, UpdateView

# from django.urls import reverse_lazy
from .models import Labels


def index(request):
    return HttpResponse('labels')


class LabelListView(ListView):
    model = Labels
    template_name = 'labels/list_labels.html'
    context_object_name = 'labels'
    paginate_by = 15
    ordering = ['-create_at']
    queryset = Labels.objects.all()
    verbose_name = _('Label')
    verbose_name_plural = _('Labels')
    extra_context = {'title': _('Labels')}
