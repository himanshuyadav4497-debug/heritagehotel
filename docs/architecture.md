# Architecture

```mermaid
flowchart TD
  U[Guest browser] --> ALB[Application Load Balancer]
  ALB --> ECS[ECS Fargate Flask container]
  ECS --> RDS[(Private PostgreSQL RDS)]
  ECS --> CW[CloudWatch Logs]
  GH[GitHub Actions] --> TEST[Lint, tests, pip-audit]
  TEST --> REG[GitHub Container Registry]
  REG --> ECS
  TF[Terraform] --> VPC[VPC, subnets, security groups]
  TF --> ALB
  TF --> ECS
  TF --> RDS
```

The guest submits a booking enquiry to the Flask API. The API validates dates, guest count, and email before writing to PostgreSQL. The application is containerized; GitHub Actions runs quality gates before publishing a commit-tagged image. Terraform defines the AWS network, load balancer, ECS service, database, IAM execution role, and CloudWatch log group.
