# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from TCA.administration.models import Course, Student
from TCA.utils.models.mixins import TimeStamped


class Attendance(TimeStamped):
    date = models.DateField(
        verbose_name='Fecha',
        db_index=True,
        blank=True,
        null=True
    )
    course = models.ForeignKey(
        Course,
        verbose_name='Curso',
        db_index=True
    )
    students = models.ManyToManyField(
        Student,
        verbose_name='Estudiantes'
    )

    def __unicode__(self):
        return '%s: %s' % (
            self.course.key,
            self.created_at
        )

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        unique_together = ('course', 'created_at')
