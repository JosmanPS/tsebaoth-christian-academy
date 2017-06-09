from django.conf.urls import url

from .views import *


urlpatterns = []


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>[\d]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/$',
        PostDetailView.as_view(), name='detail-by-slug'),
]
