from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

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
# EMAIL_SUBJECT_PREFIX = '[Test mail]'

