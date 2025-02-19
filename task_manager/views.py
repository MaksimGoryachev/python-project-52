from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import View

from task_manager.users.forms import MyAuthenticationForm


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', context={})


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'forms.html'
    form_class = MyAuthenticationForm
    next_page = reverse_lazy('base')
    success_message = _('You are logged in')
    extra_context = {
        'title': _('Login'),
        'button_text': _('Enter'),
    }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('base')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
