from backend.base import *

ALLOWED_HOSTS = str(env('ALLOWED_HOSTS')).split(',')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=env('SECRET_KEY')

# anymail
INSTALLED_APPS = +[
    # ...
    "anymail",
    # ...
]
ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "<your Mailgun key>",
    "MAILGUN_SENDER_DOMAIN": env('MAILGUN_SENDER_DOMAIN'),  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL =env('DEFAULT_FROM_EMAIL') #"you@example.com"  if you don't already have this in settings
SERVER_EMAIL =env('SERVER_EMAIL')  #"your-server@example.com" ditto (default from-email for Django errors)