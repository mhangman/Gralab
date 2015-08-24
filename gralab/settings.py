"""
Django settings for gralab project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = {os.path.join(BASE_DIR, 'templates')}
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
MEDIA_ROOT = {os.path.join(BASE_DIR, 'media')}
STATIC_ROOT = "/home/ubuntu/gralab/static"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-#)9y&(y1)x_0^6umshr5o(+#dz($#u419=i=4k_eu@dfu3n^s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#add your hosts here
ALLOWED_HOSTS = [
'.gralab.pl',
'www.gralab.pl',
'gralab.pl',
'localhost',
]

ADMINS = ('admin', 'adminmail@mail.com',)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'homepage',
    'game',
    'tinymce',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'gralab.urls'

WSGI_APPLICATION = 'gralab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'x',
	'USER': 'x',
	'PASSWORD': 'x',
	'HOST': 'x',
	'PORT' : 'x',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

TINYMCE_DEFAULT_CONFIG = {
	'theme' : 'advanced',
}

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'x'
EMAIL_HOST_PASSWORD = 'x'
EMAIL_PORT = x
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'x@x.com'

RECAPTCHA_PUBLIC_KEY = 'x'
RECAPTCHA_PRIVATE_KEY = 'x'

os.environ['S3_USE_SIGV4'] = 'True'

AWS_ACCESS_KEY_ID ="x"
AWS_SECRET_ACCESS_KEY = "x"
BOTO_S3_BUCKET = "x"
BOTO_S3_HOST = "x"
AWS_S3_FORCE_HTTP_URL = False