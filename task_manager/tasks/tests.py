from django.test import TestCase
from django.urls import reverse

from ..labels.models import Labels
from ..statuses.models import Status
from ..users.models import User
from .filter import TaskFilter
from .forms import TaskForm
from .models import Task


class TaskViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1',
                                              password='password1')
        self.user2 = User.objects.create_user(username='testuser2',
                                              password='password2')
        self.client.login(username='testuser1', password='password1')
        self.status1 = Status.objects.create(name='In development')
        self.status2 = Status.objects.create(name='In production')
        self.label1 = Labels.objects.create(name='Test Label1')
        self.label2 = Labels.objects.create(name='Test Label2')

        self.task1 = Task.objects.create(name='Task1',
                                         author=self.user1, status=self.status1)
        self.task2 = Task.objects.create(name='Task2',
                                         author=self.user1, status=self.status2)
        self.task3 = Task.objects.create(name='Task3',
                                         author=self.user2, status=self.status1)

    def test_filter_your_tasks_with_true(self):
        request = self.client.get(reverse('tasks'))
        request.user = self.user1
        filter_data = {'your_tasks': 'on'}
        task_filter = TaskFilter(filter_data, queryset=Task.objects.all(),
                                 request=request)
        self.assertEqual(list(task_filter.qs), [self.task1, self.task2])

    def test_filter_your_tasks_with_false(self):
        request = self.client.get(reverse('tasks'))
        request.user = self.user2
        filter_data = {'your_tasks': ''}
        task_filter = TaskFilter(filter_data, queryset=Task.objects.all(),
                                 request=request)
        self.assertEqual(set(task_filter.qs),
                         {self.task1, self.task2, self.task3})

    def test_model_name(self):
        self.assertEqual(str(self.task1), 'Task1')

    def test_get_context_data(self):
        response = self.client.get(reverse('task_delete',
                                           args=[self.task1.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['name'], self.task1.name)
        self.assertTemplateUsed(response, 'delete.html')
        # self.assertFalse(Task.objects.filter(id=self.task1.id).exists())

    def test_form_valid_creates_task(self):
        task_data = {
            'name': 'Test Task',
            'author': self.user1.id,
            'status': self.status1.id,
            'labels': [self.label1.id, self.label2.id]
        }

        response = self.client.post(reverse('task_create'), data=task_data)

        self.assertEqual(Task.objects.count(), 4)
        task = Task.objects.last()
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.author, self.user1)

        self.assertRedirects(response, reverse('tasks'))

        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]), 'Задача успешно создана')

    def test_form_invalid_does_not_create_task(self):
        invalid_task_data = {
            'name': 'Test Task',
            'author': self.user2.id,
            'status': '',
            'labels': [self.label1.id, self.label2.id]
        }

        form = TaskForm(data=invalid_task_data)
        self.assertFalse(form.is_valid())
        response = self.client.post(reverse('task_create'),
                                    data=invalid_task_data)

        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(response.status_code, 200)

        self.assertIn('status', form.errors)
        self.assertEqual(form.errors['status'],
                         ['Пожалуйста выберите элемент из этого списка'])
