from .base import *
from .base import env

ALLOWED_HOSTS = []
PROJECT_PROTOCOL = "https://"
PROJECT_DOMAIN = ""
PROJECT_URI = "".join((PROJECT_PROTOCOL, PROJECT_DOMAIN))


DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[UAT] ",
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

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "USER": os.getenv("MSSQL_USER"),
        "PASSWORD": os.getenv("MSSQL_PASSWORD"),
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server"},
        "NAME": os.environ.get("MSSQL_DB_NAME", default="golibro"),
        "HOST": os.environ.get("MSSQL_HOST", default="mssql2017"),
        "PORT": os.environ.get("MSSQL_PORT", default="1433"),
    },
}
