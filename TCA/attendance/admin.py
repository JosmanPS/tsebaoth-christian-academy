# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    search_fields = ['course', 'date']
    list_display = ['course', 'date']
