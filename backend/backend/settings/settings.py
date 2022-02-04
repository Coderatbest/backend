"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import environ
env = environ.Env()
DEBUG = env.bool('DEBUG', default=True)
print(f'debug: {DEBUG}')
if DEBUG:
    from backend.local import *
else:
    from backend.deploy import *