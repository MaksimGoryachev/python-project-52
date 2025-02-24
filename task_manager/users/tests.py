from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .forms import MyUserChangeForm, MyUserCreationForm
from .models import User


class UserViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='123',
                                             first_name='Test',
                                             last_name='User')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.base_url = reverse('base')
        self.update_url = reverse('user_update', kwargs={'pk': self.user.pk})
        self.delete_url = reverse('user_delete', kwargs={'pk': self.user.pk})

        self.client.login(username='testuser', password='123')

    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forms.html')

    def test_successful_login(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': '123'
        })
        self.assertRedirects(response, self.base_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), _('You are logged in'))

    def test_successful_logout(self):
        response = self.client.get(self.logout_url, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), _('You are logged out'))

    def test_user_full_name(self):
        self.assertEqual(str(self.user), 'Test User')

    def test_get_context_data(self):
        response = self.client.get(self.delete_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['name'], self.user.username)

    def test_user_can_change_own_profile(self):
        user_data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'username': 'testuser',
            'password1': '123',
            'password2': '123'
        }
        response = self.client.post(
            self.update_url,
            data=user_data,
            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('users'))

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'Name')

    def test_user_cannot_change_others(self):
        other_user = User.objects.create_user(username='otheruser',
                                              password='otherpassword')
        self.client.login(username='testuser', password='123')
        response = self.client.post(reverse('user_update',
                                            args=[other_user.id]))
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]),
                         _("You don't have the rights to change another user."))
        self.assertRedirects(response, reverse('users'))

    def test_clean_username_existing_user(self):
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
        }
        form = MyUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        # self.assertEqual(form.errors['username'],
        #                  [_('A user with that username already exists.')])
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_clean_username_can_create_user(self):
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123',
        }
        form = MyUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()
        self.user.refresh_from_db()
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_clean_username_change_form_existing_user(self):
        form_data = {
            'first_name': 'UpdateTest',
            'last_name': 'UpdateUser',
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
        }
        form = MyUserChangeForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())
        form.save()
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdateTest')
        self.assertEqual(self.user.last_name, 'UpdateUser')
        self.assertEqual(self.user.username, 'testuser')

    def test_user_cannot_change_to_existing_username(self):
        User.objects.create_user(username='testuser2', password='123')
        self.client.login(username='testuser', password='123')

        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser2',
            'password1': 'password123',
            'password2': 'password123',
        }

        form = MyUserChangeForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertEqual(form.errors['username'],
                         [_('A user with that username already exists.')])
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_profile_update_with_invalid_data(self):
        user_data = {
            'first_name': '',
            'last_name': '',
            'username': 'newuser',
            'password1': '123',
            'password2': '123'
        }
        form = MyUserChangeForm(data=user_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertEqual(form.errors['first_name'],
                         [_('Please fill in this field.')])
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertFalse(User.objects.filter(username='newuser').exists())
        self.assertTrue(self.user.first_name, 'Test')
        self.assertTrue(self.user.last_name, 'User')
