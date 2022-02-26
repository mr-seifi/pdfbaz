from .base import *

DEBUG = False

ADMINS = (
    ('Admin', 'info.pdfbaz@gmail.com')
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pdfbaz_db',
        'USER': 'pdfbaz_usr',
        'PASSWORD': 'PdF12321BAz#'
    }
}