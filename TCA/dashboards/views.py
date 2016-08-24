from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator

from TCA.administration.utils import get_user_type
from TCA.administration.models import Course, Teacher, Student
from TCA.attendance.models import Attendance
from TCA.tasks.models import Task


#
#           Main Dashboard views
#


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
        elif user == 'admin':
            return AdminDashboard().get(request)
        elif user == 'student':
            return StudentDashboard().get(request)
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


class StudentDashboard(UserDashboard):
    """Show student's assignated tasks."""

    user_type = 'student'

    def _get_custom_context(self, request):
        user_object = Student.objects.get(user=request.user)
        return {
            'tasks': self._get_student_tasks(user_object)
        }

    def _get_student_tasks(self, user):
        return Task.objects.filter(
            course__grade=user.grade,
            due_date__gte=datetime.today().date()
        )


class AdminDashboard(UserDashboard):
    """Redirect to the site's admin page."""

    user_type = 'admin'

    def get(self, request):
        """Redirect to the site's admin page."""
        return redirect('/admin/')


#
#           Courses views
#

class CourseView(View):
    """View class for control actions related to a registered course."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(CourseView, self).dispatch(*args, **kwargs)

    def get(self, request, course_key):
        """Send a `Course` object."""
        course = get_object_or_404(Course, key=course_key)
        context = {'course': course}
        context['tasks'] = self._get_course_tasks(course)
        attendance = Attendance.objects.filter(
            course=course,
            date=datetime.today().date()
        )
        if attendance:
            attendance = attendance[0]
        context['attendance'] = attendance
        return render(request, 'dashboards/course.html', context)

    def _get_course_tasks(self, course):
        return Task.objects.filter(course=course)
