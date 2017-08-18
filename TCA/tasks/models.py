# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from TCA.administration.models import Course, Student
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

    @property
    def students(self):
        """Show students assignated to this task."""
        return Student.objects.filter(grade=self.course.grade)

    @property
    def responses(self):
        """Show responses assignated to this task."""
        return Response.objects.filter(task=self)

    def init_response_objects(self):
        """Create a Response object for each student in this task."""
        for student in self.students:
            Response.objects.create(
                student=student,
                task=self
            )
        return self.responses

    def __unicode__(self):
        return '%s: %s' % (
            self.course.key,
            self.name
        )

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        unique_together = ('course', 'slug')
        ordering = ['-due_date', 'course', 'slug']


class Response(TimeStamped):
    task = models.ForeignKey(
        Task,
        verbose_name='Tarea',
        db_index=True
    )
    student = models.ForeignKey(
        Student,
        verbose_name='Estudiante',
        db_index=True
    )
    score = models.FloatField(
        verbose_name='Calificación',
        blank=True,
        null=True
    )
    response = models.TextField(
        verbose_name='Respuesta'
    )
    file = models.FileField(
        verbose_name='Archivo adjunto'
    )

    @property
    def has_answer(self):
        return (self.response and self.file)

    def __unicode__(self):
        return '%s: %s' % (
            self.task,
            self.student
        )

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        unique_together = ('task', 'student')
        ordering = ['task', 'student', 'score']
