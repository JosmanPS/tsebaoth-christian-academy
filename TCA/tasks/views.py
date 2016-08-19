from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.utils.decorators import method_decorator

from TCA.administration.models import Course


class TaskView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(TaskView, self).dispatch(*args, **kwargs)

    def get(self, request, course_key):
        """Get task form for a related course."""
        course = get_object_or_404(Course, key=course_key)
        return render(request, 'tasks/task_form.html', {'course': course})

    def post(self, request, course_key):
        """Validate and save form."""
        course = get_object_or_404(Course, key=course_key)
        print request.POST
        return redirect(reverse('dashboards.course', args=[course_key]))
