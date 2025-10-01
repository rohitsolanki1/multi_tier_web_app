# Multi-Tier Web App CI/CD with MicroK8s (On-Prem)

![MicroK8s](https://img.shields.io/badge/Kubernetes-MicroK8s-blue) ![Docker](https://img.shields.io/badge/Docker-Container-blue) ![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red)

## Project Overview

This project demonstrates how to build, containerize, and deploy a multi-tier web application using Docker, Jenkins, and MicroK8s on an **on-prem Ubuntu server**. The frontend is a static website served via Nginx, and the backend can be a simple API or service. CI/CD automation is handled by Jenkins, ensuring seamless integration and deployment.

## Key Features

* Static Website & Backend: Frontend with Nginx, backend service optional.
* GitHub Version Control: Repository triggers automated pipeline.
* Jenkins CI/CD: Automated builds, Docker image creation, and Kubernetes deployment.
* Docker: Containerization of frontend and backend.
* MicroK8s: Local Kubernetes cluster for on-prem deployment.
* NodePort Services: Application accessible from local network.
* On-Prem Environment: Fully local deployment without cloud.

## Project Structure

```
multi-tier-app/
├── frontend/
│   ├── Dockerfile
│   ├── index.html
├── backend/
│   ├── Dockerfile
│   ├── app.py
├── k8s/
│   ├── frontend-deployment.yaml
│   ├── backend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── backend-service.yaml
├── Jenkinsfile
└── README.md
```

## Setup Steps

**1. Install MicroK8s**
Install and configure MicroK8s with DNS, dashboard, storage, and local registry:

```bash
sudo snap install microk8s --classic
sudo usermod -aG microk8s $USER
newgrp microk8s
microk8s enable dns dashboard storage registry
```

**2. Install Docker**

```bash
sudo apt install -y docker.io
sudo usermod -aG docker $USER
newgrp docker
```

**3. Jenkins Installation**

```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

Access Jenkins at `http://<ubuntu-ip>:8080`.

**4. Build & Push Docker Images**

```bash
docker build -t frontend:latest ./frontend
docker build -t backend:latest ./backend
docker tag frontend localhost:32000/frontend:latest
docker tag backend localhost:32000/backend:latest
docker push localhost:32000/frontend:latest
docker push localhost:32000/backend:latest
```

**5. Deploy on MicroK8s**

```bash
microk8s kubectl apply -f k8s/
microk8s kubectl get pods
microk8s kubectl get svc
```

* Frontend URL: `http://<ubuntu-ip>:30080`
* Backend URL: `http://<ubuntu-ip>:30081` (optional)

**6. Jenkins CI/CD Pipeline**
Use the following Jenkinsfile in your repo to automate builds and deployments:

```groovy
pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps { git 'https://github.com/<your-username>/multi-tier-app.git' }
        }
        stage('Build Docker Images') {
            steps {
                sh 'docker build -t frontend:latest ./frontend'
                sh 'docker build -t backend:latest ./backend'
                sh 'docker tag frontend localhost:32000/frontend:latest'
                sh 'docker tag backend localhost:32000/backend:latest'
                sh 'docker push localhost:32000/frontend:latest'
                sh 'docker push localhost:32000/backend:latest'
            }
        }
        stage('Deploy to MicroK8s') {
            steps { sh 'microk8s kubectl apply -f k8s/' }
        }
    }
}
```

Triggers can be set to poll GitHub every minute or use webhooks.

**7. Optional Enhancements**

* Kubernetes Dashboard: `microk8s dashboard-proxy`
* Horizontal Pod Autoscaling: `microk8s kubectl autoscale deployment frontend --cpu-percent=50 --min=2 --max=5`
* LoadBalancer with MetalLB: `microk8s enable metallb`

## Portfolio Highlights

* End-to-end CI/CD pipeline with Jenkins
* On-prem MicroK8s Kubernetes deployment
* Containerization using Docker
* Application accessible on local network
* Demonstrates full DevOps workflow without cloud dependency

## References

* GitHub Repo: `https://github.com/<your-username>/multi-tier-app`
* MicroK8s Docs: [https://microk8s.io/docs](https://microk8s.io/docs)
* Jenkins Docs: [https://www.jenkins.io/doc/](https://www.jenkins.io/doc/)

---

**Diagram**
GitHub Repo → Jenkins CI/CD → Docker Build → MicroK8s Cluster → NodePort Service → LAN Access
