"""TCA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from .views import index

urlpatterns = [
    url(r'^$', index),

    url(r'^admin/', admin.site.urls),

    url(r'^filer/', include('filer.urls')),

    url(r'^accounts/', include('TCA.login.urls')),
    url(r'^administration/', include('TCA.administration.urls')),
    url(r'^dashboards/', include('TCA.dashboards.urls')),
    url(r'^tasks/', include('TCA.tasks.urls')),
    url(r'^attendance/', include('TCA.attendance.urls')),
    url(r'^posts/', include('TCA.posts.urls', namespace='posts')),
    url(r'^stream/', include('TCA.stream.urls')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

admin.site.site_header = 'Tsebaoth Christian Academy'
