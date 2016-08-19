
from .models import Teacher, Student, Father


def get_user_type(user):
    """Determine if a user is a Teacher, Student, Father or Admin."""
    if Student.objects.filter(user=user):
        return 'student'
    elif Father.objects.filter(user=user):
        return 'father'
    elif Teacher.objects.filter(user=user):
        return 'teacher'
    elif user.is_staff:
        return 'admin'
    else:
        return 'unknown'
