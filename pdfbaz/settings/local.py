from .base import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pdfbaz_db_local',
        'USER': 'postgres',
        'PASSWORD': 'PdF12321BAz#'
    }
}