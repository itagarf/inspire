terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.25.0"
    }
  }


  backend "s3" {
    bucket = "inspire-backend-bucket"
    key = "terraform.tfstate"
    region = "eu-west-1"
    dynamodb_table = "backend"
  }

}

provider "aws" {
  region  = "eu-west-1"
  profile = "favour-aws"
}


