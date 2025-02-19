from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

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
        self.assertEqual(str(messages[0]), 'Вы залогинены')

    def test_successful_logout(self):
        response = self.client.get(self.logout_url, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Вы разлогинены')

    def test_user_full_name(self):
        self.assertEqual(str(self.user), 'Test User')

    def test_get_context_data(self):
        response = self.client.get(self.delete_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['name'], self.user.username)
