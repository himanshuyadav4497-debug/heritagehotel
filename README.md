# Heritage Hotel Booking — CI/CD & Cloud Deployment

A learning project demonstrating a hotel booking/enquiry web form and API, PostgreSQL persistence, automated quality gates, container publishing, and AWS infrastructure as code.

## Technology
- Python 3.12, Flask, SQLAlchemy
- PostgreSQL 16
- Docker multi-stage build and Docker Compose
- GitHub Actions: Ruff lint, pytest, pip-audit, image build/push to GHCR
- Terraform: AWS VPC, ALB, ECS Fargate, RDS PostgreSQL, CloudWatch

## Run locally
1. Install Docker Desktop / Docker Engine and Docker Compose.
2. Copy `.env.example` to `.env` and set a unique local password.
3. Start: `docker compose up --build`
4. Check: `curl http://localhost:5000/health`
5. Create a booking:
```bash
curl -X POST http://localhost:5000/api/bookings \
  -H 'Content-Type: application/json' \
  -d '{"guest_name":"Asha Rao","email":"asha@example.com","check_in":"2027-01-10","check_out":"2027-01-12","guests":2}'
```
6. Stop: `docker compose down`. Add `-v` only if you intend to delete the local database volume.

## Run tests locally
```bash
python -m venv .venv
# activate the environment, then:
pip install -r requirements-dev.txt
ruff check app tests run.py
pytest -q
pip-audit -r requirements.txt
```

## CI/CD
Push to `main` or open a pull request. The workflow runs lint, tests, and dependency audit. On pushes to `main`, it builds and publishes an image tagged with the commit SHA and `latest` to GitHub Container Registry.

## AWS infrastructure
See `infra/terraform`. Configure AWS credentials securely, provide `container_image` and `db_password` through a secure local mechanism, then run `terraform init`, `terraform validate`, `terraform plan`, and (only after reviewing cost/security) `terraform apply`.

**Cost warning:** AWS resources such as ALB, ECS Fargate, and RDS can incur charges while running. Destroy learning resources after evidence capture. The sample is not production-ready without HTTPS, authentication/authorization, managed secret injection, private task egress design, backups/deletion protection, and stronger observability.

## Evidence to capture before submission
- Successful `docker compose up` and `/health` response
- `pytest -q` output and Ruff / pip-audit results
- GitHub Actions green run and GHCR image SHA
- `terraform validate` / `terraform plan` output
- If deployed: AWS ECS service stable, ALB URL, RDS private endpoint (do not expose credentials)
- Monitoring dashboard / alarm screenshots
- Architecture diagram and completed runbook

Do not claim cloud deployment, zero downtime, automatic rollback, cost, or test counts unless you have actually measured and captured evidence. The Terraform ECS service uses rolling deployment health checks; a fully automated rollback policy and blue-green release are further implementation work.
