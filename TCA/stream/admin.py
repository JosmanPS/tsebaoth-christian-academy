from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Stream


@admin.register(Stream)
class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('grade', 'url')
