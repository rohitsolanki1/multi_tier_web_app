pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/rohitsolanki1/multi-tier-app.git'
            }
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
            steps {
                sh 'microk8s kubectl apply -f k8s/'
            }
        }
    }
}
