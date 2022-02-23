from .base import *
DEBUG = False

ALLOWED_HOSTS = str(env('ALLOWED_HOSTS')).split(',')

for host in ALLOWED_HOSTS:
    print(f'http://{host}/{ADMIN_URL}')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=env('SECRET_KEY')

WSGI_APPLICATION = 'backend.asgi.application'
INSTALLED_APPS += [
    #cloudinary
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    # ...
    # ...
    'corsheaders',
]
MIDDLEWARE +=[
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
#cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY': env('API_KEY'),
    'API_SECRET': env('API_KEY'),
    'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, 'my-manifest-directory')
}
MEDIA_URL = '/media/'  # or any prefix you choose
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# STATIC_URL  =  '/static/' 
# STATICFILES_STORAGE  =  'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('MAIL_USER')
EMAIL_HOST_PASSWORD = env('MAIL_PASS')
EMAIL_PORT = 587

CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3030',
] # If this is used, then not need to use `CORS_ALLOW_ALL_ORIGINS = True`
CORS_ALLOWED_ORIGIN_REGEXES = [
    'http://localhost:3030',
]
print()
CLOUDINARY_STORAGE = {
    # other settings, like credentials
    'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, 'my-manifest-directory')
}