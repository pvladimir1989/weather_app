import os
from pathlib import Path
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent.parent


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASE_URL = os.environ.get('DATABASE_URL', False)
if DATABASE_URL:
    db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
    DATABASES['default'].update(db_from_env)
else:
    BACKEND_DB_ENGINE = os.getenv('BACKEND_DB_ENGINE', False)
    if BACKEND_DB_ENGINE:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.{0}'.format(BACKEND_DB_ENGINE),
                'NAME': os.getenv('BACKEND_DB_NAME'),
                'USER': os.getenv('BACKEND_DB_USER'),
                'PASSWORD': os.getenv('BACKEND_DB_PASSWORD'),
                'HOST': os.getenv('BACKEND_DB_HOST'),
                'PORT': os.getenv('BACKEND_DB_PORT'),
            },
        }
