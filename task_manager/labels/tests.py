from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ..statuses.models import Status
from ..tasks.models import Task
from ..users.models import User
from .models import Labels


class LabelNoAuthTest(TestCase):
    def test_labels_no_auth(self):
        response = self.client.get('/labels/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))


class LabelViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='test123')
        self.client.login(username='testuser', password='test123')

        self.label = Labels.objects.create(name='Test Label')

    def test_label_list_view(self):
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/labels.html')
        self.assertContains(response, 'Test Label')
        self.assertQuerySetEqual(response.context['labels'],
                                 Labels.objects.all())

    def test_label_create_view(self):
        response = self.client.post(reverse('label_create'),
                                    {'name': 'New Label'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Labels.objects.count(), 2)
        self.assertEqual(Labels.objects.get(name='New Label').name,
                         'New Label')
        self.assertTrue(Labels.objects.filter(name='New Label').exists())
        self.assertEqual(str(self.label), 'Test Label')

    def test_label_update_view(self):
        response = self.client.post(reverse('label_update',
                                            args=[self.label.id]),
                                    {'name': 'Updated Label'})
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Updated Label')
        self.assertTrue(Labels.objects.filter(name='Updated Label').exists())
        self.assertFalse(Labels.objects.filter(name='Test Label').exists())

    def test_label_delete_view(self):
        response = self.client.post(reverse('label_delete',
                                            args=[self.label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Labels.objects.filter(id=self.label.id).exists())
        self.assertFalse(Labels.objects.filter(name='Test Label').exists())
        self.assertEqual(Labels.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), _('Label successfully deleted'))

    def test_label_delete_protect_deletion(self):
        self.status = Status.objects.create(name='Test Task')
        self.task = Task.objects.create(name='Test Task', status=self.status,
                                        author=self.user)
        self.task.labels.add(self.label)
        self.assertTrue(Task.objects.filter(labels=self.label).exists())

        response = self.client.post(reverse('label_delete',
                                            args=[self.label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Labels.objects.filter(id=self.label.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), _('It is not possible to delete a '
                                             'label because it is being used'))

    def test_label_delete_view_context(self):
        response = self.client.get(reverse('label_delete',
                                           args=[self.label.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')
        self.assertEqual(response.context['name'], self.label.name)

    def test_label_update_view_context(self):
        response = self.client.get(reverse('label_update',
                                           args=[self.label.id]))
        self.assertEqual(response.status_code, 200)

        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], _('Update label'))

        self.assertIn('button_text', response.context)
        self.assertEqual(response.context['button_text'], _('Update'))