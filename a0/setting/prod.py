from a0.settings import *


SECRET_KEY = 'django-insecure-cz)=%nkg=ukgki*eq(7e72+)vkeu9rvz1=8c!z3n9lpljt14+d'

DEBUG = True

CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['p1.alinasiri.com', 'www.p1.alinasiri.com']


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'alinasir_travel',
    'USER':'alinasir_ali',
    'PASSWORD':'BvGQ]}naicJo',
    'HOST':'localhost',
    'PORT':'3306',
    }
}


STATIC_ROOT = '/home/alinasir/p1.alinasiri.com/static'
MEDIA_ROOT = '/home/alinasir/p1.alinasiri.com/media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


#django compressor
COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = True

if not COMPRESS_ENABLED:
    COMPRESS_ENABLED = True
    COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
    COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]