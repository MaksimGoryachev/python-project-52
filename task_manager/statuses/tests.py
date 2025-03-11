from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ..users.models import User
from .models import Status


class StatusViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='123')
        self.client.login(username='testuser', password='123')
        self.status = Status.objects.create(name='Test Status')
        self.login_url = reverse('login')

    def test_model_name(self):
        self.assertEqual(str(self.status), 'Test Status')

    def test_get_context_data(self):
        response = self.client.get(reverse('status_delete',
                                           args=[self.status.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['name'], self.status.name)

        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], _('Delete status'))

        self.assertIn('button_text', response.context)
        self.assertEqual(response.context['button_text'], _('Yes, delete'))
