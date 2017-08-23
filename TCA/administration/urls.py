from django.conf.urls import url

from .views import teacher_send_mail


urlpatterns = []


urlpatterns += [
    url(r'^teacher_send_mail/$',
        teacher_send_mail, name='teacher_send_mail')
]
