from django.conf.urls import url

from .views import PostListView, PostDetailView, PostView, DeletePost


urlpatterns = []


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>[\d]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/$',
        PostDetailView.as_view(), name='detail-by-slug'),

    url(r'create/(?P<course_key>[\w\-]+)/$',
        PostView.as_view(), name='form'),
    url(r'modify/(?P<course_key>[\w\-]+)/(?P<id>[\d]+)/$',
        PostView.as_view(), name='form.modify'),
    url(r'delete/(?P<model>[\w\-]+)/(?P<id>[\d]+)/$',
        DeletePost.as_view(), name='delete')
]
