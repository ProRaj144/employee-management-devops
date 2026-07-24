
# Employee Management System - DevOps CI/CD Pipeline

## Project Overview

This project demonstrates a complete DevOps CI/CD pipeline for an Employee Management System. The application consists of a React frontend, a FastAPI backend, and a MySQL database hosted on Amazon RDS. The entire deployment process is automated using Jenkins, Docker, GitHub, SonarQube, and Amazon ECR.

---

## Project Architecture

```
Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Webhook
     │
     ▼
Jenkins CI/CD Pipeline
     │
     ├── Checkout Source Code
     ├── Flake8 Code Quality Check
     ├── SonarQube Static Code Analysis
     ├── Quality Gate Validation
     ├── Pytest Unit Testing
     ├── Build Docker Images
     ├── Push Images to Amazon ECR
     ├── Deploy Containers
     └── Health Check
              │
              ▼
Docker Containers on EC2
     ├── React Frontend
     ├── FastAPI Backend
     └── Amazon RDS (MySQL)
```

---

## Technologies Used

### Cloud

- AWS EC2
- Amazon RDS
- Amazon ECR

### CI/CD

- Jenkins
- GitHub
- GitHub Webhooks

### Containers

- Docker
- Docker Compose

### Code Quality

- SonarQube
- SonarScanner
- Flake8

### Testing

- Pytest

### Backend

- Python
- FastAPI
- SQLAlchemy
- PyMySQL

### Frontend

- React
- Axios
- Nginx

---

## Features

- Employee CRUD Operations
- Automated CI/CD Pipeline
- Static Code Analysis
- Quality Gate Validation
- Unit Testing
- Dockerized Application
- Automated Deployment
- Health Monitoring
- Email Notifications
- Amazon RDS Integration

---

## CI/CD Pipeline Flow

1. Developer pushes code to GitHub.
2. GitHub Webhook triggers Jenkins automatically.
3. Jenkins checks out the latest source code.
4. Flake8 performs code quality checks.
5. SonarQube performs static code analysis.
6. Jenkins waits for the SonarQube Quality Gate.
7. Pytest executes unit tests.
8. Docker builds backend and frontend images.
9. Images are pushed to Amazon ECR.
10. Docker Compose deploys the latest containers.
11. Jenkins performs application health checks.
12. Success or failure notification is sent by email.

---

## Application URLs

### Frontend

```
http://<EC2_PUBLIC_IP>:3000
```

### Backend

```
http://<EC2_PUBLIC_IP>:8000
```

### Health Endpoint

```
http://<EC2_PUBLIC_IP>:8000/health
```

### Employees API

```
http://<EC2_PUBLIC_IP>:8000/employees/
```

---

## Project Structure

```
employee-management-devops/
│
├── backend/
├── frontend/
├── mysql/
├── docker-compose.yml
├── docker-compose.dev.yml
├── Jenkinsfile
└── README.md
```

---

## Pipeline Stages

- Checkout Source
- Code Quality (Flake8)
- SonarQube Analysis
- Quality Gate
- Unit Testing
- Build Backend
- Build Frontend
- Push Docker Images
- Deploy Development
- Health Check
- Deploy Production
- Email Notification

---

## DevOps Workflow

```
GitHub
   │
   ▼
Webhook
   │
   ▼
Jenkins
   │
   ▼
Flake8
   │
   ▼
SonarQube
   │
   ▼
Quality Gate
   │
   ▼
Pytest
   │
   ▼
Docker Build
   │
   ▼
Amazon ECR
   │
   ▼
Docker Compose
   │
   ▼
EC2
   │
   ▼
Amazon RDS
```

---

GitHub:
https://github.com/ProRaj144

LinkedIn:
https://www.linkedin.com/in/sujith-sajja-447a42254/

---

## Future Enhancements

- Kubernetes (Amazon EKS)
- Terraform Infrastructure as Code
- Prometheus Monitoring
- Grafana Dashboards
- Nginx Reverse Proxy
- HTTPS using SSL
- Blue-Green Deployment
- Rolling Updates
