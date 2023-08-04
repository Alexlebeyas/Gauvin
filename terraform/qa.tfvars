ca_min_replicas = 0
ca_max_replicas = 1

ca_web_memory = "0.5Gi"
ca_web_cpu    = 0.25
ca_web_image  = "nginxdemos/hello"

ca_api_memory = "0.5Gi"
ca_api_cpu    = 0.25
ca_api_image  = "nginxdemos/hello"

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
