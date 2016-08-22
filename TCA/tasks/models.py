# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from TCA.administration.models import Course
from TCA.utils.models.mixins import TimeStamped


class Task(TimeStamped):
    name = models.CharField(
        max_length=60,
        verbose_name='Nombre'
    )
    slug = models.SlugField(
        max_length=60,
        verbose_name='Slug',
        db_index=True
    )
    course = models.ForeignKey(
        Course,
        verbose_name='Curso',
        db_index=True
    )
    description = models.TextField(
        verbose_name='Descipción'
    )
    due_date = models.DateField(
        verbose_name='Fecha de entrega',
        db_index=True
    )
    value = models.FloatField(
        verbose_name='Valor en calificación final'
    )
    need_response = models.BooleanField(
        default=False,
        verbose_name='El alumno debe enviar respuesta'
    )

    def __unicode__(self):
        return '%s: %s' % (
            self.course.key,
            self.name
        )

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        unique_together = ('course', 'slug')
        ordering = ['course', 'due_date', 'slug']
