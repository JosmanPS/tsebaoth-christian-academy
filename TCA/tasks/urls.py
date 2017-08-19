from django.conf.urls import url

from .views import (
    TaskView,
    delete_task,
    ResponseTeacherView,
    StudentResponse,
    TaskDetails
)


urlpatterns = [
    url(r'(?P<task_id>\d+)/$', TaskDetails.as_view(), name='tasks.details'),
    url(r'delete/task/(?P<id>\d+)/$', delete_task, name='tasks.delete.task'),
    url(r'task/(?P<course_key>[\w\-]+)/$', TaskView.as_view(), name='tasks.form'),
    url(r'task/(?P<course_key>[\w\-]+)/(?P<id>\d+)/$', TaskView.as_view(), name='tasks.form.modify'),
    url(r'task/(?P<task_id>\d+)/responses/$', ResponseTeacherView.as_view(), name='task.responses'),
    url(r'response/task/$', StudentResponse.as_view(), name='task.student.response')
]
