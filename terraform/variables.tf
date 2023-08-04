variable "location" {}
variable "project_name" {}

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
