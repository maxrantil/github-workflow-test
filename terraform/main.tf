# Simple Terraform configuration for testing validation workflow

terraform {
  required_version = ">= 1.0"
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

resource "random_string" "test" {
  length  = 16
  special = false
}

output "random_value" {
  value = random_string.test.result
}
