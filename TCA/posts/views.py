# -*- coding: utf-8 -*-

from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, View

from TCA.administration.utils import get_user_type
from TCA.administration.models import Course, Teacher, Father, Student
from TCA.utils.models.shortcuts import get_object_or_none

from TCA.posts.models import Post, ImagePost, PDFPost, FilePost


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


@login_required
def allowed_posts(request):
    """Return a list of the allowed streams a user can see."""
    user = request.user
    user_type = get_user_type(user)
    if user_type in ['teacher', 'admin']:
        posts = Post.objects.all()
    elif user_type == 'teacher':
        teacher = Teacher.objects.get(user=user)
        courses = [course.id for course in teacher.courses.all()]
        posts = Post.objects.filter(course__id__in=courses)
    elif user_type == 'father':
        father = Father.objects.get(user=user)
        sons = father.sons.all()
        grades = [s.grade.id for s in sons]
        posts = Post.objects.filter(course__grade__id__in=grades)
    elif user_type == 'student':
        student = Student.objects.get(user=user)
        posts = Post.objects.filter(course__grade=student.grade)
    else:
        raise Http404('No está autorizado para ver está página.')
    context = {'post_list': posts}
    return render(request, 'posts/post_list.html', context)


class PostView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(PostView, self).dispatch(*args, **kwargs)

    def get(self, request, course_key, id=None):
        """Get task form for a related course."""
        self._is_teacher_or_staff(request)
        course = get_object_or_404(Course, key=course_key)
        context = {"course": course}
        if id:
            post = get_object_or_404(Post, id=id)
            context['post'] = post
        return render(request, 'posts/post_form.html', context)

    def post(self, request, course_key, id=None):
        """Validate and save form."""
        course = get_object_or_404(Course, key=course_key)
        if id:
            post = get_object_or_404(Post, id=id)
        else:
            post = Post()
        post.author = request.user
        post.headline = request.POST['headline']
        post.slug = slugify(request.POST['headline'])
        post.text = request.POST['text']
        post.course = course
        post.save()
        post = self._add_content_elements(post, request)
        return redirect(reverse('dashboards.course', args=[course_key]))

    def _is_teacher_or_staff(self, request):
        user = request.user
        user_type = get_user_type(user)
        if not (user_type == 'teacher' or user.is_staff):
            raise Http404('No está autorizado para ver está página.')

    def _add_content_elements(self, post, request):
        post = self._add_image(post, request)
        post = self._add_file(post, request)
        post = self._add_pdf(post, request)
        return post

    def _add_image(self, post, request):
        image = request.FILES.get('image', None)
        if image is None:
            return post
        image_post = get_object_or_none(ImagePost, post=post)
        if image_post is None:
            image_post = ImagePost(post=post)
        image_post.image.save(image.name, image)
        return post

    def _add_file(self, post, request):
        file = request.FILES.get('file', None)
        if file is None:
            return post
        file_post = get_object_or_none(FilePost, post=post)
        if file_post is None:
            file_post = FilePost(post=post)
        file_post.file.save(file.name, file)
        return post

    def _add_pdf(self, post, request):
        pdf = request.FILES.get('pdf', None)
        if pdf is None:
            return post
        pdf_post = get_object_or_none(PDFPost, post=post)
        if pdf_post is None:
            pdf_post = PDFPost(post=post)
        pdf_post.pdf.save(pdf.name, pdf)
        return post


class DeletePost(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(DeletePost, self).dispatch(*args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, model, id):
        """Delete an specific type post."""
        self._is_teacher_or_staff(request)
        _model = self.get_model(model)
        post = get_object_or_404(_model, id=id)
        post.delete()
        return JsonResponse({
            'model': model,
            'id': id,
            'message': 'Se ha eliminado correctamente el objeto.'
        })

    def get_model(self, model):
        """Return the model selected."""
        models = {
            'Post': Post,
            'ImagePost': ImagePost,
            'FilePost': FilePost,
            'PDFPost': PDFPost
        }
        return models[model]

    def _is_teacher_or_staff(self, request):
        user = request.user
        user_type = get_user_type(user)
        if not (user_type == 'teacher' or user.is_staff):
            raise Http404('No está autorizado para realizar esta acción.')
