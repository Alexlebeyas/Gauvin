provider "azurerm" {
  features {}
  skip_provider_registration = true
}

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.66"
    }
  }

  backend "azurerm" {
    resource_group_name  = "terraform"
    storage_account_name = "terraformstategauvin"
    container_name       = "envs"
    key                  = "terraform.tfstate"
  }
}


resource "azurerm_resource_group" "resource-group" {
  name     = "${var.project_name}-rg-${terraform.workspace}"
  location = var.location
}

resource "azurerm_key_vault" "key-vault" {
  name                     = "${var.project_name}-key-vault-${terraform.workspace}"
  location                 = azurerm_resource_group.resource-group.location
  resource_group_name      = azurerm_resource_group.resource-group.name
  tenant_id                = var.tenant_id
  sku_name                 = "standard"
  purge_protection_enabled = true
}

resource "azurerm_key_vault_access_policy" "key-vault-access-policy" {
  for_each     = { for index, policy in var.key_vault_access_policies : index => policy }
  key_vault_id = azurerm_key_vault.key-vault.id
  tenant_id    = var.tenant_id
  object_id    = each.value.object_id
  secret_permissions = [
    "Get", "Backup", "Delete", "List", "Purge", "Recover", "Restore", "Set"
  ]
}

# Key-Vault secrets -----------------------------------------------------------
# Key-vault secrets are created and maintained outside of terraform,
# and are referenced here as data resources
data "azurerm_key_vault_secret" "database-password" {
  name         = "database-password"
  key_vault_id = azurerm_key_vault.key-vault.id
}

resource "azurerm_container_registry" "acr" {
  name                = "${var.project_name}acr${terraform.workspace}" # alphanumeric characters only
  resource_group_name = azurerm_resource_group.resource-group.name
  location            = azurerm_resource_group.resource-group.location
  sku                 = var.acr_sku
  admin_enabled       = true
}

module "container-apps" {
  # Reference
  # https://registry.terraform.io/modules/Azure/container-apps/azure/latest
  # https://github.com/Azure/terraform-azure-container-apps/tree/main

  # 2023-08-04, JM
  # The Terraform Azure provider for Container App doesn't support scale rules
  # (See: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app)

  # There is an issue and open PR on Github for this
  # https://github.com/hashicorp/terraform-provider-azurerm/issues/20629
  # https://github.com/hashicorp/terraform-provider-azurerm/pull/21274

  # It's not yet clear if creating a new revision will erase any manually created scale rules.
  # We may have to set scale rules with Azure CLI in a pipeline during deploy
  # (See: https://learn.microsoft.com/en-us/cli/azure/containerapp?view=azure-cli-latest#az-containerapp-update)
  # TODO: Consider the above when writing the deploy pipeline, which calls the command to update the image to latest build number

  source                         = "Azure/container-apps/azure"
  version                        = "0.1.1"
  resource_group_name            = azurerm_resource_group.resource-group.name
  location                       = azurerm_resource_group.resource-group.location
  log_analytics_workspace_name   = "${var.project_name}-log-analytics-${terraform.workspace}"
  container_app_environment_name = "${var.project_name}-cae-${terraform.workspace}"

  container_apps = {
    web = {
      name          = "web-${terraform.workspace}"
      revision_mode = "Single"

      template = {
        min_replicas = var.ca_min_replicas
        max_replicas = var.ca_max_replicas
        containers = [
          {
            name   = "web"
            memory = var.ca_web_memory
            cpu    = var.ca_web_cpu
            image  = var.ca_web_image
          }
        ]
      }
      ingress = {
        allow_insecure_connections = false
        external_enabled           = true
        target_port                = 80
        traffic_weight = {
          latest_revision = true
          percentage      = 100
        }
      }
      registry = [
        {
          server               = azurerm_container_registry.acr.login_server
          username             = azurerm_container_registry.acr.admin_username
          password_secret_name = "acr-password"
        }
      ]
    },
    api = {
      name          = "api-${terraform.workspace}"
      revision_mode = "Single"

      template = {
        min_replicas = var.ca_min_replicas
        max_replicas = var.ca_max_replicas
        containers = [
          {
            name   = "api"
            memory = var.ca_api_memory
            cpu    = var.ca_api_cpu
            image  = var.ca_api_image
            env    = var.django_env_vars
            # command = "" # TODO: Overriding command to start the API web server
          }
        ]
      }
      ingress = {
        allow_insecure_connections = false
        external_enabled           = true
        target_port                = 80
        traffic_weight = {
          latest_revision = true
          percentage      = 100
        }
      }
      registry = [
        {
          server               = azurerm_container_registry.acr.login_server
          username             = azurerm_container_registry.acr.admin_username
          password_secret_name = "acr-password"
        }
      ]
    },
    celery_beat = {
      name          = "celery-beat-${terraform.workspace}"
      revision_mode = "Single"

      template = {
        min_replicas = 1 # apps with no ingress must have minimum 1
        max_replicas = 1 # celery beat must be a singleton
        containers = [
          {
            name   = "celery-beat"
            memory = var.ca_celery_beat_memory
            cpu    = var.ca_celery_beat_cpu
            image  = var.ca_celery_beat_image
            env    = var.django_env_vars
            # command = "" # TODO: Overriding command to start the celery beat scheduler
          }
        ]
      }
      registry = [
        {
          server               = azurerm_container_registry.acr.login_server
          username             = azurerm_container_registry.acr.admin_username
          password_secret_name = "acr-password"
        }
      ]
    },
    celery_worker = {
      name          = "celery-worker-${terraform.workspace}"
      revision_mode = "Single"

      template = {
        min_replicas = 1 # apps with no ingress must have minimum 1
        max_replicas = var.ca_max_replicas
        containers = [
          {
            name   = "celery-worker"
            memory = var.ca_celery_worker_memory
            cpu    = var.ca_celery_worker_cpu
            image  = var.ca_celery_worker_image
            env    = var.django_env_vars
            # command = "" # TODO: Overriding command to start the celery worker
          }
        ]
      }
      registry = [
        {
          server               = azurerm_container_registry.acr.login_server
          username             = azurerm_container_registry.acr.admin_username
          password_secret_name = "acr-password"
        }
      ]
    }
  }


  container_app_secrets = {
    # Secrets cannot be removed from container apps. They can only be blanked out.
    # See this issue: https://github.com/microsoft/azure-container-apps/issues/395
    # Also: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app

    web = [
      {
        name  = "acr-password"
        value = azurerm_container_registry.acr.admin_password
      }
    ]

    # api, celery_beat, celery_worker are all the same Django app, and share the same image.
    # Not sure if there's a way to avoid repeating these lists like there is for env vars, since these reference a data attribue.
    api = [
      {
        name  = "database-password"
        value = data.azurerm_key_vault_secret.database-password.value
      },
      {
        name  = "acr-password"
        value = azurerm_container_registry.acr.admin_password
      }
    ]

    celery_beat = [
      {
        name  = "database-password"
        value = data.azurerm_key_vault_secret.database-password.value
      },
      {
        name  = "acr-password"
        value = azurerm_container_registry.acr.admin_password
      }
    ]

    celery_worker = [
      {
        name  = "database-password"
        value = data.azurerm_key_vault_secret.database-password.value
      },
      {
        name  = "acr-password"
        value = azurerm_container_registry.acr.admin_password
      }
    ]
  }
}

resource "azurerm_redis_cache" "redis" {
  # For some reason it takes up to 30 minutes to create this resource on Azure. It's been like this for years.
  # See: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/redis_cache
  name                = "${var.project_name}-redis-${terraform.workspace}" # name must be globally unique
  location            = azurerm_resource_group.resource-group.location
  resource_group_name = azurerm_resource_group.resource-group.name
  enable_non_ssl_port = false
  minimum_tls_version = "1.2"
  sku_name            = var.redis_sku_name
  family              = var.redis_family
  capacity            = var.redis_capacity
}
