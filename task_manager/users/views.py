# from django.shortcuts import render
# from django.contrib.auth.views import UserCreationView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView  # ListView, UpdateView, DeleteView

from .forms import MyUserCreationForm
from .models import User


def index(request):
    return HttpResponse('users')


class UserCreateView(CreateView, SuccessMessageMixin):
    template_name = 'forms.html'
    model = User
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')
    extra_context = {
        'title': _('Create user'),
        'button_text': _('Register'),
    }
