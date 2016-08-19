from django.conf.urls import url

from .views import Dashboard


urlpatterns = [
    url(r'^main/$', Dashboard.as_view(), name='dashboards.main'),
]
