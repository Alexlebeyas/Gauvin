provider "azurerm" {
  features {}
}

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.66"
    }
  }

  backend "azurerm" {
    resource_group_name  = "terraform-state-testing"
    storage_account_name = "terraformojayxkjtim"
    container_name       = "envs"
    key                  = "terraform.tfstate"
  }
}


resource "azurerm_resource_group" "resource-group" {
  name     = "gauvin-${terraform.workspace}"
  location = var.location
}

resource "azurerm_log_analytics_workspace" "log-analytics-workspace" {
  name                = "log-analytics-workspace-${terraform.workspace}"
  location            = azurerm_resource_group.resource-group.location
  resource_group_name = azurerm_resource_group.resource-group.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_container_app_environment" "container-app-environment" {
  name                       = "container-app-environment-${terraform.workspace}"
  location                   = azurerm_resource_group.resource-group.location
  resource_group_name        = azurerm_resource_group.resource-group.name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.log-analytics-workspace.id
}

data "azurerm_client_config" "current" {}

# ----- # QA Container App ----------------------------------------------------
# resource "azurerm_key_vault" "key-vault-qa" {
#   count                    = terraform.workspace == "non-prod" ? 1 : 0
#   name                     = "key-vault-qa"
#   location                 = azurerm_resource_group.resource-group.location
#   resource_group_name      = azurerm_resource_group.resource-group.name
#   tenant_id                = data.azurerm_client_config.current.tenant_id
#   sku_name                 = "standard"
#   purge_protection_enabled = true
# }

# resource "azurerm_key_vault_access_policy" "key-vault-access-policy-qa" {
#   count        = terraform.workspace == "non-prod" ? 1 : 0
#   key_vault_id = azurerm_key_vault.key-vault-qa[0].id
#   tenant_id    = data.azurerm_client_config.current.tenant_id
#   object_id    = data.azurerm_client_config.current.object_id
#   secret_permissions = [
#     "Get", "Backup", "Delete", "List", "Purge", "Recover", "Restore", "Set"
#   ]
# }

resource "azurerm_container_app" "qa" {
  count                        = terraform.workspace == "non-prod" ? 1 : 0
  name                         = "container-app-qa"
  container_app_environment_id = azurerm_container_app_environment.container-app-environment.id
  resource_group_name          = azurerm_resource_group.resource-group.name
  revision_mode                = "Single"

  template {
    min_replicas = 1
    max_replicas = 1

    container {
      name   = "container-app-qa"
      image  = "nginxdemos/hello:latest"
      cpu    = 0.25
      memory = "0.5Gi"
    }
  }

  ingress {
    allow_insecure_connections = false
    external_enabled           = true
    target_port                = 80
    traffic_weight {
      percentage = 100
    }
  }
}


