django_env_vars = [
  {
    name        = "DATABASE_PASSWORD"
    secret_name = "database-password"
  },
  {
    name  = "NON_SECRET_ENV_VAR"
    value = "NotASecret"
  },
  {
    name  = "NON_SECRET_ENV_VAR_2"
    value = "AlsoNotASecret"
  },
]
