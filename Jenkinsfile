pipeline {
    agent any

    environment {
        REGISTRY = "localhost:32000"
        NAMESPACE = "multi-tier-web-app"
    }

    stages {
        stage('Build and Push Docker Images') {
            steps {
                script {
                    // Use build number as image tag
                    IMAGE_TAG = "${env.BUILD_NUMBER}"

                    sh "docker build -t $REGISTRY/frontend:$IMAGE_TAG ./frontend"
                    sh "docker build -t $REGISTRY/backend:$IMAGE_TAG ./backend"
                    sh "docker push $REGISTRY/frontend:$IMAGE_TAG"
                    sh "docker push $REGISTRY/backend:$IMAGE_TAG"

                    // Update deployments with new image
                    sh "microk8s kubectl set image deployment/frontend-deployment frontend=$REGISTRY/frontend:$IMAGE_TAG -n $NAMESPACE"
                    sh "microk8s kubectl set image deployment/backend-deployment backend=$REGISTRY/backend:$IMAGE_TAG -n $NAMESPACE"
                }
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
