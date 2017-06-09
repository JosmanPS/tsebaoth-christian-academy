from django.contrib import admin
from django.contrib.auth import get_user_model

from TCA.posts.models import Post, SimplePost, ImagePost, FilePost, PDFPost


class AbstractPostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'created_at')

    def save_model(self, request, obj, form, change):
        try:
            obj.author
        except get_user_model().DoesNotExist:
            obj.author = request.user
        obj.save()


class PostAdmin(AbstractPostAdmin):
    prepopulated_fields = {"slug": ("headline",)}

admin.site.register(Post, PostAdmin)


# @admin.register(SimplePost)
# class SimplePostAdmin(admin.ModelAdmin):
#     list_display = ('post',)


@admin.register(ImagePost)
class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')


@admin.register(FilePost)
class FilePostAdmin(admin.ModelAdmin):
    list_display = ('post', 'file')


@admin.register(PDFPost)
class PDFPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'pdf')
