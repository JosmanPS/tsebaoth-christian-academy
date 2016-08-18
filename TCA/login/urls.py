from django.conf.urls import url

from .views import Login, logout_view


urlpatterns = [
    url(r'^login/$', Login.as_view(), name='accounts.login'),
    url(r'^logout/$', logout_view, name='accounts.logout'),
]
