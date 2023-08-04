variable "location" {}
variable "project_name" {}

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
