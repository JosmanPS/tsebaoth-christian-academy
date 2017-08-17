# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-17 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0002_auto_20170817_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Modified at')),
                ('url', models.CharField(max_length=1024, verbose_name='URL')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Grade', unique=True)),
            ],
            options={
                'ordering': ['grade'],
            },
        ),
    ]
