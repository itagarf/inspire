resource "aws_dynamodb_table" "backend" {
  name = "backend"
  hash_key = "LockID"
  billing_mode = "PAY_PER_REQUEST"
  attribute {
    name = "LockID"
    type = "S"
  }
}
