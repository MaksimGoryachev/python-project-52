from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        labels = {
            'username': _('Username'),
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'password1': _('Password'),
            'password2': _('Confirm password'),
        }
        help_texts = {
            'password1': _('Your password must contain at least 3 characters.'),
            'password2': _('Please enter the password again to confirm.'),
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': _('Username')}),
            'first_name': forms.TextInput(attrs={'placeholder': _('First name')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Last name')}),
            'password1': forms.PasswordInput(attrs={'placeholder': _('Password')}),
            'password2': forms.PasswordInput(attrs={'placeholder': _('Confirm password')}),
        }

class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': _('Username'),
            'password': _('Password'),
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': _('Username'), 'autofocus': 'true'}),
            'password': forms.PasswordInput(attrs={'placeholder': _('Password')}),
        }
        error_messages = {
            'invalid_login': _(
                "Please enter a correct username and password. "
                "Note that both fields are case-sensitive."
            ),
        }

