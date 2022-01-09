from backend.base import *

ALLOWED_HOSTS = str(env('ALLOWED_HOSTS')).split(',')

for host in ALLOWED_HOSTS:
    print(f'http://{host}/{ADMIN_URL}')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=env('SECRET_KEY')

WSGI_APPLICATION = 'backend.asgi.application'
# anymail
# INSTALLED_APPS = +[
#     # ...
#     # ...
# ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('MAIL_USER')
EMAIL_HOST_PASSWORD = env('MAIL_PASS')
EMAIL_PORT = 587

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = (env('CORS_ORIGIN_WHITELIST') or '').split(',')
CORS_ALLOW_HEADERS = list(default_headers) + [
'x-retried-from',
'access-control-allow-origin'
]