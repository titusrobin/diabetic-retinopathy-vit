provider “azurerm” {
  features {}
}
resource “azurerm_resource_group” “rg” {
  name     = “DiabeticRetinopathyVIT_group2"
  location = “West US”
}
resource “azurerm_app_service_plan” “asp” {
  name                = “DiabeticRetinopathyVITASP2"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = “PremiumV3”
    size = “P3v3" // Plan being used
  }
  kind     = “Linux”
  reserved = true // Using Linux
}
resource “azurerm_app_service” “app” {
  name                = “DiabeticRetinopathyVIT2"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id
  site_config {
    linux_fx_version = “PYTHON|3.10”
    always_on        = true
  }
  app_settings = {
    “SCM_DO_BUILD_DURING_DEPLOYMENT” = “1”
  }
  https_only = true
}