# Operations runbook

## Release
1. Merge a reviewed pull request to `main`.
2. Confirm the CI workflow passed: lint, unit tests, and `pip-audit`.
3. Confirm the container image was published with the commit SHA tag.
4. Update `container_image` in Terraform to the immutable SHA-tagged image.
5. Run `terraform plan` and review all changes; obtain approval before `terraform apply`.
6. Confirm the ECS service is stable and the ALB target is healthy.

## Health and monitoring
- Application health endpoint: `GET /health` (checks the database connection).
- Container health check runs every 30 seconds.
- ECS container logs are sent to CloudWatch log group `/ecs/heritage-hotel`.
- Recommended alarms: ALB 5XX count, target response time, unhealthy host count, ECS CPU/memory, and RDS CPU/storage/connections.

## Rollback
1. Identify the last known-good image SHA from the release history.
2. Set `container_image` to that immutable image.
3. Run `terraform plan`, review, then `terraform apply`.
4. Wait for ECS deployment stability and verify `/health` and a test booking.
5. Record the incident, failed SHA, rollback time, and corrective action.

## Security and recovery
- Never commit `.env`, passwords, database URLs, or cloud credentials.
- Use GitHub environment secrets / AWS Secrets Manager and least-privilege IAM in a production hardening pass.
- Enable automated RDS backups and deletion protection before production use.
- Restrict or add authentication to `GET /api/bookings` before exposing it publicly; it is intentionally a demo endpoint in this learning project.
