from django.conf.urls import url

from .views import TaskView


urlpatterns = [
    url(r'task/(?P<course_key>[\w\-]+)/$', TaskView.as_view(), name='tasks.form')
]
