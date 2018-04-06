"""
WSGI config for pagejobs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

# PIP
from configurations import importer

# DJANGO
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phdnotes.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

importer.install()

application = get_wsgi_application()
