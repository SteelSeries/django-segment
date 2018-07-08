django-segment
==============
This a project to setup segment with django.

How to install
==============
Use pip:

.. code-block:: bash

    pip install django-segment

Or use a requirement file.

Settings
========
You must configure few things like the segment write key. You can configure
four variable in your settings file, the SEGMENT_WRITE_KEY, SEGMENT_DEBUG,
SEGMENT_SEND and SEGMENT_ON_ERROR, SEGMENT_WRITE_KEY is required others is
optional. For example:

.. code-block:: python

    DEBUG = True
    SEGMENT_WRITE_KEY = 'my_write_key'
    SEGMENT_DEBUG = DEBUG

Template
========
First add the context processors in your settings:

.. code-block:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'segment.context_processors.segment'
                ],
            },
        },
    ]

Then you can include the segment template in your base template:

.. code-block:: django

    {% include "_segment.html" %}

Enjoy folks.
