# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 22:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified at')),
                ('key', models.CharField(max_length=12, verbose_name='Clave')),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
            ],
            options={
                'ordering': ['grade', 'key', 'name'],
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Father',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified at')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='Nombre')),
                ('last_name', models.CharField(db_index=True, max_length=120, verbose_name='Apellidos')),
                ('born_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('marital_status', models.CharField(choices=[('single', 'Soltero'), ('married', 'Casado'), ('divorced', 'Divorciado'), ('widowed', 'Viudo')], default='married', max_length=15, verbose_name='Estado civil')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electr\xf3nico')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='N\xfamero telef\xf3nico')),
                ('proffession', models.CharField(max_length=60, verbose_name='Profesi\xf3n u oficio')),
                ('have_job', models.BooleanField(default=True, verbose_name='Labora actualmente')),
                ('work_address', models.TextField(verbose_name='Direcci\xf3n de trabajo')),
                ('work_charge', models.CharField(max_length=60, verbose_name='Cargo que desempe\xf1a')),
                ('employee_type', models.CharField(choices=[('permanent', 'Empleado permanente'), ('contractor', 'Por contrato'), ('both', 'Ambas')], default='permanent', max_length=60)),
                ('responsible_for_student', models.BooleanField(default=False, verbose_name='Est\xe1 encargado de sus hijos')),
                ('responsible_for_payment', models.BooleanField(default=False, verbose_name='Est\xe1 encargado del pago de colegiatura')),
            ],
            options={
                'ordering': ['last_name', 'name'],
                'verbose_name': 'Padre',
                'verbose_name_plural': 'Padres',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=60, verbose_name='Nombre - Grado escolar')),
                ('index', models.IntegerField(unique=True, verbose_name='N\xfamero - Grado escolar')),
            ],
            options={
                'ordering': ['index'],
                'verbose_name': 'Grado escolar',
                'verbose_name_plural': 'Grados escolares',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified at')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='Nombre')),
                ('last_name', models.CharField(db_index=True, max_length=120, verbose_name='Apellidos')),
                ('school_id', models.CharField(max_length=20, unique=True, verbose_name='Matr\xedcula')),
                ('identity', models.CharField(db_index=True, max_length=60, verbose_name='Identidad')),
                ('born_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('born_city', models.CharField(max_length=60, verbose_name='Ciudad de nacimiento')),
                ('born_country', models.CharField(max_length=60, verbose_name='Pa\xeds de nacimiento')),
                ('address', models.TextField(verbose_name='Direcci\xf3n')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='N\xfamero telef\xf3nico')),
                ('blood_type', models.CharField(max_length=4, verbose_name='Tipo de sangre')),
                ('alergies_illnesses', models.TextField(verbose_name='Alergias o enfermedades')),
                ('medicines', models.TextField(verbose_name='Medicinas que toma')),
                ('food_alergies', models.TextField(verbose_name='Al\xe9rgico a alimentos')),
                ('medicine_alergies', models.TextField(verbose_name='Al\xe9rgico a medicinas')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Grade', verbose_name='Grado escolar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'ordering': ['school_id', 'last_name', 'name'],
                'verbose_name': ('L\xedder',),
                'verbose_name_plural': ('L\xedderes',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified at')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='Nombre')),
                ('last_name', models.CharField(db_index=True, max_length=120, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electr\xf3nico')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='N\xfamero telef\xf3nico')),
                ('identity', models.CharField(db_index=True, max_length=60, verbose_name='Identidad')),
                ('inprema', models.CharField(db_index=True, max_length=60, verbose_name='INPREMA')),
                ('escalafon', models.CharField(db_index=True, max_length=60, verbose_name='ESCALAFON')),
                ('college', models.CharField(max_length=60, verbose_name='Colegiaci\xf3n')),
                ('grade', models.CharField(db_index=True, max_length=60, verbose_name='Grado')),
                ('academic_grade', models.CharField(choices=[('profesionalizandose', 'Profesionaliz\xe1ndose'), ('licenciatura', 'Licenciatura'), ('maestria', 'Maestr\xeda')], max_length=60, verbose_name='Formaci\xf3n acad\xe9mica')),
                ('courses', models.ManyToManyField(to='administration.Course', verbose_name='Cursos')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'ordering': ['last_name', 'name'],
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.AddField(
            model_name='father',
            name='sons',
            field=models.ManyToManyField(to='administration.Student', verbose_name='Hijos'),
        ),
        migrations.AddField(
            model_name='father',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='course',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Grade', verbose_name='Grado escolar'),
        ),
    ]
