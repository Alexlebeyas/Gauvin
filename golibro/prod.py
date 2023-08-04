from .base import *

ALLOWED_HOSTS = []
PROJECT_PROTOCOL = "https://"
PROJECT_DOMAIN = ""
PROJECT_URI = "".join((PROJECT_PROTOCOL, PROJECT_DOMAIN))


DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = ""
EMAIL_PORT = 587
SERVER_EMAIL = EMAIL_HOST_USER = os.environ.get("EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
DEFAULT_FROM_EMAIL = ""

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
