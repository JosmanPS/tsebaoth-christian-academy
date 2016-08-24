from dateutil.parser import parse

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.text import slugify

from TCA.administration.models import Course
from TCA.administration.utils import get_user_type

from .models import Task, Response


class TaskView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(TaskView, self).dispatch(*args, **kwargs)

    def get(self, request, course_key, id=None):
        """Get task form for a related course."""
        course = get_object_or_404(Course, key=course_key)
        context = {"course": course}
        if id:
            task = get_object_or_404(Task, id=id)
            context['task'] = task
        return render(request, 'tasks/task_form.html', context)

    def post(self, request, course_key, id=None):
        """Validate and save form."""
        course = get_object_or_404(Course, key=course_key)
        if id:
            initialize = False
            task = get_object_or_404(Task, id=id)
        else:
            initialize = True
            task = Task()
        task.name = request.POST['name']
        task.slug = slugify(request.POST['name'])
        task.course = course
        task.description = request.POST['description']
        task.due_date = parse(request.POST['due_date'])
        task.value = request.POST['value']
        task.need_response = request.POST.get('need_response', False)
        task.save()
        if initialize:
            task.init_response_objects()
        return redirect(reverse('dashboards.course', args=[course_key]))


@csrf_exempt
def delete_task(request, id):
    """Delete a Task object by id."""
    task = get_object_or_404(Task, id=id)
    course = task.course
    task.delete()
    return redirect(reverse('dashboards.course', args=[course.key]))


class ResponseTeacherView(View):
    """View for responses score assignment."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(ResponseTeacherView, self).dispatch(*args, **kwargs)

    def get(self, request, task_id):
        """Show form for score assignation."""
        self._validate_teacher_user(request)
        task = get_object_or_404(Task, id=task_id)
        context = {
            'task': task,
            'course': task.course,
            'responses': task.responses
        }
        return render(request, 'tasks/task_responses.html', context)

    def post(self, request, task_id):
        """Save changes to task scores."""
        self._validate_teacher_user(request)
        task = get_object_or_404(Task, id=task_id)
        responses = task.responses
        scores = request.POST.getlist('inputs[]')
        for i in range(len(responses)):
            response = responses[i]
            response.score = scores[i]
            response.save()
        return HttpResponse(responses)

    def _validate_teacher_user(self, request):
        """Only teachers can access this views."""
        user_type = get_user_type(request.user)
        if user_type is not 'teacher':
            raise Http404('You are not authorized to this page.')
        return True


class StudentResponse(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(StudentResponse, self).dispatch(*args, **kwargs)

    def post(self, request):
        self._validate_student_user(request)
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        response = get_object_or_404(Response, task=task,
                                     student__user=request.user)
        response.response = request.POST.get('response', '')
        response.file = request.FILES.get('file', None)
        print request.POST
        print request.FILES
        response.save()
        return redirect(reverse('dashboards.main'))

    def _validate_student_user(self, request):
        """Only teachers can access this views."""
        user_type = get_user_type(request.user)
        if user_type is not 'student':
            raise Http404('You are not authorized to this page.')
        return True
