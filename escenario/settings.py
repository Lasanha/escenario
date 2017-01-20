import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = os.environ.get('ESCENARIO_DEBUG', 'false') == 'true'

if DEBUG:
    GA_CODE = ''
    GADSENSE_CLIENT = ''
    GADSENSE_SLOT = ''
else:
    GA_CODE = os.environ.get('GA_CODE', '')
    GADSENSE_CLIENT = os.environ.get('GADSENSE_CLIENT', '')
    GADSENSE_SLOT = os.environ.get('GADSENSE_SLOT', '')

ADMINS = (
    ('Gabriel Marcondes', os.environ.get('ADMIN_EMAIL', 'test@example.com')),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False
USE_L10N = False
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = os.environ['SECRET_KEY']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        }
    }
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'escenario.urls'

WSGI_APPLICATION = 'escenario.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'generator',
    'django_summernote',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'default_cache',
    },
    'escenario': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'escenario_cache',
    }
}

ESCENARIO_CACHE = {
    'CACHE_NAME': 'escenario',

    'HOME_TIME': 1,
    'ABOUT_TIME': 60*60,
    'LIST_TIME': 5,

    'IMG_CREATION': {
        'F_TITULO': 34,
        'F_FALTAM': 34,
        'F_TEXTO': 12,
        'F_WRAP': 40,
        'FONT_TITLE': os.path.join(BASE_DIR, 'ROADWAY_.TTF'),
        'FONT_TEXT': os.path.join(BASE_DIR, 'kharon.ttf'),
    }
}

ADMIN_MEDIA_PREFIX = '/static/admin/'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

if os.environ.get('ESCENARIO_ENVIRONMENT') == 'PROD':
    import dj_database_url
    db_url = os.environ['HEROKU_POSTGRESQL_YELLOW_URL']
    DATABASES = {
        'default': dj_database_url.config(default=db_url)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'dev.db'
        }
    }

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/restricted/'
