from django.conf.urls import url

from .views import TaskView, delete_task, ResponseTeacherView


urlpatterns = [
    url(r'delete/task/(?P<id>\d+)/$', delete_task, name='tasks.delete.task'),
    url(r'task/(?P<course_key>[\w\-]+)/$', TaskView.as_view(), name='tasks.form'),
    url(r'task/(?P<course_key>[\w\-]+)/(?P<id>\d+)/$', TaskView.as_view(), name='tasks.form.modify'),
    url(r'task/(?P<task_id>\d+)/responses/$', ResponseTeacherView.as_view(), name='task.responses'),
]
