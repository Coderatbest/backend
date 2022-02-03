from .base import *


DEBUG=True
print(f"http://localhost:8000/{ADMIN_URL}")

ALLOWED_HOSTS = []

INSTALLED_APPS +=[
    #cloudinary
    'django.contrib.staticfiles',
    # ...
    # ...
]

WSGI_APPLICATION = 'backend.wsgi.application'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dc4t95$q3v99glye(%nh*c+a9fw_iqgucjhk$1e46cr2g4avjj'

#email Console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'