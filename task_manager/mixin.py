from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class AuthRequiredMixin(LoginRequiredMixin):
    auth_message = _('You are not logged in! Please log in.')
    auth_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_message)
            return redirect(reverse_lazy('auth_url'))
        return super().dispatch(request, *args, **kwargs)


class AuthorDeleteMixin(UserPassesTestMixin):
    protected_message = None
    protected_url = None

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.protected_message)
        return redirect(self.protected_url)


class ProtectDeletionMixin:
    protect_deletion_message = None
    protect_deletion_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(self, request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protect_deletion_message)
            return redirect(self.protect_deletion_url)
