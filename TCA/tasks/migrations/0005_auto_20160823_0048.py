# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-23 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20160822_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='score',
            field=models.FloatField(blank=True, null=True, verbose_name='Calificaci\xf3n'),
        ),
    ]
