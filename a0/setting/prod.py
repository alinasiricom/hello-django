from a0.settings import *


SECRET_KEY = 'django-insecure-cz)=%nkg=ukgki*eq(7e72+)vkeu9rvz1=8c!z3n9lpljt14+d'

DEBUG = True

CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['alinasiri.com', 'www.alinasiri.com']


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]