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

  # backend "azurerm" {
  #   resource_group_name   = ""
  #   storage_account_name  = ""
  #   container_name        = ""
  #   key                   = ""
  # }
}
