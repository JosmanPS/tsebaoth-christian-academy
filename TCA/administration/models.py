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

    @property
    def students(self):
        """Show the students registered for this course."""
        return Student.objects.filter(
            grade=self.grade
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

    ACADEMIC_GRADE_CHOICES = (
        ('profesionalizandose', 'Profesionalizándose'),
        ('licenciatura', 'Licenciatura'),
        ('maestria', 'Maestría'),
    )

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
    email = models.EmailField(
        verbose_name='Correo electrónico',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Número telefónico',
        blank=True,
        null=True
    )
    identity = models.CharField(
        max_length=60,
        verbose_name='Identidad',
        db_index=True,
        blank=True,
        null=True
    )
    inprema = models.CharField(
        max_length=60,
        verbose_name='INPREMA',
        db_index=True,
        blank=True,
        null=True
    )
    escalafon = models.CharField(
        max_length=60,
        verbose_name='ESCALAFON',
        db_index=True,
        blank=True,
        null=True
    )
    college = models.CharField(
        max_length=60,
        verbose_name='Colegiación',
        blank=True,
        null=True
    )
    grade = models.CharField(
        max_length=60,
        verbose_name='Grado',
        db_index=True,
        blank=True,
        null=True
    )
    academic_grade = models.CharField(
        max_length=60,
        verbose_name='Formación académica',
        choices=ACADEMIC_GRADE_CHOICES,
        blank=True,
        null=True
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

    def get_parents(self, course_id):
        """Return a list of the parents from a course."""
        grade = Course.objects.get(id=course_id).grade
        students = Student.objects.filter(grade=grade)
        parents = [student.parents for student in students]
        parents = [parent for subset in parents for parent in subset]
        return parents

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
        unique=True,
        blank=True,
        null=True
    )
    grade = models.ForeignKey(
        Grade,
        verbose_name='Grado escolar'
    )
    identity = models.CharField(
        max_length=60,
        verbose_name='Identidad',
        db_index=True,
        blank=True,
        null=True
    )
    born_date = models.DateField(
        verbose_name='Fecha de nacimiento',
        blank=True,
        null=True
    )
    born_city = models.CharField(
        max_length=60,
        verbose_name='Ciudad de nacimiento',
        blank=True,
        null=True
    )
    born_country = models.CharField(
        max_length=60,
        verbose_name='País de nacimiento',
        blank=True,
        null=True
    )
    address = models.TextField(
        verbose_name='Dirección',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Número telefónico',
        blank=True,
        null=True
    )
    blood_type = models.CharField(
        max_length=4,
        verbose_name='Tipo de sangre',
        blank=True,
        null=True
    )
    alergies_illnesses = models.TextField(
        verbose_name='Alergias o enfermedades',
        blank=True,
        null=True
    )
    medicines = models.TextField(
        verbose_name='Medicinas que toma',
        blank=True,
        null=True
    )
    food_alergies = models.TextField(
        verbose_name='Alérgico a alimentos',
        blank=True,
        null=True
    )
    medicine_alergies = models.TextField(
        verbose_name='Alérgico a medicinas',
        blank=True,
        null=True
    )

    @property
    def tasks(self):
        from TCA.tasks.models import Task
        return Task.objects.filter(
            course__grade=self.grade
        )

    @property
    def parents(self):
        return Father.objects.filter(sons__id=self.id).values()

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

    MARITAL_STATUS_CHOICES = (
        ('single', 'Soltero'),
        ('married', 'Casado'),
        ('divorced', 'Divorciado'),
        ('widowed', 'Viudo')
    )
    EMPLOYEE_TYPE_CHOICES = (
        ('permanent', 'Empleado permanente'),
        ('contractor', 'Por contrato'),
        ('both', 'Ambas')
    )

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
    born_date = models.DateField(
        verbose_name='Fecha de nacimiento',
        blank=True,
        null=True
    )
    marital_status = models.CharField(
        verbose_name='Estado civil',
        max_length=15,
        choices=MARITAL_STATUS_CHOICES,
        default='married',
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='Correo electrónico',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Número telefónico',
        blank=True,
        null=True
    )
    proffession = models.CharField(
        max_length=60,
        verbose_name='Profesión u oficio',
        blank=True,
        null=True
    )
    have_job = models.BooleanField(
        verbose_name='Labora actualmente',
        default=True
    )
    work_address = models.TextField(
        verbose_name='Dirección de trabajo',
        blank=True,
        null=True
    )
    work_charge = models.CharField(
        verbose_name='Cargo que desempeña',
        max_length=60,
        blank=True,
        null=True
    )
    employee_type = models.CharField(
        max_length=60,
        choices=EMPLOYEE_TYPE_CHOICES,
        default='permanent'
    )
    responsible_for_student = models.BooleanField(
        verbose_name='Está encargado de sus hijos',
        default=False
    )
    responsible_for_payment = models.BooleanField(
        verbose_name='Está encargado del pago de colegiatura',
        default=False
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
