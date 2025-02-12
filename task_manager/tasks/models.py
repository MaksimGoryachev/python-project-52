from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Labels
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        verbose_name=_('Name'),
        unique=True,

    )

    description = models.TextField(
        max_length=2000,
        blank=True,
        verbose_name=_('Description'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation date'),
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status',
        verbose_name=_('Status'),
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author'),
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
        blank=True,
        null=True,
        verbose_name=_('Executor'),
    )

    labels = models.ManyToManyField(
        Labels,
        through='TaskLabelRelation',
        through_fields=('task', 'label'),
        blank=True,
        related_name='labels',
        verbose_name=_('Labels'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )
    label = models.ForeignKey(
        Labels, on_delete=models.PROTECT,
    )
