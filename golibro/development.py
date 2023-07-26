from .base import *


DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"  # Mailhog Container
EMAIL_PORT = "1025"

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]

INSTALLED_APPS += [
    "sslserver",
]
