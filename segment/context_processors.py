# coding: utf-8
from . import settings


def segment(request):
    return {
        'SEGMENT_WRITE_KEY': settings.SEGMENT_WRITE_KEY,
        'SEGMENT_DEBUG': settings.SEGMENT_DEBUG,
    }
