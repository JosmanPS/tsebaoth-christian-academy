# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Task, Response


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug', 'course', 'description', 'due_date']
    list_display = ['name', 'description', 'course', 'due_date',
                    'value', 'need_response']


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    search_fields = ['task', 'student']
    list_display = ['task', 'student', 'created_at', 'modified_at']
