from .base import *  # noqa

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"  # Mailhog Container
EMAIL_PORT = "1025"

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]

SECRET_KEY = "django-insecure-x&z31ih$!*6noe*rbt5bzjx-45-p_$oj9hkpb1y(p^k&)i$(_$"

INSTALLED_APPS += [
    "sslserver",
]
