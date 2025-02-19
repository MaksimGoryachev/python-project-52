from django.test import TestCase
from django.urls import reverse

from .models import User


class UserViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='123',
                                             first_name='Test',
                                             last_name='User')
        self.client.login(username='testuser', password='123')
        self.delete_url = reverse('user_delete', kwargs={'pk': self.user.pk})

    def test_user_full_name(self):
        self.assertEqual(str(self.user), 'Test User')

    def test_get_context_data(self):
        response = self.client.get(self.delete_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['name'], self.user.username)
