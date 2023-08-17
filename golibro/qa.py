from .base import *
from .base import env

ALLOWED_HOSTS = []
PROJECT_PROTOCOL = "https://"
PROJECT_DOMAIN = "api-qa.blacksea-dc7dc6b2.canadacentral.azurecontainerapps.io"
PROJECT_URI = "".join((PROJECT_PROTOCOL, PROJECT_DOMAIN))

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[QA] ",
)

# TODO: Email config in Sendgrid once there is a verified client domain. See Readme.
# EMAIL_HOST = "mailhog"  # Mailhog Container
# EMAIL_PORT = "1025"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
