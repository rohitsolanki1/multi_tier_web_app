pipeline {
    agent any

    environment {
        REGISTRY = "localhost:32000"
        NAMESPACE = "multi-tier-web-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm // will checkout your main branch
            }
        }

        stage('Build Docker Images') {
            steps {
                sh """
                docker build -t $REGISTRY/frontend:latest ./frontend
                docker build -t $REGISTRY/backend:latest ./backend
                docker push $REGISTRY/frontend:latest
                docker push $REGISTRY/backend:latest
                """
            }
        }

        stage('Deploy to MicroK8s') {
            steps {
                sh """
                microk8s kubectl create namespace $NAMESPACE --dry-run=client -o yaml | microk8s kubectl apply -f -
                microk8s kubectl apply -f k8s/ -n $NAMESPACE
                """
            }
        }
    }
}
