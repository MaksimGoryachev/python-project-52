# from django.contrib.auth.views import UserCreationView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView  # UpdateView, DeleteView

from .forms import MyUserCreationForm
from .models import User


class UserListView(SuccessMessageMixin, ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    paginate_by = 15
    ordering = ['-create_at']
    extra_context = {'title': _('Users')}


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
