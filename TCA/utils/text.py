# -*- coding: utf-8 -*-

from django.http import Http404
from django.utils.text import slugify


def slugifile(filename):
    """Elimina acentos y espacios de nombre de archivo.

    Este tipo de transformación es requerida para trabajar con
    archivos en Google Cloud Store. Pues la API no acepta cierto
    tipo de caracteres.
    """
    partitions = filename.split('.')
    if len(partitions) != 2:
        raise Http404('Nombre de archivo incorrecto.')
    filename, filetype = partitions
    filename = slugify(filename)
    return filename + '.' + filetype
