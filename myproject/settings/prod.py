from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Nightly log rotation w/ 5 day history
LOGGING['handlers'].update({
    'file': {
        'level': 'INFO',
        'class': 'logging.handlers.TimedRotatingFileHandler',
        'formatter': 'verbose',
        'filename': '/home/me/logs/user/mysite/myproject_django.error.log',
        'when': 'midnight',
        'interval': 1,
        'backupCount': 5
    }
})

LOGGING['loggers']['myproject'].update({'handlers': ['file']})

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/New_York'

SITE_ID = 1

MEDIA_ROOT = '' # Example: "/home/me/mysite/media/"
MEDIA_URL = 'http://localhost:8000/common/'
ADMIN_MEDIA_PREFIX = '/admin/media/'

TEMPLATE_DIRS = () # Example: ('/home/me/mysite/templates')