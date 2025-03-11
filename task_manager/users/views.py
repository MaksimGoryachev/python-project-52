from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView

from ..base_class import BaseDeleteView, BaseUpdateView
from ..mixin import (
    ProtectChangeUserMixin,
    ProtectDeletionMixin,
)
from .forms import MyUserChangeForm, MyUserCreationForm
from .models import User


class UserListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    paginate_by = 15
    ordering = ['-date_joined']
    extra_context = {'title': _('Users')}


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'forms.html'
    model = User
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')
    extra_context = {
        'title': _('Create user'),
        'button_text': _('Register'),
    }


class UserUpdateView(ProtectChangeUserMixin, BaseUpdateView):
    model = User
    form_class = MyUserChangeForm
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')
    protected_url = reverse_lazy('users')
    protected_message = _("You don't have the rights to change another user.")
    template_name = 'forms.html'
    title = _('Update user')


class UserDeleteView(ProtectChangeUserMixin,
                     ProtectDeletionMixin, BaseDeleteView):
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully deleted')
    protected_url = reverse_lazy('users')
    protected_message = _("You don't have the rights to change another user.")
    protect_deletion_url = reverse_lazy('users')
    protect_deletion_message = _('It is not possible to delete '
                                 'a user because it is being used')
    related_name = 'author'
    name_attribute = 'username'
    title = _('Delete user')
