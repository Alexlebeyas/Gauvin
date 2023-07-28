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

# QA Container App ------------------------------------------------------------
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
      image  = "mcr.microsoft.com/azuredocs/containerapps-helloworld:latest"
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


