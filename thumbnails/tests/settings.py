# -*- coding: utf-8 -*-


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}


INSTALLED_APPS = (
    'thumbnails',
    'thumbnails.tests',
)

SECRET_KEY = 'a'

THUMBNAILS = {
    'METADATA': {
        'PREFIX': 'djthumbs-test',
        'BACKEND': 'thumbnails.backends.metadata.DatabaseBackend',
    },
    'STORAGE': {
        'BACKEND': 'thumbnails.tests.storage.TemporaryStorage'
    },
    'BASEDIR': 'thumbs',
    'POST_PROCESSORS': [{
        'processor': 'thumbnails.post_processors.optimize',
        'png_command': "/usr/local/bin/optipng -force -o7 &> /dev/null '%(filename)s'"
    }],
    'SIZES': {
        'small': {
            'processors': [
                {'processor': 'thumbnails.processors.resize', 'width': 10, 'height': 10}
            ],
        },
        'default': {
            'processors': [
                {'processor': 'thumbnails.processors.resize', 'width': 20, 'height': 20},
                {'processor': 'thumbnails.processors.flip', 'direction': 'horizontal'}
            ],
        },
        'large': {
            'processors':[
                {'processor': 'thumbnails.processors.resize', 'width': 80, 'height': 80},
                {'processor': 'thumbnails.processors.rotate', 'degrees': 45},
                {'processor': 'thumbnails.processors.crop', 'width': 80, 'height': 80, 'center': ('50%,50%')}
            ]
        },
        'source': {
            'processors': [
                {'processor': 'thumbnails.processors.resize', 'width': 90, 'height': 90}
            ]
        }
    }
}
