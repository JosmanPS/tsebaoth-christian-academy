# -*- coding: utf-8 -*-

"""Functions for mail utilites."""

from django.http import HttpResponse
from django.shortcuts import render

from google.appengine.api import app_identity, mail

from .models import Teacher, Course


def teacher_send_mail(request):
    """Send email to an specific user."""
    user = request.user
    teacher = Teacher.objects.get(user=user)
    # course_id = request.POST['course_id']
    course_id = 1
    course = Course.objects.get(id=course_id)
    parents = teacher.get_parents(course_id)
    mails = [parent['email'] for parent in parents if parent['email'] != '']
    # subject = request.POST['subject']
    subject = 'Prueba TCA'
    # body = reques.POST['body']
    body = 'Probando mail de TCA.'
    mail.send_mail(
        sender='{}@appspot.gserviceaccount.com'.format(
            app_identity.get_application_id()
        ),
        to=mails,
        subject=subject,
        body=("""
        %s

        --
        Profesor: %s %s <%s>.
        Curso: %s.
        """ % (
            body,
            teacher.name, teacher.last_name, user.email,
            unicode(course)
        ))
    )
    return HttpResponse(mails)
