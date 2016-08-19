from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator

from TCA.administration.utils import get_user_type
from TCA.administration.models import Teacher


class Dashboard(View):
    """Abstract class to control the views of the main page.

    When people click `MyTCA` a different dashboard page would
    appear depending of the user type:
        - Administrator
        - Teacher
        - Student
        - Father
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(Dashboard, self).dispatch(*args, **kwargs)

    def get(self, request):
        """Show main dashboard dependig of the user type."""
        user = get_user_type(request.user)
        if user == 'teacher':
            return TeacherDashboard().get(request)
        else:
            return UserDashboard().get(request)


class UserDashboard(View):
    """Abstract class View for user's dashboards."""

    user_type = 'abstract'

    def get(self, request):
        """Show user's custom dashboard."""
        context = self._get_custom_context(request)
        context['user_type'] = self.user_type
        return render(request, 'dashboards/dashboards.html', context)

    def _get_custom_context(self, request):
        return {}


class TeacherDashboard(UserDashboard):
    """Show teacher's registered courses."""

    user_type = 'teacher'

    def _get_custom_context(self, request):
        user_object = Teacher.objects.get(user=request.user)
        return {
            'courses': self._get_teacher_courses(user_object)
        }

    def _get_teacher_courses(self, user_object):
        return user_object.courses.all()
