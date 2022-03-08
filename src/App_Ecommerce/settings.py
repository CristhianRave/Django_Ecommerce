import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------------------------------------------

SECRET_KEY = 'django-insecure-zofe88bd8-$w)d68a%u3-6b7^qp2lc@ne!!zbv7mirc5#$c^su'


DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# -----------------------------------------------------------

DEFAULT_FROM_EMAIL= ('cristhian233027@gmail.com')
NOTIFY_EMAIL = ('Notificacion dede Django_Ecommerce')
# -----------------------------------------------------------

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'cart',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'App_Ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'App_Ecommerce.wsgi.application'



# -----------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -----------------------------------------------------------

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



# -----------------------------------------------------------

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# -----------------------------------------------------------

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -----------------------------------------------------------

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# -----------------------------------------------------------

# if DEBUG is False:
#     SESSION_COOKIE_SECURE = True
#     SECURE_BROWSER_XSS_FILTER = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_SECONDS = 31536000
#     SECURE_REDIRECT_EXEMPT = []
#     SECURE_SSL_REDIRECT = True
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#     ALLOWED_HOSTS = ['https://google.com']

#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': '',
#             'USER': '',
#             'PASSWORD': '',
#             'HOST': '',
#             'PORT': '',
#         }

#     }

# -----------------------------------------------------------


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
