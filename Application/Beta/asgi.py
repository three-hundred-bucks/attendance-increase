"""
ASGI config for Beta project.

It exposes the ASGI callable as a module-level variable named ``login``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Beta.settings')

application = get_asgi_application()
