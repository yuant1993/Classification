from settings.base import *
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'

INSTALLED_APPS += (
    "django_extensions",
)

INTERNAL_IPS = (
    '127.0.0.1',
)

USE_HTTPS = False
SESSION_COOKIE_SECURE = USE_HTTPS
