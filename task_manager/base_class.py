from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView

from .mixin import AuthRequiredMixin


class BaseView(AuthRequiredMixin, SuccessMessageMixin):
    title = None
    button_text = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.title:
            context['title'] = self.title
        if self.button_text:
            context['button_text'] = self.button_text
        return context


class BaseCreateView(BaseView, CreateView):
    template_name = 'forms.html'
    button_text = _('Create')


class BaseUpdateView(BaseView, UpdateView):
    template_name = 'forms.html'
    button_text = _('Update')


class BaseDeleteView(BaseView, DeleteView):
    template_name = 'delete.html'
    button_text = _('Yes, delete')
    name_attribute = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = getattr(self.object, self.name_attribute)
        return context
