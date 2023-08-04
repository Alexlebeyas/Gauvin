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

data "azurerm_client_config" "current" {}

resource "azurerm_key_vault" "key-vault" {
  name                     = "${var.project_name}-key-vault-${terraform.workspace}"
  location                 = azurerm_resource_group.resource-group.location
  resource_group_name      = azurerm_resource_group.resource-group.name
  tenant_id                = data.azurerm_client_config.current.tenant_id
  sku_name                 = "standard"
  purge_protection_enabled = true
}

resource "azurerm_key_vault_access_policy" "key-vault-access-policy-qa" {
  key_vault_id = azurerm_key_vault.key-vault.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id
  secret_permissions = [
    "Get", "Backup", "Delete", "List", "Purge", "Recover", "Restore", "Set"
  ]
}


module "container-apps-non-prod" {
  # No scale rules in this module. Is that a blocker?
  # Certificates?

  count = terraform.workspace == "prod" ? 0 : 1

  # https://registry.terraform.io/modules/Azure/container-apps/azure/latest
  # https://github.com/Azure/terraform-azure-container-apps/tree/main
  source  = "Azure/container-apps/azure"
  version = "0.1.1"
  resource_group_name                                = azurerm_resource_group.resource-group.name
  location                                           = azurerm_resource_group.resource-group.location
  log_analytics_workspace_name                       = "${var.project_name}-log-analytics-${terraform.workspace}"
  container_app_environment_name                     = "${var.project_name}-cae-${terraform.workspace}"

  container_apps = {
    nginx = {
      name          = "nginx"
      revision_mode = "Single"

      template = {
        containers = [
          {
            name   = "nginx"
            memory = "0.5Gi"
            cpu    = 0.25
            image  = "nginxdemos/hello"
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

    }
  }

  # container_app_secrets = {
  #   nginx = [
  #     {
  #       name  = "secname"
  #       value = azurerm_container_registry_token_password.pulltokenpassword.password1[0].value
  #     }
  #   ]
  # }
}


