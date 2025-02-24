from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )
        labels = {
            'username': _('Username'),
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'password1': _('Password'),
            'password2': _('Confirm password'),
        }
        help_texts = {
            'password1': _(
                'Your password must contain at least 3 characters.'
            ),
            'password2': _(
                'Please enter the password again to confirm.'
            ),
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': _('Username'),
                'autofocus': 'true',
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': _('First name'),
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': _('Last name'),
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': _('Password')
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': _('Confirm password')
            }),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_('A user with that username'
                                          ' already exists.'))
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError(_('Please fill in this field.'))
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError(_('Please fill in this field.'))
        return last_name


class MyUserChangeForm(MyUserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(
                username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(_('A user with that username'
                                          ' already exists.'))
        return username


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': _('Username'),
            'password': _('Password'),
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': _('Username'),
                'autofocus': 'true'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': _('Password')
            }),
        }
        error_messages = {
            'invalid_login': _(
                "Please enter a correct username and password. "
                "Note that both fields are case-sensitive."
            ),
        }
