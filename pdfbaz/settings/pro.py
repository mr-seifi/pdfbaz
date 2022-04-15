DEBUG = False

ADMINS = [
    ('Admin', 'info.pdfbaz@gmail.com')
]

ALLOWED_HOSTS = ['pdfbaz.com', 'www.pdfbaz.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pdfbaz_db',
        'USER': 'postgres',
        'PASSWORD': 'PdF12321BAz#'
    }
}
