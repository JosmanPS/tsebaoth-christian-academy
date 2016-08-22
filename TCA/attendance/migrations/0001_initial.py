# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified at')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Course', verbose_name='Curso')),
                ('students', models.ManyToManyField(to='administration.Student', verbose_name='Estudiantes')),
            ],
            options={
                'verbose_name': 'Asistencia',
                'verbose_name_plural': 'Asistencias',
            },
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('course', 'created_at')]),
        ),
    ]