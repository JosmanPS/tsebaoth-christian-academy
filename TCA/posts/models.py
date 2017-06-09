# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from TCA.administration.models import Course
from TCA.utils.models.mixins import TimeStamped


class AbstractPost(TimeStamped):
    author = models.ForeignKey(
        User,
        editable=False,
        related_name="%(app_label)s_%(class)s"
    )
    headline = models.CharField(
        'Encabezado',
        max_length=255,
        db_index=True)
    text = models.TextField('Texto')

    class Meta:
        ordering = ['-created_at']
        abstract = True

    def __unicode__(self):
        return self.headline


class SlugPostMixin(models.Model):
    slug = models.SlugField("Slug", max_length=150)

    @models.permalink
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

    class Meta:
        abstract = True


class TCAPostMixin(models.Model):
    course = models.ForeignKey(
        Course,
        db_index=True,
        verbose_name='Curso'
    )

    @property
    def grade(self):
        return self.course.grade

    class Meta:
        abstract = True


class Post(AbstractPost, SlugPostMixin, TCAPostMixin):
    pass


class PostContentAbstract(TimeStamped):
    post = models.ForeignKey(
        Post,
        verbose_name='Post'
    )

    class Meta:
        ordering = ['-created_at']
        abstract = True

    def __unicode__(self):
        return unicode(self.post)


class SimplePost(PostContentAbstract):
    pass


class ImagePost(PostContentAbstract):
    image = models.ImageField(
        verbose_name='Imágen'
    )


class PDFPost(PostContentAbstract):
    pdf = models.FileField(
        verbose_name='Archivo PDF'
    )


class FilePost(PostContentAbstract):
    file = models.FileField(
        verbose_name='Archivo adjunto'
    )
