# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-17 23:47
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
