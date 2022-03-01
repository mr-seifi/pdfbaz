DEBUG = False

ADMINS = (
    ('Admin', 'info.pdfbaz@gmail.com')
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pdfbaz_db',
        'USER': 'postgres',
        'PASSWORD': 'PdF12321BAz#'
    }
}