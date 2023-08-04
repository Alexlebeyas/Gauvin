variable "location" {}
variable "project_name" {}

variable "ca_min_replicas" {}
variable "ca_max_replicas" {}

variable "ca_web_memory" {}
variable "ca_web_cpu" {}
variable "ca_web_image" {}

variable "ca_api_memory" {}
variable "ca_api_cpu" {}
variable "ca_api_image" {}


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
