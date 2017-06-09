# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView

from TCA.posts.models import Post, SimplePost, ImagePost, FilePost, PDFPost


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class SimplePostListView(ListView):
    model = SimplePost


class SimplePostDetailView(DetailView):
    model = SimplePost


class ImagePostListView(ListView):
    model = ImagePost


class ImagePostDetailView(DetailView):
    model = ImagePost


class FilePostListView(ListView):
    model = FilePost


class FilePostDetailView(DetailView):
    model = FilePost


class PDFPostListView(ListView):
    model = PDFPost


class PDFPostDetailView(DetailView):
    model = PDFPost
