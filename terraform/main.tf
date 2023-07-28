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
