from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView

from .mixin import AuthRequiredMixin


class BaseCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'forms.html'
    extra_context = {'button_text': _('Create')}
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.title:
            context['title'] = self.title
        return context


class BaseUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'forms.html'
    extra_context = {'button_text': _('Update')}
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.title:
            context['title'] = self.title
        return context


class BaseDeleteView(AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'delete.html'
    extra_context = {'button_text': _('Yes, delete')}
    name_attribute = 'name'
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = getattr(self.object, self.name_attribute)
        if self.title:
            context['title'] = self.title
        return context
