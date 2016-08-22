from django.conf.urls import url

from .views import AttendanceView


urlpatterns = [
    url(
        r'course_attendance/(?P<course_key>[\w\-]+)/$',
        AttendanceView.as_view(),
        name='attendance.course'
    ),
]
