resource "aws_s3_bucket" "backend" {
  bucket = "inspire-backend-bucket"
  tags = {
    Description = "Backend bucket for Inspire"
  }
}



resource "aws_s3_bucket" "inspire-static-buckt" {
  bucket = "inspire-static-buckt"
    lifecycle {
    ignore_changes = [
      grant
    ]
  }
  tags = {
    Description = "Static files for Inspire"
  }
}

resource "aws_s3_bucket_policy" "inspire-bucket-policy" {
  bucket = aws_s3_bucket.inspire-static-buckt.id
  policy = file("s3_iam.json")
}

resource "aws_s3_bucket_acl" "bucket_acl" {
  bucket = aws_s3_bucket.inspire-static-buckt.id
  acl    = "public-read"
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
  bucket = aws_s3_bucket.inspire-static-buckt.id
  key = "/static/${each.value}"
  source = "../app/static/${each.value}"
  etag = filemd5("../app/static/${each.value}")
  content_type = lookup(local.content_type_map, regex("\\.(?P<extension>[A-Za-z0-9]+)$", each.value).extension, "application/octet-stream")
}



resource "aws_s3_bucket" "inspirestaticfiles" {
  bucket = "inspire-static-files"
  tags = {
    Description = "Bucket for static files"
  }
}

resource "aws_s3_object" "css-bootstrap" {
  source = "../app/static/css/bootstrap.min.css"
  key = "/static/css/bootstrap.min.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}
resource "aws_s3_object" "css-font-awesome" {
  source = "../app/static/css/font-awesome.min.css"
  key = "/static/css/font-awesome.min.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}
resource "aws_s3_object" "css-helper" {
  source = "../app/static/css/helper.css"
  key = "/static/css/helper.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}
resource "aws_s3_object" "css-home" {
  source = "../app/static/css/home.css"
  key = "/static/css/home.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}
resource "aws_s3_object" "css-login" {
  source = "../app/static/css/login.css"
  key = "/static/css/login.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}
resource "aws_s3_object" "css-owl" {
  source = "../app/static/css/owl.theme.default.min.css"
  key = "/static/css/owl.theme.default.min.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}
resource "aws_s3_object" "css-sidebar" {
  source = "../app/static/css/sidebar.css"
  key = "/static/css/sidebar.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}
resource "aws_s3_object" "css-style" {
  source = "../app/static/css/style.css"
  key = "/static/css/style.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}
resource "aws_s3_object" "css-themify" {
  source = "../app/static/css/themify-icons.css"
  key = "/static/css/themify-icons.css"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "text/css"
}



resource "aws_s3_object" "js-bootstrap" {
  source = "../app/static/js/bootstrap.min.js"
  key = "/static/js/bootstrap.min.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}
resource "aws_s3_object" "js-dashboard" {
  source = "../app/static/js/dashboard2.js"
  key = "/static/js/dashboard2.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}
resource "aws_s3_object" "js-home" {
  source = "../app/static/js/home.js"
  key = "/static/js/home.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}
resource "aws_s3_object" "js-jquery" {
  source = "../app/static/js/jquery.min.js"
  key = "/static/js/jquery.min.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}
resource "aws_s3_object" "js-nanoscroller" {
  source = "../app/static/js/jquery.nanoscroller.min.js"
  key = "/static/js/jquery.nanoscroller.min.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}
resource "aws_s3_object" "js-login" {
  source = "../app/static/js/login.js"
  key = "/static/js/login.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}
resource "aws_s3_object" "js-pace" {
  source = "../app/static/js/pace.min.js"
  key = "/static/js/pace.min.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}
resource "aws_s3_object" "js-script" {
  source = "../app/static/js/script.js"
  key = "/static/js/script.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}
resource "aws_s3_object" "js-sidebar" {
  source = "../app/static/js/sidebar.js"
  key = "/static/js/sidebar.js"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "application/javascript"
}



resource "aws_s3_object" "img1" {
  source = "../app/static/imgs/logodark.svg"
  key = "/static/imgs/logodark.svg"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/svg+xml"
}
resource "aws_s3_object" "img2" {
  source = "../app/static/imgs/home.png"
  key = "/static/imgs/home.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img3" {
  source = "../app/static/imgs/jonathanadler-furniture.png"
  key = "/static/imgs/jonathanadler-furniture.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img4" {
  source = "../app/static/imgs/horchow-decor.png"
  key = "/static/imgs/horchow-decor.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img5" {
  source = "../app/static/imgs/coyuchi-bed.png"
  key = "/static/imgs/coyuchi-bed.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img6" {
  source = "../app/static/imgs/society6-bath.png"
  key = "/static/imgs/society6-bath.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img7" {
  source = "../app/static/imgs/jonathanadle2-art.png"
  key = "/static/imgs/jonathanadle2-art.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img8" {
  source = "../app/static/imgs/Hung Jae In.png"
  key = "/static/imgs/Hung Jae In.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img9" {
  source = "../app/static/imgs/favour Itagar.png"
  key = "/static/imgs/favour Itagar.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img10" {
  source = "../app/static/imgs/Cole.png"
  key = "/static/imgs/Cole.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/png"
}
resource "aws_s3_object" "img11" {
  source = "../app/static/imgs/Rocky.png"
  key = "/static/imgs/Rocky.png"
  bucket = aws_s3_bucket.inspirestaticfiles.id
}
resource "aws_s3_object" "img12" {
  source = "../app/static/imgs/social-icons.svg"
  key = "/static/imgs/social-icons.svg"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/svg+xml"
}
resource "aws_s3_object" "img13" {
  source = "../app/static/imgs/icon-hamburger.svg"
  key = "/static/imgs/icon-hamburger.svg"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/svg+xml"
}
resource "aws_s3_object" "img14" {
  source = "../app/static/imgs/icon-close.svg"
  key = "/static/imgs/icon-close.svg"
  bucket = aws_s3_bucket.inspirestaticfiles.id
  content_type = "image/svg+xml"
}


