# coding: utf-8
from django.conf import settings


SEGMENT_WRITE_KEY = getattr(settings, 'SEGMENT_WRITE_KEY')
SEGMENT_DEBUG = getattr(settings, 'SEGMENT_DEBUG', False)
SEGMENT_SEND = getattr(settings, 'SEGMENT_SEND', True)
SEGMENT_ON_ERROR = getattr(settings, 'SEGMENT_ON_ERROR', None)
