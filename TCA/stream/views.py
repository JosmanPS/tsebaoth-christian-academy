# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render, get_object_or_404

from TCA.administration.models import Father
from TCA.administration.utils import get_user_type

from .models import Stream


def stream(request, grade_id):
    user = request.user
    user_type = get_user_type(user)
    if not (user_type == 'teacher' or user.is_staff):
        if user_type == 'student':
            raise Http404('No está autorizado para ver está página.')
        else:
            father = Father.objects.get(user=user)
            sons = father.sons.all()
            grades = [int(s.grade.id) for s in sons]
            if int(grade_id) not in grades:
                raise Http404('No está autorizado para ver está página.')
    stream = get_object_or_404(Stream, grade=grade_id)
    context = {'stream': stream}
    return render(request, 'stream/stream.html', context)


def allowed_streams(request):
    """Return a list of the allowed streams a user can see."""
    user = request.user
    user_type = get_user_type(user)
    if user_type in ['teacher', 'admin']:
        streams = Stream.objects.all()
    elif user_type == 'father':
        father = Father.objects.get(user=user)
        sons = father.sons.all()
        grades = [s.grade.id for s in sons]
        streams = Stream.objects.filter(grade__id__in=grades)
    else:
        raise Http404('No está autorizado para ver está página.')
    context = {'streams': streams}
    return render(request, 'stream/allowed_streams.html', context)
