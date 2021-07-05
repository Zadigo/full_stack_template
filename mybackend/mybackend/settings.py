from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

FRONTEND_DIR = Path.joinpath(BASE_DIR, 'frontend')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0+8o3mn#2myq16qx@%56z48m2$juvr(d*8eb+%@&li@bac_-+@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_extensions',

    'accounts',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mybackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            Path.joinpath(FRONTEND_DIR, 'dist')
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

WSGI_APPLICATION = 'mybackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_ROOT = Path.joinpath(BASE_DIR, 'static')

STATICFILES_DIRS = [
    Path.joinpath(FRONTEND_DIR, 'dist/static')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')


# CORS

# If this is used then `CORS_ORIGIN_WHITELIST` 
# will not have any effect
CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_CREDENTIALS = True

# If this is used, then not need 
# to use `CORS_ORIGIN_ALLOW_ALL = True`
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://192.168.0.104:8080',
]

CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:8080',
    'http://192.168.0.104:8080',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',
    'http://192.168.0.104:8080',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}


# ACCOUNTS

AUTH_USER_MODEL = 'accounts.MyUser'

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailAuthenticationBackend'
]

AUTH_USER_PROFILE_MODEL = 'accounts.MyUserProfile'


# Emailing

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = ''

EMAIL_HOST_PASSWORD = ''

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_USE_LOCALTIME = True


# Debug

INTERNAL_IPS = [
    '127.0.0.1'
]
