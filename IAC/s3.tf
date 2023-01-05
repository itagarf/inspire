resource "aws_s3_bucket" "backend" {
  bucket = "inspire-backend-bucket"
  tags = {
    Description = "Backend bucket for Inspire"
  }
}


resource "aws_s3_bucket" "inspire-static-files" {
  bucket = "inspire-static-files"
  tags = {
    Description = "Bucket for static files"
  }
}

locals {
  content_type_map = {
    html        = "text/html",
    js          = "application/javascript",
    css         = "text/css",
    svg         = "image/svg+xml",
    png         = "image/png"
  }
}


resource "aws_s3_object" "staticfiles" {
  for_each = fileset("../app/static/", "/**/*.*")
  bucket = aws_s3_bucket.inspire-static-files.id
  key = "/static/${each.value}"
  source = "../app/static/${each.value}"
  etag = filemd5("../app/static/${each.value}")
  content_type = lookup(local.content_type_map, regex("\\.(?P<extension>[A-Za-z0-9]+)$", each.value).extension, "application/octet-stream")
}


