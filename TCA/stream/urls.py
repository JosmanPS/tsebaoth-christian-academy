from django.conf.urls import url

from .views import stream, allowed_streams


urlpatterns = []


urlpatterns += [
    url(r'^$', allowed_streams, name='streams'),
    url(r'^stream/(?P<grade_id>[\d]+)/$', stream, name='stream')
]
