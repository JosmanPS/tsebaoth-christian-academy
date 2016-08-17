# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from TCA.utils.models.mixins import TimeStamped


class Grade(TimeStamped):
    name = models.CharField(
        max_length=60,
        verbose_name='Nombre - Grado escolar'
    )
    index = models.IntegerField(
        verbose_name='Número - Grado escolar',
        unique=True
    )

    def __unicode__(self):
        return '%s - %s' % (
            self.index,
            self.name
        )

    class Meta:
        verbose_name = 'Grado escolar'
        verbose_name_plural = 'Grados escolares'
        ordering = ['index']


class Course(TimeStamped):
    key = models.CharField(
        max_length=12,
        verbose_name='Clave'
    )
    name = models.CharField(
        max_length=120,
        verbose_name='Nombre'
    )
    grade = models.ForeignKey(
        Grade,
        verbose_name='Grado escolar'
    )

    def __unicode__(self):
        return '%s - %s' % (
            self.key,
            self.name
        )

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['grade', 'key', 'name']


class Teacher(TimeStamped):
    user = models.OneToOneField(
        User,
        verbose_name='Usuario',
    )
    name = models.CharField(
        max_length=120,
        verbose_name='Nombre',
        db_index=True
    )
    last_name = models.CharField(
        max_length=120,
        verbose_name='Apellidos',
        db_index=True
    )
    courses = models.ManyToManyField(
        Course,
        verbose_name='Cursos'
    )

    def __unicode__(self):
        return 'Profesor: %s, %s' % (
            self.last_name,
            self.name
        )

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['last_name', 'name']


class Student(TimeStamped):
    user = models.OneToOneField(
        User,
        verbose_name='Usuario',
    )
    name = models.CharField(
        max_length=120,
        verbose_name='Nombre',
        db_index=True
    )
    last_name = models.CharField(
        max_length=120,
        verbose_name='Apellidos',
        db_index=True
    )
    school_id = models.CharField(
        max_length=20,
        verbose_name='Matrícula',
        unique=True
    )
    grade = models.ForeignKey(
        Grade,
        verbose_name='Grado escolar'
    )

    def __unicode__(self):
        return '%s - %s %s' % (
            self.school_id,
            self.name,
            self.last_name
        )

    class Meta:
        verbose_name = 'Líder',
        verbose_name_plural = 'Líderes',
        ordering = ['school_id', 'last_name', 'name']


class Father(TimeStamped):
    user = models.OneToOneField(
        User,
        verbose_name='Usuario',
    )
    name = models.CharField(
        max_length=120,
        verbose_name='Nombre',
        db_index=True
    )
    last_name = models.CharField(
        max_length=120,
        verbose_name='Apellidos',
        db_index=True
    )
    sons = models.ManyToManyField(
        Student,
        verbose_name='Hijos'
    )

    def __unicode__(self):
        return '%s %s' % (self.name, self.last_name)

    class Meta:
        verbose_name = 'Padre'
        verbose_name_plural = 'Padres'
        ordering = ['last_name', 'name']
