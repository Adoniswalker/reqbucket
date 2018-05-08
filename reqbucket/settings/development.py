from .base import *

DEBUG = True

# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'putsreq',  # put the database name
        'USER': 'adoniswalker',  # put your username
        'PASSWORD': 'adonis254',  # put your password
        'HOST': 'localhost',  # specify the host
        'PORT': '5432',  # specify the port
    }
}
