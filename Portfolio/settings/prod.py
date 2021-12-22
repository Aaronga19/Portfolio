from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['aaronportfol.herokuapp.com', 'localhost']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Config with decouple
# import dj_database_url
# from decouple import config

# DATABASES = {
#     'default':dj_database_url.config(
#         default=config(settings.database_url)
#     )

# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': settings.database_name,
        'USER': settings.database_username,
        'PASSWORD': settings.database_password,
        'HOST': settings.database_hostname,
        'PORT': settings.database_port
    }
}
# TO HEROKU

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
) 
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# AWS S3

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'

AWS_ACCESS_KEY_ID = settings.aws_id
AWS_SECRET_ACCESS_KEY = settings.aws_access
AWS_STORAGE_BUCKET_NAME = settings.aws_name

AWS_QUERYSTRING_AUTH = False
                                                # DOCKER --- MEDIA_ROOT = '/Portfolio/media/' #MEDIA_ROOT = '/media/'

# ckeditor SETTINGS

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
 
CKEDITOR_CONFIGS = {
    'default':{
        'toolbar':'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline',],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyList'],
            ['TextColor', 'Format', 'FontSize', 'Link'],
            ['Smiley', 'Image', 'Iframe'],
            ['RemoveFormat', 'Source'],
        ],
        'stylesSet' : [],
    }
}


# EMAIL SETTINGS

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = settings.email
EMAIL_HOST_PASSWORD = settings.pass_email
EMAIL_PORT = 587


