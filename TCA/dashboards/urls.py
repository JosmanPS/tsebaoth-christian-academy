from django.conf.urls import url

from .views import Dashboard, CourseView


urlpatterns = [
    url(r'^main/$', Dashboard.as_view(), name='dashboards.main'),
    url(r'course/(?P<course_key>[\w\-]+)/$', CourseView.as_view(), name='dashboards.course')
]
