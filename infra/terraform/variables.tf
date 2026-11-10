variable "aws_region" { type = string, default = "ap-south-1" }
variable "project_name" { type = string, default = "heritage-hotel" }
variable "container_image" {
  type        = string
  description = "Published GHCR/ECR image URI; set to a real accessible image before apply."
}
variable "db_password" {
  type      = string
  sensitive = true
}
