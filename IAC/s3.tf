resource "aws_s3_bucket" "backend" {
  bucket = "inspire-backend-bucket"
  tags = {
    Description = "Backend bucket for Inspire"
  }
}


resource "aws_s3_bucket" "inspirestaticfiles" {
  bucket = "inspire-static-files"
  tags = {
    Description = "Static files for Inspire"
  }
}

resource "aws_s3_object" "css-bootstrap" {
  source = "../app/static/css/bootstrap.min.css"
  key = "/static/css/bootstrap.min.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "css-font-awesome" {
  source = "../app/static/css/font-awesome.min.css"
  key = "/static/css/font-awesome.min.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "css-helper" {
  source = "../app/static/css/helper.css"
  key = "/static/css/helper.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "css-home" {
  source = "../app/static/css/home.css"
  key = "/static/css/home.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "css-login" {
  source = "../app/static/css/login.css"
  key = "/static/css/login.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "css-owl" {
  source = "../app/static/css/owl.theme.default.min.css"
  key = "/static/css/owl.theme.default.min.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "css-sidebar" {
  source = "../app/static/css/sidebar.css"
  key = "/static/css/sidebar.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "css-style" {
  source = "../app/static/css/style.css"
  key = "/static/css/style.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "css-themify" {
  source = "../app/static/css/themify-icons.css"
  key = "/static/css/themify-icons.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}



resource "aws_s3_object" "js-bootstrap" {
  source = "../app/static/js/bootstrap.min.js"
  key = "/static/js/bootstrap.min.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "js-dashboard" {
  source = "../app/static/js/dashboard2.js"
  key = "/static/js/dashboard2.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "js-home" {
  source = "../app/static/js/home.js"
  key = "/static/js/home.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "js-jquery" {
  source = "../app/static/js/jquery.min.js"
  key = "/static/js/jquery.min.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "js-nanoscroller" {
  source = "../app/static/js/jquery.nanoscroller.min.js"
  key = "/static/js/jquery.nanoscroller.min.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "js-login" {
  source = "../app/static/js/login.js"
  key = "/static/js/login.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "js-pace" {
  source = "../app/static/js/pace.min.js"
  key = "/static/js/pace.min.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "js-script" {
  source = "../app/static/js/script.js"
  key = "/static/js/script.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "js-sidebar" {
  source = "../app/static/js/sidebar.js"
  key = "/static/js/sidebar.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}