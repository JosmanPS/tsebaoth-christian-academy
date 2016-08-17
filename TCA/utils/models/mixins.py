"""Models classes for mixins utilities."""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStamped(models.Model):

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
        db_index=True
    )
    modified_at = models.DateTimeField(
        verbose_name=_('Modified at'),
        auto_now=True,
        db_index=True
    )

    class Meta:
        abstract = True


class WithTitle(models.Model):

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=50
    )

    class Meta:
        abstract = True
