# !!! DO NOT CHECK SECRET VALUES (passwords, API keys, etc.) INTO THIS FILE !!!
# See the README for handling secret values

variable "location" {}
variable "project_name" {}

variable "acr_sku" { default = "Basic" }

# Default values are meant for placeholders in non-prod environments, and should be overriden where necessary
variable "ca_min_replicas" { default = 0 }
variable "ca_max_replicas" { default = 1 }

variable "ca_web_memory" { default = "0.5Gi" }
variable "ca_web_cpu" { default = 0.25 }
variable "ca_web_image" { default = "nginxdemos/hello" }

variable "ca_api_memory" { default = "0.5Gi" }
variable "ca_api_cpu" { default = 0.25 }
variable "ca_api_image" { default = "nginxdemos/hello" }

variable "ca_celery_beat_memory" { default = "0.5Gi" }
variable "ca_celery_beat_cpu" { default = 0.25 }
variable "ca_celery_beat_image" { default = "nginxdemos/hello" }

variable "ca_celery_worker_memory" { default = "0.5Gi" }
variable "ca_celery_worker_cpu" { default = 0.25 }
variable "ca_celery_worker_image" { default = "nginxdemos/hello" }

variable "redis_sku_name" { default = "Basic" }
variable "redis_family" { default = "C" }
variable "redis_capacity" { default = "0" }

variable "tenant_id" { default = "cc7729dc-3c18-40f5-a43e-addf722fa974" }

variable "key_vault_access_policies" {
  description = "Azure active directory object IDs having access to the environment key vault"

  type = list(map(any))
  default = [
    {
      key1 = "value1"
      key2 = "value2"
    }
  ]
}

variable "django_env_vars" {
  description = "Common shared environment variables used in Django apps"

  type = list(map(any))
  default = [
    {
      key1 = "value1"
      key2 = "value2"
    }
  ]
}

