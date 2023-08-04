from .base import *

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"  # Mailhog Container
EMAIL_PORT = "1025"

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]

INSTALLED_APPS += [
    "sslserver",
]

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
