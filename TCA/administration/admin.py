# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Grade, Course, Teacher, Student, Father


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    search_fields = ['index', 'name']
    list_display = ['index', 'name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['key', 'name', 'grade']
    list_display = ['key', 'name', 'grade']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'last_name']
    list_display = ['name', 'last_name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['school_id', 'name', 'last_name', 'grade']
    list_display = ['school_id', 'name', 'last_name', 'grade']


@admin.register(Father)
class FatherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'last_name']
    list_display = ['name', 'last_name']
