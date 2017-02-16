from .common import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'statc')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'nomade.mysql.pythonanywhere-services.com',
        'NAME': 'nomade$default',
        'USER': 'nomade',
        'PASSWORD': 'qwer1234',
        'OPTIONS': {
            'sql_mode': 'traditional',  # strict mode
        },
    },
}

