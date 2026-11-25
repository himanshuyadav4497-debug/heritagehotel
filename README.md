# Heritage Hotel — CI/CD & Cloud Deployment

A Flask-based hotel enquiry application demonstrating web development, database integration, containerization, automated testing, security auditing, and cloud deployment.

**Live Website:** https://heritagehotel.onrender.com  
**GitHub Repository:** https://github.com/himanshuyadav4497-debug/heritagehotel

## Project Overview

Heritage Hotel is a web application that allows visitors to explore a hotel welcome page and submit accommodation enquiries through a dedicated enquiry form.

The application stores enquiry details in a PostgreSQL database and provides a health-check endpoint to verify database connectivity.

The project demonstrates a CI/CD workflow using GitHub Actions and cloud hosting using Render and Neon PostgreSQL.

## Features

- Attractive hotel landing page with welcome and hotel experience sections.
- Separate accommodation enquiry form.
- Guest name, email, check-in date, check-out date, guest count and special request fields.
- Server-side validation of submitted enquiry details.
- PostgreSQL database integration using Flask-SQLAlchemy.
- Database health-check endpoint.
- Docker containerization and Docker Compose configuration.
- Automated linting, testing and dependency security auditing.
- GitHub Actions CI workflow.
- Cloud deployment on Render with Neon PostgreSQL.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Database | PostgreSQL |
| ORM | Flask-SQLAlchemy |
| Frontend | HTML, CSS, JavaScript |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Code quality | Ruff |
| Testing | Pytest |
| Security audit | pip-audit |
| Cloud hosting | Render |
| Hosted database | Neon PostgreSQL |
| Container registry | GitHub Container Registry (GHCR) |

## Application Pages and API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Heritage Hotel landing page |
| `/enquiry` | Hotel enquiry form |
| `/health` | Application and database health check |
| `/api/bookings` (POST) | Submit a new enquiry |
| `/api/bookings` (GET) | Retrieve recent enquiry records (demo endpoint) |

**Note:** Enquiries are requests, not confirmed hotel reservations.

## Run Locally on Windows

### 1. Clone the repository

```powershell
git clone https://github.com/himanshuyadav4497-debug/heritagehotel.git
cd heritagehotel
```

### 2. Install dependencies

```powershell
py -m pip install -r requirements-dev.txt
```

### 3. Initialize the database

For the default local SQLite configuration:

```powershell
py init_db.py
```

### 4. Start the application

```powershell
py run.py
```

Open the application:

- Homepage: http://localhost:5000/
- Enquiry form: http://localhost:5000/enquiry
- Health check: http://localhost:5000/health

For a PostgreSQL local setup, configure the `DATABASE_URL` environment variable before initializing the database.

### Docker alternative

Docker Desktop must be running before using Docker Compose.

```powershell
docker compose up --build
```

## Testing and Code Quality

Run the following commands from the project directory:

```powershell
py -m pytest -v
py -m ruff check app tests run.py
py -m pip_audit -r requirements.txt
```

The project has been locally verified with:

- Pytest: 4 tests passed.
- Ruff: All checks passed.
- pip-audit: No known vulnerabilities found.

These results describe the reported local test run; results may change after future code or dependency updates.

## CI/CD Pipeline

The GitHub Actions workflow automates important quality checks whenever changes are pushed to the main branch or a pull request is opened.

The pipeline includes:

1. Checking out the source code.
2. Setting up Python.
3. Installing project dependencies.
4. Running Ruff code-quality checks.
5. Running automated Pytest tests.
6. Auditing dependencies using pip-audit.
7. Building and publishing the Docker image to GitHub Container Registry on eligible pushes to the main branch.

The latest landing-page and enquiry-page update was pushed in commit `b8ed848`, and its GitHub Actions workflow completed successfully.

## Cloud Deployment

The application is hosted using:

- **Render:** Hosts the Flask web application.
- **Neon:** Provides the hosted PostgreSQL database.

Live application:

https://heritagehotel.onrender.com

The deployed application provides a hotel homepage, enquiry form and database-backed enquiry submission functionality.

Render's free service may spin down after inactivity, so the first request after a period of inactivity can take longer to load.

**Deployment scope:** The completed cloud deployment uses Render and Neon. AWS infrastructure deployment using the Terraform files in the repository has not been completed and is not claimed as a live deployment.

## Security and Limitations

- Server-side validation is implemented for enquiry submissions.
- Database exceptions are handled with transaction rollback and logging.
- Dependencies are checked using pip-audit.
- Database credentials should be stored in environment variables and never committed to GitHub.
- The GET `/api/bookings` endpoint is intended for demonstration and should be protected with authentication and authorization before production use.
- Additional production improvements include authentication, role-based access, stronger input validation, monitoring, backups and production-grade operational controls.

## Future Improvements

- Add an authenticated hotel administration dashboard.
- Protect booking records using role-based authorization.
- Add email notifications for new enquiries.
- Improve monitoring and application logging.
- Introduce automated deployment and rollback improvements.
- Add more automated integration and security tests.

## Author and Repository

**Project:** Heritage Hotel CI/CD & Cloud Deployment

**GitHub:** https://github.com/himanshuyadav4497-debug/heritagehotel

**Live Website:** https://heritagehotel.onrender.com
