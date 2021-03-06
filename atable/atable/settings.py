"""
Django settings for atable project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vb^$p2-whw+vumg_byi_k1g#ero1#el6s_jvx!*u0jip=+p6rx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'recipes',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'atable.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static')],
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

WSGI_APPLICATION = 'atable.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = reverse_lazy('admin:login')
LOGOUT_URL = reverse_lazy('admin:logout')

# Grappelli

GRAPPELLI_ADMIN_TITLE = 'À Table'

GRAPPELLI_INDEX_DASHBOARD = 'atable.dashboard.CustomIndexDashboard'

# Django Debug Toolbar

DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': STATIC_URL + 'jquery-2.1.4.min.js',
                        }

# Atable specific settings

DEFAULT_RECIPE_LICENCE = """<h2> CC0 1.0 universel (CC0 1.0)</h2>
<em>Transfert dans le Domaine Public</em>

<h3>Cette licence est acceptable pour des œuvres culturelles libres.</h3>

<p>La personne qui a associé une œuvre à cet acte a dédié l’œuvre au domaine
public en renonçant dans le monde entier à ses droits sur l’œuvre selon les
lois sur le droit d’auteur, droit voisin et connexes, dans la mesure permise
par la loi.</p>

<p>Vous pouvez copier, modifier, distribuer et représenter l’œuvre, même à des
fins commerciales, sans avoir besoin de demander l’autorisation. Voir d’autres
informations ci-dessous.</p>

<h3>Autres informations</h3>

<ul>
<li>Les brevets et droits de marque commerciale qui peuvent être détenus par
autrui ne sont en aucune façon affectés par CC0, de même pour les droits que
pourraient détenir d’autres personnes sur l’œuvre ou sur la façon dont elle est
utilisée, comme le droit à l’image ou à la vie privée.</li>
<li>À moins d’une mention expresse contraire, la personne qui a identifié une
œuvre à cette notice ne concède aucune garantie sur l’œuvre et décline toute
responsabilité de toute utilisation de l’œuvre, dans la mesure permise par la
loi.</li>
<li>Quand vous utilisez ou citez l’œuvre, vous ne devez pas sous-entendre le
soutien de l’auteur ou de la personne qui affirme.</li>
</ul>"""

DEFAULT_RECIPE_AUTHOR = 'La Grande Ourse'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'

try:
    from .localsettings import *
except ImportError:
    pass
