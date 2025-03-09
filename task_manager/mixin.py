from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class AuthRequiredMixin(LoginRequiredMixin):
    auth_message = _('You are not logged in! Please log in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_message)
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class AuthorDeleteMixin(UserPassesTestMixin):
    protected_author_message = None
    protected_author_url = None

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.protected_author_message)
        return redirect(self.protected_author_url)


class ProtectDeletionMixin:
    protect_deletion_message = None
    protect_deletion_url = None
    related_name = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if getattr(self.object, self.related_name).exists():
            messages.error(request, self.protect_deletion_message)
            return redirect(self.protect_deletion_url)

        self.object.delete()
        messages.success(request, self.success_message)
        return redirect(self.success_url)


class ProtectChangeUserMixin(UserPassesTestMixin):
    protected_message = None
    protected_url = None

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.protected_message)
        return redirect(self.protected_url)
