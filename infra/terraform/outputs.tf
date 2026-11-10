output "application_url" { value = "http://${aws_lb.app.dns_name}" }
output "database_endpoint" { value = aws_db_instance.postgres.address }
output "ecs_cluster_name" { value = aws_ecs_cluster.main.name }
