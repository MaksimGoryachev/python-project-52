from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView

from .mixin import AuthRequiredMixin


class BaseDeleteView(AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'delete.html'
    extra_context = {'button_text': _('Yes, delete')}
    name_attribute = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = getattr(self.object, self.name_attribute)
        return context
