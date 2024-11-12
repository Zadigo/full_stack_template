import os
from datetime import timedelta
from pathlib import Path

import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

if (BASE_DIR / '.env').exists():
    dotenv.load_dotenv(BASE_DIR / '.env')


def get_debug():
    debug = os.getenv('DEBUG', '0')
    return True if debug == '0' else False


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_debug()

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',

    'allauth',
    'allauth.usersessions',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',


    'rest_framework',
    'rest_framework.authtoken',

    'channels',
    'django_analytics',
    'django_seo',
    'django_mobile',
    'django_extensions',
    'django_celery_beat',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_ckeditor_5',
    'debug_toolbar',
    'import_export',

    'accounts',
    'promailing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'myfullstack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION = 'myfullstack.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'filename': 'myfullstack/django_debug.log'
        },
        'failed_requests': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'filename': 'myfullstack/failed_requests.log'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True
        },
        'django.request': {
            'handlers': ['failed_requests'],
            'filters': ['failed_request_filter'],
            'formatter': 'failed',
            'propagate': False
        }
    },
    'formatters': {
        'failed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'style': '%'
        }
    },
    'filters': {
        'failed_request_filter': {
            '()': 'myfullstack.custom_logging.FailedRequestFilter'
        }
    }
}


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'cache'
    }
}

if not DEBUG:
    # Use Redis a backend for caching instead of
    # the file system caching that we use for debugging
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

    REDIS_URL = f'redis://:{REDIS_PASSWORD}@redis:6379'

    CACHES['default'] = {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 60 * 15,
        'OPTIONS': {
            'PASSWORD': REDIS_PASSWORD,
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }

    CACHES['memcache'] = {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': 'memcache:11211'
    }


# Celery
# https://docs.celeryq.dev/en/stable/index.html

CELERY_TIMEZONE = 'Europe/Paris'

CELERY_TASK_TRACK_STARTED = True

CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'Europe/Oslo'

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


if os.getenv('USES_HTTP_SCHEME', 'http') == 'https':
    SESSION_COOKIE_SECURE = True

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    SECURE_PROXY_SSL_HEADERSSL_REDIRECT = True


# Sites

SITE_ID = 1


# CORS

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGIN_REGEXES = [
    r'https://*.ngrok-free.app',
    r'^https?\:\/\/*.gency313.fr$'
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'https://app.gency313.fr',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'https://app.gency313.fr',
    'https://emailing-admin.gency313.fr'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
    'UPDATE_LAST_LOGIN': True,
    'AUTH_HEADER_TYPES': ['Token']
}


# Sites

SITE_ID = 1


# ACCOUNTS

AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'accounts.backends.EmailAuthenticationBackend'
]


# Emailing

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_USE_LOCALTIME = True


# Debug

INTERNAL_IPS = [
    '127.0.0.1'
]


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Promailing

# PROMAILING_EMAIL_VERIFICATION_BACKEND = 'accounts.EmailVerificationCode'

PROMAILING_EMAIL_VERIFICATION_REDIRECT = 'http://localhost:3000?redirect=verify'


# Django All Auth for more information
# on the settings for django-allauth
# https://docs.allauth.org/en/latest/socialaccount/provider_configuration.html
# For two factor authentication, see:
# https://stackoverflow.com/questions/54908541/django-two-factor-authentication
# https://github.com/pyauth/pyotp?tab=readme-ov-file
# https://github.com/soldair/node-qrcode

USERSESSIONS_TRACK_ACTIVITY = False

SOCIALACCOUNT_FORMS = {
    'signup': 'accounts.forms.SocialSignupForm',
    'disconnect': 'accounts.forms.SocialLogoutForm',
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APPS': [
            {
                'client_id': os.getenv('GOOGLE_CLIENT_ID'),
                'secret': os.getenv('GOOGLE_SECRET'),
                'key': ''
            }
        ],
        # These are provider-specific settings that can only be
        # listed here:
        'SCOPE': [
            "profile",
            "email",
        ],
        'AUTH_PARAMS': {
            "access_type": "online",
        }
    }
}

DEFAULT_FROM_EMAIL = 'contact@gency313.fr'

N8N_TEST_API_URL = 'https://n8n.gency313.fr/webhook-test/'

N8N_API_URL = 'https://n8n.gency313.fr/webhook/'


USE_S3 = False
