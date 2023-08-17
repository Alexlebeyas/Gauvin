ca_web_image           = "gauvinacrqa.azurecr.io/golibro-web:latest"
ca_api_image           = "gauvinacrqa.azurecr.io/golibro-api:latest"
ca_celery_beat_image   = "gauvinacrqa.azurecr.io/golibro-api:latest"
ca_celery_worker_image = "gauvinacrqa.azurecr.io/golibro-api:latest"

django_env_vars = [
  {
    name        = "DATABASE_PASSWORD"
    secret_name = "database-password"
  },
  {
    name  = "DJANGO_SETTINGS_MODULE"
    value = "golibro.qa"
  },
]
