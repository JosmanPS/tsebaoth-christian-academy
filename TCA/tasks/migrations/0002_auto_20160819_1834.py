# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 18:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['course', 'due_date', 'slug'], 'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
    ]
