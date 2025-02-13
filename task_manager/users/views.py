# from django.contrib.auth.views import UserCreationView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..mixin import AuthRequiredMixin, ProtectDeletionMixin
from .forms import MyUserCreationForm
from .models import User


class UserListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    paginate_by = 15
    ordering = ['-date_joined']
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


class UserUpdateView(AuthRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = MyUserCreationForm
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')
    protected_message = _("You don't have the rights to change another user.")
    template_name = 'forms.html'
    extra_context = {
        'title': _('Update user'),
        'button_text': _('Update'),
    }


class UserDeleteView(AuthRequiredMixin, DeleteView,
                     ProtectDeletionMixin, SuccessMessageMixin):
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully deleted')
    protected_message = _("You don't have the rights to change another user.")
    protect_deletion_message = _('It is not possible to delete '
                                 'a user because it is being used')
    protect_deletion_url = reverse_lazy('users')
    template_name = 'delete.html'
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.object.username
        return context
