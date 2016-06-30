# coding: utf-8
from django.apps import AppConfig
from django.utils.module_loading import import_string
from django.core.exceptions import ImproperlyConfigured
import analytics

from . import settings


class SegmentConfig(AppConfig):
    name = 'segment'

    def ready(self):
        analytics.write_key = settings.SEGMENT_WRITE_KEY
        try:
            analytics.debug = bool(settings.SEGMENT_DEBUG)
        except Exception:
            raise ImproperlyConfigured('SEGMENT_DEBUG settings must be a boolean value')

        try:
            analytics.send = bool(settings.SEGMENT_SEND)
        except Exception:
            raise ImproperlyConfigured('SEGMENT_SEND must be a boolean value')

        if settings.SEGMENT_ON_ERROR is not None:
            analytics.on_error = import_string(settings.SEGMENT_ON_ERROR)
