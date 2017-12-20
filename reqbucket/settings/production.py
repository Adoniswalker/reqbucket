from .base import *

DEBUG = False

ALLOWED_HOSTS = ['adoniswalker.pythonanywhere.com', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adoniswalker$req_db',
        'USER': 'adoniswalker',
        'PASSWORD': 'Adonis254.',
        'HOST': 'adoniswalker.mysql.pythonanywhere-services.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


