from django.core.exceptions import ObjectDoesNotExist


def get_object_or_none(object_class, **kwargs):
    try:
        return object_class.objects.get(**kwargs)
    except ObjectDoesNotExist:
        return None