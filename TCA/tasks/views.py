from dateutil.parser import parse

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.text import slugify

from TCA.administration.models import Course

from .models import Task


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
            task = get_object_or_404(Task, id=id)
        else:
            task = Task()
        task.name = request.POST['name']
        task.slug = slugify(request.POST['name'])
        task.course = course
        task.description = request.POST['description']
        task.due_date = parse(request.POST['due_date'])
        task.value = request.POST['value']
        task.need_response = request.POST.get('need_response', False)
        task.save()
        return redirect(reverse('dashboards.course', args=[course_key]))


@csrf_exempt
def delete_task(request, id):
    """Delete a Task object by id."""
    print 'DELETE TASK'
    task = get_object_or_404(Task, id=id)
    course = task.course
    task.delete()
    return redirect(reverse('dashboards.course', args=[course.key]))
