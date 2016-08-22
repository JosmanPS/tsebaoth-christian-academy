from datetime import datetime
from dateutil.parser import parse

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.utils.decorators import method_decorator

from TCA.administration.utils import get_user_type
from TCA.administration.models import Course, Student

from .models import Attendance


class AttendanceView(View):
    """Main controller for saving attendance to courses."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Ask for login."""
        return super(AttendanceView, self).dispatch(*args, **kwargs)

    def get(self, request, course_key):
        """Show the form for saving attendance."""
        course = get_object_or_404(Course, key=course_key)
        today = datetime.today().date()
        attendance = Attendance.objects.filter(course=course, date=today)
        if attendance:
            attendance = [a.school_id for a in attendance[0].students.all()]
        return render(
            request,
            'attendance/course_attendance.html',
            {
                'course': course,
                'date': datetime.today().date(),
                'attendance': attendance
            }
        )

    def post(self, request, course_key):
        """Validate and save the attendance form."""
        course = get_object_or_404(Course, key=course_key)
        date = parse(request.POST.get('date')).date()
        attendance = request.POST.getlist('attendance[]', [])
        students = Student.objects.filter(school_id__in=attendance)
        obj = Attendance.objects.filter(course=course, date=date)
        if obj:
            obj = obj[0]
        else:
            obj = Attendance()
        obj.date = date
        obj.course = course
        obj.save()
        obj.students = students
        obj.save()
        return redirect(reverse('dashboards.course', args=[course_key]))

    def _validate_teacher_user(self, request):
        """Only teachers can access this views."""
        user_type = get_user_type(request.user)
        if user_type is not 'teacher':
            raise Http404('You are not authorized to this page.')
        return True
