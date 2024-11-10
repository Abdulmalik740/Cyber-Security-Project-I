from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

"""
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')
DEBUG = True
ALLOWED_HOSTS = []
"""

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')  # Fetch from environment variable
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'  # Fetch from environment variable (should be False in production)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'voting',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add custom template directories here, if any
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'votingsystem.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
        # For PostgreSQL or other database types, you can use environment variables
        'USER': os.getenv('DB_USER', 'default_user'),  # Get from environment variable
        'PASSWORD': os.getenv('DB_PASSWORD', 'default_password'),  # Get from environment variable
        'HOST': os.getenv('DB_HOST', 'localhost'),    # Get from environment variable
        'PORT': os.getenv('DB_PORT', '5432'),         # Get from environment variable
    }
}
STATIC_URL = '/static/'

