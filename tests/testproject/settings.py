import os

DEBUG = True
TEMPLATE_DEBUG = True

TIME_ZONE = 'Europe/Berlin'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'rest_framework',
    'testproject'
)

ROOT_URLCONF = 'testproject.urls'

SECRET_KEY = '9q7324#45RWtw843q$%&/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3'),
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    'DEFAULT_PAGINATION_CLASS': 'drf_hal_json.pagination.HalPageNumberPagination',
    'DEFAULT_PARSER_CLASSES': ('drf_hal_json.parsers.JsonHalParser',),
    'DEFAULT_RENDERER_CLASSES': ('drf_hal_json.renderers.JsonHalRenderer',),
}

STATIC_URL = '/static/'
