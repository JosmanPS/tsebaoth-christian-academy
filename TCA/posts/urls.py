from django.conf.urls import url

from .views import PostListView, PostDetailView, PostView, DeletePost, allowed_posts


urlpatterns = []


urlpatterns = [
    url(r'^$', allowed_posts, name='list'),
    url(r'^grade/(?P<grade_id>[\d]+)/$', allowed_posts, name='list.grade'),
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
