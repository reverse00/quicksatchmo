import os
DIRNAME = os.path.abspath(os.path.dirname(__file__))
LOCAL_DEV = True

MEDIA_ROOT = os.path.join(DIRNAME, 'static/')
MEDIA_URL = '/static/'

MIDDLEWARE_CLASSES = ("django.middleware.locale.LocaleMiddleware",
                      "django.middleware.common.CommonMiddleware",
                      "django.contrib.sessions.middleware.SessionMiddleware",
                      "django.middleware.doc.XViewMiddleware",
                      "django.contrib.auth.middleware.AuthenticationMiddleware",
                      "satchmo.shop.SSLMiddleware.SSLRedirect",
                      "satchmo.recentlist.middleware.RecentProductMiddleware")

TEMPLATE_DIRS = (os.path.join(DIRNAME, "templates"))
TEMPLATE_CONTEXT_PROCESSORS =   ('satchmo.shop.context_processors.settings',
                                 'django.core.context_processors.auth',
                                 'satchmo.recentlist.context_processors.recent_products',
                                 )

INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.comments',
        'comment_utils',
        'django.contrib.sitemaps',
        'satchmo.caching',
        'satchmo.configuration',
        'satchmo.shop',
        'satchmo.contact',
        'satchmo.product',
        'satchmo.shipping',
        'satchmo.payment',
        'satchmo.discount',
        'satchmo.giftcertificate',
        'satchmo.supplier',
        'satchmo.thumbnail',
        'satchmo.l10n',
        'satchmo.tax',
        'satchmo.recentlist',
        )

AUTHENTICATION_BACKENDS = (
    'satchmo.accounts.email-auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend'
    )

# Load the local settings
from local_settings import *
from qs_settings import *
