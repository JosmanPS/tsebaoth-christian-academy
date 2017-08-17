# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from TCA.administration.models import Grade
from TCA.utils.models.mixins import TimeStamped


class Stream(TimeStamped):
    grade = models.OneToOneField(
        Grade,
        db_index=True
    )
    url = models.CharField(
        'URL',
        max_length=1024)

    class Meta:
        ordering = ['grade']

    def __unicode__(self):
        return 'Stream: %s' % unicode(self.grade)
