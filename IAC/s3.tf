resource "aws_s3_bucket" "backend" {
  bucket = "inspire-backend-bucket"
  tags = {
    Description = "Backend bucket for Inspire"
  }
}


